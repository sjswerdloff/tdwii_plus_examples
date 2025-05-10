import logging
import os
import shutil
import signal
import tempfile
import unittest
from logging.handlers import MemoryHandler
from subprocess import TimeoutExpired

import psutil

from tdwii_plus_examples.tests.utils.generate_sop_instances import generate_ups
from tdwii_plus_examples.tests.utils.utils import get_configured_logger, start_scp
from tdwii_plus_examples.upspullnactionscu import UPSPullNActionSCU
from tdwii_plus_examples.upspushncreatescu import UPSPushNCreateSCU


class TestUPSPullNActionSCUIntegration(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Set up the logger for the UPSPullNActionSCU to DEBUG level
        # with a memory handler to store up to 100 log messages
        cls.scu_logger, cls.memory_handler = get_configured_logger(
            "upspullnactionscu", level=logging.DEBUG, handler_class=MemoryHandler, capacity=100
        )

        # Set up the logger for this test to DEBUG level
        cls.test_logger, cls.stream_handler = get_configured_logger("test_upspullnactionscu", level=logging.DEBUG)

        # Create a temporary directory for UPSSCP staging area
        cls.temp_dir = tempfile.mkdtemp()
        cls.test_logger.info(f"{cls.temp_dir} directory created")

        # Start the UPS SCP Server (replace with your actual SCP command)
        command = [
            "./tdwii_plus_examples/cli/upsscp/upsscp.py",
            "-v",
            "--database-location",
            f"{cls.temp_dir}/test.sqlite",
            "--instance-location",
            cls.temp_dir,
        ]

        cls.upsscp_started, cls.process, cls.stdout_thread, cls.stdout_lines = start_scp(command, cls.test_logger)
        cls.test_logger.info(f"Started process with PID: {cls.process.pid}")

        # Create the UPSPullNActionSCU instance
        cls.scu = UPSPullNActionSCU(
            calling_ae_title="UPSPULLSCU",
            called_ae_title="ANYSCP",
            called_ip="localhost",
            called_port=11114,
            logger=cls.scu_logger,
        )

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

        # Remove and close the memory handler for scu and test loggers
        for logger, handler in [(cls.scu_logger, cls.memory_handler), (cls.test_logger, cls.stream_handler)]:
            logger.removeHandler(handler)
            handler.close()

    def test_claim_and_complete_ups(self):
        """Integration test for claiming and completing a UPS instance."""

        if not self.upsscp_started:
            self.fail("upsscp server failed to start.")
            return

        # Create a UPS in the SCP
        ups_instance = generate_ups()
        scu = UPSPushNCreateSCU(
            calling_ae_title="UPSPUSH",
            called_ae_title="UPSSCP",
            called_ip="localhost",
            called_port=11114,
            logger=self.scu_logger,
        )
        num_created_instances = scu.create_ups_instances([ups_instance])

        if num_created_instances != 1:
            self.fail("failed to create UPS.")
            return

        sop_instance_uid = ups_instance.SOPInstanceUID

        # Try to claim the UPS
        transaction_uid = self.scu.claim_ups(sop_instance_uid)
        self.assertIsNotNone(transaction_uid)
        self.test_logger.info(f"Claimed UPS with transaction UID: {transaction_uid}")

        # Try to complete the UPS if it was claimed
        if transaction_uid:
            result = self.scu.complete_ups(sop_instance_uid, transaction_uid)
            self.assertTrue(result)
            self.test_logger.info("Completed UPS successfully.")

    def test_claim_and_cancel_ups(self):
        """Integration test for claiming and completing a UPS instance."""

        if not self.upsscp_started:
            self.fail("upsscp server failed to start.")
            return

        # Create a UPS in the SCP
        ups_instance = generate_ups()
        scu = UPSPushNCreateSCU(
            calling_ae_title="UPSPUSH",
            called_ae_title="UPSSCP",
            called_ip="localhost",
            called_port=11114,
            logger=self.scu_logger,
        )
        num_created_instances = scu.create_ups_instances([ups_instance])

        if num_created_instances != 1:
            self.fail("failed to create UPS.")
            return

        sop_instance_uid = ups_instance.SOPInstanceUID

        # Try to claim the UPS
        transaction_uid = self.scu.claim_ups(sop_instance_uid)
        self.assertIsNotNone(transaction_uid)
        self.test_logger.info(f"Claimed UPS with transaction UID: {transaction_uid}")

        # Try to complete the UPS if it was claimed
        if transaction_uid:
            result = self.scu.cancel_ups(sop_instance_uid, transaction_uid)
            self.assertTrue(result)
            self.test_logger.info("Canceled UPS successfully.")


if __name__ == "__main__":
    unittest.main()
