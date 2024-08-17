from decimal import Decimal
from typing import Any, List, Optional  # noqa

import pydicom


class PlaneOrientationSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ImageOrientationPatient(self) -> Optional[List[Decimal]]:
        if "ImageOrientationPatient" in self._dataset:
            return self._dataset.ImageOrientationPatient
        return None

    @ImageOrientationPatient.setter
    def ImageOrientationPatient(self, value: Optional[List[Decimal]]):
        if value is None:
            if "ImageOrientationPatient" in self._dataset:
                del self._dataset.ImageOrientationPatient
        else:
            self._dataset.ImageOrientationPatient = value
