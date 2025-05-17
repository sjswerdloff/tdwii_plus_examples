import logging
import unittest
from unittest import mock

from pydicom import Dataset
from pydicom.uid import generate_uid

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
        # simulating current handler implementation returning 2 responses (pending and dataset)
        mock_assoc_obj = mock.Mock()
        mock_assoc_obj.send_n_set.return_value = [(Dataset(), Dataset()), (Dataset(), Dataset())]
        self.scu.assoc = mock_assoc_obj

        # Mock handle_response to return a successful result
        mock_result = mock.Mock(status_category="Success")
        mock_handle_response.return_value = mock_result

        sop_instance_uid = generate_uid()

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

        sop_instance_uid = generate_uid()
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
        # simulating current handler implementation returning 2 responses (pending and dataset)
        mock_assoc_obj = mock.Mock()
        mock_assoc_obj.send_n_set.return_value = [(Dataset(), Dataset()), (Dataset(), Dataset())]
        self.scu.assoc = mock_assoc_obj

        # Mock handle_response to return a successful result
        mock_result = mock.Mock(status_category="Success")
        mock_handle_response.return_value = mock_result

        sop_instance_uid = generate_uid()
        modification_list = Dataset()
        result = self.scu.modify_ups(sop_instance_uid, modification_list)

        mock_associate.assert_called_once_with(required_sop_classes=[mock.ANY])
        mock_assoc_obj.send_n_set.assert_called_once()
        self.assertEqual(mock_handle_response.call_count, 2)
        mock_assoc_obj.release.assert_called_once()
        self.assertEqual(result, mock_result)

    from parameterized import parameterized

    @parameterized.expand(
        [
            ("no_description", None),
            ("with_description", "Halfway done"),
        ]
    )
    @mock.patch("tdwii_plus_examples.upspullnsetscu.UPSPullNSetSCU.modify_ups")
    def test_update_progress_information(self, name, description, mock_modify_ups):
        """Test update_progress_information calls modify_ups with correct dataset and optional description."""
        mock_result = mock.Mock()
        mock_modify_ups.return_value = mock_result

        sop_instance_uid = generate_uid()
        tx_uid = "1.2.3.4"
        progress = 50

        result = self.scu.update_progress_information(sop_instance_uid, tx_uid, progress, description)

        mock_modify_ups.assert_called_once()
        args, kwargs = mock_modify_ups.call_args
        self.assertEqual(args[0], sop_instance_uid)
        ds = args[1]
        self.assertEqual(ds.TransactionUID, tx_uid)
        self.assertEqual(ds.ProcedureStepProgressInformationSequence[0].ProcedureStepProgress, str(progress))
        if description is not None:
            self.assertEqual(ds.ProcedureStepProgressInformationSequence[0].ProcedureStepProgressDescription, description)
        else:
            self.assertFalse(hasattr(ds.ProcedureStepProgressInformationSequence[0], "ProcedureStepProgressDescription"))
        self.assertEqual(result, mock_result)

    from parameterized import parameterized

    @parameterized.expand(
        [
            ("no_human_performer", None, None),
            ("with_human_performer", ("AS", "TMS", "Alice Smith"), None),
            ("with_human_performer_and_name", ("AS", "TMS", "Alice Smith"), "Alice"),
            ("with_human_performer_name_only", None, "Bob"),
        ]
    )
    @mock.patch("tdwii_plus_examples.upspullnsetscu.UPSPullNSetSCU.modify_ups")
    def test_update_start_info(self, name, human_performer, human_performer_name, mock_modify_ups):
        """Test update_start_info calls modify_ups with correct dataset and optional args."""
        mock_result = mock.Mock()
        mock_modify_ups.return_value = mock_result

        sop_instance_uid = generate_uid()
        tx_uid = "1.2.3.4"
        station_name = ("GTR", "TMS", "Gantry")
        workitem_code = ("121726", "DCM", "RT Treatment with Internal Verification")

        result = self.scu.update_start_info(
            sop_instance_uid,
            tx_uid,
            station_name,
            workitem_code,
            human_performer=human_performer,
            human_performer_name=human_performer_name,
        )

        mock_modify_ups.assert_called_once()
        args, kwargs = mock_modify_ups.call_args
        self.assertEqual(args[0], sop_instance_uid)
        ds = args[1]
        self.assertEqual(ds.TransactionUID, tx_uid)
        seq = ds.UnifiedProcedureStepPerformedProcedureSequence[0]
        self.assertTrue(hasattr(seq, "PerformedStationNameCodeSequence"))
        self.assertTrue(hasattr(seq, "PerformedWorkitemCodeSequence"))
        if human_performer is not None or human_performer_name is not None:
            self.assertTrue(hasattr(seq, "ActualHumanPerformersSequence"))
            performer_item = seq.ActualHumanPerformersSequence[0]
            if human_performer is not None:
                self.assertTrue(hasattr(performer_item, "HumanPerformerCodeSequence"))
            if human_performer_name is not None:
                self.assertEqual(performer_item.HumanPerformerName, human_performer_name)
        self.assertEqual(result, mock_result)

    @mock.patch("tdwii_plus_examples.upspullnsetscu.UPSPullNSetSCU.modify_ups")
    def test_update_end_info(self, mock_modify_ups):
        """Test update_end_info calls modify_ups with correct dataset."""
        mock_result = mock.Mock()
        mock_modify_ups.return_value = mock_result

        sop_instance_uid = generate_uid()
        tx_uid = "1.2.3.4"

        result = self.scu.update_end_info(sop_instance_uid, tx_uid)

        mock_modify_ups.assert_called_once()
        args, kwargs = mock_modify_ups.call_args
        self.assertEqual(args[0], sop_instance_uid)
        ds = args[1]
        self.assertEqual(ds.TransactionUID, tx_uid)
        seq = ds.UnifiedProcedureStepPerformedProcedureSequence[0]
        self.assertTrue(hasattr(seq, "PerformedProcedureStepEndDateTime"))
        self.assertEqual(result, mock_result)

    @parameterized.expand(
        [
            ("no_reason", None),
            ("with_reason", "Test reason"),
        ]
    )
    @mock.patch("tdwii_plus_examples.upspullnsetscu.UPSPullNSetSCU.modify_ups")
    def test_update_cancel_info(self, name, reason, mock_modify_ups):
        """Test update_cancel_info calls modify_ups with correct dataset and optional reason."""
        mock_result = mock.Mock()
        mock_modify_ups.return_value = mock_result

        sop_instance_uid = generate_uid()
        tx_uid = "1.2.3.4"

        result = self.scu.update_cancel_info(sop_instance_uid, tx_uid, reason)

        mock_modify_ups.assert_called_once()
        args, kwargs = mock_modify_ups.call_args
        self.assertEqual(args[0], sop_instance_uid)
        ds = args[1]
        self.assertEqual(ds.TransactionUID, tx_uid)
        seq = ds.ProcedureStepProgressInformationSequence[0]
        if reason is not None:
            self.assertEqual(seq.ReasonForCancellation, reason)
        self.assertEqual(result, mock_result)

    @mock.patch("tdwii_plus_examples.upspullnsetscu.UPSPullNSetSCU.modify_ups")
    def test_update_output_information(self, mock_modify_ups):
        """Test update_output_information calls modify_ups with correct dataset."""
        mock_result = mock.Mock()
        mock_modify_ups.return_value = mock_result

        sop_instance_uid = generate_uid()
        tx_uid = "1.2.3.4"
        output_information_args = [("AET", generate_uid(), generate_uid(), "1.2.840.10008.5.1.4.1.1.2", generate_uid())]

        result = self.scu.update_output_information(sop_instance_uid, tx_uid, output_information_args)

        mock_modify_ups.assert_called_once()
        args, kwargs = mock_modify_ups.call_args
        self.assertEqual(args[0], sop_instance_uid)
        ds = args[1]
        self.assertEqual(ds.TransactionUID, tx_uid)
        seq = ds.UnifiedProcedureStepPerformedProcedureSequence[0]
        self.assertTrue(hasattr(seq, "OutputInformationSequence"))
        self.assertEqual(result, mock_result)
