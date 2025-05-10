import logging
import unittest
from unittest import mock

from parameterized import parameterized
from pydicom import Dataset
from pydicom.uid import generate_uid

from tdwii_plus_examples.upspullnactionscu import UPSPullNActionSCU

LOGGER = logging.getLogger(__name__)


class TestUPSPullNActionSCU(unittest.TestCase):
    def setUp(self):
        """Setup before each test."""
        # Create UPSPullNActionSCU instance
        self.scu = UPSPullNActionSCU(
            calling_ae_title="CALLING_AE",
            called_ip="127.0.0.1",
            called_port=11112,
            called_ae_title="CALLED_AE",
            logger=LOGGER,
        )

    @parameterized.expand(
        [
            ("success", "Success", True),
            ("failure", "Failure", False),
        ]
    )
    @mock.patch("tdwii_plus_examples.upspullnactionscu.UPSPullNActionSCU._handle_response")
    @mock.patch("tdwii_plus_examples.upspullnactionscu.UPSPullNActionSCU._associate")
    def test_claim_ups(self, name, status_category, expected, mock_associate, mock_handle_response):
        """Test claiming a UPS with parameterized status_category."""

        # Mock the association instance
        mock_assoc_instance = mock.Mock()
        # Mock the release method
        mock_assoc_instance.release = mock.Mock()
        # Mock the send_n_action method to return a tuple of (status, dataset)
        mock_assoc_instance.send_n_action.return_value = (Dataset(), Dataset())
        # Mock _associate to return the mock association instance
        mock_associate.return_value = True, mock_assoc_instance
        # Assign the mock association instance to the SCU's assoc attribute
        self.scu.assoc = mock_assoc_instance
        # Mock the _handle_response method return value status
        mock_handle_response.return_value = mock.Mock(status_category=status_category)

        sop_instance_uid = generate_uid()
        transaction_uid = self.scu.claim_ups(sop_instance_uid)

        # Check if transaction UID is generated and stored
        if expected:
            # On success, transaction_uid should be stored and not None
            self.assertIsNotNone(transaction_uid)
            self.assertEqual(self.scu.ups_transaction_info[sop_instance_uid], transaction_uid)
        else:
            # On failure, transaction_uid should be None and not stored
            self.assertIsNone(transaction_uid)
            self.assertNotIn(sop_instance_uid, self.scu.ups_transaction_info)

        # Assert _associate was called
        mock_associate.assert_called_once()
        # Assert send_n_action was called
        self.assertTrue(mock_assoc_instance.send_n_action.called)
        # Assert _handle_response was called
        mock_handle_response.assert_called_once()

    @parameterized.expand(
        [
            ("success", "Success", True),
            ("failure", "Failure", False),
        ]
    )
    @mock.patch("tdwii_plus_examples.upspullnactionscu.UPSPullNActionSCU._handle_response")
    @mock.patch("tdwii_plus_examples.upspullnactionscu.UPSPullNActionSCU._associate")
    def test_complete_ups(self, name, status_category, expected, mock_associate, mock_handle_response):
        """Test completing a UPS with parameterized status_category."""

        # Mock the association instance
        mock_assoc_instance = mock.Mock()
        mock_assoc_instance.release = mock.Mock()
        mock_assoc_instance.send_n_action.return_value = (Dataset(), Dataset())
        mock_associate.return_value = True, mock_assoc_instance
        self.scu.assoc = mock_assoc_instance
        mock_handle_response.return_value = mock.Mock(status_category=status_category)

        sop_instance_uid = generate_uid()
        transaction_uid = generate_uid()
        self.scu.ups_transaction_info[sop_instance_uid] = transaction_uid

        result = self.scu.complete_ups(sop_instance_uid, transaction_uid)

        self.assertEqual(result, expected)
        mock_associate.assert_called_once()
        self.assertTrue(mock_assoc_instance.send_n_action.called)
        mock_handle_response.assert_called_once()

    @parameterized.expand(
        [
            ("success", "Success", True),
            ("failure", "Failure", False),
        ]
    )
    @mock.patch("tdwii_plus_examples.upspullnactionscu.UPSPullNActionSCU._handle_response")
    @mock.patch("tdwii_plus_examples.upspullnactionscu.UPSPullNActionSCU._associate")
    def test_cancel_ups(self, name, status_category, expected, mock_associate, mock_handle_response):
        """Test canceling a UPS with parameterized status_category."""

        # Mock the association instance
        mock_assoc_instance = mock.Mock()
        mock_assoc_instance.release = mock.Mock()
        mock_assoc_instance.send_n_action.return_value = (Dataset(), Dataset())
        mock_associate.return_value = True, mock_assoc_instance
        self.scu.assoc = mock_assoc_instance
        mock_handle_response.return_value = mock.Mock(status_category=status_category)

        sop_instance_uid = generate_uid()
        transaction_uid = generate_uid()
        self.scu.ups_transaction_info[sop_instance_uid] = transaction_uid

        result = self.scu.cancel_ups(sop_instance_uid, transaction_uid)

        self.assertEqual(result, expected)
        mock_associate.assert_called_once()
        self.assertTrue(mock_assoc_instance.send_n_action.called)
        mock_handle_response.assert_called_once()

    def test_complete_ups_missing_transaction_uid(self):
        """Test complete_ups when transaction_uid is missing from ups_transaction_info and not passed as arg."""
        sop_instance_uid = generate_uid()
        # Do not set transaction_uid in ups_transaction_info

        with (
            mock.patch("tdwii_plus_examples.upspullnactionscu.UPSPullNActionSCU._handle_response") as mock_handle_response,
            mock.patch("tdwii_plus_examples.upspullnactionscu.UPSPullNActionSCU._associate") as mock_associate,
        ):
            result = self.scu.complete_ups(sop_instance_uid)
            self.assertFalse(result)
            mock_associate.assert_not_called()
            mock_handle_response.assert_not_called()

    def test_complete_ups_transaction_uid_passed_as_arg(self):
        """Test complete_ups when transaction_uid is not in ups_transaction_info but is passed as an argument."""
        sop_instance_uid = generate_uid()
        transaction_uid = generate_uid()
        # Do not set transaction_uid in ups_transaction_info

        with (
            mock.patch("tdwii_plus_examples.upspullnactionscu.UPSPullNActionSCU._handle_response") as mock_handle_response,
            mock.patch("tdwii_plus_examples.upspullnactionscu.UPSPullNActionSCU._associate") as mock_associate,
        ):
            mock_assoc_instance = mock.Mock()
            mock_assoc_instance.release = mock.Mock()
            mock_assoc_instance.send_n_action.return_value = (Dataset(), Dataset())
            mock_associate.return_value = True, mock_assoc_instance
            self.scu.assoc = mock_assoc_instance
            mock_handle_response.return_value = mock.Mock(status_category="Success")

            result = self.scu.complete_ups(sop_instance_uid, transaction_uid)
            self.assertTrue(result)
            mock_associate.assert_called_once()
            self.assertTrue(mock_assoc_instance.send_n_action.called)
            mock_handle_response.assert_called_once()
