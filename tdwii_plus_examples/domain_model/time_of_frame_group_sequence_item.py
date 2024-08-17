from typing import Any, List, Optional  # noqa

import pydicom


class TimeOfFrameGroupSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def FrameOriginTimestamp(self) -> Optional[bytes]:
        if "FrameOriginTimestamp" in self._dataset:
            return self._dataset.FrameOriginTimestamp
        return None

    @FrameOriginTimestamp.setter
    def FrameOriginTimestamp(self, value: Optional[bytes]):
        if value is None:
            if "FrameOriginTimestamp" in self._dataset:
                del self._dataset.FrameOriginTimestamp
        else:
            self._dataset.FrameOriginTimestamp = value
