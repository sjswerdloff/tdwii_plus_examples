from typing import List, Optional, Union

from pydicom.dataset import Dataset


class RangeShifterSettings:
    def __init__(self, dataset: Optional[Dataset] = None) -> None:
        self._dataset: Dataset = Dataset() if dataset is None else dataset
        if dataset is not None:
            self.validate()

    @classmethod
    def from_dataset(cls, dataset: Dataset) -> "RangeShifterSettings":
        return cls(dataset)

    @property
    def referenced_range_shifter_number(self) -> Optional[str]:
        return self._dataset.get("ReferencedRangeShifterNumber")

    @referenced_range_shifter_number.setter
    def referenced_range_shifter_number(self, value: Union[str, int]) -> None:
        self._dataset.ReferencedRangeShifterNumber = str(value)

    @property
    def range_shifter_setting(self) -> Optional[str]:
        return self._dataset.get("RangeShifterSetting")

    @range_shifter_setting.setter
    def range_shifter_setting(self, value: str) -> None:
        self._dataset.RangeShifterSetting = str(value)

    @property
    def isocenter_to_range_shifter_distance(self) -> Optional[float]:
        return self._dataset.get("IsocenterToRangeShifterDistance")

    @isocenter_to_range_shifter_distance.setter
    def isocenter_to_range_shifter_distance(self, value: float) -> None:
        self._dataset.IsocenterToRangeShifterDistance = float(value)

    @property
    def range_shifter_water_equivalent_thickness(self) -> Optional[float]:
        return self._dataset.get("RangeShifterWaterEquivalentThickness")

    @range_shifter_water_equivalent_thickness.setter
    def range_shifter_water_equivalent_thickness(self, value: float) -> None:
        self._dataset.RangeShifterWaterEquivalentThickness = float(value)

    def validate(self) -> List[str]:
        errors: List[str] = []

        # Check Type 1 elements
        if "ReferencedRangeShifterNumber" not in self._dataset or not self._dataset.ReferencedRangeShifterNumber:
            errors.append("Referenced Range Shifter Number (Type 1) is missing or empty")
        if "RangeShifterSetting" not in self._dataset or not self._dataset.RangeShifterSetting:
            errors.append("Range Shifter Setting (Type 1) is missing or empty")

        # Type 3 elements are optional, so we don't need to check for their presence

        return errors

    def to_dataset(self) -> Dataset:
        return self._dataset
