from typing import Any, List, Optional

import pydicom


class RangeShifterSequenceItem:
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
    def RangeShifterNumber(self) -> Optional[int]:
        if "RangeShifterNumber" in self._dataset:
            return self._dataset.RangeShifterNumber
        return None

    @RangeShifterNumber.setter
    def RangeShifterNumber(self, value: Optional[int]):
        if value is None:
            if "RangeShifterNumber" in self._dataset:
                del self._dataset.RangeShifterNumber
        else:
            self._dataset.RangeShifterNumber = value

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
    def RangeShifterType(self) -> Optional[str]:
        if "RangeShifterType" in self._dataset:
            return self._dataset.RangeShifterType
        return None

    @RangeShifterType.setter
    def RangeShifterType(self, value: Optional[str]):
        if value is None:
            if "RangeShifterType" in self._dataset:
                del self._dataset.RangeShifterType
        else:
            self._dataset.RangeShifterType = value

    @property
    def RangeShifterDescription(self) -> Optional[str]:
        if "RangeShifterDescription" in self._dataset:
            return self._dataset.RangeShifterDescription
        return None

    @RangeShifterDescription.setter
    def RangeShifterDescription(self, value: Optional[str]):
        if value is None:
            if "RangeShifterDescription" in self._dataset:
                del self._dataset.RangeShifterDescription
        else:
            self._dataset.RangeShifterDescription = value
