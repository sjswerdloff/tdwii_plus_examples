import logging
import subprocess
import sys
import time
import unittest
from logging.handlers import MemoryHandler

from parameterized import parameterized
from pydicom import Dataset, Sequence

from tdwii_plus_examples.upswatchnactionscu import UPSWatchNActionSCU


def create_matching_keys():
    matching_keys = Dataset()
    item = Dataset()
    item.CodeValue = "MyMachineName"
    item.CodingSchemeDesignator = "99IHERO2008"
    item.CodeMeaning = "MyMachineName treatment machine"
    seq = Sequence([item])
    matching_keys.ScheduledStationNameCodeSequence = seq
    return matching_keys


class TestUPSWatchNActionSCU(unittest.TestCase):
    def setUp(self):
        # Set up the logger for the UPSWatchNActionSCU to INFO level
        # with a memory handler to store up to 100 log messages
        self.scu_logger = logging.getLogger("upswatchscu")
        self.scu_logger.setLevel(logging.INFO)
        self.memory_handler = MemoryHandler(100)
        self.scu_logger.addHandler(self.memory_handler)

        # Set up the logger for this test to DEBUG level
        # with a stream handler to print the log messages to the console
        self.test_logger = logging.getLogger("test_upswatchscu")
        self.test_logger.setLevel(logging.INFO)
        self.stream_handler = logging.StreamHandler()
        self.test_logger.addHandler(self.stream_handler)

        # Create a UPSWatchNActionSCU instance
        self.upswatch_scu = UPSWatchNActionSCU(called_ip="localhost", called_port=11114, logger=self.scu_logger)

    def tearDown(self):
        # Remove and close the memory handler for the UPSWatchNActionSCU logger
        self.scu_logger.removeHandler(self.memory_handler)
        self.memory_handler.close()

        # Remove and close the stream handler for the test logger
        self.test_logger.removeHandler(self.stream_handler)
        self.stream_handler.close()

    @parameterized.expand(
        [
            ("global_sub", "subscribe_globally", None, False, None, "Success", 0, ""),
            ("global_sub_lock", "subscribe_globally", None, True, None, "Success", 0, ""),
            ("filtered_global_sub", "subscribe_globally", None, True, create_matching_keys(), "Success", 0, ""),
            ("global_unsub", "unsubscribe_globally", None, False, None, "Success", 0, ""),
            (
                "suspend_global_sub",
                "suspend_global_subscription",
                None,
                False,
                None,
                "Failure",
                0x0211,
                "Unrecognised Operation",
            ),
            ("single_sub", "subscribe", "1.2.3.4", None, None, "Failure", 0x0211, "Unrecognised Operation"),
            ("single_unsub", "unsubscribe", "1.2.3.4", None, None, "Failure", 0x0211, "Unrecognised Operation"),
        ]
    )
    def test_run_and_check_log(
        self,
        name,
        method_name,
        instance_uid,
        lock,
        matching_keys,
        expected_status_category,
        expected_status_code,
        expected_status_description,
    ):
        # Ensure the correct Python interpreter is used for the subprocess call
        python_executable = sys.executable

        # Start the UPS Watch SCP CLI App upsscp.py
        process = subprocess.Popen([python_executable, "tdwii_plus_examples/cli/upsscp/upsscp.py"])

        # Check that the SCP is running
        time.sleep(1)  # give some time for the SCP to start
        self.assertEqual(self.upswatch_scu.verify().status_category, "Success")

        # Run the test case
        try:
            if method_name == "subscribe_globally":
                result = getattr(self.upswatch_scu, method_name)(lock=lock, matching_keys=matching_keys)
            elif method_name == "unsubscribe_globally" or method_name == "suspend_global_subscription":
                result = getattr(self.upswatch_scu, method_name)()
            elif method_name == "subscribe":
                result = getattr(self.upswatch_scu, method_name)(instance_uid=instance_uid, lock=lock)
            elif method_name == "unsubscribe":
                result = getattr(self.upswatch_scu, method_name)(instance_uid=instance_uid)

            self.test_logger.info(result)
            self.assertEqual(result.status_category, expected_status_category)
            self.assertEqual(result.status_code, expected_status_code)
            self.assertEqual(result.status_description, expected_status_description)

            # Get the log messages
            log_messages = [record.getMessage() for record in self.memory_handler.buffer]
            self.test_logger.info(log_messages)

        except Exception as e:
            self.test_logger.error(e)
            raise
        finally:
            # Terminate the UPS Watch SCP CLI App subprocess
            process.terminate()
            process.wait()


if __name__ == "__main__":
    unittest.main()


if __name__ == "__main__":
    unittest.main()
