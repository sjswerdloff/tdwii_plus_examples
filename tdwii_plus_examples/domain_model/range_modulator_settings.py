from typing import List, Optional

from pydicom.dataset import Dataset


class RangeModulatorSettings:
    def __init__(self, dataset: Optional[Dataset] = None) -> None:
        self._dataset = dataset or Dataset()
        if dataset:
            self.validate(dataset)

    @property
    def range_modulator_gating_start_value(self) -> Optional[float]:
        return self._dataset.get("RangeModulatorGatingStartValue")

    @range_modulator_gating_start_value.setter
    def range_modulator_gating_start_value(self, value: Optional[float]) -> None:
        if value is None:
            self._dataset.pop("RangeModulatorGatingStartValue", None)
        else:
            self._dataset.RangeModulatorGatingStartValue = value

    @property
    def range_modulator_gating_stop_value(self) -> Optional[float]:
        return self._dataset.get("RangeModulatorGatingStopValue")

    @range_modulator_gating_stop_value.setter
    def range_modulator_gating_stop_value(self, value: Optional[float]) -> None:
        if value is None:
            self._dataset.pop("RangeModulatorGatingStopValue", None)
        else:
            self._dataset.RangeModulatorGatingStopValue = value

    @property
    def range_modulator_gating_start_water_equivalent_thickness(self) -> Optional[float]:
        return self._dataset.get("RangeModulatorGatingStartWaterEquivalentThickness")

    @range_modulator_gating_start_water_equivalent_thickness.setter
    def range_modulator_gating_start_water_equivalent_thickness(self, value: Optional[float]) -> None:
        if value is None:
            self._dataset.pop("RangeModulatorGatingStartWaterEquivalentThickness", None)
        else:
            self._dataset.RangeModulatorGatingStartWaterEquivalentThickness = value

    @property
    def range_modulator_gating_stop_water_equivalent_thickness(self) -> Optional[float]:
        return self._dataset.get("RangeModulatorGatingStopWaterEquivalentThickness")

    @range_modulator_gating_stop_water_equivalent_thickness.setter
    def range_modulator_gating_stop_water_equivalent_thickness(self, value: Optional[float]) -> None:
        if value is None:
            self._dataset.pop("RangeModulatorGatingStopWaterEquivalentThickness", None)
        else:
            self._dataset.RangeModulatorGatingStopWaterEquivalentThickness = value

    @property
    def referenced_range_modulator_number(self) -> Optional[int]:
        return self._dataset.get("ReferencedRangeModulatorNumber")

    @referenced_range_modulator_number.setter
    def referenced_range_modulator_number(self, value: int) -> None:
        self._dataset.ReferencedRangeModulatorNumber = value

    def validate(self, dataset: Dataset) -> List[str]:
        validation_errors: List[str] = []

        # Type 1 elements
        type1_elements = ["ReferencedRangeModulatorNumber"]

        for elem in type1_elements:
            if elem not in dataset or dataset[elem].value is None:
                validation_errors.append(f"Type 1 element '{elem}' is missing or empty")

        # Type 3 elements don't need to be validated for presence or value

        return validation_errors

    def to_dataset(self) -> Dataset:
        return self._dataset
