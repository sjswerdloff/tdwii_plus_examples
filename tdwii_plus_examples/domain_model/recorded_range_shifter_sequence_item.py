from typing import Any, List, Optional  # noqa

import pydicom


class RecordedRangeShifterSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def AccessoryCode(self) -> Optional[str]:
        if "AccessoryCode" in self._dataset:
            return self._dataset.AccessoryCode
        return None

    @AccessoryCode.setter
    def AccessoryCode(self, value: Optional[str]):
        if value is None:
            if "AccessoryCode" in self._dataset:
                del self._dataset.AccessoryCode
        else:
            self._dataset.AccessoryCode = value

    @property
    def RangeShifterID(self) -> Optional[str]:
        if "RangeShifterID" in self._dataset:
            return self._dataset.RangeShifterID
        return None

    @RangeShifterID.setter
    def RangeShifterID(self, value: Optional[str]):
        if value is None:
            if "RangeShifterID" in self._dataset:
                del self._dataset.RangeShifterID
        else:
            self._dataset.RangeShifterID = value

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
