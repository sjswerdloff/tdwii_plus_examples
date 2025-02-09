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
            assoc_result = self.base_scu._associate()
            self.assertEqual(assoc_result.status, "Error")
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

        assoc_result = base_scu._associate()
        self.assertEqual(assoc_result.status, "Error")
        self.assertEqual(str(assoc_result.description), "Called AE parameters not set")
        self.test_logger.info(
            f"Test _associate with called AE parameters not set with called_ip={called_ip}, called_port={called_port}"
        )

    @parameterized.expand(
        [
            # Test case where all contexts are accepted
            (
                [MagicMock(abstract_syntax="1.2.840.10008.1.1"), MagicMock(abstract_syntax="1.2.840.10008.5.1.4.34.6.2")],
                [MagicMock(abstract_syntax="1.2.840.10008.1.1"), MagicMock(abstract_syntax="1.2.840.10008.5.1.4.34.6.2")],
                "Success",
            ),
            # Test case where some contexts are not accepted
            (
                [MagicMock(abstract_syntax="1.2.840.10008.1.1"), MagicMock(abstract_syntax="1.2.840.10008.5.1.4.34.6.2")],
                [MagicMock(abstract_syntax="1.2.840.10008.1.1")],
                "Warning",
            ),
        ]
    )
    def test_all_contexts_accepted(self, requested_contexts, accepted_contexts, expected_result):
        # Initialize instance and assoc
        assoc = MagicMock(spec=Association)

        # Set the requested and accepted contexts
        self.base_scu.ae = MagicMock()
        self.base_scu.ae.requested_contexts = requested_contexts
        type(assoc).accepted_contexts = PropertyMock(return_value=accepted_contexts)

        if expected_result == "Warning":
            assoc_result = self.base_scu._all_contexts_accepted(assoc)
            self.assertEqual(assoc_result.status, expected_result)
            self.assertEqual(len(assoc_result.accepted_sop_classes), len(accepted_contexts))
            # Check the log messages in the memory handler
            self.memory_handler.flush()
            log_messages = [record.getMessage() for record in self.memory_handler.buffer]
            self.test_logger.debug("Warning expected - log messages: %s", log_messages)
        else:
            assoc_result = self.base_scu._all_contexts_accepted(assoc)
            self.assertEqual(assoc_result.status, expected_result)
            self.memory_handler.flush()
            log_messages = [record.getMessage() for record in self.memory_handler.buffer]
            self.test_logger.debug("No warning expected - log messages: %s", log_messages)
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

    def _create_minimal_test_dataset(self):
        ds = Dataset()
        ds.SOPInstanceUID = UID("1.2.3.4")
        return ds

    def test_handle_response_success(self):
        rsp_status = MagicMock()
        rsp_status.Status = Status.SUCCESS
        rsp_status.__len__.return_value = 1  # Ensure rsp_status is not empty
        rsp_dataset = self._create_minimal_test_dataset()

        result = self.base_scu._handle_response(rsp_status, rsp_dataset)
        self.assertTrue(result.status_category == "Success")
        self.assertTrue(result.status_code == Status.SUCCESS)
        self.assertTrue(result.status_description == "")
        self.assertIsNotNone(result.dataset)

    def test_handle_response_empty_dataset(self):
        rsp_status = MagicMock()
        rsp_status.Status = Status.SUCCESS
        rsp_status.__len__.return_value = 1  # Ensure rsp_status is not empty
        rsp_dataset = None

        result = self.base_scu._handle_response(rsp_status, rsp_dataset)
        self.assertTrue(result.status_category == "Success")
        self.assertTrue(result.status_code == Status.SUCCESS)
        self.assertTrue(result.status_description == "")
        self.assertIsNone(result.dataset)

        # Check the log messages in the memory handler
        self.memory_handler.flush()
        log_messages = [record.getMessage() for record in self.memory_handler.buffer]
        self.assertIn("Response Dataset is None or empty", log_messages)

    def test_handle_response_failure(self):
        rsp_status = MagicMock()
        rsp_status.Status = 0x0211  # Failure status code
        rsp_status.__len__.return_value = 1  # Ensure rsp_status is not empty
        rsp_dataset = self._create_minimal_test_dataset()

        result = self.base_scu._handle_response(rsp_status, rsp_dataset)
        self.assertTrue(result.status_category == "Failure")
        self.assertTrue(result.status_code == 0x0211)
        self.assertTrue(result.status_description == "Unrecognised Operation")
        self.assertIsNotNone(result.dataset)

    def test_handle_response_warning(self):
        rsp_status = MagicMock()
        rsp_status.Status = 0x0116  # Warning status code
        rsp_status.__len__.return_value = 1  # Ensure rsp_status is not empty
        rsp_dataset = self._create_minimal_test_dataset()

        result = self.base_scu._handle_response(rsp_status, rsp_dataset)
        self.assertTrue(result.status_category == "Warning")
        self.assertTrue(result.status_code == 0x0116)
        self.assertTrue(result.status_description == "Attribute Value Out of Range")
        self.assertIsNotNone(result.dataset)

    @patch("tdwii_plus_examples.basescu.BaseSCU._get_status_description")
    def test_handle_response_cancel(self, mock_get_status_description):
        rsp_status = MagicMock()
        rsp_status.Status = 0xFE00  # Cancel status code
        rsp_status.__len__.return_value = 1  # Ensure rsp_status is not empty
        rsp_dataset = self._create_minimal_test_dataset()
        mock_get_status_description.return_value = "Cancel"

        result = self.base_scu._handle_response(rsp_status, rsp_dataset)
        self.assertTrue(result.status_category == "Cancel")
        self.assertTrue(result.status_code == 0xFE00)
        self.assertTrue(result.status_description == "Cancel")
        self.assertIsNotNone(result.dataset)

    @patch("tdwii_plus_examples.basescu.BaseSCU._get_status_description")
    def test_handle_response_pending(self, mock_get_status_description):
        rsp_status = MagicMock()
        rsp_status.Status = 0xFF00  # Pending status code
        rsp_status.__len__.return_value = 1  # Ensure rsp_status is not empty
        rsp_dataset = self._create_minimal_test_dataset()
        mock_get_status_description.return_value = "Matches are continuing, current match supplied"

        result = self.base_scu._handle_response(rsp_status, rsp_dataset)
        self.assertTrue(result.status_category == "Pending")
        self.assertTrue(result.status_code == 0xFF00)
        self.assertTrue(result.status_description == "Matches are continuing, current match supplied")
        self.assertIsNotNone(result.dataset)

    @patch("tdwii_plus_examples.basescu.BaseSCU._get_status_description")
    def test_handle_response_unknown(self, mock_get_status_description):
        rsp_status = MagicMock()
        rsp_status.Status = 0xE000  # Unknown status code
        rsp_status.__len__.return_value = 1  # Ensure rsp_status is not empty
        rsp_dataset = self._create_minimal_test_dataset()
        mock_get_status_description.return_value = "Unknown status code"

        result = self.base_scu._handle_response(rsp_status, rsp_dataset)
        self.assertTrue(result.status_category == "Unknown")
        self.assertTrue(result.status_code == 0xE000)
        self.assertTrue(result.status_description == "Unknown status code")
        self.assertIsNotNone(result.dataset)

    @patch("tdwii_plus_examples.basescu.BaseSCU._associate")
    @patch("tdwii_plus_examples.basescu.BaseSCU._handle_response")
    def test_verify_success(self, mock_handle_response, mock_associate):
        # Mock the association and response handling
        mock_assoc_instance = MagicMock()
        mock_assoc_instance.send_c_echo.return_value = MagicMock()
        mock_assoc_instance.release.return_value = None

        # Set the assoc attribute on the base_scu instance
        self.base_scu.assoc = mock_assoc_instance

        mock_handle_response.return_value = BaseSCU.PrimitiveResult(
            status_category="Success", status_code=0x0000, status_description="", dataset=None
        )

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
    def test_verify_context_warning(self, name, accepted_sop_classes, expected_abstract_syntax, mock_handle_response):
        # Mock the association and response handling
        mock_assoc_instance = MagicMock()
        mock_assoc_instance.send_c_echo.return_value = MagicMock()
        mock_assoc_instance.release.return_value = None

        # Set the assoc attribute on the base_scu instance
        self.base_scu.assoc = mock_assoc_instance

        mock_handle_response.return_value = BaseSCU.PrimitiveResult(
            status_category="Success",
            status_code=0x0000,  # Example status code for success
            status_description="Request successful",
            dataset=None,
        )
        # Patch the _associate method with the appropriate result
        with patch(
            "tdwii_plus_examples.basescu.BaseSCU._associate",
            return_value=BaseSCU.AssociationResult(
                status="Warning",
                description="Some SOP classes were refused",
                accepted_sop_classes=accepted_sop_classes,
            ),
        ) as mock_associate:
            # Call the verify method
            result = self.base_scu.verify()
            # Check that the association was attempted
            mock_associate.assert_called_once()
            mock_assoc_instance.release.assert_called_once()

            if expected_abstract_syntax:
                mock_assoc_instance.send_c_echo.assert_called_once()
                mock_handle_response.assert_called_once()
            else:
                mock_assoc_instance.send_c_echo.assert_not_called()
                mock_handle_response.assert_not_called()

                self.assertEqual(result.status_category, "AssocFailure")
                self.assertEqual(result.status_code, 0xD001)
                self.assertEqual(result.status_description, "Some SOP classes were refused")
                self.assertIsNone(result.dataset)

            # Check the log messages in the memory handler
            self.memory_handler.flush()
            log_messages = [record.getMessage() for record in self.memory_handler.buffer]
            self.assertTrue(any("Some SOP classes were refused" in message for message in log_messages))
            self.assertTrue(any(f"Accepted SOP Classes: {expected_abstract_syntax}" in message for message in log_messages))


if __name__ == "__main__":
    unittest.main()
