import datetime
import os
from typing import Optional

import numpy as np
from pydicom import Sequence
from pydicom.dataset import Dataset, FileMetaDataset
from pydicom.uid import PYDICOM_IMPLEMENTATION_UID, UID, ExplicitVRLittleEndian, generate_uid
from pynetdicom.sop_class import RTBeamsDeliveryInstructionStorage, RTIonPlanStorage

from tdwii_plus_examples._dicom_macros import (
    create_code_seq_item,
    create_content_item,
    create_referenced_instances_and_access_item,
)


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
        ds.SOPInstanceUID = generate_uid()
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
    """
    Generates a DICOM UPS dataset.

    Returns:
        A DICOM datasets representing a UPS.

    Requirements:
        Extracted from PS3.4 CC.2.5.1 Unified Procedure Step Attribute Specification.
    +----------------------+----------------------+----------------------+----------------------+----------------------+
    | Attribute Name       | Tag                  | Usage N-CREATE (SCU) | Remark/Matching Type | Comment              |
    +======================+======================+======================+======================+======================+
    | Transaction UID      | (0008,1195)          | 2                    | Cannot be queried.   | Shall be empty       |
    +----------------------+----------------------+----------------------+----------------------+----------------------+
    | Specific Character   | (0008,0005)          | 1C                   | Required if extended |                      |
    | Set                  |                      |                      | or replacement       |                      |
    |                      |                      |                      | character set is     |                      |
    |                      |                      |                      | used                 |                      |
    +----------------------+----------------------+----------------------+----------------------+----------------------+
    | SOP Class UID        | (0008,0016)          | See CC.2.5.1.3.1     | Uniquely identifies  |                      |
    |                      |                      |                      | the SOP Class of the |                      |
    |                      |                      |                      | Unified Procedure    |                      |
    |                      |                      |                      | Step.                |                      |
    |                      |                      |                      | See Section CC.3.1   |                      |
    |                      |                      |                      | for further          |                      |
    |                      |                      |                      | explanation.         |                      |
    +----------------------+----------------------+----------------------+----------------------+----------------------+
    | SOP Instance UID     | (0008,0018)          | Not allowed.         | Uniquely identifies  | SOP Instance is      |
    |                      |                      |                      | the SOP Instance of  | conveyed in the      |
    |                      |                      |                      | the UPS.             | Affected SOP         |
    |                      |                      |                      | SOP Instance UID     | Instance UID         |
    |                      |                      |                      | shall be retrieved   | (0000,1000)          |
    |                      |                      |                      | with Single Value    |                      |
    |                      |                      |                      | Matching.            |                      |
    +----------------------+----------------------+----------------------+----------------------+----------------------+
    | Scheduled Procedure  | (0074,1200)          | 1                    | Scheduled Procedure  |                      |
    | Step Priority        |                      |                      | Step Priority shall  |                      |
    |                      |                      |                      | be retrieved with    |                      |
    |                      |                      |                      | Single Value         |                      |
    |                      |                      |                      | Matching.            |                      |
    +----------------------+----------------------+----------------------+----------------------+----------------------+
    | Procedure Step Label | (0074,1204)          | 1                    |                      |                      |
    +----------------------+----------------------+----------------------+----------------------+----------------------+
    | Worklist Label       | (0074,1202)          | 2                    |                      | If a value is not    |
    |                      |                      |                      |                      | provided by the SCU, |
    |                      |                      |                      |                      | the SCP shall fill   |
    |                      |                      |                      |                      | in the Worklist      |
    |                      |                      |                      |                      | Label, e.g., using a |
    |                      |                      |                      |                      | default value or by  |
    |                      |                      |                      |                      | assigning the UPS    |
    |                      |                      |                      |                      | instance to a        |
    |                      |                      |                      |                      | logical worklist.    |
    +----------------------+----------------------+----------------------+----------------------+----------------------+
    | Scheduled Processing | (0074,1210)          | 2                    |                      |                      |
    | Parameters Sequence  |                      |                      |                      |                      |
    +----------------------+----------------------+----------------------+----------------------+----------------------+
    | Scheduled Station    | (0040,4025)          | 2                    | The Attributes of    |                      |
    | Name Code Sequence   |                      |                      | the Scheduled        |                      |
    |                      |                      |                      | Station Name Code    |                      |
    |                      |                      |                      | Sequence shall only  |                      |
    |                      |                      |                      | be retrieved with    |                      |
    |                      |                      |                      | Sequence Matching.   |                      |
    |                      |                      |                      | In Push Scenario,    |                      |
    |                      |                      |                      | the SCP-Performer    |                      |
    |                      |                      |                      | has to create empty  |                      |
    |                      |                      |                      | but could self fill  |                      |
    |                      |                      |                      | later.               |                      |
    +----------------------+----------------------+----------------------+----------------------+----------------------+
    | Scheduled Station    | (0040,4026)          | 2                    | The Attributes of    |                      |
    | Class Code Sequence  |                      |                      | the Scheduled        |                      |
    |                      |                      |                      | Station Class Code   |                      |
    |                      |                      |                      | Sequence shall only  |                      |
    |                      |                      |                      | be retrieved with    |                      |
    |                      |                      |                      | Sequence Matching.   |                      |
    +----------------------+----------------------+----------------------+----------------------+----------------------+
    | Scheduled Station    | (0040,4027)          | 2                    | The Attributes of    |                      |
    | Geographic Location  |                      |                      | the Scheduled        |                      |
    | Code Sequence        |                      |                      | Station Geographic   |                      |
    |                      |                      |                      | Location Code        |                      |
    |                      |                      |                      | Sequence shall only  |                      |
    |                      |                      |                      | be retrieved with    |                      |
    |                      |                      |                      | Sequence Matching.   |                      |
    +----------------------+----------------------+----------------------+----------------------+----------------------+
    | Scheduled Human      | (0040,4034)          | 2C                   | The Attributes of    |                      |
    | Performers Sequence  |                      |                      | the Scheduled Human  |                      |
    |                      |                      |                      | Performers Sequence  |                      |
    |                      |                      |                      | shall only be        |                      |
    |                      |                      |                      | retrieved with       |                      |
    |                      |                      |                      | Sequence Matching.   |                      |
    |                      |                      |                      | Required if a Human  |                      |
    |                      |                      |                      | Performer is         |                      |
    |                      |                      |                      | specified.           |                      |
    +----------------------+----------------------+----------------------+----------------------+----------------------+
    | Scheduled Procedure  | (0040,4005)          | 1                    | Scheduled Procedure  |                      |
    | Step Start DateTime  |                      |                      | Step Start DateTime  |                      |
    |                      |                      |                      | shall be retrieved   |                      |
    |                      |                      |                      | with Single Value    |                      |
    |                      |                      |                      | Matching or Range    |                      |
    |                      |                      |                      | Matching.            |                      |
    +----------------------+----------------------+----------------------+----------------------+----------------------+
    | Scheduled Workitem   | (0040,4018)          | 2                    | The Attributes of    |                      |
    | Code Sequence        |                      |                      | the Scheduled        |                      |
    |                      |                      |                      | Workitem Code        |                      |
    |                      |                      |                      | Sequence shall only  |                      |
    |                      |                      |                      | be retrieved with    |                      |
    |                      |                      |                      | Sequence Matching.   |                      |
    +----------------------+----------------------+----------------------+----------------------+----------------------+
    | Comments on the      | (0040,0400)          | 2                    |                      |                      |
    | Scheduled Procedure  |                      |                      |                      |                      |
    | Step                 |                      |                      |                      |                      |
    +----------------------+----------------------+----------------------+----------------------+----------------------+
    | Input Readiness      | (0040,4041)          | 1                    | Input Readiness      |                      |
    | State                |                      |                      | State shall be       |                      |
    |                      |                      |                      | retrieved with       |                      |
    |                      |                      |                      | Single Value         |                      |
    |                      |                      |                      | Matching.            |                      |
    +----------------------+----------------------+----------------------+----------------------+----------------------+
    | Input Information    | (0040,4021)          | 2                    | The Attributes of    |                      |
    | Sequence             |                      |                      | the Input            |                      |
    |                      |                      |                      | Information Sequence |                      |
    |                      |                      |                      | shall only be        |                      |
    |                      |                      |                      | retrieved with       |                      |
    |                      |                      |                      | Sequence Matching.   |                      |
    +----------------------+----------------------+----------------------+----------------------+----------------------+
    | Study Instance UID   | (0020,000D)          | 1C                   | Required if the      |                      |
    |                      |                      |                      | Workitem is expected |                      |
    |                      |                      |                      | to result in the     |                      |
    |                      |                      |                      | creation of any      |                      |
    |                      |                      |                      | DICOM Composite      |                      |
    |                      |                      |                      | Instances whose IOD  |                      |
    |                      |                      |                      | contains the Study   |                      |
    |                      |                      |                      | IE.                  |                      |
    |                      |                      |                      | There may be         |                      |
    |                      |                      |                      | situations where the |                      |
    |                      |                      |                      | performer does not   |                      |
    |                      |                      |                      | use the Study        |                      |
    |                      |                      |                      | Instance UID         |                      |
    |                      |                      |                      | suggested by the     |                      |
    |                      |                      |                      | Scheduler.           |                      |
    +----------------------+----------------------+----------------------+----------------------+----------------------+
    | Patient's Name       | (0010,0010)          | 2                    |                      |                      |
    +----------------------+----------------------+----------------------+----------------------+----------------------+
    | Patient ID           | (0010,0020)          | 1C                   | Required if the      |                      |
    |                      |                      |                      | subject of the       |                      |
    |                      |                      |                      | workitem requires    |                      |
    |                      |                      |                      | identification or if |                      |
    |                      |                      |                      | the workitem is      |                      |
    |                      |                      |                      | expected to result   |                      |
    |                      |                      |                      | in the creation of   |                      |
    |                      |                      |                      | objects that         |                      |
    |                      |                      |                      | identify the         |                      |
    |                      |                      |                      | subject.             |                      |
    |                      |                      |                      | See Section C.30.4.1 |                      |
    |                      |                      |                      | “Patient             |                      |
    |                      |                      |                      | Identification” in   |                      |
    |                      |                      |                      | PS3.3                |                      |
    +----------------------+----------------------+----------------------+----------------------+----------------------+
    | Issuer of Patient ID | (0010,0021)          | 2                    |                      |                      |
    +----------------------+----------------------+----------------------+----------------------+----------------------+
    | Issuer of Patient ID | (0010,0024)          | 2                    |                      |                      |
    | Qualifiers Sequence  |                      |                      |                      |                      |
    +----------------------+----------------------+----------------------+----------------------+----------------------+
    | Other Patient IDs    | (0010,1002)          | 2                    |                      |                      |
    | Sequence             |                      |                      |                      |                      |
    +----------------------+----------------------+----------------------+----------------------+----------------------+
    | Patient's Birth Date | (0010,0030)          | 2                    |                      |                      |
    +----------------------+----------------------+----------------------+----------------------+----------------------+
    | Patient's Sex        | (0010,0040)          | 2                    |                      |                      |
    +----------------------+----------------------+----------------------+----------------------+----------------------+
    | Admission ID         | (0038,0010)          | 2                    |                      |                      |
    +----------------------+----------------------+----------------------+----------------------+----------------------+
    | Issuer of Admission  | (0038,0014)          | 2                    |                      |                      |
    | ID Sequence          |                      |                      |                      |                      |
    +----------------------+----------------------+----------------------+----------------------+----------------------+
    | Admitting Diagnoses  | (0008,1080)          | 2                    |                      |                      |
    | Description          |                      |                      |                      |                      |
    +----------------------+----------------------+----------------------+----------------------+----------------------+
    | Admitting Diagnoses  | (0008,1084)          | 2                    | The Attributes of    |                      |
    | Code Sequence        |                      |                      | the Admitting        |                      |
    |                      |                      |                      | Diagnoses Code       |                      |
    |                      |                      |                      | Sequence shall only  |                      |
    |                      |                      |                      | be retrieved with    |                      |
    |                      |                      |                      | Sequence Matching.   |                      |
    +----------------------+----------------------+----------------------+----------------------+----------------------+
    | Referenced Request   | (0040,A370)          | 2                    | Could be "changed"   |                      |
    | Sequence             |                      |                      | while SCHEDULED by   |                      |
    |                      |                      |                      | canceling and        |                      |
    |                      |                      |                      | re-creating with the |                      |
    |                      |                      |                      | "correct" values.    |                      |
    +----------------------+----------------------+----------------------+----------------------+----------------------+
    | Replaced Procedure   | (0074,1224)          | 1C                   | Required if the UPS  |                      |
    | Step Sequence        |                      |                      | replaces another     |                      |
    |                      |                      |                      | Procedure Step.      |                      |
    +----------------------+----------------------+----------------------+----------------------+----------------------+
    | >Referenced SOP      | (0008,1150)          | 1                    |                      |                      |
    | Class UID            |                      |                      |                      |                      |
    +----------------------+----------------------+----------------------+----------------------+----------------------+
    | >Referenced SOP      | (0008,1155)          | 1                    |                      |                      |
    | Instance UID         |                      |                      |                      |                      |
    +----------------------+----------------------+----------------------+----------------------+----------------------+
    | Procedure Step State | (0074,1000)          | 1                    | Procedure Step State | Shall be created     |
    |                      |                      |                      | shall be retrieved   | with a value of      |
    |                      |                      |                      | with Single Value    | "SCHEDULED"          |
    |                      |                      |                      | Matching             |                      |
    +----------------------+----------------------+----------------------+----------------------+----------------------+
    | Procedure Step       | (0074,1002)          | 2                    |                      | Shall be empty       |
    | Progress Information |                      |                      |                      |                      |
    | Sequence             |                      |                      |                      |                      |
    +----------------------+----------------------+----------------------+----------------------+----------------------+
    | Unified Procedure    | (0074,1216)          | 2                    | See CC.2.5.1.3.2.    | Shall be created     |
    | Step Performed       |                      |                      |                      | empty                |
    | Procedure Sequence   |                      |                      |                      |                      |
    +----------------------+----------------------+----------------------+----------------------+----------------------+
    """
    ds = Dataset()

    ds.SOPClassUID = "1.2.840.10008.5.1.4.34.6.1"  # UPS Push
    ds.SOPInstanceUID = generate_uid()  # Not allowed, conveyed in Affected SOP Instance UID
    ds.ScheduledProcedureStepPriority = "MEDIUM"  # Type 1
    ds.ProcedureStepLabel = "Test UPS"  # Type 1
    ds.WorklistLabel = ""  # Type 2

    # IHE-RO TDW-II Table 7.4.2.2.2-2: Scheduled Processing Parameters Sequence Items
    scheduled_processing_parameters_list = []

    treatment_delivery_concept = create_code_seq_item("121740", "DCM", "Treatment Delivery Type")
    treatment_delivery_type = "TREATMENT"
    treatment_param_item = create_content_item("TEXT", treatment_delivery_type, treatment_delivery_concept)
    scheduled_processing_parameters_list.append(treatment_param_item)

    plan_label_concept = create_code_seq_item("2018001", "99IHERO2018", "Plan Label")
    plan_label_value = "No Plan Label"
    plan_label_item = create_content_item("TEXT", plan_label_value, plan_label_concept)
    scheduled_processing_parameters_list.append(plan_label_item)

    current_fraction_concept = create_code_seq_item("2018002", "99IHERO2018", "Current Fraction Number")
    current_fraction_number = "1"
    current_fraction_item = create_content_item("NUMERIC", int(current_fraction_number), current_fraction_concept)
    scheduled_processing_parameters_list.append(current_fraction_item)

    fractions_planned_concept = create_code_seq_item("2018003", "99IHERO2018", "Number of Fractions Planned")
    number_of_fractions_planned = "30"
    fractions_planned_item = create_content_item("NUMERIC", int(number_of_fractions_planned), fractions_planned_concept)
    scheduled_processing_parameters_list.append(fractions_planned_item)

    ds.ScheduledProcessingParametersSequence = Sequence(scheduled_processing_parameters_list)  # Type 2. RC+*

    # IHE-RO TDW-II 7.4.2.2.1 UPS Scheduled Procedure Information Base
    station_name_concept = create_code_seq_item("GTR1", "TDW-II_PLUS", "Gantry 1")
    ds.ScheduledStationNameCodeSequence = Sequence([station_name_concept])  # Type 2. Expected to be filled later. R*

    ds.ScheduledStationClassCodeSequence = []  # Type 2
    ds.ScheduledStationGeographicLocationCodeSequence = []  # Type 2
    ds.ScheduledHumanPerformersSequence = []  # Type 2C. Required if specified
    ds.ScheduledProcedureStepStartDateTime = "20250101120000"

    # IHE-RO TDW-II 7.4.2.2.2 UPS Scheduled Procedure Information for ‘Treatment Delivery’
    work_item_concept = create_code_seq_item("121726", "DCM", "RT Treatment with Internal Verification")
    ds.ScheduledWorkitemCodeSequence = Sequence([work_item_concept])  # Type 2. R+

    ds.CommentsOnTheScheduledProcedureStep = []  # Type 2
    ds.InputReadinessState = "READY"  # Type 1

    # IHE-RO TDW-II 7.4.2.2.2 UPS Scheduled Procedure Information for ‘Treatment Delivery’
    list_of_reference_items = []

    ost_ae_title = "OST"
    plan_study_instance_uid = generate_uid()
    plan_series_instance_uid = generate_uid()
    plan_sop_class_uid = RTIonPlanStorage
    plan_sop_instance_uid = generate_uid()
    plan_reference_item = create_referenced_instances_and_access_item(
        ost_ae_title, plan_study_instance_uid, plan_series_instance_uid, plan_sop_class_uid, plan_sop_instance_uid
    )
    list_of_reference_items.append(plan_reference_item)

    tms_ae_title = "TMS"
    bdi_study_instance_uid = plan_study_instance_uid
    bdi_series_instance_uid = generate_uid()
    bdi_sop_class_uid = RTBeamsDeliveryInstructionStorage
    bdi_sop_instance_uid = generate_uid()
    bdi_reference_item = create_referenced_instances_and_access_item(
        tms_ae_title, bdi_study_instance_uid, bdi_series_instance_uid, bdi_sop_class_uid, bdi_sop_instance_uid
    )
    list_of_reference_items.append(bdi_reference_item)

    ds.InputInformationSequence = Sequence(list_of_reference_items)  # Type 2. RC+*

    ds.StudyInstanceUID = plan_study_instance_uid  # Type 2. R+*
    ds.PatientName = "Test^Patient"  # Type 2. R+
    ds.PatientID = "123456"  # Type 1C. R+
    ds.IssuerOfPatientID = ""  # Type 2
    ds.IssuerOfPatientIDQualifiersSequence = []  # Type 2
    ds.OtherPatientIDsSequence = []  # Type 2
    ds.PatientBirthDate = "19700101"  # Type 2
    ds.PatientSex = "O"  # Type 2
    ds.AdmissionID = ""  # Type 2
    ds.IssuerOfAdmissionIDSequence = []  # Type 2
    ds.AdmittingDiagnosesDescription = ""  # Type 2
    ds.ReferencedRequestSequence = []  # Type 2
    ds.ProcedureStepState = "SCHEDULED"
    ds.ProcedureStepProgressInformationSequence = []  # Type 2
    ds.UnifiedProcedureStepPerformedProcedureSequence = []  # Type 2

    return ds


