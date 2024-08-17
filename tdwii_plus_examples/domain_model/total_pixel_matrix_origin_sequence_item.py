from decimal import Decimal
from typing import Any, List, Optional  # noqa

import pydicom


class TotalPixelMatrixOriginSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def XOffsetInSlideCoordinateSystem(self) -> Optional[Decimal]:
        if "XOffsetInSlideCoordinateSystem" in self._dataset:
            return self._dataset.XOffsetInSlideCoordinateSystem
        return None

    @XOffsetInSlideCoordinateSystem.setter
    def XOffsetInSlideCoordinateSystem(self, value: Optional[Decimal]):
        if value is None:
            if "XOffsetInSlideCoordinateSystem" in self._dataset:
                del self._dataset.XOffsetInSlideCoordinateSystem
        else:
            self._dataset.XOffsetInSlideCoordinateSystem = value

    @property
    def YOffsetInSlideCoordinateSystem(self) -> Optional[Decimal]:
        if "YOffsetInSlideCoordinateSystem" in self._dataset:
            return self._dataset.YOffsetInSlideCoordinateSystem
        return None

    @YOffsetInSlideCoordinateSystem.setter
    def YOffsetInSlideCoordinateSystem(self, value: Optional[Decimal]):
        if value is None:
            if "YOffsetInSlideCoordinateSystem" in self._dataset:
                del self._dataset.YOffsetInSlideCoordinateSystem
        else:
            self._dataset.YOffsetInSlideCoordinateSystem = value

    @property
    def ZOffsetInSlideCoordinateSystem(self) -> Optional[Decimal]:
        if "ZOffsetInSlideCoordinateSystem" in self._dataset:
            return self._dataset.ZOffsetInSlideCoordinateSystem
        return None

    @ZOffsetInSlideCoordinateSystem.setter
    def ZOffsetInSlideCoordinateSystem(self, value: Optional[Decimal]):
        if value is None:
            if "ZOffsetInSlideCoordinateSystem" in self._dataset:
                del self._dataset.ZOffsetInSlideCoordinateSystem
        else:
            self._dataset.ZOffsetInSlideCoordinateSystem = value
