import unittest
import logging
from logging.handlers import MemoryHandler
import subprocess
import time
from tdwii_plus_examples.basescp import BaseSCP
from pynetdicom.sop_class import Verification


class CEchoSCP(BaseSCP):
    def __init__(self, bind_address, logger=None):
        super().__init__(bind_address=bind_address, logger=logger)

    def _add_contexts(self):
        super()._add_contexts()
        self.ae.add_supported_context(Verification, "1.2.840.10008.1.2")


class TestBaseSCP(unittest.TestCase):

    def setUp(self):
        # Set up the logger for the BaseSCP to INFO level
        # with a memory handler to store up to 100 log messages
        self.scp_logger = logging.getLogger('basescp')
        self.scp_logger.setLevel(logging.INFO)
        self.memory_handler = MemoryHandler(100)
        self.scp_logger.addHandler(self.memory_handler)

        # Set up the logger for this test to DEBUG level
        # with a stream handler to print the log messages to the console
        self.test_logger = logging.getLogger('test_basescp')
        self.test_logger.setLevel(logging.DEBUG)
        self.stream_handler = logging.StreamHandler()
        self.test_logger.addHandler(self.stream_handler)

        # Create a subclass of BaseSCP with only 1 presentation context:
        # the required Verification presentation context with the
        # default DICOM transfer syntax (Implicit VR Little Endian)
        self.scp = CEchoSCP(bind_address="localhost", logger=self.scp_logger)

    def test_run_and_check_log(self):
        # Run the SCP
        self.scp.run()

        # Send an echo request using pynetdicom's echoscu.py
        subprocess.check_call(['python', '-m', 'pynetdicom', 'echoscu',
                               'localhost', '11112',
                               '-aet', 'ECHOSCU', '-aec', 'BASE_SCP'])

        # Wait for 1 second to ensure the logs are generated
        time.sleep(1)

        # Get the log messages
        log_messages = [record.getMessage() for record
                        in self.memory_handler.buffer]

        # Check the EVT_CONN_OPEN event log message
        self.test_logger.info(f"Checking EVT_CONN_OPEN event log message: "
                              f"{log_messages[-2]}")
        self.assertRegex(log_messages[-2],
                         r"Succesful connection from " +
                         r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):([\w]{3,5})")
        # Stop the SCP
        self.scp.stop()

        # Check the EVT_CONN_CLOSED event log message
        self.test_logger.info(f"Checking EVT_CONN_CLOSE event log message: "
                              f"{log_messages[-1]}")
        self.assertRegex(log_messages[-1],
                         r"Closed connection with " +
                         r"([\w]+)@" +
                         r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):([\w]{3,5})")


if __name__ == "__main__":
    unittest.main()
