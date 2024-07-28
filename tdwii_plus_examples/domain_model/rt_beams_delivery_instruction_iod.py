from enum import Enum
from typing import List, Optional

import pydicom
from pydicom.dataset import Dataset

from .referenced_rt_plan import ReferencedRTPlanSequenceItem


class VerificationImageTiming(Enum):
    BEFORE_BEAM = "BEFORE_BEAM"
    DURING_BEAM = "DURING_BEAM"
    AFTER_BEAM = "AFTER_BEAM"


class DoubleExposureFlag(Enum):
    SINGLE = "SINGLE"
    DOUBLE = "DOUBLE"


class DoubleExposureOrdering(Enum):
    OPEN_FIRST = "OPEN_FIRST"
    OPEN_SECOND = "OPEN_SECOND"


class BeamTaskType(Enum):
    VERIFY = "VERIFY"
    TREAT = "TREAT"
    VERIFY_AND_TREAT = "VERIFY_AND_TREAT"


class TreatmentDeliveryType(Enum):
    TREATMENT = "TREATMENT"
    CONTINUATION = "CONTINUATION"


class PrimaryDosimeterUnit(Enum):
    MU = "MU"
    MINUTE = "MINUTE"
    NP = "NP"


class AutosequenceFlag(Enum):
    YES = "YES"
    NO = "NO"


class OmittedBeamTaskSequence:
    def __init__(self, dataset: Optional[Dataset] = None):
        self._dataset = dataset if dataset is not None else Dataset()
        self.validation_errors = [] if dataset is None else self.validate()

    @property
    def referenced_beam_number(self) -> int:
        return self._dataset.ReferencedBeamNumber

    @referenced_beam_number.setter
    def referenced_beam_number(self, value: int):
        self._dataset.ReferencedBeamNumber = value

    @property
    def reason_for_omission(self) -> str:
        return self._dataset.ReasonForOmission

    @reason_for_omission.setter
    def reason_for_omission(self, value: str):
        self._dataset.ReasonForOmission = value

    @property
    def reason_for_omission_description(self) -> Optional[str]:
        return self._dataset.get("ReasonForOmissionDescription")

    @reason_for_omission_description.setter
    def reason_for_omission_description(self, value: Optional[str]):
        if value is not None:
            self._dataset.ReasonForOmissionDescription = value

    def validate(self) -> List[str]:
        errors = []

        # Type 1 validation
        if not self.referenced_beam_number:
            errors.append("Referenced Beam Number is required")
        if not self.reason_for_omission:
            errors.append("Reason for Omission is required")

        return errors

    def to_dataset(self) -> Dataset:
        return self._dataset


