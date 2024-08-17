from decimal import Decimal
from typing import Any, List, Optional

import pydicom


class FieldOfViewSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def FieldOfViewShape(self) -> Optional[str]:
        if "FieldOfViewShape" in self._dataset:
            return self._dataset.FieldOfViewShape
        return None

    @FieldOfViewShape.setter
    def FieldOfViewShape(self, value: Optional[str]):
        if value is None:
            if "FieldOfViewShape" in self._dataset:
                del self._dataset.FieldOfViewShape
        else:
            self._dataset.FieldOfViewShape = value

    @property
    def FieldOfViewOrigin(self) -> Optional[List[Decimal]]:
        if "FieldOfViewOrigin" in self._dataset:
            return self._dataset.FieldOfViewOrigin
        return None

    @FieldOfViewOrigin.setter
    def FieldOfViewOrigin(self, value: Optional[List[Decimal]]):
        if value is None:
            if "FieldOfViewOrigin" in self._dataset:
                del self._dataset.FieldOfViewOrigin
        else:
            self._dataset.FieldOfViewOrigin = value

    @property
    def FieldOfViewRotation(self) -> Optional[Decimal]:
        if "FieldOfViewRotation" in self._dataset:
            return self._dataset.FieldOfViewRotation
        return None

    @FieldOfViewRotation.setter
    def FieldOfViewRotation(self, value: Optional[Decimal]):
        if value is None:
            if "FieldOfViewRotation" in self._dataset:
                del self._dataset.FieldOfViewRotation
        else:
            self._dataset.FieldOfViewRotation = value

    @property
    def FieldOfViewHorizontalFlip(self) -> Optional[str]:
        if "FieldOfViewHorizontalFlip" in self._dataset:
            return self._dataset.FieldOfViewHorizontalFlip
        return None

    @FieldOfViewHorizontalFlip.setter
    def FieldOfViewHorizontalFlip(self, value: Optional[str]):
        if value is None:
            if "FieldOfViewHorizontalFlip" in self._dataset:
                del self._dataset.FieldOfViewHorizontalFlip
        else:
            self._dataset.FieldOfViewHorizontalFlip = value

    @property
    def FieldOfViewDescription(self) -> Optional[str]:
        if "FieldOfViewDescription" in self._dataset:
            return self._dataset.FieldOfViewDescription
        return None

    @FieldOfViewDescription.setter
    def FieldOfViewDescription(self, value: Optional[str]):
        if value is None:
            if "FieldOfViewDescription" in self._dataset:
                del self._dataset.FieldOfViewDescription
        else:
            self._dataset.FieldOfViewDescription = value

    @property
    def FieldOfViewDimensionsInFloat(self) -> Optional[List[float]]:
        if "FieldOfViewDimensionsInFloat" in self._dataset:
            return self._dataset.FieldOfViewDimensionsInFloat
        return None

    @FieldOfViewDimensionsInFloat.setter
    def FieldOfViewDimensionsInFloat(self, value: Optional[List[float]]):
        if value is None:
            if "FieldOfViewDimensionsInFloat" in self._dataset:
                del self._dataset.FieldOfViewDimensionsInFloat
        else:
            self._dataset.FieldOfViewDimensionsInFloat = value
