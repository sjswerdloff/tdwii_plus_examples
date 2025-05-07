import logging
import os
import signal
import unittest
from logging.handlers import MemoryHandler
from subprocess import TimeoutExpired

import psutil

from tdwii_plus_examples.tests.utils.generate_sop_instances import generate_ups
from tdwii_plus_examples.tests.utils.utils import get_configured_logger, start_scp
from tdwii_plus_examples.upspushncreatescu import UPSPushNCreateSCU


class TestUPSPushNCreateSCU(unittest.TestCase):
    def setUp(self):
        # Set up the logger for the UPSPushNCreateSCU to INFO level
        # with a memory handler to store up to 100 log messages
        self.scu_logger, self.memory_handler = get_configured_logger(
            "upspushscu", level=logging.DEBUG, handler_class=MemoryHandler, capacity=100
        )

        # Set up the logger for this test to INFO level
        # with a stream handler to print the log messages to the console
        self.test_logger, self.stream_handler = get_configured_logger("test_upspushscu", level=logging.DEBUG)

        # Create a UPSPushNCreateSCU instance
        self.upspush_ncreate_scu = UPSPushNCreateSCU(
            calling_ae_title="UPSPUSH",
            called_ae_title="UPSSCP",
            called_ip="localhost",
            called_port=11114,
            logger=self.scu_logger,
        )

        # Create a UPS instance for testing
        self.ups_instance = generate_ups()

    def tearDown(self):
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

    def test_verif_create(self):
        # Start the UPS Push SCP CLI App upsscp.py
        command = ["tdwii_plus_examples/cli/upsscp/upsscp.py", "-v"]

        self.upsscp_started, self.process, self.stdout_thread = start_scp(command, self.test_logger)
        self.test_logger.info(f"Started process with PID: {self.process.pid}")

        if not self.upsscp_started:
            self.fail("storescp server failed to start.")
            return

        # Check that the SCP is running
        self.assertEqual(self.upspush_ncreate_scu.verify().status_category, "Success")

        # Run the test case
        try:
            success_count = self.upspush_ncreate_scu.create_ups_instances([self.ups_instance])

            # Get the log messages
            log_messages = [record.getMessage() for record in self.memory_handler.buffer]
            self.test_logger.info("Log messages: %s", log_messages)

            self.assertEqual(success_count, 1)

        except Exception as e:
            self.test_logger.error(e)
            raise


if __name__ == "__main__":
    unittest.main()
