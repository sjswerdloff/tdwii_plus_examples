import logging
import os
import shutil
import signal
import tempfile
import unittest
from logging.handlers import MemoryHandler
from subprocess import TimeoutExpired

import psutil
from parameterized import parameterized
from pydicom.uid import ExplicitVRLittleEndian
from pynetdicom.presentation import build_context
from pynetdicom.sop_class import _STORAGE_CLASSES

from tdwii_plus_examples.cstorescu import CStoreSCU
from tdwii_plus_examples.tests.utils.generate_sop_instances import generate_sc_images
from tdwii_plus_examples.tests.utils.utils import get_configured_logger, start_scp


class TestCStoreSCU(unittest.TestCase):
    def setUp(self):
        # Set up the logger for the CStoreSCU to INFO level
        # with a memory handler to store up to 100 log messages
        self.scu_logger, self.memory_handler = get_configured_logger(
            "cstorescu", level=logging.DEBUG, handler_class=MemoryHandler, capacity=100
        )

        # Set up the logger for this test to INFO level
        # with a stream handler to print the log messages to the console
        self.test_logger, self.stream_handler = get_configured_logger("test_cstorescu", level=logging.DEBUG)

        # Create 3 10x10 SC Image instances for testing
        self.sc_images = generate_sc_images(3, 10, 10)

        # Create a temporary directory
        self.temp_dir = tempfile.mkdtemp()
        self.test_logger.info(f"{self.temp_dir} directory created")

        # Create a UPSPushNCreateSCU instance
        required_contexts = [
            build_context(sop_class_uid, ExplicitVRLittleEndian)
            for sop_class_uid in [
                _STORAGE_CLASSES["SecondaryCaptureImageStorage"],
                _STORAGE_CLASSES["CTImageStorage"],
            ]
        ]
        self.cstore_scu = CStoreSCU(
            calling_ae_title="STORESCU",
            called_ae_title="ANYSCP",
            called_ip="localhost",
            called_port=11112,
            contexts=required_contexts,
            logger=self.scu_logger,
        )

    def tearDown(self):
        # Remove the temporary directory and its contents
        files_in_temp_dir = os.listdir(self.temp_dir)
        shutil.rmtree(self.temp_dir)
        self.test_logger.info(f"Removed the temp directory: {self.temp_dir} and its contents: {files_in_temp_dir}")

        # Try to gracefully terminate the process.
        self.test_logger.info(f"Terminating process with PID: {self.process.pid}")
        try:
            self.process.terminate()
            self.process.wait(timeout=1)
            self.test_logger.info("Process terminated gracefully.")
        except (ChildProcessError, TimeoutExpired):
            self.test_logger.warning("Process termination timed out or process already finished.")

        # Try to kill child processes.
        try:
            parent = psutil.Process(self.process.pid)
            for child in parent.children(recursive=True):
                child.kill()
            self.test_logger.info("Child processes terminated.")
        except psutil.NoSuchProcess:
            self.test_logger.warning("Error killing subprocesses. Parent process not found. Probably already terminated.")

        # Try to forcefully kill the process.
        try:
            os.kill(self.process.pid, signal.SIGKILL)
            self.process.wait(timeout=1)  # Ensure process termination
            self.test_logger.info("Process forcefully terminated.")
        except OSError:
            self.test_logger.warning("Error killing process. Probably already terminated.")

        finally:
            # Ensure the stdout thread has finished
            if self.stdout_thread:
                self.stdout_thread.join(timeout=1.0)

        # Remove and close the memory handler for scu and test loggers
        for logger, handler in [(self.scu_logger, self.memory_handler), (self.test_logger, self.stream_handler)]:
            logger.removeHandler(handler)
            handler.close()

    @parameterized.expand(
        [
            ("all_contexts_accepted", "SecondaryCaptureImageStorage,CTImageStorage", 3),
            ("some_contexts_rejected", "CTImageStorage", 0),
        ]
    )
    def test_verif_storage(self, name, supported_contexts, expected_success_count):
        # sourcery skip: merge-list-append
        """Test the Verification and Storage SOP Classes."""

        # Start the Storage SCP Server
        command = ["./tdwii_plus_examples/cli/storescp.py", "-v", "-o", self.temp_dir]
        command.append("-s")
        command.extend(supported_contexts.split(","))

        self.storescp_started, self.process, self.stdout_thread = start_scp(command, self.test_logger)
        self.test_logger.info(f"Started process with PID: {self.process.pid}")

        if not self.storescp_started:
            self.fail("storescp server failed to start.")
            return

        # Test Verification SOP Class
        self.assertEqual(self.cstore_scu.verify().status_category, "Success")

        # Test Secondary Capture Storage SOP Class
        try:
            success_count = self.cstore_scu.store_instances(self.sc_images)

            log_messages = [record.getMessage() for record in self.memory_handler.buffer]
            self.test_logger.info("Log messages: %s", log_messages)

            self.assertEqual(success_count, expected_success_count)

        except Exception as e:
            self.test_logger.error(e)
            raise


if __name__ == "__main__":
    unittest.main()
