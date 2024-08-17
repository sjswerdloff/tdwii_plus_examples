from typing import Any, List, Optional

import pydicom


class LateralSpreadingDeviceSequenceItem:
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
    def LateralSpreadingDeviceNumber(self) -> Optional[int]:
        if "LateralSpreadingDeviceNumber" in self._dataset:
            return self._dataset.LateralSpreadingDeviceNumber
        return None

    @LateralSpreadingDeviceNumber.setter
    def LateralSpreadingDeviceNumber(self, value: Optional[int]):
        if value is None:
            if "LateralSpreadingDeviceNumber" in self._dataset:
                del self._dataset.LateralSpreadingDeviceNumber
        else:
            self._dataset.LateralSpreadingDeviceNumber = value

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
    def LateralSpreadingDeviceType(self) -> Optional[str]:
        if "LateralSpreadingDeviceType" in self._dataset:
            return self._dataset.LateralSpreadingDeviceType
        return None

    @LateralSpreadingDeviceType.setter
    def LateralSpreadingDeviceType(self, value: Optional[str]):
        if value is None:
            if "LateralSpreadingDeviceType" in self._dataset:
                del self._dataset.LateralSpreadingDeviceType
        else:
            self._dataset.LateralSpreadingDeviceType = value

    @property
    def LateralSpreadingDeviceDescription(self) -> Optional[str]:
        if "LateralSpreadingDeviceDescription" in self._dataset:
            return self._dataset.LateralSpreadingDeviceDescription
        return None

    @LateralSpreadingDeviceDescription.setter
    def LateralSpreadingDeviceDescription(self, value: Optional[str]):
        if value is None:
            if "LateralSpreadingDeviceDescription" in self._dataset:
                del self._dataset.LateralSpreadingDeviceDescription
        else:
            self._dataset.LateralSpreadingDeviceDescription = value
