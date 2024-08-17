from typing import Any, List, Optional

import pydicom

from .definition_source_sequence_item import DefinitionSourceSequenceItem
from .referenced_beam_sequence_item import ReferencedBeamSequenceItem
from .referenced_brachy_application_setup_sequence_item import (
    ReferencedBrachyApplicationSetupSequenceItem,
)
from .referenced_dose_reference_sequence_item import ReferencedDoseReferenceSequenceItem
from .referenced_dose_sequence_item import ReferencedDoseSequenceItem


class FractionGroupSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._DefinitionSourceSequence: List[DefinitionSourceSequenceItem] = []
        self._ReferencedBeamSequence: List[ReferencedBeamSequenceItem] = []
        self._ReferencedBrachyApplicationSetupSequence: List[ReferencedBrachyApplicationSetupSequenceItem] = []
        self._ReferencedDoseReferenceSequence: List[ReferencedDoseReferenceSequenceItem] = []
        self._ReferencedDoseSequence: List[ReferencedDoseSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def DefinitionSourceSequence(self) -> Optional[List[DefinitionSourceSequenceItem]]:
        if "DefinitionSourceSequence" in self._dataset:
            if len(self._DefinitionSourceSequence) == len(self._dataset.DefinitionSourceSequence):
                return self._DefinitionSourceSequence
            else:
                return [DefinitionSourceSequenceItem(x) for x in self._dataset.DefinitionSourceSequence]
        return None

    @DefinitionSourceSequence.setter
    def DefinitionSourceSequence(self, value: Optional[List[DefinitionSourceSequenceItem]]):
        if value is None:
            self._DefinitionSourceSequence = []
            if "DefinitionSourceSequence" in self._dataset:
                del self._dataset.DefinitionSourceSequence
        elif not isinstance(value, list) or not all(isinstance(item, DefinitionSourceSequenceItem) for item in value):
            raise ValueError(f"DefinitionSourceSequence must be a list of DefinitionSourceSequenceItem objects")
        else:
            self._DefinitionSourceSequence = value
            if "DefinitionSourceSequence" not in self._dataset:
                self._dataset.DefinitionSourceSequence = pydicom.Sequence()
            self._dataset.DefinitionSourceSequence.clear()
            self._dataset.DefinitionSourceSequence.extend([item.to_dataset() for item in value])

    def add_DefinitionSource(self, item: DefinitionSourceSequenceItem):
        if not isinstance(item, DefinitionSourceSequenceItem):
            raise ValueError(f"Item must be an instance of DefinitionSourceSequenceItem")
        self._DefinitionSourceSequence.append(item)
        if "DefinitionSourceSequence" not in self._dataset:
            self._dataset.DefinitionSourceSequence = pydicom.Sequence()
        self._dataset.DefinitionSourceSequence.append(item.to_dataset())

    @property
    def FractionGroupNumber(self) -> Optional[int]:
        if "FractionGroupNumber" in self._dataset:
            return self._dataset.FractionGroupNumber
        return None

    @FractionGroupNumber.setter
    def FractionGroupNumber(self, value: Optional[int]):
        if value is None:
            if "FractionGroupNumber" in self._dataset:
                del self._dataset.FractionGroupNumber
        else:
            self._dataset.FractionGroupNumber = value

    @property
    def FractionGroupDescription(self) -> Optional[str]:
        if "FractionGroupDescription" in self._dataset:
            return self._dataset.FractionGroupDescription
        return None

    @FractionGroupDescription.setter
    def FractionGroupDescription(self, value: Optional[str]):
        if value is None:
            if "FractionGroupDescription" in self._dataset:
                del self._dataset.FractionGroupDescription
        else:
            self._dataset.FractionGroupDescription = value

    @property
    def NumberOfFractionsPlanned(self) -> Optional[int]:
        if "NumberOfFractionsPlanned" in self._dataset:
            return self._dataset.NumberOfFractionsPlanned
        return None

    @NumberOfFractionsPlanned.setter
    def NumberOfFractionsPlanned(self, value: Optional[int]):
        if value is None:
            if "NumberOfFractionsPlanned" in self._dataset:
                del self._dataset.NumberOfFractionsPlanned
        else:
            self._dataset.NumberOfFractionsPlanned = value

    @property
    def NumberOfFractionPatternDigitsPerDay(self) -> Optional[int]:
        if "NumberOfFractionPatternDigitsPerDay" in self._dataset:
            return self._dataset.NumberOfFractionPatternDigitsPerDay
        return None

    @NumberOfFractionPatternDigitsPerDay.setter
    def NumberOfFractionPatternDigitsPerDay(self, value: Optional[int]):
        if value is None:
            if "NumberOfFractionPatternDigitsPerDay" in self._dataset:
                del self._dataset.NumberOfFractionPatternDigitsPerDay
        else:
            self._dataset.NumberOfFractionPatternDigitsPerDay = value

    @property
    def RepeatFractionCycleLength(self) -> Optional[int]:
        if "RepeatFractionCycleLength" in self._dataset:
            return self._dataset.RepeatFractionCycleLength
        return None

    @RepeatFractionCycleLength.setter
    def RepeatFractionCycleLength(self, value: Optional[int]):
        if value is None:
            if "RepeatFractionCycleLength" in self._dataset:
                del self._dataset.RepeatFractionCycleLength
        else:
            self._dataset.RepeatFractionCycleLength = value

    @property
    def FractionPattern(self) -> Optional[str]:
        if "FractionPattern" in self._dataset:
            return self._dataset.FractionPattern
        return None

    @FractionPattern.setter
    def FractionPattern(self, value: Optional[str]):
        if value is None:
            if "FractionPattern" in self._dataset:
                del self._dataset.FractionPattern
        else:
            self._dataset.FractionPattern = value

    @property
    def NumberOfBeams(self) -> Optional[int]:
        if "NumberOfBeams" in self._dataset:
            return self._dataset.NumberOfBeams
        return None

    @NumberOfBeams.setter
    def NumberOfBeams(self, value: Optional[int]):
        if value is None:
            if "NumberOfBeams" in self._dataset:
                del self._dataset.NumberOfBeams
        else:
            self._dataset.NumberOfBeams = value

    @property
    def BeamDoseMeaning(self) -> Optional[str]:
        if "BeamDoseMeaning" in self._dataset:
            return self._dataset.BeamDoseMeaning
        return None

    @BeamDoseMeaning.setter
    def BeamDoseMeaning(self, value: Optional[str]):
        if value is None:
            if "BeamDoseMeaning" in self._dataset:
                del self._dataset.BeamDoseMeaning
        else:
            self._dataset.BeamDoseMeaning = value

    @property
    def NumberOfBrachyApplicationSetups(self) -> Optional[int]:
        if "NumberOfBrachyApplicationSetups" in self._dataset:
            return self._dataset.NumberOfBrachyApplicationSetups
        return None

    @NumberOfBrachyApplicationSetups.setter
    def NumberOfBrachyApplicationSetups(self, value: Optional[int]):
        if value is None:
            if "NumberOfBrachyApplicationSetups" in self._dataset:
                del self._dataset.NumberOfBrachyApplicationSetups
        else:
            self._dataset.NumberOfBrachyApplicationSetups = value

    @property
    def ReferencedBeamSequence(self) -> Optional[List[ReferencedBeamSequenceItem]]:
        if "ReferencedBeamSequence" in self._dataset:
            if len(self._ReferencedBeamSequence) == len(self._dataset.ReferencedBeamSequence):
                return self._ReferencedBeamSequence
            else:
                return [ReferencedBeamSequenceItem(x) for x in self._dataset.ReferencedBeamSequence]
        return None

    @ReferencedBeamSequence.setter
    def ReferencedBeamSequence(self, value: Optional[List[ReferencedBeamSequenceItem]]):
        if value is None:
            self._ReferencedBeamSequence = []
            if "ReferencedBeamSequence" in self._dataset:
                del self._dataset.ReferencedBeamSequence
        elif not isinstance(value, list) or not all(isinstance(item, ReferencedBeamSequenceItem) for item in value):
            raise ValueError(f"ReferencedBeamSequence must be a list of ReferencedBeamSequenceItem objects")
        else:
            self._ReferencedBeamSequence = value
            if "ReferencedBeamSequence" not in self._dataset:
                self._dataset.ReferencedBeamSequence = pydicom.Sequence()
            self._dataset.ReferencedBeamSequence.clear()
            self._dataset.ReferencedBeamSequence.extend([item.to_dataset() for item in value])

    def add_ReferencedBeam(self, item: ReferencedBeamSequenceItem):
        if not isinstance(item, ReferencedBeamSequenceItem):
            raise ValueError(f"Item must be an instance of ReferencedBeamSequenceItem")
        self._ReferencedBeamSequence.append(item)
        if "ReferencedBeamSequence" not in self._dataset:
            self._dataset.ReferencedBeamSequence = pydicom.Sequence()
        self._dataset.ReferencedBeamSequence.append(item.to_dataset())

    @property
    def ReferencedBrachyApplicationSetupSequence(self) -> Optional[List[ReferencedBrachyApplicationSetupSequenceItem]]:
        if "ReferencedBrachyApplicationSetupSequence" in self._dataset:
            if len(self._ReferencedBrachyApplicationSetupSequence) == len(
                self._dataset.ReferencedBrachyApplicationSetupSequence
            ):
                return self._ReferencedBrachyApplicationSetupSequence
            else:
                return [
                    ReferencedBrachyApplicationSetupSequenceItem(x)
                    for x in self._dataset.ReferencedBrachyApplicationSetupSequence
                ]
        return None

    @ReferencedBrachyApplicationSetupSequence.setter
    def ReferencedBrachyApplicationSetupSequence(self, value: Optional[List[ReferencedBrachyApplicationSetupSequenceItem]]):
        if value is None:
            self._ReferencedBrachyApplicationSetupSequence = []
            if "ReferencedBrachyApplicationSetupSequence" in self._dataset:
                del self._dataset.ReferencedBrachyApplicationSetupSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, ReferencedBrachyApplicationSetupSequenceItem) for item in value
        ):
            raise ValueError(
                f"ReferencedBrachyApplicationSetupSequence must be a list of ReferencedBrachyApplicationSetupSequenceItem objects"
            )
        else:
            self._ReferencedBrachyApplicationSetupSequence = value
            if "ReferencedBrachyApplicationSetupSequence" not in self._dataset:
                self._dataset.ReferencedBrachyApplicationSetupSequence = pydicom.Sequence()
            self._dataset.ReferencedBrachyApplicationSetupSequence.clear()
            self._dataset.ReferencedBrachyApplicationSetupSequence.extend([item.to_dataset() for item in value])

    def add_ReferencedBrachyApplicationSetup(self, item: ReferencedBrachyApplicationSetupSequenceItem):
        if not isinstance(item, ReferencedBrachyApplicationSetupSequenceItem):
            raise ValueError(f"Item must be an instance of ReferencedBrachyApplicationSetupSequenceItem")
        self._ReferencedBrachyApplicationSetupSequence.append(item)
        if "ReferencedBrachyApplicationSetupSequence" not in self._dataset:
            self._dataset.ReferencedBrachyApplicationSetupSequence = pydicom.Sequence()
        self._dataset.ReferencedBrachyApplicationSetupSequence.append(item.to_dataset())

    @property
    def ReferencedDoseReferenceSequence(self) -> Optional[List[ReferencedDoseReferenceSequenceItem]]:
        if "ReferencedDoseReferenceSequence" in self._dataset:
            if len(self._ReferencedDoseReferenceSequence) == len(self._dataset.ReferencedDoseReferenceSequence):
                return self._ReferencedDoseReferenceSequence
            else:
                return [ReferencedDoseReferenceSequenceItem(x) for x in self._dataset.ReferencedDoseReferenceSequence]
        return None

    @ReferencedDoseReferenceSequence.setter
    def ReferencedDoseReferenceSequence(self, value: Optional[List[ReferencedDoseReferenceSequenceItem]]):
        if value is None:
            self._ReferencedDoseReferenceSequence = []
            if "ReferencedDoseReferenceSequence" in self._dataset:
                del self._dataset.ReferencedDoseReferenceSequence
        elif not isinstance(value, list) or not all(isinstance(item, ReferencedDoseReferenceSequenceItem) for item in value):
            raise ValueError(f"ReferencedDoseReferenceSequence must be a list of ReferencedDoseReferenceSequenceItem objects")
        else:
            self._ReferencedDoseReferenceSequence = value
            if "ReferencedDoseReferenceSequence" not in self._dataset:
                self._dataset.ReferencedDoseReferenceSequence = pydicom.Sequence()
            self._dataset.ReferencedDoseReferenceSequence.clear()
            self._dataset.ReferencedDoseReferenceSequence.extend([item.to_dataset() for item in value])

    def add_ReferencedDoseReference(self, item: ReferencedDoseReferenceSequenceItem):
        if not isinstance(item, ReferencedDoseReferenceSequenceItem):
            raise ValueError(f"Item must be an instance of ReferencedDoseReferenceSequenceItem")
        self._ReferencedDoseReferenceSequence.append(item)
        if "ReferencedDoseReferenceSequence" not in self._dataset:
            self._dataset.ReferencedDoseReferenceSequence = pydicom.Sequence()
        self._dataset.ReferencedDoseReferenceSequence.append(item.to_dataset())

    @property
    def ReferencedDoseSequence(self) -> Optional[List[ReferencedDoseSequenceItem]]:
        if "ReferencedDoseSequence" in self._dataset:
            if len(self._ReferencedDoseSequence) == len(self._dataset.ReferencedDoseSequence):
                return self._ReferencedDoseSequence
            else:
                return [ReferencedDoseSequenceItem(x) for x in self._dataset.ReferencedDoseSequence]
        return None

    @ReferencedDoseSequence.setter
    def ReferencedDoseSequence(self, value: Optional[List[ReferencedDoseSequenceItem]]):
        if value is None:
            self._ReferencedDoseSequence = []
            if "ReferencedDoseSequence" in self._dataset:
                del self._dataset.ReferencedDoseSequence
        elif not isinstance(value, list) or not all(isinstance(item, ReferencedDoseSequenceItem) for item in value):
            raise ValueError(f"ReferencedDoseSequence must be a list of ReferencedDoseSequenceItem objects")
        else:
            self._ReferencedDoseSequence = value
            if "ReferencedDoseSequence" not in self._dataset:
                self._dataset.ReferencedDoseSequence = pydicom.Sequence()
            self._dataset.ReferencedDoseSequence.clear()
            self._dataset.ReferencedDoseSequence.extend([item.to_dataset() for item in value])

    def add_ReferencedDose(self, item: ReferencedDoseSequenceItem):
        if not isinstance(item, ReferencedDoseSequenceItem):
            raise ValueError(f"Item must be an instance of ReferencedDoseSequenceItem")
        self._ReferencedDoseSequence.append(item)
        if "ReferencedDoseSequence" not in self._dataset:
            self._dataset.ReferencedDoseSequence = pydicom.Sequence()
        self._dataset.ReferencedDoseSequence.append(item.to_dataset())
