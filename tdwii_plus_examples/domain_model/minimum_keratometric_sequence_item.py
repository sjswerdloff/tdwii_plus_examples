from typing import Any, List, Optional  # noqa

import pydicom


class MinimumKeratometricSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def RadiusOfCurvature(self) -> Optional[float]:
        if "RadiusOfCurvature" in self._dataset:
            return self._dataset.RadiusOfCurvature
        return None

    @RadiusOfCurvature.setter
    def RadiusOfCurvature(self, value: Optional[float]):
        if value is None:
            if "RadiusOfCurvature" in self._dataset:
                del self._dataset.RadiusOfCurvature
        else:
            self._dataset.RadiusOfCurvature = value

    @property
    def KeratometricPower(self) -> Optional[float]:
        if "KeratometricPower" in self._dataset:
            return self._dataset.KeratometricPower
        return None

    @KeratometricPower.setter
    def KeratometricPower(self, value: Optional[float]):
        if value is None:
            if "KeratometricPower" in self._dataset:
                del self._dataset.KeratometricPower
        else:
            self._dataset.KeratometricPower = value

    @property
    def KeratometricAxis(self) -> Optional[float]:
        if "KeratometricAxis" in self._dataset:
            return self._dataset.KeratometricAxis
        return None

    @KeratometricAxis.setter
    def KeratometricAxis(self, value: Optional[float]):
        if value is None:
            if "KeratometricAxis" in self._dataset:
                del self._dataset.KeratometricAxis
        else:
            self._dataset.KeratometricAxis = value
