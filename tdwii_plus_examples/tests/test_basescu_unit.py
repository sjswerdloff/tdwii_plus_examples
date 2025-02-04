import logging
import unittest
from logging.handlers import MemoryHandler
from unittest.mock import MagicMock, PropertyMock, patch

from parameterized import parameterized
from pydicom.dataset import Dataset
from pydicom.uid import UID
from pynetdicom import AE, Association
from pynetdicom.sop_class import Verification
from pynetdicom.status import Status

from tdwii_plus_examples.basescu import BaseSCU
from tdwii_plus_examples.dicom_exceptions import (
    AssociationError,
    ContextWarning,
    ResponseCancel,
    ResponseError,
    ResponsePending,
    ResponseUnknown,
    ResponseWarning,
)


class TestBaseSCU(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Set up the logger for this test case to DEBUG level
        # with a stream handler to print the log messages to the console
        cls.test_logger = logging.getLogger("test_basescu")
        cls.test_logger.setLevel(logging.INFO)
        cls.stream_handler = logging.StreamHandler()
        cls.test_logger.addHandler(cls.stream_handler)

    def setUp(self):
        # Set up the logger for the BaseSCU to DEBUG level
        # with a memory handler to store up to 100 log messages
        self.scu_logger = logging.getLogger("basescu")
        self.scu_logger.setLevel(logging.DEBUG)
        self.memory_handler = MemoryHandler(100)
        self.scu_logger.addHandler(self.memory_handler)

        self.base_scu = BaseSCU(self.scu_logger, "MY_AE_TITLE", "192.168.1.1", 11112, "SCP_AE_TITLE")

    def tearDown(self):
        self.scu_logger.removeHandler(self.memory_handler)
        self.memory_handler.close()

    @parameterized.expand(
        [
            ("BASESCU", None, None, None),
            ("MY_AE_TITLE", "192.168.1.1", 11112, "SCP_AE_TITLE"),
            (None, "192.168.1.1", 11112, "SCP_AE_TITLE"),
            ("", "192.168.1.1", 11112, "SCP_AE_TITLE"),
            ("MY_AE_TITLE", None, None, None),
        ]
    )
    def test_init(
        self,
        calling_ae_title,
        called_ip,
        called_port,
        called_ae_title,
    ):
        with patch.object(BaseSCU, "_add_requested_context") as mock_add_requested_context:
            base_scu = BaseSCU(self.scu_logger, calling_ae_title, called_ip, called_port, called_ae_title)
            if calling_ae_title is None or calling_ae_title == "":
                expected_calling_ae_title = "BASESCU"
            else:
                expected_calling_ae_title = calling_ae_title
            self.assertEqual(base_scu.logger, self.scu_logger)
            self.assertEqual(base_scu.calling_ae_title, expected_calling_ae_title)
            self.assertEqual(base_scu.called_ip, called_ip)
            self.assertEqual(base_scu.called_port, called_port)
            self.assertEqual(base_scu.called_ae_title, called_ae_title)
            self.assertIsInstance(base_scu.ae, AE)
            self.assertEqual(base_scu.ae.ae_title, expected_calling_ae_title)
            self.assertIsNone(base_scu.assoc)
            self.assertFalse(base_scu.status)
            mock_add_requested_context.assert_called_once()
            self.test_logger.info(
                "Test init with calling_ae_title=%s, called_ip=%s, called_port=%s, called_ae_title=%s",
                calling_ae_title,
                called_ip,
                called_port,
                called_ae_title,
            )

    def test_add_requested_context(self):
        with patch.object(self.base_scu.ae, "add_requested_context") as mock_add_requested_context:
            self.base_scu._add_requested_context()
            mock_add_requested_context.assert_called_once_with(Verification)
            self.test_logger.info("Test _add_requested_context")

    def test_associate_rejection(self):
        self.base_scu.ae = MagicMock()  # Initialize the ae attribute
        self.base_scu.assoc = MagicMock()

        # Mock the associate method
        mock_assoc = MagicMock()
        mock_assoc.is_established = False
        self.base_scu.ae.associate.return_value = mock_assoc

        with patch.object(self.base_scu.assoc, "is_established", new_callable=PropertyMock) as mock_is_established:
            # Test association rejection
            mock_is_established.return_value = False
            with self.assertRaises(AssociationError):
                self.base_scu._associate()
        self.test_logger.info("Test _associate with rejection")

    @parameterized.expand(
        [
            (None, 11112),
            ("", 11112),
            ("192.168.1.1", None),
        ]
    )
    def test_associate_ae_params_not_set(self, called_ip, called_port):
        base_scu = BaseSCU(self.scu_logger, "MY_AE_TITLE", called_ip, called_port, "SCP_AE_TITLE")

        with self.assertRaises(AssociationError) as e:
            base_scu._associate()
        self.assertEqual(str(e.exception), "Called AE parameters not set")
        self.test_logger.info(
            f"Test _associate with called AE parameters not set with called_ip={called_ip}, called_port={called_port}"
        )

    @parameterized.expand(
        [
            # Test case where all contexts are accepted
            (
                [MagicMock(abstract_syntax="1.2.840.10008.1.1"), MagicMock(abstract_syntax="1.2.840.10008.5.1.4.34.6.2")],
                [MagicMock(abstract_syntax="1.2.840.10008.1.1"), MagicMock(abstract_syntax="1.2.840.10008.5.1.4.34.6.2")],
                True,
                None,
            ),
            # Test case where some contexts are not accepted
            (
                [MagicMock(abstract_syntax="1.2.840.10008.1.1"), MagicMock(abstract_syntax="1.2.840.10008.5.1.4.34.6.2")],
                [MagicMock(abstract_syntax="1.2.840.10008.1.1")],
                False,
                ContextWarning,
            ),
        ]
    )
    def test_all_contexts_accepted(self, requested_contexts, accepted_contexts, expected_result, expected_exception):
        # Initialize instance and assoc
        assoc = MagicMock(spec=Association)

        # Set the requested and accepted contexts
        self.base_scu.ae = MagicMock()
        self.base_scu.ae.requested_contexts = requested_contexts
        type(assoc).accepted_contexts = PropertyMock(return_value=accepted_contexts)

        if expected_exception:
            with self.assertRaises(expected_exception) as cm:
                self.base_scu._all_contexts_accepted(assoc)
            exception = cm.exception
            self.assertEqual(len(exception.accepted_sop_classes), len(accepted_contexts))
            self.assertEqual(len(exception.refused_sop_classes), len(requested_contexts) - len(accepted_contexts))
            # Check the log messages in the memory handler
            self.memory_handler.flush()
            log_messages = [record.getMessage() for record in self.memory_handler.buffer]
            self.test_logger.debug("Exception expected - log messages: %s", log_messages)
        else:
            result = self.base_scu._all_contexts_accepted(assoc)
            self.assertEqual(result, expected_result)
            self.memory_handler.flush()
            log_messages = [record.getMessage() for record in self.memory_handler.buffer]
            self.test_logger.debug("No exception expected - log messages: %s", log_messages)
        self.test_logger.info("Test _all_contexts_accepted")

    @parameterized.expand(
        [
            (0x0211, "Unrecognised Operation"),
            (0x9999, "Unknown status code"),
        ]
    )
    def test_get_status_description(self, status_code, expected_description):
        description = self.base_scu._get_status_description(status_code)
        self.assertEqual(description, expected_description)

    def test_handle_response_empty_dataset(self):
        rsp_status = MagicMock()
        rsp_status.Status = Status.SUCCESS
        rsp_status.__len__.return_value = 1  # Ensure rsp_status is not empty
        rsp_dataset = None

        result = self.base_scu._handle_response(rsp_status, rsp_dataset)
        self.assertTrue(result)

        # Check the log messages in the memory handler
        self.memory_handler.flush()
        log_messages = [record.getMessage() for record in self.memory_handler.buffer]
        self.assertIn("Response Dataset is None or empty", log_messages)

    @patch("tdwii_plus_examples.basescu.BaseSCU._get_status_description")
    def test_handle_response_success(self, mock_get_status_description):
        rsp_status = MagicMock()
        rsp_status.Status = Status.SUCCESS
        rsp_status.__len__.return_value = 1  # Ensure rsp_status is not empty
        rsp_dataset = MagicMock(spec=Dataset)
        mock_get_status_description.return_value = "Success"

        result = self.base_scu._handle_response(rsp_status, rsp_dataset)
        self.assertTrue(result)

        # Check the log messages in the memory handler
        self.memory_handler.flush()
        log_messages = [record.getMessage() for record in self.memory_handler.buffer]
        self.assertIn("Request successful", log_messages)

    def test_handle_response_failure(self):
        rsp_status = MagicMock()
        rsp_status.Status = 0x0211  # Failure status code
        rsp_status.__len__.return_value = 1  # Ensure rsp_status is not empty
        rsp_dataset = MagicMock(spec=Dataset)

        with self.assertRaises(ResponseError) as cm:
            self.base_scu._handle_response(rsp_status, rsp_dataset)
        self.assertEqual(str(cm.exception), "Unrecognised Operation (Status Code: 0x0211)")

    def test_handle_response_warning(self):
        rsp_status = MagicMock()
        rsp_status.Status = 0x0116  # Warning status code
        rsp_status.__len__.return_value = 1  # Ensure rsp_status is not empty
        rsp_dataset = MagicMock(spec=Dataset)

        with self.assertRaises(ResponseWarning) as cm:
            self.base_scu._handle_response(rsp_status, rsp_dataset)
        self.assertEqual(str(cm.exception), "Attribute Value Out of Range (Status Code: 0x0116)")

    @patch("tdwii_plus_examples.basescu.BaseSCU._get_status_description")
    def test_handle_response_cancel(self, mock_get_status_description):
        rsp_status = MagicMock()
        rsp_status.Status = 0xFE00  # Pending status code
        rsp_status.__len__.return_value = 1  # Ensure rsp_status is not empty
        rsp_dataset = MagicMock(spec=Dataset)
        mock_get_status_description.return_value = "Cancel"

        with self.assertRaises(ResponseCancel) as cm:
            self.base_scu._handle_response(rsp_status, rsp_dataset)
        self.assertEqual(str(cm.exception), "Cancel (Status Code: 0xFE00)")

    @patch("tdwii_plus_examples.basescu.BaseSCU._get_status_description")
    def test_handle_response_pending(self, mock_get_status_description):
        rsp_status = MagicMock()
        rsp_status.Status = 0xFF00  # Pending status code
        rsp_status.__len__.return_value = 1  # Ensure rsp_status is not empty
        rsp_dataset = MagicMock(spec=Dataset)
        mock_get_status_description.return_value = "Matches are continuing, current match supplied"

        with self.assertRaises(ResponsePending) as cm:
            self.base_scu._handle_response(rsp_status, rsp_dataset)
        self.assertEqual(str(cm.exception), "Matches are continuing, current match supplied (Status Code: 0xFF00)")

    @patch("tdwii_plus_examples.basescu.BaseSCU._get_status_description")
    def test_handle_response_unknown(self, mock_get_status_description):
        rsp_status = MagicMock()
        rsp_status.Status = 0xE000  # Unkwnown status code
        rsp_status.__len__.return_value = 1  # Ensure rsp_status is not empty
        rsp_dataset = MagicMock(spec=Dataset)
        mock_get_status_description.return_value = "Unknown status code"

        with self.assertRaises(ResponseUnknown) as cm:
            self.base_scu._handle_response(rsp_status, rsp_dataset)
        self.assertEqual(str(cm.exception), "Unknown status code (Status Code: 0xE000)")

    @patch("tdwii_plus_examples.basescu.BaseSCU._associate")
    @patch("tdwii_plus_examples.basescu.BaseSCU._handle_response")
    def test_verify_success(self, mock_handle_response, mock_associate):
        # Mock the association and response handling
        mock_assoc_instance = MagicMock()
        mock_assoc_instance.send_c_echo.return_value = MagicMock()
        mock_assoc_instance.release.return_value = None

        # Set the assoc attribute on the base_scu instance
        self.base_scu.assoc = mock_assoc_instance

        mock_handle_response.return_value = None

        # Call the verify method
        self.base_scu.verify()

        # Check that the association and response handling were called
        mock_associate.assert_called_once()
        mock_assoc_instance.send_c_echo.assert_called_once()
        mock_handle_response.assert_called_once()

        # Check the log messages in the memory handler
        self.memory_handler.flush()
        log_messages = [record.getMessage() for record in self.memory_handler.buffer]
        self.assertIn("Verification (C-ECHO) successful", log_messages)

    @parameterized.expand(
        [("with_verification", [UID("1.2.840.10008.1.1")], "[Verification SOP Class]"), ("without_verification", [], "")]
    )
    @patch("tdwii_plus_examples.basescu.BaseSCU._handle_response")
    def test_verify_context_warning(self, name, accepted_sop_classes, expected_transfer_syntax, mock_handle_response):
        # Mock the association and response handling
        mock_assoc_instance = MagicMock()
        mock_assoc_instance.send_c_echo.return_value = MagicMock()
        mock_assoc_instance.release.return_value = None

        # Set the assoc attribute on the base_scu instance
        self.base_scu.assoc = mock_assoc_instance

        mock_handle_response.return_value = None

        # Patch the _associate method with the appropriate side effect
        with patch(
            "tdwii_plus_examples.basescu.BaseSCU._associate",
            side_effect=ContextWarning(
                "Some SOP classes were refused",
                accepted_sop_classes=accepted_sop_classes,
                refused_sop_classes=[UID("1.2.840.10008.5.1.4.34.6.2")],  # UPS Watch SOP Class
            ),
        ) as mock_associate:
            # Call the verify method and expect it to raise ContextWarning
            try:
                self.base_scu.verify()
            except ContextWarning as e:
                self.scu_logger.debug(f"ContextWarning raised: {e}")

            # Check that the association was attempted
            mock_associate.assert_called_once()
            mock_assoc_instance.release.assert_called_once()

            if expected_transfer_syntax:
                mock_assoc_instance.send_c_echo.assert_called_once()
                mock_handle_response.assert_called_once()

            # Check the log messages in the memory handler
            self.memory_handler.flush()
            log_messages = [record.getMessage() for record in self.memory_handler.buffer]
            self.assertTrue(any("Some SOP classes were refused" in message for message in log_messages))
            self.assertTrue(
                any(f"Accepted Transfer Syntaxes: {expected_transfer_syntax}" in message for message in log_messages)
            )


if __name__ == "__main__":
    unittest.main()
