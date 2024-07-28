from typing import List, Optional, Union

from pydicom.dataset import Dataset


class RTIonToleranceTable:
    def __init__(self):
        self._dataset = Dataset()

    # Type 1 elements
    @property
    def tolerance_table_number(self) -> int:
        return self._dataset.ToleranceTableNumber

    @tolerance_table_number.setter
    def tolerance_table_number(self, value: int):
        self._dataset.ToleranceTableNumber = value

    @property
    def tolerance_table_label(self) -> str:
        return self._dataset.ToleranceTableLabel

    @tolerance_table_label.setter
    def tolerance_table_label(self, value: str):
        self._dataset.ToleranceTableLabel = value

    # Type 2 elements
    @property
    def gantry_angle_tolerance(self) -> Optional[float]:
        return self._dataset.get("GantryAngleTolerance")

    @gantry_angle_tolerance.setter
    def gantry_angle_tolerance(self, value: Optional[float]):
        self._dataset.GantryAngleTolerance = value

    @property
    def beam_limiting_device_angle_tolerance(self) -> Optional[float]:
        return self._dataset.get("BeamLimitingDeviceAngleTolerance")

    @beam_limiting_device_angle_tolerance.setter
    def beam_limiting_device_angle_tolerance(self, value: Optional[float]):
        self._dataset.BeamLimitingDeviceAngleTolerance = value

    @property
    def patient_support_angle_tolerance(self) -> Optional[float]:
        return self._dataset.get("PatientSupportAngleTolerance")

    @patient_support_angle_tolerance.setter
    def patient_support_angle_tolerance(self, value: Optional[float]):
        self._dataset.PatientSupportAngleTolerance = value

    # Type 3 elements
    @property
    def table_top_vertical_position_tolerance(self) -> Optional[float]:
        return self._dataset.get("TableTopVerticalPositionTolerance")

    @table_top_vertical_position_tolerance.setter
    def table_top_vertical_position_tolerance(self, value: Optional[float]):
        if value is not None:
            self._dataset.TableTopVerticalPositionTolerance = value

    @property
    def table_top_longitudinal_position_tolerance(self) -> Optional[float]:
        return self._dataset.get("TableTopLongitudinalPositionTolerance")

    @table_top_longitudinal_position_tolerance.setter
    def table_top_longitudinal_position_tolerance(self, value: Optional[float]):
        if value is not None:
            self._dataset.TableTopLongitudinalPositionTolerance = value

    @property
    def table_top_lateral_position_tolerance(self) -> Optional[float]:
        return self._dataset.get("TableTopLateralPositionTolerance")

    @table_top_lateral_position_tolerance.setter
    def table_top_lateral_position_tolerance(self, value: Optional[float]):
        if value is not None:
            self._dataset.TableTopLateralPositionTolerance = value

    @property
    def snout_position_tolerance(self) -> Optional[float]:
        return self._dataset.get("SnoutPositionTolerance")

    @snout_position_tolerance.setter
    def snout_position_tolerance(self, value: Optional[float]):
        if value is not None:
            self._dataset.SnoutPositionTolerance = value

    def to_dataset(self) -> Dataset:
        return self._dataset

    @classmethod
    def from_dataset(cls, dataset: Dataset):
        tolerance_table = cls()
        tolerance_table._dataset = dataset
        return tolerance_table

    def validate(self) -> List[str]:
        errors = []

        # Check Type 1 elements
        if not hasattr(self._dataset, "ToleranceTableNumber"):
            errors.append("ToleranceTableNumber is missing")
        if not hasattr(self._dataset, "ToleranceTableLabel"):
            errors.append("ToleranceTableLabel is missing")

        # Check Type 2 elements
        type2_elements = ["GantryAngleTolerance", "BeamLimitingDeviceAngleTolerance", "PatientSupportAngleTolerance"]
        for elem in type2_elements:
            if not hasattr(self._dataset, elem):
                errors.append(f"{elem} is missing")

        return errors
