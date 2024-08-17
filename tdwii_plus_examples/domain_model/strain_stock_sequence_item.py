from typing import Any, List, Optional  # noqa

import pydicom

from .code_sequence_item import CodeSequenceItem


class StrainStockSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._StrainSourceRegistryCodeSequence: List[CodeSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def StrainStockNumber(self) -> Optional[str]:
        if "StrainStockNumber" in self._dataset:
            return self._dataset.StrainStockNumber
        return None

    @StrainStockNumber.setter
    def StrainStockNumber(self, value: Optional[str]):
        if value is None:
            if "StrainStockNumber" in self._dataset:
                del self._dataset.StrainStockNumber
        else:
            self._dataset.StrainStockNumber = value

    @property
    def StrainSourceRegistryCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "StrainSourceRegistryCodeSequence" in self._dataset:
            if len(self._StrainSourceRegistryCodeSequence) == len(self._dataset.StrainSourceRegistryCodeSequence):
                return self._StrainSourceRegistryCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.StrainSourceRegistryCodeSequence]
        return None

    @StrainSourceRegistryCodeSequence.setter
    def StrainSourceRegistryCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._StrainSourceRegistryCodeSequence = []
            if "StrainSourceRegistryCodeSequence" in self._dataset:
                del self._dataset.StrainSourceRegistryCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("StrainSourceRegistryCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._StrainSourceRegistryCodeSequence = value
            if "StrainSourceRegistryCodeSequence" not in self._dataset:
                self._dataset.StrainSourceRegistryCodeSequence = pydicom.Sequence()
            self._dataset.StrainSourceRegistryCodeSequence.clear()
            self._dataset.StrainSourceRegistryCodeSequence.extend([item.to_dataset() for item in value])

    def add_StrainSourceRegistryCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._StrainSourceRegistryCodeSequence.append(item)
        if "StrainSourceRegistryCodeSequence" not in self._dataset:
            self._dataset.StrainSourceRegistryCodeSequence = pydicom.Sequence()
        self._dataset.StrainSourceRegistryCodeSequence.append(item.to_dataset())

    @property
    def StrainSource(self) -> Optional[str]:
        if "StrainSource" in self._dataset:
            return self._dataset.StrainSource
        return None

    @StrainSource.setter
    def StrainSource(self, value: Optional[str]):
        if value is None:
            if "StrainSource" in self._dataset:
                del self._dataset.StrainSource
        else:
            self._dataset.StrainSource = value
