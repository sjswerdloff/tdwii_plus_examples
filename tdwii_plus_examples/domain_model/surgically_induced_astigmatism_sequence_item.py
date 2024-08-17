from typing import Any, List, Optional  # noqa

import pydicom


class SurgicallyInducedAstigmatismSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def CylinderAxis(self) -> Optional[float]:
        if "CylinderAxis" in self._dataset:
            return self._dataset.CylinderAxis
        return None

    @CylinderAxis.setter
    def CylinderAxis(self, value: Optional[float]):
        if value is None:
            if "CylinderAxis" in self._dataset:
                del self._dataset.CylinderAxis
        else:
            self._dataset.CylinderAxis = value

    @property
    def CylinderPower(self) -> Optional[float]:
        if "CylinderPower" in self._dataset:
            return self._dataset.CylinderPower
        return None

    @CylinderPower.setter
    def CylinderPower(self, value: Optional[float]):
        if value is None:
            if "CylinderPower" in self._dataset:
                del self._dataset.CylinderPower
        else:
            self._dataset.CylinderPower = value
