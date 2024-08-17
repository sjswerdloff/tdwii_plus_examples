from typing import Any, List, Optional

import pydicom

from .referenced_series_sequence_item import ReferencedSeriesSequenceItem


class ReferencedRTPlanSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._ReferencedSeriesSequence: List[ReferencedSeriesSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

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
