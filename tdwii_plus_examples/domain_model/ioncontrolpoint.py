from typing import List, Optional, Union

from pydicom.dataset import Dataset


class IonControlPoint:
    def __init__(self):
        self._dataset = Dataset()

    @property
    def control_point_index(self) -> int:
        return self._dataset.ControlPointIndex

    @control_point_index.setter
    def control_point_index(self, value: int):
        self._dataset.ControlPointIndex = value

    @property
    def nominal_beam_energy(self) -> float:
        return self._dataset.NominalBeamEnergy

    @nominal_beam_energy.setter
    def nominal_beam_energy(self, value: float):
        self._dataset.NominalBeamEnergy = value

    @property
    def gantry_angle(self) -> Optional[float]:
        return self._dataset.get("GantryAngle")

    @gantry_angle.setter
    def gantry_angle(self, value: Optional[float]):
        if value is not None:
            self._dataset.GantryAngle = value

    # Add more properties as needed

    def to_dataset(self) -> Dataset:
        return self._dataset

    @classmethod
    def from_dataset(cls, dataset: Dataset):
        control_point = cls()
        control_point._dataset = dataset
        return control_point

    def validate(self) -> List[str]:
        errors = []

        # Check Type 1 elements
        type1_elements = ["ControlPointIndex", "NominalBeamEnergy"]
        for elem in type1_elements:
            if not hasattr(self._dataset, elem):
                errors.append(f"{elem} is missing")
            elif getattr(self._dataset, elem) is None:
                errors.append(f"{elem} has no value assigned")

        return errors