class DeliveryVerificationImageSequence:
    def __init__(self, dataset: Optional[Dataset] = None):
        self._dataset = dataset if dataset is not None else Dataset()
        self.validation_errors = [] if dataset is None else self.validate()

    @property
    def verification_image_timing(self) -> VerificationImageTiming:
        return VerificationImageTiming(self._dataset.VerificationImageTiming)

    @verification_image_timing.setter
    def verification_image_timing(self, value: VerificationImageTiming):
        self._dataset.VerificationImageTiming = value.value

    @property
    def start_cumulative_meterset_weight(self) -> Optional[float]:
        return self._dataset.get("StartCumulativeMetersetWeight")

    @start_cumulative_meterset_weight.setter
    def start_cumulative_meterset_weight(self, value: Optional[float]):
        if value is not None:
            self._dataset.StartCumulativeMetersetWeight = value

    @property
    def meterset_exposure(self) -> Optional[float]:
        return self._dataset.get("MetersetExposure")

    @meterset_exposure.setter
    def meterset_exposure(self, value: Optional[float]):
        if value is not None:
            self._dataset.MetersetExposure = value

    @property
    def end_cumulative_meterset_weight(self) -> Optional[float]:
        return self._dataset.get("EndCumulativeMetersetWeight")

    @end_cumulative_meterset_weight.setter
    def end_cumulative_meterset_weight(self, value: Optional[float]):
        if value is not None:
            self._dataset.EndCumulativeMetersetWeight = value

    @property
    def double_exposure_flag(self) -> DoubleExposureFlag:
        return DoubleExposureFlag(self._dataset.DoubleExposureFlag)

    @double_exposure_flag.setter
    def double_exposure_flag(self, value: DoubleExposureFlag):
        self._dataset.DoubleExposureFlag = value.value

    @property
    def double_exposure_ordering(self) -> Optional[DoubleExposureOrdering]:
        value = self._dataset.get("DoubleExposureOrdering")
        return DoubleExposureOrdering(value) if value else None

    @double_exposure_ordering.setter
    def double_exposure_ordering(self, value: Optional[DoubleExposureOrdering]):
        if value is not None:
            self._dataset.DoubleExposureOrdering = value.value

    @property
    def double_exposure_meterset(self) -> Optional[float]:
        return self._dataset.get("DoubleExposureMeterset")

    @double_exposure_meterset.setter
    def double_exposure_meterset(self, value: Optional[float]):
        if value is not None:
            self._dataset.DoubleExposureMeterset = value

    @property
    def double_exposure_field_delta(self) -> Optional[List[float]]:
        return self._dataset.get("DoubleExposureFieldDelta")

    @double_exposure_field_delta.setter
    def double_exposure_field_delta(self, value: Optional[List[float]]):
        if value is not None:
            self._dataset.DoubleExposureFieldDelta = value

    @property
    def x_ray_image_receptor_translation(self) -> Optional[List[float]]:
        return self._dataset.get("XRayImageReceptorTranslation")

    @x_ray_image_receptor_translation.setter
    def x_ray_image_receptor_translation(self, value: Optional[List[float]]):
        if value is not None:
            self._dataset.XRayImageReceptorTranslation = value

    def validate(self) -> List[str]:
        errors = []

        # Type 1 validation
        if not self.verification_image_timing:
            errors.append("Verification Image Timing is required")
        if not self.double_exposure_flag:
            errors.append("Double Exposure Flag is required")

        # Type 1C validation
        if self.verification_image_timing == VerificationImageTiming.DURING_BEAM:
            if self.start_cumulative_meterset_weight is None:
                errors.append("Start Cumulative Meterset Weight is required when Verification Image Timing is DURING_BEAM")

        if self.verification_image_timing in [VerificationImageTiming.BEFORE_BEAM, VerificationImageTiming.AFTER_BEAM]:
            if self.meterset_exposure is None:
                errors.append("Meterset Exposure is required when Verification Image Timing is BEFORE_BEAM or AFTER_BEAM")

        if self.double_exposure_flag == DoubleExposureFlag.DOUBLE:
            if self.double_exposure_ordering is None:
                errors.append("Double Exposure Ordering is required when Double Exposure Flag is DOUBLE")
            if self.double_exposure_meterset is None:
                errors.append("Double Exposure Meterset is required when Double Exposure Flag is DOUBLE")
            if self.double_exposure_field_delta is None:
                errors.append("Double Exposure Field Delta is required when Double Exposure Flag is DOUBLE")

        # Enumerated values validation
        if not isinstance(self.verification_image_timing, VerificationImageTiming):
            errors.append(f"Invalid Verification Image Timing: {self.verification_image_timing}")
        if not isinstance(self.double_exposure_flag, DoubleExposureFlag):
            errors.append(f"Invalid Double Exposure Flag: {self.double_exposure_flag}")
        if self.double_exposure_ordering and not isinstance(self.double_exposure_ordering, DoubleExposureOrdering):
            errors.append(f"Invalid Double Exposure Ordering: {self.double_exposure_ordering}")

        return errors

    def to_dataset(self) -> Dataset:
        return self._dataset


