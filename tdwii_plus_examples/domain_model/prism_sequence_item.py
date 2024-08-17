from typing import Any, List, Optional

import pydicom


class PrismSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def VertexDistance(self) -> Optional[float]:
        if "VertexDistance" in self._dataset:
            return self._dataset.VertexDistance
        return None

    @VertexDistance.setter
    def VertexDistance(self, value: Optional[float]):
        if value is None:
            if "VertexDistance" in self._dataset:
                del self._dataset.VertexDistance
        else:
            self._dataset.VertexDistance = value

    @property
    def HorizontalPrismPower(self) -> Optional[float]:
        if "HorizontalPrismPower" in self._dataset:
            return self._dataset.HorizontalPrismPower
        return None

    @HorizontalPrismPower.setter
    def HorizontalPrismPower(self, value: Optional[float]):
        if value is None:
            if "HorizontalPrismPower" in self._dataset:
                del self._dataset.HorizontalPrismPower
        else:
            self._dataset.HorizontalPrismPower = value

    @property
    def HorizontalPrismBase(self) -> Optional[str]:
        if "HorizontalPrismBase" in self._dataset:
            return self._dataset.HorizontalPrismBase
        return None

    @HorizontalPrismBase.setter
    def HorizontalPrismBase(self, value: Optional[str]):
        if value is None:
            if "HorizontalPrismBase" in self._dataset:
                del self._dataset.HorizontalPrismBase
        else:
            self._dataset.HorizontalPrismBase = value

    @property
    def VerticalPrismPower(self) -> Optional[float]:
        if "VerticalPrismPower" in self._dataset:
            return self._dataset.VerticalPrismPower
        return None

    @VerticalPrismPower.setter
    def VerticalPrismPower(self, value: Optional[float]):
        if value is None:
            if "VerticalPrismPower" in self._dataset:
                del self._dataset.VerticalPrismPower
        else:
            self._dataset.VerticalPrismPower = value

    @property
    def VerticalPrismBase(self) -> Optional[str]:
        if "VerticalPrismBase" in self._dataset:
            return self._dataset.VerticalPrismBase
        return None

    @VerticalPrismBase.setter
    def VerticalPrismBase(self, value: Optional[str]):
        if value is None:
            if "VerticalPrismBase" in self._dataset:
                del self._dataset.VerticalPrismBase
        else:
            self._dataset.VerticalPrismBase = value
