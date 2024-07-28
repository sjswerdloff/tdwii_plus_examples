from typing import List, Optional

import pydicom


class LateralSpreadingDeviceSettings:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset or pydicom.Dataset()

        if dataset:
            self.validate()

    def validate(self) -> List[str]:
        errors = []

        # Type 1 validations
        type1_elements = [
            "LateralSpreadingDeviceSetting",
            "ReferencedLateralSpreadingDeviceNumber",
        ]
        for elem in type1_elements:
            if elem not in self._dataset or self._dataset.get(elem) == "":
                errors.append(f"Type 1 element '{elem}' is missing or empty")

        return errors

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def lateral_spreading_device_water_equivalent_thickness(self) -> Optional[float]:
        return self._dataset.get("LateralSpreadingDeviceWaterEquivalentThickness")

    @lateral_spreading_device_water_equivalent_thickness.setter
    def lateral_spreading_device_water_equivalent_thickness(self, value: Optional[float]) -> None:
        if value is not None:
            self._dataset.LateralSpreadingDeviceWaterEquivalentThickness = float(value)
        elif "LateralSpreadingDeviceWaterEquivalentThickness" in self._dataset:
            del self._dataset.LateralSpreadingDeviceWaterEquivalentThickness

    @property
    def lateral_spreading_device_setting(self) -> str:
        return self._dataset.get("LateralSpreadingDeviceSetting", "")

    @lateral_spreading_device_setting.setter
    def lateral_spreading_device_setting(self, value: str) -> None:
        self._dataset.LateralSpreadingDeviceSetting = str(value)

    @property
    def isocenter_to_lateral_spreading_device_distance(self) -> Optional[float]:
        return self._dataset.get("IsocenterToLateralSpreadingDeviceDistance")

    @isocenter_to_lateral_spreading_device_distance.setter
    def isocenter_to_lateral_spreading_device_distance(self, value: Optional[float]) -> None:
        if value is not None:
            self._dataset.IsocenterToLateralSpreadingDeviceDistance = float(value)
        elif "IsocenterToLateralSpreadingDeviceDistance" in self._dataset:
            del self._dataset.IsocenterToLateralSpreadingDeviceDistance

    @property
    def referenced_lateral_spreading_device_number(self) -> str:
        return self._dataset.get("ReferencedLateralSpreadingDeviceNumber", "")

    @referenced_lateral_spreading_device_number.setter
    def referenced_lateral_spreading_device_number(self, value: str) -> None:
        self._dataset.ReferencedLateralSpreadingDeviceNumber = str(value)
