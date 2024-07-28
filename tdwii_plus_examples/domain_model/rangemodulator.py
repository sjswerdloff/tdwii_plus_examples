from typing import List, Optional, Union

from pydicom.dataset import Dataset


class RangeModulator:
    def __init__(self):
        self._dataset = Dataset()

    @property
    def range_modulator_id(self) -> str:
        return self._dataset.RangeModulatorID

    @range_modulator_id.setter
    def range_modulator_id(self, value: str):
        self._dataset.RangeModulatorID = value

    @property
    def range_modulator_type(self) -> str:
        return self._dataset.RangeModulatorType

    @range_modulator_type.setter
    def range_modulator_type(self, value: str):
        self._dataset.RangeModulatorType = value

    def to_dataset(self) -> Dataset:
        return self._dataset

    @classmethod
    def from_dataset(cls, dataset: Dataset):
        modulator = cls()
        modulator._dataset = dataset
        return modulator

    def validate(self) -> List[str]:
        errors = []

        # Check Type 1 elements
        type1_elements = ["RangeModulatorID", "RangeModulatorType"]
        for elem in type1_elements:
            if not hasattr(self._dataset, elem):
                errors.append(f"{elem} is missing")
            elif getattr(self._dataset, elem) is None:
                errors.append(f"{elem} has no value assigned")

        return errors
