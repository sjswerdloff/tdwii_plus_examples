from typing import Any, List, Optional  # noqa

import pydicom

from .threshold_value_sequence_item import ThresholdValueSequenceItem


class ThresholdSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._ThresholdValueSequence: List[ThresholdValueSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ThresholdValueSequence(self) -> Optional[List[ThresholdValueSequenceItem]]:
        if "ThresholdValueSequence" in self._dataset:
            if len(self._ThresholdValueSequence) == len(self._dataset.ThresholdValueSequence):
                return self._ThresholdValueSequence
            else:
                return [ThresholdValueSequenceItem(x) for x in self._dataset.ThresholdValueSequence]
        return None

    @ThresholdValueSequence.setter
    def ThresholdValueSequence(self, value: Optional[List[ThresholdValueSequenceItem]]):
        if value is None:
            self._ThresholdValueSequence = []
            if "ThresholdValueSequence" in self._dataset:
                del self._dataset.ThresholdValueSequence
        elif not isinstance(value, list) or not all(isinstance(item, ThresholdValueSequenceItem) for item in value):
            raise ValueError("ThresholdValueSequence must be a list of ThresholdValueSequenceItem objects")
        else:
            self._ThresholdValueSequence = value
            if "ThresholdValueSequence" not in self._dataset:
                self._dataset.ThresholdValueSequence = pydicom.Sequence()
            self._dataset.ThresholdValueSequence.clear()
            self._dataset.ThresholdValueSequence.extend([item.to_dataset() for item in value])

    def add_ThresholdValue(self, item: ThresholdValueSequenceItem):
        if not isinstance(item, ThresholdValueSequenceItem):
            raise ValueError("Item must be an instance of ThresholdValueSequenceItem")
        self._ThresholdValueSequence.append(item)
        if "ThresholdValueSequence" not in self._dataset:
            self._dataset.ThresholdValueSequence = pydicom.Sequence()
        self._dataset.ThresholdValueSequence.append(item.to_dataset())

    @property
    def ThresholdType(self) -> Optional[str]:
        if "ThresholdType" in self._dataset:
            return self._dataset.ThresholdType
        return None

    @ThresholdType.setter
    def ThresholdType(self, value: Optional[str]):
        if value is None:
            if "ThresholdType" in self._dataset:
                del self._dataset.ThresholdType
        else:
            self._dataset.ThresholdType = value
