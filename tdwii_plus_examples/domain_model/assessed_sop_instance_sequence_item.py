from typing import Any, List, Optional  # noqa

import pydicom

from .referenced_comparison_sop_instance_sequence_item import (
    ReferencedComparisonSOPInstanceSequenceItem,
)


class AssessedSOPInstanceSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._ReferencedComparisonSOPInstanceSequence: List[ReferencedComparisonSOPInstanceSequenceItem] = []

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
    def ReferencedComparisonSOPInstanceSequence(self) -> Optional[List[ReferencedComparisonSOPInstanceSequenceItem]]:
        if "ReferencedComparisonSOPInstanceSequence" in self._dataset:
            if len(self._ReferencedComparisonSOPInstanceSequence) == len(
                self._dataset.ReferencedComparisonSOPInstanceSequence
            ):
                return self._ReferencedComparisonSOPInstanceSequence
            else:
                return [
                    ReferencedComparisonSOPInstanceSequenceItem(x)
                    for x in self._dataset.ReferencedComparisonSOPInstanceSequence
                ]
        return None

    @ReferencedComparisonSOPInstanceSequence.setter
    def ReferencedComparisonSOPInstanceSequence(self, value: Optional[List[ReferencedComparisonSOPInstanceSequenceItem]]):
        if value is None:
            self._ReferencedComparisonSOPInstanceSequence = []
            if "ReferencedComparisonSOPInstanceSequence" in self._dataset:
                del self._dataset.ReferencedComparisonSOPInstanceSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, ReferencedComparisonSOPInstanceSequenceItem) for item in value
        ):
            raise ValueError(
                "ReferencedComparisonSOPInstanceSequence must be a list of ReferencedComparisonSOPInstanceSequenceItem objects"
            )
        else:
            self._ReferencedComparisonSOPInstanceSequence = value
            if "ReferencedComparisonSOPInstanceSequence" not in self._dataset:
                self._dataset.ReferencedComparisonSOPInstanceSequence = pydicom.Sequence()
            self._dataset.ReferencedComparisonSOPInstanceSequence.clear()
            self._dataset.ReferencedComparisonSOPInstanceSequence.extend([item.to_dataset() for item in value])

    def add_ReferencedComparisonSOPInstance(self, item: ReferencedComparisonSOPInstanceSequenceItem):
        if not isinstance(item, ReferencedComparisonSOPInstanceSequenceItem):
            raise ValueError("Item must be an instance of ReferencedComparisonSOPInstanceSequenceItem")
        self._ReferencedComparisonSOPInstanceSequence.append(item)
        if "ReferencedComparisonSOPInstanceSequence" not in self._dataset:
            self._dataset.ReferencedComparisonSOPInstanceSequence = pydicom.Sequence()
        self._dataset.ReferencedComparisonSOPInstanceSequence.append(item.to_dataset())