class BeamTaskSequence:
    def __init__(self, dataset: Optional[Dataset] = None):
        self._dataset = dataset if dataset is not None else Dataset()
        self.validation_errors = [] if dataset is None else self.validate()

    @property
    def beam_task_type(self) -> BeamTaskType:
        return BeamTaskType(self._dataset.BeamTaskType)

    @beam_task_type.setter
    def beam_task_type(self, value: BeamTaskType):
        self._dataset.BeamTaskType = value.value

    @property
    def treatment_delivery_type(self) -> TreatmentDeliveryType:
        return TreatmentDeliveryType(self._dataset.TreatmentDeliveryType)

    @treatment_delivery_type.setter
    def treatment_delivery_type(self, value: TreatmentDeliveryType):
        self._dataset.TreatmentDeliveryType = value.value

    @property
    def primary_dosimeter_unit(self) -> Optional[PrimaryDosimeterUnit]:
        value = self._dataset.get("PrimaryDosimeterUnit")
        return PrimaryDosimeterUnit(value) if value else None

    @primary_dosimeter_unit.setter
    def primary_dosimeter_unit(self, value: Optional[PrimaryDosimeterUnit]):
        if value is not None:
            self._dataset.PrimaryDosimeterUnit = value.value

    @property
    def continuation_start_meterset(self) -> Optional[float]:
        return self._dataset.get("ContinuationStartMeterset")

    @continuation_start_meterset.setter
    def continuation_start_meterset(self, value: Optional[float]):
        if value is not None:
            self._dataset.ContinuationStartMeterset = value

    @property
    def continuation_end_meterset(self) -> Optional[float]:
        return self._dataset.get("ContinuationEndMeterset")

    @continuation_end_meterset.setter
    def continuation_end_meterset(self, value: Optional[float]):
        if value is not None:
            self._dataset.ContinuationEndMeterset = value

    @property
    def current_fraction_number(self) -> int:
        return self._dataset.CurrentFractionNumber

    @current_fraction_number.setter
    def current_fraction_number(self, value: int):
        self._dataset.CurrentFractionNumber = value

    @property
    def referenced_fraction_group_number(self) -> Optional[int]:
        return self._dataset.get("ReferencedFractionGroupNumber")

    @referenced_fraction_group_number.setter
    def referenced_fraction_group_number(self, value: Optional[int]):
        if value is not None:
            self._dataset.ReferencedFractionGroupNumber = value

    @property
    def referenced_beam_number(self) -> int:
        return self._dataset.ReferencedBeamNumber

    @referenced_beam_number.setter
    def referenced_beam_number(self, value: int):
        self._dataset.ReferencedBeamNumber = value

    @property
    def beam_order_index(self) -> Optional[int]:
        return self._dataset.get("BeamOrderIndex")

    @beam_order_index.setter
    def beam_order_index(self, value: Optional[int]):
        if value is not None:
            self._dataset.BeamOrderIndex = value

    @property
    def autosequence_flag(self) -> Optional[AutosequenceFlag]:
        value = self._dataset.get("AutosequenceFlag")
        return AutosequenceFlag(value) if value else None

    @autosequence_flag.setter
    def autosequence_flag(self, value: Optional[AutosequenceFlag]):
        if value is not None:
            self._dataset.AutosequenceFlag = value.value

    @property
    def delivery_verification_image_sequence(self) -> Optional[List[DeliveryVerificationImageSequence]]:
        value = self._dataset.get("DeliveryVerificationImageSequence")
        if value is None or len(value) == 0:
            return None
        return [DeliveryVerificationImageSequence(x) for x in value]

    @delivery_verification_image_sequence.setter
    def delivery_verification_image_sequence(self, value: Optional[List[DeliveryVerificationImageSequence]]):
        if value is not None:
            self._dataset.DeliveryVerificationImageSequence = pydicom.Sequence([x.to_dataset() for x in value])

    def validate(self) -> List[str]:
        errors = []

        # Type 1 validation
        if not self.beam_task_type:
            errors.append("Beam Task Type is required")
        if not self.treatment_delivery_type:
            errors.append("Treatment Delivery Type is required")
        if not self.current_fraction_number:
            errors.append("Current Fraction Number is required")
        if not self.referenced_beam_number:
            errors.append("Referenced Beam Number is required")

        # Type 1C validation
        if self.treatment_delivery_type == TreatmentDeliveryType.CONTINUATION:
            if self.primary_dosimeter_unit is None:
                errors.append("Primary Dosimeter Unit is required when Treatment Delivery Type is CONTINUATION")
            if self.continuation_start_meterset is None:
                errors.append("Continuation Start Meterset is required when Treatment Delivery Type is CONTINUATION")
            if self.continuation_end_meterset is None:
                errors.append("Continuation End Meterset is required when Treatment Delivery Type is CONTINUATION")

        # Type 2 validation (checking presence)
        type2_attributes = [
            "table_top_vertical_adjusted_position",
            "table_top_longitudinal_adjusted_position",
            "table_top_lateral_adjusted_position",
            "patient_support_adjusted_angle",
            "table_top_eccentric_adjusted_angle",
            "table_top_pitch_adjusted_angle",
            "table_top_roll_adjusted_angle",
            "table_top_vertical_setup_displacement",
            "table_top_longitudinal_setup_displacement",
            "table_top_lateral_setup_displacement",
        ]
        for attr in type2_attributes:
            if not hasattr(self, attr):
                errors.append(f"{attr.replace('_', ' ').capitalize()} is a required attribute")

        # Enumerated values validation
        if not isinstance(self.beam_task_type, BeamTaskType):
            errors.append(f"Invalid Beam Task Type: {self.beam_task_type}")
        if not isinstance(self.treatment_delivery_type, TreatmentDeliveryType):
            errors.append(f"Invalid Treatment Delivery Type: {self.treatment_delivery_type}")
        if self.primary_dosimeter_unit and not isinstance(self.primary_dosimeter_unit, PrimaryDosimeterUnit):
            errors.append(f"Invalid Primary Dosimeter Unit: {self.primary_dosimeter_unit}")
        if self.autosequence_flag and not isinstance(self.autosequence_flag, AutosequenceFlag):
            errors.append(f"Invalid Autosequence Flag: {self.autosequence_flag}")

        return errors

    def to_dataset(self) -> Dataset:
        return self._dataset


