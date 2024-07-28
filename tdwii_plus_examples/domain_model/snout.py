from typing import List, Optional, Union

from pydicom.dataset import Dataset


class Snout:
    def __init__(self):
        self._dataset = Dataset()

    @property
    def snout_id(self) -> str:
        return self._dataset.SnoutID

    @snout_id.setter
    def snout_id(self, value: str):
        self._dataset.SnoutID = value

    def to_dataset(self) -> Dataset:
        return self._dataset

    @classmethod
    def from_dataset(cls, dataset: Dataset):
        snout = cls()
        snout._dataset = dataset
        return snout

    def validate(self) -> List[str]:
        errors = []

        # Check Type 1 elements
        type1_elements = ["SnoutID"]
        for elem in type1_elements:
            if not hasattr(self._dataset, elem):
                errors.append(f"{elem} is missing")
            elif getattr(self._dataset, elem) is None:
                errors.append(f"{elem} has no value assigned")

        return errors
