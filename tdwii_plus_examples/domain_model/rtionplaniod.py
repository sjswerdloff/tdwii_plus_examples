from datetime import datetime
from typing import List, Optional, Union

from pydicom.dataset import Dataset, FileDataset
from pydicom.uid import PYDICOM_IMPLEMENTATION_UID

from .fractiongroup import FractionGroup
from .ionbeam import IonBeam
from .patientsetup import PatientSetup
from .rtiontolerancetable import RTIonToleranceTable


class RTIonPlanIOD:
    def __init__(self, dataset: Optional[Dataset] = None):
        self._dataset = dataset if dataset is not None else Dataset()
        self.validation_errors = [] if dataset is None else self.validate()

    # SOP Common Module (Type 1)
    @property
    def sop_class_uid(self) -> str:
        return self._dataset.SOPClassUID

    @sop_class_uid.setter
    def sop_class_uid(self, value: str):
        self._dataset.SOPClassUID = value

    @property
    def sop_instance_uid(self) -> str:
        return self._dataset.SOPInstanceUID

    @sop_instance_uid.setter
    def sop_instance_uid(self, value: str):
        self._dataset.SOPInstanceUID = value

    # Patient Module (Type 2)
    @property
    def patient_name(self) -> Optional[str]:
        return self._dataset.PatientName

    @patient_name.setter
    def patient_name(self, value: Optional[str]):
        self._dataset.PatientName = value

    @property
    def patient_id(self) -> Optional[str]:
        return self._dataset.PatientID

    @patient_id.setter
    def patient_id(self, value: Optional[str]):
        self._dataset.PatientID = value

    @property
    def patient_birth_date(self) -> Optional[str]:
        return self._dataset.get("PatientBirthDate")

    @patient_birth_date.setter
    def patient_birth_date(self, value: Optional[str]):
        if value:
            self._dataset.PatientBirthDate = value

    @property
    def patient_sex(self) -> Optional[str]:
        return self._dataset.get("PatientSex")

    @patient_sex.setter
    def patient_sex(self, value: Optional[str]):
        if value:
            self._dataset.PatientSex = value

    # General Study Module (Type 2)
    @property
    def study_instance_uid(self) -> str:
        return self._dataset.StudyInstanceUID

    @study_instance_uid.setter
    def study_instance_uid(self, value: str):
        self._dataset.StudyInstanceUID = value

    @property
    def study_date(self) -> Optional[str]:
        return self._dataset.StudyDate

    @study_date.setter
    def study_date(self, value: Optional[str]):
        self._dataset.StudyDate = value

    @property
    def study_time(self) -> Optional[str]:
        return self._dataset.StudyTime

    @study_time.setter
    def study_time(self, value: Optional[str]):
        self._dataset.StudyTime = value

    @property
    def referring_physician_name(self) -> Optional[str]:
        return self._dataset.get("ReferringPhysicianName")

    @referring_physician_name.setter
    def referring_physician_name(self, value: Optional[str]):
        if value:
            self._dataset.ReferringPhysicianName = value

    @property
    def study_id(self) -> Optional[str]:
        return self._dataset.get("StudyID")

    @study_id.setter
    def study_id(self, value: Optional[str]):
        if value:
            self._dataset.StudyID = value

    @property
    def accession_number(self) -> Optional[str]:
        return self._dataset.get("AccessionNumber")

    @accession_number.setter
    def accession_number(self, value: Optional[str]):
        if value:
            self._dataset.AccessionNumber = value

    # RT Series Module (Type 1)
    @property
    def modality(self) -> str:
        return self._dataset.Modality

    @modality.setter
    def modality(self, value: str):
        self._dataset.Modality = value

    @property
    def series_instance_uid(self) -> str:
        return self._dataset.SeriesInstanceUID

    @series_instance_uid.setter
    def series_instance_uid(self, value: str):
        self._dataset.SeriesInstanceUID = value

    @property
    def series_number(self) -> int:
        return self._dataset.SeriesNumber

    @series_number.setter
    def series_number(self, value: int):
        self._dataset.SeriesNumber = value

    # Frame of Reference Module (Type 1)
    @property
    def frame_of_reference_uid(self) -> str:
        return self._dataset.FrameOfReferenceUID

    @frame_of_reference_uid.setter
    def frame_of_reference_uid(self, value: str):
        self._dataset.FrameOfReferenceUID = value

    # General Equipment Module (Type 2)
    @property
    def manufacturer(self) -> Optional[str]:
        return self._dataset.get("Manufacturer")

    @manufacturer.setter
    def manufacturer(self, value: Optional[str]):
        if value:
            self._dataset.Manufacturer = value

    # RT General Plan Module (Type 1)
    @property
    def rt_plan_label(self) -> str:
        return self._dataset.RTPlanLabel

    @rt_plan_label.setter
    def rt_plan_label(self, value: str):
        self._dataset.RTPlanLabel = value

    @property
    def rt_plan_name(self) -> Optional[str]:
        return self._dataset.get("RTPlanName")

    @rt_plan_name.setter
    def rt_plan_name(self, value: Optional[str]):
        if value:
            self._dataset.RTPlanName = value

    @property
    def rt_plan_description(self) -> Optional[str]:
        return self._dataset.get("RTPlanDescription")

    @rt_plan_description.setter
    def rt_plan_description(self, value: Optional[str]):
        if value:
            self._dataset.RTPlanDescription = value

    @property
    def instance_number(self) -> int:
        return self._dataset.InstanceNumber

    @instance_number.setter
    def instance_number(self, value: int):
        self._dataset.InstanceNumber = value

    @property
    def rt_plan_date(self) -> Optional[str]:
        return self._dataset.get("RTPlanDate")

    @rt_plan_date.setter
    def rt_plan_date(self, value: Optional[str]):
        if value:
            self._dataset.RTPlanDate = value

    @property
    def rt_plan_time(self) -> Optional[str]:
        return self._dataset.get("RTPlanTime")

    @rt_plan_time.setter
    def rt_plan_time(self, value: Optional[str]):
        if value:
            self._dataset.RTPlanTime = value

    # RT Ion Prescription Module (Type 1)
    @property
    def prescription_description(self) -> str:
        return self._dataset.PrescriptionDescription

    @prescription_description.setter
    def prescription_description(self, value: str):
        self._dataset.PrescriptionDescription = value

    # RT Ion Tolerance Tables Module (Type 3)
    # This would typically be a sequence of tolerance tables
    # For simplicity, we'll just add a method to set/get the whole sequence
    def set_tolerance_tables(self, tolerance_tables: List[Dataset]):
        self._dataset.ToleranceTableSequence = tolerance_tables

    def get_tolerance_tables(self) -> List[Dataset]:
        return self._dataset.get("ToleranceTableSequence", [])

    # RT Ion Patient Setup Module (Type 1)
    # This would typically be a sequence of patient setups
    # For simplicity, we'll just add a method to set/get the whole sequence
    def set_patient_setups(self, patient_setups: List[Dataset]):
        self._dataset.PatientSetupSequence = patient_setups

    def get_patient_setups(self) -> List[Dataset]:
        return self._dataset.PatientSetupSequence

    # RT Ion Fraction Scheme Module (Type 1)
    # This would typically be a sequence of fraction groups
    # For simplicity, we'll just add a method to set/get the whole sequence
    def set_fraction_groups(self, fraction_groups: List[Dataset]):
        self._dataset.FractionGroupSequence = fraction_groups

    def get_fraction_groups(self) -> List[Dataset]:
        return self._dataset.FractionGroupSequence

    # RT Ion Beams Module (Type 1)
    # This would typically be a sequence of ion beams
    # For simplicity, we'll just add a method to set/get the whole sequence
    def set_ion_beams(self, ion_beams: List[Dataset]):
        self._dataset.IonBeamSequence = ion_beams

    def get_ion_beams(self) -> List[Dataset]:
        return self._dataset.IonBeamSequence

    # Approval Module (Type 3)
    @property
    def approval_status(self) -> Optional[str]:
        return self._dataset.get("ApprovalStatus")

    @approval_status.setter
    def approval_status(self, value: Optional[str]):
        if value:
            self._dataset.ApprovalStatus = value

    def validate(self) -> List[str]:
        errors = []

        # Check Type 1 elements
        type1_elements = [
            ("SOPClassUID", "sop_class_uid"),
            ("SOPInstanceUID", "sop_instance_uid"),
            ("StudyInstanceUID", "study_instance_uid"),
            ("SeriesInstanceUID", "series_instance_uid"),
            ("Modality", "modality"),
            ("FrameOfReferenceUID", "frame_of_reference_uid"),
            ("RTPlanLabel", "rt_plan_label"),
            ("PrescriptionDescription", "prescription_description"),
        ]

        for dicom_tag, attr_name in type1_elements:
            if not hasattr(self._dataset, dicom_tag) or getattr(self, attr_name) is None:
                errors.append(f"Type 1 element '{dicom_tag}' is missing or empty")

        # Check Type 2 elements
        type2_elements = [
            "PatientName",
            "PatientID",
            "StudyDate",
            "StudyTime",
            "ReferringPhysicianName",
            "StudyID",
            "AccessionNumber",
            "Manufacturer",
        ]

        for element in type2_elements:
            if not hasattr(self._dataset, element):
                errors.append(f"Type 2 element '{element}' is missing")

        # Check for required sequences
        required_sequences = ["PatientSetupSequence", "FractionGroupSequence", "IonBeamSequence"]

        for sequence in required_sequences:
            if not hasattr(self._dataset, sequence) or not getattr(self._dataset, sequence):
                errors.append(f"Required sequence '{sequence}' is missing or empty")

        return errors

    def to_dataset(self) -> FileDataset:
        file_meta = Dataset()
        file_meta.MediaStorageSOPClassUID = self.sop_class_uid
        file_meta.MediaStorageSOPInstanceUID = self.sop_instance_uid
        file_meta.ImplementationClassUID = PYDICOM_IMPLEMENTATION_UID

        ds = FileDataset(None, {}, file_meta=file_meta, preamble=b"\0" * 128)
        ds.update(self._dataset)

        # Set creation date/time
        dt = datetime.now()
        ds.ContentDate = dt.strftime("%Y%m%d")
        ds.ContentTime = dt.strftime("%H%M%S.%f")

        return ds

    def from_dataset(self, dataset: Dataset):
        self._dataset = dataset
        # You might want to add more logic here to ensure all required elements are properly set

    # ... (previous properties and methods)

    def add_tolerance_table(self, tolerance_table: "RTIonToleranceTable"):
        if not hasattr(self._dataset, "ToleranceTableSequence"):
            self._dataset.ToleranceTableSequence = []
        self._dataset.ToleranceTableSequence.append(tolerance_table.to_dataset())

    def add_patient_setup(self, patient_setup: "PatientSetup"):
        if not hasattr(self._dataset, "PatientSetupSequence"):
            self._dataset.PatientSetupSequence = []
        self._dataset.PatientSetupSequence.append(patient_setup.to_dataset())

    def add_fraction_group(self, fraction_group: "FractionGroup"):
        if not hasattr(self._dataset, "FractionGroupSequence"):
            self._dataset.FractionGroupSequence = []
        self._dataset.FractionGroupSequence.append(fraction_group.to_dataset())

    def add_ion_beam(self, ion_beam: "IonBeam"):
        if not hasattr(self._dataset, "IonBeamSequence"):
            self._dataset.IonBeamSequence = []
        self._dataset.IonBeamSequence.append(ion_beam.to_dataset())
