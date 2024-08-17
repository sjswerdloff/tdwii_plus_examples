from typing import Any, List, Optional  # noqa

import pydicom

from .chemical_shift_sequence_item import ChemicalShiftSequenceItem
from .code_sequence_item import CodeSequenceItem


class MRMetaboliteMapSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._MetaboliteMapCodeSequence: List[CodeSequenceItem] = []
        self._ChemicalShiftSequence: List[ChemicalShiftSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def MetaboliteMapDescription(self) -> Optional[str]:
        if "MetaboliteMapDescription" in self._dataset:
            return self._dataset.MetaboliteMapDescription
        return None

    @MetaboliteMapDescription.setter
    def MetaboliteMapDescription(self, value: Optional[str]):
        if value is None:
            if "MetaboliteMapDescription" in self._dataset:
                del self._dataset.MetaboliteMapDescription
        else:
            self._dataset.MetaboliteMapDescription = value

    @property
    def MetaboliteMapCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "MetaboliteMapCodeSequence" in self._dataset:
            if len(self._MetaboliteMapCodeSequence) == len(self._dataset.MetaboliteMapCodeSequence):
                return self._MetaboliteMapCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.MetaboliteMapCodeSequence]
        return None

    @MetaboliteMapCodeSequence.setter
    def MetaboliteMapCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._MetaboliteMapCodeSequence = []
            if "MetaboliteMapCodeSequence" in self._dataset:
                del self._dataset.MetaboliteMapCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("MetaboliteMapCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._MetaboliteMapCodeSequence = value
            if "MetaboliteMapCodeSequence" not in self._dataset:
                self._dataset.MetaboliteMapCodeSequence = pydicom.Sequence()
            self._dataset.MetaboliteMapCodeSequence.clear()
            self._dataset.MetaboliteMapCodeSequence.extend([item.to_dataset() for item in value])

    def add_MetaboliteMapCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._MetaboliteMapCodeSequence.append(item)
        if "MetaboliteMapCodeSequence" not in self._dataset:
            self._dataset.MetaboliteMapCodeSequence = pydicom.Sequence()
        self._dataset.MetaboliteMapCodeSequence.append(item.to_dataset())

    @property
    def ChemicalShiftSequence(self) -> Optional[List[ChemicalShiftSequenceItem]]:
        if "ChemicalShiftSequence" in self._dataset:
            if len(self._ChemicalShiftSequence) == len(self._dataset.ChemicalShiftSequence):
                return self._ChemicalShiftSequence
            else:
                return [ChemicalShiftSequenceItem(x) for x in self._dataset.ChemicalShiftSequence]
        return None

    @ChemicalShiftSequence.setter
    def ChemicalShiftSequence(self, value: Optional[List[ChemicalShiftSequenceItem]]):
        if value is None:
            self._ChemicalShiftSequence = []
            if "ChemicalShiftSequence" in self._dataset:
                del self._dataset.ChemicalShiftSequence
        elif not isinstance(value, list) or not all(isinstance(item, ChemicalShiftSequenceItem) for item in value):
            raise ValueError("ChemicalShiftSequence must be a list of ChemicalShiftSequenceItem objects")
        else:
            self._ChemicalShiftSequence = value
            if "ChemicalShiftSequence" not in self._dataset:
                self._dataset.ChemicalShiftSequence = pydicom.Sequence()
            self._dataset.ChemicalShiftSequence.clear()
            self._dataset.ChemicalShiftSequence.extend([item.to_dataset() for item in value])

    def add_ChemicalShift(self, item: ChemicalShiftSequenceItem):
        if not isinstance(item, ChemicalShiftSequenceItem):
            raise ValueError("Item must be an instance of ChemicalShiftSequenceItem")
        self._ChemicalShiftSequence.append(item)
        if "ChemicalShiftSequence" not in self._dataset:
            self._dataset.ChemicalShiftSequence = pydicom.Sequence()
        self._dataset.ChemicalShiftSequence.append(item.to_dataset())
