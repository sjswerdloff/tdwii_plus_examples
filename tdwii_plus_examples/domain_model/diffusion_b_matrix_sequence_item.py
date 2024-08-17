from typing import Any, List, Optional  # noqa

import pydicom


class DiffusionBMatrixSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def DiffusionBValueXX(self) -> Optional[float]:
        if "DiffusionBValueXX" in self._dataset:
            return self._dataset.DiffusionBValueXX
        return None

    @DiffusionBValueXX.setter
    def DiffusionBValueXX(self, value: Optional[float]):
        if value is None:
            if "DiffusionBValueXX" in self._dataset:
                del self._dataset.DiffusionBValueXX
        else:
            self._dataset.DiffusionBValueXX = value

    @property
    def DiffusionBValueXY(self) -> Optional[float]:
        if "DiffusionBValueXY" in self._dataset:
            return self._dataset.DiffusionBValueXY
        return None

    @DiffusionBValueXY.setter
    def DiffusionBValueXY(self, value: Optional[float]):
        if value is None:
            if "DiffusionBValueXY" in self._dataset:
                del self._dataset.DiffusionBValueXY
        else:
            self._dataset.DiffusionBValueXY = value

    @property
    def DiffusionBValueXZ(self) -> Optional[float]:
        if "DiffusionBValueXZ" in self._dataset:
            return self._dataset.DiffusionBValueXZ
        return None

    @DiffusionBValueXZ.setter
    def DiffusionBValueXZ(self, value: Optional[float]):
        if value is None:
            if "DiffusionBValueXZ" in self._dataset:
                del self._dataset.DiffusionBValueXZ
        else:
            self._dataset.DiffusionBValueXZ = value

    @property
    def DiffusionBValueYY(self) -> Optional[float]:
        if "DiffusionBValueYY" in self._dataset:
            return self._dataset.DiffusionBValueYY
        return None

    @DiffusionBValueYY.setter
    def DiffusionBValueYY(self, value: Optional[float]):
        if value is None:
            if "DiffusionBValueYY" in self._dataset:
                del self._dataset.DiffusionBValueYY
        else:
            self._dataset.DiffusionBValueYY = value

    @property
    def DiffusionBValueYZ(self) -> Optional[float]:
        if "DiffusionBValueYZ" in self._dataset:
            return self._dataset.DiffusionBValueYZ
        return None

    @DiffusionBValueYZ.setter
    def DiffusionBValueYZ(self, value: Optional[float]):
        if value is None:
            if "DiffusionBValueYZ" in self._dataset:
                del self._dataset.DiffusionBValueYZ
        else:
            self._dataset.DiffusionBValueYZ = value

    @property
    def DiffusionBValueZZ(self) -> Optional[float]:
        if "DiffusionBValueZZ" in self._dataset:
            return self._dataset.DiffusionBValueZZ
        return None

    @DiffusionBValueZZ.setter
    def DiffusionBValueZZ(self, value: Optional[float]):
        if value is None:
            if "DiffusionBValueZZ" in self._dataset:
                del self._dataset.DiffusionBValueZZ
        else:
            self._dataset.DiffusionBValueZZ = value
