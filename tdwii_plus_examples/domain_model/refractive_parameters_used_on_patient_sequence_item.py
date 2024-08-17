from typing import Any, List, Optional  # noqa

import pydicom


class RefractiveParametersUsedOnPatientSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def SphericalLensPower(self) -> Optional[float]:
        if "SphericalLensPower" in self._dataset:
            return self._dataset.SphericalLensPower
        return None

    @SphericalLensPower.setter
    def SphericalLensPower(self, value: Optional[float]):
        if value is None:
            if "SphericalLensPower" in self._dataset:
                del self._dataset.SphericalLensPower
        else:
            self._dataset.SphericalLensPower = value

    @property
    def CylinderLensPower(self) -> Optional[float]:
        if "CylinderLensPower" in self._dataset:
            return self._dataset.CylinderLensPower
        return None

    @CylinderLensPower.setter
    def CylinderLensPower(self, value: Optional[float]):
        if value is None:
            if "CylinderLensPower" in self._dataset:
                del self._dataset.CylinderLensPower
        else:
            self._dataset.CylinderLensPower = value

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
