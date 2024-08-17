from typing import Any, List, Optional

import pydicom

from .energy_window_range_sequence_item import EnergyWindowRangeSequenceItem


class EnergyWindowInformationSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._EnergyWindowRangeSequence: List[EnergyWindowRangeSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def EnergyWindowRangeSequence(self) -> Optional[List[EnergyWindowRangeSequenceItem]]:
        if "EnergyWindowRangeSequence" in self._dataset:
            if len(self._EnergyWindowRangeSequence) == len(self._dataset.EnergyWindowRangeSequence):
                return self._EnergyWindowRangeSequence
            else:
                return [EnergyWindowRangeSequenceItem(x) for x in self._dataset.EnergyWindowRangeSequence]
        return None

    @EnergyWindowRangeSequence.setter
    def EnergyWindowRangeSequence(self, value: Optional[List[EnergyWindowRangeSequenceItem]]):
        if value is None:
            self._EnergyWindowRangeSequence = []
            if "EnergyWindowRangeSequence" in self._dataset:
                del self._dataset.EnergyWindowRangeSequence
        elif not isinstance(value, list) or not all(isinstance(item, EnergyWindowRangeSequenceItem) for item in value):
            raise ValueError(f"EnergyWindowRangeSequence must be a list of EnergyWindowRangeSequenceItem objects")
        else:
            self._EnergyWindowRangeSequence = value
            if "EnergyWindowRangeSequence" not in self._dataset:
                self._dataset.EnergyWindowRangeSequence = pydicom.Sequence()
            self._dataset.EnergyWindowRangeSequence.clear()
            self._dataset.EnergyWindowRangeSequence.extend([item.to_dataset() for item in value])

    def add_EnergyWindowRange(self, item: EnergyWindowRangeSequenceItem):
        if not isinstance(item, EnergyWindowRangeSequenceItem):
            raise ValueError(f"Item must be an instance of EnergyWindowRangeSequenceItem")
        self._EnergyWindowRangeSequence.append(item)
        if "EnergyWindowRangeSequence" not in self._dataset:
            self._dataset.EnergyWindowRangeSequence = pydicom.Sequence()
        self._dataset.EnergyWindowRangeSequence.append(item.to_dataset())

    @property
    def EnergyWindowName(self) -> Optional[str]:
        if "EnergyWindowName" in self._dataset:
            return self._dataset.EnergyWindowName
        return None

    @EnergyWindowName.setter
    def EnergyWindowName(self, value: Optional[str]):
        if value is None:
            if "EnergyWindowName" in self._dataset:
                del self._dataset.EnergyWindowName
        else:
            self._dataset.EnergyWindowName = value
