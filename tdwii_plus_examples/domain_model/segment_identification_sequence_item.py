from typing import Any, List, Optional

import pydicom


class SegmentIdentificationSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ReferencedSegmentNumber(self) -> Optional[List[int]]:
        if "ReferencedSegmentNumber" in self._dataset:
            return self._dataset.ReferencedSegmentNumber
        return None

    @ReferencedSegmentNumber.setter
    def ReferencedSegmentNumber(self, value: Optional[List[int]]):
        if value is None:
            if "ReferencedSegmentNumber" in self._dataset:
                del self._dataset.ReferencedSegmentNumber
        else:
            self._dataset.ReferencedSegmentNumber = value
