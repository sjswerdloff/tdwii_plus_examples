import logging
import os
import shutil
import signal
import tempfile
import unittest
from logging import StreamHandler
from subprocess import TimeoutExpired

import psutil

from tdwii_plus_examples.tests.utils.generate_sop_instances import generate_ups
from tdwii_plus_examples.tests.utils.utils import get_configured_logger, start_scp
from tdwii_plus_examples.upspullcfindscu import UPSPullCFindSCU
from tdwii_plus_examples.upspushncreatescu import UPSPushNCreateSCU


class TestUPSPullCFindSCUIntegration(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Set up the logger for the SCU to DEBUG level with a stream handler
        cls.scu_logger, cls.stream_handler = get_configured_logger(
            "upspullnsetscu", level=logging.INFO, handler_class=StreamHandler
        )

        # Set up the logger for this test to DEBUG level
        cls.test_logger, cls.stream_handler = get_configured_logger("test_upspullcfindscu", level=logging.DEBUG)

        # Create a temporary directory for UPSSCP staging area
        cls.temp_dir = tempfile.mkdtemp()
        cls.test_logger.info(f"{cls.temp_dir} directory created")

        # Start the UPS SCP Server (replace with your actual SCP command)
        command = [
            "./tdwii_plus_examples/cli/upsscp/upsscp.py",
            "-d",
            "--database-location",
            f"{cls.temp_dir}/test.sqlite",
            "--instance-location",
            cls.temp_dir,
        ]

        cls.upsscp_started, cls.process, cls.stdout_thread, cls.stdout_lines = start_scp(command, cls.test_logger)
        cls.test_logger.info(f"Started process with PID: {cls.process.pid}")

        if not cls.upsscp_started:
            raise RuntimeError("upsscp server failed to start.")

        # Create the UPSPullCFindSCU instance
        cls.scu = UPSPullCFindSCU(
            calling_ae_title="UPSPULLSCU",
            called_ae_title="UPSSCP",
            called_ip="localhost",
            called_port=11114,
            logger=cls.scu_logger,
        )

        # Create 2 UPS in the SCP
        ups_instances = []
        ups_instances.extend(generate_ups() for _ in range(2))
        push_scu = UPSPushNCreateSCU(
            calling_ae_title="UPSPUSHSCU",
            called_ae_title="UPSSCP",
            called_ip="localhost",
            called_port=11114,
            logger=cls.scu_logger,
        )
        num_created_instances = push_scu.create_ups_instances(ups_instances)

        if num_created_instances != 2:
            cls.tearDownClass()
            cls.fail("Failed to create UPS instances.")

        # Store the SOPInstanceUIDs and machine names of all created instances in lists
        cls.sop_instance_uids = [ds.SOPInstanceUID for ds in ups_instances]
        cls.machine_names = [ds.ScheduledStationNameCodeSequence[0].CodeValue for ds in ups_instances]

    @classmethod
    def tearDownClass(cls):
        # Try to gracefully terminate the process.
        cls.test_logger.info(f"Terminating process with PID: {cls.process.pid}")
        try:
            cls.process.terminate()
            cls.process.wait(timeout=1)
            cls.test_logger.info("Process terminated gracefully.")
        except (ChildProcessError, TimeoutExpired):
            cls.test_logger.warning("Process termination timed out or process already finished.")

        # Try to kill child processes.
        try:
            parent = psutil.Process(cls.process.pid)
            for child in parent.children(recursive=True):
                child.kill()
            cls.test_logger.info("Child processes terminated.")
        except psutil.NoSuchProcess:
            cls.test_logger.warning("Error killing subprocesses. Parent process not found. Probably already terminated.")

        # Try to forcefully kill the process.
        try:
            os.kill(cls.process.pid, signal.SIGKILL)
            cls.process.wait(timeout=1)  # Ensure process termination
            cls.test_logger.info("Process forcefully terminated.")
        except OSError:
            cls.test_logger.warning("Error killing process. Probably already terminated.")

        finally:
            # Ensure the stdout thread has finished
            if cls.stdout_thread:
                cls.stdout_thread.join(timeout=1.0)

        # Print the SCP server output
        if hasattr(cls, "stdout_lines"):
            print(
                "\n"
                + "*" * 80
                + "\n*** BEGIN SCP SERVER OUTPUT ***\n"
                + "\n".join(cls.stdout_lines)
                + "\n*** END SCP SERVER OUTPUT ***\n"
                + "*" * 80
                + "\n"
            )

        # Remove the temporary directory and its contents
        files_in_temp_dir = os.listdir(cls.temp_dir)
        shutil.rmtree(cls.temp_dir)
        cls.test_logger.info(f"Removed the temp directory: {cls.temp_dir} and its contents: {files_in_temp_dir}")

        # Remove and close the handlers for scu and test loggers
        for logger, handler in [(cls.scu_logger, cls.stream_handler), (cls.test_logger, cls.stream_handler)]:
            logger.removeHandler(handler)
            handler.close()

    def test_find_ups_by_uid(self):
        """Integration test: find a UPS by SOPInstanceUID."""
        scu = UPSPullCFindSCU(
            calling_ae_title="UPSPUSHSCU",
            called_ae_title="UPSSCP",
            called_ip="localhost",
            called_port=11114,
            logger=self.scu_logger,
        )
        ds_query = scu.create_ups_query(
            ups_uid=self.sop_instance_uids[0],
            machine_name="",
            procedure_step_state="",
        )
        ups_responses = scu.get_ups(ds_query)
        self.assertTrue(any(ds.SOPInstanceUID == self.sop_instance_uids[0] for ds in ups_responses))

    def test_find_ups_by_machine(self):
        """Integration test: find UPS by machine name and check all created instances are found."""
        scu = UPSPullCFindSCU(
            calling_ae_title="UPSPUSHSCU",
            called_ae_title="UPSSCP",
            called_ip="localhost",
            called_port=11114,
            logger=self.scu_logger,
        )
        ds_query = scu.create_ups_query(
            ups_uid="",
            machine_name=self.machine_names[0],
            procedure_step_state="SCHEDULED",
        )
        ups_responses = scu.get_ups(ds_query)
        # Assert that there are 2 UPS in the response
        self.assertEqual(len(ups_responses), 2)
        # Assert that their SOPInstanceUIDs match the ones we created (order-independent)
        response_uids = sorted(ds.SOPInstanceUID for ds in ups_responses)
        created_uids = sorted(self.sop_instance_uids)
        self.assertEqual(response_uids, created_uids)


if __name__ == "__main__":
    unittest.main()
