import logging
import os
import shutil
import signal
import tempfile
import unittest
from logging.handlers import MemoryHandler
from subprocess import TimeoutExpired

import psutil
from pydicom import Dataset
from pynetdicom.sop_class import UnifiedProcedureStepPush

from tdwii_plus_examples.tests.utils.generate_sop_instances import generate_ups
from tdwii_plus_examples.tests.utils.utils import get_configured_logger, start_scp
from tdwii_plus_examples.upspullnactionscu import UPSPullNActionSCU
from tdwii_plus_examples.upspullnsetscu import UPSPullNSetSCU
from tdwii_plus_examples.upspushncreatescu import UPSPushNCreateSCU


class TestUPSPullNSetSCUIntegration(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Set up the logger for the SCU to DEBUG level with a memory handler
        cls.scu_logger, cls.memory_handler = get_configured_logger(
            "upspullnsetscu", level=logging.DEBUG, handler_class=MemoryHandler, capacity=100
        )

        # Set up the logger for this test to DEBUG level
        cls.test_logger, cls.stream_handler = get_configured_logger("test_upspullnsetscu", level=logging.DEBUG)

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

        cls.upsscp_started, cls.process, cls.stdout_thread = start_scp(command, cls.test_logger)
        cls.test_logger.info(f"Started process with PID: {cls.process.pid}")

        # Create the UPSPullNSetSCU instance
        cls.scu = UPSPullNSetSCU(
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

        # Remove the temporary directory and its contents
        files_in_temp_dir = os.listdir(cls.temp_dir)
        shutil.rmtree(cls.temp_dir)
        cls.test_logger.info(f"Removed the temp directory: {cls.temp_dir} and its contents: {files_in_temp_dir}")

        # Remove and close the memory handler for scu and test loggers
        for logger, handler in [(cls.scu_logger, cls.memory_handler), (cls.test_logger, cls.stream_handler)]:
            logger.removeHandler(handler)
            handler.close()

    def test_modify_ups_integration(self):
        """Integration test for modifying a UPS instance using N-SET."""

        if not self.upsscp_started:
            self.fail("upsscp server failed to start.")
            return

        # Create a UPS in the SCP
        ups_instance = generate_ups()
        push_scu = UPSPushNCreateSCU(
            calling_ae_title="UPSPUSH",
            called_ae_title="UPSSCP",
            called_ip="localhost",
            called_port=11114,
            logger=self.scu_logger,
        )
        num_created_instances = push_scu.create_ups_instances([ups_instance])

        if num_created_instances != 1:
            self.fail("failed to create UPS.")
            return

        sop_instance_uid = ups_instance.SOPInstanceUID

        change_state_scu = UPSPullNActionSCU(
            calling_ae_title="UPSPULL",
            called_ae_title="UPSSCP",
            called_ip="localhost",
            called_port=11114,
            logger=self.scu_logger,
        )
        tx_uid = change_state_scu.claim_ups(sop_instance_uid)

        if not tx_uid:
            self.fail("failed to claim UPS.")
            return

        # Create the modification list dataset
        modification_list = Dataset()
        modification_list.AffectedSOPInstanceUID = sop_instance_uid
        modification_list.AffectedSOPClassUID = UnifiedProcedureStepPush
        modification_list.TransactionUID = tx_uid
        # Create the sequence item
        sequence_item = Dataset()
        sequence_item.ProcedureStepProgress = "10"
        # Add the sequence item to the sequence
        modification_list.ProcedureStepProgressInformationSequence = [sequence_item]

        # Try to modify the UPS
        result = self.scu.modify_ups(sop_instance_uid, modification_list)

        # Print the SCP server output
        if hasattr(self.__class__, "stdout_thread") and getattr(self.__class__.stdout_thread, "output", None):
            print("SCP server output:\n", self.__class__.stdout_thread.output)

        # Get the log messages
        log_messages = [record.getMessage() for record in self.memory_handler.buffer]
        self.test_logger.info("Log messages: %s", log_messages)

        self.assertEqual(result.status_category, "Success")
        self.test_logger.info("Modified UPS successfully.")
