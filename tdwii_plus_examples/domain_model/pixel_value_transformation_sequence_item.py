from decimal import Decimal
from typing import Any, List, Optional  # noqa

import pydicom


class PixelValueTransformationSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def RescaleIntercept(self) -> Optional[Decimal]:
        if "RescaleIntercept" in self._dataset:
            return self._dataset.RescaleIntercept
        return None

    @RescaleIntercept.setter
    def RescaleIntercept(self, value: Optional[Decimal]):
        if value is None:
            if "RescaleIntercept" in self._dataset:
                del self._dataset.RescaleIntercept
        else:
            self._dataset.RescaleIntercept = value

    @property
    def RescaleSlope(self) -> Optional[Decimal]:
        if "RescaleSlope" in self._dataset:
            return self._dataset.RescaleSlope
        return None

    @RescaleSlope.setter
    def RescaleSlope(self, value: Optional[Decimal]):
        if value is None:
            if "RescaleSlope" in self._dataset:
                del self._dataset.RescaleSlope
        else:
            self._dataset.RescaleSlope = value

    @property
    def RescaleType(self) -> Optional[str]:
        if "RescaleType" in self._dataset:
            return self._dataset.RescaleType
        return None

    @RescaleType.setter
    def RescaleType(self, value: Optional[str]):
        if value is None:
            if "RescaleType" in self._dataset:
                del self._dataset.RescaleType
        else:
            self._dataset.RescaleType = value
