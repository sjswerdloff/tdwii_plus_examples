from decimal import Decimal
from typing import Any, List, Optional

import pydicom


class BrachyAccessoryDeviceSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ReferencedROINumber(self) -> Optional[int]:
        if "ReferencedROINumber" in self._dataset:
            return self._dataset.ReferencedROINumber
        return None

    @ReferencedROINumber.setter
    def ReferencedROINumber(self, value: Optional[int]):
        if value is None:
            if "ReferencedROINumber" in self._dataset:
                del self._dataset.ReferencedROINumber
        else:
            self._dataset.ReferencedROINumber = value

    @property
    def MaterialID(self) -> Optional[str]:
        if "MaterialID" in self._dataset:
            return self._dataset.MaterialID
        return None

    @MaterialID.setter
    def MaterialID(self, value: Optional[str]):
        if value is None:
            if "MaterialID" in self._dataset:
                del self._dataset.MaterialID
        else:
            self._dataset.MaterialID = value

    @property
    def BrachyAccessoryDeviceNumber(self) -> Optional[int]:
        if "BrachyAccessoryDeviceNumber" in self._dataset:
            return self._dataset.BrachyAccessoryDeviceNumber
        return None

    @BrachyAccessoryDeviceNumber.setter
    def BrachyAccessoryDeviceNumber(self, value: Optional[int]):
        if value is None:
            if "BrachyAccessoryDeviceNumber" in self._dataset:
                del self._dataset.BrachyAccessoryDeviceNumber
        else:
            self._dataset.BrachyAccessoryDeviceNumber = value

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

    @property
    def BrachyAccessoryDeviceNominalThickness(self) -> Optional[Decimal]:
        if "BrachyAccessoryDeviceNominalThickness" in self._dataset:
            return self._dataset.BrachyAccessoryDeviceNominalThickness
        return None

    @BrachyAccessoryDeviceNominalThickness.setter
    def BrachyAccessoryDeviceNominalThickness(self, value: Optional[Decimal]):
        if value is None:
            if "BrachyAccessoryDeviceNominalThickness" in self._dataset:
                del self._dataset.BrachyAccessoryDeviceNominalThickness
        else:
            self._dataset.BrachyAccessoryDeviceNominalThickness = value

    @property
    def BrachyAccessoryDeviceNominalTransmission(self) -> Optional[Decimal]:
        if "BrachyAccessoryDeviceNominalTransmission" in self._dataset:
            return self._dataset.BrachyAccessoryDeviceNominalTransmission
        return None

    @BrachyAccessoryDeviceNominalTransmission.setter
    def BrachyAccessoryDeviceNominalTransmission(self, value: Optional[Decimal]):
        if value is None:
            if "BrachyAccessoryDeviceNominalTransmission" in self._dataset:
                del self._dataset.BrachyAccessoryDeviceNominalTransmission
        else:
            self._dataset.BrachyAccessoryDeviceNominalTransmission = value
