from typing import Any, List, Optional  # noqa

import pydicom


class SelectedFrameFunctionalGroupsSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def SelectedFrameNumber(self) -> Optional[int]:
        if "SelectedFrameNumber" in self._dataset:
            return self._dataset.SelectedFrameNumber
        return None

    @SelectedFrameNumber.setter
    def SelectedFrameNumber(self, value: Optional[int]):
        if value is None:
            if "SelectedFrameNumber" in self._dataset:
                del self._dataset.SelectedFrameNumber
        else:
            self._dataset.SelectedFrameNumber = value
