from typing import Any, List, Optional  # noqa

import pydicom


class LateralSpreadingDeviceSettingsSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def LateralSpreadingDeviceSetting(self) -> Optional[str]:
        if "LateralSpreadingDeviceSetting" in self._dataset:
            return self._dataset.LateralSpreadingDeviceSetting
        return None

    @LateralSpreadingDeviceSetting.setter
    def LateralSpreadingDeviceSetting(self, value: Optional[str]):
        if value is None:
            if "LateralSpreadingDeviceSetting" in self._dataset:
                del self._dataset.LateralSpreadingDeviceSetting
        else:
            self._dataset.LateralSpreadingDeviceSetting = value

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
