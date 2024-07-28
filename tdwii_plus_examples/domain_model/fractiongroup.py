# fraction_group_sequence.py

from typing import List, Optional

from pydicom.dataset import Dataset


class FractionGroup:
    def __init__(self):
        self._dataset = Dataset()

    # Type 1 elements
    @property
    def fraction_group_number(self) -> int:
        return self._dataset.FractionGroupNumber

    @fraction_group_number.setter
    def fraction_group_number(self, value: int):
        self._dataset.FractionGroupNumber = value

    @property
    def number_of_fractions_planned(self) -> int:
        return self._dataset.NumberOfFractionsPlanned

    @number_of_fractions_planned.setter
    def number_of_fractions_planned(self, value: int):
        self._dataset.NumberOfFractionsPlanned = value

    # Type 2 elements
    @property
    def number_of_beams(self) -> int:
        return self._dataset.NumberOfBeams

    @number_of_beams.setter
    def number_of_beams(self, value: int):
        self._dataset.NumberOfBeams = value

    @property
    def number_of_brachy_application_setups(self) -> int:
        return self._dataset.NumberOfBrachyApplicationSetups

    @number_of_brachy_application_setups.setter
    def number_of_brachy_application_setups(self, value: int):
        self._dataset.NumberOfBrachyApplicationSetups = value

    # Type 3 elements
    @property
    def fraction_group_description(self) -> Optional[str]:
        return self._dataset.get("FractionGroupDescription")

    @fraction_group_description.setter
    def fraction_group_description(self, value: Optional[str]):
        if value is not None:
            self._dataset.FractionGroupDescription = value

    @property
    def fraction_pattern(self) -> Optional[str]:
        return self._dataset.get("FractionPattern")

    @fraction_pattern.setter
    def fraction_pattern(self, value: Optional[str]):
        if value is not None:
            self._dataset.FractionPattern = value

    def to_dataset(self) -> Dataset:
        return self._dataset

    @classmethod
    def from_dataset(cls, dataset: Dataset):
        fraction_group = cls()
        fraction_group._dataset = dataset
        return fraction_group

    def validate(self) -> List[str]:
        errors = []

        # Check Type 1 elements
        if not hasattr(self._dataset, "FractionGroupNumber"):
            errors.append("FractionGroupNumber is missing")
        if not hasattr(self._dataset, "NumberOfFractionsPlanned"):
            errors.append("NumberOfFractionsPlanned is missing")

        # Check Type 2 elements
        if not hasattr(self._dataset, "NumberOfBeams"):
            errors.append("NumberOfBeams is missing")
        if not hasattr(self._dataset, "NumberOfBrachyApplicationSetups"):
            errors.append("NumberOfBrachyApplicationSetups is missing")

        return errors
