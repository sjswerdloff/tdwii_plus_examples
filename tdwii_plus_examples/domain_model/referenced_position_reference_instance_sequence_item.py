from typing import Any, List, Optional

import pydicom

from .code_sequence_item import CodeSequenceItem
from .referenced_study_sequence_item import ReferencedStudySequenceItem


class ReferencedPositionReferenceInstanceSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._ReferencedStudySequence: List[ReferencedStudySequenceItem] = []
        self._PurposeOfReferenceCodeSequence: List[CodeSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ReferencedStudySequence(self) -> Optional[List[ReferencedStudySequenceItem]]:
        if "ReferencedStudySequence" in self._dataset:
            if len(self._ReferencedStudySequence) == len(self._dataset.ReferencedStudySequence):
                return self._ReferencedStudySequence
            else:
                return [ReferencedStudySequenceItem(x) for x in self._dataset.ReferencedStudySequence]
        return None

    @ReferencedStudySequence.setter
    def ReferencedStudySequence(self, value: Optional[List[ReferencedStudySequenceItem]]):
        if value is None:
            self._ReferencedStudySequence = []
            if "ReferencedStudySequence" in self._dataset:
                del self._dataset.ReferencedStudySequence
        elif not isinstance(value, list) or not all(isinstance(item, ReferencedStudySequenceItem) for item in value):
            raise ValueError(f"ReferencedStudySequence must be a list of ReferencedStudySequenceItem objects")
        else:
            self._ReferencedStudySequence = value
            if "ReferencedStudySequence" not in self._dataset:
                self._dataset.ReferencedStudySequence = pydicom.Sequence()
            self._dataset.ReferencedStudySequence.clear()
            self._dataset.ReferencedStudySequence.extend([item.to_dataset() for item in value])

    def add_ReferencedStudy(self, item: ReferencedStudySequenceItem):
        if not isinstance(item, ReferencedStudySequenceItem):
            raise ValueError(f"Item must be an instance of ReferencedStudySequenceItem")
        self._ReferencedStudySequence.append(item)
        if "ReferencedStudySequence" not in self._dataset:
            self._dataset.ReferencedStudySequence = pydicom.Sequence()
        self._dataset.ReferencedStudySequence.append(item.to_dataset())

    @property
    def PurposeOfReferenceCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "PurposeOfReferenceCodeSequence" in self._dataset:
            if len(self._PurposeOfReferenceCodeSequence) == len(self._dataset.PurposeOfReferenceCodeSequence):
                return self._PurposeOfReferenceCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.PurposeOfReferenceCodeSequence]
        return None

    @PurposeOfReferenceCodeSequence.setter
    def PurposeOfReferenceCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._PurposeOfReferenceCodeSequence = []
            if "PurposeOfReferenceCodeSequence" in self._dataset:
                del self._dataset.PurposeOfReferenceCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError(f"PurposeOfReferenceCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._PurposeOfReferenceCodeSequence = value
            if "PurposeOfReferenceCodeSequence" not in self._dataset:
                self._dataset.PurposeOfReferenceCodeSequence = pydicom.Sequence()
            self._dataset.PurposeOfReferenceCodeSequence.clear()
            self._dataset.PurposeOfReferenceCodeSequence.extend([item.to_dataset() for item in value])

    def add_PurposeOfReferenceCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError(f"Item must be an instance of CodeSequenceItem")
        self._PurposeOfReferenceCodeSequence.append(item)
        if "PurposeOfReferenceCodeSequence" not in self._dataset:
            self._dataset.PurposeOfReferenceCodeSequence = pydicom.Sequence()
        self._dataset.PurposeOfReferenceCodeSequence.append(item.to_dataset())
