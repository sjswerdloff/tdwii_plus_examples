from typing import Any, List, Optional  # noqa

import pydicom


class SurfacePointsNormalsSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def NumberOfVectors(self) -> Optional[int]:
        if "NumberOfVectors" in self._dataset:
            return self._dataset.NumberOfVectors
        return None

    @NumberOfVectors.setter
    def NumberOfVectors(self, value: Optional[int]):
        if value is None:
            if "NumberOfVectors" in self._dataset:
                del self._dataset.NumberOfVectors
        else:
            self._dataset.NumberOfVectors = value

    @property
    def VectorDimensionality(self) -> Optional[int]:
        if "VectorDimensionality" in self._dataset:
            return self._dataset.VectorDimensionality
        return None

    @VectorDimensionality.setter
    def VectorDimensionality(self, value: Optional[int]):
        if value is None:
            if "VectorDimensionality" in self._dataset:
                del self._dataset.VectorDimensionality
        else:
            self._dataset.VectorDimensionality = value

    @property
    def VectorAccuracy(self) -> Optional[List[float]]:
        if "VectorAccuracy" in self._dataset:
            return self._dataset.VectorAccuracy
        return None

    @VectorAccuracy.setter
    def VectorAccuracy(self, value: Optional[List[float]]):
        if value is None:
            if "VectorAccuracy" in self._dataset:
                del self._dataset.VectorAccuracy
        else:
            self._dataset.VectorAccuracy = value

    @property
    def VectorCoordinateData(self) -> Optional[bytes]:
        if "VectorCoordinateData" in self._dataset:
            return self._dataset.VectorCoordinateData
        return None

    @VectorCoordinateData.setter
    def VectorCoordinateData(self, value: Optional[bytes]):
        if value is None:
            if "VectorCoordinateData" in self._dataset:
                del self._dataset.VectorCoordinateData
        else:
            self._dataset.VectorCoordinateData = value
