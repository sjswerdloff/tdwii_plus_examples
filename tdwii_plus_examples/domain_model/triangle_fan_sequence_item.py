from typing import Any, List, Optional

import pydicom


class TriangleFanSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def LongPrimitivePointIndexList(self) -> Optional[bytes]:
        if "LongPrimitivePointIndexList" in self._dataset:
            return self._dataset.LongPrimitivePointIndexList
        return None

    @LongPrimitivePointIndexList.setter
    def LongPrimitivePointIndexList(self, value: Optional[bytes]):
        if value is None:
            if "LongPrimitivePointIndexList" in self._dataset:
                del self._dataset.LongPrimitivePointIndexList
        else:
            self._dataset.LongPrimitivePointIndexList = value
