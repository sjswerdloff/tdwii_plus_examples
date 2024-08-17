from typing import Any, List, Optional  # noqa

import pydicom

from .code_sequence_item import CodeSequenceItem


class BreedRegistrationSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._BreedRegistryCodeSequence: List[CodeSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def BreedRegistrationNumber(self) -> Optional[str]:
        if "BreedRegistrationNumber" in self._dataset:
            return self._dataset.BreedRegistrationNumber
        return None

    @BreedRegistrationNumber.setter
    def BreedRegistrationNumber(self, value: Optional[str]):
        if value is None:
            if "BreedRegistrationNumber" in self._dataset:
                del self._dataset.BreedRegistrationNumber
        else:
            self._dataset.BreedRegistrationNumber = value

    @property
    def BreedRegistryCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "BreedRegistryCodeSequence" in self._dataset:
            if len(self._BreedRegistryCodeSequence) == len(self._dataset.BreedRegistryCodeSequence):
                return self._BreedRegistryCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.BreedRegistryCodeSequence]
        return None

    @BreedRegistryCodeSequence.setter
    def BreedRegistryCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._BreedRegistryCodeSequence = []
            if "BreedRegistryCodeSequence" in self._dataset:
                del self._dataset.BreedRegistryCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("BreedRegistryCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._BreedRegistryCodeSequence = value
            if "BreedRegistryCodeSequence" not in self._dataset:
                self._dataset.BreedRegistryCodeSequence = pydicom.Sequence()
            self._dataset.BreedRegistryCodeSequence.clear()
            self._dataset.BreedRegistryCodeSequence.extend([item.to_dataset() for item in value])

    def add_BreedRegistryCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._BreedRegistryCodeSequence.append(item)
        if "BreedRegistryCodeSequence" not in self._dataset:
            self._dataset.BreedRegistryCodeSequence = pydicom.Sequence()
        self._dataset.BreedRegistryCodeSequence.append(item.to_dataset())
