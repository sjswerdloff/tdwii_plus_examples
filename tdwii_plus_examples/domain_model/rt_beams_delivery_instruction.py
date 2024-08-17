from decimal import Decimal
from typing import Any, List, Optional

import pydicom

from .beam_task_sequence_item import BeamTaskSequenceItem
from .breed_registration_sequence_item import BreedRegistrationSequenceItem
from .code_sequence_item import CodeSequenceItem
from .coding_scheme_identification_sequence_item import (
    CodingSchemeIdentificationSequenceItem,
)
from .consent_for_clinical_trial_use_sequence_item import (
    ConsentForClinicalTrialUseSequenceItem,
)
from .consulting_physician_identification_sequence_item import (
    ConsultingPhysicianIdentificationSequenceItem,
)
from .context_group_identification_sequence_item import (
    ContextGroupIdentificationSequenceItem,
)
from .contributing_equipment_sequence_item import ContributingEquipmentSequenceItem
from .conversion_source_attributes_sequence_item import (
    ConversionSourceAttributesSequenceItem,
)
from .digital_signatures_sequence_item import DigitalSignaturesSequenceItem
from .encrypted_attributes_sequence_item import EncryptedAttributesSequenceItem
from .genetic_modifications_sequence_item import GeneticModificationsSequenceItem
from .group_of_patients_identification_sequence_item import (
    GroupOfPatientsIdentificationSequenceItem,
)
from .hl7_structured_document_reference_sequence_item import (
    HL7StructuredDocumentReferenceSequenceItem,
)
from .issuer_of_accession_number_sequence_item import (
    IssuerOfAccessionNumberSequenceItem,
)
from .issuer_of_admission_id_sequence_item import IssuerOfAdmissionIDSequenceItem
from .issuer_of_patient_id_qualifiers_sequence_item import (
    IssuerOfPatientIDQualifiersSequenceItem,
)
from .issuer_of_service_episode_id_sequence_item import (
    IssuerOfServiceEpisodeIDSequenceItem,
)
from .mac_parameters_sequence_item import MACParametersSequenceItem
from .mapping_resource_identification_sequence_item import (
    MappingResourceIdentificationSequenceItem,
)
from .omitted_beam_task_sequence_item import OmittedBeamTaskSequenceItem
from .operator_identification_sequence_item import OperatorIdentificationSequenceItem
from .original_attributes_sequence_item import OriginalAttributesSequenceItem
from .other_clinical_trial_protocol_i_ds_sequence_item import (
    OtherClinicalTrialProtocolIDsSequenceItem,
)
from .other_patient_i_ds_sequence_item import OtherPatientIDsSequenceItem
from .performing_physician_identification_sequence_item import (
    PerformingPhysicianIdentificationSequenceItem,
)
from .physicians_of_record_identification_sequence_item import (
    PhysiciansOfRecordIdentificationSequenceItem,
)
from .physicians_reading_study_identification_sequence_item import (
    PhysiciansReadingStudyIdentificationSequenceItem,
)
from .private_data_element_characteristics_sequence_item import (
    PrivateDataElementCharacteristicsSequenceItem,
)
from .referenced_defined_protocol_sequence_item import (
    ReferencedDefinedProtocolSequenceItem,
)
from .referenced_image_sequence_item import ReferencedImageSequenceItem
from .referenced_instance_sequence_item import ReferencedInstanceSequenceItem
from .referenced_patient_photo_sequence_item import ReferencedPatientPhotoSequenceItem
from .referenced_patient_sequence_item import ReferencedPatientSequenceItem
from .referenced_performed_procedure_step_sequence_item import (
    ReferencedPerformedProcedureStepSequenceItem,
)
from .referenced_performed_protocol_sequence_item import (
    ReferencedPerformedProtocolSequenceItem,
)
from .referenced_rt_plan_sequence_item import ReferencedRTPlanSequenceItem
from .referenced_series_sequence_item import ReferencedSeriesSequenceItem
from .referenced_study_sequence_item import ReferencedStudySequenceItem
from .referring_physician_identification_sequence_item import (
    ReferringPhysicianIdentificationSequenceItem,
)
from .related_series_sequence_item import RelatedSeriesSequenceItem
from .request_attributes_sequence_item import RequestAttributesSequenceItem
from .source_image_sequence_item import SourceImageSequenceItem
from .source_instance_sequence_item import SourceInstanceSequenceItem
from .source_patient_group_identification_sequence_item import (
    SourcePatientGroupIdentificationSequenceItem,
)
from .strain_stock_sequence_item import StrainStockSequenceItem
from .studies_containing_other_referenced_instances_sequence_item import (
    StudiesContainingOtherReferencedInstancesSequenceItem,
)
from .udi_sequence_item import UDISequenceItem