def generate_ups_file(folder_path: str, output_filename: Optional[str] = None) -> str:
    """
    Generates a DICOM UPS dataset and saves it to the specified folder.

    Args:
        folder_path: The directory where the DICOM file will be saved.

    Returns:
        The file path of the saved DICOM UPS file.
    """

    ups_dataset = generate_ups()

    # Create the File Meta Information
    file_meta = FileMetaDataset()
    file_meta.MediaStorageSOPClassUID = ups_dataset.SOPClassUID
    file_meta.MediaStorageSOPInstanceUID = ups_dataset.SOPInstanceUID
    file_meta.TransferSyntaxUID = ExplicitVRLittleEndian
    file_meta.ImplementationClassUID = PYDICOM_IMPLEMENTATION_UID

    # Add the File Meta Information
    ups_dataset.file_meta = file_meta

    # Generate output filename using SOP Instance UID
    if output_filename is None:
        output_filename = f"UPS_{ups_dataset.SOPInstanceUID}.dcm"
    # Ensure the output folder exists
    os.makedirs(folder_path, exist_ok=True)
    # Build the full path
    file_path = os.path.join(folder_path, output_filename)

    # Save the dataset as a DICOM Part 10 file
    ups_dataset.save_as(file_path, write_like_original=False)

    return file_path
