from typing import Any, List, Optional  # noqa

import pydicom

from .rt_referenced_series_sequence_item import RTReferencedSeriesSequenceItem


class RTReferencedStudySequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._RTReferencedSeriesSequence: List[RTReferencedSeriesSequenceItem] = []

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
    def RTReferencedSeriesSequence(self) -> Optional[List[RTReferencedSeriesSequenceItem]]:
        if "RTReferencedSeriesSequence" in self._dataset:
            if len(self._RTReferencedSeriesSequence) == len(self._dataset.RTReferencedSeriesSequence):
                return self._RTReferencedSeriesSequence
            else:
                return [RTReferencedSeriesSequenceItem(x) for x in self._dataset.RTReferencedSeriesSequence]
        return None

    @RTReferencedSeriesSequence.setter
    def RTReferencedSeriesSequence(self, value: Optional[List[RTReferencedSeriesSequenceItem]]):
        if value is None:
            self._RTReferencedSeriesSequence = []
            if "RTReferencedSeriesSequence" in self._dataset:
                del self._dataset.RTReferencedSeriesSequence
        elif not isinstance(value, list) or not all(isinstance(item, RTReferencedSeriesSequenceItem) for item in value):
            raise ValueError("RTReferencedSeriesSequence must be a list of RTReferencedSeriesSequenceItem objects")
        else:
            self._RTReferencedSeriesSequence = value
            if "RTReferencedSeriesSequence" not in self._dataset:
                self._dataset.RTReferencedSeriesSequence = pydicom.Sequence()
            self._dataset.RTReferencedSeriesSequence.clear()
            self._dataset.RTReferencedSeriesSequence.extend([item.to_dataset() for item in value])

    def add_RTReferencedSeries(self, item: RTReferencedSeriesSequenceItem):
        if not isinstance(item, RTReferencedSeriesSequenceItem):
            raise ValueError("Item must be an instance of RTReferencedSeriesSequenceItem")
        self._RTReferencedSeriesSequence.append(item)
        if "RTReferencedSeriesSequence" not in self._dataset:
            self._dataset.RTReferencedSeriesSequence = pydicom.Sequence()
        self._dataset.RTReferencedSeriesSequence.append(item.to_dataset())
