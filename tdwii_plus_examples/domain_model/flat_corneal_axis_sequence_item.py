from typing import Any, List, Optional  # noqa

import pydicom


class FlatCornealAxisSequenceItem:
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
    def CornealPower(self) -> Optional[float]:
        if "CornealPower" in self._dataset:
            return self._dataset.CornealPower
        return None

    @CornealPower.setter
    def CornealPower(self, value: Optional[float]):
        if value is None:
            if "CornealPower" in self._dataset:
                del self._dataset.CornealPower
        else:
            self._dataset.CornealPower = value

    @property
    def CornealAxis(self) -> Optional[float]:
        if "CornealAxis" in self._dataset:
            return self._dataset.CornealAxis
        return None

    @CornealAxis.setter
    def CornealAxis(self, value: Optional[float]):
        if value is None:
            if "CornealAxis" in self._dataset:
                del self._dataset.CornealAxis
        else:
            self._dataset.CornealAxis = value
