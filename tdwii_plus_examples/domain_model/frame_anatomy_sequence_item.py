from typing import Any, List, Optional  # noqa

import pydicom

from .anatomic_region_sequence_item import AnatomicRegionSequenceItem
from .primary_anatomic_structure_sequence_item import (
    PrimaryAnatomicStructureSequenceItem,
)


class FrameAnatomySequenceItem:
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
            raise ValueError("AnatomicRegionSequence must be a list of AnatomicRegionSequenceItem objects")
        else:
            self._AnatomicRegionSequence = value
            if "AnatomicRegionSequence" not in self._dataset:
                self._dataset.AnatomicRegionSequence = pydicom.Sequence()
            self._dataset.AnatomicRegionSequence.clear()
            self._dataset.AnatomicRegionSequence.extend([item.to_dataset() for item in value])

    def add_AnatomicRegion(self, item: AnatomicRegionSequenceItem):
        if not isinstance(item, AnatomicRegionSequenceItem):
            raise ValueError("Item must be an instance of AnatomicRegionSequenceItem")
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
            raise ValueError("PrimaryAnatomicStructureSequence must be a list of PrimaryAnatomicStructureSequenceItem objects")
        else:
            self._PrimaryAnatomicStructureSequence = value
            if "PrimaryAnatomicStructureSequence" not in self._dataset:
                self._dataset.PrimaryAnatomicStructureSequence = pydicom.Sequence()
            self._dataset.PrimaryAnatomicStructureSequence.clear()
            self._dataset.PrimaryAnatomicStructureSequence.extend([item.to_dataset() for item in value])

    def add_PrimaryAnatomicStructure(self, item: PrimaryAnatomicStructureSequenceItem):
        if not isinstance(item, PrimaryAnatomicStructureSequenceItem):
            raise ValueError("Item must be an instance of PrimaryAnatomicStructureSequenceItem")
        self._PrimaryAnatomicStructureSequence.append(item)
        if "PrimaryAnatomicStructureSequence" not in self._dataset:
            self._dataset.PrimaryAnatomicStructureSequence = pydicom.Sequence()
        self._dataset.PrimaryAnatomicStructureSequence.append(item.to_dataset())

    @property
    def FrameLaterality(self) -> Optional[str]:
        if "FrameLaterality" in self._dataset:
            return self._dataset.FrameLaterality
        return None

    @FrameLaterality.setter
    def FrameLaterality(self, value: Optional[str]):
        if value is None:
            if "FrameLaterality" in self._dataset:
                del self._dataset.FrameLaterality
        else:
            self._dataset.FrameLaterality = value