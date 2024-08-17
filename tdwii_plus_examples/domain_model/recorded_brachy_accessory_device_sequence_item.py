from typing import Any, List, Optional

import pydicom


class RecordedBrachyAccessoryDeviceSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ReferencedBrachyAccessoryDeviceNumber(self) -> Optional[int]:
        if "ReferencedBrachyAccessoryDeviceNumber" in self._dataset:
            return self._dataset.ReferencedBrachyAccessoryDeviceNumber
        return None

    @ReferencedBrachyAccessoryDeviceNumber.setter
    def ReferencedBrachyAccessoryDeviceNumber(self, value: Optional[int]):
        if value is None:
            if "ReferencedBrachyAccessoryDeviceNumber" in self._dataset:
                del self._dataset.ReferencedBrachyAccessoryDeviceNumber
        else:
            self._dataset.ReferencedBrachyAccessoryDeviceNumber = value

    @property
    def BrachyAccessoryDeviceID(self) -> Optional[str]:
        if "BrachyAccessoryDeviceID" in self._dataset:
            return self._dataset.BrachyAccessoryDeviceID
        return None

    @BrachyAccessoryDeviceID.setter
    def BrachyAccessoryDeviceID(self, value: Optional[str]):
        if value is None:
            if "BrachyAccessoryDeviceID" in self._dataset:
                del self._dataset.BrachyAccessoryDeviceID
        else:
            self._dataset.BrachyAccessoryDeviceID = value

    @property
    def BrachyAccessoryDeviceType(self) -> Optional[str]:
        if "BrachyAccessoryDeviceType" in self._dataset:
            return self._dataset.BrachyAccessoryDeviceType
        return None

    @BrachyAccessoryDeviceType.setter
    def BrachyAccessoryDeviceType(self, value: Optional[str]):
        if value is None:
            if "BrachyAccessoryDeviceType" in self._dataset:
                del self._dataset.BrachyAccessoryDeviceType
        else:
            self._dataset.BrachyAccessoryDeviceType = value

    @property
    def BrachyAccessoryDeviceName(self) -> Optional[str]:
        if "BrachyAccessoryDeviceName" in self._dataset:
            return self._dataset.BrachyAccessoryDeviceName
        return None

    @BrachyAccessoryDeviceName.setter
    def BrachyAccessoryDeviceName(self, value: Optional[str]):
        if value is None:
            if "BrachyAccessoryDeviceName" in self._dataset:
                del self._dataset.BrachyAccessoryDeviceName
        else:
            self._dataset.BrachyAccessoryDeviceName = value
