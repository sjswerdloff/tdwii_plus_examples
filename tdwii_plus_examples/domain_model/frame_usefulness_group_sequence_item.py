from typing import Any, List, Optional

import pydicom


class FrameUsefulnessGroupSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def IncludesImagingSubject(self) -> Optional[str]:
        if "IncludesImagingSubject" in self._dataset:
            return self._dataset.IncludesImagingSubject
        return None

    @IncludesImagingSubject.setter
    def IncludesImagingSubject(self, value: Optional[str]):
        if value is None:
            if "IncludesImagingSubject" in self._dataset:
                del self._dataset.IncludesImagingSubject
        else:
            self._dataset.IncludesImagingSubject = value

    @property
    def IncludesInformation(self) -> Optional[str]:
        if "IncludesInformation" in self._dataset:
            return self._dataset.IncludesInformation
        return None

    @IncludesInformation.setter
    def IncludesInformation(self, value: Optional[str]):
        if value is None:
            if "IncludesInformation" in self._dataset:
                del self._dataset.IncludesInformation
        else:
            self._dataset.IncludesInformation = value
