from typing import Any, List, Optional  # noqa

import pydicom


class TwoDimensionalToThreeDimensionalMapSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ReferencedFrameNumber(self) -> Optional[List[int]]:
        if "ReferencedFrameNumber" in self._dataset:
            return self._dataset.ReferencedFrameNumber
        return None

    @ReferencedFrameNumber.setter
    def ReferencedFrameNumber(self, value: Optional[List[int]]):
        if value is None:
            if "ReferencedFrameNumber" in self._dataset:
                del self._dataset.ReferencedFrameNumber
        else:
            self._dataset.ReferencedFrameNumber = value

    @property
    def NumberOfMapPoints(self) -> Optional[int]:
        if "NumberOfMapPoints" in self._dataset:
            return self._dataset.NumberOfMapPoints
        return None

    @NumberOfMapPoints.setter
    def NumberOfMapPoints(self, value: Optional[int]):
        if value is None:
            if "NumberOfMapPoints" in self._dataset:
                del self._dataset.NumberOfMapPoints
        else:
            self._dataset.NumberOfMapPoints = value

    @property
    def TwoDimensionalToThreeDimensionalMapData(self) -> Optional[bytes]:
        if "TwoDimensionalToThreeDimensionalMapData" in self._dataset:
            return self._dataset.TwoDimensionalToThreeDimensionalMapData
        return None

    @TwoDimensionalToThreeDimensionalMapData.setter
    def TwoDimensionalToThreeDimensionalMapData(self, value: Optional[bytes]):
        if value is None:
            if "TwoDimensionalToThreeDimensionalMapData" in self._dataset:
                del self._dataset.TwoDimensionalToThreeDimensionalMapData
        else:
            self._dataset.TwoDimensionalToThreeDimensionalMapData = value
