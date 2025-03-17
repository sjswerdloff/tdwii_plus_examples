import logging
import unittest
from io import BytesIO
from unittest.mock import MagicMock, Mock, patch

from parameterized import parameterized
from pydicom.dataset import Dataset
from pydicom.uid import UID
from pynetdicom.events import Event

from tdwii_plus_examples._dicom_uids import UPS_SOP_CLASSES
from tdwii_plus_examples.upsneventhandler import UPS_EVENT_TYPES, handle_nevent, nevent_callback

# Custom BytesIO class that raises an exception on read


class FaultyBytesIO(BytesIO):
    def read(self, *args, **kwargs):
        raise ValueError("Simulated read error")


class TestHandleNEvent(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.logger = logging.getLogger("TestHandleNEvent")
        handler = logging.StreamHandler()
        handler.setLevel(logging.DEBUG)
        cls.logger.addHandler(handler)
        cls.logger.setLevel(logging.DEBUG)

    def setUp(self):
        # Create a mock event
        self.mock_event = Mock(spec=Event)
        self.mock_event.request = Mock()
        self.mock_event.assoc = Mock()
        self.mock_event.request.AffectedSOPClassUID = UID(UPS_SOP_CLASSES["UnifiedProcedureStepPush"])
        self.mock_event.request.AffectedSOPInstanceUID = UID("1.2.3.4.5.6.7.8.9.0")
        self.mock_event.request.EventTypeID = 1

        # Create a mock file-like object for EventInformation
        event_info = BytesIO()
        ds = Dataset()
        ds.InputReadinessState = "READY"
        ds.ProcedureStepState = "IN PROGRESS"

        # Set transfer syntax attributes
        ds.is_little_endian = True
        ds.is_implicit_VR = True

        ds.save_as(event_info)
        event_info.seek(0)

        self.mock_event.request.EventInformation = event_info

        self.mock_event.assoc.requestor.address = "127.0.0.1"
        self.mock_event.assoc.requestor.port = 11112
        self.mock_event.timestamp = MagicMock()
        self.mock_event.timestamp.strftime.return_value = "2023-01-01 12:00:00"

    @parameterized.expand(
        [
            (1, 0x0000),  # Status.SUCCESS
            (2, 0x0000),  # Status.SUCCESS
            (3, 0x0000),  # Status.SUCCESS
            (4, 0x0000),  # Status.SUCCESS
            (5, 0x0000),  # Status.SUCCESS
            (6, 0x0113),  # Status.NO_SUCH_EVENT_TYPE
        ]
    )
    @patch("logging.Logger")
    def test_handle_nevent(self, event_type_id, expected_status, MockLogger):
        # Set the event type ID
        self.mock_event.request.EventTypeID = event_type_id

        # Create a mock logger
        mock_logger = MockLogger()

        # Call the function
        status_ds, _ = handle_nevent(self.mock_event, nevent_callback, mock_logger)

        # Debugging output
        self.logger.debug(
            "\nTest case parameters:\n event_type_id = %s\n expected_status = 0x%04X" % (event_type_id, expected_status)
        )
        self.logger.debug(
            "\nTest case results:\n actual status = 0x%04X\n logger calls : %s," % (status_ds.Status, mock_logger.mock_calls)
        )

        # Check the status
        self.assertEqual(status_ds.Status, expected_status)

        # Check that the logger was called with the correct messages
        if event_type_id in UPS_EVENT_TYPES:
            mock_logger.debug.assert_any_call(
                f"UPS Event valid Event Type ID: {event_type_id} ({UPS_EVENT_TYPES[event_type_id]})"
            )
        else:
            mock_logger.error.assert_called_once_with(f"UPS Event invalid Event Type ID: {event_type_id}")

    @patch("logging.Logger")
    def test_handle_nevent_invalid_sop_class(self, MockLogger):
        # Set an invalid SOP Class UID
        self.mock_event.request.AffectedSOPClassUID = UID("1.2.840.10008.1.1")

        # Create a mock logger
        mock_logger = MockLogger()

        # Call the function
        status_ds, _ = handle_nevent(self.mock_event, nevent_callback, mock_logger)

        # Debugging output
        self.logger.debug(
            "\nTest case parameters:\n invalid_sop_class_uid = %s"
            "\n expected_status = 0x0122" % (self.mock_event.request.AffectedSOPClassUID)
        )
        self.logger.debug(
            "\nTest case results:\n actual status = 0x%04X\n logger calls : %s," % (status_ds.Status, mock_logger.mock_calls)
        )

        # Check the status
        self.assertEqual(status_ds.Status, 0x0122)

        # Check that the logger was called with the correct messages
        mock_logger.error.assert_called_once_with("UPS Event invalid SOP Class UID: 1.2.840.10008.1.1")

    @patch("logging.Logger")
    def test_handle_nevent_invalid_event_info(self, MockLogger):
        # Set an invalid Event Information dataset
        # Create a mock file-like object for EventInformation
        event_info = FaultyBytesIO()
        ds = Dataset()
        ds.InputReadinessState = "READY"
        ds.ProcedureStepState = "IN PROGRESS"

        # Set transfer syntax attributes
        ds.is_little_endian = True
        ds.is_implicit_VR = True

        ds.save_as(event_info)
        event_info.seek(0)

        self.mock_event.request.EventInformation = event_info

        # Create a mock logger
        mock_logger = MockLogger()

        # Call the function
        status_ds, _ = handle_nevent(self.mock_event, nevent_callback, mock_logger)

        # Debugging output
        self.logger.debug(
            "\nTest case parameters:\n invalid_event_info = %s"
            "\n expected_status = 0x0107" % (self.mock_event.request.EventInformation)
        )
        self.logger.debug(
            "\nTest case results:\n actual status = 0x%04X\n logger calls : %s," % (status_ds.Status, mock_logger.mock_calls)
        )

        # Check the status
        self.assertEqual(status_ds.Status, 0x0107)

        # Check that the logger was called with the correct messages
        mock_logger.error.assert_called_once_with("InvalidException encountered: Simulated read error")

    @patch("logging.Logger")
    def test_handle_nevent_callback_exception(self, MockLogger):
        # Create a mock callback that raises an exception
        mock_callback = MagicMock(side_effect=Exception("Callback error"))

        # Create a mock logger
        mock_logger = MockLogger()

        # Call the function
        status_ds, _ = handle_nevent(self.mock_event, mock_callback, mock_logger)

        # Debugging output
        self.logger.debug("\nTest case parameters:\n callback_exception = %s\n expected_status = 0x0110" % ("Callback error"))
        self.logger.debug(
            "\nTest case results:\n actual status = 0x%04X\n logger calls : %s," % (status_ds.Status, mock_logger.mock_calls)
        )

        # Check the status
        self.assertEqual(status_ds.Status, 0x0110)

        # Check that the logger was called with the correct messages
        mock_logger.error.assert_called_once_with("Exception encountered in UPS Event callback: Callback error")


if __name__ == "__main__":
    unittest.main()
