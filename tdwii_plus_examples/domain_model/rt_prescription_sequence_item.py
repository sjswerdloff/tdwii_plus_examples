from typing import Any, List, Optional  # noqa

import pydicom

from .code_sequence_item import CodeSequenceItem
from .fraction_based_relationship_sequence_item import (
    FractionBasedRelationshipSequenceItem,
)
from .fraction_pattern_sequence_item import FractionPatternSequenceItem
from .patient_treatment_orientation_sequence_item import (
    PatientTreatmentOrientationSequenceItem,
)
from .planning_input_information_sequence_item import (
    PlanningInputInformationSequenceItem,
)
from .prescription_notes_sequence_item import PrescriptionNotesSequenceItem
from .prior_treatment_reference_sequence_item import PriorTreatmentReferenceSequenceItem
from .referenced_dosimetric_objectives_sequence_item import (
    ReferencedDosimetricObjectivesSequenceItem,
)
from .referenced_rt_treatment_phase_sequence_item import (
    ReferencedRTTreatmentPhaseSequenceItem,
)
from .rt_anatomic_prescription_sequence_item import RTAnatomicPrescriptionSequenceItem


class RTPrescriptionSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._PatientTreatmentOrientationSequence: List[PatientTreatmentOrientationSequenceItem] = []
        self._ReferencedRTTreatmentPhaseSequence: List[ReferencedRTTreatmentPhaseSequenceItem] = []
        self._RTAnatomicPrescriptionSequence: List[RTAnatomicPrescriptionSequenceItem] = []
        self._PriorTreatmentReferenceSequence: List[PriorTreatmentReferenceSequenceItem] = []
        self._ReferencedDosimetricObjectivesSequence: List[ReferencedDosimetricObjectivesSequenceItem] = []
        self._PlanningInputInformationSequence: List[PlanningInputInformationSequenceItem] = []
        self._FractionPatternSequence: List[FractionPatternSequenceItem] = []
        self._RTTreatmentTechniqueCodeSequence: List[CodeSequenceItem] = []
        self._PrescriptionNotesSequence: List[PrescriptionNotesSequenceItem] = []
        self._FractionBasedRelationshipSequence: List[FractionBasedRelationshipSequenceItem] = []
        self._DeliveryTimeStructureCodeSequence: List[CodeSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def PatientTreatmentOrientationSequence(self) -> Optional[List[PatientTreatmentOrientationSequenceItem]]:
        if "PatientTreatmentOrientationSequence" in self._dataset:
            if len(self._PatientTreatmentOrientationSequence) == len(self._dataset.PatientTreatmentOrientationSequence):
                return self._PatientTreatmentOrientationSequence
            else:
                return [PatientTreatmentOrientationSequenceItem(x) for x in self._dataset.PatientTreatmentOrientationSequence]
        return None

    @PatientTreatmentOrientationSequence.setter
    def PatientTreatmentOrientationSequence(self, value: Optional[List[PatientTreatmentOrientationSequenceItem]]):
        if value is None:
            self._PatientTreatmentOrientationSequence = []
            if "PatientTreatmentOrientationSequence" in self._dataset:
                del self._dataset.PatientTreatmentOrientationSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, PatientTreatmentOrientationSequenceItem) for item in value
        ):
            raise ValueError(
                "PatientTreatmentOrientationSequence must be a list of PatientTreatmentOrientationSequenceItem objects"
            )
        else:
            self._PatientTreatmentOrientationSequence = value
            if "PatientTreatmentOrientationSequence" not in self._dataset:
                self._dataset.PatientTreatmentOrientationSequence = pydicom.Sequence()
            self._dataset.PatientTreatmentOrientationSequence.clear()
            self._dataset.PatientTreatmentOrientationSequence.extend([item.to_dataset() for item in value])

    def add_PatientTreatmentOrientation(self, item: PatientTreatmentOrientationSequenceItem):
        if not isinstance(item, PatientTreatmentOrientationSequenceItem):
            raise ValueError("Item must be an instance of PatientTreatmentOrientationSequenceItem")
        self._PatientTreatmentOrientationSequence.append(item)
        if "PatientTreatmentOrientationSequence" not in self._dataset:
            self._dataset.PatientTreatmentOrientationSequence = pydicom.Sequence()
        self._dataset.PatientTreatmentOrientationSequence.append(item.to_dataset())

    @property
    def RTPrescriptionIndex(self) -> Optional[int]:
        if "RTPrescriptionIndex" in self._dataset:
            return self._dataset.RTPrescriptionIndex
        return None

    @RTPrescriptionIndex.setter
    def RTPrescriptionIndex(self, value: Optional[int]):
        if value is None:
            if "RTPrescriptionIndex" in self._dataset:
                del self._dataset.RTPrescriptionIndex
        else:
            self._dataset.RTPrescriptionIndex = value

    @property
    def ReferencedParentRTPrescriptionIndex(self) -> Optional[int]:
        if "ReferencedParentRTPrescriptionIndex" in self._dataset:
            return self._dataset.ReferencedParentRTPrescriptionIndex
        return None

    @ReferencedParentRTPrescriptionIndex.setter
    def ReferencedParentRTPrescriptionIndex(self, value: Optional[int]):
        if value is None:
            if "ReferencedParentRTPrescriptionIndex" in self._dataset:
                del self._dataset.ReferencedParentRTPrescriptionIndex
        else:
            self._dataset.ReferencedParentRTPrescriptionIndex = value

    @property
    def RadiotherapyTreatmentType(self) -> Optional[str]:
        if "RadiotherapyTreatmentType" in self._dataset:
            return self._dataset.RadiotherapyTreatmentType
        return None

    @RadiotherapyTreatmentType.setter
    def RadiotherapyTreatmentType(self, value: Optional[str]):
        if value is None:
            if "RadiotherapyTreatmentType" in self._dataset:
                del self._dataset.RadiotherapyTreatmentType
        else:
            self._dataset.RadiotherapyTreatmentType = value

    @property
    def TeletherapyRadiationType(self) -> Optional[List[str]]:
        if "TeletherapyRadiationType" in self._dataset:
            return self._dataset.TeletherapyRadiationType
        return None

    @TeletherapyRadiationType.setter
    def TeletherapyRadiationType(self, value: Optional[List[str]]):
        if value is None:
            if "TeletherapyRadiationType" in self._dataset:
                del self._dataset.TeletherapyRadiationType
        else:
            self._dataset.TeletherapyRadiationType = value

    @property
    def BrachytherapySourceType(self) -> Optional[List[str]]:
        if "BrachytherapySourceType" in self._dataset:
            return self._dataset.BrachytherapySourceType
        return None

    @BrachytherapySourceType.setter
    def BrachytherapySourceType(self, value: Optional[List[str]]):
        if value is None:
            if "BrachytherapySourceType" in self._dataset:
                del self._dataset.BrachytherapySourceType
        else:
            self._dataset.BrachytherapySourceType = value

    @property
    def ReferencedRTTreatmentPhaseSequence(self) -> Optional[List[ReferencedRTTreatmentPhaseSequenceItem]]:
        if "ReferencedRTTreatmentPhaseSequence" in self._dataset:
            if len(self._ReferencedRTTreatmentPhaseSequence) == len(self._dataset.ReferencedRTTreatmentPhaseSequence):
                return self._ReferencedRTTreatmentPhaseSequence
            else:
                return [ReferencedRTTreatmentPhaseSequenceItem(x) for x in self._dataset.ReferencedRTTreatmentPhaseSequence]
        return None

    @ReferencedRTTreatmentPhaseSequence.setter
    def ReferencedRTTreatmentPhaseSequence(self, value: Optional[List[ReferencedRTTreatmentPhaseSequenceItem]]):
        if value is None:
            self._ReferencedRTTreatmentPhaseSequence = []
            if "ReferencedRTTreatmentPhaseSequence" in self._dataset:
                del self._dataset.ReferencedRTTreatmentPhaseSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, ReferencedRTTreatmentPhaseSequenceItem) for item in value
        ):
            raise ValueError(
                "ReferencedRTTreatmentPhaseSequence must be a list of ReferencedRTTreatmentPhaseSequenceItem objects"
            )
        else:
            self._ReferencedRTTreatmentPhaseSequence = value
            if "ReferencedRTTreatmentPhaseSequence" not in self._dataset:
                self._dataset.ReferencedRTTreatmentPhaseSequence = pydicom.Sequence()
            self._dataset.ReferencedRTTreatmentPhaseSequence.clear()
            self._dataset.ReferencedRTTreatmentPhaseSequence.extend([item.to_dataset() for item in value])

    def add_ReferencedRTTreatmentPhase(self, item: ReferencedRTTreatmentPhaseSequenceItem):
        if not isinstance(item, ReferencedRTTreatmentPhaseSequenceItem):
            raise ValueError("Item must be an instance of ReferencedRTTreatmentPhaseSequenceItem")
        self._ReferencedRTTreatmentPhaseSequence.append(item)
        if "ReferencedRTTreatmentPhaseSequence" not in self._dataset:
            self._dataset.ReferencedRTTreatmentPhaseSequence = pydicom.Sequence()
        self._dataset.ReferencedRTTreatmentPhaseSequence.append(item.to_dataset())

    @property
    def RTPrescriptionLabel(self) -> Optional[str]:
        if "RTPrescriptionLabel" in self._dataset:
            return self._dataset.RTPrescriptionLabel
        return None

    @RTPrescriptionLabel.setter
    def RTPrescriptionLabel(self, value: Optional[str]):
        if value is None:
            if "RTPrescriptionLabel" in self._dataset:
                del self._dataset.RTPrescriptionLabel
        else:
            self._dataset.RTPrescriptionLabel = value

    @property
    def ReferencedRTPhysicianIntentIndex(self) -> Optional[int]:
        if "ReferencedRTPhysicianIntentIndex" in self._dataset:
            return self._dataset.ReferencedRTPhysicianIntentIndex
        return None

    @ReferencedRTPhysicianIntentIndex.setter
    def ReferencedRTPhysicianIntentIndex(self, value: Optional[int]):
        if value is None:
            if "ReferencedRTPhysicianIntentIndex" in self._dataset:
                del self._dataset.ReferencedRTPhysicianIntentIndex
        else:
            self._dataset.ReferencedRTPhysicianIntentIndex = value

    @property
    def RTAnatomicPrescriptionSequence(self) -> Optional[List[RTAnatomicPrescriptionSequenceItem]]:
        if "RTAnatomicPrescriptionSequence" in self._dataset:
            if len(self._RTAnatomicPrescriptionSequence) == len(self._dataset.RTAnatomicPrescriptionSequence):
                return self._RTAnatomicPrescriptionSequence
            else:
                return [RTAnatomicPrescriptionSequenceItem(x) for x in self._dataset.RTAnatomicPrescriptionSequence]
        return None

    @RTAnatomicPrescriptionSequence.setter
    def RTAnatomicPrescriptionSequence(self, value: Optional[List[RTAnatomicPrescriptionSequenceItem]]):
        if value is None:
            self._RTAnatomicPrescriptionSequence = []
            if "RTAnatomicPrescriptionSequence" in self._dataset:
                del self._dataset.RTAnatomicPrescriptionSequence
        elif not isinstance(value, list) or not all(isinstance(item, RTAnatomicPrescriptionSequenceItem) for item in value):
            raise ValueError("RTAnatomicPrescriptionSequence must be a list of RTAnatomicPrescriptionSequenceItem objects")
        else:
            self._RTAnatomicPrescriptionSequence = value
            if "RTAnatomicPrescriptionSequence" not in self._dataset:
                self._dataset.RTAnatomicPrescriptionSequence = pydicom.Sequence()
            self._dataset.RTAnatomicPrescriptionSequence.clear()
            self._dataset.RTAnatomicPrescriptionSequence.extend([item.to_dataset() for item in value])

    def add_RTAnatomicPrescription(self, item: RTAnatomicPrescriptionSequenceItem):
        if not isinstance(item, RTAnatomicPrescriptionSequenceItem):
            raise ValueError("Item must be an instance of RTAnatomicPrescriptionSequenceItem")
        self._RTAnatomicPrescriptionSequence.append(item)
        if "RTAnatomicPrescriptionSequence" not in self._dataset:
            self._dataset.RTAnatomicPrescriptionSequence = pydicom.Sequence()
        self._dataset.RTAnatomicPrescriptionSequence.append(item.to_dataset())

    @property
    def PriorTreatmentDoseDescription(self) -> Optional[str]:
        if "PriorTreatmentDoseDescription" in self._dataset:
            return self._dataset.PriorTreatmentDoseDescription
        return None

    @PriorTreatmentDoseDescription.setter
    def PriorTreatmentDoseDescription(self, value: Optional[str]):
        if value is None:
            if "PriorTreatmentDoseDescription" in self._dataset:
                del self._dataset.PriorTreatmentDoseDescription
        else:
            self._dataset.PriorTreatmentDoseDescription = value

    @property
    def PriorTreatmentReferenceSequence(self) -> Optional[List[PriorTreatmentReferenceSequenceItem]]:
        if "PriorTreatmentReferenceSequence" in self._dataset:
            if len(self._PriorTreatmentReferenceSequence) == len(self._dataset.PriorTreatmentReferenceSequence):
                return self._PriorTreatmentReferenceSequence
            else:
                return [PriorTreatmentReferenceSequenceItem(x) for x in self._dataset.PriorTreatmentReferenceSequence]
        return None

    @PriorTreatmentReferenceSequence.setter
    def PriorTreatmentReferenceSequence(self, value: Optional[List[PriorTreatmentReferenceSequenceItem]]):
        if value is None:
            self._PriorTreatmentReferenceSequence = []
            if "PriorTreatmentReferenceSequence" in self._dataset:
                del self._dataset.PriorTreatmentReferenceSequence
        elif not isinstance(value, list) or not all(isinstance(item, PriorTreatmentReferenceSequenceItem) for item in value):
            raise ValueError("PriorTreatmentReferenceSequence must be a list of PriorTreatmentReferenceSequenceItem objects")
        else:
            self._PriorTreatmentReferenceSequence = value
            if "PriorTreatmentReferenceSequence" not in self._dataset:
                self._dataset.PriorTreatmentReferenceSequence = pydicom.Sequence()
            self._dataset.PriorTreatmentReferenceSequence.clear()
            self._dataset.PriorTreatmentReferenceSequence.extend([item.to_dataset() for item in value])

    def add_PriorTreatmentReference(self, item: PriorTreatmentReferenceSequenceItem):
        if not isinstance(item, PriorTreatmentReferenceSequenceItem):
            raise ValueError("Item must be an instance of PriorTreatmentReferenceSequenceItem")
        self._PriorTreatmentReferenceSequence.append(item)
        if "PriorTreatmentReferenceSequence" not in self._dataset:
            self._dataset.PriorTreatmentReferenceSequence = pydicom.Sequence()
        self._dataset.PriorTreatmentReferenceSequence.append(item.to_dataset())

    @property
    def ReferencedDosimetricObjectivesSequence(self) -> Optional[List[ReferencedDosimetricObjectivesSequenceItem]]:
        if "ReferencedDosimetricObjectivesSequence" in self._dataset:
            if len(self._ReferencedDosimetricObjectivesSequence) == len(self._dataset.ReferencedDosimetricObjectivesSequence):
                return self._ReferencedDosimetricObjectivesSequence
            else:
                return [
                    ReferencedDosimetricObjectivesSequenceItem(x) for x in self._dataset.ReferencedDosimetricObjectivesSequence
                ]
        return None

    @ReferencedDosimetricObjectivesSequence.setter
    def ReferencedDosimetricObjectivesSequence(self, value: Optional[List[ReferencedDosimetricObjectivesSequenceItem]]):
        if value is None:
            self._ReferencedDosimetricObjectivesSequence = []
            if "ReferencedDosimetricObjectivesSequence" in self._dataset:
                del self._dataset.ReferencedDosimetricObjectivesSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, ReferencedDosimetricObjectivesSequenceItem) for item in value
        ):
            raise ValueError(
                "ReferencedDosimetricObjectivesSequence must be a list of ReferencedDosimetricObjectivesSequenceItem objects"
            )
        else:
            self._ReferencedDosimetricObjectivesSequence = value
            if "ReferencedDosimetricObjectivesSequence" not in self._dataset:
                self._dataset.ReferencedDosimetricObjectivesSequence = pydicom.Sequence()
            self._dataset.ReferencedDosimetricObjectivesSequence.clear()
            self._dataset.ReferencedDosimetricObjectivesSequence.extend([item.to_dataset() for item in value])

    def add_ReferencedDosimetricObjectives(self, item: ReferencedDosimetricObjectivesSequenceItem):
        if not isinstance(item, ReferencedDosimetricObjectivesSequenceItem):
            raise ValueError("Item must be an instance of ReferencedDosimetricObjectivesSequenceItem")
        self._ReferencedDosimetricObjectivesSequence.append(item)
        if "ReferencedDosimetricObjectivesSequence" not in self._dataset:
            self._dataset.ReferencedDosimetricObjectivesSequence = pydicom.Sequence()
        self._dataset.ReferencedDosimetricObjectivesSequence.append(item.to_dataset())

    @property
    def PlanningInputInformationSequence(self) -> Optional[List[PlanningInputInformationSequenceItem]]:
        if "PlanningInputInformationSequence" in self._dataset:
            if len(self._PlanningInputInformationSequence) == len(self._dataset.PlanningInputInformationSequence):
                return self._PlanningInputInformationSequence
            else:
                return [PlanningInputInformationSequenceItem(x) for x in self._dataset.PlanningInputInformationSequence]
        return None

    @PlanningInputInformationSequence.setter
    def PlanningInputInformationSequence(self, value: Optional[List[PlanningInputInformationSequenceItem]]):
        if value is None:
            self._PlanningInputInformationSequence = []
            if "PlanningInputInformationSequence" in self._dataset:
                del self._dataset.PlanningInputInformationSequence
        elif not isinstance(value, list) or not all(isinstance(item, PlanningInputInformationSequenceItem) for item in value):
            raise ValueError("PlanningInputInformationSequence must be a list of PlanningInputInformationSequenceItem objects")
        else:
            self._PlanningInputInformationSequence = value
            if "PlanningInputInformationSequence" not in self._dataset:
                self._dataset.PlanningInputInformationSequence = pydicom.Sequence()
            self._dataset.PlanningInputInformationSequence.clear()
            self._dataset.PlanningInputInformationSequence.extend([item.to_dataset() for item in value])

    def add_PlanningInputInformation(self, item: PlanningInputInformationSequenceItem):
        if not isinstance(item, PlanningInputInformationSequenceItem):
            raise ValueError("Item must be an instance of PlanningInputInformationSequenceItem")
        self._PlanningInputInformationSequence.append(item)
        if "PlanningInputInformationSequence" not in self._dataset:
            self._dataset.PlanningInputInformationSequence = pydicom.Sequence()
        self._dataset.PlanningInputInformationSequence.append(item.to_dataset())

    @property
    def FractionPatternSequence(self) -> Optional[List[FractionPatternSequenceItem]]:
        if "FractionPatternSequence" in self._dataset:
            if len(self._FractionPatternSequence) == len(self._dataset.FractionPatternSequence):
                return self._FractionPatternSequence
            else:
                return [FractionPatternSequenceItem(x) for x in self._dataset.FractionPatternSequence]
        return None

    @FractionPatternSequence.setter
    def FractionPatternSequence(self, value: Optional[List[FractionPatternSequenceItem]]):
        if value is None:
            self._FractionPatternSequence = []
            if "FractionPatternSequence" in self._dataset:
                del self._dataset.FractionPatternSequence
        elif not isinstance(value, list) or not all(isinstance(item, FractionPatternSequenceItem) for item in value):
            raise ValueError("FractionPatternSequence must be a list of FractionPatternSequenceItem objects")
        else:
            self._FractionPatternSequence = value
            if "FractionPatternSequence" not in self._dataset:
                self._dataset.FractionPatternSequence = pydicom.Sequence()
            self._dataset.FractionPatternSequence.clear()
            self._dataset.FractionPatternSequence.extend([item.to_dataset() for item in value])

    def add_FractionPattern(self, item: FractionPatternSequenceItem):
        if not isinstance(item, FractionPatternSequenceItem):
            raise ValueError("Item must be an instance of FractionPatternSequenceItem")
        self._FractionPatternSequence.append(item)
        if "FractionPatternSequence" not in self._dataset:
            self._dataset.FractionPatternSequence = pydicom.Sequence()
        self._dataset.FractionPatternSequence.append(item.to_dataset())

    @property
    def TreatmentTechniqueNotes(self) -> Optional[str]:
        if "TreatmentTechniqueNotes" in self._dataset:
            return self._dataset.TreatmentTechniqueNotes
        return None

    @TreatmentTechniqueNotes.setter
    def TreatmentTechniqueNotes(self, value: Optional[str]):
        if value is None:
            if "TreatmentTechniqueNotes" in self._dataset:
                del self._dataset.TreatmentTechniqueNotes
        else:
            self._dataset.TreatmentTechniqueNotes = value

    @property
    def PrescriptionNotes(self) -> Optional[str]:
        if "PrescriptionNotes" in self._dataset:
            return self._dataset.PrescriptionNotes
        return None

    @PrescriptionNotes.setter
    def PrescriptionNotes(self, value: Optional[str]):
        if value is None:
            if "PrescriptionNotes" in self._dataset:
                del self._dataset.PrescriptionNotes
        else:
            self._dataset.PrescriptionNotes = value

    @property
    def NumberOfFractions(self) -> Optional[int]:
        if "NumberOfFractions" in self._dataset:
            return self._dataset.NumberOfFractions
        return None

    @NumberOfFractions.setter
    def NumberOfFractions(self, value: Optional[int]):
        if value is None:
            if "NumberOfFractions" in self._dataset:
                del self._dataset.NumberOfFractions
        else:
            self._dataset.NumberOfFractions = value

    @property
    def IntendedDeliveryDuration(self) -> Optional[int]:
        if "IntendedDeliveryDuration" in self._dataset:
            return self._dataset.IntendedDeliveryDuration
        return None

    @IntendedDeliveryDuration.setter
    def IntendedDeliveryDuration(self, value: Optional[int]):
        if value is None:
            if "IntendedDeliveryDuration" in self._dataset:
                del self._dataset.IntendedDeliveryDuration
        else:
            self._dataset.IntendedDeliveryDuration = value

    @property
    def FractionationNotes(self) -> Optional[str]:
        if "FractionationNotes" in self._dataset:
            return self._dataset.FractionationNotes
        return None

    @FractionationNotes.setter
    def FractionationNotes(self, value: Optional[str]):
        if value is None:
            if "FractionationNotes" in self._dataset:
                del self._dataset.FractionationNotes
        else:
            self._dataset.FractionationNotes = value

    @property
    def RTTreatmentTechniqueCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "RTTreatmentTechniqueCodeSequence" in self._dataset:
            if len(self._RTTreatmentTechniqueCodeSequence) == len(self._dataset.RTTreatmentTechniqueCodeSequence):
                return self._RTTreatmentTechniqueCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.RTTreatmentTechniqueCodeSequence]
        return None

    @RTTreatmentTechniqueCodeSequence.setter
    def RTTreatmentTechniqueCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._RTTreatmentTechniqueCodeSequence = []
            if "RTTreatmentTechniqueCodeSequence" in self._dataset:
                del self._dataset.RTTreatmentTechniqueCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("RTTreatmentTechniqueCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._RTTreatmentTechniqueCodeSequence = value
            if "RTTreatmentTechniqueCodeSequence" not in self._dataset:
                self._dataset.RTTreatmentTechniqueCodeSequence = pydicom.Sequence()
            self._dataset.RTTreatmentTechniqueCodeSequence.clear()
            self._dataset.RTTreatmentTechniqueCodeSequence.extend([item.to_dataset() for item in value])

    def add_RTTreatmentTechniqueCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._RTTreatmentTechniqueCodeSequence.append(item)
        if "RTTreatmentTechniqueCodeSequence" not in self._dataset:
            self._dataset.RTTreatmentTechniqueCodeSequence = pydicom.Sequence()
        self._dataset.RTTreatmentTechniqueCodeSequence.append(item.to_dataset())

    @property
    def PrescriptionNotesSequence(self) -> Optional[List[PrescriptionNotesSequenceItem]]:
        if "PrescriptionNotesSequence" in self._dataset:
            if len(self._PrescriptionNotesSequence) == len(self._dataset.PrescriptionNotesSequence):
                return self._PrescriptionNotesSequence
            else:
                return [PrescriptionNotesSequenceItem(x) for x in self._dataset.PrescriptionNotesSequence]
        return None

    @PrescriptionNotesSequence.setter
    def PrescriptionNotesSequence(self, value: Optional[List[PrescriptionNotesSequenceItem]]):
        if value is None:
            self._PrescriptionNotesSequence = []
            if "PrescriptionNotesSequence" in self._dataset:
                del self._dataset.PrescriptionNotesSequence
        elif not isinstance(value, list) or not all(isinstance(item, PrescriptionNotesSequenceItem) for item in value):
            raise ValueError("PrescriptionNotesSequence must be a list of PrescriptionNotesSequenceItem objects")
        else:
            self._PrescriptionNotesSequence = value
            if "PrescriptionNotesSequence" not in self._dataset:
                self._dataset.PrescriptionNotesSequence = pydicom.Sequence()
            self._dataset.PrescriptionNotesSequence.clear()
            self._dataset.PrescriptionNotesSequence.extend([item.to_dataset() for item in value])

    def add_PrescriptionNotes(self, item: PrescriptionNotesSequenceItem):
        if not isinstance(item, PrescriptionNotesSequenceItem):
            raise ValueError("Item must be an instance of PrescriptionNotesSequenceItem")
        self._PrescriptionNotesSequence.append(item)
        if "PrescriptionNotesSequence" not in self._dataset:
            self._dataset.PrescriptionNotesSequence = pydicom.Sequence()
        self._dataset.PrescriptionNotesSequence.append(item.to_dataset())

    @property
    def FractionBasedRelationshipSequence(self) -> Optional[List[FractionBasedRelationshipSequenceItem]]:
        if "FractionBasedRelationshipSequence" in self._dataset:
            if len(self._FractionBasedRelationshipSequence) == len(self._dataset.FractionBasedRelationshipSequence):
                return self._FractionBasedRelationshipSequence
            else:
                return [FractionBasedRelationshipSequenceItem(x) for x in self._dataset.FractionBasedRelationshipSequence]
        return None

    @FractionBasedRelationshipSequence.setter
    def FractionBasedRelationshipSequence(self, value: Optional[List[FractionBasedRelationshipSequenceItem]]):
        if value is None:
            self._FractionBasedRelationshipSequence = []
            if "FractionBasedRelationshipSequence" in self._dataset:
                del self._dataset.FractionBasedRelationshipSequence
        elif not isinstance(value, list) or not all(isinstance(item, FractionBasedRelationshipSequenceItem) for item in value):
            raise ValueError(
                "FractionBasedRelationshipSequence must be a list of FractionBasedRelationshipSequenceItem objects"
            )
        else:
            self._FractionBasedRelationshipSequence = value
            if "FractionBasedRelationshipSequence" not in self._dataset:
                self._dataset.FractionBasedRelationshipSequence = pydicom.Sequence()
            self._dataset.FractionBasedRelationshipSequence.clear()
            self._dataset.FractionBasedRelationshipSequence.extend([item.to_dataset() for item in value])

    def add_FractionBasedRelationship(self, item: FractionBasedRelationshipSequenceItem):
        if not isinstance(item, FractionBasedRelationshipSequenceItem):
            raise ValueError("Item must be an instance of FractionBasedRelationshipSequenceItem")
        self._FractionBasedRelationshipSequence.append(item)
        if "FractionBasedRelationshipSequence" not in self._dataset:
            self._dataset.FractionBasedRelationshipSequence = pydicom.Sequence()
        self._dataset.FractionBasedRelationshipSequence.append(item.to_dataset())

    @property
    def DeliveryTimeStructureCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "DeliveryTimeStructureCodeSequence" in self._dataset:
            if len(self._DeliveryTimeStructureCodeSequence) == len(self._dataset.DeliveryTimeStructureCodeSequence):
                return self._DeliveryTimeStructureCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.DeliveryTimeStructureCodeSequence]
        return None

    @DeliveryTimeStructureCodeSequence.setter
    def DeliveryTimeStructureCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._DeliveryTimeStructureCodeSequence = []
            if "DeliveryTimeStructureCodeSequence" in self._dataset:
                del self._dataset.DeliveryTimeStructureCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("DeliveryTimeStructureCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._DeliveryTimeStructureCodeSequence = value
            if "DeliveryTimeStructureCodeSequence" not in self._dataset:
                self._dataset.DeliveryTimeStructureCodeSequence = pydicom.Sequence()
            self._dataset.DeliveryTimeStructureCodeSequence.clear()
            self._dataset.DeliveryTimeStructureCodeSequence.extend([item.to_dataset() for item in value])

    def add_DeliveryTimeStructureCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._DeliveryTimeStructureCodeSequence.append(item)
        if "DeliveryTimeStructureCodeSequence" not in self._dataset:
            self._dataset.DeliveryTimeStructureCodeSequence = pydicom.Sequence()
        self._dataset.DeliveryTimeStructureCodeSequence.append(item.to_dataset())
