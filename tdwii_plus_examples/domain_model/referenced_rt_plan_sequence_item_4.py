from typing import Any, List, Optional

import pydicom

from .referenced_fraction_group_sequence_item import ReferencedFractionGroupSequenceItem


class ReferencedRTPlanSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._ReferencedFractionGroupSequence: List[ReferencedFractionGroupSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ReferencedSOPClassUID(self) -> Optional[str]:
        if "ReferencedSOPClassUID" in self._dataset:
            return self._dataset.ReferencedSOPClassUID
        return None

    @ReferencedSOPClassUID.setter
    def ReferencedSOPClassUID(self, value: Optional[str]):
        if value is None:
            if "ReferencedSOPClassUID" in self._dataset:
                del self._dataset.ReferencedSOPClassUID
        else:
            self._dataset.ReferencedSOPClassUID = value

    @property
    def ReferencedSOPInstanceUID(self) -> Optional[str]:
        if "ReferencedSOPInstanceUID" in self._dataset:
            return self._dataset.ReferencedSOPInstanceUID
        return None

    @ReferencedSOPInstanceUID.setter
    def ReferencedSOPInstanceUID(self, value: Optional[str]):
        if value is None:
            if "ReferencedSOPInstanceUID" in self._dataset:
                del self._dataset.ReferencedSOPInstanceUID
        else:
            self._dataset.ReferencedSOPInstanceUID = value

    @property
    def ReferencedFractionGroupSequence(self) -> Optional[List[ReferencedFractionGroupSequenceItem]]:
        if "ReferencedFractionGroupSequence" in self._dataset:
            if len(self._ReferencedFractionGroupSequence) == len(self._dataset.ReferencedFractionGroupSequence):
                return self._ReferencedFractionGroupSequence
            else:
                return [ReferencedFractionGroupSequenceItem(x) for x in self._dataset.ReferencedFractionGroupSequence]
        return None

    @ReferencedFractionGroupSequence.setter
    def ReferencedFractionGroupSequence(self, value: Optional[List[ReferencedFractionGroupSequenceItem]]):
        if value is None:
            self._ReferencedFractionGroupSequence = []
            if "ReferencedFractionGroupSequence" in self._dataset:
                del self._dataset.ReferencedFractionGroupSequence
        elif not isinstance(value, list) or not all(isinstance(item, ReferencedFractionGroupSequenceItem) for item in value):
            raise ValueError(f"ReferencedFractionGroupSequence must be a list of ReferencedFractionGroupSequenceItem objects")
        else:
            self._ReferencedFractionGroupSequence = value
            if "ReferencedFractionGroupSequence" not in self._dataset:
                self._dataset.ReferencedFractionGroupSequence = pydicom.Sequence()
            self._dataset.ReferencedFractionGroupSequence.clear()
            self._dataset.ReferencedFractionGroupSequence.extend([item.to_dataset() for item in value])

    def add_ReferencedFractionGroup(self, item: ReferencedFractionGroupSequenceItem):
        if not isinstance(item, ReferencedFractionGroupSequenceItem):
            raise ValueError(f"Item must be an instance of ReferencedFractionGroupSequenceItem")
        self._ReferencedFractionGroupSequence.append(item)
        if "ReferencedFractionGroupSequence" not in self._dataset:
            self._dataset.ReferencedFractionGroupSequence = pydicom.Sequence()
        self._dataset.ReferencedFractionGroupSequence.append(item.to_dataset())

    @property
    def ReferencedPlanOverviewIndex(self) -> Optional[int]:
        if "ReferencedPlanOverviewIndex" in self._dataset:
            return self._dataset.ReferencedPlanOverviewIndex
        return None

    @ReferencedPlanOverviewIndex.setter
    def ReferencedPlanOverviewIndex(self, value: Optional[int]):
        if value is None:
            if "ReferencedPlanOverviewIndex" in self._dataset:
                del self._dataset.ReferencedPlanOverviewIndex
        else:
            self._dataset.ReferencedPlanOverviewIndex = value
