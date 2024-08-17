from typing import Any, List, Optional  # noqa

import pydicom


class FrameExtractionSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def SimpleFrameList(self) -> Optional[List[int]]:
        if "SimpleFrameList" in self._dataset:
            return self._dataset.SimpleFrameList
        return None

    @SimpleFrameList.setter
    def SimpleFrameList(self, value: Optional[List[int]]):
        if value is None:
            if "SimpleFrameList" in self._dataset:
                del self._dataset.SimpleFrameList
        else:
            self._dataset.SimpleFrameList = value

    @property
    def CalculatedFrameList(self) -> Optional[List[int]]:
        if "CalculatedFrameList" in self._dataset:
            return self._dataset.CalculatedFrameList
        return None

    @CalculatedFrameList.setter
    def CalculatedFrameList(self, value: Optional[List[int]]):
        if value is None:
            if "CalculatedFrameList" in self._dataset:
                del self._dataset.CalculatedFrameList
        else:
            self._dataset.CalculatedFrameList = value

    @property
    def TimeRange(self) -> Optional[List[float]]:
        if "TimeRange" in self._dataset:
            return self._dataset.TimeRange
        return None

    @TimeRange.setter
    def TimeRange(self, value: Optional[List[float]]):
        if value is None:
            if "TimeRange" in self._dataset:
                del self._dataset.TimeRange
        else:
            self._dataset.TimeRange = value

    @property
    def MultiFrameSourceSOPInstanceUID(self) -> Optional[str]:
        if "MultiFrameSourceSOPInstanceUID" in self._dataset:
            return self._dataset.MultiFrameSourceSOPInstanceUID
        return None

    @MultiFrameSourceSOPInstanceUID.setter
    def MultiFrameSourceSOPInstanceUID(self, value: Optional[str]):
        if value is None:
            if "MultiFrameSourceSOPInstanceUID" in self._dataset:
                del self._dataset.MultiFrameSourceSOPInstanceUID
        else:
            self._dataset.MultiFrameSourceSOPInstanceUID = value
