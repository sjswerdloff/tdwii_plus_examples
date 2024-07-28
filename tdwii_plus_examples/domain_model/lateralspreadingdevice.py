from typing import List, Optional, Union

from pydicom.dataset import Dataset


class LateralSpreadingDevice:
    def __init__(self):
        self._dataset = Dataset()

    @property
    def lateral_spreading_device_id(self) -> str:
        return self._dataset.LateralSpreadingDeviceID

    @lateral_spreading_device_id.setter
    def lateral_spreading_device_id(self, value: str):
        self._dataset.LateralSpreadingDeviceID = value

    @property
    def lateral_spreading_device_type(self) -> str:
        return self._dataset.LateralSpreadingDeviceType

    @lateral_spreading_device_type.setter
    def lateral_spreading_device_type(self, value: str):
        self._dataset.LateralSpreadingDeviceType = value

    def to_dataset(self) -> Dataset:
        return self._dataset

    @classmethod
    def from_dataset(cls, dataset: Dataset):
        device = cls()
        device._dataset = dataset
        return device

    def validate(self) -> List[str]:
        errors = []

        # Check Type 1 elements
        type1_elements = ["LateralSpreadingDeviceID", "LateralSpreadingDeviceType"]
        for elem in type1_elements:
            if not hasattr(self._dataset, elem):
                errors.append(f"{elem} is missing")
            elif getattr(self._dataset, elem) is None:
                errors.append(f"{elem} has no value assigned")

        return errors
