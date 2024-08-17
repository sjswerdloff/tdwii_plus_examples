from decimal import Decimal
from typing import Any, List, Optional  # noqa

import pydicom


class XRayFilterSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def FilterType(self) -> Optional[str]:
        if "FilterType" in self._dataset:
            return self._dataset.FilterType
        return None

    @FilterType.setter
    def FilterType(self, value: Optional[str]):
        if value is None:
            if "FilterType" in self._dataset:
                del self._dataset.FilterType
        else:
            self._dataset.FilterType = value

    @property
    def FilterMaterial(self) -> Optional[List[str]]:
        if "FilterMaterial" in self._dataset:
            return self._dataset.FilterMaterial
        return None

    @FilterMaterial.setter
    def FilterMaterial(self, value: Optional[List[str]]):
        if value is None:
            if "FilterMaterial" in self._dataset:
                del self._dataset.FilterMaterial
        else:
            self._dataset.FilterMaterial = value

    @property
    def FilterThicknessMinimum(self) -> Optional[List[Decimal]]:
        if "FilterThicknessMinimum" in self._dataset:
            return self._dataset.FilterThicknessMinimum
        return None

    @FilterThicknessMinimum.setter
    def FilterThicknessMinimum(self, value: Optional[List[Decimal]]):
        if value is None:
            if "FilterThicknessMinimum" in self._dataset:
                del self._dataset.FilterThicknessMinimum
        else:
            self._dataset.FilterThicknessMinimum = value

    @property
    def FilterThicknessMaximum(self) -> Optional[List[Decimal]]:
        if "FilterThicknessMaximum" in self._dataset:
            return self._dataset.FilterThicknessMaximum
        return None

    @FilterThicknessMaximum.setter
    def FilterThicknessMaximum(self, value: Optional[List[Decimal]]):
        if value is None:
            if "FilterThicknessMaximum" in self._dataset:
                del self._dataset.FilterThicknessMaximum
        else:
            self._dataset.FilterThicknessMaximum = value

    @property
    def FilterBeamPathLengthMinimum(self) -> Optional[List[float]]:
        if "FilterBeamPathLengthMinimum" in self._dataset:
            return self._dataset.FilterBeamPathLengthMinimum
        return None

    @FilterBeamPathLengthMinimum.setter
    def FilterBeamPathLengthMinimum(self, value: Optional[List[float]]):
        if value is None:
            if "FilterBeamPathLengthMinimum" in self._dataset:
                del self._dataset.FilterBeamPathLengthMinimum
        else:
            self._dataset.FilterBeamPathLengthMinimum = value

    @property
    def FilterBeamPathLengthMaximum(self) -> Optional[List[float]]:
        if "FilterBeamPathLengthMaximum" in self._dataset:
            return self._dataset.FilterBeamPathLengthMaximum
        return None

    @FilterBeamPathLengthMaximum.setter
    def FilterBeamPathLengthMaximum(self, value: Optional[List[float]]):
        if value is None:
            if "FilterBeamPathLengthMaximum" in self._dataset:
                del self._dataset.FilterBeamPathLengthMaximum
        else:
            self._dataset.FilterBeamPathLengthMaximum = value
