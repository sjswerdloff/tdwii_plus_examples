from typing import Any, List, Optional

import pydicom


class BlendingDisplayInputSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def BlendingInputNumber(self) -> Optional[int]:
        if "BlendingInputNumber" in self._dataset:
            return self._dataset.BlendingInputNumber
        return None

    @BlendingInputNumber.setter
    def BlendingInputNumber(self, value: Optional[int]):
        if value is None:
            if "BlendingInputNumber" in self._dataset:
                del self._dataset.BlendingInputNumber
        else:
            self._dataset.BlendingInputNumber = value
