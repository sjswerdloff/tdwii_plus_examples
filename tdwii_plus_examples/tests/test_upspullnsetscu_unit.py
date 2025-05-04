import logging
import unittest
from unittest import mock

from pydicom import Dataset

from tdwii_plus_examples.upspullnsetscu import UPSPullNSetSCU

LOGGER = logging.getLogger(__name__)


class TestUPSPullNSetSCU(unittest.TestCase):
    def setUp(self):
        """Setup before each test."""
        # Create UPSPullNSetSCU instance
        self.scu = UPSPullNSetSCU(
            logger=LOGGER,
            calling_ae_title="CALLING_AE",
            called_ip="127.0.0.1",
            called_port=11112,
            called_ae_title="CALLED_AE",
        )

    @mock.patch("tdwii_plus_examples.upspullnsetscu.UPSPullNSetSCU._handle_response")
    @mock.patch("tdwii_plus_examples.upspullnsetscu.UPSPullNSetSCU._associate")
    def test_modify_ups_success(self, mock_associate, mock_handle_response):
        """Test successful N-SET modification of a UPS instance."""
        # Mock association result
        mock_assoc_result = mock.Mock()
        mock_assoc_result.status = "Success"
        mock_associate.return_value = True, mock_assoc_result

        # Mock association object and send_n_set
        mock_assoc_obj = mock.Mock()
        mock_assoc_obj.send_n_set.return_value = (Dataset(), Dataset())
        self.scu.assoc = mock_assoc_obj

        # Mock handle_response to return a successful result
        mock_result = mock.Mock(status_category="Success")
        mock_handle_response.return_value = mock_result

        sop_instance_uid = "1.2.3.4.5"

        # Create the modification list dataset
        modification_list = Dataset()
        # Create the sequence item
        sequence_item = Dataset()
        sequence_item.ProcedureStepProgress = "10"
        # Add the sequence item to the sequence
        modification_list.ProcedureStepProgressInformationSequence = [sequence_item]

        result = self.scu.modify_ups(sop_instance_uid, modification_list)

        mock_associate.assert_called_once_with(required_sop_classes=[mock.ANY])
        mock_assoc_obj.send_n_set.assert_called_once_with(
            dataset=modification_list,
            class_uid=mock.ANY,
            instance_uid=sop_instance_uid,
            meta_uid=mock.ANY,
        )
        mock_handle_response.assert_called()
        self.assertEqual(mock_handle_response.call_count, 2)
        mock_assoc_obj.release.assert_called_once()
        self.assertEqual(result, mock_result)

    @mock.patch("tdwii_plus_examples.upspullnsetscu.UPSPullNSetSCU._handle_response")
    @mock.patch("tdwii_plus_examples.upspullnsetscu.UPSPullNSetSCU._associate")
    def test_modify_ups_assoc_error(self, mock_associate, mock_handle_response):
        """Test N-SET modification fails if association fails."""
        mock_assoc_result = mock.Mock()
        mock_assoc_result.status = "Error"
        mock_assoc_result.description = "Association failed"
        mock_associate.return_value = False, mock_assoc_result

        sop_instance_uid = "1.2.3.4.5"
        modification_list = Dataset()
        result = self.scu.modify_ups(sop_instance_uid, modification_list)

        mock_associate.assert_called_once_with(required_sop_classes=[mock.ANY])
        mock_handle_response.assert_not_called()
        self.assertEqual(result.status_category, "AssocFailure")
        self.assertEqual(result.status_code, 0xD000)
        self.assertEqual(result.status_description, "Association failed")

    @mock.patch("tdwii_plus_examples.upspullnsetscu.UPSPullNSetSCU._handle_response")
    @mock.patch("tdwii_plus_examples.upspullnsetscu.UPSPullNSetSCU._associate")
    def test_modify_ups_warning(self, mock_associate, mock_handle_response):
        """Test N-SET modification with association warning."""
        mock_assoc_result = mock.Mock()
        mock_assoc_result.status = "Warning"
        mock_assoc_result.description = "Association warning"
        mock_assoc_result.accepted_sop_classes = ["1.2.840.10008.5.1.4.34.5"]
        mock_associate.return_value = True, mock_assoc_result

        # Mock association object and send_n_set
        mock_assoc_obj = mock.Mock()
        mock_assoc_obj.send_n_set.return_value = ("rsp_status", "rsp_dataset")
        self.scu.assoc = mock_assoc_obj

        # Mock handle_response to return a successful result
        mock_result = mock.Mock(status_category="Success")
        mock_handle_response.return_value = mock_result

        sop_instance_uid = "1.2.3.4.5"
        modification_list = Dataset()
        result = self.scu.modify_ups(sop_instance_uid, modification_list)

        mock_associate.assert_called_once_with(required_sop_classes=[mock.ANY])
        mock_assoc_obj.send_n_set.assert_called_once()
        self.assertEqual(mock_handle_response.call_count, 2)
        mock_assoc_obj.release.assert_called_once()
        self.assertEqual(result, mock_result)
