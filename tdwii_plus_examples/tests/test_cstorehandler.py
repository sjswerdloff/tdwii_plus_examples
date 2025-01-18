import sys
import unittest
import tempfile
import shutil
import os
import logging
from unittest.mock import MagicMock, patch
from parameterized import parameterized
from pydicom.dataset import Dataset, FileMetaDataset
from pydicom import uid
from tdwii_plus_examples.cstorehandler import handle_cstore


def create_mock_dataset():
    ds = Dataset()
    ds.SOPClassUID = uid.SecondaryCaptureImageStorage
    ds.SOPInstanceUID = uid.generate_uid()
    ds.PatientName = 'Test^Patient'
    ds.PatientID = '123456'
    ds.StudyInstanceUID = uid.generate_uid()
    ds.SeriesInstanceUID = uid.generate_uid()
    return ds


def create_mock_file_meta(sop_instance_uid):
    file_meta = FileMetaDataset()
    # Secondary Capture Image Storage
    file_meta.MediaStorageSOPClassUID = uid.SecondaryCaptureImageStorage
    file_meta.MediaStorageSOPInstanceUID = sop_instance_uid
    file_meta.TransferSyntaxUID = uid.ExplicitVRLittleEndian
    file_meta.ImplementationClassUID = uid.PYDICOM_IMPLEMENTATION_UID
    return file_meta


class TestHandleCStoreEvent(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp_dir = tempfile.mkdtemp()
        cls.logger = logging.getLogger("TestHandleCStoreEvent")
        handler = logging.StreamHandler()
        handler.setLevel(logging.DEBUG)
        cls.logger.addHandler(handler)
        cls.logger.setLevel(logging.DEBUG)

    def setUp(self):
        # Create a mock event
        self.mock_event = MagicMock()
        self.mock_event.dataset = create_mock_dataset()
        self.mock_event.file_meta = create_mock_file_meta(
            self.mock_event.dataset.SOPInstanceUID)
        self.mock_event.context.transfer_syntax = '1.2.840.10008.1.2.1'

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.temp_dir)

    @parameterized.expand([
        (False, 'output', 0x0000),  # Status.SUCCESS
        (True, 'output', 0x0000),   # Status.SUCCESS
        (False, None, 0xC212),      # Status.MISSING_ARGUMENT
        (False, 'output', 0xC210),  # Status.UNABLE_TO_DECODE_DATASET
        (False, '/invalid/path\0', 0xA700),  # Status.OUT_OF_RESOURCES
    ])
    @patch('logging.Logger')
    def test_handle_cstore(self, ignore, output_directory, expected_status,
                           MockLogger):

        # Create a mock args
        mock_args = MagicMock()
        mock_args.ignore = ignore
        if output_directory is not None:
            mock_args.output_directory = os.path.join(
                self.temp_dir, output_directory)
        else:
            mock_args.output_directory = None

        # Create an invalid dataset with missing SOPClassUID
        if expected_status == 0xC210:
            del self.mock_event.dataset.SOPClassUID

        # Create a mock logger
        mock_logger = MockLogger()

        # Call the function
        status_ds = handle_cstore(self.mock_event, mock_args, mock_logger)

        # Debugging output
        self.logger.debug(
            "\nTest case parameters:\n ignore = %s"
            "\n output_directory = %s"
            "\n expected_status = 0x%04X" % (
                ignore, mock_args.output_directory, expected_status))
        self.logger.debug(
            "\nTest case results:"
            "\n actual status = 0x%04X"
            "\n logger calls : %s," % (
                status_ds.Status, mock_logger.mock_calls))

        # Check the status
        self.assertEqual(status_ds.Status, expected_status)

        # Check that the logger was called with the correct messages
        if ignore:
            mock_logger.info.assert_called_once_with(
                "Ignoring C-STORE request")
        elif output_directory is None:
            mock_logger.error.assert_called_once_with(
                "args.output_directory attribute not present or None")
        elif '/invalid/path' in output_directory:
            expected_message = (
                "Unable to create the output directory: /invalid/path\x00")
            if sys.platform.startswith('win'):
                expected_message = expected_message.replace(
                    "/invalid/path", "C:/invalid/path"
                )
            mock_logger.exception.assert_called_once_with(expected_message)
        elif expected_status == 0xC210:
            mock_logger.exception.assert_called_once_with(
                "Unable to decode the data set and/or the command set")
        else:
            mock_logger.info.assert_any_call("Processing C-STORE request")
            mock_logger.info.assert_any_call(
                "Storing DICOM file: SC.%s.dcm"
                % self.mock_event.dataset.SOPInstanceUID)


if __name__ == '__main__':
    unittest.main()
