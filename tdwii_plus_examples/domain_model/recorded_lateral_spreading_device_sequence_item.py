from typing import Any, List, Optional

import pydicom


class RecordedLateralSpreadingDeviceSequenceItem:
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
    def LateralSpreadingDeviceID(self) -> Optional[str]:
        if "LateralSpreadingDeviceID" in self._dataset:
            return self._dataset.LateralSpreadingDeviceID
        return None

    @LateralSpreadingDeviceID.setter
    def LateralSpreadingDeviceID(self, value: Optional[str]):
        if value is None:
            if "LateralSpreadingDeviceID" in self._dataset:
                del self._dataset.LateralSpreadingDeviceID
        else:
            self._dataset.LateralSpreadingDeviceID = value

    @property
    def ReferencedLateralSpreadingDeviceNumber(self) -> Optional[int]:
        if "ReferencedLateralSpreadingDeviceNumber" in self._dataset:
            return self._dataset.ReferencedLateralSpreadingDeviceNumber
        return None

    @ReferencedLateralSpreadingDeviceNumber.setter
    def ReferencedLateralSpreadingDeviceNumber(self, value: Optional[int]):
        if value is None:
            if "ReferencedLateralSpreadingDeviceNumber" in self._dataset:
                del self._dataset.ReferencedLateralSpreadingDeviceNumber
        else:
            self._dataset.ReferencedLateralSpreadingDeviceNumber = value
