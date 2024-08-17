from typing import Any, List, Optional

import pydicom


class MeasurementValuesSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def FloatingPointValues(self) -> Optional[bytes]:
        if "FloatingPointValues" in self._dataset:
            return self._dataset.FloatingPointValues
        return None

    @FloatingPointValues.setter
    def FloatingPointValues(self, value: Optional[bytes]):
        if value is None:
            if "FloatingPointValues" in self._dataset:
                del self._dataset.FloatingPointValues
        else:
            self._dataset.FloatingPointValues = value

    @property
    def TrackPointIndexList(self) -> Optional[bytes]:
        if "TrackPointIndexList" in self._dataset:
            return self._dataset.TrackPointIndexList
        return None

    @TrackPointIndexList.setter
    def TrackPointIndexList(self, value: Optional[bytes]):
        if value is None:
            if "TrackPointIndexList" in self._dataset:
                del self._dataset.TrackPointIndexList
        else:
            self._dataset.TrackPointIndexList = value
