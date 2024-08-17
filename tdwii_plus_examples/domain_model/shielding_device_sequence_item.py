from typing import Any, List, Optional  # noqa

import pydicom


class ShieldingDeviceSequenceItem:
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
    def ShieldingDeviceType(self) -> Optional[str]:
        if "ShieldingDeviceType" in self._dataset:
            return self._dataset.ShieldingDeviceType
        return None

    @ShieldingDeviceType.setter
    def ShieldingDeviceType(self, value: Optional[str]):
        if value is None:
            if "ShieldingDeviceType" in self._dataset:
                del self._dataset.ShieldingDeviceType
        else:
            self._dataset.ShieldingDeviceType = value

    @property
    def ShieldingDeviceLabel(self) -> Optional[str]:
        if "ShieldingDeviceLabel" in self._dataset:
            return self._dataset.ShieldingDeviceLabel
        return None

    @ShieldingDeviceLabel.setter
    def ShieldingDeviceLabel(self, value: Optional[str]):
        if value is None:
            if "ShieldingDeviceLabel" in self._dataset:
                del self._dataset.ShieldingDeviceLabel
        else:
            self._dataset.ShieldingDeviceLabel = value

    @property
    def ShieldingDeviceDescription(self) -> Optional[str]:
        if "ShieldingDeviceDescription" in self._dataset:
            return self._dataset.ShieldingDeviceDescription
        return None

    @ShieldingDeviceDescription.setter
    def ShieldingDeviceDescription(self, value: Optional[str]):
        if value is None:
            if "ShieldingDeviceDescription" in self._dataset:
                del self._dataset.ShieldingDeviceDescription
        else:
            self._dataset.ShieldingDeviceDescription = value

    @property
    def ShieldingDevicePosition(self) -> Optional[str]:
        if "ShieldingDevicePosition" in self._dataset:
            return self._dataset.ShieldingDevicePosition
        return None

    @ShieldingDevicePosition.setter
    def ShieldingDevicePosition(self, value: Optional[str]):
        if value is None:
            if "ShieldingDevicePosition" in self._dataset:
                del self._dataset.ShieldingDevicePosition
        else:
            self._dataset.ShieldingDevicePosition = value
