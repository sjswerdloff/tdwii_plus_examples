import datetime

import numpy as np
import pydicom
from pydicom.dataset import Dataset, FileMetaDataset
from pydicom.uid import PYDICOM_IMPLEMENTATION_UID, UID, ExplicitVRLittleEndian, generate_uid


def generate_sc_images(num_images: int, rows: int, columns: int) -> list[Dataset]:
    """Generates a list of DICOM datasets for Secondary Capture images.

    Args:
        num_images: The number of images to generate.
        rows: The number of rows in each image.
        columns: The number of columns in each image.

    Returns:
        A list of DICOM datasets, each representing a Secondary Capture image.
    """
    # Generate a single StudyInstanceUID for all images
    study_instance_uid = generate_uid()
    series_instance_uid = generate_uid()

    datasets = []

    for i in range(num_images):
        ds = Dataset()

        # Set Patient Module required attributes
        ds.PatientName = "Test^Object"
        ds.PatientID = "123456"
        ds.PatientBirthDate = "19930822"
        ds.PatientSex = "O"

        # Set General Study Module required attributes
        dt = datetime.datetime.now()
        ds.StudyDate = dt.strftime("%Y%m%d")
        ds.StudyTime = dt.strftime("%H%M%S.%f")  # long format with micro seconds
        ds.AccessionNumber = ""
        ds.ReferringPhysicianName = ""
        ds.StudyInstanceUID = study_instance_uid
        ds.StudyID = "1"

        # Set General Series Module required attributes
        ds.Modality = "SC"
        ds.SeriesInstanceUID = series_instance_uid
        ds.SeriesNumber = "1"

        # Set General Equipment Module required attributes
        ds.Manufacturer = "ME"

        # Set SC Equipment Module required attributes
        ds.ConversionType = "WSD"

        # Set General Image Module required attributes
        ds.ImageType = ["ORIGINAL", "PRIMARY", "BLANK"]  # not required but usually set
        dt = datetime.datetime.now()
        ds.ContentDate = dt.strftime("%Y%m%d")
        ds.ContentTime = dt.strftime("%H%M%S.%f")  # long format with micro seconds
        ds.InstanceNumber = f"{i + 1}"

        # Set Image Pixel Module required attributes        ds.SamplesPerPixel = 1
        ds.SamplesPerPixel = 1
        ds.PhotometricInterpretation = "MONOCHROME2"
        ds.Rows = rows
        ds.Columns = columns
        ds.BitsAllocated = 16
        ds.BitsStored = 16
        ds.HighBit = 15
        ds.PixelRepresentation = 0
        ds.PixelData = np.zeros((rows, columns), dtype=np.uint16).tobytes()

        # Add SOP Common Module required attributes
        ds.SOPInstanceUID = pydicom.uid.generate_uid()
        ds.SOPClassUID = UID("1.2.840.10008.5.1.4.1.1.7")  # SC Image Storage

        # Other attributes which may be required by remote application
        ds.PatientOrientation = ""

        # Populate required values for file meta information
        file_meta = FileMetaDataset()
        file_meta.MediaStorageSOPClassUID = UID("1.2.840.10008.5.1.4.1.1.7")  # SC Image Storage
        file_meta.MediaStorageSOPInstanceUID = ds.SOPInstanceUID
        file_meta.ImplementationClassUID = PYDICOM_IMPLEMENTATION_UID
        file_meta.TransferSyntaxUID = ExplicitVRLittleEndian
        file_meta.is_little_endian = True
        file_meta.is_implicit_VR = False

        # Add the file meta information
        ds.file_meta = file_meta

        datasets.append(ds)

    return datasets


def generate_ups() -> Dataset:
    """Generates a DICOM datasets for UPS.

    Returns:
        A DICOM datasets representing a UPS.
    """
    ds = Dataset()

    ds.PatientName = "Test^Patient"
    ds.PatientID = "123456"
    ds.SOPClassUID = "1.2.840.10008.5.1.4.34.6.1"
    ds.SOPInstanceUID = generate_uid()
    ds.ProcedureStepState = "SCHEDULED"
    ds.InputReadinessState = "READY"
    ds.ProcedureStepLabel = "Test UPS"
    ds.ScheduledProcedureStepStartDateTime = "20250101120000"
    ds.ScheduledProcedureStepPriority = "MEDIUM"
    ds.ProcedureStepProgressInformationSequence = []

    return ds
