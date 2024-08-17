from typing import Any, List, Optional

import pydicom


class ObliqueCroppingPlaneSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def Plane(self) -> Optional[List[float]]:
        if "Plane" in self._dataset:
            return self._dataset.Plane
        return None

    @Plane.setter
    def Plane(self, value: Optional[List[float]]):
        if value is None:
            if "Plane" in self._dataset:
                del self._dataset.Plane
        else:
            self._dataset.Plane = value

    @property
    def PlaneNormal(self) -> Optional[List[float]]:
        if "PlaneNormal" in self._dataset:
            return self._dataset.PlaneNormal
        return None

    @PlaneNormal.setter
    def PlaneNormal(self, value: Optional[List[float]]):
        if value is None:
            if "PlaneNormal" in self._dataset:
                del self._dataset.PlaneNormal
        else:
            self._dataset.PlaneNormal = value
