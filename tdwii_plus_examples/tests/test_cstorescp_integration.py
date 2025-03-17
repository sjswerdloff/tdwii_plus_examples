import datetime
import logging
import os
import shutil
import subprocess
import sys
import tempfile
import time
import unittest
from logging.handlers import MemoryHandler

from parameterized import parameterized
from pydicom import dcmread, uid
from pydicom.dataset import FileDataset, FileMetaDataset

from tdwii_plus_examples.cstorescp import CStoreSCP


class TestCStoreSCP(unittest.TestCase):
    def setUp(self):
        # Set up loggers
        self.memory_handler = MemoryHandler(100)
        self.scp_logger = self._setup_logger("cstorescp", logging.DEBUG, self.memory_handler)
        self.test_logger = self._setup_logger("test_cstorescp", logging.INFO, logging.StreamHandler())

        # Create a temporary directory
        self.temp_dir = tempfile.mkdtemp()

        # Create a mock DICOM file
        self.dataset_file_little_endian, self.ds = self._create_dicom_file(self.temp_dir)

        # Save the mock DICOM file
        self.ds.save_as(self.dataset_file_little_endian)
        self.test_logger.info("Created temporary file with ExplicitVRLittleEndian: %s" % self.dataset_file_little_endian)

        # Save the same dataset in another file with ExplicitVRBigEndian
        self.dataset_file_big_endian = os.path.join(self.temp_dir, "mock_sc_image_big_endian.dcm")
        self.ds.is_little_endian = False
        self.ds.file_meta.TransferSyntaxUID = uid.ExplicitVRBigEndian
        self.ds.save_as(self.dataset_file_big_endian)
        self.test_logger.info("Created temporary file with ExplicitVRBigEndian: %s" % self.dataset_file_big_endian)

    def _setup_logger(self, name, level, handler):
        logger = logging.getLogger(name)
        logger.setLevel(level)
        logger.addHandler(handler)
        return logger

    def _create_dicom_file(self, temp_dir):
        file_meta = self._get_file_meta()
        dataset_file = os.path.join(temp_dir, "mock_sc_image_little_endian.dcm")
        ds = FileDataset(dataset_file, {}, file_meta=file_meta, preamble=b"\0" * 128)
        self._add_metadata(ds)
        self._add_private_elements(ds)
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
        ds.PatientName = "Test^Patient"
        ds.PatientID = "123456"
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

    def _add_private_elements(self, ds):
        # Reserve a private block
        block = ds.private_block(0x0011, "PrivateCreator", create=True)
        # Add private elements
        block.add_new(0x01, "DS", "123.456")  # Decimal String
        block.add_new(0x02, "FL", 789.0123456789)  # Float
        block.add_new(0x03, "FD", 789.0123456789)  # Double

    def tearDown(self):
        # Remove the temporary directory and its contents
        files_in_temp_dir = os.listdir(self.temp_dir)
        shutil.rmtree(self.temp_dir)

        # Log the removal of the temporary directory
        self.test_logger.info("Removed the temp directory: %s and its contents: %s" % (self.temp_dir, files_in_temp_dir))

    @parameterized.expand(
        [
            ([],),
            ([uid.ExplicitVRLittleEndian],),
            ([uid.ImplicitVRLittleEndian],),
            ([uid.ExplicitVRLittleEndian, uid.ImplicitVRLittleEndian],),
            ([uid.ExplicitVRBigEndian, uid.ImplicitVRLittleEndian],),
            ([uid.ImplicitVRLittleEndian, uid.ExplicitVRLittleEndian],),
        ]
    )
    def test_run_and_check_log(self, transfer_syntaxes):
        # Create a CStoreSCP instance
        self.scp = CStoreSCP(
            bind_address="localhost",
            store_directory=self.temp_dir,
            logger=self.scp_logger,
            sop_classes=[uid.SecondaryCaptureImageStorage],
            transfer_syntaxes=transfer_syntaxes,
        )
        # Run the SCP
        self.scp.run()
        self.test_logger.info("SCP started successfully")

        # Ensure the correct Python interpreter is used for the subprocess call
        python_executable = sys.executable

        if uid.ExplicitVRBigEndian not in transfer_syntaxes:
            self.dataset_file = self.dataset_file_little_endian
        else:
            self.dataset_file = self.dataset_file_big_endian

        # Send the dataset using pynetdicom's storescu.py
        subprocess.check_call(
            [
                python_executable,
                "-m",
                "pynetdicom",
                "storescu",
                "localhost",
                "11112",
                "-aet",
                "STORESCU",
                "-aec",
                "STORE_SCP",
                self.dataset_file,
            ]
        )

        # Wait for 1 second to ensure the logs are generated
        time.sleep(1)

        # Get the log messages
        log_messages = [record.getMessage() for record in self.memory_handler.buffer]
        self.test_logger.debug(f"Log messages: {log_messages}")

        # Check that the log messages contain the expected message
        filename = f"SC.{self.ds.SOPInstanceUID}.dcm"
        self.assertIn(f"Storing DICOM file: {filename}", log_messages, "Log messages do not contain the expected message")
        # Check that the received dataset was stored
        file_path = os.path.join(self.temp_dir, filename)
        self.assertTrue(os.path.isfile(file_path), f"The dataset {file_path} was not stored")

        # Print the stored DICOM file content
        ds = dcmread(file_path)
        self.test_logger.debug(f"DICOM file content:\n{ds}")

        # Check that the private elements are present in the stored file
        private_block = ds.private_block(0x0011, "PrivateCreator")
        self.assertIn(0x01, private_block, "Private element 0x00110001 not found")
        self.assertIn(0x02, private_block, "Private element 0x00110002 not found")
        if ds.file_meta.TransferSyntaxUID in [uid.ExplicitVRLittleEndian, uid.ExplicitVRBigEndian]:
            self.assertEqual(private_block[0x01].value, "123.456", "Private element 0x00110001 has incorrect value")
            self.assertAlmostEqual(
                private_block[0x02].value, 789.0123456789, places=4, msg="Private element 0x00110002 has incorrect value"
            )
            self.assertEqual(private_block[0x03].value, 789.0123456789, msg="Private element 0x00110003 has incorrect value")
        else:
            self.assertEqual(private_block[0x01].VR, "UN", "Private element 0x00110001 has incorrect VR")
            self.assertEqual(private_block[0x01].value, b"123.456 ", "Private element 0x00110001 has incorrect value")
            self.assertEqual(private_block[0x02].VR, "UN", "Private element 0x00110002 has incorrect VR")
            self.assertEqual(private_block[0x02].value, b"\xca@ED", "Private element 0x00110002 has incorrect value")
            self.assertEqual(
                private_block[0x03].value, b"\xfb\xf8\xb0H\x19\xa8\x88@", "Private element 0x00110003 has incorrect value"
            )

        # Stop the SCP
        self.scp.stop()


if __name__ == "__main__":
    unittest.main()
