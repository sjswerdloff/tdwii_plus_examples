import logging
import unittest
from unittest import mock

from pydicom import Dataset
from pydicom.uid import UID, generate_uid
from pynetdicom.sop_class import UnifiedProcedureStepPush

from tdwii_plus_examples.upspushncreatescu import UPSPushNCreateSCU

LOGGER = logging.getLogger(__name__)


class TestUPSPushNCreateSCU(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Setup before all tests."""
        # Create UPSPushNCreateSCU instance
        cls.upspush_ncreate_scu = UPSPushNCreateSCU(
            calling_ae_title="CALLING_AE_TITLE",
            called_ae_title="CALLED_AE_TITLE",
            called_ip="127.0.0.1",
            called_port=11112,
            logger=LOGGER,
        )

    @mock.patch("tdwii_plus_examples.upspushncreatescu.UPSPushNCreateSCU._handle_response")
    @mock.patch("tdwii_plus_examples.upspushncreatescu.UPSPushNCreateSCU._associate")
    def test_create_ups_instances(self, mock_associate, mock_handle_response):
        """Test creating multiple valid UPS instances."""
        # Create 2 'valid' UPS instances
        ds_1 = Dataset()
        ds_1.SOPClassUID = UnifiedProcedureStepPush
        ds_1.SOPInstanceUID = generate_uid()
        ds_2 = Dataset()
        ds_2.SOPClassUID = UnifiedProcedureStepPush
        ds_2.SOPInstanceUID = generate_uid()
        instances = [ds_1, ds_2]

        # Mock the association instance.
        mock_assoc_instance = mock.Mock()
        # Mock the release method.
        mock_assoc_instance.release = mock.Mock()
        # Mock the send_n_create method to return a success status and an empty dataset.
        mock_assoc_instance.send_n_create.return_value = (Dataset(), Dataset())
        # Mock _associate to return the mock association instance, preventing a real association.
        mock_associate.return_value = True, mock_assoc_instance
        # Assign the mock association instance to the SCU's assoc attribute.
        self.upspush_ncreate_scu.assoc = mock_assoc_instance
        # Mock the _handle_response method to return a success status.
        mock_handle_response.return_value = mock.Mock(status_category="Success")

        # Call the method
        success_count = self.upspush_ncreate_scu.create_ups_instances(instances)

        # Assert 2 UPS N-CREATE messages were sent and succeeded
        self.assertEqual(success_count, 2)
        mock_assoc_instance.send_n_create.assert_called()
        self.assertEqual(mock_assoc_instance.send_n_create.call_count, 2)

    @mock.patch("tdwii_plus_examples.upspushncreatescu.Association")
    def test_create_ups_instances_no_valid_instances(self, mock_assoc):
        """Test creating UPS instances with no valid instances."""

        # Create an invalid UPS instance
        ds = Dataset()
        ds.SOPClassUID = UID("1.2.3")  # Invalid SOP Class UID
        instances = [ds]

        # Call the method
        success_count = self.upspush_ncreate_scu.create_ups_instances(instances)

        # Assert UPS N-CREATE was not sent
        self.assertEqual(success_count, 0)
        mock_assoc.assert_not_called()

    @mock.patch("tdwii_plus_examples.upspushncreatescu.UPSPushNCreateSCU._associate")
    def test_create_ups_instances_association_failure(self, mock_associate):
        """Test creating UPS instances with association failure."""
        # Create 1 'valid' UPS instance
        ds = Dataset()
        ds.SOPClassUID = UnifiedProcedureStepPush
        ds.SOPInstanceUID = generate_uid()
        instances = [ds]

        # Mock the association instance.
        mock_assoc_instance = mock.Mock()
        # Mock the release method.
        mock_assoc_instance.release = mock.Mock()
        # Mock _associate to return the mock association instance, preventing a real association.
        mock_associate.return_value = False, mock_assoc_instance
        # Set the status to "Error" to simulate an association failure.
        mock_assoc_instance.status = "Error"

        # Call the method
        success_count = self.upspush_ncreate_scu.create_ups_instances(instances)

        # Assert UPS creation failed
        self.assertEqual(success_count, 0)
