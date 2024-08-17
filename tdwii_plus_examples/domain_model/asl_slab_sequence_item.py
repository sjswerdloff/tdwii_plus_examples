from typing import Any, List, Optional

import pydicom

from .anatomic_region_sequence_item import AnatomicRegionSequenceItem
from .primary_anatomic_structure_sequence_item import (
    PrimaryAnatomicStructureSequenceItem,
)


class ASLSlabSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._AnatomicRegionSequence: List[AnatomicRegionSequenceItem] = []
        self._PrimaryAnatomicStructureSequence: List[PrimaryAnatomicStructureSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def AnatomicRegionSequence(self) -> Optional[List[AnatomicRegionSequenceItem]]:
        if "AnatomicRegionSequence" in self._dataset:
            if len(self._AnatomicRegionSequence) == len(self._dataset.AnatomicRegionSequence):
                return self._AnatomicRegionSequence
            else:
                return [AnatomicRegionSequenceItem(x) for x in self._dataset.AnatomicRegionSequence]
        return None

    @AnatomicRegionSequence.setter
    def AnatomicRegionSequence(self, value: Optional[List[AnatomicRegionSequenceItem]]):
        if value is None:
            self._AnatomicRegionSequence = []
            if "AnatomicRegionSequence" in self._dataset:
                del self._dataset.AnatomicRegionSequence
        elif not isinstance(value, list) or not all(isinstance(item, AnatomicRegionSequenceItem) for item in value):
            raise ValueError(f"AnatomicRegionSequence must be a list of AnatomicRegionSequenceItem objects")
        else:
            self._AnatomicRegionSequence = value
            if "AnatomicRegionSequence" not in self._dataset:
                self._dataset.AnatomicRegionSequence = pydicom.Sequence()
            self._dataset.AnatomicRegionSequence.clear()
            self._dataset.AnatomicRegionSequence.extend([item.to_dataset() for item in value])

    def add_AnatomicRegion(self, item: AnatomicRegionSequenceItem):
        if not isinstance(item, AnatomicRegionSequenceItem):
            raise ValueError(f"Item must be an instance of AnatomicRegionSequenceItem")
        self._AnatomicRegionSequence.append(item)
        if "AnatomicRegionSequence" not in self._dataset:
            self._dataset.AnatomicRegionSequence = pydicom.Sequence()
        self._dataset.AnatomicRegionSequence.append(item.to_dataset())

    @property
    def PrimaryAnatomicStructureSequence(self) -> Optional[List[PrimaryAnatomicStructureSequenceItem]]:
        if "PrimaryAnatomicStructureSequence" in self._dataset:
            if len(self._PrimaryAnatomicStructureSequence) == len(self._dataset.PrimaryAnatomicStructureSequence):
                return self._PrimaryAnatomicStructureSequence
            else:
                return [PrimaryAnatomicStructureSequenceItem(x) for x in self._dataset.PrimaryAnatomicStructureSequence]
        return None

    @PrimaryAnatomicStructureSequence.setter
    def PrimaryAnatomicStructureSequence(self, value: Optional[List[PrimaryAnatomicStructureSequenceItem]]):
        if value is None:
            self._PrimaryAnatomicStructureSequence = []
            if "PrimaryAnatomicStructureSequence" in self._dataset:
                del self._dataset.PrimaryAnatomicStructureSequence
        elif not isinstance(value, list) or not all(isinstance(item, PrimaryAnatomicStructureSequenceItem) for item in value):
            raise ValueError(
                f"PrimaryAnatomicStructureSequence must be a list of PrimaryAnatomicStructureSequenceItem objects"
            )
        else:
            self._PrimaryAnatomicStructureSequence = value
            if "PrimaryAnatomicStructureSequence" not in self._dataset:
                self._dataset.PrimaryAnatomicStructureSequence = pydicom.Sequence()
            self._dataset.PrimaryAnatomicStructureSequence.clear()
            self._dataset.PrimaryAnatomicStructureSequence.extend([item.to_dataset() for item in value])

    def add_PrimaryAnatomicStructure(self, item: PrimaryAnatomicStructureSequenceItem):
        if not isinstance(item, PrimaryAnatomicStructureSequenceItem):
            raise ValueError(f"Item must be an instance of PrimaryAnatomicStructureSequenceItem")
        self._PrimaryAnatomicStructureSequence.append(item)
        if "PrimaryAnatomicStructureSequence" not in self._dataset:
            self._dataset.PrimaryAnatomicStructureSequence = pydicom.Sequence()
        self._dataset.PrimaryAnatomicStructureSequence.append(item.to_dataset())

    @property
    def ASLSlabNumber(self) -> Optional[int]:
        if "ASLSlabNumber" in self._dataset:
            return self._dataset.ASLSlabNumber
        return None

    @ASLSlabNumber.setter
    def ASLSlabNumber(self, value: Optional[int]):
        if value is None:
            if "ASLSlabNumber" in self._dataset:
                del self._dataset.ASLSlabNumber
        else:
            self._dataset.ASLSlabNumber = value

    @property
    def ASLSlabThickness(self) -> Optional[float]:
        if "ASLSlabThickness" in self._dataset:
            return self._dataset.ASLSlabThickness
        return None

    @ASLSlabThickness.setter
    def ASLSlabThickness(self, value: Optional[float]):
        if value is None:
            if "ASLSlabThickness" in self._dataset:
                del self._dataset.ASLSlabThickness
        else:
            self._dataset.ASLSlabThickness = value

    @property
    def ASLSlabOrientation(self) -> Optional[List[float]]:
        if "ASLSlabOrientation" in self._dataset:
            return self._dataset.ASLSlabOrientation
        return None

    @ASLSlabOrientation.setter
    def ASLSlabOrientation(self, value: Optional[List[float]]):
        if value is None:
            if "ASLSlabOrientation" in self._dataset:
                del self._dataset.ASLSlabOrientation
        else:
            self._dataset.ASLSlabOrientation = value

    @property
    def ASLMidSlabPosition(self) -> Optional[List[float]]:
        if "ASLMidSlabPosition" in self._dataset:
            return self._dataset.ASLMidSlabPosition
        return None

    @ASLMidSlabPosition.setter
    def ASLMidSlabPosition(self, value: Optional[List[float]]):
        if value is None:
            if "ASLMidSlabPosition" in self._dataset:
                del self._dataset.ASLMidSlabPosition
        else:
            self._dataset.ASLMidSlabPosition = value

    @property
    def ASLPulseTrainDuration(self) -> Optional[int]:
        if "ASLPulseTrainDuration" in self._dataset:
            return self._dataset.ASLPulseTrainDuration
        return None

    @ASLPulseTrainDuration.setter
    def ASLPulseTrainDuration(self, value: Optional[int]):
        if value is None:
            if "ASLPulseTrainDuration" in self._dataset:
                del self._dataset.ASLPulseTrainDuration
        else:
            self._dataset.ASLPulseTrainDuration = value
