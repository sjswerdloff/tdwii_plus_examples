from typing import Any, List, Optional  # noqa

import pydicom

from .code_sequence_item import CodeSequenceItem


class AlternateContentDescriptionSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._LanguageCodeSequence: List[CodeSequenceItem] = []
        self._ConceptNameCodeSequence: List[CodeSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def LanguageCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "LanguageCodeSequence" in self._dataset:
            if len(self._LanguageCodeSequence) == len(self._dataset.LanguageCodeSequence):
                return self._LanguageCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.LanguageCodeSequence]
        return None

    @LanguageCodeSequence.setter
    def LanguageCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._LanguageCodeSequence = []
            if "LanguageCodeSequence" in self._dataset:
                del self._dataset.LanguageCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("LanguageCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._LanguageCodeSequence = value
            if "LanguageCodeSequence" not in self._dataset:
                self._dataset.LanguageCodeSequence = pydicom.Sequence()
            self._dataset.LanguageCodeSequence.clear()
            self._dataset.LanguageCodeSequence.extend([item.to_dataset() for item in value])

    def add_LanguageCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._LanguageCodeSequence.append(item)
        if "LanguageCodeSequence" not in self._dataset:
            self._dataset.LanguageCodeSequence = pydicom.Sequence()
        self._dataset.LanguageCodeSequence.append(item.to_dataset())

    @property
    def ConceptNameCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "ConceptNameCodeSequence" in self._dataset:
            if len(self._ConceptNameCodeSequence) == len(self._dataset.ConceptNameCodeSequence):
                return self._ConceptNameCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.ConceptNameCodeSequence]
        return None

    @ConceptNameCodeSequence.setter
    def ConceptNameCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._ConceptNameCodeSequence = []
            if "ConceptNameCodeSequence" in self._dataset:
                del self._dataset.ConceptNameCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("ConceptNameCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._ConceptNameCodeSequence = value
            if "ConceptNameCodeSequence" not in self._dataset:
                self._dataset.ConceptNameCodeSequence = pydicom.Sequence()
            self._dataset.ConceptNameCodeSequence.clear()
            self._dataset.ConceptNameCodeSequence.extend([item.to_dataset() for item in value])

    def add_ConceptNameCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._ConceptNameCodeSequence.append(item)
        if "ConceptNameCodeSequence" not in self._dataset:
            self._dataset.ConceptNameCodeSequence = pydicom.Sequence()
        self._dataset.ConceptNameCodeSequence.append(item.to_dataset())

    @property
    def ContentDescription(self) -> Optional[str]:
        if "ContentDescription" in self._dataset:
            return self._dataset.ContentDescription
        return None

    @ContentDescription.setter
    def ContentDescription(self, value: Optional[str]):
        if value is None:
            if "ContentDescription" in self._dataset:
                del self._dataset.ContentDescription
        else:
            self._dataset.ContentDescription = value
