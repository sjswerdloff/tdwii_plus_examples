from typing import Any, List, Optional  # noqa

import pydicom


class ReferencedFirstFrameSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ReferencedSOPClassUID(self) -> Optional[str]:
        if "ReferencedSOPClassUID" in self._dataset:
            return self._dataset.ReferencedSOPClassUID
        return None

    @ReferencedSOPClassUID.setter
    def ReferencedSOPClassUID(self, value: Optional[str]):
        if value is None:
            if "ReferencedSOPClassUID" in self._dataset:
                del self._dataset.ReferencedSOPClassUID
        else:
            self._dataset.ReferencedSOPClassUID = value

    @property
    def ReferencedSOPInstanceUID(self) -> Optional[str]:
        if "ReferencedSOPInstanceUID" in self._dataset:
            return self._dataset.ReferencedSOPInstanceUID
        return None

    @ReferencedSOPInstanceUID.setter
    def ReferencedSOPInstanceUID(self, value: Optional[str]):
        if value is None:
            if "ReferencedSOPInstanceUID" in self._dataset:
                del self._dataset.ReferencedSOPInstanceUID
        else:
            self._dataset.ReferencedSOPInstanceUID = value

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
    def ReferencedSegmentNumber(self) -> Optional[List[int]]:
        if "ReferencedSegmentNumber" in self._dataset:
            return self._dataset.ReferencedSegmentNumber
        return None

    @ReferencedSegmentNumber.setter
    def ReferencedSegmentNumber(self, value: Optional[List[int]]):
        if value is None:
            if "ReferencedSegmentNumber" in self._dataset:
                del self._dataset.ReferencedSegmentNumber
        else:
            self._dataset.ReferencedSegmentNumber = value
