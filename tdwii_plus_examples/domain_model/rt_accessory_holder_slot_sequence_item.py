from typing import Any, List, Optional  # noqa

import pydicom


class RTAccessoryHolderSlotSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def RTAccessoryHolderSlotID(self) -> Optional[str]:
        if "RTAccessoryHolderSlotID" in self._dataset:
            return self._dataset.RTAccessoryHolderSlotID
        return None

    @RTAccessoryHolderSlotID.setter
    def RTAccessoryHolderSlotID(self, value: Optional[str]):
        if value is None:
            if "RTAccessoryHolderSlotID" in self._dataset:
                del self._dataset.RTAccessoryHolderSlotID
        else:
            self._dataset.RTAccessoryHolderSlotID = value

    @property
    def RTAccessoryHolderSlotDistance(self) -> Optional[float]:
        if "RTAccessoryHolderSlotDistance" in self._dataset:
            return self._dataset.RTAccessoryHolderSlotDistance
        return None

    @RTAccessoryHolderSlotDistance.setter
    def RTAccessoryHolderSlotDistance(self, value: Optional[float]):
        if value is None:
            if "RTAccessoryHolderSlotDistance" in self._dataset:
                del self._dataset.RTAccessoryHolderSlotDistance
        else:
            self._dataset.RTAccessoryHolderSlotDistance = value
