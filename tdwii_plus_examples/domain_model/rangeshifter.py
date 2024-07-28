from typing import List, Optional, Union

from pydicom.dataset import Dataset


class RangeShifter:
    def __init__(self):
        self._dataset = Dataset()

    @property
    def range_shifter_id(self) -> str:
        return self._dataset.RangeShifterID

    @range_shifter_id.setter
    def range_shifter_id(self, value: str):
        self._dataset.RangeShifterID = value

    @property
    def range_shifter_type(self) -> str:
        return self._dataset.RangeShifterType

    @range_shifter_type.setter
    def range_shifter_type(self, value: str):
        self._dataset.RangeShifterType = value

    def to_dataset(self) -> Dataset:
        return self._dataset

    @classmethod
    def from_dataset(cls, dataset: Dataset):
        range_shifter = cls()
        range_shifter._dataset = dataset
        return range_shifter

    def validate(self) -> List[str]:
        errors = []

        # Check Type 1 elements
        type1_elements = ["RangeShifterID", "RangeShifterType"]
        for elem in type1_elements:
            if not hasattr(self._dataset, elem):
                errors.append(f"{elem} is missing")
            elif getattr(self._dataset, elem) is None:
                errors.append(f"{elem} has no value assigned")

        return errors
