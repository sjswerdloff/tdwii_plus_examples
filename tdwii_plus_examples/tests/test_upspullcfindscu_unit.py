import unittest
from unittest import mock

from parameterized import parameterized
from pydicom import Dataset
from pydicom.uid import generate_uid
from pynetdicom.sop_class import UnifiedProcedureStepPull

from tdwii_plus_examples.upspullcfindscu import UPSPullCFindSCU


class TestUPSPullCFindSCU(unittest.TestCase):
    def setUp(self):
        """Setup before each test."""
        self.scu = UPSPullCFindSCU(
            logger=None,
            calling_ae_title="CALLING_AE",
            called_ip="127.0.0.1",
            called_port=11112,
            called_ae_title="CALLED_AE",
        )

    @mock.patch("tdwii_plus_examples.upspullcfindscu.UPSPullCFindSCU._handle_response")
    @mock.patch("tdwii_plus_examples.upspullcfindscu.UPSPullCFindSCU._associate")
    def test_get_ups_success(self, mock_associate, mock_handle_response):
        """Test successful C-FIND query for UPS instances."""
        # Mock association result
        mock_assoc_result = mock.Mock()
        mock_assoc_result.status = "Success"
        mock_associate.return_value = True, mock_assoc_result

        # Mock association object and send_c_find
        mock_assoc_obj = mock.Mock()
        # Simulate two C-FIND responses with status "Pending"
        ds1 = Dataset()
        ds2 = Dataset()
        mock_assoc_obj.send_c_find.return_value = [
            (mock.Mock(Status=0xFF00), ds1),
            (mock.Mock(Status=0xFF00), ds2),
            (mock.Mock(Status=0x0000), None),  # Success
        ]
        mock_assoc_obj.release = mock.Mock()
        self.scu.assoc = mock_assoc_obj

        # Mock handle_response to return a "Pending" result for first two, "Success" for last
        pending_result = mock.Mock(status_category="Pending")
        success_result = mock.Mock(status_category="Success")
        mock_handle_response.side_effect = [pending_result, pending_result, success_result]

        ds_query = Dataset()
        result = self.scu.get_ups(ds_query)

        mock_associate.assert_called_once_with(required_sop_classes=[UnifiedProcedureStepPull])
        mock_assoc_obj.send_c_find.assert_called_once_with(ds_query, query_model=UnifiedProcedureStepPull)
        self.assertEqual(mock_handle_response.call_count, 3)
        mock_assoc_obj.release.assert_called_once()
        self.assertEqual(result, [ds1, ds2])

    @mock.patch("tdwii_plus_examples.upspullcfindscu.UPSPullCFindSCU._handle_response")
    @mock.patch("tdwii_plus_examples.upspullcfindscu.UPSPullCFindSCU._associate")
    def test_get_ups_assoc_error(self, mock_associate, mock_handle_response):
        """Test C-FIND query fails if association fails."""
        mock_assoc_result = mock.Mock()
        mock_assoc_result.status = "Error"
        mock_assoc_result.description = "Association failed"
        mock_associate.return_value = False, mock_assoc_result

        # Mock assoc to test that the release method is not called
        mock_assoc_obj = mock.Mock()
        mock_assoc_obj.release = mock.Mock()
        self.scu.assoc = mock_assoc_obj

        ds_query = Dataset()
        result = self.scu.get_ups(ds_query)

        mock_associate.assert_called_once_with(required_sop_classes=[UnifiedProcedureStepPull])
        mock_handle_response.assert_not_called()
        self.scu.assoc.release.assert_not_called()
        self.assertEqual(result, [])

    @mock.patch("tdwii_plus_examples.upspullcfindscu.UPSPullCFindSCU._handle_response")
    @mock.patch("tdwii_plus_examples.upspullcfindscu.UPSPullCFindSCU._associate")
    def test_get_ups_warning(self, mock_associate, mock_handle_response):
        """Test C-FIND query with association warning."""
        mock_assoc_result = mock.Mock()
        mock_assoc_result.status = "Warning"
        mock_assoc_result.description = "Association warning"
        mock_assoc_result.accepted_sop_classes = ["1.2.840.10008.5.1.4.34.5"]
        mock_associate.return_value = True, mock_assoc_result

        # Mock association object and send_c_find
        mock_assoc_obj = mock.Mock()
        ds1 = Dataset()
        mock_assoc_obj.send_c_find.return_value = [
            (mock.Mock(Status=0xFF00), ds1),
            (mock.Mock(Status=0x0000), None),
        ]
        mock_assoc_obj.release = mock.Mock()
        self.scu.assoc = mock_assoc_obj

        pending_result = mock.Mock(status_category="Pending")
        success_result = mock.Mock(status_category="Success")
        mock_handle_response.side_effect = [pending_result, success_result]

        ds_query = Dataset()
        result = self.scu.get_ups(ds_query)

        mock_associate.assert_called_once_with(required_sop_classes=[UnifiedProcedureStepPull])
        mock_assoc_obj.send_c_find.assert_called_once_with(ds_query, query_model=UnifiedProcedureStepPull)
        self.assertEqual(mock_handle_response.call_count, 2)
        mock_assoc_obj.release.assert_called_once()
        self.assertEqual(result, [ds1])

    @parameterized.expand(
        [
            # (description, send_c_find_return, handle_response_side_effect, expected_result, expected_call_count)
            (
                "failure_status",
                [
                    (mock.Mock(Status=0xFF00), Dataset()),  # Pending
                    (mock.Mock(Status=0xC322), None),  # Failure
                ],
                [
                    mock.Mock(status_category="Pending"),
                    mock.Mock(status_category="Failure", status_description="Unable to process"),
                ],
                [Dataset()],  # Only the first dataset should be returned
                2,
            ),
            (
                "pending_no_dataset",
                [
                    (mock.Mock(Status=0xFF00), None),  # Pending with no dataset
                    (mock.Mock(Status=0x0000), None),  # Success
                ],
                [mock.Mock(status_category="Pending"), mock.Mock(status_category="Success")],
                [],  # No datasets should be returned
                1,  # Breaking on error is expected
            ),
            ("empty_response_list", [], [], [], 0),
        ]
    )
    @mock.patch("tdwii_plus_examples.upspullcfindscu.UPSPullCFindSCU._handle_response")
    @mock.patch("tdwii_plus_examples.upspullcfindscu.UPSPullCFindSCU._associate")
    def test_get_ups_failures(
        self,
        name,
        send_c_find_return,
        handle_response_side_effect,
        expected_result,
        expected_call_count,
        mock_associate,
        mock_handle_response,
    ):
        """Test C-FIND query failure and edge cases using parameterized."""
        mock_assoc_result = mock.Mock()
        mock_assoc_result.status = "Success"
        mock_associate.return_value = True, mock_assoc_result

        # Mock association object and send_c_find
        mock_assoc_obj = mock.Mock()
        # If there are Dataset() objects in send_c_find_return, replace with unique objects for assertion
        for idx, (status, ds) in enumerate(send_c_find_return):
            if isinstance(ds, Dataset):
                send_c_find_return[idx] = (status, Dataset())
        mock_assoc_obj.send_c_find.return_value = send_c_find_return
        mock_assoc_obj.release = mock.Mock()
        self.scu.assoc = mock_assoc_obj

        mock_handle_response.side_effect = handle_response_side_effect

        ds_query = Dataset()
        result = self.scu.get_ups(ds_query)

        mock_associate.assert_called_once_with(required_sop_classes=[UnifiedProcedureStepPull])
        mock_assoc_obj.send_c_find.assert_called_once_with(ds_query, query_model=UnifiedProcedureStepPull)
        self.assertEqual(mock_handle_response.call_count, expected_call_count)
        mock_assoc_obj.release.assert_called_once()
        # Compare the number of datasets returned, since Dataset() objects are not the same
        self.assertEqual(len(result), len(expected_result))

    def test_create_ups_query(self):
        """Test the creation of a UPS query dataset with various parameters."""
        # Test with all defaults
        ds = self.scu.create_ups_query()
        self.assertIn("SOPInstanceUID", ds)
        self.assertIn("PatientName", ds)
        self.assertIn("PatientID", ds)
        self.assertIn("ScheduledWorkitemCodeSequence", ds)
        self.assertIn("InputInformationSequence", ds)
        self.assertIn("ScheduledStationNameCodeSequence", ds)
        self.assertIn("ProcedureStepState", ds)
        self.assertIn("ScheduledProcessingParametersSequence", ds)
        self.assertIn("WorklistLabel", ds)
        self.assertIn("ScheduledProcedureStepStartDateTime", ds)
        # Test with specific values
        sop_instance_uid = generate_uid()
        ds2 = self.scu.create_ups_query(
            ups_uid=sop_instance_uid,
            machine_name="Gantry1",
            procedure_step_state="IN PROGRESS",
            scheduled_no_sooner_than="202501010000",
            scheduled_no_later_than="202501012359",
        )
        self.assertEqual(ds2.SOPInstanceUID, sop_instance_uid)
        self.assertEqual(ds2.ScheduledStationNameCodeSequence[0].CodeValue, "Gantry1")
        self.assertEqual(ds2.ProcedureStepState, "")
        self.assertEqual(ds2.ScheduledProcedureStepStartDateTime, "202501010000-202501012359")


if __name__ == "__main__":
    unittest.main()