class RTBeamsDeliveryInstructionIOD:
    def __init__(self, dataset: Optional[Dataset] = None):
        self._dataset = dataset if dataset is not None else Dataset()
        self.validation_errors = [] if dataset is None else self.validate()

    # Patient Module
    @property
    def patients_name(self) -> str:
        return self._dataset.get("PatientsName", "")

    @patients_name.setter
    def patients_name(self, value: str):
        if value:
            self._dataset.PatientsName = value

    @property
    def patient_id(self) -> str:
        return self._dataset.get("PatientID", "")

    @patient_id.setter
    def patient_id(self, value: str):
        if value:
            self._dataset.PatientID = value

    @property
    def patients_birth_date(self) -> Optional[str]:
        return self._dataset.get("PatientsBirthDate")

    @patients_birth_date.setter
    def patients_birth_date(self, value: Optional[str]):
        if value is not None:
            self._dataset.PatientsBirthDate = value

    @property
    def patients_sex(self) -> Optional[str]:
        return self._dataset.get("PatientsSex")

    @patients_sex.setter
    def patients_sex(self, value: Optional[str]):
        if value is not None:
            self._dataset.PatientsSex = value

    # Clinical Trial Subject Module
    @property
    def clinical_trial_sponsor_name(self) -> Optional[str]:
        return self._dataset.get("ClinicalTrialSponsorName")

    @clinical_trial_sponsor_name.setter
    def clinical_trial_sponsor_name(self, value: Optional[str]):
        if value is not None:
            self._dataset.ClinicalTrialSponsorName = value

    @property
    def clinical_trial_protocol_id(self) -> Optional[str]:
        return self._dataset.get("ClinicalTrialProtocolID")

    @clinical_trial_protocol_id.setter
    def clinical_trial_protocol_id(self, value: Optional[str]):
        if value is not None:
            self._dataset.ClinicalTrialProtocolID = value

    @property
    def clinical_trial_protocol_name(self) -> Optional[str]:
        return self._dataset.get("ClinicalTrialProtocolName")

    @clinical_trial_protocol_name.setter
    def clinical_trial_protocol_name(self, value: Optional[str]):
        if value is not None:
            self._dataset.ClinicalTrialProtocolName = value

    @property
    def clinical_trial_site_id(self) -> Optional[str]:
        return self._dataset.get("ClinicalTrialSiteID")

    @clinical_trial_site_id.setter
    def clinical_trial_site_id(self, value: Optional[str]):
        if value is not None:
            self._dataset.ClinicalTrialSiteID = value

    @property
    def clinical_trial_site_name(self) -> Optional[str]:
        return self._dataset.get("ClinicalTrialSiteName")

    @clinical_trial_site_name.setter
    def clinical_trial_site_name(self, value: Optional[str]):
        if value is not None:
            self._dataset.ClinicalTrialSiteName = value

    @property
    def clinical_trial_subject_id(self) -> Optional[str]:
        return self._dataset.get("ClinicalTrialSubjectID")

    @clinical_trial_subject_id.setter
    def clinical_trial_subject_id(self, value: Optional[str]):
        if value is not None:
            self._dataset.ClinicalTrialSubjectID = value

    @property
    def clinical_trial_subject_reading_id(self) -> Optional[str]:
        return self._dataset.get("ClinicalTrialSubjectReadingID")

    @clinical_trial_subject_reading_id.setter
    def clinical_trial_subject_reading_id(self, value: Optional[str]):
        if value is not None:
            self._dataset.ClinicalTrialSubjectReadingID = value

    # General Study Module
    @property
    def study_instance_uid(self) -> str:
        return self._dataset.get("StudyInstanceUID", "")

    @study_instance_uid.setter
    def study_instance_uid(self, value: str):
        if value:
            self._dataset.StudyInstanceUID = value

    @property
    def study_date(self) -> Optional[str]:
        return self._dataset.get("StudyDate")

    @study_date.setter
    def study_date(self, value: Optional[str]):
        if value is not None:
            self._dataset.StudyDate = value

    @property
    def study_time(self) -> Optional[str]:
        return self._dataset.get("StudyTime")

    @study_time.setter
    def study_time(self, value: Optional[str]):
        if value is not None:
            self._dataset.StudyTime = value

    @property
    def referring_physicians_name(self) -> Optional[str]:
        return self._dataset.get("ReferringPhysiciansName")

    @referring_physicians_name.setter
    def referring_physicians_name(self, value: Optional[str]):
        if value is not None:
            self._dataset.ReferringPhysiciansName = value

    @property
    def study_id(self) -> Optional[str]:
        return self._dataset.get("StudyID")

    @study_id.setter
    def study_id(self, value: Optional[str]):
        if value is not None:
            self._dataset.StudyID = value

    @property
    def accession_number(self) -> Optional[str]:
        return self._dataset.get("AccessionNumber")

    @accession_number.setter
    def accession_number(self, value: Optional[str]):
        if value is not None:
            self._dataset.AccessionNumber = value

    @property
    def study_description(self) -> Optional[str]:
        return self._dataset.get("StudyDescription")

    @study_description.setter
    def study_description(self, value: Optional[str]):
        if value is not None:
            self._dataset.StudyDescription = value

    # Patient Study Module
    @property
    def admitting_diagnoses_description(self) -> Optional[List[str]]:
        return self._dataset.get("AdmittingDiagnosesDescription")

    @admitting_diagnoses_description.setter
    def admitting_diagnoses_description(self, value: Optional[List[str]]):
        if value is not None:
            self._dataset.AdmittingDiagnosesDescription = value

    @property
    def patients_age(self) -> Optional[str]:
        return self._dataset.get("PatientsAge")

    @patients_age.setter
    def patients_age(self, value: Optional[str]):
        if value is not None:
            self._dataset.PatientsAge = value

    @property
    def patients_size(self) -> Optional[float]:
        return self._dataset.get("PatientsSize")

    @patients_size.setter
    def patients_size(self, value: Optional[float]):
        if value is not None:
            self._dataset.PatientsSize = value

    @property
    def patients_weight(self) -> Optional[float]:
        return self._dataset.get("PatientsWeight")

    @patients_weight.setter
    def patients_weight(self, value: Optional[float]):
        if value is not None:
            self._dataset.PatientsWeight = value

    # RT Series Module
    @property
    def modality(self) -> str:
        return self._dataset.get("Modality", "")

    @modality.setter
    def modality(self, value: str):
        if value:
            self._dataset.Modality = value

    @property
    def series_instance_uid(self) -> str:
        return self._dataset.get("SeriesInstanceUID", "")

    @series_instance_uid.setter
    def series_instance_uid(self, value: str):
        if value:
            self._dataset.SeriesInstanceUID = value

    @property
    def series_number(self) -> Optional[int]:
        return self._dataset.get("SeriesNumber")

    @series_number.setter
    def series_number(self, value: Optional[int]):
        if value is not None:
            self._dataset.SeriesNumber = value

    @property
    def series_description(self) -> Optional[str]:
        return self._dataset.get("SeriesDescription")

    @series_description.setter
    def series_description(self, value: Optional[str]):
        if value is not None:
            self._dataset.SeriesDescription = value

    @property
    def series_date(self) -> Optional[str]:
        return self._dataset.get("SeriesDate")

    @series_date.setter
    def series_date(self, value: Optional[str]):
        if value is not None:
            self._dataset.SeriesDate = value

    @property
    def series_time(self) -> Optional[str]:
        return self._dataset.get("SeriesTime")

    @series_time.setter
    def series_time(self, value: Optional[str]):
        if value is not None:
            self._dataset.SeriesTime = value

    # Clinical Trial Series Module
    @property
    def clinical_trial_coordinating_center_name(self) -> Optional[str]:
        return self._dataset.get("ClinicalTrialCoordinatingCenterName")

    @clinical_trial_coordinating_center_name.setter
    def clinical_trial_coordinating_center_name(self, value: Optional[str]):
        if value is not None:
            self._dataset.ClinicalTrialCoordinatingCenterName = value

    @property
    def clinical_trial_series_id(self) -> Optional[str]:
        return self._dataset.get("ClinicalTrialSeriesID")

    @clinical_trial_series_id.setter
    def clinical_trial_series_id(self, value: Optional[str]):
        if value is not None:
            self._dataset.ClinicalTrialSeriesID = value

    @property
    def clinical_trial_series_description(self) -> Optional[str]:
        return self._dataset.get("ClinicalTrialSeriesDescription")

    @clinical_trial_series_description.setter
    def clinical_trial_series_description(self, value: Optional[str]):
        if value is not None:
            self._dataset.ClinicalTrialSeriesDescription = value

    # General Equipment Module
    @property
    def manufacturer(self) -> str:
        return self._dataset.get("Manufacturer", "")

    @manufacturer.setter
    def manufacturer(self, value: str):
        if value:
            self._dataset.Manufacturer = value

    @property
    def institution_name(self) -> Optional[str]:
        return self._dataset.get("InstitutionName")

    @institution_name.setter
    def institution_name(self, value: Optional[str]):
        if value is not None:
            self._dataset.InstitutionName = value

    @property
    def institution_address(self) -> Optional[str]:
        return self._dataset.get("InstitutionAddress")

    @institution_address.setter
    def institution_address(self, value: Optional[str]):
        if value is not None:
            self._dataset.InstitutionAddress = value

    @property
    def station_name(self) -> Optional[str]:
        return self._dataset.get("StationName")

    @station_name.setter
    def station_name(self, value: Optional[str]):
        if value is not None:
            self._dataset.StationName = value

    @property
    def institutional_department_name(self) -> Optional[str]:
        return self._dataset.get("InstitutionalDepartmentName")

    @institutional_department_name.setter
    def institutional_department_name(self, value: Optional[str]):
        if value is not None:
            self._dataset.InstitutionalDepartmentName = value

    @property
    def manufacturers_model_name(self) -> Optional[str]:
        return self._dataset.get("ManufacturersModelName")

    @manufacturers_model_name.setter
    def manufacturers_model_name(self, value: Optional[str]):
        if value is not None:
            self._dataset.ManufacturersModelName = value

    @property
    def device_serial_number(self) -> Optional[str]:
        return self._dataset.get("DeviceSerialNumber")

    @device_serial_number.setter
    def device_serial_number(self, value: Optional[str]):
        if value is not None:
            self._dataset.DeviceSerialNumber = value

    @property
    def software_versions(self) -> Optional[List[str]]:
        return self._dataset.get("SoftwareVersions")

    @software_versions.setter
    def software_versions(self, value: Optional[List[str]]):
        if value is not None:
            self._dataset.SoftwareVersions = value

    @property
    def beam_task_sequence(self) -> Optional[List[BeamTaskSequence]]:
        value = self._dataset.get("BeamTaskSequence")
        if value is None or len(value) == 0:
            return None
        return [BeamTaskSequence(x) for x in value]

    @beam_task_sequence.setter
    def beam_task_sequence(self, value: Optional[List[BeamTaskSequence]]):
        if value is not None:
            self._dataset.BeamTaskSequence = pydicom.Sequence([x.to_dataset() for x in value])

    @property
    def omitted_beam_task_sequence(self) -> Optional[List[OmittedBeamTaskSequence]]:
        value = self._dataset.get("BeamTaskSequence")
        if value is None or len(value) == 0:
            return None
        return [OmittedBeamTaskSequence(x) for x in value]

    @omitted_beam_task_sequence.setter
    def omitted_beam_task_sequence(self, value: Optional[List[OmittedBeamTaskSequence]]):
        if value is not None:
            self._dataset.OmittedBeamTaskSequence = pydicom.Sequence([x.to_dataset() for x in value])

    @property
    def referenced_rt_plan(self) -> Optional[List[ReferencedRTPlanSequenceItem]]:
        value = self._dataset.get("ReferencedRTPlanSequence")
        if value is None or len(value) == 0:
            return None
        return [ReferencedRTPlanSequenceItem(x) for x in value]

    @beam_task_sequence.setter
    def beam_task_sequence(self, value: Optional[List[ReferencedRTPlanSequenceItem]]):
        if value is not None:
            self._dataset.ReferencedRTPlanSequence = pydicom.Sequence([x.to_dataset() for x in value])

    def validate(self) -> List[str]:
        errors = []

        # Patient Module validation
        if not self.patients_name:
            errors.append("Patient's Name (Type 2) is missing or empty")
        if not self.patient_id:
            errors.append("Patient ID (Type 2) is missing or empty")

        # General Study Module validation
        if not self.study_instance_uid:
            errors.append("Study Instance UID (Type 1) is missing or empty")
        if "StudyDate" not in self._dataset:
            errors.append("Study Date (Type 2) is missing")
        if "StudyTime" not in self._dataset:
            errors.append("Study Time (Type 2) is missing")
        if "ReferringPhysiciansName" not in self._dataset:
            errors.append("Referring Physician's Name (Type 2) is missing")
        if "StudyID" not in self._dataset:
            errors.append("Study ID (Type 2) is missing")
        if "AccessionNumber" not in self._dataset:
            errors.append("Accession Number (Type 2) is missing")

        # RT Series Module validation
        if self.modality != "PLAN":
            errors.append("Modality (Type 1) must be 'PLAN'")
        if not self.series_instance_uid:
            errors.append("Series Instance UID (Type 1) is missing or empty")
        if "SeriesNumber" not in self._dataset:
            errors.append("Series Number (Type 2) is missing")

        # Frame of Reference Module validation
        if not self.frame_of_reference_uid:
            errors.append("Frame of Reference UID (Type 1) is missing or empty")

        # General Equipment Module validation
        if not self.manufacturer:
            errors.append("Manufacturer (Type 2) is missing or empty")

        # General RT Beams Delivery Instruction Module validation
        if self.instance_number == 0:
            errors.append("Instance Number (Type 1) is missing or zero")
        if not self.rt_beams_delivery_instruction_label:
            errors.append("RT Beams Delivery Instruction Label (Type 1) is missing or empty")

        return errors

    def to_dataset(self) -> Dataset:
        return self._dataset
