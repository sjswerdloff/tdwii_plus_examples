from typing import Any, List, Optional  # noqa

import pydicom


class WholeSlideMicroscopyImageFrameTypeSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def FrameType(self) -> Optional[List[str]]:
        if "FrameType" in self._dataset:
            return self._dataset.FrameType
        return None

    @FrameType.setter
    def FrameType(self, value: Optional[List[str]]):
        if value is None:
            if "FrameType" in self._dataset:
                del self._dataset.FrameType
        else:
            self._dataset.FrameType = value
