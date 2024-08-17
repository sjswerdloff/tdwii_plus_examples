from typing import Any, List, Optional

import pydicom

from .flat_keratometric_axis_sequence_item import FlatKeratometricAxisSequenceItem
from .steep_keratometric_axis_sequence_item import SteepKeratometricAxisSequenceItem


class KeratometryLeftEyeSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._SteepKeratometricAxisSequence: List[SteepKeratometricAxisSequenceItem] = []
        self._FlatKeratometricAxisSequence: List[FlatKeratometricAxisSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def SteepKeratometricAxisSequence(self) -> Optional[List[SteepKeratometricAxisSequenceItem]]:
        if "SteepKeratometricAxisSequence" in self._dataset:
            if len(self._SteepKeratometricAxisSequence) == len(self._dataset.SteepKeratometricAxisSequence):
                return self._SteepKeratometricAxisSequence
            else:
                return [SteepKeratometricAxisSequenceItem(x) for x in self._dataset.SteepKeratometricAxisSequence]
        return None

    @SteepKeratometricAxisSequence.setter
    def SteepKeratometricAxisSequence(self, value: Optional[List[SteepKeratometricAxisSequenceItem]]):
        if value is None:
            self._SteepKeratometricAxisSequence = []
            if "SteepKeratometricAxisSequence" in self._dataset:
                del self._dataset.SteepKeratometricAxisSequence
        elif not isinstance(value, list) or not all(isinstance(item, SteepKeratometricAxisSequenceItem) for item in value):
            raise ValueError(f"SteepKeratometricAxisSequence must be a list of SteepKeratometricAxisSequenceItem objects")
        else:
            self._SteepKeratometricAxisSequence = value
            if "SteepKeratometricAxisSequence" not in self._dataset:
                self._dataset.SteepKeratometricAxisSequence = pydicom.Sequence()
            self._dataset.SteepKeratometricAxisSequence.clear()
            self._dataset.SteepKeratometricAxisSequence.extend([item.to_dataset() for item in value])

    def add_SteepKeratometricAxis(self, item: SteepKeratometricAxisSequenceItem):
        if not isinstance(item, SteepKeratometricAxisSequenceItem):
            raise ValueError(f"Item must be an instance of SteepKeratometricAxisSequenceItem")
        self._SteepKeratometricAxisSequence.append(item)
        if "SteepKeratometricAxisSequence" not in self._dataset:
            self._dataset.SteepKeratometricAxisSequence = pydicom.Sequence()
        self._dataset.SteepKeratometricAxisSequence.append(item.to_dataset())

    @property
    def FlatKeratometricAxisSequence(self) -> Optional[List[FlatKeratometricAxisSequenceItem]]:
        if "FlatKeratometricAxisSequence" in self._dataset:
            if len(self._FlatKeratometricAxisSequence) == len(self._dataset.FlatKeratometricAxisSequence):
                return self._FlatKeratometricAxisSequence
            else:
                return [FlatKeratometricAxisSequenceItem(x) for x in self._dataset.FlatKeratometricAxisSequence]
        return None

    @FlatKeratometricAxisSequence.setter
    def FlatKeratometricAxisSequence(self, value: Optional[List[FlatKeratometricAxisSequenceItem]]):
        if value is None:
            self._FlatKeratometricAxisSequence = []
            if "FlatKeratometricAxisSequence" in self._dataset:
                del self._dataset.FlatKeratometricAxisSequence
        elif not isinstance(value, list) or not all(isinstance(item, FlatKeratometricAxisSequenceItem) for item in value):
            raise ValueError(f"FlatKeratometricAxisSequence must be a list of FlatKeratometricAxisSequenceItem objects")
        else:
            self._FlatKeratometricAxisSequence = value
            if "FlatKeratometricAxisSequence" not in self._dataset:
                self._dataset.FlatKeratometricAxisSequence = pydicom.Sequence()
            self._dataset.FlatKeratometricAxisSequence.clear()
            self._dataset.FlatKeratometricAxisSequence.extend([item.to_dataset() for item in value])

    def add_FlatKeratometricAxis(self, item: FlatKeratometricAxisSequenceItem):
        if not isinstance(item, FlatKeratometricAxisSequenceItem):
            raise ValueError(f"Item must be an instance of FlatKeratometricAxisSequenceItem")
        self._FlatKeratometricAxisSequence.append(item)
        if "FlatKeratometricAxisSequence" not in self._dataset:
            self._dataset.FlatKeratometricAxisSequence = pydicom.Sequence()
        self._dataset.FlatKeratometricAxisSequence.append(item.to_dataset())
