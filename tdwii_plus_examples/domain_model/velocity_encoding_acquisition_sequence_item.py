from typing import Any, List, Optional

import pydicom


class VelocityEncodingAcquisitionSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def VelocityEncodingDirection(self) -> Optional[List[float]]:
        if "VelocityEncodingDirection" in self._dataset:
            return self._dataset.VelocityEncodingDirection
        return None

    @VelocityEncodingDirection.setter
    def VelocityEncodingDirection(self, value: Optional[List[float]]):
        if value is None:
            if "VelocityEncodingDirection" in self._dataset:
                del self._dataset.VelocityEncodingDirection
        else:
            self._dataset.VelocityEncodingDirection = value
