from typing import Any, List, Optional  # noqa

import pydicom

from .code_sequence_item import CodeSequenceItem


class CustodialOrganizationSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._InstitutionCodeSequence: List[CodeSequenceItem] = []
        self._ResponsibleGroupCodeSequence: List[CodeSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def InstitutionName(self) -> Optional[str]:
        if "InstitutionName" in self._dataset:
            return self._dataset.InstitutionName
        return None

    @InstitutionName.setter
    def InstitutionName(self, value: Optional[str]):
        if value is None:
            if "InstitutionName" in self._dataset:
                del self._dataset.InstitutionName
        else:
            self._dataset.InstitutionName = value

    @property
    def InstitutionCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "InstitutionCodeSequence" in self._dataset:
            if len(self._InstitutionCodeSequence) == len(self._dataset.InstitutionCodeSequence):
                return self._InstitutionCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.InstitutionCodeSequence]
        return None

    @InstitutionCodeSequence.setter
    def InstitutionCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._InstitutionCodeSequence = []
            if "InstitutionCodeSequence" in self._dataset:
                del self._dataset.InstitutionCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("InstitutionCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._InstitutionCodeSequence = value
            if "InstitutionCodeSequence" not in self._dataset:
                self._dataset.InstitutionCodeSequence = pydicom.Sequence()
            self._dataset.InstitutionCodeSequence.clear()
            self._dataset.InstitutionCodeSequence.extend([item.to_dataset() for item in value])

    def add_InstitutionCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._InstitutionCodeSequence.append(item)
        if "InstitutionCodeSequence" not in self._dataset:
            self._dataset.InstitutionCodeSequence = pydicom.Sequence()
        self._dataset.InstitutionCodeSequence.append(item.to_dataset())

    @property
    def ResponsibleGroupCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "ResponsibleGroupCodeSequence" in self._dataset:
            if len(self._ResponsibleGroupCodeSequence) == len(self._dataset.ResponsibleGroupCodeSequence):
                return self._ResponsibleGroupCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.ResponsibleGroupCodeSequence]
        return None

    @ResponsibleGroupCodeSequence.setter
    def ResponsibleGroupCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._ResponsibleGroupCodeSequence = []
            if "ResponsibleGroupCodeSequence" in self._dataset:
                del self._dataset.ResponsibleGroupCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("ResponsibleGroupCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._ResponsibleGroupCodeSequence = value
            if "ResponsibleGroupCodeSequence" not in self._dataset:
                self._dataset.ResponsibleGroupCodeSequence = pydicom.Sequence()
            self._dataset.ResponsibleGroupCodeSequence.clear()
            self._dataset.ResponsibleGroupCodeSequence.extend([item.to_dataset() for item in value])

    def add_ResponsibleGroupCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._ResponsibleGroupCodeSequence.append(item)
        if "ResponsibleGroupCodeSequence" not in self._dataset:
            self._dataset.ResponsibleGroupCodeSequence = pydicom.Sequence()
        self._dataset.ResponsibleGroupCodeSequence.append(item.to_dataset())
