from typing import Any, List, Optional  # noqa

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
    def AnnotationIndexList(self) -> Optional[bytes]:
        if "AnnotationIndexList" in self._dataset:
            return self._dataset.AnnotationIndexList
        return None

    @AnnotationIndexList.setter
    def AnnotationIndexList(self, value: Optional[bytes]):
        if value is None:
            if "AnnotationIndexList" in self._dataset:
                del self._dataset.AnnotationIndexList
        else:
            self._dataset.AnnotationIndexList = value
