import unittest
import tempfile
import shutil
import os
import datetime
import logging
from logging.handlers import MemoryHandler
import subprocess
import time

from pydicom.dataset import FileMetaDataset, FileDataset
from pydicom import uid

from tdwii_plus_examples.cstorescp import CStoreSCP


class TestCStoreSCP(unittest.TestCase):

    def setUp(self):
        # Set up loggers
        self.memory_handler = MemoryHandler(100)
        self.scp_logger = self._setup_logger(
            'cstorescp', logging.DEBUG, self.memory_handler)
        self.test_logger = self._setup_logger(
            'test_cstorescp', logging.DEBUG, logging.StreamHandler())

        # Create a temporary directory
        self.temp_dir = tempfile.mkdtemp()

        # Create a mock DICOM file
        self.dataset_file, self.ds = self._create_dicom_file(self.temp_dir)

        # Save the mock DICOM file
        self.ds.save_as(self.dataset_file)
        self.test_logger.info(f"Created temporary file: {self.dataset_file}")

        # Create a CStoreSCP instance
        self.scp = CStoreSCP(bind_address="localhost",
                             store_directory=self.temp_dir,
                             logger=self.scp_logger)

    def _setup_logger(self, name, level, handler):
        logger = logging.getLogger(name)
        logger.setLevel(level)
        logger.addHandler(handler)
        return logger

    def _create_dicom_file(self, temp_dir):
        file_meta = self._get_file_meta()
        dataset_file = os.path.join(temp_dir, "mock_sc_image.dcm")
        ds = FileDataset(dataset_file, {}, file_meta=file_meta,
                         preamble=b"\0" * 128)
        self._add_metadata(ds)
        self._set_pixel_data(ds)
        ds.is_little_endian = True
        ds.is_implicit_VR = False
        return dataset_file, ds

    def _get_file_meta(self):
        file_meta = FileMetaDataset()
        file_meta.MediaStorageSOPClassUID = uid.SecondaryCaptureImageStorage
        file_meta.MediaStorageSOPInstanceUID = uid.generate_uid()
        file_meta.ImplementationClassUID = uid.PYDICOM_IMPLEMENTATION_UID
        file_meta.TransferSyntaxUID = uid.ExplicitVRLittleEndian
        return file_meta

    def _add_metadata(self, ds):
        ds.SOPClassUID = uid.SecondaryCaptureImageStorage
        ds.SOPInstanceUID = uid.generate_uid()
        ds.PatientName = 'Test^Patient'
        ds.PatientID = '123456'
        ds.StudyInstanceUID = uid.generate_uid()
        ds.SeriesInstanceUID = uid.generate_uid()
        dt = datetime.datetime.now()
        ds.ContentDate = dt.strftime("%Y%m%d")
        ds.ContentTime = dt.strftime("%H%M%S.%f")
        ds.Modality = "SC"

    def _set_pixel_data(self, ds):
        rows, columns = 10, 10
        pixel_data = bytes([0] * rows * columns)
        ds.Rows = rows
        ds.Columns = columns
        ds.SamplesPerPixel = 1
        ds.PhotometricInterpretation = "MONOCHROME2"
        ds.PixelRepresentation = 0
        ds.BitsAllocated = 8
        ds.BitsStored = 8
        ds.HighBit = 7
        ds.PixelData = pixel_data

    def tearDown(self):
        # Remove the temporary directory and its contents
        files_in_temp_dir = os.listdir(self.temp_dir)
        shutil.rmtree(self.temp_dir)
        self.test_logger.info(
            "Removed the temp directory: %s and its contents: %s" %
            (self.temp_dir, files_in_temp_dir))

    def test_run_and_check_log(self):
        # Run the SCP
        self.scp.run()

        # Send the dataset using pynetdicom's storescu.py
        subprocess.check_call(
            [
                'python', '-m', 'pynetdicom', 'storescu',
                'localhost', '11112', '-aet', 'STORESCU',
                '-aec', 'STORE_SCP', self.dataset_file
            ]
        )

        # Wait for 1 second to ensure the logs are generated
        time.sleep(1)

        # Get the log messages
        log_messages = [record.getMessage() for record
                        in self.memory_handler.buffer]

        # Check that the log messages contain the expected message
        filename = f"SC.{self.ds.SOPInstanceUID}.dcm"
        self.assertIn(
            f"Storing DICOM file: {filename}",
            log_messages,
            "Log messages do not contain the expected message"
        )
        # Check that the received dataset was stored
        file_path = os.path.join(self.temp_dir, filename)
        self.assertTrue(os.path.isfile(file_path),
                        f"The dataset {file_path} was not stored")
        # Stop the SCP
        self.scp.stop()


if __name__ == "__main__":
    unittest.main()
