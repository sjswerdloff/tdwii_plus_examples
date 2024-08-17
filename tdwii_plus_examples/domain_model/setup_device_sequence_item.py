from decimal import Decimal
from typing import Any, List, Optional  # noqa

import pydicom


class SetupDeviceSequenceItem:
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
    def SetupDeviceType(self) -> Optional[str]:
        if "SetupDeviceType" in self._dataset:
            return self._dataset.SetupDeviceType
        return None

    @SetupDeviceType.setter
    def SetupDeviceType(self, value: Optional[str]):
        if value is None:
            if "SetupDeviceType" in self._dataset:
                del self._dataset.SetupDeviceType
        else:
            self._dataset.SetupDeviceType = value

    @property
    def SetupDeviceLabel(self) -> Optional[str]:
        if "SetupDeviceLabel" in self._dataset:
            return self._dataset.SetupDeviceLabel
        return None

    @SetupDeviceLabel.setter
    def SetupDeviceLabel(self, value: Optional[str]):
        if value is None:
            if "SetupDeviceLabel" in self._dataset:
                del self._dataset.SetupDeviceLabel
        else:
            self._dataset.SetupDeviceLabel = value

    @property
    def SetupDeviceDescription(self) -> Optional[str]:
        if "SetupDeviceDescription" in self._dataset:
            return self._dataset.SetupDeviceDescription
        return None

    @SetupDeviceDescription.setter
    def SetupDeviceDescription(self, value: Optional[str]):
        if value is None:
            if "SetupDeviceDescription" in self._dataset:
                del self._dataset.SetupDeviceDescription
        else:
            self._dataset.SetupDeviceDescription = value

    @property
    def SetupDeviceParameter(self) -> Optional[Decimal]:
        if "SetupDeviceParameter" in self._dataset:
            return self._dataset.SetupDeviceParameter
        return None

    @SetupDeviceParameter.setter
    def SetupDeviceParameter(self, value: Optional[Decimal]):
        if value is None:
            if "SetupDeviceParameter" in self._dataset:
                del self._dataset.SetupDeviceParameter
        else:
            self._dataset.SetupDeviceParameter = value

    @property
    def SetupReferenceDescription(self) -> Optional[str]:
        if "SetupReferenceDescription" in self._dataset:
            return self._dataset.SetupReferenceDescription
        return None

    @SetupReferenceDescription.setter
    def SetupReferenceDescription(self, value: Optional[str]):
        if value is None:
            if "SetupReferenceDescription" in self._dataset:
                del self._dataset.SetupReferenceDescription
        else:
            self._dataset.SetupReferenceDescription = value
