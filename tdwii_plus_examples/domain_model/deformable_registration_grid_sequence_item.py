from decimal import Decimal
from typing import Any, List, Optional  # noqa

import pydicom


class DeformableRegistrationGridSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ImagePositionPatient(self) -> Optional[List[Decimal]]:
        if "ImagePositionPatient" in self._dataset:
            return self._dataset.ImagePositionPatient
        return None

    @ImagePositionPatient.setter
    def ImagePositionPatient(self, value: Optional[List[Decimal]]):
        if value is None:
            if "ImagePositionPatient" in self._dataset:
                del self._dataset.ImagePositionPatient
        else:
            self._dataset.ImagePositionPatient = value

    @property
    def ImageOrientationPatient(self) -> Optional[List[Decimal]]:
        if "ImageOrientationPatient" in self._dataset:
            return self._dataset.ImageOrientationPatient
        return None

    @ImageOrientationPatient.setter
    def ImageOrientationPatient(self, value: Optional[List[Decimal]]):
        if value is None:
            if "ImageOrientationPatient" in self._dataset:
                del self._dataset.ImageOrientationPatient
        else:
            self._dataset.ImageOrientationPatient = value

    @property
    def GridDimensions(self) -> Optional[List[int]]:
        if "GridDimensions" in self._dataset:
            return self._dataset.GridDimensions
        return None

    @GridDimensions.setter
    def GridDimensions(self, value: Optional[List[int]]):
        if value is None:
            if "GridDimensions" in self._dataset:
                del self._dataset.GridDimensions
        else:
            self._dataset.GridDimensions = value

    @property
    def GridResolution(self) -> Optional[List[float]]:
        if "GridResolution" in self._dataset:
            return self._dataset.GridResolution
        return None

    @GridResolution.setter
    def GridResolution(self, value: Optional[List[float]]):
        if value is None:
            if "GridResolution" in self._dataset:
                del self._dataset.GridResolution
        else:
            self._dataset.GridResolution = value

    @property
    def VectorGridData(self) -> Optional[bytes]:
        if "VectorGridData" in self._dataset:
            return self._dataset.VectorGridData
        return None

    @VectorGridData.setter
    def VectorGridData(self, value: Optional[bytes]):
        if value is None:
            if "VectorGridData" in self._dataset:
                del self._dataset.VectorGridData
        else:
            self._dataset.VectorGridData = value
