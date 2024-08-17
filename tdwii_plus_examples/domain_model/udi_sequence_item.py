from typing import Any, List, Optional

import pydicom


class UDISequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def UniqueDeviceIdentifier(self) -> Optional[str]:
        if "UniqueDeviceIdentifier" in self._dataset:
            return self._dataset.UniqueDeviceIdentifier
        return None

    @UniqueDeviceIdentifier.setter
    def UniqueDeviceIdentifier(self, value: Optional[str]):
        if value is None:
            if "UniqueDeviceIdentifier" in self._dataset:
                del self._dataset.UniqueDeviceIdentifier
        else:
            self._dataset.UniqueDeviceIdentifier = value

    @property
    def DeviceDescription(self) -> Optional[str]:
        if "DeviceDescription" in self._dataset:
            return self._dataset.DeviceDescription
        return None

    @DeviceDescription.setter
    def DeviceDescription(self, value: Optional[str]):
        if value is None:
            if "DeviceDescription" in self._dataset:
                del self._dataset.DeviceDescription
        else:
            self._dataset.DeviceDescription = value
