from typing import Any, List, Optional

import pydicom


class RangeShifterSettingsSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def RangeShifterSetting(self) -> Optional[str]:
        if "RangeShifterSetting" in self._dataset:
            return self._dataset.RangeShifterSetting
        return None

    @RangeShifterSetting.setter
    def RangeShifterSetting(self, value: Optional[str]):
        if value is None:
            if "RangeShifterSetting" in self._dataset:
                del self._dataset.RangeShifterSetting
        else:
            self._dataset.RangeShifterSetting = value

    @property
    def ReferencedRangeShifterNumber(self) -> Optional[int]:
        if "ReferencedRangeShifterNumber" in self._dataset:
            return self._dataset.ReferencedRangeShifterNumber
        return None

    @ReferencedRangeShifterNumber.setter
    def ReferencedRangeShifterNumber(self, value: Optional[int]):
        if value is None:
            if "ReferencedRangeShifterNumber" in self._dataset:
                del self._dataset.ReferencedRangeShifterNumber
        else:
            self._dataset.ReferencedRangeShifterNumber = value
