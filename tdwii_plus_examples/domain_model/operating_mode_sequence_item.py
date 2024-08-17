from typing import Any, List, Optional  # noqa

import pydicom


class OperatingModeSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def OperatingModeType(self) -> Optional[str]:
        if "OperatingModeType" in self._dataset:
            return self._dataset.OperatingModeType
        return None

    @OperatingModeType.setter
    def OperatingModeType(self, value: Optional[str]):
        if value is None:
            if "OperatingModeType" in self._dataset:
                del self._dataset.OperatingModeType
        else:
            self._dataset.OperatingModeType = value

    @property
    def OperatingMode(self) -> Optional[str]:
        if "OperatingMode" in self._dataset:
            return self._dataset.OperatingMode
        return None

    @OperatingMode.setter
    def OperatingMode(self, value: Optional[str]):
        if value is None:
            if "OperatingMode" in self._dataset:
                del self._dataset.OperatingMode
        else:
            self._dataset.OperatingMode = value
