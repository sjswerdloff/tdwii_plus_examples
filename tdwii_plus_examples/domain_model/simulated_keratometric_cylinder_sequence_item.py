from typing import Any, List, Optional

import pydicom


class SimulatedKeratometricCylinderSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

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
