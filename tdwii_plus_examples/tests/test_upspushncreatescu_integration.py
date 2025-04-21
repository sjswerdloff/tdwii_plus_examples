import logging
import subprocess
import sys
import time
import unittest
from logging.handlers import MemoryHandler

from parameterized import parameterized
from pydicom import Dataset
from pydicom.uid import generate_uid

from tdwii_plus_examples.upspushncreatescu import UPSPushNCreateSCU


class TestUPSPushNCreateSCU(unittest.TestCase):
    def setUp(self):
        # Set up the logger for the UPSPushNCreateSCU to INFO level
        # with a memory handler to store up to 100 log messages
        self.scu_logger = logging.getLogger("upspushscu")
        self.scu_logger.setLevel(logging.DEBUG)
        self.memory_handler = MemoryHandler(100)
        self.scu_logger.addHandler(self.memory_handler)

        # Set up the logger for this test to DEBUG level
        # with a stream handler to print the log messages to the console
        self.test_logger = logging.getLogger("test_upspushscu")
        self.test_logger.setLevel(logging.DEBUG)
        self.stream_handler = logging.StreamHandler()
        self.test_logger.addHandler(self.stream_handler)

        # Create a UPSPushNCreateSCU instance
        self.upspush_ncreate_scu = UPSPushNCreateSCU(
            calling_ae_title="UPSPUSH",
            called_ae_title="UPSSCP",
            called_ip="localhost",
            called_port=11114,
            logger=self.scu_logger,
        )

        # Create a UPS instance for testing
        self.ups_instance = Dataset()
        self.ups_instance.PatientName = "Test^Patient"
        self.ups_instance.PatientID = "123456"
        self.ups_instance.SOPClassUID = "1.2.840.10008.5.1.4.34.6.1"
        self.ups_instance.SOPInstanceUID = generate_uid()
        self.ups_instance.ProcedureStepState = "SCHEDULED"
        self.ups_instance.InputReadinessState = "READY"
        self.ups_instance.ProcedureStepLabel = "Test UPS"
        self.ups_instance.ScheduledProcedureStepStartDateTime = "20250101120000"
        self.ups_instance.ScheduledProcedureStepPriority = "MEDIUM"

    def tearDown(self):
        # Remove and close the memory handler for the UPSPushNCreateSCU logger
        self.scu_logger.removeHandler(self.memory_handler)
        self.memory_handler.close()

        # Remove and close the stream handler for the test logger
        self.test_logger.removeHandler(self.stream_handler)
        self.stream_handler.close()

    @parameterized.expand(
        [
            ("success", "Success", 0, ""),
        ]
    )
    def test_run_and_check_log(
        self,
        name,
        expected_status_category,
        expected_status_code,
        expected_status_description,
    ):
        # Ensure the correct Python interpreter is used for the subprocess call
        python_executable = sys.executable

        # Start the UPS Push SCP CLI App upsscp.py
        process = subprocess.Popen([python_executable, "tdwii_plus_examples/cli/upsscp/upsscp.py"])

        # Check that the SCP is running
        time.sleep(1)  # give some time for the SCP to start
        self.assertEqual(self.upspush_ncreate_scu.verify().status_category, "Success")

        # Run the test case
        try:
            success_count = self.upspush_ncreate_scu.create_ups_instances([self.ups_instance])

            self.assertEqual(success_count, 1)

            # Get the log messages
            log_messages = [record.getMessage() for record in self.memory_handler.buffer]
            self.test_logger.info("Log messages: %s", log_messages)

        except Exception as e:
            self.test_logger.error(e)
            raise
        finally:
            # Terminate the UPS SCP CLI App subprocess
            process.terminate()
            process.wait()


if __name__ == "__main__":
    unittest.main()


if __name__ == "__main__":
    unittest.main()
