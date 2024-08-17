from typing import Any, List, Optional

import pydicom


class AddNearSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def AddPower(self) -> Optional[float]:
        if "AddPower" in self._dataset:
            return self._dataset.AddPower
        return None

    @AddPower.setter
    def AddPower(self, value: Optional[float]):
        if value is None:
            if "AddPower" in self._dataset:
                del self._dataset.AddPower
        else:
            self._dataset.AddPower = value

    @property
    def ViewingDistance(self) -> Optional[float]:
        if "ViewingDistance" in self._dataset:
            return self._dataset.ViewingDistance
        return None

    @ViewingDistance.setter
    def ViewingDistance(self, value: Optional[float]):
        if value is None:
            if "ViewingDistance" in self._dataset:
                del self._dataset.ViewingDistance
        else:
            self._dataset.ViewingDistance = value
