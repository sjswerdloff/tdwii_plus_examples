from typing import Any, List, Optional  # noqa

import pydicom

from .code_sequence_item import CodeSequenceItem


class GeneticModificationsSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._GeneticModificationsCodeSequence: List[CodeSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def GeneticModificationsDescription(self) -> Optional[str]:
        if "GeneticModificationsDescription" in self._dataset:
            return self._dataset.GeneticModificationsDescription
        return None

    @GeneticModificationsDescription.setter
    def GeneticModificationsDescription(self, value: Optional[str]):
        if value is None:
            if "GeneticModificationsDescription" in self._dataset:
                del self._dataset.GeneticModificationsDescription
        else:
            self._dataset.GeneticModificationsDescription = value

    @property
    def GeneticModificationsNomenclature(self) -> Optional[str]:
        if "GeneticModificationsNomenclature" in self._dataset:
            return self._dataset.GeneticModificationsNomenclature
        return None

    @GeneticModificationsNomenclature.setter
    def GeneticModificationsNomenclature(self, value: Optional[str]):
        if value is None:
            if "GeneticModificationsNomenclature" in self._dataset:
                del self._dataset.GeneticModificationsNomenclature
        else:
            self._dataset.GeneticModificationsNomenclature = value

    @property
    def GeneticModificationsCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "GeneticModificationsCodeSequence" in self._dataset:
            if len(self._GeneticModificationsCodeSequence) == len(self._dataset.GeneticModificationsCodeSequence):
                return self._GeneticModificationsCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.GeneticModificationsCodeSequence]
        return None

    @GeneticModificationsCodeSequence.setter
    def GeneticModificationsCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._GeneticModificationsCodeSequence = []
            if "GeneticModificationsCodeSequence" in self._dataset:
                del self._dataset.GeneticModificationsCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("GeneticModificationsCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._GeneticModificationsCodeSequence = value
            if "GeneticModificationsCodeSequence" not in self._dataset:
                self._dataset.GeneticModificationsCodeSequence = pydicom.Sequence()
            self._dataset.GeneticModificationsCodeSequence.clear()
            self._dataset.GeneticModificationsCodeSequence.extend([item.to_dataset() for item in value])

    def add_GeneticModificationsCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._GeneticModificationsCodeSequence.append(item)
        if "GeneticModificationsCodeSequence" not in self._dataset:
            self._dataset.GeneticModificationsCodeSequence = pydicom.Sequence()
        self._dataset.GeneticModificationsCodeSequence.append(item.to_dataset())
