from decimal import Decimal
from typing import Any, List, Optional  # noqa

import pydicom


class PlanePositionSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ImagePositionPatient(self) -> Optional[List[Decimal]]:
        if "ImagePositionPatient" in self._dataset:
            return self._dataset.ImagePositionPatient
        return None

    @ImagePositionPatient.setter
    def ImagePositionPatient(self, value: Optional[List[Decimal]]):
        if value is None:
            if "ImagePositionPatient" in self._dataset:
                del self._dataset.ImagePositionPatient
        else:
            self._dataset.ImagePositionPatient = value
