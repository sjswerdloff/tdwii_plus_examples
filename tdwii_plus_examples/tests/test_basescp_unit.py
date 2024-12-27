import unittest
import logging
from logging.handlers import MemoryHandler
from unittest.mock import MagicMock, patch
from parameterized import parameterized

from tdwii_plus_examples.basescp import BaseSCP
from tdwii_plus_examples.basehandlers import handle_open, handle_close
from pynetdicom import AE, evt


class TestBaseSCP(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Set up the logger for this test case to DEBUG level
        # with a stream handler to print the log messages to the console
        cls.test_logger = logging.getLogger('test_basescp')
        cls.test_logger.setLevel(logging.INFO)
        cls.stream_handler = logging.StreamHandler()
        cls.test_logger.addHandler(cls.stream_handler)

    def setUp(self):
        # Set up the logger for the BaseSCP to DEBUG level
        # with a memory handler to store up to 100 log messages
        self.scp_logger = logging.getLogger('basescp')
        self.scp_logger.setLevel(logging.DEBUG)
        self.memory_handler = MemoryHandler(100)
        self.scp_logger.addHandler(self.memory_handler)

        # Patch the AE class to return a mock instance
        self.patcher = patch('tdwii_plus_examples.basescp.AE', autospec=True)
        self.mock_ae_class = self.patcher.start()
        self.mock_ae = self.mock_ae_class.return_value

    def tearDown(self):
        self.scp_logger.removeHandler(self.memory_handler)
        self.memory_handler.close()
        self.patcher.stop()

    # Parameterized unit tests for the constructor parameters

    # Define expected warnings text
    W_PORT_104 = 'DICOM port 104 may need admin privileges'
    W_PORT_REG = 'Registered port (1024-49151) may be used by others'

    # Define test cases parameters
    test_cases = [
        (None, None, None, None, None, None),  # DEFAULT_PARAMS
        (None, None, None, "scp_logger", None, None),  # CUSTOM_LOGGER
        ("", None, None, None, None, None),  # EMPTY_AE_TITLE
        (None, "", None, None, None, None),  # EMPTY_BIND_ADDRESS
        (123, None, None, None, TypeError, None),  # INVALID_AE_TITLE_TYPE
        (None, 123, None, None, TypeError, None),  # INVALID_BIND_ADDRESS_TYPE
        (None, None, "", None, TypeError, None),  # INVALID_PORT_TYPE
        (None, None, "123", None, TypeError, None),  # INVALID_PORT_TYPE_NAME
        (None, None, -1, None, ValueError, None),  # NEGATIVE_PORT
        (None, None, 65536, None, ValueError, None),  # OUT_OF_RANGE_PORT
        (None, None, 4711, "scp_logger", None, W_PORT_REG),  # REGISTERED_PORT
        (None, None, 104, "scp_logger", None, W_PORT_104),  # DICOM_WK_REG_PORT
        (None, None, 11112, "scp_logger", None, None),  # DICOM_REG_PORT
        (None, None, 11114, "scp_logger", None, None),  # UNASSIGNED_REG_PORT
        ("SCP", "127.0.0.1", 104, "scp_logger", None, None)  # CUSTOM_PARAMS
    ]

    # Define a function to generate test names
    def custom_name_func(testcase_func, param_num, param):
        return f"{testcase_func.__name__}_{param_num}"

    @parameterized.expand(test_cases, name_func=custom_name_func)
    def test_init_params(
        self,
        ae_title,
        bind_address,
        port,
        logger_name,
        expected_exception,
        expected_warning
    ):
        logger = getattr(self, logger_name) if logger_name else None

        if expected_exception:
            with self.assertRaises(expected_exception) as exception_context:
                BaseSCP(ae_title, bind_address, port, logger)
                self.test_logger.info(
                    f"Raised expected exception: {expected_exception.__name__}:"
                    f" {exception_context.exception}")
        else:
            scp = BaseSCP(ae_title, bind_address, port, logger)

            # Check ae_title
            self.assertEqual(
                scp.ae_title, "BASE_SCP" if not ae_title else ae_title)

            # Check bind_address
            self.assertEqual(
                scp.bind_address, "" if not bind_address else bind_address)

            # Check port
            self.assertEqual(
                scp.port, 11112 if not port else port)

            # Check logger
            if logger is None:
                self.assertEqual(scp.logger.name, 'base_scp')
            else:
                self.assertEqual(scp.logger.name, logger.name)
                self.assertIsInstance(scp.logger, logging.Logger)

            # Check for expected warning
            self.memory_handler.flush()
            log_output = [record.getMessage()
                          for record in self.memory_handler.buffer]
            if expected_warning:
                self.assertIn(f'{expected_warning}', log_output)

        # Print the log messages
        # for record in self.memory_handler.buffer:
        #     self.test_logger.info(f"{record.levelname}: {record.getMessage()}")

    # Mock unit tests for the run method

    def test_run_success(self):
        self.base_scp = BaseSCP(bind_address="localhost",
                                logger=self.scp_logger)

        self.mock_server = MagicMock()
        self.mock_ae.start_server.return_value = self.mock_server
        self.base_scp.run()
        self.mock_ae.start_server.assert_called_once_with(
            ("localhost", 11112),
            evt_handlers=self.base_scp.handlers,
            block=False
        )

        # Check the log messages
        self.memory_handler.flush()
        log_output = [record.getMessage()
                      for record in self.memory_handler.buffer]
        # Print the log output for debugging
        # self.test_logger.info(f"Log output: {log_output}")
        self.assertIn("SCP server started successfully", log_output)

    def test_run_failure(self):
        self.base_scp = BaseSCP(bind_address="localhost",
                                logger=self.scp_logger)

        self.mock_ae.start_server.side_effect = Exception(
            "Failed to start server")
        self.base_scp.run()
        self.mock_ae.start_server.assert_called_once_with(
            ("localhost", 11112),
            evt_handlers=self.base_scp.handlers,
            block=False
        )

        # Check the log messages
        self.memory_handler.flush()
        log_output = [record.getMessage()
                      for record in self.memory_handler.buffer]
        # Print the log output for debugging
        # self.test_logger.info(f"Log output: {log_output}")
        self.assertIn(
            "SCP server failed to start: Failed to start server", log_output)

    # Other unit tests

    def test_add_handlers(self):
        self.base_scp = BaseSCP(bind_address="localhost",
                                logger=self.scp_logger)
        # Check that the handlers list contains the expected handlers
        expected_handlers = [
            (evt.EVT_CONN_OPEN, handle_open, [self.scp_logger]),
            (evt.EVT_CONN_CLOSE, handle_close, [self.scp_logger])
        ]

        # Print the actual handlers for debugging
        # self.test_logger.info(f"Actual handlers: {self.base_scp.handlers}")
        self.assertEqual(self.base_scp.handlers, expected_handlers)


if __name__ == "__main__":
    unittest.main()
