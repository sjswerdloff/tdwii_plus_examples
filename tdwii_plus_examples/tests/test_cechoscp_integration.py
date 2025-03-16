import logging
import re
import subprocess
import sys
import time
import unittest
from logging.handlers import MemoryHandler

from tdwii_plus_examples.cechoscp import CEchoSCP


class TestCEchoSCP(unittest.TestCase):
    def setUp(self):
        # Set up the logger for the CEchoSCP to INFO level
        # with a memory handler to store up to 100 log messages
        self.scp_logger = logging.getLogger("cechoscp")
        self.scp_logger.setLevel(logging.INFO)
        self.memory_handler = MemoryHandler(100)
        self.scp_logger.addHandler(self.memory_handler)

        # Set up the logger for this test to DEBUG level
        # with a stream handler to print the log messages to the console
        self.test_logger = logging.getLogger("test_cechoscp")
        self.test_logger.setLevel(logging.DEBUG)
        self.stream_handler = logging.StreamHandler()
        self.test_logger.addHandler(self.stream_handler)

        # Create a CEchoSCP instance
        self.scp = CEchoSCP(bind_address="localhost", logger=self.scp_logger)

    def test_run_and_check_log(self):
        # Run the SCP
        self.scp.run()

        # Ensure the correct Python interpreter is used for the subprocess call
        python_executable = sys.executable

        # Send an echo request using pynetdicom's echoscu.py
        subprocess.check_call(
            [python_executable, "-m", "pynetdicom", "echoscu", "localhost", "11112", "-aet", "ECHOSCU", "-aec", "ECHO_SCP"]
        )

        # Wait for 1 second to ensure the logs are generated
        time.sleep(1)

        # Get the log messages
        log_messages = [record.getMessage() for record in self.memory_handler.buffer]

        # Search for the EVT_C_ECHO event log message
        self.test_logger.info("Searching for EVT_C_ECHO event log message")
        pattern = r"^Received C-ECHO request from ECHOSCU@" + r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):([\w]{3,5})"
        matching_message = None
        for message in log_messages:
            if re.search(pattern, message):
                matching_message = message
                break
        self.test_logger.info(f"EVT_C_ECHO event log message found: {matching_message}")
        self.assertIsNotNone(matching_message, "EVT_C_ECHO event log message not found")

        # Stop the SCP
        self.scp.stop()


if __name__ == "__main__":
    unittest.main()
