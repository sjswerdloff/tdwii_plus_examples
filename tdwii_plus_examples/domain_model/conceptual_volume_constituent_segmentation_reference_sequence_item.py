from typing import Any, List, Optional  # noqa

import pydicom

from .referenced_direct_segment_instance_sequence_item import (
    ReferencedDirectSegmentInstanceSequenceItem,
)


class ConceptualVolumeConstituentSegmentationReferenceSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._ReferencedDirectSegmentInstanceSequence: List[ReferencedDirectSegmentInstanceSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ReferencedSegmentReferenceIndex(self) -> Optional[int]:
        if "ReferencedSegmentReferenceIndex" in self._dataset:
            return self._dataset.ReferencedSegmentReferenceIndex
        return None

    @ReferencedSegmentReferenceIndex.setter
    def ReferencedSegmentReferenceIndex(self, value: Optional[int]):
        if value is None:
            if "ReferencedSegmentReferenceIndex" in self._dataset:
                del self._dataset.ReferencedSegmentReferenceIndex
        else:
            self._dataset.ReferencedSegmentReferenceIndex = value

    @property
    def ReferencedDirectSegmentInstanceSequence(self) -> Optional[List[ReferencedDirectSegmentInstanceSequenceItem]]:
        if "ReferencedDirectSegmentInstanceSequence" in self._dataset:
            if len(self._ReferencedDirectSegmentInstanceSequence) == len(
                self._dataset.ReferencedDirectSegmentInstanceSequence
            ):
                return self._ReferencedDirectSegmentInstanceSequence
            else:
                return [
                    ReferencedDirectSegmentInstanceSequenceItem(x)
                    for x in self._dataset.ReferencedDirectSegmentInstanceSequence
                ]
        return None

    @ReferencedDirectSegmentInstanceSequence.setter
    def ReferencedDirectSegmentInstanceSequence(self, value: Optional[List[ReferencedDirectSegmentInstanceSequenceItem]]):
        if value is None:
            self._ReferencedDirectSegmentInstanceSequence = []
            if "ReferencedDirectSegmentInstanceSequence" in self._dataset:
                del self._dataset.ReferencedDirectSegmentInstanceSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, ReferencedDirectSegmentInstanceSequenceItem) for item in value
        ):
            raise ValueError(
                "ReferencedDirectSegmentInstanceSequence must be a list of ReferencedDirectSegmentInstanceSequenceItem objects"
            )
        else:
            self._ReferencedDirectSegmentInstanceSequence = value
            if "ReferencedDirectSegmentInstanceSequence" not in self._dataset:
                self._dataset.ReferencedDirectSegmentInstanceSequence = pydicom.Sequence()
            self._dataset.ReferencedDirectSegmentInstanceSequence.clear()
            self._dataset.ReferencedDirectSegmentInstanceSequence.extend([item.to_dataset() for item in value])

    def add_ReferencedDirectSegmentInstance(self, item: ReferencedDirectSegmentInstanceSequenceItem):
        if not isinstance(item, ReferencedDirectSegmentInstanceSequenceItem):
            raise ValueError("Item must be an instance of ReferencedDirectSegmentInstanceSequenceItem")
        self._ReferencedDirectSegmentInstanceSequence.append(item)
        if "ReferencedDirectSegmentInstanceSequence" not in self._dataset:
            self._dataset.ReferencedDirectSegmentInstanceSequence = pydicom.Sequence()
        self._dataset.ReferencedDirectSegmentInstanceSequence.append(item.to_dataset())