class RtBeamsDeliveryInstruction:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._CodingSchemeIdentificationSequence: List[CodingSchemeIdentificationSequenceItem] = []
        self._ContextGroupIdentificationSequence: List[ContextGroupIdentificationSequenceItem] = []
        self._MappingResourceIdentificationSequence: List[MappingResourceIdentificationSequenceItem] = []
        self._PrivateDataElementCharacteristicsSequence: List[PrivateDataElementCharacteristicsSequenceItem] = []
        self._ReferencedDefinedProtocolSequence: List[ReferencedDefinedProtocolSequenceItem] = []
        self._ReferencedPerformedProtocolSequence: List[ReferencedPerformedProtocolSequenceItem] = []
        self._ContributingEquipmentSequence: List[ContributingEquipmentSequenceItem] = []
        self._ConversionSourceAttributesSequence: List[ConversionSourceAttributesSequenceItem] = []
        self._HL7StructuredDocumentReferenceSequence: List[HL7StructuredDocumentReferenceSequenceItem] = []
        self._EncryptedAttributesSequence: List[EncryptedAttributesSequenceItem] = []
        self._OriginalAttributesSequence: List[OriginalAttributesSequenceItem] = []
        self._MACParametersSequence: List[MACParametersSequenceItem] = []
        self._DigitalSignaturesSequence: List[DigitalSignaturesSequenceItem] = []
        self._ReferencedImageSequence: List[ReferencedImageSequenceItem] = []
        self._ReferencedInstanceSequence: List[ReferencedInstanceSequenceItem] = []
        self._SourceImageSequence: List[SourceImageSequenceItem] = []
        self._DerivationCodeSequence: List[CodeSequenceItem] = []
        self._SourceInstanceSequence: List[SourceInstanceSequenceItem] = []
        self._ReferencedSeriesSequence: List[ReferencedSeriesSequenceItem] = []
        self._StudiesContainingOtherReferencedInstancesSequence: List[
            StudiesContainingOtherReferencedInstancesSequenceItem
        ] = []
        self._SeriesDescriptionCodeSequence: List[CodeSequenceItem] = []
        self._PerformingPhysicianIdentificationSequence: List[PerformingPhysicianIdentificationSequenceItem] = []
        self._OperatorIdentificationSequence: List[OperatorIdentificationSequenceItem] = []
        self._ReferencedPerformedProcedureStepSequence: List[ReferencedPerformedProcedureStepSequenceItem] = []
        self._RelatedSeriesSequence: List[RelatedSeriesSequenceItem] = []
        self._PerformedProtocolCodeSequence: List[CodeSequenceItem] = []
        self._RequestAttributesSequence: List[RequestAttributesSequenceItem] = []
        self._AdmittingDiagnosesCodeSequence: List[CodeSequenceItem] = []
        self._PatientSizeCodeSequence: List[CodeSequenceItem] = []
        self._ReasonForVisitCodeSequence: List[CodeSequenceItem] = []
        self._IssuerOfAdmissionIDSequence: List[IssuerOfAdmissionIDSequenceItem] = []
        self._IssuerOfServiceEpisodeIDSequence: List[IssuerOfServiceEpisodeIDSequenceItem] = []
        self._InstitutionalDepartmentTypeCodeSequence: List[CodeSequenceItem] = []
        self._UDISequence: List[UDISequenceItem] = []
        self._BeamTaskSequence: List[BeamTaskSequenceItem] = []
        self._ReferencedRTPlanSequence: List[ReferencedRTPlanSequenceItem] = []
        self._OmittedBeamTaskSequence: List[OmittedBeamTaskSequenceItem] = []
        self._ReferencedPatientSequence: List[ReferencedPatientSequenceItem] = []
        self._IssuerOfPatientIDQualifiersSequence: List[IssuerOfPatientIDQualifiersSequenceItem] = []
        self._SourcePatientGroupIdentificationSequence: List[SourcePatientGroupIdentificationSequenceItem] = []
        self._GroupOfPatientsIdentificationSequence: List[GroupOfPatientsIdentificationSequenceItem] = []
        self._StrainStockSequence: List[StrainStockSequenceItem] = []
        self._StrainCodeSequence: List[CodeSequenceItem] = []
        self._GeneticModificationsSequence: List[GeneticModificationsSequenceItem] = []
        self._OtherPatientIDsSequence: List[OtherPatientIDsSequenceItem] = []
        self._ReferencedPatientPhotoSequence: List[ReferencedPatientPhotoSequenceItem] = []
        self._PatientSpeciesCodeSequence: List[CodeSequenceItem] = []
        self._PatientBreedCodeSequence: List[CodeSequenceItem] = []
        self._BreedRegistrationSequence: List[BreedRegistrationSequenceItem] = []
        self._DeidentificationMethodCodeSequence: List[CodeSequenceItem] = []
        self._ClinicalTrialTimePointTypeCodeSequence: List[CodeSequenceItem] = []
        self._ConsentForClinicalTrialUseSequence: List[ConsentForClinicalTrialUseSequenceItem] = []
        self._IssuerOfAccessionNumberSequence: List[IssuerOfAccessionNumberSequenceItem] = []
        self._ReferringPhysicianIdentificationSequence: List[ReferringPhysicianIdentificationSequenceItem] = []
        self._ConsultingPhysicianIdentificationSequence: List[ConsultingPhysicianIdentificationSequenceItem] = []
        self._ProcedureCodeSequence: List[CodeSequenceItem] = []
        self._PhysiciansOfRecordIdentificationSequence: List[PhysiciansOfRecordIdentificationSequenceItem] = []
        self._PhysiciansReadingStudyIdentificationSequence: List[PhysiciansReadingStudyIdentificationSequenceItem] = []
        self._ReferencedStudySequence: List[ReferencedStudySequenceItem] = []
        self._RequestingServiceCodeSequence: List[CodeSequenceItem] = []
        self._ReasonForPerformedProcedureCodeSequence: List[CodeSequenceItem] = []
        self._OtherClinicalTrialProtocolIDsSequence: List[OtherClinicalTrialProtocolIDsSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def SpecificCharacterSet(self) -> Optional[List[str]]:
        if "SpecificCharacterSet" in self._dataset:
            return self._dataset.SpecificCharacterSet
        return None

    @SpecificCharacterSet.setter
    def SpecificCharacterSet(self, value: Optional[List[str]]):
        if value is None:
            if "SpecificCharacterSet" in self._dataset:
                del self._dataset.SpecificCharacterSet
        else:
            self._dataset.SpecificCharacterSet = value

    @property
    def InstanceCreationDate(self) -> Optional[str]:
        if "InstanceCreationDate" in self._dataset:
            return self._dataset.InstanceCreationDate
        return None

    @InstanceCreationDate.setter
    def InstanceCreationDate(self, value: Optional[str]):
        if value is None:
            if "InstanceCreationDate" in self._dataset:
                del self._dataset.InstanceCreationDate
        else:
            self._dataset.InstanceCreationDate = value

    @property
    def InstanceCreationTime(self) -> Optional[str]:
        if "InstanceCreationTime" in self._dataset:
            return self._dataset.InstanceCreationTime
        return None

    @InstanceCreationTime.setter
    def InstanceCreationTime(self, value: Optional[str]):
        if value is None:
            if "InstanceCreationTime" in self._dataset:
                del self._dataset.InstanceCreationTime
        else:
            self._dataset.InstanceCreationTime = value

    @property
    def InstanceCreatorUID(self) -> Optional[str]:
        if "InstanceCreatorUID" in self._dataset:
            return self._dataset.InstanceCreatorUID
        return None

    @InstanceCreatorUID.setter
    def InstanceCreatorUID(self, value: Optional[str]):
        if value is None:
            if "InstanceCreatorUID" in self._dataset:
                del self._dataset.InstanceCreatorUID
        else:
            self._dataset.InstanceCreatorUID = value

    @property
    def InstanceCoercionDateTime(self) -> Optional[str]:
        if "InstanceCoercionDateTime" in self._dataset:
            return self._dataset.InstanceCoercionDateTime
        return None

    @InstanceCoercionDateTime.setter
    def InstanceCoercionDateTime(self, value: Optional[str]):
        if value is None:
            if "InstanceCoercionDateTime" in self._dataset:
                del self._dataset.InstanceCoercionDateTime
        else:
            self._dataset.InstanceCoercionDateTime = value

    @property
    def SOPClassUID(self) -> Optional[str]:
        if "SOPClassUID" in self._dataset:
            return self._dataset.SOPClassUID
        return None

    @SOPClassUID.setter
    def SOPClassUID(self, value: Optional[str]):
        if value is None:
            if "SOPClassUID" in self._dataset:
                del self._dataset.SOPClassUID
        else:
            self._dataset.SOPClassUID = value

    @property
    def SOPInstanceUID(self) -> Optional[str]:
        if "SOPInstanceUID" in self._dataset:
            return self._dataset.SOPInstanceUID
        return None

    @SOPInstanceUID.setter
    def SOPInstanceUID(self, value: Optional[str]):
        if value is None:
            if "SOPInstanceUID" in self._dataset:
                del self._dataset.SOPInstanceUID
        else:
            self._dataset.SOPInstanceUID = value

    @property
    def RelatedGeneralSOPClassUID(self) -> Optional[List[str]]:
        if "RelatedGeneralSOPClassUID" in self._dataset:
            return self._dataset.RelatedGeneralSOPClassUID
        return None

    @RelatedGeneralSOPClassUID.setter
    def RelatedGeneralSOPClassUID(self, value: Optional[List[str]]):
        if value is None:
            if "RelatedGeneralSOPClassUID" in self._dataset:
                del self._dataset.RelatedGeneralSOPClassUID
        else:
            self._dataset.RelatedGeneralSOPClassUID = value

    @property
    def OriginalSpecializedSOPClassUID(self) -> Optional[str]:
        if "OriginalSpecializedSOPClassUID" in self._dataset:
            return self._dataset.OriginalSpecializedSOPClassUID
        return None

    @OriginalSpecializedSOPClassUID.setter
    def OriginalSpecializedSOPClassUID(self, value: Optional[str]):
        if value is None:
            if "OriginalSpecializedSOPClassUID" in self._dataset:
                del self._dataset.OriginalSpecializedSOPClassUID
        else:
            self._dataset.OriginalSpecializedSOPClassUID = value

    @property
    def SyntheticData(self) -> Optional[str]:
        if "SyntheticData" in self._dataset:
            return self._dataset.SyntheticData
        return None

    @SyntheticData.setter
    def SyntheticData(self, value: Optional[str]):
        if value is None:
            if "SyntheticData" in self._dataset:
                del self._dataset.SyntheticData
        else:
            self._dataset.SyntheticData = value

    @property
    def QueryRetrieveView(self) -> Optional[str]:
        if "QueryRetrieveView" in self._dataset:
            return self._dataset.QueryRetrieveView
        return None

    @QueryRetrieveView.setter
    def QueryRetrieveView(self, value: Optional[str]):
        if value is None:
            if "QueryRetrieveView" in self._dataset:
                del self._dataset.QueryRetrieveView
        else:
            self._dataset.QueryRetrieveView = value

    @property
    def CodingSchemeIdentificationSequence(self) -> Optional[List[CodingSchemeIdentificationSequenceItem]]:
        if "CodingSchemeIdentificationSequence" in self._dataset:
            if len(self._CodingSchemeIdentificationSequence) == len(self._dataset.CodingSchemeIdentificationSequence):
                return self._CodingSchemeIdentificationSequence
            else:
                return [CodingSchemeIdentificationSequenceItem(x) for x in self._dataset.CodingSchemeIdentificationSequence]
        return None

    @CodingSchemeIdentificationSequence.setter
    def CodingSchemeIdentificationSequence(self, value: Optional[List[CodingSchemeIdentificationSequenceItem]]):
        if value is None:
            self._CodingSchemeIdentificationSequence = []
            if "CodingSchemeIdentificationSequence" in self._dataset:
                del self._dataset.CodingSchemeIdentificationSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, CodingSchemeIdentificationSequenceItem) for item in value
        ):
            raise ValueError(
                f"CodingSchemeIdentificationSequence must be a list of CodingSchemeIdentificationSequenceItem objects"
            )
        else:
            self._CodingSchemeIdentificationSequence = value
            if "CodingSchemeIdentificationSequence" not in self._dataset:
                self._dataset.CodingSchemeIdentificationSequence = pydicom.Sequence()
            self._dataset.CodingSchemeIdentificationSequence.clear()
            self._dataset.CodingSchemeIdentificationSequence.extend([item.to_dataset() for item in value])

    def add_CodingSchemeIdentification(self, item: CodingSchemeIdentificationSequenceItem):
        if not isinstance(item, CodingSchemeIdentificationSequenceItem):
            raise ValueError(f"Item must be an instance of CodingSchemeIdentificationSequenceItem")
        self._CodingSchemeIdentificationSequence.append(item)
        if "CodingSchemeIdentificationSequence" not in self._dataset:
            self._dataset.CodingSchemeIdentificationSequence = pydicom.Sequence()
        self._dataset.CodingSchemeIdentificationSequence.append(item.to_dataset())

    @property
    def ContextGroupIdentificationSequence(self) -> Optional[List[ContextGroupIdentificationSequenceItem]]:
        if "ContextGroupIdentificationSequence" in self._dataset:
            if len(self._ContextGroupIdentificationSequence) == len(self._dataset.ContextGroupIdentificationSequence):
                return self._ContextGroupIdentificationSequence
            else:
                return [ContextGroupIdentificationSequenceItem(x) for x in self._dataset.ContextGroupIdentificationSequence]
        return None

    @ContextGroupIdentificationSequence.setter
    def ContextGroupIdentificationSequence(self, value: Optional[List[ContextGroupIdentificationSequenceItem]]):
        if value is None:
            self._ContextGroupIdentificationSequence = []
            if "ContextGroupIdentificationSequence" in self._dataset:
                del self._dataset.ContextGroupIdentificationSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, ContextGroupIdentificationSequenceItem) for item in value
        ):
            raise ValueError(
                f"ContextGroupIdentificationSequence must be a list of ContextGroupIdentificationSequenceItem objects"
            )
        else:
            self._ContextGroupIdentificationSequence = value
            if "ContextGroupIdentificationSequence" not in self._dataset:
                self._dataset.ContextGroupIdentificationSequence = pydicom.Sequence()
            self._dataset.ContextGroupIdentificationSequence.clear()
            self._dataset.ContextGroupIdentificationSequence.extend([item.to_dataset() for item in value])

    def add_ContextGroupIdentification(self, item: ContextGroupIdentificationSequenceItem):
        if not isinstance(item, ContextGroupIdentificationSequenceItem):
            raise ValueError(f"Item must be an instance of ContextGroupIdentificationSequenceItem")
        self._ContextGroupIdentificationSequence.append(item)
        if "ContextGroupIdentificationSequence" not in self._dataset:
            self._dataset.ContextGroupIdentificationSequence = pydicom.Sequence()
        self._dataset.ContextGroupIdentificationSequence.append(item.to_dataset())

    @property
    def MappingResourceIdentificationSequence(self) -> Optional[List[MappingResourceIdentificationSequenceItem]]:
        if "MappingResourceIdentificationSequence" in self._dataset:
            if len(self._MappingResourceIdentificationSequence) == len(self._dataset.MappingResourceIdentificationSequence):
                return self._MappingResourceIdentificationSequence
            else:
                return [
                    MappingResourceIdentificationSequenceItem(x) for x in self._dataset.MappingResourceIdentificationSequence
                ]
        return None

    @MappingResourceIdentificationSequence.setter
    def MappingResourceIdentificationSequence(self, value: Optional[List[MappingResourceIdentificationSequenceItem]]):
        if value is None:
            self._MappingResourceIdentificationSequence = []
            if "MappingResourceIdentificationSequence" in self._dataset:
                del self._dataset.MappingResourceIdentificationSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, MappingResourceIdentificationSequenceItem) for item in value
        ):
            raise ValueError(
                f"MappingResourceIdentificationSequence must be a list of MappingResourceIdentificationSequenceItem objects"
            )
        else:
            self._MappingResourceIdentificationSequence = value
            if "MappingResourceIdentificationSequence" not in self._dataset:
                self._dataset.MappingResourceIdentificationSequence = pydicom.Sequence()
            self._dataset.MappingResourceIdentificationSequence.clear()
            self._dataset.MappingResourceIdentificationSequence.extend([item.to_dataset() for item in value])

    def add_MappingResourceIdentification(self, item: MappingResourceIdentificationSequenceItem):
        if not isinstance(item, MappingResourceIdentificationSequenceItem):
            raise ValueError(f"Item must be an instance of MappingResourceIdentificationSequenceItem")
        self._MappingResourceIdentificationSequence.append(item)
        if "MappingResourceIdentificationSequence" not in self._dataset:
            self._dataset.MappingResourceIdentificationSequence = pydicom.Sequence()
        self._dataset.MappingResourceIdentificationSequence.append(item.to_dataset())

    @property
    def TimezoneOffsetFromUTC(self) -> Optional[str]:
        if "TimezoneOffsetFromUTC" in self._dataset:
            return self._dataset.TimezoneOffsetFromUTC
        return None

    @TimezoneOffsetFromUTC.setter
    def TimezoneOffsetFromUTC(self, value: Optional[str]):
        if value is None:
            if "TimezoneOffsetFromUTC" in self._dataset:
                del self._dataset.TimezoneOffsetFromUTC
        else:
            self._dataset.TimezoneOffsetFromUTC = value

    @property
    def PrivateDataElementCharacteristicsSequence(self) -> Optional[List[PrivateDataElementCharacteristicsSequenceItem]]:
        if "PrivateDataElementCharacteristicsSequence" in self._dataset:
            if len(self._PrivateDataElementCharacteristicsSequence) == len(
                self._dataset.PrivateDataElementCharacteristicsSequence
            ):
                return self._PrivateDataElementCharacteristicsSequence
            else:
                return [
                    PrivateDataElementCharacteristicsSequenceItem(x)
                    for x in self._dataset.PrivateDataElementCharacteristicsSequence
                ]
        return None

    @PrivateDataElementCharacteristicsSequence.setter
    def PrivateDataElementCharacteristicsSequence(self, value: Optional[List[PrivateDataElementCharacteristicsSequenceItem]]):
        if value is None:
            self._PrivateDataElementCharacteristicsSequence = []
            if "PrivateDataElementCharacteristicsSequence" in self._dataset:
                del self._dataset.PrivateDataElementCharacteristicsSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, PrivateDataElementCharacteristicsSequenceItem) for item in value
        ):
            raise ValueError(
                f"PrivateDataElementCharacteristicsSequence must be a list of PrivateDataElementCharacteristicsSequenceItem objects"
            )
        else:
            self._PrivateDataElementCharacteristicsSequence = value
            if "PrivateDataElementCharacteristicsSequence" not in self._dataset:
                self._dataset.PrivateDataElementCharacteristicsSequence = pydicom.Sequence()
            self._dataset.PrivateDataElementCharacteristicsSequence.clear()
            self._dataset.PrivateDataElementCharacteristicsSequence.extend([item.to_dataset() for item in value])

    def add_PrivateDataElementCharacteristics(self, item: PrivateDataElementCharacteristicsSequenceItem):
        if not isinstance(item, PrivateDataElementCharacteristicsSequenceItem):
            raise ValueError(f"Item must be an instance of PrivateDataElementCharacteristicsSequenceItem")
        self._PrivateDataElementCharacteristicsSequence.append(item)
        if "PrivateDataElementCharacteristicsSequence" not in self._dataset:
            self._dataset.PrivateDataElementCharacteristicsSequence = pydicom.Sequence()
        self._dataset.PrivateDataElementCharacteristicsSequence.append(item.to_dataset())

    @property
    def ContentQualification(self) -> Optional[str]:
        if "ContentQualification" in self._dataset:
            return self._dataset.ContentQualification
        return None

    @ContentQualification.setter
    def ContentQualification(self, value: Optional[str]):
        if value is None:
            if "ContentQualification" in self._dataset:
                del self._dataset.ContentQualification
        else:
            self._dataset.ContentQualification = value

    @property
    def ReferencedDefinedProtocolSequence(self) -> Optional[List[ReferencedDefinedProtocolSequenceItem]]:
        if "ReferencedDefinedProtocolSequence" in self._dataset:
            if len(self._ReferencedDefinedProtocolSequence) == len(self._dataset.ReferencedDefinedProtocolSequence):
                return self._ReferencedDefinedProtocolSequence
            else:
                return [ReferencedDefinedProtocolSequenceItem(x) for x in self._dataset.ReferencedDefinedProtocolSequence]
        return None

    @ReferencedDefinedProtocolSequence.setter
    def ReferencedDefinedProtocolSequence(self, value: Optional[List[ReferencedDefinedProtocolSequenceItem]]):
        if value is None:
            self._ReferencedDefinedProtocolSequence = []
            if "ReferencedDefinedProtocolSequence" in self._dataset:
                del self._dataset.ReferencedDefinedProtocolSequence
        elif not isinstance(value, list) or not all(isinstance(item, ReferencedDefinedProtocolSequenceItem) for item in value):
            raise ValueError(
                f"ReferencedDefinedProtocolSequence must be a list of ReferencedDefinedProtocolSequenceItem objects"
            )
        else:
            self._ReferencedDefinedProtocolSequence = value
            if "ReferencedDefinedProtocolSequence" not in self._dataset:
                self._dataset.ReferencedDefinedProtocolSequence = pydicom.Sequence()
            self._dataset.ReferencedDefinedProtocolSequence.clear()
            self._dataset.ReferencedDefinedProtocolSequence.extend([item.to_dataset() for item in value])

    def add_ReferencedDefinedProtocol(self, item: ReferencedDefinedProtocolSequenceItem):
        if not isinstance(item, ReferencedDefinedProtocolSequenceItem):
            raise ValueError(f"Item must be an instance of ReferencedDefinedProtocolSequenceItem")
        self._ReferencedDefinedProtocolSequence.append(item)
        if "ReferencedDefinedProtocolSequence" not in self._dataset:
            self._dataset.ReferencedDefinedProtocolSequence = pydicom.Sequence()
        self._dataset.ReferencedDefinedProtocolSequence.append(item.to_dataset())

    @property
    def ReferencedPerformedProtocolSequence(self) -> Optional[List[ReferencedPerformedProtocolSequenceItem]]:
        if "ReferencedPerformedProtocolSequence" in self._dataset:
            if len(self._ReferencedPerformedProtocolSequence) == len(self._dataset.ReferencedPerformedProtocolSequence):
                return self._ReferencedPerformedProtocolSequence
            else:
                return [ReferencedPerformedProtocolSequenceItem(x) for x in self._dataset.ReferencedPerformedProtocolSequence]
        return None

    @ReferencedPerformedProtocolSequence.setter
    def ReferencedPerformedProtocolSequence(self, value: Optional[List[ReferencedPerformedProtocolSequenceItem]]):
        if value is None:
            self._ReferencedPerformedProtocolSequence = []
            if "ReferencedPerformedProtocolSequence" in self._dataset:
                del self._dataset.ReferencedPerformedProtocolSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, ReferencedPerformedProtocolSequenceItem) for item in value
        ):
            raise ValueError(
                f"ReferencedPerformedProtocolSequence must be a list of ReferencedPerformedProtocolSequenceItem objects"
            )
        else:
            self._ReferencedPerformedProtocolSequence = value
            if "ReferencedPerformedProtocolSequence" not in self._dataset:
                self._dataset.ReferencedPerformedProtocolSequence = pydicom.Sequence()
            self._dataset.ReferencedPerformedProtocolSequence.clear()
            self._dataset.ReferencedPerformedProtocolSequence.extend([item.to_dataset() for item in value])

    def add_ReferencedPerformedProtocol(self, item: ReferencedPerformedProtocolSequenceItem):
        if not isinstance(item, ReferencedPerformedProtocolSequenceItem):
            raise ValueError(f"Item must be an instance of ReferencedPerformedProtocolSequenceItem")
        self._ReferencedPerformedProtocolSequence.append(item)
        if "ReferencedPerformedProtocolSequence" not in self._dataset:
            self._dataset.ReferencedPerformedProtocolSequence = pydicom.Sequence()
        self._dataset.ReferencedPerformedProtocolSequence.append(item.to_dataset())

    @property
    def ContributingEquipmentSequence(self) -> Optional[List[ContributingEquipmentSequenceItem]]:
        if "ContributingEquipmentSequence" in self._dataset:
            if len(self._ContributingEquipmentSequence) == len(self._dataset.ContributingEquipmentSequence):
                return self._ContributingEquipmentSequence
            else:
                return [ContributingEquipmentSequenceItem(x) for x in self._dataset.ContributingEquipmentSequence]
        return None

    @ContributingEquipmentSequence.setter
    def ContributingEquipmentSequence(self, value: Optional[List[ContributingEquipmentSequenceItem]]):
        if value is None:
            self._ContributingEquipmentSequence = []
            if "ContributingEquipmentSequence" in self._dataset:
                del self._dataset.ContributingEquipmentSequence
        elif not isinstance(value, list) or not all(isinstance(item, ContributingEquipmentSequenceItem) for item in value):
            raise ValueError(f"ContributingEquipmentSequence must be a list of ContributingEquipmentSequenceItem objects")
        else:
            self._ContributingEquipmentSequence = value
            if "ContributingEquipmentSequence" not in self._dataset:
                self._dataset.ContributingEquipmentSequence = pydicom.Sequence()
            self._dataset.ContributingEquipmentSequence.clear()
            self._dataset.ContributingEquipmentSequence.extend([item.to_dataset() for item in value])

    def add_ContributingEquipment(self, item: ContributingEquipmentSequenceItem):
        if not isinstance(item, ContributingEquipmentSequenceItem):
            raise ValueError(f"Item must be an instance of ContributingEquipmentSequenceItem")
        self._ContributingEquipmentSequence.append(item)
        if "ContributingEquipmentSequence" not in self._dataset:
            self._dataset.ContributingEquipmentSequence = pydicom.Sequence()
        self._dataset.ContributingEquipmentSequence.append(item.to_dataset())

    @property
    def InstanceNumber(self) -> Optional[int]:
        if "InstanceNumber" in self._dataset:
            return self._dataset.InstanceNumber
        return None

    @InstanceNumber.setter
    def InstanceNumber(self, value: Optional[int]):
        if value is None:
            if "InstanceNumber" in self._dataset:
                del self._dataset.InstanceNumber
        else:
            self._dataset.InstanceNumber = value

    @property
    def ConversionSourceAttributesSequence(self) -> Optional[List[ConversionSourceAttributesSequenceItem]]:
        if "ConversionSourceAttributesSequence" in self._dataset:
            if len(self._ConversionSourceAttributesSequence) == len(self._dataset.ConversionSourceAttributesSequence):
                return self._ConversionSourceAttributesSequence
            else:
                return [ConversionSourceAttributesSequenceItem(x) for x in self._dataset.ConversionSourceAttributesSequence]
        return None

    @ConversionSourceAttributesSequence.setter
    def ConversionSourceAttributesSequence(self, value: Optional[List[ConversionSourceAttributesSequenceItem]]):
        if value is None:
            self._ConversionSourceAttributesSequence = []
            if "ConversionSourceAttributesSequence" in self._dataset:
                del self._dataset.ConversionSourceAttributesSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, ConversionSourceAttributesSequenceItem) for item in value
        ):
            raise ValueError(
                f"ConversionSourceAttributesSequence must be a list of ConversionSourceAttributesSequenceItem objects"
            )
        else:
            self._ConversionSourceAttributesSequence = value
            if "ConversionSourceAttributesSequence" not in self._dataset:
                self._dataset.ConversionSourceAttributesSequence = pydicom.Sequence()
            self._dataset.ConversionSourceAttributesSequence.clear()
            self._dataset.ConversionSourceAttributesSequence.extend([item.to_dataset() for item in value])

    def add_ConversionSourceAttributes(self, item: ConversionSourceAttributesSequenceItem):
        if not isinstance(item, ConversionSourceAttributesSequenceItem):
            raise ValueError(f"Item must be an instance of ConversionSourceAttributesSequenceItem")
        self._ConversionSourceAttributesSequence.append(item)
        if "ConversionSourceAttributesSequence" not in self._dataset:
            self._dataset.ConversionSourceAttributesSequence = pydicom.Sequence()
        self._dataset.ConversionSourceAttributesSequence.append(item.to_dataset())

    @property
    def LongitudinalTemporalInformationModified(self) -> Optional[str]:
        if "LongitudinalTemporalInformationModified" in self._dataset:
            return self._dataset.LongitudinalTemporalInformationModified
        return None

    @LongitudinalTemporalInformationModified.setter
    def LongitudinalTemporalInformationModified(self, value: Optional[str]):
        if value is None:
            if "LongitudinalTemporalInformationModified" in self._dataset:
                del self._dataset.LongitudinalTemporalInformationModified
        else:
            self._dataset.LongitudinalTemporalInformationModified = value

    @property
    def HL7StructuredDocumentReferenceSequence(self) -> Optional[List[HL7StructuredDocumentReferenceSequenceItem]]:
        if "HL7StructuredDocumentReferenceSequence" in self._dataset:
            if len(self._HL7StructuredDocumentReferenceSequence) == len(self._dataset.HL7StructuredDocumentReferenceSequence):
                return self._HL7StructuredDocumentReferenceSequence
            else:
                return [
                    HL7StructuredDocumentReferenceSequenceItem(x) for x in self._dataset.HL7StructuredDocumentReferenceSequence
                ]
        return None

    @HL7StructuredDocumentReferenceSequence.setter
    def HL7StructuredDocumentReferenceSequence(self, value: Optional[List[HL7StructuredDocumentReferenceSequenceItem]]):
        if value is None:
            self._HL7StructuredDocumentReferenceSequence = []
            if "HL7StructuredDocumentReferenceSequence" in self._dataset:
                del self._dataset.HL7StructuredDocumentReferenceSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, HL7StructuredDocumentReferenceSequenceItem) for item in value
        ):
            raise ValueError(
                f"HL7StructuredDocumentReferenceSequence must be a list of HL7StructuredDocumentReferenceSequenceItem objects"
            )
        else:
            self._HL7StructuredDocumentReferenceSequence = value
            if "HL7StructuredDocumentReferenceSequence" not in self._dataset:
                self._dataset.HL7StructuredDocumentReferenceSequence = pydicom.Sequence()
            self._dataset.HL7StructuredDocumentReferenceSequence.clear()
            self._dataset.HL7StructuredDocumentReferenceSequence.extend([item.to_dataset() for item in value])

    def add_HL7StructuredDocumentReference(self, item: HL7StructuredDocumentReferenceSequenceItem):
        if not isinstance(item, HL7StructuredDocumentReferenceSequenceItem):
            raise ValueError(f"Item must be an instance of HL7StructuredDocumentReferenceSequenceItem")
        self._HL7StructuredDocumentReferenceSequence.append(item)
        if "HL7StructuredDocumentReferenceSequence" not in self._dataset:
            self._dataset.HL7StructuredDocumentReferenceSequence = pydicom.Sequence()
        self._dataset.HL7StructuredDocumentReferenceSequence.append(item.to_dataset())

    @property
    def SOPInstanceStatus(self) -> Optional[str]:
        if "SOPInstanceStatus" in self._dataset:
            return self._dataset.SOPInstanceStatus
        return None

    @SOPInstanceStatus.setter
    def SOPInstanceStatus(self, value: Optional[str]):
        if value is None:
            if "SOPInstanceStatus" in self._dataset:
                del self._dataset.SOPInstanceStatus
        else:
            self._dataset.SOPInstanceStatus = value

    @property
    def SOPAuthorizationDateTime(self) -> Optional[str]:
        if "SOPAuthorizationDateTime" in self._dataset:
            return self._dataset.SOPAuthorizationDateTime
        return None

    @SOPAuthorizationDateTime.setter
    def SOPAuthorizationDateTime(self, value: Optional[str]):
        if value is None:
            if "SOPAuthorizationDateTime" in self._dataset:
                del self._dataset.SOPAuthorizationDateTime
        else:
            self._dataset.SOPAuthorizationDateTime = value

    @property
    def SOPAuthorizationComment(self) -> Optional[str]:
        if "SOPAuthorizationComment" in self._dataset:
            return self._dataset.SOPAuthorizationComment
        return None

    @SOPAuthorizationComment.setter
    def SOPAuthorizationComment(self, value: Optional[str]):
        if value is None:
            if "SOPAuthorizationComment" in self._dataset:
                del self._dataset.SOPAuthorizationComment
        else:
            self._dataset.SOPAuthorizationComment = value

    @property
    def AuthorizationEquipmentCertificationNumber(self) -> Optional[str]:
        if "AuthorizationEquipmentCertificationNumber" in self._dataset:
            return self._dataset.AuthorizationEquipmentCertificationNumber
        return None

    @AuthorizationEquipmentCertificationNumber.setter
    def AuthorizationEquipmentCertificationNumber(self, value: Optional[str]):
        if value is None:
            if "AuthorizationEquipmentCertificationNumber" in self._dataset:
                del self._dataset.AuthorizationEquipmentCertificationNumber
        else:
            self._dataset.AuthorizationEquipmentCertificationNumber = value

    @property
    def EncryptedAttributesSequence(self) -> Optional[List[EncryptedAttributesSequenceItem]]:
        if "EncryptedAttributesSequence" in self._dataset:
            if len(self._EncryptedAttributesSequence) == len(self._dataset.EncryptedAttributesSequence):
                return self._EncryptedAttributesSequence
            else:
                return [EncryptedAttributesSequenceItem(x) for x in self._dataset.EncryptedAttributesSequence]
        return None

    @EncryptedAttributesSequence.setter
    def EncryptedAttributesSequence(self, value: Optional[List[EncryptedAttributesSequenceItem]]):
        if value is None:
            self._EncryptedAttributesSequence = []
            if "EncryptedAttributesSequence" in self._dataset:
                del self._dataset.EncryptedAttributesSequence
        elif not isinstance(value, list) or not all(isinstance(item, EncryptedAttributesSequenceItem) for item in value):
            raise ValueError(f"EncryptedAttributesSequence must be a list of EncryptedAttributesSequenceItem objects")
        else:
            self._EncryptedAttributesSequence = value
            if "EncryptedAttributesSequence" not in self._dataset:
                self._dataset.EncryptedAttributesSequence = pydicom.Sequence()
            self._dataset.EncryptedAttributesSequence.clear()
            self._dataset.EncryptedAttributesSequence.extend([item.to_dataset() for item in value])

    def add_EncryptedAttributes(self, item: EncryptedAttributesSequenceItem):
        if not isinstance(item, EncryptedAttributesSequenceItem):
            raise ValueError(f"Item must be an instance of EncryptedAttributesSequenceItem")
        self._EncryptedAttributesSequence.append(item)
        if "EncryptedAttributesSequence" not in self._dataset:
            self._dataset.EncryptedAttributesSequence = pydicom.Sequence()
        self._dataset.EncryptedAttributesSequence.append(item.to_dataset())

    @property
    def OriginalAttributesSequence(self) -> Optional[List[OriginalAttributesSequenceItem]]:
        if "OriginalAttributesSequence" in self._dataset:
            if len(self._OriginalAttributesSequence) == len(self._dataset.OriginalAttributesSequence):
                return self._OriginalAttributesSequence
            else:
                return [OriginalAttributesSequenceItem(x) for x in self._dataset.OriginalAttributesSequence]
        return None

    @OriginalAttributesSequence.setter
    def OriginalAttributesSequence(self, value: Optional[List[OriginalAttributesSequenceItem]]):
        if value is None:
            self._OriginalAttributesSequence = []
            if "OriginalAttributesSequence" in self._dataset:
                del self._dataset.OriginalAttributesSequence
        elif not isinstance(value, list) or not all(isinstance(item, OriginalAttributesSequenceItem) for item in value):
            raise ValueError(f"OriginalAttributesSequence must be a list of OriginalAttributesSequenceItem objects")
        else:
            self._OriginalAttributesSequence = value
            if "OriginalAttributesSequence" not in self._dataset:
                self._dataset.OriginalAttributesSequence = pydicom.Sequence()
            self._dataset.OriginalAttributesSequence.clear()
            self._dataset.OriginalAttributesSequence.extend([item.to_dataset() for item in value])

    def add_OriginalAttributes(self, item: OriginalAttributesSequenceItem):
        if not isinstance(item, OriginalAttributesSequenceItem):
            raise ValueError(f"Item must be an instance of OriginalAttributesSequenceItem")
        self._OriginalAttributesSequence.append(item)
        if "OriginalAttributesSequence" not in self._dataset:
            self._dataset.OriginalAttributesSequence = pydicom.Sequence()
        self._dataset.OriginalAttributesSequence.append(item.to_dataset())

    @property
    def InstanceOriginStatus(self) -> Optional[str]:
        if "InstanceOriginStatus" in self._dataset:
            return self._dataset.InstanceOriginStatus
        return None

    @InstanceOriginStatus.setter
    def InstanceOriginStatus(self, value: Optional[str]):
        if value is None:
            if "InstanceOriginStatus" in self._dataset:
                del self._dataset.InstanceOriginStatus
        else:
            self._dataset.InstanceOriginStatus = value

    @property
    def BarcodeValue(self) -> Optional[str]:
        if "BarcodeValue" in self._dataset:
            return self._dataset.BarcodeValue
        return None

    @BarcodeValue.setter
    def BarcodeValue(self, value: Optional[str]):
        if value is None:
            if "BarcodeValue" in self._dataset:
                del self._dataset.BarcodeValue
        else:
            self._dataset.BarcodeValue = value

    @property
    def MACParametersSequence(self) -> Optional[List[MACParametersSequenceItem]]:
        if "MACParametersSequence" in self._dataset:
            if len(self._MACParametersSequence) == len(self._dataset.MACParametersSequence):
                return self._MACParametersSequence
            else:
                return [MACParametersSequenceItem(x) for x in self._dataset.MACParametersSequence]
        return None

    @MACParametersSequence.setter
    def MACParametersSequence(self, value: Optional[List[MACParametersSequenceItem]]):
        if value is None:
            self._MACParametersSequence = []
            if "MACParametersSequence" in self._dataset:
                del self._dataset.MACParametersSequence
        elif not isinstance(value, list) or not all(isinstance(item, MACParametersSequenceItem) for item in value):
            raise ValueError(f"MACParametersSequence must be a list of MACParametersSequenceItem objects")
        else:
            self._MACParametersSequence = value
            if "MACParametersSequence" not in self._dataset:
                self._dataset.MACParametersSequence = pydicom.Sequence()
            self._dataset.MACParametersSequence.clear()
            self._dataset.MACParametersSequence.extend([item.to_dataset() for item in value])

    def add_MACParameters(self, item: MACParametersSequenceItem):
        if not isinstance(item, MACParametersSequenceItem):
            raise ValueError(f"Item must be an instance of MACParametersSequenceItem")
        self._MACParametersSequence.append(item)
        if "MACParametersSequence" not in self._dataset:
            self._dataset.MACParametersSequence = pydicom.Sequence()
        self._dataset.MACParametersSequence.append(item.to_dataset())

    @property
    def DigitalSignaturesSequence(self) -> Optional[List[DigitalSignaturesSequenceItem]]:
        if "DigitalSignaturesSequence" in self._dataset:
            if len(self._DigitalSignaturesSequence) == len(self._dataset.DigitalSignaturesSequence):
                return self._DigitalSignaturesSequence
            else:
                return [DigitalSignaturesSequenceItem(x) for x in self._dataset.DigitalSignaturesSequence]
        return None

    @DigitalSignaturesSequence.setter
    def DigitalSignaturesSequence(self, value: Optional[List[DigitalSignaturesSequenceItem]]):
        if value is None:
            self._DigitalSignaturesSequence = []
            if "DigitalSignaturesSequence" in self._dataset:
                del self._dataset.DigitalSignaturesSequence
        elif not isinstance(value, list) or not all(isinstance(item, DigitalSignaturesSequenceItem) for item in value):
            raise ValueError(f"DigitalSignaturesSequence must be a list of DigitalSignaturesSequenceItem objects")
        else:
            self._DigitalSignaturesSequence = value
            if "DigitalSignaturesSequence" not in self._dataset:
                self._dataset.DigitalSignaturesSequence = pydicom.Sequence()
            self._dataset.DigitalSignaturesSequence.clear()
            self._dataset.DigitalSignaturesSequence.extend([item.to_dataset() for item in value])

    def add_DigitalSignatures(self, item: DigitalSignaturesSequenceItem):
        if not isinstance(item, DigitalSignaturesSequenceItem):
            raise ValueError(f"Item must be an instance of DigitalSignaturesSequenceItem")
        self._DigitalSignaturesSequence.append(item)
        if "DigitalSignaturesSequence" not in self._dataset:
            self._dataset.DigitalSignaturesSequence = pydicom.Sequence()
        self._dataset.DigitalSignaturesSequence.append(item.to_dataset())

    @property
    def ClinicalTrialCoordinatingCenterName(self) -> Optional[str]:
        if "ClinicalTrialCoordinatingCenterName" in self._dataset:
            return self._dataset.ClinicalTrialCoordinatingCenterName
        return None

    @ClinicalTrialCoordinatingCenterName.setter
    def ClinicalTrialCoordinatingCenterName(self, value: Optional[str]):
        if value is None:
            if "ClinicalTrialCoordinatingCenterName" in self._dataset:
                del self._dataset.ClinicalTrialCoordinatingCenterName
        else:
            self._dataset.ClinicalTrialCoordinatingCenterName = value

    @property
    def ClinicalTrialSeriesID(self) -> Optional[str]:
        if "ClinicalTrialSeriesID" in self._dataset:
            return self._dataset.ClinicalTrialSeriesID
        return None

    @ClinicalTrialSeriesID.setter
    def ClinicalTrialSeriesID(self, value: Optional[str]):
        if value is None:
            if "ClinicalTrialSeriesID" in self._dataset:
                del self._dataset.ClinicalTrialSeriesID
        else:
            self._dataset.ClinicalTrialSeriesID = value

    @property
    def ClinicalTrialSeriesDescription(self) -> Optional[str]:
        if "ClinicalTrialSeriesDescription" in self._dataset:
            return self._dataset.ClinicalTrialSeriesDescription
        return None

    @ClinicalTrialSeriesDescription.setter
    def ClinicalTrialSeriesDescription(self, value: Optional[str]):
        if value is None:
            if "ClinicalTrialSeriesDescription" in self._dataset:
                del self._dataset.ClinicalTrialSeriesDescription
        else:
            self._dataset.ClinicalTrialSeriesDescription = value

    @property
    def IssuerOfClinicalTrialSeriesID(self) -> Optional[str]:
        if "IssuerOfClinicalTrialSeriesID" in self._dataset:
            return self._dataset.IssuerOfClinicalTrialSeriesID
        return None

    @IssuerOfClinicalTrialSeriesID.setter
    def IssuerOfClinicalTrialSeriesID(self, value: Optional[str]):
        if value is None:
            if "IssuerOfClinicalTrialSeriesID" in self._dataset:
                del self._dataset.IssuerOfClinicalTrialSeriesID
        else:
            self._dataset.IssuerOfClinicalTrialSeriesID = value

    @property
    def ReferencedImageSequence(self) -> Optional[List[ReferencedImageSequenceItem]]:
        if "ReferencedImageSequence" in self._dataset:
            if len(self._ReferencedImageSequence) == len(self._dataset.ReferencedImageSequence):
                return self._ReferencedImageSequence
            else:
                return [ReferencedImageSequenceItem(x) for x in self._dataset.ReferencedImageSequence]
        return None

    @ReferencedImageSequence.setter
    def ReferencedImageSequence(self, value: Optional[List[ReferencedImageSequenceItem]]):
        if value is None:
            self._ReferencedImageSequence = []
            if "ReferencedImageSequence" in self._dataset:
                del self._dataset.ReferencedImageSequence
        elif not isinstance(value, list) or not all(isinstance(item, ReferencedImageSequenceItem) for item in value):
            raise ValueError(f"ReferencedImageSequence must be a list of ReferencedImageSequenceItem objects")
        else:
            self._ReferencedImageSequence = value
            if "ReferencedImageSequence" not in self._dataset:
                self._dataset.ReferencedImageSequence = pydicom.Sequence()
            self._dataset.ReferencedImageSequence.clear()
            self._dataset.ReferencedImageSequence.extend([item.to_dataset() for item in value])

    def add_ReferencedImage(self, item: ReferencedImageSequenceItem):
        if not isinstance(item, ReferencedImageSequenceItem):
            raise ValueError(f"Item must be an instance of ReferencedImageSequenceItem")
        self._ReferencedImageSequence.append(item)
        if "ReferencedImageSequence" not in self._dataset:
            self._dataset.ReferencedImageSequence = pydicom.Sequence()
        self._dataset.ReferencedImageSequence.append(item.to_dataset())

    @property
    def ReferencedInstanceSequence(self) -> Optional[List[ReferencedInstanceSequenceItem]]:
        if "ReferencedInstanceSequence" in self._dataset:
            if len(self._ReferencedInstanceSequence) == len(self._dataset.ReferencedInstanceSequence):
                return self._ReferencedInstanceSequence
            else:
                return [ReferencedInstanceSequenceItem(x) for x in self._dataset.ReferencedInstanceSequence]
        return None

    @ReferencedInstanceSequence.setter
    def ReferencedInstanceSequence(self, value: Optional[List[ReferencedInstanceSequenceItem]]):
        if value is None:
            self._ReferencedInstanceSequence = []
            if "ReferencedInstanceSequence" in self._dataset:
                del self._dataset.ReferencedInstanceSequence
        elif not isinstance(value, list) or not all(isinstance(item, ReferencedInstanceSequenceItem) for item in value):
            raise ValueError(f"ReferencedInstanceSequence must be a list of ReferencedInstanceSequenceItem objects")
        else:
            self._ReferencedInstanceSequence = value
            if "ReferencedInstanceSequence" not in self._dataset:
                self._dataset.ReferencedInstanceSequence = pydicom.Sequence()
            self._dataset.ReferencedInstanceSequence.clear()
            self._dataset.ReferencedInstanceSequence.extend([item.to_dataset() for item in value])

    def add_ReferencedInstance(self, item: ReferencedInstanceSequenceItem):
        if not isinstance(item, ReferencedInstanceSequenceItem):
            raise ValueError(f"Item must be an instance of ReferencedInstanceSequenceItem")
        self._ReferencedInstanceSequence.append(item)
        if "ReferencedInstanceSequence" not in self._dataset:
            self._dataset.ReferencedInstanceSequence = pydicom.Sequence()
        self._dataset.ReferencedInstanceSequence.append(item.to_dataset())

    @property
    def DerivationDescription(self) -> Optional[str]:
        if "DerivationDescription" in self._dataset:
            return self._dataset.DerivationDescription
        return None

    @DerivationDescription.setter
    def DerivationDescription(self, value: Optional[str]):
        if value is None:
            if "DerivationDescription" in self._dataset:
                del self._dataset.DerivationDescription
        else:
            self._dataset.DerivationDescription = value

    @property
    def SourceImageSequence(self) -> Optional[List[SourceImageSequenceItem]]:
        if "SourceImageSequence" in self._dataset:
            if len(self._SourceImageSequence) == len(self._dataset.SourceImageSequence):
                return self._SourceImageSequence
            else:
                return [SourceImageSequenceItem(x) for x in self._dataset.SourceImageSequence]
        return None

    @SourceImageSequence.setter
    def SourceImageSequence(self, value: Optional[List[SourceImageSequenceItem]]):
        if value is None:
            self._SourceImageSequence = []
            if "SourceImageSequence" in self._dataset:
                del self._dataset.SourceImageSequence
        elif not isinstance(value, list) or not all(isinstance(item, SourceImageSequenceItem) for item in value):
            raise ValueError(f"SourceImageSequence must be a list of SourceImageSequenceItem objects")
        else:
            self._SourceImageSequence = value
            if "SourceImageSequence" not in self._dataset:
                self._dataset.SourceImageSequence = pydicom.Sequence()
            self._dataset.SourceImageSequence.clear()
            self._dataset.SourceImageSequence.extend([item.to_dataset() for item in value])

    def add_SourceImage(self, item: SourceImageSequenceItem):
        if not isinstance(item, SourceImageSequenceItem):
            raise ValueError(f"Item must be an instance of SourceImageSequenceItem")
        self._SourceImageSequence.append(item)
        if "SourceImageSequence" not in self._dataset:
            self._dataset.SourceImageSequence = pydicom.Sequence()
        self._dataset.SourceImageSequence.append(item.to_dataset())

    @property
    def DerivationCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "DerivationCodeSequence" in self._dataset:
            if len(self._DerivationCodeSequence) == len(self._dataset.DerivationCodeSequence):
                return self._DerivationCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.DerivationCodeSequence]
        return None

    @DerivationCodeSequence.setter
    def DerivationCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._DerivationCodeSequence = []
            if "DerivationCodeSequence" in self._dataset:
                del self._dataset.DerivationCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError(f"DerivationCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._DerivationCodeSequence = value
            if "DerivationCodeSequence" not in self._dataset:
                self._dataset.DerivationCodeSequence = pydicom.Sequence()
            self._dataset.DerivationCodeSequence.clear()
            self._dataset.DerivationCodeSequence.extend([item.to_dataset() for item in value])

    def add_DerivationCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError(f"Item must be an instance of CodeSequenceItem")
        self._DerivationCodeSequence.append(item)
        if "DerivationCodeSequence" not in self._dataset:
            self._dataset.DerivationCodeSequence = pydicom.Sequence()
        self._dataset.DerivationCodeSequence.append(item.to_dataset())

    @property
    def SourceInstanceSequence(self) -> Optional[List[SourceInstanceSequenceItem]]:
        if "SourceInstanceSequence" in self._dataset:
            if len(self._SourceInstanceSequence) == len(self._dataset.SourceInstanceSequence):
                return self._SourceInstanceSequence
            else:
                return [SourceInstanceSequenceItem(x) for x in self._dataset.SourceInstanceSequence]
        return None

    @SourceInstanceSequence.setter
    def SourceInstanceSequence(self, value: Optional[List[SourceInstanceSequenceItem]]):
        if value is None:
            self._SourceInstanceSequence = []
            if "SourceInstanceSequence" in self._dataset:
                del self._dataset.SourceInstanceSequence
        elif not isinstance(value, list) or not all(isinstance(item, SourceInstanceSequenceItem) for item in value):
            raise ValueError(f"SourceInstanceSequence must be a list of SourceInstanceSequenceItem objects")
        else:
            self._SourceInstanceSequence = value
            if "SourceInstanceSequence" not in self._dataset:
                self._dataset.SourceInstanceSequence = pydicom.Sequence()
            self._dataset.SourceInstanceSequence.clear()
            self._dataset.SourceInstanceSequence.extend([item.to_dataset() for item in value])

    def add_SourceInstance(self, item: SourceInstanceSequenceItem):
        if not isinstance(item, SourceInstanceSequenceItem):
            raise ValueError(f"Item must be an instance of SourceInstanceSequenceItem")
        self._SourceInstanceSequence.append(item)
        if "SourceInstanceSequence" not in self._dataset:
            self._dataset.SourceInstanceSequence = pydicom.Sequence()
        self._dataset.SourceInstanceSequence.append(item.to_dataset())

    @property
    def ReferencedSeriesSequence(self) -> Optional[List[ReferencedSeriesSequenceItem]]:
        if "ReferencedSeriesSequence" in self._dataset:
            if len(self._ReferencedSeriesSequence) == len(self._dataset.ReferencedSeriesSequence):
                return self._ReferencedSeriesSequence
            else:
                return [ReferencedSeriesSequenceItem(x) for x in self._dataset.ReferencedSeriesSequence]
        return None

    @ReferencedSeriesSequence.setter
    def ReferencedSeriesSequence(self, value: Optional[List[ReferencedSeriesSequenceItem]]):
        if value is None:
            self._ReferencedSeriesSequence = []
            if "ReferencedSeriesSequence" in self._dataset:
                del self._dataset.ReferencedSeriesSequence
        elif not isinstance(value, list) or not all(isinstance(item, ReferencedSeriesSequenceItem) for item in value):
            raise ValueError(f"ReferencedSeriesSequence must be a list of ReferencedSeriesSequenceItem objects")
        else:
            self._ReferencedSeriesSequence = value
            if "ReferencedSeriesSequence" not in self._dataset:
                self._dataset.ReferencedSeriesSequence = pydicom.Sequence()
            self._dataset.ReferencedSeriesSequence.clear()
            self._dataset.ReferencedSeriesSequence.extend([item.to_dataset() for item in value])

    def add_ReferencedSeries(self, item: ReferencedSeriesSequenceItem):
        if not isinstance(item, ReferencedSeriesSequenceItem):
            raise ValueError(f"Item must be an instance of ReferencedSeriesSequenceItem")
        self._ReferencedSeriesSequence.append(item)
        if "ReferencedSeriesSequence" not in self._dataset:
            self._dataset.ReferencedSeriesSequence = pydicom.Sequence()
        self._dataset.ReferencedSeriesSequence.append(item.to_dataset())

    @property
    def StudiesContainingOtherReferencedInstancesSequence(
        self,
    ) -> Optional[List[StudiesContainingOtherReferencedInstancesSequenceItem]]:
        if "StudiesContainingOtherReferencedInstancesSequence" in self._dataset:
            if len(self._StudiesContainingOtherReferencedInstancesSequence) == len(
                self._dataset.StudiesContainingOtherReferencedInstancesSequence
            ):
                return self._StudiesContainingOtherReferencedInstancesSequence
            else:
                return [
                    StudiesContainingOtherReferencedInstancesSequenceItem(x)
                    for x in self._dataset.StudiesContainingOtherReferencedInstancesSequence
                ]
        return None

    @StudiesContainingOtherReferencedInstancesSequence.setter
    def StudiesContainingOtherReferencedInstancesSequence(
        self, value: Optional[List[StudiesContainingOtherReferencedInstancesSequenceItem]]
    ):
        if value is None:
            self._StudiesContainingOtherReferencedInstancesSequence = []
            if "StudiesContainingOtherReferencedInstancesSequence" in self._dataset:
                del self._dataset.StudiesContainingOtherReferencedInstancesSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, StudiesContainingOtherReferencedInstancesSequenceItem) for item in value
        ):
            raise ValueError(
                f"StudiesContainingOtherReferencedInstancesSequence must be a list of StudiesContainingOtherReferencedInstancesSequenceItem objects"
            )
        else:
            self._StudiesContainingOtherReferencedInstancesSequence = value
            if "StudiesContainingOtherReferencedInstancesSequence" not in self._dataset:
                self._dataset.StudiesContainingOtherReferencedInstancesSequence = pydicom.Sequence()
            self._dataset.StudiesContainingOtherReferencedInstancesSequence.clear()
            self._dataset.StudiesContainingOtherReferencedInstancesSequence.extend([item.to_dataset() for item in value])

    def add_StudiesContainingOtherReferencedInstances(self, item: StudiesContainingOtherReferencedInstancesSequenceItem):
        if not isinstance(item, StudiesContainingOtherReferencedInstancesSequenceItem):
            raise ValueError(f"Item must be an instance of StudiesContainingOtherReferencedInstancesSequenceItem")
        self._StudiesContainingOtherReferencedInstancesSequence.append(item)
        if "StudiesContainingOtherReferencedInstancesSequence" not in self._dataset:
            self._dataset.StudiesContainingOtherReferencedInstancesSequence = pydicom.Sequence()
        self._dataset.StudiesContainingOtherReferencedInstancesSequence.append(item.to_dataset())

    @property
    def SeriesDate(self) -> Optional[str]:
        if "SeriesDate" in self._dataset:
            return self._dataset.SeriesDate
        return None

    @SeriesDate.setter
    def SeriesDate(self, value: Optional[str]):
        if value is None:
            if "SeriesDate" in self._dataset:
                del self._dataset.SeriesDate
        else:
            self._dataset.SeriesDate = value

    @property
    def SeriesTime(self) -> Optional[str]:
        if "SeriesTime" in self._dataset:
            return self._dataset.SeriesTime
        return None

    @SeriesTime.setter
    def SeriesTime(self, value: Optional[str]):
        if value is None:
            if "SeriesTime" in self._dataset:
                del self._dataset.SeriesTime
        else:
            self._dataset.SeriesTime = value

    @property
    def Modality(self) -> Optional[str]:
        if "Modality" in self._dataset:
            return self._dataset.Modality
        return None

    @Modality.setter
    def Modality(self, value: Optional[str]):
        if value is None:
            if "Modality" in self._dataset:
                del self._dataset.Modality
        else:
            self._dataset.Modality = value

    @property
    def SeriesDescription(self) -> Optional[str]:
        if "SeriesDescription" in self._dataset:
            return self._dataset.SeriesDescription
        return None

    @SeriesDescription.setter
    def SeriesDescription(self, value: Optional[str]):
        if value is None:
            if "SeriesDescription" in self._dataset:
                del self._dataset.SeriesDescription
        else:
            self._dataset.SeriesDescription = value

    @property
    def SeriesDescriptionCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "SeriesDescriptionCodeSequence" in self._dataset:
            if len(self._SeriesDescriptionCodeSequence) == len(self._dataset.SeriesDescriptionCodeSequence):
                return self._SeriesDescriptionCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.SeriesDescriptionCodeSequence]
        return None

    @SeriesDescriptionCodeSequence.setter
    def SeriesDescriptionCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._SeriesDescriptionCodeSequence = []
            if "SeriesDescriptionCodeSequence" in self._dataset:
                del self._dataset.SeriesDescriptionCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError(f"SeriesDescriptionCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._SeriesDescriptionCodeSequence = value
            if "SeriesDescriptionCodeSequence" not in self._dataset:
                self._dataset.SeriesDescriptionCodeSequence = pydicom.Sequence()
            self._dataset.SeriesDescriptionCodeSequence.clear()
            self._dataset.SeriesDescriptionCodeSequence.extend([item.to_dataset() for item in value])

    def add_SeriesDescriptionCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError(f"Item must be an instance of CodeSequenceItem")
        self._SeriesDescriptionCodeSequence.append(item)
        if "SeriesDescriptionCodeSequence" not in self._dataset:
            self._dataset.SeriesDescriptionCodeSequence = pydicom.Sequence()
        self._dataset.SeriesDescriptionCodeSequence.append(item.to_dataset())

    @property
    def PerformingPhysicianName(self) -> Optional[List[str]]:
        if "PerformingPhysicianName" in self._dataset:
            return self._dataset.PerformingPhysicianName
        return None

    @PerformingPhysicianName.setter
    def PerformingPhysicianName(self, value: Optional[List[str]]):
        if value is None:
            if "PerformingPhysicianName" in self._dataset:
                del self._dataset.PerformingPhysicianName
        else:
            self._dataset.PerformingPhysicianName = value

    @property
    def PerformingPhysicianIdentificationSequence(self) -> Optional[List[PerformingPhysicianIdentificationSequenceItem]]:
        if "PerformingPhysicianIdentificationSequence" in self._dataset:
            if len(self._PerformingPhysicianIdentificationSequence) == len(
                self._dataset.PerformingPhysicianIdentificationSequence
            ):
                return self._PerformingPhysicianIdentificationSequence
            else:
                return [
                    PerformingPhysicianIdentificationSequenceItem(x)
                    for x in self._dataset.PerformingPhysicianIdentificationSequence
                ]
        return None

    @PerformingPhysicianIdentificationSequence.setter
    def PerformingPhysicianIdentificationSequence(self, value: Optional[List[PerformingPhysicianIdentificationSequenceItem]]):
        if value is None:
            self._PerformingPhysicianIdentificationSequence = []
            if "PerformingPhysicianIdentificationSequence" in self._dataset:
                del self._dataset.PerformingPhysicianIdentificationSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, PerformingPhysicianIdentificationSequenceItem) for item in value
        ):
            raise ValueError(
                f"PerformingPhysicianIdentificationSequence must be a list of PerformingPhysicianIdentificationSequenceItem objects"
            )
        else:
            self._PerformingPhysicianIdentificationSequence = value
            if "PerformingPhysicianIdentificationSequence" not in self._dataset:
                self._dataset.PerformingPhysicianIdentificationSequence = pydicom.Sequence()
            self._dataset.PerformingPhysicianIdentificationSequence.clear()
            self._dataset.PerformingPhysicianIdentificationSequence.extend([item.to_dataset() for item in value])

    def add_PerformingPhysicianIdentification(self, item: PerformingPhysicianIdentificationSequenceItem):
        if not isinstance(item, PerformingPhysicianIdentificationSequenceItem):
            raise ValueError(f"Item must be an instance of PerformingPhysicianIdentificationSequenceItem")
        self._PerformingPhysicianIdentificationSequence.append(item)
        if "PerformingPhysicianIdentificationSequence" not in self._dataset:
            self._dataset.PerformingPhysicianIdentificationSequence = pydicom.Sequence()
        self._dataset.PerformingPhysicianIdentificationSequence.append(item.to_dataset())

    @property
    def OperatorsName(self) -> Optional[List[str]]:
        if "OperatorsName" in self._dataset:
            return self._dataset.OperatorsName
        return None

    @OperatorsName.setter
    def OperatorsName(self, value: Optional[List[str]]):
        if value is None:
            if "OperatorsName" in self._dataset:
                del self._dataset.OperatorsName
        else:
            self._dataset.OperatorsName = value

    @property
    def OperatorIdentificationSequence(self) -> Optional[List[OperatorIdentificationSequenceItem]]:
        if "OperatorIdentificationSequence" in self._dataset:
            if len(self._OperatorIdentificationSequence) == len(self._dataset.OperatorIdentificationSequence):
                return self._OperatorIdentificationSequence
            else:
                return [OperatorIdentificationSequenceItem(x) for x in self._dataset.OperatorIdentificationSequence]
        return None

    @OperatorIdentificationSequence.setter
    def OperatorIdentificationSequence(self, value: Optional[List[OperatorIdentificationSequenceItem]]):
        if value is None:
            self._OperatorIdentificationSequence = []
            if "OperatorIdentificationSequence" in self._dataset:
                del self._dataset.OperatorIdentificationSequence
        elif not isinstance(value, list) or not all(isinstance(item, OperatorIdentificationSequenceItem) for item in value):
            raise ValueError(f"OperatorIdentificationSequence must be a list of OperatorIdentificationSequenceItem objects")
        else:
            self._OperatorIdentificationSequence = value
            if "OperatorIdentificationSequence" not in self._dataset:
                self._dataset.OperatorIdentificationSequence = pydicom.Sequence()
            self._dataset.OperatorIdentificationSequence.clear()
            self._dataset.OperatorIdentificationSequence.extend([item.to_dataset() for item in value])

    def add_OperatorIdentification(self, item: OperatorIdentificationSequenceItem):
        if not isinstance(item, OperatorIdentificationSequenceItem):
            raise ValueError(f"Item must be an instance of OperatorIdentificationSequenceItem")
        self._OperatorIdentificationSequence.append(item)
        if "OperatorIdentificationSequence" not in self._dataset:
            self._dataset.OperatorIdentificationSequence = pydicom.Sequence()
        self._dataset.OperatorIdentificationSequence.append(item.to_dataset())

    @property
    def ReferencedPerformedProcedureStepSequence(self) -> Optional[List[ReferencedPerformedProcedureStepSequenceItem]]:
        if "ReferencedPerformedProcedureStepSequence" in self._dataset:
            if len(self._ReferencedPerformedProcedureStepSequence) == len(
                self._dataset.ReferencedPerformedProcedureStepSequence
            ):
                return self._ReferencedPerformedProcedureStepSequence
            else:
                return [
                    ReferencedPerformedProcedureStepSequenceItem(x)
                    for x in self._dataset.ReferencedPerformedProcedureStepSequence
                ]
        return None

    @ReferencedPerformedProcedureStepSequence.setter
    def ReferencedPerformedProcedureStepSequence(self, value: Optional[List[ReferencedPerformedProcedureStepSequenceItem]]):
        if value is None:
            self._ReferencedPerformedProcedureStepSequence = []
            if "ReferencedPerformedProcedureStepSequence" in self._dataset:
                del self._dataset.ReferencedPerformedProcedureStepSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, ReferencedPerformedProcedureStepSequenceItem) for item in value
        ):
            raise ValueError(
                f"ReferencedPerformedProcedureStepSequence must be a list of ReferencedPerformedProcedureStepSequenceItem objects"
            )
        else:
            self._ReferencedPerformedProcedureStepSequence = value
            if "ReferencedPerformedProcedureStepSequence" not in self._dataset:
                self._dataset.ReferencedPerformedProcedureStepSequence = pydicom.Sequence()
            self._dataset.ReferencedPerformedProcedureStepSequence.clear()
            self._dataset.ReferencedPerformedProcedureStepSequence.extend([item.to_dataset() for item in value])

    def add_ReferencedPerformedProcedureStep(self, item: ReferencedPerformedProcedureStepSequenceItem):
        if not isinstance(item, ReferencedPerformedProcedureStepSequenceItem):
            raise ValueError(f"Item must be an instance of ReferencedPerformedProcedureStepSequenceItem")
        self._ReferencedPerformedProcedureStepSequence.append(item)
        if "ReferencedPerformedProcedureStepSequence" not in self._dataset:
            self._dataset.ReferencedPerformedProcedureStepSequence = pydicom.Sequence()
        self._dataset.ReferencedPerformedProcedureStepSequence.append(item.to_dataset())

    @property
    def RelatedSeriesSequence(self) -> Optional[List[RelatedSeriesSequenceItem]]:
        if "RelatedSeriesSequence" in self._dataset:
            if len(self._RelatedSeriesSequence) == len(self._dataset.RelatedSeriesSequence):
                return self._RelatedSeriesSequence
            else:
                return [RelatedSeriesSequenceItem(x) for x in self._dataset.RelatedSeriesSequence]
        return None

    @RelatedSeriesSequence.setter
    def RelatedSeriesSequence(self, value: Optional[List[RelatedSeriesSequenceItem]]):
        if value is None:
            self._RelatedSeriesSequence = []
            if "RelatedSeriesSequence" in self._dataset:
                del self._dataset.RelatedSeriesSequence
        elif not isinstance(value, list) or not all(isinstance(item, RelatedSeriesSequenceItem) for item in value):
            raise ValueError(f"RelatedSeriesSequence must be a list of RelatedSeriesSequenceItem objects")
        else:
            self._RelatedSeriesSequence = value
            if "RelatedSeriesSequence" not in self._dataset:
                self._dataset.RelatedSeriesSequence = pydicom.Sequence()
            self._dataset.RelatedSeriesSequence.clear()
            self._dataset.RelatedSeriesSequence.extend([item.to_dataset() for item in value])

    def add_RelatedSeries(self, item: RelatedSeriesSequenceItem):
        if not isinstance(item, RelatedSeriesSequenceItem):
            raise ValueError(f"Item must be an instance of RelatedSeriesSequenceItem")
        self._RelatedSeriesSequence.append(item)
        if "RelatedSeriesSequence" not in self._dataset:
            self._dataset.RelatedSeriesSequence = pydicom.Sequence()
        self._dataset.RelatedSeriesSequence.append(item.to_dataset())

    @property
    def AnatomicalOrientationType(self) -> Optional[str]:
        if "AnatomicalOrientationType" in self._dataset:
            return self._dataset.AnatomicalOrientationType
        return None

    @AnatomicalOrientationType.setter
    def AnatomicalOrientationType(self, value: Optional[str]):
        if value is None:
            if "AnatomicalOrientationType" in self._dataset:
                del self._dataset.AnatomicalOrientationType
        else:
            self._dataset.AnatomicalOrientationType = value

    @property
    def BodyPartExamined(self) -> Optional[str]:
        if "BodyPartExamined" in self._dataset:
            return self._dataset.BodyPartExamined
        return None

    @BodyPartExamined.setter
    def BodyPartExamined(self, value: Optional[str]):
        if value is None:
            if "BodyPartExamined" in self._dataset:
                del self._dataset.BodyPartExamined
        else:
            self._dataset.BodyPartExamined = value

    @property
    def ProtocolName(self) -> Optional[str]:
        if "ProtocolName" in self._dataset:
            return self._dataset.ProtocolName
        return None

    @ProtocolName.setter
    def ProtocolName(self, value: Optional[str]):
        if value is None:
            if "ProtocolName" in self._dataset:
                del self._dataset.ProtocolName
        else:
            self._dataset.ProtocolName = value

    @property
    def PatientPosition(self) -> Optional[str]:
        if "PatientPosition" in self._dataset:
            return self._dataset.PatientPosition
        return None

    @PatientPosition.setter
    def PatientPosition(self, value: Optional[str]):
        if value is None:
            if "PatientPosition" in self._dataset:
                del self._dataset.PatientPosition
        else:
            self._dataset.PatientPosition = value

    @property
    def SeriesInstanceUID(self) -> Optional[str]:
        if "SeriesInstanceUID" in self._dataset:
            return self._dataset.SeriesInstanceUID
        return None

    @SeriesInstanceUID.setter
    def SeriesInstanceUID(self, value: Optional[str]):
        if value is None:
            if "SeriesInstanceUID" in self._dataset:
                del self._dataset.SeriesInstanceUID
        else:
            self._dataset.SeriesInstanceUID = value

    @property
    def SeriesNumber(self) -> Optional[int]:
        if "SeriesNumber" in self._dataset:
            return self._dataset.SeriesNumber
        return None

    @SeriesNumber.setter
    def SeriesNumber(self, value: Optional[int]):
        if value is None:
            if "SeriesNumber" in self._dataset:
                del self._dataset.SeriesNumber
        else:
            self._dataset.SeriesNumber = value

    @property
    def Laterality(self) -> Optional[str]:
        if "Laterality" in self._dataset:
            return self._dataset.Laterality
        return None

    @Laterality.setter
    def Laterality(self, value: Optional[str]):
        if value is None:
            if "Laterality" in self._dataset:
                del self._dataset.Laterality
        else:
            self._dataset.Laterality = value

    @property
    def SmallestPixelValueInSeries(self) -> Optional[int]:
        if "SmallestPixelValueInSeries" in self._dataset:
            return self._dataset.SmallestPixelValueInSeries
        return None

    @SmallestPixelValueInSeries.setter
    def SmallestPixelValueInSeries(self, value: Optional[int]):
        if value is None:
            if "SmallestPixelValueInSeries" in self._dataset:
                del self._dataset.SmallestPixelValueInSeries
        else:
            self._dataset.SmallestPixelValueInSeries = value

    @property
    def LargestPixelValueInSeries(self) -> Optional[int]:
        if "LargestPixelValueInSeries" in self._dataset:
            return self._dataset.LargestPixelValueInSeries
        return None

    @LargestPixelValueInSeries.setter
    def LargestPixelValueInSeries(self, value: Optional[int]):
        if value is None:
            if "LargestPixelValueInSeries" in self._dataset:
                del self._dataset.LargestPixelValueInSeries
        else:
            self._dataset.LargestPixelValueInSeries = value

    @property
    def PerformedProcedureStepStartDate(self) -> Optional[str]:
        if "PerformedProcedureStepStartDate" in self._dataset:
            return self._dataset.PerformedProcedureStepStartDate
        return None

    @PerformedProcedureStepStartDate.setter
    def PerformedProcedureStepStartDate(self, value: Optional[str]):
        if value is None:
            if "PerformedProcedureStepStartDate" in self._dataset:
                del self._dataset.PerformedProcedureStepStartDate
        else:
            self._dataset.PerformedProcedureStepStartDate = value

    @property
    def PerformedProcedureStepStartTime(self) -> Optional[str]:
        if "PerformedProcedureStepStartTime" in self._dataset:
            return self._dataset.PerformedProcedureStepStartTime
        return None

    @PerformedProcedureStepStartTime.setter
    def PerformedProcedureStepStartTime(self, value: Optional[str]):
        if value is None:
            if "PerformedProcedureStepStartTime" in self._dataset:
                del self._dataset.PerformedProcedureStepStartTime
        else:
            self._dataset.PerformedProcedureStepStartTime = value

    @property
    def PerformedProcedureStepEndDate(self) -> Optional[str]:
        if "PerformedProcedureStepEndDate" in self._dataset:
            return self._dataset.PerformedProcedureStepEndDate
        return None

    @PerformedProcedureStepEndDate.setter
    def PerformedProcedureStepEndDate(self, value: Optional[str]):
        if value is None:
            if "PerformedProcedureStepEndDate" in self._dataset:
                del self._dataset.PerformedProcedureStepEndDate
        else:
            self._dataset.PerformedProcedureStepEndDate = value

    @property
    def PerformedProcedureStepEndTime(self) -> Optional[str]:
        if "PerformedProcedureStepEndTime" in self._dataset:
            return self._dataset.PerformedProcedureStepEndTime
        return None

    @PerformedProcedureStepEndTime.setter
    def PerformedProcedureStepEndTime(self, value: Optional[str]):
        if value is None:
            if "PerformedProcedureStepEndTime" in self._dataset:
                del self._dataset.PerformedProcedureStepEndTime
        else:
            self._dataset.PerformedProcedureStepEndTime = value

    @property
    def PerformedProcedureStepID(self) -> Optional[str]:
        if "PerformedProcedureStepID" in self._dataset:
            return self._dataset.PerformedProcedureStepID
        return None

    @PerformedProcedureStepID.setter
    def PerformedProcedureStepID(self, value: Optional[str]):
        if value is None:
            if "PerformedProcedureStepID" in self._dataset:
                del self._dataset.PerformedProcedureStepID
        else:
            self._dataset.PerformedProcedureStepID = value

    @property
    def PerformedProcedureStepDescription(self) -> Optional[str]:
        if "PerformedProcedureStepDescription" in self._dataset:
            return self._dataset.PerformedProcedureStepDescription
        return None

    @PerformedProcedureStepDescription.setter
    def PerformedProcedureStepDescription(self, value: Optional[str]):
        if value is None:
            if "PerformedProcedureStepDescription" in self._dataset:
                del self._dataset.PerformedProcedureStepDescription
        else:
            self._dataset.PerformedProcedureStepDescription = value

    @property
    def PerformedProtocolCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "PerformedProtocolCodeSequence" in self._dataset:
            if len(self._PerformedProtocolCodeSequence) == len(self._dataset.PerformedProtocolCodeSequence):
                return self._PerformedProtocolCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.PerformedProtocolCodeSequence]
        return None

    @PerformedProtocolCodeSequence.setter
    def PerformedProtocolCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._PerformedProtocolCodeSequence = []
            if "PerformedProtocolCodeSequence" in self._dataset:
                del self._dataset.PerformedProtocolCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError(f"PerformedProtocolCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._PerformedProtocolCodeSequence = value
            if "PerformedProtocolCodeSequence" not in self._dataset:
                self._dataset.PerformedProtocolCodeSequence = pydicom.Sequence()
            self._dataset.PerformedProtocolCodeSequence.clear()
            self._dataset.PerformedProtocolCodeSequence.extend([item.to_dataset() for item in value])

    def add_PerformedProtocolCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError(f"Item must be an instance of CodeSequenceItem")
        self._PerformedProtocolCodeSequence.append(item)
        if "PerformedProtocolCodeSequence" not in self._dataset:
            self._dataset.PerformedProtocolCodeSequence = pydicom.Sequence()
        self._dataset.PerformedProtocolCodeSequence.append(item.to_dataset())

    @property
    def RequestAttributesSequence(self) -> Optional[List[RequestAttributesSequenceItem]]:
        if "RequestAttributesSequence" in self._dataset:
            if len(self._RequestAttributesSequence) == len(self._dataset.RequestAttributesSequence):
                return self._RequestAttributesSequence
            else:
                return [RequestAttributesSequenceItem(x) for x in self._dataset.RequestAttributesSequence]
        return None

    @RequestAttributesSequence.setter
    def RequestAttributesSequence(self, value: Optional[List[RequestAttributesSequenceItem]]):
        if value is None:
            self._RequestAttributesSequence = []
            if "RequestAttributesSequence" in self._dataset:
                del self._dataset.RequestAttributesSequence
        elif not isinstance(value, list) or not all(isinstance(item, RequestAttributesSequenceItem) for item in value):
            raise ValueError(f"RequestAttributesSequence must be a list of RequestAttributesSequenceItem objects")
        else:
            self._RequestAttributesSequence = value
            if "RequestAttributesSequence" not in self._dataset:
                self._dataset.RequestAttributesSequence = pydicom.Sequence()
            self._dataset.RequestAttributesSequence.clear()
            self._dataset.RequestAttributesSequence.extend([item.to_dataset() for item in value])

    def add_RequestAttributes(self, item: RequestAttributesSequenceItem):
        if not isinstance(item, RequestAttributesSequenceItem):
            raise ValueError(f"Item must be an instance of RequestAttributesSequenceItem")
        self._RequestAttributesSequence.append(item)
        if "RequestAttributesSequence" not in self._dataset:
            self._dataset.RequestAttributesSequence = pydicom.Sequence()
        self._dataset.RequestAttributesSequence.append(item.to_dataset())

    @property
    def CommentsOnThePerformedProcedureStep(self) -> Optional[str]:
        if "CommentsOnThePerformedProcedureStep" in self._dataset:
            return self._dataset.CommentsOnThePerformedProcedureStep
        return None

    @CommentsOnThePerformedProcedureStep.setter
    def CommentsOnThePerformedProcedureStep(self, value: Optional[str]):
        if value is None:
            if "CommentsOnThePerformedProcedureStep" in self._dataset:
                del self._dataset.CommentsOnThePerformedProcedureStep
        else:
            self._dataset.CommentsOnThePerformedProcedureStep = value

    @property
    def TreatmentSessionUID(self) -> Optional[str]:
        if "TreatmentSessionUID" in self._dataset:
            return self._dataset.TreatmentSessionUID
        return None

    @TreatmentSessionUID.setter
    def TreatmentSessionUID(self, value: Optional[str]):
        if value is None:
            if "TreatmentSessionUID" in self._dataset:
                del self._dataset.TreatmentSessionUID
        else:
            self._dataset.TreatmentSessionUID = value

    @property
    def AdmittingDiagnosesDescription(self) -> Optional[List[str]]:
        if "AdmittingDiagnosesDescription" in self._dataset:
            return self._dataset.AdmittingDiagnosesDescription
        return None

    @AdmittingDiagnosesDescription.setter
    def AdmittingDiagnosesDescription(self, value: Optional[List[str]]):
        if value is None:
            if "AdmittingDiagnosesDescription" in self._dataset:
                del self._dataset.AdmittingDiagnosesDescription
        else:
            self._dataset.AdmittingDiagnosesDescription = value

    @property
    def AdmittingDiagnosesCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "AdmittingDiagnosesCodeSequence" in self._dataset:
            if len(self._AdmittingDiagnosesCodeSequence) == len(self._dataset.AdmittingDiagnosesCodeSequence):
                return self._AdmittingDiagnosesCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.AdmittingDiagnosesCodeSequence]
        return None

    @AdmittingDiagnosesCodeSequence.setter
    def AdmittingDiagnosesCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._AdmittingDiagnosesCodeSequence = []
            if "AdmittingDiagnosesCodeSequence" in self._dataset:
                del self._dataset.AdmittingDiagnosesCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError(f"AdmittingDiagnosesCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._AdmittingDiagnosesCodeSequence = value
            if "AdmittingDiagnosesCodeSequence" not in self._dataset:
                self._dataset.AdmittingDiagnosesCodeSequence = pydicom.Sequence()
            self._dataset.AdmittingDiagnosesCodeSequence.clear()
            self._dataset.AdmittingDiagnosesCodeSequence.extend([item.to_dataset() for item in value])

    def add_AdmittingDiagnosesCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError(f"Item must be an instance of CodeSequenceItem")
        self._AdmittingDiagnosesCodeSequence.append(item)
        if "AdmittingDiagnosesCodeSequence" not in self._dataset:
            self._dataset.AdmittingDiagnosesCodeSequence = pydicom.Sequence()
        self._dataset.AdmittingDiagnosesCodeSequence.append(item.to_dataset())

    @property
    def PatientAge(self) -> Optional[str]:
        if "PatientAge" in self._dataset:
            return self._dataset.PatientAge
        return None

    @PatientAge.setter
    def PatientAge(self, value: Optional[str]):
        if value is None:
            if "PatientAge" in self._dataset:
                del self._dataset.PatientAge
        else:
            self._dataset.PatientAge = value

    @property
    def PatientSize(self) -> Optional[Decimal]:
        if "PatientSize" in self._dataset:
            return self._dataset.PatientSize
        return None

    @PatientSize.setter
    def PatientSize(self, value: Optional[Decimal]):
        if value is None:
            if "PatientSize" in self._dataset:
                del self._dataset.PatientSize
        else:
            self._dataset.PatientSize = value

    @property
    def PatientSizeCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "PatientSizeCodeSequence" in self._dataset:
            if len(self._PatientSizeCodeSequence) == len(self._dataset.PatientSizeCodeSequence):
                return self._PatientSizeCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.PatientSizeCodeSequence]
        return None

    @PatientSizeCodeSequence.setter
    def PatientSizeCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._PatientSizeCodeSequence = []
            if "PatientSizeCodeSequence" in self._dataset:
                del self._dataset.PatientSizeCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError(f"PatientSizeCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._PatientSizeCodeSequence = value
            if "PatientSizeCodeSequence" not in self._dataset:
                self._dataset.PatientSizeCodeSequence = pydicom.Sequence()
            self._dataset.PatientSizeCodeSequence.clear()
            self._dataset.PatientSizeCodeSequence.extend([item.to_dataset() for item in value])

    def add_PatientSizeCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError(f"Item must be an instance of CodeSequenceItem")
        self._PatientSizeCodeSequence.append(item)
        if "PatientSizeCodeSequence" not in self._dataset:
            self._dataset.PatientSizeCodeSequence = pydicom.Sequence()
        self._dataset.PatientSizeCodeSequence.append(item.to_dataset())

    @property
    def PatientBodyMassIndex(self) -> Optional[Decimal]:
        if "PatientBodyMassIndex" in self._dataset:
            return self._dataset.PatientBodyMassIndex
        return None

    @PatientBodyMassIndex.setter
    def PatientBodyMassIndex(self, value: Optional[Decimal]):
        if value is None:
            if "PatientBodyMassIndex" in self._dataset:
                del self._dataset.PatientBodyMassIndex
        else:
            self._dataset.PatientBodyMassIndex = value

    @property
    def MeasuredAPDimension(self) -> Optional[Decimal]:
        if "MeasuredAPDimension" in self._dataset:
            return self._dataset.MeasuredAPDimension
        return None

    @MeasuredAPDimension.setter
    def MeasuredAPDimension(self, value: Optional[Decimal]):
        if value is None:
            if "MeasuredAPDimension" in self._dataset:
                del self._dataset.MeasuredAPDimension
        else:
            self._dataset.MeasuredAPDimension = value

    @property
    def MeasuredLateralDimension(self) -> Optional[Decimal]:
        if "MeasuredLateralDimension" in self._dataset:
            return self._dataset.MeasuredLateralDimension
        return None

    @MeasuredLateralDimension.setter
    def MeasuredLateralDimension(self, value: Optional[Decimal]):
        if value is None:
            if "MeasuredLateralDimension" in self._dataset:
                del self._dataset.MeasuredLateralDimension
        else:
            self._dataset.MeasuredLateralDimension = value

    @property
    def PatientWeight(self) -> Optional[Decimal]:
        if "PatientWeight" in self._dataset:
            return self._dataset.PatientWeight
        return None

    @PatientWeight.setter
    def PatientWeight(self, value: Optional[Decimal]):
        if value is None:
            if "PatientWeight" in self._dataset:
                del self._dataset.PatientWeight
        else:
            self._dataset.PatientWeight = value

    @property
    def MedicalAlerts(self) -> Optional[List[str]]:
        if "MedicalAlerts" in self._dataset:
            return self._dataset.MedicalAlerts
        return None

    @MedicalAlerts.setter
    def MedicalAlerts(self, value: Optional[List[str]]):
        if value is None:
            if "MedicalAlerts" in self._dataset:
                del self._dataset.MedicalAlerts
        else:
            self._dataset.MedicalAlerts = value

    @property
    def Allergies(self) -> Optional[List[str]]:
        if "Allergies" in self._dataset:
            return self._dataset.Allergies
        return None

    @Allergies.setter
    def Allergies(self, value: Optional[List[str]]):
        if value is None:
            if "Allergies" in self._dataset:
                del self._dataset.Allergies
        else:
            self._dataset.Allergies = value

    @property
    def Occupation(self) -> Optional[str]:
        if "Occupation" in self._dataset:
            return self._dataset.Occupation
        return None

    @Occupation.setter
    def Occupation(self, value: Optional[str]):
        if value is None:
            if "Occupation" in self._dataset:
                del self._dataset.Occupation
        else:
            self._dataset.Occupation = value

    @property
    def SmokingStatus(self) -> Optional[str]:
        if "SmokingStatus" in self._dataset:
            return self._dataset.SmokingStatus
        return None

    @SmokingStatus.setter
    def SmokingStatus(self, value: Optional[str]):
        if value is None:
            if "SmokingStatus" in self._dataset:
                del self._dataset.SmokingStatus
        else:
            self._dataset.SmokingStatus = value

    @property
    def AdditionalPatientHistory(self) -> Optional[str]:
        if "AdditionalPatientHistory" in self._dataset:
            return self._dataset.AdditionalPatientHistory
        return None

    @AdditionalPatientHistory.setter
    def AdditionalPatientHistory(self, value: Optional[str]):
        if value is None:
            if "AdditionalPatientHistory" in self._dataset:
                del self._dataset.AdditionalPatientHistory
        else:
            self._dataset.AdditionalPatientHistory = value

    @property
    def PregnancyStatus(self) -> Optional[int]:
        if "PregnancyStatus" in self._dataset:
            return self._dataset.PregnancyStatus
        return None

    @PregnancyStatus.setter
    def PregnancyStatus(self, value: Optional[int]):
        if value is None:
            if "PregnancyStatus" in self._dataset:
                del self._dataset.PregnancyStatus
        else:
            self._dataset.PregnancyStatus = value

    @property
    def LastMenstrualDate(self) -> Optional[str]:
        if "LastMenstrualDate" in self._dataset:
            return self._dataset.LastMenstrualDate
        return None

    @LastMenstrualDate.setter
    def LastMenstrualDate(self, value: Optional[str]):
        if value is None:
            if "LastMenstrualDate" in self._dataset:
                del self._dataset.LastMenstrualDate
        else:
            self._dataset.LastMenstrualDate = value

    @property
    def PatientSexNeutered(self) -> Optional[str]:
        if "PatientSexNeutered" in self._dataset:
            return self._dataset.PatientSexNeutered
        return None

    @PatientSexNeutered.setter
    def PatientSexNeutered(self, value: Optional[str]):
        if value is None:
            if "PatientSexNeutered" in self._dataset:
                del self._dataset.PatientSexNeutered
        else:
            self._dataset.PatientSexNeutered = value

    @property
    def ReasonForVisit(self) -> Optional[str]:
        if "ReasonForVisit" in self._dataset:
            return self._dataset.ReasonForVisit
        return None

    @ReasonForVisit.setter
    def ReasonForVisit(self, value: Optional[str]):
        if value is None:
            if "ReasonForVisit" in self._dataset:
                del self._dataset.ReasonForVisit
        else:
            self._dataset.ReasonForVisit = value

    @property
    def ReasonForVisitCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "ReasonForVisitCodeSequence" in self._dataset:
            if len(self._ReasonForVisitCodeSequence) == len(self._dataset.ReasonForVisitCodeSequence):
                return self._ReasonForVisitCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.ReasonForVisitCodeSequence]
        return None

    @ReasonForVisitCodeSequence.setter
    def ReasonForVisitCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._ReasonForVisitCodeSequence = []
            if "ReasonForVisitCodeSequence" in self._dataset:
                del self._dataset.ReasonForVisitCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError(f"ReasonForVisitCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._ReasonForVisitCodeSequence = value
            if "ReasonForVisitCodeSequence" not in self._dataset:
                self._dataset.ReasonForVisitCodeSequence = pydicom.Sequence()
            self._dataset.ReasonForVisitCodeSequence.clear()
            self._dataset.ReasonForVisitCodeSequence.extend([item.to_dataset() for item in value])

    def add_ReasonForVisitCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError(f"Item must be an instance of CodeSequenceItem")
        self._ReasonForVisitCodeSequence.append(item)
        if "ReasonForVisitCodeSequence" not in self._dataset:
            self._dataset.ReasonForVisitCodeSequence = pydicom.Sequence()
        self._dataset.ReasonForVisitCodeSequence.append(item.to_dataset())

    @property
    def AdmissionID(self) -> Optional[str]:
        if "AdmissionID" in self._dataset:
            return self._dataset.AdmissionID
        return None

    @AdmissionID.setter
    def AdmissionID(self, value: Optional[str]):
        if value is None:
            if "AdmissionID" in self._dataset:
                del self._dataset.AdmissionID
        else:
            self._dataset.AdmissionID = value

    @property
    def IssuerOfAdmissionIDSequence(self) -> Optional[List[IssuerOfAdmissionIDSequenceItem]]:
        if "IssuerOfAdmissionIDSequence" in self._dataset:
            if len(self._IssuerOfAdmissionIDSequence) == len(self._dataset.IssuerOfAdmissionIDSequence):
                return self._IssuerOfAdmissionIDSequence
            else:
                return [IssuerOfAdmissionIDSequenceItem(x) for x in self._dataset.IssuerOfAdmissionIDSequence]
        return None

    @IssuerOfAdmissionIDSequence.setter
    def IssuerOfAdmissionIDSequence(self, value: Optional[List[IssuerOfAdmissionIDSequenceItem]]):
        if value is None:
            self._IssuerOfAdmissionIDSequence = []
            if "IssuerOfAdmissionIDSequence" in self._dataset:
                del self._dataset.IssuerOfAdmissionIDSequence
        elif not isinstance(value, list) or not all(isinstance(item, IssuerOfAdmissionIDSequenceItem) for item in value):
            raise ValueError(f"IssuerOfAdmissionIDSequence must be a list of IssuerOfAdmissionIDSequenceItem objects")
        else:
            self._IssuerOfAdmissionIDSequence = value
            if "IssuerOfAdmissionIDSequence" not in self._dataset:
                self._dataset.IssuerOfAdmissionIDSequence = pydicom.Sequence()
            self._dataset.IssuerOfAdmissionIDSequence.clear()
            self._dataset.IssuerOfAdmissionIDSequence.extend([item.to_dataset() for item in value])

    def add_IssuerOfAdmissionID(self, item: IssuerOfAdmissionIDSequenceItem):
        if not isinstance(item, IssuerOfAdmissionIDSequenceItem):
            raise ValueError(f"Item must be an instance of IssuerOfAdmissionIDSequenceItem")
        self._IssuerOfAdmissionIDSequence.append(item)
        if "IssuerOfAdmissionIDSequence" not in self._dataset:
            self._dataset.IssuerOfAdmissionIDSequence = pydicom.Sequence()
        self._dataset.IssuerOfAdmissionIDSequence.append(item.to_dataset())

    @property
    def ServiceEpisodeID(self) -> Optional[str]:
        if "ServiceEpisodeID" in self._dataset:
            return self._dataset.ServiceEpisodeID
        return None

    @ServiceEpisodeID.setter
    def ServiceEpisodeID(self, value: Optional[str]):
        if value is None:
            if "ServiceEpisodeID" in self._dataset:
                del self._dataset.ServiceEpisodeID
        else:
            self._dataset.ServiceEpisodeID = value

    @property
    def ServiceEpisodeDescription(self) -> Optional[str]:
        if "ServiceEpisodeDescription" in self._dataset:
            return self._dataset.ServiceEpisodeDescription
        return None

    @ServiceEpisodeDescription.setter
    def ServiceEpisodeDescription(self, value: Optional[str]):
        if value is None:
            if "ServiceEpisodeDescription" in self._dataset:
                del self._dataset.ServiceEpisodeDescription
        else:
            self._dataset.ServiceEpisodeDescription = value

    @property
    def IssuerOfServiceEpisodeIDSequence(self) -> Optional[List[IssuerOfServiceEpisodeIDSequenceItem]]:
        if "IssuerOfServiceEpisodeIDSequence" in self._dataset:
            if len(self._IssuerOfServiceEpisodeIDSequence) == len(self._dataset.IssuerOfServiceEpisodeIDSequence):
                return self._IssuerOfServiceEpisodeIDSequence
            else:
                return [IssuerOfServiceEpisodeIDSequenceItem(x) for x in self._dataset.IssuerOfServiceEpisodeIDSequence]
        return None

    @IssuerOfServiceEpisodeIDSequence.setter
    def IssuerOfServiceEpisodeIDSequence(self, value: Optional[List[IssuerOfServiceEpisodeIDSequenceItem]]):
        if value is None:
            self._IssuerOfServiceEpisodeIDSequence = []
            if "IssuerOfServiceEpisodeIDSequence" in self._dataset:
                del self._dataset.IssuerOfServiceEpisodeIDSequence
        elif not isinstance(value, list) or not all(isinstance(item, IssuerOfServiceEpisodeIDSequenceItem) for item in value):
            raise ValueError(
                f"IssuerOfServiceEpisodeIDSequence must be a list of IssuerOfServiceEpisodeIDSequenceItem objects"
            )
        else:
            self._IssuerOfServiceEpisodeIDSequence = value
            if "IssuerOfServiceEpisodeIDSequence" not in self._dataset:
                self._dataset.IssuerOfServiceEpisodeIDSequence = pydicom.Sequence()
            self._dataset.IssuerOfServiceEpisodeIDSequence.clear()
            self._dataset.IssuerOfServiceEpisodeIDSequence.extend([item.to_dataset() for item in value])

    def add_IssuerOfServiceEpisodeID(self, item: IssuerOfServiceEpisodeIDSequenceItem):
        if not isinstance(item, IssuerOfServiceEpisodeIDSequenceItem):
            raise ValueError(f"Item must be an instance of IssuerOfServiceEpisodeIDSequenceItem")
        self._IssuerOfServiceEpisodeIDSequence.append(item)
        if "IssuerOfServiceEpisodeIDSequence" not in self._dataset:
            self._dataset.IssuerOfServiceEpisodeIDSequence = pydicom.Sequence()
        self._dataset.IssuerOfServiceEpisodeIDSequence.append(item.to_dataset())

    @property
    def PatientState(self) -> Optional[str]:
        if "PatientState" in self._dataset:
            return self._dataset.PatientState
        return None

    @PatientState.setter
    def PatientState(self, value: Optional[str]):
        if value is None:
            if "PatientState" in self._dataset:
                del self._dataset.PatientState
        else:
            self._dataset.PatientState = value

    @property
    def Manufacturer(self) -> Optional[str]:
        if "Manufacturer" in self._dataset:
            return self._dataset.Manufacturer
        return None

    @Manufacturer.setter
    def Manufacturer(self, value: Optional[str]):
        if value is None:
            if "Manufacturer" in self._dataset:
                del self._dataset.Manufacturer
        else:
            self._dataset.Manufacturer = value

    @property
    def InstitutionName(self) -> Optional[str]:
        if "InstitutionName" in self._dataset:
            return self._dataset.InstitutionName
        return None

    @InstitutionName.setter
    def InstitutionName(self, value: Optional[str]):
        if value is None:
            if "InstitutionName" in self._dataset:
                del self._dataset.InstitutionName
        else:
            self._dataset.InstitutionName = value

    @property
    def InstitutionAddress(self) -> Optional[str]:
        if "InstitutionAddress" in self._dataset:
            return self._dataset.InstitutionAddress
        return None

    @InstitutionAddress.setter
    def InstitutionAddress(self, value: Optional[str]):
        if value is None:
            if "InstitutionAddress" in self._dataset:
                del self._dataset.InstitutionAddress
        else:
            self._dataset.InstitutionAddress = value

    @property
    def StationName(self) -> Optional[str]:
        if "StationName" in self._dataset:
            return self._dataset.StationName
        return None

    @StationName.setter
    def StationName(self, value: Optional[str]):
        if value is None:
            if "StationName" in self._dataset:
                del self._dataset.StationName
        else:
            self._dataset.StationName = value

    @property
    def InstitutionalDepartmentName(self) -> Optional[str]:
        if "InstitutionalDepartmentName" in self._dataset:
            return self._dataset.InstitutionalDepartmentName
        return None

    @InstitutionalDepartmentName.setter
    def InstitutionalDepartmentName(self, value: Optional[str]):
        if value is None:
            if "InstitutionalDepartmentName" in self._dataset:
                del self._dataset.InstitutionalDepartmentName
        else:
            self._dataset.InstitutionalDepartmentName = value

    @property
    def InstitutionalDepartmentTypeCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "InstitutionalDepartmentTypeCodeSequence" in self._dataset:
            if len(self._InstitutionalDepartmentTypeCodeSequence) == len(
                self._dataset.InstitutionalDepartmentTypeCodeSequence
            ):
                return self._InstitutionalDepartmentTypeCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.InstitutionalDepartmentTypeCodeSequence]
        return None

    @InstitutionalDepartmentTypeCodeSequence.setter
    def InstitutionalDepartmentTypeCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._InstitutionalDepartmentTypeCodeSequence = []
            if "InstitutionalDepartmentTypeCodeSequence" in self._dataset:
                del self._dataset.InstitutionalDepartmentTypeCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError(f"InstitutionalDepartmentTypeCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._InstitutionalDepartmentTypeCodeSequence = value
            if "InstitutionalDepartmentTypeCodeSequence" not in self._dataset:
                self._dataset.InstitutionalDepartmentTypeCodeSequence = pydicom.Sequence()
            self._dataset.InstitutionalDepartmentTypeCodeSequence.clear()
            self._dataset.InstitutionalDepartmentTypeCodeSequence.extend([item.to_dataset() for item in value])

    def add_InstitutionalDepartmentTypeCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError(f"Item must be an instance of CodeSequenceItem")
        self._InstitutionalDepartmentTypeCodeSequence.append(item)
        if "InstitutionalDepartmentTypeCodeSequence" not in self._dataset:
            self._dataset.InstitutionalDepartmentTypeCodeSequence = pydicom.Sequence()
        self._dataset.InstitutionalDepartmentTypeCodeSequence.append(item.to_dataset())

    @property
    def ManufacturerModelName(self) -> Optional[str]:
        if "ManufacturerModelName" in self._dataset:
            return self._dataset.ManufacturerModelName
        return None

    @ManufacturerModelName.setter
    def ManufacturerModelName(self, value: Optional[str]):
        if value is None:
            if "ManufacturerModelName" in self._dataset:
                del self._dataset.ManufacturerModelName
        else:
            self._dataset.ManufacturerModelName = value

    @property
    def DeviceSerialNumber(self) -> Optional[str]:
        if "DeviceSerialNumber" in self._dataset:
            return self._dataset.DeviceSerialNumber
        return None

    @DeviceSerialNumber.setter
    def DeviceSerialNumber(self, value: Optional[str]):
        if value is None:
            if "DeviceSerialNumber" in self._dataset:
                del self._dataset.DeviceSerialNumber
        else:
            self._dataset.DeviceSerialNumber = value

    @property
    def DeviceUID(self) -> Optional[str]:
        if "DeviceUID" in self._dataset:
            return self._dataset.DeviceUID
        return None

    @DeviceUID.setter
    def DeviceUID(self, value: Optional[str]):
        if value is None:
            if "DeviceUID" in self._dataset:
                del self._dataset.DeviceUID
        else:
            self._dataset.DeviceUID = value

    @property
    def GantryID(self) -> Optional[str]:
        if "GantryID" in self._dataset:
            return self._dataset.GantryID
        return None

    @GantryID.setter
    def GantryID(self, value: Optional[str]):
        if value is None:
            if "GantryID" in self._dataset:
                del self._dataset.GantryID
        else:
            self._dataset.GantryID = value

    @property
    def UDISequence(self) -> Optional[List[UDISequenceItem]]:
        if "UDISequence" in self._dataset:
            if len(self._UDISequence) == len(self._dataset.UDISequence):
                return self._UDISequence
            else:
                return [UDISequenceItem(x) for x in self._dataset.UDISequence]
        return None

    @UDISequence.setter
    def UDISequence(self, value: Optional[List[UDISequenceItem]]):
        if value is None:
            self._UDISequence = []
            if "UDISequence" in self._dataset:
                del self._dataset.UDISequence
        elif not isinstance(value, list) or not all(isinstance(item, UDISequenceItem) for item in value):
            raise ValueError(f"UDISequence must be a list of UDISequenceItem objects")
        else:
            self._UDISequence = value
            if "UDISequence" not in self._dataset:
                self._dataset.UDISequence = pydicom.Sequence()
            self._dataset.UDISequence.clear()
            self._dataset.UDISequence.extend([item.to_dataset() for item in value])

    def add_UDI(self, item: UDISequenceItem):
        if not isinstance(item, UDISequenceItem):
            raise ValueError(f"Item must be an instance of UDISequenceItem")
        self._UDISequence.append(item)
        if "UDISequence" not in self._dataset:
            self._dataset.UDISequence = pydicom.Sequence()
        self._dataset.UDISequence.append(item.to_dataset())

    @property
    def ManufacturerDeviceClassUID(self) -> Optional[List[str]]:
        if "ManufacturerDeviceClassUID" in self._dataset:
            return self._dataset.ManufacturerDeviceClassUID
        return None

    @ManufacturerDeviceClassUID.setter
    def ManufacturerDeviceClassUID(self, value: Optional[List[str]]):
        if value is None:
            if "ManufacturerDeviceClassUID" in self._dataset:
                del self._dataset.ManufacturerDeviceClassUID
        else:
            self._dataset.ManufacturerDeviceClassUID = value

    @property
    def SoftwareVersions(self) -> Optional[List[str]]:
        if "SoftwareVersions" in self._dataset:
            return self._dataset.SoftwareVersions
        return None

    @SoftwareVersions.setter
    def SoftwareVersions(self, value: Optional[List[str]]):
        if value is None:
            if "SoftwareVersions" in self._dataset:
                del self._dataset.SoftwareVersions
        else:
            self._dataset.SoftwareVersions = value

    @property
    def SpatialResolution(self) -> Optional[Decimal]:
        if "SpatialResolution" in self._dataset:
            return self._dataset.SpatialResolution
        return None

    @SpatialResolution.setter
    def SpatialResolution(self, value: Optional[Decimal]):
        if value is None:
            if "SpatialResolution" in self._dataset:
                del self._dataset.SpatialResolution
        else:
            self._dataset.SpatialResolution = value

    @property
    def DateOfLastCalibration(self) -> Optional[List[str]]:
        if "DateOfLastCalibration" in self._dataset:
            return self._dataset.DateOfLastCalibration
        return None

    @DateOfLastCalibration.setter
    def DateOfLastCalibration(self, value: Optional[List[str]]):
        if value is None:
            if "DateOfLastCalibration" in self._dataset:
                del self._dataset.DateOfLastCalibration
        else:
            self._dataset.DateOfLastCalibration = value

    @property
    def TimeOfLastCalibration(self) -> Optional[List[str]]:
        if "TimeOfLastCalibration" in self._dataset:
            return self._dataset.TimeOfLastCalibration
        return None

    @TimeOfLastCalibration.setter
    def TimeOfLastCalibration(self, value: Optional[List[str]]):
        if value is None:
            if "TimeOfLastCalibration" in self._dataset:
                del self._dataset.TimeOfLastCalibration
        else:
            self._dataset.TimeOfLastCalibration = value

    @property
    def DateOfManufacture(self) -> Optional[str]:
        if "DateOfManufacture" in self._dataset:
            return self._dataset.DateOfManufacture
        return None

    @DateOfManufacture.setter
    def DateOfManufacture(self, value: Optional[str]):
        if value is None:
            if "DateOfManufacture" in self._dataset:
                del self._dataset.DateOfManufacture
        else:
            self._dataset.DateOfManufacture = value

    @property
    def DateOfInstallation(self) -> Optional[str]:
        if "DateOfInstallation" in self._dataset:
            return self._dataset.DateOfInstallation
        return None

    @DateOfInstallation.setter
    def DateOfInstallation(self, value: Optional[str]):
        if value is None:
            if "DateOfInstallation" in self._dataset:
                del self._dataset.DateOfInstallation
        else:
            self._dataset.DateOfInstallation = value

    @property
    def PixelPaddingValue(self) -> Optional[int]:
        if "PixelPaddingValue" in self._dataset:
            return self._dataset.PixelPaddingValue
        return None

    @PixelPaddingValue.setter
    def PixelPaddingValue(self, value: Optional[int]):
        if value is None:
            if "PixelPaddingValue" in self._dataset:
                del self._dataset.PixelPaddingValue
        else:
            self._dataset.PixelPaddingValue = value

    @property
    def BeamTaskSequence(self) -> Optional[List[BeamTaskSequenceItem]]:
        if "BeamTaskSequence" in self._dataset:
            if len(self._BeamTaskSequence) == len(self._dataset.BeamTaskSequence):
                return self._BeamTaskSequence
            else:
                return [BeamTaskSequenceItem(x) for x in self._dataset.BeamTaskSequence]
        return None

    @BeamTaskSequence.setter
    def BeamTaskSequence(self, value: Optional[List[BeamTaskSequenceItem]]):
        if value is None:
            self._BeamTaskSequence = []
            if "BeamTaskSequence" in self._dataset:
                del self._dataset.BeamTaskSequence
        elif not isinstance(value, list) or not all(isinstance(item, BeamTaskSequenceItem) for item in value):
            raise ValueError(f"BeamTaskSequence must be a list of BeamTaskSequenceItem objects")
        else:
            self._BeamTaskSequence = value
            if "BeamTaskSequence" not in self._dataset:
                self._dataset.BeamTaskSequence = pydicom.Sequence()
            self._dataset.BeamTaskSequence.clear()
            self._dataset.BeamTaskSequence.extend([item.to_dataset() for item in value])

    def add_BeamTask(self, item: BeamTaskSequenceItem):
        if not isinstance(item, BeamTaskSequenceItem):
            raise ValueError(f"Item must be an instance of BeamTaskSequenceItem")
        self._BeamTaskSequence.append(item)
        if "BeamTaskSequence" not in self._dataset:
            self._dataset.BeamTaskSequence = pydicom.Sequence()
        self._dataset.BeamTaskSequence.append(item.to_dataset())

    @property
    def ReferencedRTPlanSequence(self) -> Optional[List[ReferencedRTPlanSequenceItem]]:
        if "ReferencedRTPlanSequence" in self._dataset:
            if len(self._ReferencedRTPlanSequence) == len(self._dataset.ReferencedRTPlanSequence):
                return self._ReferencedRTPlanSequence
            else:
                return [ReferencedRTPlanSequenceItem(x) for x in self._dataset.ReferencedRTPlanSequence]
        return None

    @ReferencedRTPlanSequence.setter
    def ReferencedRTPlanSequence(self, value: Optional[List[ReferencedRTPlanSequenceItem]]):
        if value is None:
            self._ReferencedRTPlanSequence = []
            if "ReferencedRTPlanSequence" in self._dataset:
                del self._dataset.ReferencedRTPlanSequence
        elif not isinstance(value, list) or not all(isinstance(item, ReferencedRTPlanSequenceItem) for item in value):
            raise ValueError(f"ReferencedRTPlanSequence must be a list of ReferencedRTPlanSequenceItem objects")
        else:
            self._ReferencedRTPlanSequence = value
            if "ReferencedRTPlanSequence" not in self._dataset:
                self._dataset.ReferencedRTPlanSequence = pydicom.Sequence()
            self._dataset.ReferencedRTPlanSequence.clear()
            self._dataset.ReferencedRTPlanSequence.extend([item.to_dataset() for item in value])

    def add_ReferencedRTPlan(self, item: ReferencedRTPlanSequenceItem):
        if not isinstance(item, ReferencedRTPlanSequenceItem):
            raise ValueError(f"Item must be an instance of ReferencedRTPlanSequenceItem")
        self._ReferencedRTPlanSequence.append(item)
        if "ReferencedRTPlanSequence" not in self._dataset:
            self._dataset.ReferencedRTPlanSequence = pydicom.Sequence()
        self._dataset.ReferencedRTPlanSequence.append(item.to_dataset())

    @property
    def OmittedBeamTaskSequence(self) -> Optional[List[OmittedBeamTaskSequenceItem]]:
        if "OmittedBeamTaskSequence" in self._dataset:
            if len(self._OmittedBeamTaskSequence) == len(self._dataset.OmittedBeamTaskSequence):
                return self._OmittedBeamTaskSequence
            else:
                return [OmittedBeamTaskSequenceItem(x) for x in self._dataset.OmittedBeamTaskSequence]
        return None

    @OmittedBeamTaskSequence.setter
    def OmittedBeamTaskSequence(self, value: Optional[List[OmittedBeamTaskSequenceItem]]):
        if value is None:
            self._OmittedBeamTaskSequence = []
            if "OmittedBeamTaskSequence" in self._dataset:
                del self._dataset.OmittedBeamTaskSequence
        elif not isinstance(value, list) or not all(isinstance(item, OmittedBeamTaskSequenceItem) for item in value):
            raise ValueError(f"OmittedBeamTaskSequence must be a list of OmittedBeamTaskSequenceItem objects")
        else:
            self._OmittedBeamTaskSequence = value
            if "OmittedBeamTaskSequence" not in self._dataset:
                self._dataset.OmittedBeamTaskSequence = pydicom.Sequence()
            self._dataset.OmittedBeamTaskSequence.clear()
            self._dataset.OmittedBeamTaskSequence.extend([item.to_dataset() for item in value])

    def add_OmittedBeamTask(self, item: OmittedBeamTaskSequenceItem):
        if not isinstance(item, OmittedBeamTaskSequenceItem):
            raise ValueError(f"Item must be an instance of OmittedBeamTaskSequenceItem")
        self._OmittedBeamTaskSequence.append(item)
        if "OmittedBeamTaskSequence" not in self._dataset:
            self._dataset.OmittedBeamTaskSequence = pydicom.Sequence()
        self._dataset.OmittedBeamTaskSequence.append(item.to_dataset())

    @property
    def ReferencedPatientSequence(self) -> Optional[List[ReferencedPatientSequenceItem]]:
        if "ReferencedPatientSequence" in self._dataset:
            if len(self._ReferencedPatientSequence) == len(self._dataset.ReferencedPatientSequence):
                return self._ReferencedPatientSequence
            else:
                return [ReferencedPatientSequenceItem(x) for x in self._dataset.ReferencedPatientSequence]
        return None

    @ReferencedPatientSequence.setter
    def ReferencedPatientSequence(self, value: Optional[List[ReferencedPatientSequenceItem]]):
        if value is None:
            self._ReferencedPatientSequence = []
            if "ReferencedPatientSequence" in self._dataset:
                del self._dataset.ReferencedPatientSequence
        elif not isinstance(value, list) or not all(isinstance(item, ReferencedPatientSequenceItem) for item in value):
            raise ValueError(f"ReferencedPatientSequence must be a list of ReferencedPatientSequenceItem objects")
        else:
            self._ReferencedPatientSequence = value
            if "ReferencedPatientSequence" not in self._dataset:
                self._dataset.ReferencedPatientSequence = pydicom.Sequence()
            self._dataset.ReferencedPatientSequence.clear()
            self._dataset.ReferencedPatientSequence.extend([item.to_dataset() for item in value])

    def add_ReferencedPatient(self, item: ReferencedPatientSequenceItem):
        if not isinstance(item, ReferencedPatientSequenceItem):
            raise ValueError(f"Item must be an instance of ReferencedPatientSequenceItem")
        self._ReferencedPatientSequence.append(item)
        if "ReferencedPatientSequence" not in self._dataset:
            self._dataset.ReferencedPatientSequence = pydicom.Sequence()
        self._dataset.ReferencedPatientSequence.append(item.to_dataset())

    @property
    def PatientName(self) -> Optional[str]:
        if "PatientName" in self._dataset:
            return self._dataset.PatientName
        return None

    @PatientName.setter
    def PatientName(self, value: Optional[str]):
        if value is None:
            if "PatientName" in self._dataset:
                del self._dataset.PatientName
        else:
            self._dataset.PatientName = value

    @property
    def PatientID(self) -> Optional[str]:
        if "PatientID" in self._dataset:
            return self._dataset.PatientID
        return None

    @PatientID.setter
    def PatientID(self, value: Optional[str]):
        if value is None:
            if "PatientID" in self._dataset:
                del self._dataset.PatientID
        else:
            self._dataset.PatientID = value

    @property
    def IssuerOfPatientID(self) -> Optional[str]:
        if "IssuerOfPatientID" in self._dataset:
            return self._dataset.IssuerOfPatientID
        return None

    @IssuerOfPatientID.setter
    def IssuerOfPatientID(self, value: Optional[str]):
        if value is None:
            if "IssuerOfPatientID" in self._dataset:
                del self._dataset.IssuerOfPatientID
        else:
            self._dataset.IssuerOfPatientID = value

    @property
    def TypeOfPatientID(self) -> Optional[str]:
        if "TypeOfPatientID" in self._dataset:
            return self._dataset.TypeOfPatientID
        return None

    @TypeOfPatientID.setter
    def TypeOfPatientID(self, value: Optional[str]):
        if value is None:
            if "TypeOfPatientID" in self._dataset:
                del self._dataset.TypeOfPatientID
        else:
            self._dataset.TypeOfPatientID = value

    @property
    def IssuerOfPatientIDQualifiersSequence(self) -> Optional[List[IssuerOfPatientIDQualifiersSequenceItem]]:
        if "IssuerOfPatientIDQualifiersSequence" in self._dataset:
            if len(self._IssuerOfPatientIDQualifiersSequence) == len(self._dataset.IssuerOfPatientIDQualifiersSequence):
                return self._IssuerOfPatientIDQualifiersSequence
            else:
                return [IssuerOfPatientIDQualifiersSequenceItem(x) for x in self._dataset.IssuerOfPatientIDQualifiersSequence]
        return None

    @IssuerOfPatientIDQualifiersSequence.setter
    def IssuerOfPatientIDQualifiersSequence(self, value: Optional[List[IssuerOfPatientIDQualifiersSequenceItem]]):
        if value is None:
            self._IssuerOfPatientIDQualifiersSequence = []
            if "IssuerOfPatientIDQualifiersSequence" in self._dataset:
                del self._dataset.IssuerOfPatientIDQualifiersSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, IssuerOfPatientIDQualifiersSequenceItem) for item in value
        ):
            raise ValueError(
                f"IssuerOfPatientIDQualifiersSequence must be a list of IssuerOfPatientIDQualifiersSequenceItem objects"
            )
        else:
            self._IssuerOfPatientIDQualifiersSequence = value
            if "IssuerOfPatientIDQualifiersSequence" not in self._dataset:
                self._dataset.IssuerOfPatientIDQualifiersSequence = pydicom.Sequence()
            self._dataset.IssuerOfPatientIDQualifiersSequence.clear()
            self._dataset.IssuerOfPatientIDQualifiersSequence.extend([item.to_dataset() for item in value])

    def add_IssuerOfPatientIDQualifiers(self, item: IssuerOfPatientIDQualifiersSequenceItem):
        if not isinstance(item, IssuerOfPatientIDQualifiersSequenceItem):
            raise ValueError(f"Item must be an instance of IssuerOfPatientIDQualifiersSequenceItem")
        self._IssuerOfPatientIDQualifiersSequence.append(item)
        if "IssuerOfPatientIDQualifiersSequence" not in self._dataset:
            self._dataset.IssuerOfPatientIDQualifiersSequence = pydicom.Sequence()
        self._dataset.IssuerOfPatientIDQualifiersSequence.append(item.to_dataset())

    @property
    def SourcePatientGroupIdentificationSequence(self) -> Optional[List[SourcePatientGroupIdentificationSequenceItem]]:
        if "SourcePatientGroupIdentificationSequence" in self._dataset:
            if len(self._SourcePatientGroupIdentificationSequence) == len(
                self._dataset.SourcePatientGroupIdentificationSequence
            ):
                return self._SourcePatientGroupIdentificationSequence
            else:
                return [
                    SourcePatientGroupIdentificationSequenceItem(x)
                    for x in self._dataset.SourcePatientGroupIdentificationSequence
                ]
        return None

    @SourcePatientGroupIdentificationSequence.setter
    def SourcePatientGroupIdentificationSequence(self, value: Optional[List[SourcePatientGroupIdentificationSequenceItem]]):
        if value is None:
            self._SourcePatientGroupIdentificationSequence = []
            if "SourcePatientGroupIdentificationSequence" in self._dataset:
                del self._dataset.SourcePatientGroupIdentificationSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, SourcePatientGroupIdentificationSequenceItem) for item in value
        ):
            raise ValueError(
                f"SourcePatientGroupIdentificationSequence must be a list of SourcePatientGroupIdentificationSequenceItem objects"
            )
        else:
            self._SourcePatientGroupIdentificationSequence = value
            if "SourcePatientGroupIdentificationSequence" not in self._dataset:
                self._dataset.SourcePatientGroupIdentificationSequence = pydicom.Sequence()
            self._dataset.SourcePatientGroupIdentificationSequence.clear()
            self._dataset.SourcePatientGroupIdentificationSequence.extend([item.to_dataset() for item in value])

    def add_SourcePatientGroupIdentification(self, item: SourcePatientGroupIdentificationSequenceItem):
        if not isinstance(item, SourcePatientGroupIdentificationSequenceItem):
            raise ValueError(f"Item must be an instance of SourcePatientGroupIdentificationSequenceItem")
        self._SourcePatientGroupIdentificationSequence.append(item)
        if "SourcePatientGroupIdentificationSequence" not in self._dataset:
            self._dataset.SourcePatientGroupIdentificationSequence = pydicom.Sequence()
        self._dataset.SourcePatientGroupIdentificationSequence.append(item.to_dataset())

    @property
    def GroupOfPatientsIdentificationSequence(self) -> Optional[List[GroupOfPatientsIdentificationSequenceItem]]:
        if "GroupOfPatientsIdentificationSequence" in self._dataset:
            if len(self._GroupOfPatientsIdentificationSequence) == len(self._dataset.GroupOfPatientsIdentificationSequence):
                return self._GroupOfPatientsIdentificationSequence
            else:
                return [
                    GroupOfPatientsIdentificationSequenceItem(x) for x in self._dataset.GroupOfPatientsIdentificationSequence
                ]
        return None

    @GroupOfPatientsIdentificationSequence.setter
    def GroupOfPatientsIdentificationSequence(self, value: Optional[List[GroupOfPatientsIdentificationSequenceItem]]):
        if value is None:
            self._GroupOfPatientsIdentificationSequence = []
            if "GroupOfPatientsIdentificationSequence" in self._dataset:
                del self._dataset.GroupOfPatientsIdentificationSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, GroupOfPatientsIdentificationSequenceItem) for item in value
        ):
            raise ValueError(
                f"GroupOfPatientsIdentificationSequence must be a list of GroupOfPatientsIdentificationSequenceItem objects"
            )
        else:
            self._GroupOfPatientsIdentificationSequence = value
            if "GroupOfPatientsIdentificationSequence" not in self._dataset:
                self._dataset.GroupOfPatientsIdentificationSequence = pydicom.Sequence()
            self._dataset.GroupOfPatientsIdentificationSequence.clear()
            self._dataset.GroupOfPatientsIdentificationSequence.extend([item.to_dataset() for item in value])

    def add_GroupOfPatientsIdentification(self, item: GroupOfPatientsIdentificationSequenceItem):
        if not isinstance(item, GroupOfPatientsIdentificationSequenceItem):
            raise ValueError(f"Item must be an instance of GroupOfPatientsIdentificationSequenceItem")
        self._GroupOfPatientsIdentificationSequence.append(item)
        if "GroupOfPatientsIdentificationSequence" not in self._dataset:
            self._dataset.GroupOfPatientsIdentificationSequence = pydicom.Sequence()
        self._dataset.GroupOfPatientsIdentificationSequence.append(item.to_dataset())

    @property
    def PatientBirthDate(self) -> Optional[str]:
        if "PatientBirthDate" in self._dataset:
            return self._dataset.PatientBirthDate
        return None

    @PatientBirthDate.setter
    def PatientBirthDate(self, value: Optional[str]):
        if value is None:
            if "PatientBirthDate" in self._dataset:
                del self._dataset.PatientBirthDate
        else:
            self._dataset.PatientBirthDate = value

    @property
    def PatientBirthTime(self) -> Optional[str]:
        if "PatientBirthTime" in self._dataset:
            return self._dataset.PatientBirthTime
        return None

    @PatientBirthTime.setter
    def PatientBirthTime(self, value: Optional[str]):
        if value is None:
            if "PatientBirthTime" in self._dataset:
                del self._dataset.PatientBirthTime
        else:
            self._dataset.PatientBirthTime = value

    @property
    def PatientBirthDateInAlternativeCalendar(self) -> Optional[str]:
        if "PatientBirthDateInAlternativeCalendar" in self._dataset:
            return self._dataset.PatientBirthDateInAlternativeCalendar
        return None

    @PatientBirthDateInAlternativeCalendar.setter
    def PatientBirthDateInAlternativeCalendar(self, value: Optional[str]):
        if value is None:
            if "PatientBirthDateInAlternativeCalendar" in self._dataset:
                del self._dataset.PatientBirthDateInAlternativeCalendar
        else:
            self._dataset.PatientBirthDateInAlternativeCalendar = value

    @property
    def PatientDeathDateInAlternativeCalendar(self) -> Optional[str]:
        if "PatientDeathDateInAlternativeCalendar" in self._dataset:
            return self._dataset.PatientDeathDateInAlternativeCalendar
        return None

    @PatientDeathDateInAlternativeCalendar.setter
    def PatientDeathDateInAlternativeCalendar(self, value: Optional[str]):
        if value is None:
            if "PatientDeathDateInAlternativeCalendar" in self._dataset:
                del self._dataset.PatientDeathDateInAlternativeCalendar
        else:
            self._dataset.PatientDeathDateInAlternativeCalendar = value

    @property
    def PatientAlternativeCalendar(self) -> Optional[str]:
        if "PatientAlternativeCalendar" in self._dataset:
            return self._dataset.PatientAlternativeCalendar
        return None

    @PatientAlternativeCalendar.setter
    def PatientAlternativeCalendar(self, value: Optional[str]):
        if value is None:
            if "PatientAlternativeCalendar" in self._dataset:
                del self._dataset.PatientAlternativeCalendar
        else:
            self._dataset.PatientAlternativeCalendar = value

    @property
    def PatientSex(self) -> Optional[str]:
        if "PatientSex" in self._dataset:
            return self._dataset.PatientSex
        return None

    @PatientSex.setter
    def PatientSex(self, value: Optional[str]):
        if value is None:
            if "PatientSex" in self._dataset:
                del self._dataset.PatientSex
        else:
            self._dataset.PatientSex = value

    @property
    def QualityControlSubject(self) -> Optional[str]:
        if "QualityControlSubject" in self._dataset:
            return self._dataset.QualityControlSubject
        return None

    @QualityControlSubject.setter
    def QualityControlSubject(self, value: Optional[str]):
        if value is None:
            if "QualityControlSubject" in self._dataset:
                del self._dataset.QualityControlSubject
        else:
            self._dataset.QualityControlSubject = value

    @property
    def StrainDescription(self) -> Optional[str]:
        if "StrainDescription" in self._dataset:
            return self._dataset.StrainDescription
        return None

    @StrainDescription.setter
    def StrainDescription(self, value: Optional[str]):
        if value is None:
            if "StrainDescription" in self._dataset:
                del self._dataset.StrainDescription
        else:
            self._dataset.StrainDescription = value

    @property
    def StrainNomenclature(self) -> Optional[str]:
        if "StrainNomenclature" in self._dataset:
            return self._dataset.StrainNomenclature
        return None

    @StrainNomenclature.setter
    def StrainNomenclature(self, value: Optional[str]):
        if value is None:
            if "StrainNomenclature" in self._dataset:
                del self._dataset.StrainNomenclature
        else:
            self._dataset.StrainNomenclature = value

    @property
    def StrainStockSequence(self) -> Optional[List[StrainStockSequenceItem]]:
        if "StrainStockSequence" in self._dataset:
            if len(self._StrainStockSequence) == len(self._dataset.StrainStockSequence):
                return self._StrainStockSequence
            else:
                return [StrainStockSequenceItem(x) for x in self._dataset.StrainStockSequence]
        return None

    @StrainStockSequence.setter
    def StrainStockSequence(self, value: Optional[List[StrainStockSequenceItem]]):
        if value is None:
            self._StrainStockSequence = []
            if "StrainStockSequence" in self._dataset:
                del self._dataset.StrainStockSequence
        elif not isinstance(value, list) or not all(isinstance(item, StrainStockSequenceItem) for item in value):
            raise ValueError(f"StrainStockSequence must be a list of StrainStockSequenceItem objects")
        else:
            self._StrainStockSequence = value
            if "StrainStockSequence" not in self._dataset:
                self._dataset.StrainStockSequence = pydicom.Sequence()
            self._dataset.StrainStockSequence.clear()
            self._dataset.StrainStockSequence.extend([item.to_dataset() for item in value])

    def add_StrainStock(self, item: StrainStockSequenceItem):
        if not isinstance(item, StrainStockSequenceItem):
            raise ValueError(f"Item must be an instance of StrainStockSequenceItem")
        self._StrainStockSequence.append(item)
        if "StrainStockSequence" not in self._dataset:
            self._dataset.StrainStockSequence = pydicom.Sequence()
        self._dataset.StrainStockSequence.append(item.to_dataset())

    @property
    def StrainAdditionalInformation(self) -> Optional[str]:
        if "StrainAdditionalInformation" in self._dataset:
            return self._dataset.StrainAdditionalInformation
        return None

    @StrainAdditionalInformation.setter
    def StrainAdditionalInformation(self, value: Optional[str]):
        if value is None:
            if "StrainAdditionalInformation" in self._dataset:
                del self._dataset.StrainAdditionalInformation
        else:
            self._dataset.StrainAdditionalInformation = value

    @property
    def StrainCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "StrainCodeSequence" in self._dataset:
            if len(self._StrainCodeSequence) == len(self._dataset.StrainCodeSequence):
                return self._StrainCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.StrainCodeSequence]
        return None

    @StrainCodeSequence.setter
    def StrainCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._StrainCodeSequence = []
            if "StrainCodeSequence" in self._dataset:
                del self._dataset.StrainCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError(f"StrainCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._StrainCodeSequence = value
            if "StrainCodeSequence" not in self._dataset:
                self._dataset.StrainCodeSequence = pydicom.Sequence()
            self._dataset.StrainCodeSequence.clear()
            self._dataset.StrainCodeSequence.extend([item.to_dataset() for item in value])

    def add_StrainCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError(f"Item must be an instance of CodeSequenceItem")
        self._StrainCodeSequence.append(item)
        if "StrainCodeSequence" not in self._dataset:
            self._dataset.StrainCodeSequence = pydicom.Sequence()
        self._dataset.StrainCodeSequence.append(item.to_dataset())

    @property
    def GeneticModificationsSequence(self) -> Optional[List[GeneticModificationsSequenceItem]]:
        if "GeneticModificationsSequence" in self._dataset:
            if len(self._GeneticModificationsSequence) == len(self._dataset.GeneticModificationsSequence):
                return self._GeneticModificationsSequence
            else:
                return [GeneticModificationsSequenceItem(x) for x in self._dataset.GeneticModificationsSequence]
        return None

    @GeneticModificationsSequence.setter
    def GeneticModificationsSequence(self, value: Optional[List[GeneticModificationsSequenceItem]]):
        if value is None:
            self._GeneticModificationsSequence = []
            if "GeneticModificationsSequence" in self._dataset:
                del self._dataset.GeneticModificationsSequence
        elif not isinstance(value, list) or not all(isinstance(item, GeneticModificationsSequenceItem) for item in value):
            raise ValueError(f"GeneticModificationsSequence must be a list of GeneticModificationsSequenceItem objects")
        else:
            self._GeneticModificationsSequence = value
            if "GeneticModificationsSequence" not in self._dataset:
                self._dataset.GeneticModificationsSequence = pydicom.Sequence()
            self._dataset.GeneticModificationsSequence.clear()
            self._dataset.GeneticModificationsSequence.extend([item.to_dataset() for item in value])

    def add_GeneticModifications(self, item: GeneticModificationsSequenceItem):
        if not isinstance(item, GeneticModificationsSequenceItem):
            raise ValueError(f"Item must be an instance of GeneticModificationsSequenceItem")
        self._GeneticModificationsSequence.append(item)
        if "GeneticModificationsSequence" not in self._dataset:
            self._dataset.GeneticModificationsSequence = pydicom.Sequence()
        self._dataset.GeneticModificationsSequence.append(item.to_dataset())

    @property
    def OtherPatientNames(self) -> Optional[List[str]]:
        if "OtherPatientNames" in self._dataset:
            return self._dataset.OtherPatientNames
        return None

    @OtherPatientNames.setter
    def OtherPatientNames(self, value: Optional[List[str]]):
        if value is None:
            if "OtherPatientNames" in self._dataset:
                del self._dataset.OtherPatientNames
        else:
            self._dataset.OtherPatientNames = value

    @property
    def OtherPatientIDsSequence(self) -> Optional[List[OtherPatientIDsSequenceItem]]:
        if "OtherPatientIDsSequence" in self._dataset:
            if len(self._OtherPatientIDsSequence) == len(self._dataset.OtherPatientIDsSequence):
                return self._OtherPatientIDsSequence
            else:
                return [OtherPatientIDsSequenceItem(x) for x in self._dataset.OtherPatientIDsSequence]
        return None

    @OtherPatientIDsSequence.setter
    def OtherPatientIDsSequence(self, value: Optional[List[OtherPatientIDsSequenceItem]]):
        if value is None:
            self._OtherPatientIDsSequence = []
            if "OtherPatientIDsSequence" in self._dataset:
                del self._dataset.OtherPatientIDsSequence
        elif not isinstance(value, list) or not all(isinstance(item, OtherPatientIDsSequenceItem) for item in value):
            raise ValueError(f"OtherPatientIDsSequence must be a list of OtherPatientIDsSequenceItem objects")
        else:
            self._OtherPatientIDsSequence = value
            if "OtherPatientIDsSequence" not in self._dataset:
                self._dataset.OtherPatientIDsSequence = pydicom.Sequence()
            self._dataset.OtherPatientIDsSequence.clear()
            self._dataset.OtherPatientIDsSequence.extend([item.to_dataset() for item in value])

    def add_OtherPatientIDs(self, item: OtherPatientIDsSequenceItem):
        if not isinstance(item, OtherPatientIDsSequenceItem):
            raise ValueError(f"Item must be an instance of OtherPatientIDsSequenceItem")
        self._OtherPatientIDsSequence.append(item)
        if "OtherPatientIDsSequence" not in self._dataset:
            self._dataset.OtherPatientIDsSequence = pydicom.Sequence()
        self._dataset.OtherPatientIDsSequence.append(item.to_dataset())

    @property
    def ReferencedPatientPhotoSequence(self) -> Optional[List[ReferencedPatientPhotoSequenceItem]]:
        if "ReferencedPatientPhotoSequence" in self._dataset:
            if len(self._ReferencedPatientPhotoSequence) == len(self._dataset.ReferencedPatientPhotoSequence):
                return self._ReferencedPatientPhotoSequence
            else:
                return [ReferencedPatientPhotoSequenceItem(x) for x in self._dataset.ReferencedPatientPhotoSequence]
        return None

    @ReferencedPatientPhotoSequence.setter
    def ReferencedPatientPhotoSequence(self, value: Optional[List[ReferencedPatientPhotoSequenceItem]]):
        if value is None:
            self._ReferencedPatientPhotoSequence = []
            if "ReferencedPatientPhotoSequence" in self._dataset:
                del self._dataset.ReferencedPatientPhotoSequence
        elif not isinstance(value, list) or not all(isinstance(item, ReferencedPatientPhotoSequenceItem) for item in value):
            raise ValueError(f"ReferencedPatientPhotoSequence must be a list of ReferencedPatientPhotoSequenceItem objects")
        else:
            self._ReferencedPatientPhotoSequence = value
            if "ReferencedPatientPhotoSequence" not in self._dataset:
                self._dataset.ReferencedPatientPhotoSequence = pydicom.Sequence()
            self._dataset.ReferencedPatientPhotoSequence.clear()
            self._dataset.ReferencedPatientPhotoSequence.extend([item.to_dataset() for item in value])

    def add_ReferencedPatientPhoto(self, item: ReferencedPatientPhotoSequenceItem):
        if not isinstance(item, ReferencedPatientPhotoSequenceItem):
            raise ValueError(f"Item must be an instance of ReferencedPatientPhotoSequenceItem")
        self._ReferencedPatientPhotoSequence.append(item)
        if "ReferencedPatientPhotoSequence" not in self._dataset:
            self._dataset.ReferencedPatientPhotoSequence = pydicom.Sequence()
        self._dataset.ReferencedPatientPhotoSequence.append(item.to_dataset())

    @property
    def EthnicGroup(self) -> Optional[str]:
        if "EthnicGroup" in self._dataset:
            return self._dataset.EthnicGroup
        return None

    @EthnicGroup.setter
    def EthnicGroup(self, value: Optional[str]):
        if value is None:
            if "EthnicGroup" in self._dataset:
                del self._dataset.EthnicGroup
        else:
            self._dataset.EthnicGroup = value

    @property
    def PatientSpeciesDescription(self) -> Optional[str]:
        if "PatientSpeciesDescription" in self._dataset:
            return self._dataset.PatientSpeciesDescription
        return None

    @PatientSpeciesDescription.setter
    def PatientSpeciesDescription(self, value: Optional[str]):
        if value is None:
            if "PatientSpeciesDescription" in self._dataset:
                del self._dataset.PatientSpeciesDescription
        else:
            self._dataset.PatientSpeciesDescription = value

    @property
    def PatientSpeciesCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "PatientSpeciesCodeSequence" in self._dataset:
            if len(self._PatientSpeciesCodeSequence) == len(self._dataset.PatientSpeciesCodeSequence):
                return self._PatientSpeciesCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.PatientSpeciesCodeSequence]
        return None

    @PatientSpeciesCodeSequence.setter
    def PatientSpeciesCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._PatientSpeciesCodeSequence = []
            if "PatientSpeciesCodeSequence" in self._dataset:
                del self._dataset.PatientSpeciesCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError(f"PatientSpeciesCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._PatientSpeciesCodeSequence = value
            if "PatientSpeciesCodeSequence" not in self._dataset:
                self._dataset.PatientSpeciesCodeSequence = pydicom.Sequence()
            self._dataset.PatientSpeciesCodeSequence.clear()
            self._dataset.PatientSpeciesCodeSequence.extend([item.to_dataset() for item in value])

    def add_PatientSpeciesCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError(f"Item must be an instance of CodeSequenceItem")
        self._PatientSpeciesCodeSequence.append(item)
        if "PatientSpeciesCodeSequence" not in self._dataset:
            self._dataset.PatientSpeciesCodeSequence = pydicom.Sequence()
        self._dataset.PatientSpeciesCodeSequence.append(item.to_dataset())

    @property
    def PatientBreedDescription(self) -> Optional[str]:
        if "PatientBreedDescription" in self._dataset:
            return self._dataset.PatientBreedDescription
        return None

    @PatientBreedDescription.setter
    def PatientBreedDescription(self, value: Optional[str]):
        if value is None:
            if "PatientBreedDescription" in self._dataset:
                del self._dataset.PatientBreedDescription
        else:
            self._dataset.PatientBreedDescription = value

    @property
    def PatientBreedCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "PatientBreedCodeSequence" in self._dataset:
            if len(self._PatientBreedCodeSequence) == len(self._dataset.PatientBreedCodeSequence):
                return self._PatientBreedCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.PatientBreedCodeSequence]
        return None

    @PatientBreedCodeSequence.setter
    def PatientBreedCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._PatientBreedCodeSequence = []
            if "PatientBreedCodeSequence" in self._dataset:
                del self._dataset.PatientBreedCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError(f"PatientBreedCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._PatientBreedCodeSequence = value
            if "PatientBreedCodeSequence" not in self._dataset:
                self._dataset.PatientBreedCodeSequence = pydicom.Sequence()
            self._dataset.PatientBreedCodeSequence.clear()
            self._dataset.PatientBreedCodeSequence.extend([item.to_dataset() for item in value])

    def add_PatientBreedCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError(f"Item must be an instance of CodeSequenceItem")
        self._PatientBreedCodeSequence.append(item)
        if "PatientBreedCodeSequence" not in self._dataset:
            self._dataset.PatientBreedCodeSequence = pydicom.Sequence()
        self._dataset.PatientBreedCodeSequence.append(item.to_dataset())

    @property
    def BreedRegistrationSequence(self) -> Optional[List[BreedRegistrationSequenceItem]]:
        if "BreedRegistrationSequence" in self._dataset:
            if len(self._BreedRegistrationSequence) == len(self._dataset.BreedRegistrationSequence):
                return self._BreedRegistrationSequence
            else:
                return [BreedRegistrationSequenceItem(x) for x in self._dataset.BreedRegistrationSequence]
        return None

    @BreedRegistrationSequence.setter
    def BreedRegistrationSequence(self, value: Optional[List[BreedRegistrationSequenceItem]]):
        if value is None:
            self._BreedRegistrationSequence = []
            if "BreedRegistrationSequence" in self._dataset:
                del self._dataset.BreedRegistrationSequence
        elif not isinstance(value, list) or not all(isinstance(item, BreedRegistrationSequenceItem) for item in value):
            raise ValueError(f"BreedRegistrationSequence must be a list of BreedRegistrationSequenceItem objects")
        else:
            self._BreedRegistrationSequence = value
            if "BreedRegistrationSequence" not in self._dataset:
                self._dataset.BreedRegistrationSequence = pydicom.Sequence()
            self._dataset.BreedRegistrationSequence.clear()
            self._dataset.BreedRegistrationSequence.extend([item.to_dataset() for item in value])

    def add_BreedRegistration(self, item: BreedRegistrationSequenceItem):
        if not isinstance(item, BreedRegistrationSequenceItem):
            raise ValueError(f"Item must be an instance of BreedRegistrationSequenceItem")
        self._BreedRegistrationSequence.append(item)
        if "BreedRegistrationSequence" not in self._dataset:
            self._dataset.BreedRegistrationSequence = pydicom.Sequence()
        self._dataset.BreedRegistrationSequence.append(item.to_dataset())

    @property
    def ResponsiblePerson(self) -> Optional[str]:
        if "ResponsiblePerson" in self._dataset:
            return self._dataset.ResponsiblePerson
        return None

    @ResponsiblePerson.setter
    def ResponsiblePerson(self, value: Optional[str]):
        if value is None:
            if "ResponsiblePerson" in self._dataset:
                del self._dataset.ResponsiblePerson
        else:
            self._dataset.ResponsiblePerson = value

    @property
    def ResponsiblePersonRole(self) -> Optional[str]:
        if "ResponsiblePersonRole" in self._dataset:
            return self._dataset.ResponsiblePersonRole
        return None

    @ResponsiblePersonRole.setter
    def ResponsiblePersonRole(self, value: Optional[str]):
        if value is None:
            if "ResponsiblePersonRole" in self._dataset:
                del self._dataset.ResponsiblePersonRole
        else:
            self._dataset.ResponsiblePersonRole = value

    @property
    def ResponsibleOrganization(self) -> Optional[str]:
        if "ResponsibleOrganization" in self._dataset:
            return self._dataset.ResponsibleOrganization
        return None

    @ResponsibleOrganization.setter
    def ResponsibleOrganization(self, value: Optional[str]):
        if value is None:
            if "ResponsibleOrganization" in self._dataset:
                del self._dataset.ResponsibleOrganization
        else:
            self._dataset.ResponsibleOrganization = value

    @property
    def PatientComments(self) -> Optional[str]:
        if "PatientComments" in self._dataset:
            return self._dataset.PatientComments
        return None

    @PatientComments.setter
    def PatientComments(self, value: Optional[str]):
        if value is None:
            if "PatientComments" in self._dataset:
                del self._dataset.PatientComments
        else:
            self._dataset.PatientComments = value

    @property
    def PatientIdentityRemoved(self) -> Optional[str]:
        if "PatientIdentityRemoved" in self._dataset:
            return self._dataset.PatientIdentityRemoved
        return None

    @PatientIdentityRemoved.setter
    def PatientIdentityRemoved(self, value: Optional[str]):
        if value is None:
            if "PatientIdentityRemoved" in self._dataset:
                del self._dataset.PatientIdentityRemoved
        else:
            self._dataset.PatientIdentityRemoved = value

    @property
    def DeidentificationMethod(self) -> Optional[List[str]]:
        if "DeidentificationMethod" in self._dataset:
            return self._dataset.DeidentificationMethod
        return None

    @DeidentificationMethod.setter
    def DeidentificationMethod(self, value: Optional[List[str]]):
        if value is None:
            if "DeidentificationMethod" in self._dataset:
                del self._dataset.DeidentificationMethod
        else:
            self._dataset.DeidentificationMethod = value

    @property
    def DeidentificationMethodCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "DeidentificationMethodCodeSequence" in self._dataset:
            if len(self._DeidentificationMethodCodeSequence) == len(self._dataset.DeidentificationMethodCodeSequence):
                return self._DeidentificationMethodCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.DeidentificationMethodCodeSequence]
        return None

    @DeidentificationMethodCodeSequence.setter
    def DeidentificationMethodCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._DeidentificationMethodCodeSequence = []
            if "DeidentificationMethodCodeSequence" in self._dataset:
                del self._dataset.DeidentificationMethodCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError(f"DeidentificationMethodCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._DeidentificationMethodCodeSequence = value
            if "DeidentificationMethodCodeSequence" not in self._dataset:
                self._dataset.DeidentificationMethodCodeSequence = pydicom.Sequence()
            self._dataset.DeidentificationMethodCodeSequence.clear()
            self._dataset.DeidentificationMethodCodeSequence.extend([item.to_dataset() for item in value])

    def add_DeidentificationMethodCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError(f"Item must be an instance of CodeSequenceItem")
        self._DeidentificationMethodCodeSequence.append(item)
        if "DeidentificationMethodCodeSequence" not in self._dataset:
            self._dataset.DeidentificationMethodCodeSequence = pydicom.Sequence()
        self._dataset.DeidentificationMethodCodeSequence.append(item.to_dataset())

    @property
    def ClinicalTrialTimePointID(self) -> Optional[str]:
        if "ClinicalTrialTimePointID" in self._dataset:
            return self._dataset.ClinicalTrialTimePointID
        return None

    @ClinicalTrialTimePointID.setter
    def ClinicalTrialTimePointID(self, value: Optional[str]):
        if value is None:
            if "ClinicalTrialTimePointID" in self._dataset:
                del self._dataset.ClinicalTrialTimePointID
        else:
            self._dataset.ClinicalTrialTimePointID = value

    @property
    def ClinicalTrialTimePointDescription(self) -> Optional[str]:
        if "ClinicalTrialTimePointDescription" in self._dataset:
            return self._dataset.ClinicalTrialTimePointDescription
        return None

    @ClinicalTrialTimePointDescription.setter
    def ClinicalTrialTimePointDescription(self, value: Optional[str]):
        if value is None:
            if "ClinicalTrialTimePointDescription" in self._dataset:
                del self._dataset.ClinicalTrialTimePointDescription
        else:
            self._dataset.ClinicalTrialTimePointDescription = value

    @property
    def LongitudinalTemporalOffsetFromEvent(self) -> Optional[float]:
        if "LongitudinalTemporalOffsetFromEvent" in self._dataset:
            return self._dataset.LongitudinalTemporalOffsetFromEvent
        return None

    @LongitudinalTemporalOffsetFromEvent.setter
    def LongitudinalTemporalOffsetFromEvent(self, value: Optional[float]):
        if value is None:
            if "LongitudinalTemporalOffsetFromEvent" in self._dataset:
                del self._dataset.LongitudinalTemporalOffsetFromEvent
        else:
            self._dataset.LongitudinalTemporalOffsetFromEvent = value

    @property
    def LongitudinalTemporalEventType(self) -> Optional[str]:
        if "LongitudinalTemporalEventType" in self._dataset:
            return self._dataset.LongitudinalTemporalEventType
        return None

    @LongitudinalTemporalEventType.setter
    def LongitudinalTemporalEventType(self, value: Optional[str]):
        if value is None:
            if "LongitudinalTemporalEventType" in self._dataset:
                del self._dataset.LongitudinalTemporalEventType
        else:
            self._dataset.LongitudinalTemporalEventType = value

    @property
    def ClinicalTrialTimePointTypeCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "ClinicalTrialTimePointTypeCodeSequence" in self._dataset:
            if len(self._ClinicalTrialTimePointTypeCodeSequence) == len(self._dataset.ClinicalTrialTimePointTypeCodeSequence):
                return self._ClinicalTrialTimePointTypeCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.ClinicalTrialTimePointTypeCodeSequence]
        return None

    @ClinicalTrialTimePointTypeCodeSequence.setter
    def ClinicalTrialTimePointTypeCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._ClinicalTrialTimePointTypeCodeSequence = []
            if "ClinicalTrialTimePointTypeCodeSequence" in self._dataset:
                del self._dataset.ClinicalTrialTimePointTypeCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError(f"ClinicalTrialTimePointTypeCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._ClinicalTrialTimePointTypeCodeSequence = value
            if "ClinicalTrialTimePointTypeCodeSequence" not in self._dataset:
                self._dataset.ClinicalTrialTimePointTypeCodeSequence = pydicom.Sequence()
            self._dataset.ClinicalTrialTimePointTypeCodeSequence.clear()
            self._dataset.ClinicalTrialTimePointTypeCodeSequence.extend([item.to_dataset() for item in value])

    def add_ClinicalTrialTimePointTypeCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError(f"Item must be an instance of CodeSequenceItem")
        self._ClinicalTrialTimePointTypeCodeSequence.append(item)
        if "ClinicalTrialTimePointTypeCodeSequence" not in self._dataset:
            self._dataset.ClinicalTrialTimePointTypeCodeSequence = pydicom.Sequence()
        self._dataset.ClinicalTrialTimePointTypeCodeSequence.append(item.to_dataset())

    @property
    def IssuerOfClinicalTrialTimePointID(self) -> Optional[str]:
        if "IssuerOfClinicalTrialTimePointID" in self._dataset:
            return self._dataset.IssuerOfClinicalTrialTimePointID
        return None

    @IssuerOfClinicalTrialTimePointID.setter
    def IssuerOfClinicalTrialTimePointID(self, value: Optional[str]):
        if value is None:
            if "IssuerOfClinicalTrialTimePointID" in self._dataset:
                del self._dataset.IssuerOfClinicalTrialTimePointID
        else:
            self._dataset.IssuerOfClinicalTrialTimePointID = value

    @property
    def ConsentForClinicalTrialUseSequence(self) -> Optional[List[ConsentForClinicalTrialUseSequenceItem]]:
        if "ConsentForClinicalTrialUseSequence" in self._dataset:
            if len(self._ConsentForClinicalTrialUseSequence) == len(self._dataset.ConsentForClinicalTrialUseSequence):
                return self._ConsentForClinicalTrialUseSequence
            else:
                return [ConsentForClinicalTrialUseSequenceItem(x) for x in self._dataset.ConsentForClinicalTrialUseSequence]
        return None

    @ConsentForClinicalTrialUseSequence.setter
    def ConsentForClinicalTrialUseSequence(self, value: Optional[List[ConsentForClinicalTrialUseSequenceItem]]):
        if value is None:
            self._ConsentForClinicalTrialUseSequence = []
            if "ConsentForClinicalTrialUseSequence" in self._dataset:
                del self._dataset.ConsentForClinicalTrialUseSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, ConsentForClinicalTrialUseSequenceItem) for item in value
        ):
            raise ValueError(
                f"ConsentForClinicalTrialUseSequence must be a list of ConsentForClinicalTrialUseSequenceItem objects"
            )
        else:
            self._ConsentForClinicalTrialUseSequence = value
            if "ConsentForClinicalTrialUseSequence" not in self._dataset:
                self._dataset.ConsentForClinicalTrialUseSequence = pydicom.Sequence()
            self._dataset.ConsentForClinicalTrialUseSequence.clear()
            self._dataset.ConsentForClinicalTrialUseSequence.extend([item.to_dataset() for item in value])

    def add_ConsentForClinicalTrialUse(self, item: ConsentForClinicalTrialUseSequenceItem):
        if not isinstance(item, ConsentForClinicalTrialUseSequenceItem):
            raise ValueError(f"Item must be an instance of ConsentForClinicalTrialUseSequenceItem")
        self._ConsentForClinicalTrialUseSequence.append(item)
        if "ConsentForClinicalTrialUseSequence" not in self._dataset:
            self._dataset.ConsentForClinicalTrialUseSequence = pydicom.Sequence()
        self._dataset.ConsentForClinicalTrialUseSequence.append(item.to_dataset())

    @property
    def StudyDate(self) -> Optional[str]:
        if "StudyDate" in self._dataset:
            return self._dataset.StudyDate
        return None

    @StudyDate.setter
    def StudyDate(self, value: Optional[str]):
        if value is None:
            if "StudyDate" in self._dataset:
                del self._dataset.StudyDate
        else:
            self._dataset.StudyDate = value

    @property
    def StudyTime(self) -> Optional[str]:
        if "StudyTime" in self._dataset:
            return self._dataset.StudyTime
        return None

    @StudyTime.setter
    def StudyTime(self, value: Optional[str]):
        if value is None:
            if "StudyTime" in self._dataset:
                del self._dataset.StudyTime
        else:
            self._dataset.StudyTime = value

    @property
    def AccessionNumber(self) -> Optional[str]:
        if "AccessionNumber" in self._dataset:
            return self._dataset.AccessionNumber
        return None

    @AccessionNumber.setter
    def AccessionNumber(self, value: Optional[str]):
        if value is None:
            if "AccessionNumber" in self._dataset:
                del self._dataset.AccessionNumber
        else:
            self._dataset.AccessionNumber = value

    @property
    def IssuerOfAccessionNumberSequence(self) -> Optional[List[IssuerOfAccessionNumberSequenceItem]]:
        if "IssuerOfAccessionNumberSequence" in self._dataset:
            if len(self._IssuerOfAccessionNumberSequence) == len(self._dataset.IssuerOfAccessionNumberSequence):
                return self._IssuerOfAccessionNumberSequence
            else:
                return [IssuerOfAccessionNumberSequenceItem(x) for x in self._dataset.IssuerOfAccessionNumberSequence]
        return None

    @IssuerOfAccessionNumberSequence.setter
    def IssuerOfAccessionNumberSequence(self, value: Optional[List[IssuerOfAccessionNumberSequenceItem]]):
        if value is None:
            self._IssuerOfAccessionNumberSequence = []
            if "IssuerOfAccessionNumberSequence" in self._dataset:
                del self._dataset.IssuerOfAccessionNumberSequence
        elif not isinstance(value, list) or not all(isinstance(item, IssuerOfAccessionNumberSequenceItem) for item in value):
            raise ValueError(f"IssuerOfAccessionNumberSequence must be a list of IssuerOfAccessionNumberSequenceItem objects")
        else:
            self._IssuerOfAccessionNumberSequence = value
            if "IssuerOfAccessionNumberSequence" not in self._dataset:
                self._dataset.IssuerOfAccessionNumberSequence = pydicom.Sequence()
            self._dataset.IssuerOfAccessionNumberSequence.clear()
            self._dataset.IssuerOfAccessionNumberSequence.extend([item.to_dataset() for item in value])

    def add_IssuerOfAccessionNumber(self, item: IssuerOfAccessionNumberSequenceItem):
        if not isinstance(item, IssuerOfAccessionNumberSequenceItem):
            raise ValueError(f"Item must be an instance of IssuerOfAccessionNumberSequenceItem")
        self._IssuerOfAccessionNumberSequence.append(item)
        if "IssuerOfAccessionNumberSequence" not in self._dataset:
            self._dataset.IssuerOfAccessionNumberSequence = pydicom.Sequence()
        self._dataset.IssuerOfAccessionNumberSequence.append(item.to_dataset())

    @property
    def ReferringPhysicianName(self) -> Optional[str]:
        if "ReferringPhysicianName" in self._dataset:
            return self._dataset.ReferringPhysicianName
        return None

    @ReferringPhysicianName.setter
    def ReferringPhysicianName(self, value: Optional[str]):
        if value is None:
            if "ReferringPhysicianName" in self._dataset:
                del self._dataset.ReferringPhysicianName
        else:
            self._dataset.ReferringPhysicianName = value

    @property
    def ReferringPhysicianIdentificationSequence(self) -> Optional[List[ReferringPhysicianIdentificationSequenceItem]]:
        if "ReferringPhysicianIdentificationSequence" in self._dataset:
            if len(self._ReferringPhysicianIdentificationSequence) == len(
                self._dataset.ReferringPhysicianIdentificationSequence
            ):
                return self._ReferringPhysicianIdentificationSequence
            else:
                return [
                    ReferringPhysicianIdentificationSequenceItem(x)
                    for x in self._dataset.ReferringPhysicianIdentificationSequence
                ]
        return None

    @ReferringPhysicianIdentificationSequence.setter
    def ReferringPhysicianIdentificationSequence(self, value: Optional[List[ReferringPhysicianIdentificationSequenceItem]]):
        if value is None:
            self._ReferringPhysicianIdentificationSequence = []
            if "ReferringPhysicianIdentificationSequence" in self._dataset:
                del self._dataset.ReferringPhysicianIdentificationSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, ReferringPhysicianIdentificationSequenceItem) for item in value
        ):
            raise ValueError(
                f"ReferringPhysicianIdentificationSequence must be a list of ReferringPhysicianIdentificationSequenceItem objects"
            )
        else:
            self._ReferringPhysicianIdentificationSequence = value
            if "ReferringPhysicianIdentificationSequence" not in self._dataset:
                self._dataset.ReferringPhysicianIdentificationSequence = pydicom.Sequence()
            self._dataset.ReferringPhysicianIdentificationSequence.clear()
            self._dataset.ReferringPhysicianIdentificationSequence.extend([item.to_dataset() for item in value])

    def add_ReferringPhysicianIdentification(self, item: ReferringPhysicianIdentificationSequenceItem):
        if not isinstance(item, ReferringPhysicianIdentificationSequenceItem):
            raise ValueError(f"Item must be an instance of ReferringPhysicianIdentificationSequenceItem")
        self._ReferringPhysicianIdentificationSequence.append(item)
        if "ReferringPhysicianIdentificationSequence" not in self._dataset:
            self._dataset.ReferringPhysicianIdentificationSequence = pydicom.Sequence()
        self._dataset.ReferringPhysicianIdentificationSequence.append(item.to_dataset())

    @property
    def ConsultingPhysicianName(self) -> Optional[List[str]]:
        if "ConsultingPhysicianName" in self._dataset:
            return self._dataset.ConsultingPhysicianName
        return None

    @ConsultingPhysicianName.setter
    def ConsultingPhysicianName(self, value: Optional[List[str]]):
        if value is None:
            if "ConsultingPhysicianName" in self._dataset:
                del self._dataset.ConsultingPhysicianName
        else:
            self._dataset.ConsultingPhysicianName = value

    @property
    def ConsultingPhysicianIdentificationSequence(self) -> Optional[List[ConsultingPhysicianIdentificationSequenceItem]]:
        if "ConsultingPhysicianIdentificationSequence" in self._dataset:
            if len(self._ConsultingPhysicianIdentificationSequence) == len(
                self._dataset.ConsultingPhysicianIdentificationSequence
            ):
                return self._ConsultingPhysicianIdentificationSequence
            else:
                return [
                    ConsultingPhysicianIdentificationSequenceItem(x)
                    for x in self._dataset.ConsultingPhysicianIdentificationSequence
                ]
        return None

    @ConsultingPhysicianIdentificationSequence.setter
    def ConsultingPhysicianIdentificationSequence(self, value: Optional[List[ConsultingPhysicianIdentificationSequenceItem]]):
        if value is None:
            self._ConsultingPhysicianIdentificationSequence = []
            if "ConsultingPhysicianIdentificationSequence" in self._dataset:
                del self._dataset.ConsultingPhysicianIdentificationSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, ConsultingPhysicianIdentificationSequenceItem) for item in value
        ):
            raise ValueError(
                f"ConsultingPhysicianIdentificationSequence must be a list of ConsultingPhysicianIdentificationSequenceItem objects"
            )
        else:
            self._ConsultingPhysicianIdentificationSequence = value
            if "ConsultingPhysicianIdentificationSequence" not in self._dataset:
                self._dataset.ConsultingPhysicianIdentificationSequence = pydicom.Sequence()
            self._dataset.ConsultingPhysicianIdentificationSequence.clear()
            self._dataset.ConsultingPhysicianIdentificationSequence.extend([item.to_dataset() for item in value])

    def add_ConsultingPhysicianIdentification(self, item: ConsultingPhysicianIdentificationSequenceItem):
        if not isinstance(item, ConsultingPhysicianIdentificationSequenceItem):
            raise ValueError(f"Item must be an instance of ConsultingPhysicianIdentificationSequenceItem")
        self._ConsultingPhysicianIdentificationSequence.append(item)
        if "ConsultingPhysicianIdentificationSequence" not in self._dataset:
            self._dataset.ConsultingPhysicianIdentificationSequence = pydicom.Sequence()
        self._dataset.ConsultingPhysicianIdentificationSequence.append(item.to_dataset())

    @property
    def StudyDescription(self) -> Optional[str]:
        if "StudyDescription" in self._dataset:
            return self._dataset.StudyDescription
        return None

    @StudyDescription.setter
    def StudyDescription(self, value: Optional[str]):
        if value is None:
            if "StudyDescription" in self._dataset:
                del self._dataset.StudyDescription
        else:
            self._dataset.StudyDescription = value

    @property
    def ProcedureCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "ProcedureCodeSequence" in self._dataset:
            if len(self._ProcedureCodeSequence) == len(self._dataset.ProcedureCodeSequence):
                return self._ProcedureCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.ProcedureCodeSequence]
        return None

    @ProcedureCodeSequence.setter
    def ProcedureCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._ProcedureCodeSequence = []
            if "ProcedureCodeSequence" in self._dataset:
                del self._dataset.ProcedureCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError(f"ProcedureCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._ProcedureCodeSequence = value
            if "ProcedureCodeSequence" not in self._dataset:
                self._dataset.ProcedureCodeSequence = pydicom.Sequence()
            self._dataset.ProcedureCodeSequence.clear()
            self._dataset.ProcedureCodeSequence.extend([item.to_dataset() for item in value])

    def add_ProcedureCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError(f"Item must be an instance of CodeSequenceItem")
        self._ProcedureCodeSequence.append(item)
        if "ProcedureCodeSequence" not in self._dataset:
            self._dataset.ProcedureCodeSequence = pydicom.Sequence()
        self._dataset.ProcedureCodeSequence.append(item.to_dataset())

    @property
    def PhysiciansOfRecord(self) -> Optional[List[str]]:
        if "PhysiciansOfRecord" in self._dataset:
            return self._dataset.PhysiciansOfRecord
        return None

    @PhysiciansOfRecord.setter
    def PhysiciansOfRecord(self, value: Optional[List[str]]):
        if value is None:
            if "PhysiciansOfRecord" in self._dataset:
                del self._dataset.PhysiciansOfRecord
        else:
            self._dataset.PhysiciansOfRecord = value

    @property
    def PhysiciansOfRecordIdentificationSequence(self) -> Optional[List[PhysiciansOfRecordIdentificationSequenceItem]]:
        if "PhysiciansOfRecordIdentificationSequence" in self._dataset:
            if len(self._PhysiciansOfRecordIdentificationSequence) == len(
                self._dataset.PhysiciansOfRecordIdentificationSequence
            ):
                return self._PhysiciansOfRecordIdentificationSequence
            else:
                return [
                    PhysiciansOfRecordIdentificationSequenceItem(x)
                    for x in self._dataset.PhysiciansOfRecordIdentificationSequence
                ]
        return None

    @PhysiciansOfRecordIdentificationSequence.setter
    def PhysiciansOfRecordIdentificationSequence(self, value: Optional[List[PhysiciansOfRecordIdentificationSequenceItem]]):
        if value is None:
            self._PhysiciansOfRecordIdentificationSequence = []
            if "PhysiciansOfRecordIdentificationSequence" in self._dataset:
                del self._dataset.PhysiciansOfRecordIdentificationSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, PhysiciansOfRecordIdentificationSequenceItem) for item in value
        ):
            raise ValueError(
                f"PhysiciansOfRecordIdentificationSequence must be a list of PhysiciansOfRecordIdentificationSequenceItem objects"
            )
        else:
            self._PhysiciansOfRecordIdentificationSequence = value
            if "PhysiciansOfRecordIdentificationSequence" not in self._dataset:
                self._dataset.PhysiciansOfRecordIdentificationSequence = pydicom.Sequence()
            self._dataset.PhysiciansOfRecordIdentificationSequence.clear()
            self._dataset.PhysiciansOfRecordIdentificationSequence.extend([item.to_dataset() for item in value])

    def add_PhysiciansOfRecordIdentification(self, item: PhysiciansOfRecordIdentificationSequenceItem):
        if not isinstance(item, PhysiciansOfRecordIdentificationSequenceItem):
            raise ValueError(f"Item must be an instance of PhysiciansOfRecordIdentificationSequenceItem")
        self._PhysiciansOfRecordIdentificationSequence.append(item)
        if "PhysiciansOfRecordIdentificationSequence" not in self._dataset:
            self._dataset.PhysiciansOfRecordIdentificationSequence = pydicom.Sequence()
        self._dataset.PhysiciansOfRecordIdentificationSequence.append(item.to_dataset())

    @property
    def NameOfPhysiciansReadingStudy(self) -> Optional[List[str]]:
        if "NameOfPhysiciansReadingStudy" in self._dataset:
            return self._dataset.NameOfPhysiciansReadingStudy
        return None

    @NameOfPhysiciansReadingStudy.setter
    def NameOfPhysiciansReadingStudy(self, value: Optional[List[str]]):
        if value is None:
            if "NameOfPhysiciansReadingStudy" in self._dataset:
                del self._dataset.NameOfPhysiciansReadingStudy
        else:
            self._dataset.NameOfPhysiciansReadingStudy = value

    @property
    def PhysiciansReadingStudyIdentificationSequence(self) -> Optional[List[PhysiciansReadingStudyIdentificationSequenceItem]]:
        if "PhysiciansReadingStudyIdentificationSequence" in self._dataset:
            if len(self._PhysiciansReadingStudyIdentificationSequence) == len(
                self._dataset.PhysiciansReadingStudyIdentificationSequence
            ):
                return self._PhysiciansReadingStudyIdentificationSequence
            else:
                return [
                    PhysiciansReadingStudyIdentificationSequenceItem(x)
                    for x in self._dataset.PhysiciansReadingStudyIdentificationSequence
                ]
        return None

    @PhysiciansReadingStudyIdentificationSequence.setter
    def PhysiciansReadingStudyIdentificationSequence(
        self, value: Optional[List[PhysiciansReadingStudyIdentificationSequenceItem]]
    ):
        if value is None:
            self._PhysiciansReadingStudyIdentificationSequence = []
            if "PhysiciansReadingStudyIdentificationSequence" in self._dataset:
                del self._dataset.PhysiciansReadingStudyIdentificationSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, PhysiciansReadingStudyIdentificationSequenceItem) for item in value
        ):
            raise ValueError(
                f"PhysiciansReadingStudyIdentificationSequence must be a list of PhysiciansReadingStudyIdentificationSequenceItem objects"
            )
        else:
            self._PhysiciansReadingStudyIdentificationSequence = value
            if "PhysiciansReadingStudyIdentificationSequence" not in self._dataset:
                self._dataset.PhysiciansReadingStudyIdentificationSequence = pydicom.Sequence()
            self._dataset.PhysiciansReadingStudyIdentificationSequence.clear()
            self._dataset.PhysiciansReadingStudyIdentificationSequence.extend([item.to_dataset() for item in value])

    def add_PhysiciansReadingStudyIdentification(self, item: PhysiciansReadingStudyIdentificationSequenceItem):
        if not isinstance(item, PhysiciansReadingStudyIdentificationSequenceItem):
            raise ValueError(f"Item must be an instance of PhysiciansReadingStudyIdentificationSequenceItem")
        self._PhysiciansReadingStudyIdentificationSequence.append(item)
        if "PhysiciansReadingStudyIdentificationSequence" not in self._dataset:
            self._dataset.PhysiciansReadingStudyIdentificationSequence = pydicom.Sequence()
        self._dataset.PhysiciansReadingStudyIdentificationSequence.append(item.to_dataset())

    @property
    def ReferencedStudySequence(self) -> Optional[List[ReferencedStudySequenceItem]]:
        if "ReferencedStudySequence" in self._dataset:
            if len(self._ReferencedStudySequence) == len(self._dataset.ReferencedStudySequence):
                return self._ReferencedStudySequence
            else:
                return [ReferencedStudySequenceItem(x) for x in self._dataset.ReferencedStudySequence]
        return None

    @ReferencedStudySequence.setter
    def ReferencedStudySequence(self, value: Optional[List[ReferencedStudySequenceItem]]):
        if value is None:
            self._ReferencedStudySequence = []
            if "ReferencedStudySequence" in self._dataset:
                del self._dataset.ReferencedStudySequence
        elif not isinstance(value, list) or not all(isinstance(item, ReferencedStudySequenceItem) for item in value):
            raise ValueError(f"ReferencedStudySequence must be a list of ReferencedStudySequenceItem objects")
        else:
            self._ReferencedStudySequence = value
            if "ReferencedStudySequence" not in self._dataset:
                self._dataset.ReferencedStudySequence = pydicom.Sequence()
            self._dataset.ReferencedStudySequence.clear()
            self._dataset.ReferencedStudySequence.extend([item.to_dataset() for item in value])

    def add_ReferencedStudy(self, item: ReferencedStudySequenceItem):
        if not isinstance(item, ReferencedStudySequenceItem):
            raise ValueError(f"Item must be an instance of ReferencedStudySequenceItem")
        self._ReferencedStudySequence.append(item)
        if "ReferencedStudySequence" not in self._dataset:
            self._dataset.ReferencedStudySequence = pydicom.Sequence()
        self._dataset.ReferencedStudySequence.append(item.to_dataset())

    @property
    def StudyInstanceUID(self) -> Optional[str]:
        if "StudyInstanceUID" in self._dataset:
            return self._dataset.StudyInstanceUID
        return None

    @StudyInstanceUID.setter
    def StudyInstanceUID(self, value: Optional[str]):
        if value is None:
            if "StudyInstanceUID" in self._dataset:
                del self._dataset.StudyInstanceUID
        else:
            self._dataset.StudyInstanceUID = value

    @property
    def StudyID(self) -> Optional[str]:
        if "StudyID" in self._dataset:
            return self._dataset.StudyID
        return None

    @StudyID.setter
    def StudyID(self, value: Optional[str]):
        if value is None:
            if "StudyID" in self._dataset:
                del self._dataset.StudyID
        else:
            self._dataset.StudyID = value

    @property
    def RequestingService(self) -> Optional[str]:
        if "RequestingService" in self._dataset:
            return self._dataset.RequestingService
        return None

    @RequestingService.setter
    def RequestingService(self, value: Optional[str]):
        if value is None:
            if "RequestingService" in self._dataset:
                del self._dataset.RequestingService
        else:
            self._dataset.RequestingService = value

    @property
    def RequestingServiceCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "RequestingServiceCodeSequence" in self._dataset:
            if len(self._RequestingServiceCodeSequence) == len(self._dataset.RequestingServiceCodeSequence):
                return self._RequestingServiceCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.RequestingServiceCodeSequence]
        return None

    @RequestingServiceCodeSequence.setter
    def RequestingServiceCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._RequestingServiceCodeSequence = []
            if "RequestingServiceCodeSequence" in self._dataset:
                del self._dataset.RequestingServiceCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError(f"RequestingServiceCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._RequestingServiceCodeSequence = value
            if "RequestingServiceCodeSequence" not in self._dataset:
                self._dataset.RequestingServiceCodeSequence = pydicom.Sequence()
            self._dataset.RequestingServiceCodeSequence.clear()
            self._dataset.RequestingServiceCodeSequence.extend([item.to_dataset() for item in value])

    def add_RequestingServiceCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError(f"Item must be an instance of CodeSequenceItem")
        self._RequestingServiceCodeSequence.append(item)
        if "RequestingServiceCodeSequence" not in self._dataset:
            self._dataset.RequestingServiceCodeSequence = pydicom.Sequence()
        self._dataset.RequestingServiceCodeSequence.append(item.to_dataset())

    @property
    def ReasonForPerformedProcedureCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "ReasonForPerformedProcedureCodeSequence" in self._dataset:
            if len(self._ReasonForPerformedProcedureCodeSequence) == len(
                self._dataset.ReasonForPerformedProcedureCodeSequence
            ):
                return self._ReasonForPerformedProcedureCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.ReasonForPerformedProcedureCodeSequence]
        return None

    @ReasonForPerformedProcedureCodeSequence.setter
    def ReasonForPerformedProcedureCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._ReasonForPerformedProcedureCodeSequence = []
            if "ReasonForPerformedProcedureCodeSequence" in self._dataset:
                del self._dataset.ReasonForPerformedProcedureCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError(f"ReasonForPerformedProcedureCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._ReasonForPerformedProcedureCodeSequence = value
            if "ReasonForPerformedProcedureCodeSequence" not in self._dataset:
                self._dataset.ReasonForPerformedProcedureCodeSequence = pydicom.Sequence()
            self._dataset.ReasonForPerformedProcedureCodeSequence.clear()
            self._dataset.ReasonForPerformedProcedureCodeSequence.extend([item.to_dataset() for item in value])

    def add_ReasonForPerformedProcedureCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError(f"Item must be an instance of CodeSequenceItem")
        self._ReasonForPerformedProcedureCodeSequence.append(item)
        if "ReasonForPerformedProcedureCodeSequence" not in self._dataset:
            self._dataset.ReasonForPerformedProcedureCodeSequence = pydicom.Sequence()
        self._dataset.ReasonForPerformedProcedureCodeSequence.append(item.to_dataset())

    @property
    def ClinicalTrialSponsorName(self) -> Optional[str]:
        if "ClinicalTrialSponsorName" in self._dataset:
            return self._dataset.ClinicalTrialSponsorName
        return None

    @ClinicalTrialSponsorName.setter
    def ClinicalTrialSponsorName(self, value: Optional[str]):
        if value is None:
            if "ClinicalTrialSponsorName" in self._dataset:
                del self._dataset.ClinicalTrialSponsorName
        else:
            self._dataset.ClinicalTrialSponsorName = value

    @property
    def ClinicalTrialProtocolID(self) -> Optional[str]:
        if "ClinicalTrialProtocolID" in self._dataset:
            return self._dataset.ClinicalTrialProtocolID
        return None

    @ClinicalTrialProtocolID.setter
    def ClinicalTrialProtocolID(self, value: Optional[str]):
        if value is None:
            if "ClinicalTrialProtocolID" in self._dataset:
                del self._dataset.ClinicalTrialProtocolID
        else:
            self._dataset.ClinicalTrialProtocolID = value

    @property
    def ClinicalTrialProtocolName(self) -> Optional[str]:
        if "ClinicalTrialProtocolName" in self._dataset:
            return self._dataset.ClinicalTrialProtocolName
        return None

    @ClinicalTrialProtocolName.setter
    def ClinicalTrialProtocolName(self, value: Optional[str]):
        if value is None:
            if "ClinicalTrialProtocolName" in self._dataset:
                del self._dataset.ClinicalTrialProtocolName
        else:
            self._dataset.ClinicalTrialProtocolName = value

    @property
    def IssuerOfClinicalTrialProtocolID(self) -> Optional[str]:
        if "IssuerOfClinicalTrialProtocolID" in self._dataset:
            return self._dataset.IssuerOfClinicalTrialProtocolID
        return None

    @IssuerOfClinicalTrialProtocolID.setter
    def IssuerOfClinicalTrialProtocolID(self, value: Optional[str]):
        if value is None:
            if "IssuerOfClinicalTrialProtocolID" in self._dataset:
                del self._dataset.IssuerOfClinicalTrialProtocolID
        else:
            self._dataset.IssuerOfClinicalTrialProtocolID = value

    @property
    def OtherClinicalTrialProtocolIDsSequence(self) -> Optional[List[OtherClinicalTrialProtocolIDsSequenceItem]]:
        if "OtherClinicalTrialProtocolIDsSequence" in self._dataset:
            if len(self._OtherClinicalTrialProtocolIDsSequence) == len(self._dataset.OtherClinicalTrialProtocolIDsSequence):
                return self._OtherClinicalTrialProtocolIDsSequence
            else:
                return [
                    OtherClinicalTrialProtocolIDsSequenceItem(x) for x in self._dataset.OtherClinicalTrialProtocolIDsSequence
                ]
        return None

    @OtherClinicalTrialProtocolIDsSequence.setter
    def OtherClinicalTrialProtocolIDsSequence(self, value: Optional[List[OtherClinicalTrialProtocolIDsSequenceItem]]):
        if value is None:
            self._OtherClinicalTrialProtocolIDsSequence = []
            if "OtherClinicalTrialProtocolIDsSequence" in self._dataset:
                del self._dataset.OtherClinicalTrialProtocolIDsSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, OtherClinicalTrialProtocolIDsSequenceItem) for item in value
        ):
            raise ValueError(
                f"OtherClinicalTrialProtocolIDsSequence must be a list of OtherClinicalTrialProtocolIDsSequenceItem objects"
            )
        else:
            self._OtherClinicalTrialProtocolIDsSequence = value
            if "OtherClinicalTrialProtocolIDsSequence" not in self._dataset:
                self._dataset.OtherClinicalTrialProtocolIDsSequence = pydicom.Sequence()
            self._dataset.OtherClinicalTrialProtocolIDsSequence.clear()
            self._dataset.OtherClinicalTrialProtocolIDsSequence.extend([item.to_dataset() for item in value])

    def add_OtherClinicalTrialProtocolIDs(self, item: OtherClinicalTrialProtocolIDsSequenceItem):
        if not isinstance(item, OtherClinicalTrialProtocolIDsSequenceItem):
            raise ValueError(f"Item must be an instance of OtherClinicalTrialProtocolIDsSequenceItem")
        self._OtherClinicalTrialProtocolIDsSequence.append(item)
        if "OtherClinicalTrialProtocolIDsSequence" not in self._dataset:
            self._dataset.OtherClinicalTrialProtocolIDsSequence = pydicom.Sequence()
        self._dataset.OtherClinicalTrialProtocolIDsSequence.append(item.to_dataset())

    @property
    def ClinicalTrialSiteID(self) -> Optional[str]:
        if "ClinicalTrialSiteID" in self._dataset:
            return self._dataset.ClinicalTrialSiteID
        return None

    @ClinicalTrialSiteID.setter
    def ClinicalTrialSiteID(self, value: Optional[str]):
        if value is None:
            if "ClinicalTrialSiteID" in self._dataset:
                del self._dataset.ClinicalTrialSiteID
        else:
            self._dataset.ClinicalTrialSiteID = value

    @property
    def ClinicalTrialSiteName(self) -> Optional[str]:
        if "ClinicalTrialSiteName" in self._dataset:
            return self._dataset.ClinicalTrialSiteName
        return None

    @ClinicalTrialSiteName.setter
    def ClinicalTrialSiteName(self, value: Optional[str]):
        if value is None:
            if "ClinicalTrialSiteName" in self._dataset:
                del self._dataset.ClinicalTrialSiteName
        else:
            self._dataset.ClinicalTrialSiteName = value

    @property
    def IssuerOfClinicalTrialSiteID(self) -> Optional[str]:
        if "IssuerOfClinicalTrialSiteID" in self._dataset:
            return self._dataset.IssuerOfClinicalTrialSiteID
        return None

    @IssuerOfClinicalTrialSiteID.setter
    def IssuerOfClinicalTrialSiteID(self, value: Optional[str]):
        if value is None:
            if "IssuerOfClinicalTrialSiteID" in self._dataset:
                del self._dataset.IssuerOfClinicalTrialSiteID
        else:
            self._dataset.IssuerOfClinicalTrialSiteID = value

    @property
    def ClinicalTrialSubjectID(self) -> Optional[str]:
        if "ClinicalTrialSubjectID" in self._dataset:
            return self._dataset.ClinicalTrialSubjectID
        return None

    @ClinicalTrialSubjectID.setter
    def ClinicalTrialSubjectID(self, value: Optional[str]):
        if value is None:
            if "ClinicalTrialSubjectID" in self._dataset:
                del self._dataset.ClinicalTrialSubjectID
        else:
            self._dataset.ClinicalTrialSubjectID = value

    @property
    def IssuerOfClinicalTrialSubjectID(self) -> Optional[str]:
        if "IssuerOfClinicalTrialSubjectID" in self._dataset:
            return self._dataset.IssuerOfClinicalTrialSubjectID
        return None

    @IssuerOfClinicalTrialSubjectID.setter
    def IssuerOfClinicalTrialSubjectID(self, value: Optional[str]):
        if value is None:
            if "IssuerOfClinicalTrialSubjectID" in self._dataset:
                del self._dataset.IssuerOfClinicalTrialSubjectID
        else:
            self._dataset.IssuerOfClinicalTrialSubjectID = value

    @property
    def ClinicalTrialSubjectReadingID(self) -> Optional[str]:
        if "ClinicalTrialSubjectReadingID" in self._dataset:
            return self._dataset.ClinicalTrialSubjectReadingID
        return None

    @ClinicalTrialSubjectReadingID.setter
    def ClinicalTrialSubjectReadingID(self, value: Optional[str]):
        if value is None:
            if "ClinicalTrialSubjectReadingID" in self._dataset:
                del self._dataset.ClinicalTrialSubjectReadingID
        else:
            self._dataset.ClinicalTrialSubjectReadingID = value

    @property
    def IssuerOfClinicalTrialSubjectReadingID(self) -> Optional[str]:
        if "IssuerOfClinicalTrialSubjectReadingID" in self._dataset:
            return self._dataset.IssuerOfClinicalTrialSubjectReadingID
        return None

    @IssuerOfClinicalTrialSubjectReadingID.setter
    def IssuerOfClinicalTrialSubjectReadingID(self, value: Optional[str]):
        if value is None:
            if "IssuerOfClinicalTrialSubjectReadingID" in self._dataset:
                del self._dataset.IssuerOfClinicalTrialSubjectReadingID
        else:
            self._dataset.IssuerOfClinicalTrialSubjectReadingID = value

    @property
    def ClinicalTrialProtocolEthicsCommitteeName(self) -> Optional[str]:
        if "ClinicalTrialProtocolEthicsCommitteeName" in self._dataset:
            return self._dataset.ClinicalTrialProtocolEthicsCommitteeName
        return None

    @ClinicalTrialProtocolEthicsCommitteeName.setter
    def ClinicalTrialProtocolEthicsCommitteeName(self, value: Optional[str]):
        if value is None:
            if "ClinicalTrialProtocolEthicsCommitteeName" in self._dataset:
                del self._dataset.ClinicalTrialProtocolEthicsCommitteeName
        else:
            self._dataset.ClinicalTrialProtocolEthicsCommitteeName = value

    @property
    def ClinicalTrialProtocolEthicsCommitteeApprovalNumber(self) -> Optional[str]:
        if "ClinicalTrialProtocolEthicsCommitteeApprovalNumber" in self._dataset:
            return self._dataset.ClinicalTrialProtocolEthicsCommitteeApprovalNumber
        return None

    @ClinicalTrialProtocolEthicsCommitteeApprovalNumber.setter
    def ClinicalTrialProtocolEthicsCommitteeApprovalNumber(self, value: Optional[str]):
        if value is None:
            if "ClinicalTrialProtocolEthicsCommitteeApprovalNumber" in self._dataset:
                del self._dataset.ClinicalTrialProtocolEthicsCommitteeApprovalNumber
        else:
            self._dataset.ClinicalTrialProtocolEthicsCommitteeApprovalNumber = value
