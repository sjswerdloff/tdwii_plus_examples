from typing import Any, List, Optional

import pydicom


class ReferencedControlPointSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ReferencedStartControlPointIndex(self) -> Optional[int]:
        if "ReferencedStartControlPointIndex" in self._dataset:
            return self._dataset.ReferencedStartControlPointIndex
        return None

    @ReferencedStartControlPointIndex.setter
    def ReferencedStartControlPointIndex(self, value: Optional[int]):
        if value is None:
            if "ReferencedStartControlPointIndex" in self._dataset:
                del self._dataset.ReferencedStartControlPointIndex
        else:
            self._dataset.ReferencedStartControlPointIndex = value

    @property
    def ReferencedStopControlPointIndex(self) -> Optional[int]:
        if "ReferencedStopControlPointIndex" in self._dataset:
            return self._dataset.ReferencedStopControlPointIndex
        return None

    @ReferencedStopControlPointIndex.setter
    def ReferencedStopControlPointIndex(self, value: Optional[int]):
        if value is None:
            if "ReferencedStopControlPointIndex" in self._dataset:
                del self._dataset.ReferencedStopControlPointIndex
        else:
            self._dataset.ReferencedStopControlPointIndex = value
