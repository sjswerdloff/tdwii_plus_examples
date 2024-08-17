from typing import Any, List, Optional  # noqa

import pydicom

from .data_observation_sequence_item import DataObservationSequenceItem
from .index_probability_sequence_item import IndexProbabilitySequenceItem


class VisualFieldGlobalResultsIndexSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._DataObservationSequence: List[DataObservationSequenceItem] = []
        self._IndexProbabilitySequence: List[IndexProbabilitySequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def DataObservationSequence(self) -> Optional[List[DataObservationSequenceItem]]:
        if "DataObservationSequence" in self._dataset:
            if len(self._DataObservationSequence) == len(self._dataset.DataObservationSequence):
                return self._DataObservationSequence
            else:
                return [DataObservationSequenceItem(x) for x in self._dataset.DataObservationSequence]
        return None

    @DataObservationSequence.setter
    def DataObservationSequence(self, value: Optional[List[DataObservationSequenceItem]]):
        if value is None:
            self._DataObservationSequence = []
            if "DataObservationSequence" in self._dataset:
                del self._dataset.DataObservationSequence
        elif not isinstance(value, list) or not all(isinstance(item, DataObservationSequenceItem) for item in value):
            raise ValueError("DataObservationSequence must be a list of DataObservationSequenceItem objects")
        else:
            self._DataObservationSequence = value
            if "DataObservationSequence" not in self._dataset:
                self._dataset.DataObservationSequence = pydicom.Sequence()
            self._dataset.DataObservationSequence.clear()
            self._dataset.DataObservationSequence.extend([item.to_dataset() for item in value])

    def add_DataObservation(self, item: DataObservationSequenceItem):
        if not isinstance(item, DataObservationSequenceItem):
            raise ValueError("Item must be an instance of DataObservationSequenceItem")
        self._DataObservationSequence.append(item)
        if "DataObservationSequence" not in self._dataset:
            self._dataset.DataObservationSequence = pydicom.Sequence()
        self._dataset.DataObservationSequence.append(item.to_dataset())

    @property
    def IndexNormalsFlag(self) -> Optional[str]:
        if "IndexNormalsFlag" in self._dataset:
            return self._dataset.IndexNormalsFlag
        return None

    @IndexNormalsFlag.setter
    def IndexNormalsFlag(self, value: Optional[str]):
        if value is None:
            if "IndexNormalsFlag" in self._dataset:
                del self._dataset.IndexNormalsFlag
        else:
            self._dataset.IndexNormalsFlag = value

    @property
    def IndexProbabilitySequence(self) -> Optional[List[IndexProbabilitySequenceItem]]:
        if "IndexProbabilitySequence" in self._dataset:
            if len(self._IndexProbabilitySequence) == len(self._dataset.IndexProbabilitySequence):
                return self._IndexProbabilitySequence
            else:
                return [IndexProbabilitySequenceItem(x) for x in self._dataset.IndexProbabilitySequence]
        return None

    @IndexProbabilitySequence.setter
    def IndexProbabilitySequence(self, value: Optional[List[IndexProbabilitySequenceItem]]):
        if value is None:
            self._IndexProbabilitySequence = []
            if "IndexProbabilitySequence" in self._dataset:
                del self._dataset.IndexProbabilitySequence
        elif not isinstance(value, list) or not all(isinstance(item, IndexProbabilitySequenceItem) for item in value):
            raise ValueError("IndexProbabilitySequence must be a list of IndexProbabilitySequenceItem objects")
        else:
            self._IndexProbabilitySequence = value
            if "IndexProbabilitySequence" not in self._dataset:
                self._dataset.IndexProbabilitySequence = pydicom.Sequence()
            self._dataset.IndexProbabilitySequence.clear()
            self._dataset.IndexProbabilitySequence.extend([item.to_dataset() for item in value])

    def add_IndexProbability(self, item: IndexProbabilitySequenceItem):
        if not isinstance(item, IndexProbabilitySequenceItem):
            raise ValueError("Item must be an instance of IndexProbabilitySequenceItem")
        self._IndexProbabilitySequence.append(item)
        if "IndexProbabilitySequence" not in self._dataset:
            self._dataset.IndexProbabilitySequence = pydicom.Sequence()
        self._dataset.IndexProbabilitySequence.append(item.to_dataset())
