from typing import Any, List, Optional  # noqa

import pydicom


class FixationDeviceSequenceItem:
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
    def FixationDeviceType(self) -> Optional[str]:
        if "FixationDeviceType" in self._dataset:
            return self._dataset.FixationDeviceType
        return None

    @FixationDeviceType.setter
    def FixationDeviceType(self, value: Optional[str]):
        if value is None:
            if "FixationDeviceType" in self._dataset:
                del self._dataset.FixationDeviceType
        else:
            self._dataset.FixationDeviceType = value

    @property
    def FixationDeviceLabel(self) -> Optional[str]:
        if "FixationDeviceLabel" in self._dataset:
            return self._dataset.FixationDeviceLabel
        return None

    @FixationDeviceLabel.setter
    def FixationDeviceLabel(self, value: Optional[str]):
        if value is None:
            if "FixationDeviceLabel" in self._dataset:
                del self._dataset.FixationDeviceLabel
        else:
            self._dataset.FixationDeviceLabel = value

    @property
    def FixationDeviceDescription(self) -> Optional[str]:
        if "FixationDeviceDescription" in self._dataset:
            return self._dataset.FixationDeviceDescription
        return None

    @FixationDeviceDescription.setter
    def FixationDeviceDescription(self, value: Optional[str]):
        if value is None:
            if "FixationDeviceDescription" in self._dataset:
                del self._dataset.FixationDeviceDescription
        else:
            self._dataset.FixationDeviceDescription = value

    @property
    def FixationDevicePosition(self) -> Optional[str]:
        if "FixationDevicePosition" in self._dataset:
            return self._dataset.FixationDevicePosition
        return None

    @FixationDevicePosition.setter
    def FixationDevicePosition(self, value: Optional[str]):
        if value is None:
            if "FixationDevicePosition" in self._dataset:
                del self._dataset.FixationDevicePosition
        else:
            self._dataset.FixationDevicePosition = value

    @property
    def FixationDevicePitchAngle(self) -> Optional[float]:
        if "FixationDevicePitchAngle" in self._dataset:
            return self._dataset.FixationDevicePitchAngle
        return None

    @FixationDevicePitchAngle.setter
    def FixationDevicePitchAngle(self, value: Optional[float]):
        if value is None:
            if "FixationDevicePitchAngle" in self._dataset:
                del self._dataset.FixationDevicePitchAngle
        else:
            self._dataset.FixationDevicePitchAngle = value

    @property
    def FixationDeviceRollAngle(self) -> Optional[float]:
        if "FixationDeviceRollAngle" in self._dataset:
            return self._dataset.FixationDeviceRollAngle
        return None

    @FixationDeviceRollAngle.setter
    def FixationDeviceRollAngle(self, value: Optional[float]):
        if value is None:
            if "FixationDeviceRollAngle" in self._dataset:
                del self._dataset.FixationDeviceRollAngle
        else:
            self._dataset.FixationDeviceRollAngle = value
