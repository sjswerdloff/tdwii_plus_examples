from typing import Any, List, Optional

import pydicom

from .combination_segment_reference_sequence_item import (
    CombinationSegmentReferenceSequenceItem,
)
from .direct_segment_reference_sequence_item import DirectSegmentReferenceSequenceItem


class SegmentReferenceSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._DirectSegmentReferenceSequence: List[DirectSegmentReferenceSequenceItem] = []
        self._CombinationSegmentReferenceSequence: List[CombinationSegmentReferenceSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def SegmentReferenceIndex(self) -> Optional[int]:
        if "SegmentReferenceIndex" in self._dataset:
            return self._dataset.SegmentReferenceIndex
        return None

    @SegmentReferenceIndex.setter
    def SegmentReferenceIndex(self, value: Optional[int]):
        if value is None:
            if "SegmentReferenceIndex" in self._dataset:
                del self._dataset.SegmentReferenceIndex
        else:
            self._dataset.SegmentReferenceIndex = value

    @property
    def DirectSegmentReferenceSequence(self) -> Optional[List[DirectSegmentReferenceSequenceItem]]:
        if "DirectSegmentReferenceSequence" in self._dataset:
            if len(self._DirectSegmentReferenceSequence) == len(self._dataset.DirectSegmentReferenceSequence):
                return self._DirectSegmentReferenceSequence
            else:
                return [DirectSegmentReferenceSequenceItem(x) for x in self._dataset.DirectSegmentReferenceSequence]
        return None

    @DirectSegmentReferenceSequence.setter
    def DirectSegmentReferenceSequence(self, value: Optional[List[DirectSegmentReferenceSequenceItem]]):
        if value is None:
            self._DirectSegmentReferenceSequence = []
            if "DirectSegmentReferenceSequence" in self._dataset:
                del self._dataset.DirectSegmentReferenceSequence
        elif not isinstance(value, list) or not all(isinstance(item, DirectSegmentReferenceSequenceItem) for item in value):
            raise ValueError(f"DirectSegmentReferenceSequence must be a list of DirectSegmentReferenceSequenceItem objects")
        else:
            self._DirectSegmentReferenceSequence = value
            if "DirectSegmentReferenceSequence" not in self._dataset:
                self._dataset.DirectSegmentReferenceSequence = pydicom.Sequence()
            self._dataset.DirectSegmentReferenceSequence.clear()
            self._dataset.DirectSegmentReferenceSequence.extend([item.to_dataset() for item in value])

    def add_DirectSegmentReference(self, item: DirectSegmentReferenceSequenceItem):
        if not isinstance(item, DirectSegmentReferenceSequenceItem):
            raise ValueError(f"Item must be an instance of DirectSegmentReferenceSequenceItem")
        self._DirectSegmentReferenceSequence.append(item)
        if "DirectSegmentReferenceSequence" not in self._dataset:
            self._dataset.DirectSegmentReferenceSequence = pydicom.Sequence()
        self._dataset.DirectSegmentReferenceSequence.append(item.to_dataset())

    @property
    def CombinationSegmentReferenceSequence(self) -> Optional[List[CombinationSegmentReferenceSequenceItem]]:
        if "CombinationSegmentReferenceSequence" in self._dataset:
            if len(self._CombinationSegmentReferenceSequence) == len(self._dataset.CombinationSegmentReferenceSequence):
                return self._CombinationSegmentReferenceSequence
            else:
                return [CombinationSegmentReferenceSequenceItem(x) for x in self._dataset.CombinationSegmentReferenceSequence]
        return None

    @CombinationSegmentReferenceSequence.setter
    def CombinationSegmentReferenceSequence(self, value: Optional[List[CombinationSegmentReferenceSequenceItem]]):
        if value is None:
            self._CombinationSegmentReferenceSequence = []
            if "CombinationSegmentReferenceSequence" in self._dataset:
                del self._dataset.CombinationSegmentReferenceSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, CombinationSegmentReferenceSequenceItem) for item in value
        ):
            raise ValueError(
                f"CombinationSegmentReferenceSequence must be a list of CombinationSegmentReferenceSequenceItem objects"
            )
        else:
            self._CombinationSegmentReferenceSequence = value
            if "CombinationSegmentReferenceSequence" not in self._dataset:
                self._dataset.CombinationSegmentReferenceSequence = pydicom.Sequence()
            self._dataset.CombinationSegmentReferenceSequence.clear()
            self._dataset.CombinationSegmentReferenceSequence.extend([item.to_dataset() for item in value])

    def add_CombinationSegmentReference(self, item: CombinationSegmentReferenceSequenceItem):
        if not isinstance(item, CombinationSegmentReferenceSequenceItem):
            raise ValueError(f"Item must be an instance of CombinationSegmentReferenceSequenceItem")
        self._CombinationSegmentReferenceSequence.append(item)
        if "CombinationSegmentReferenceSequence" not in self._dataset:
            self._dataset.CombinationSegmentReferenceSequence = pydicom.Sequence()
        self._dataset.CombinationSegmentReferenceSequence.append(item.to_dataset())
