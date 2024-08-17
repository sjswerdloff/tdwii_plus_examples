from typing import Any, List, Optional  # noqa

import pydicom

from .rt_referenced_study_sequence_item import RTReferencedStudySequenceItem


class ReferencedFrameOfReferenceSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._RTReferencedStudySequence: List[RTReferencedStudySequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def FrameOfReferenceUID(self) -> Optional[str]:
        if "FrameOfReferenceUID" in self._dataset:
            return self._dataset.FrameOfReferenceUID
        return None

    @FrameOfReferenceUID.setter
    def FrameOfReferenceUID(self, value: Optional[str]):
        if value is None:
            if "FrameOfReferenceUID" in self._dataset:
                del self._dataset.FrameOfReferenceUID
        else:
            self._dataset.FrameOfReferenceUID = value

    @property
    def RTReferencedStudySequence(self) -> Optional[List[RTReferencedStudySequenceItem]]:
        if "RTReferencedStudySequence" in self._dataset:
            if len(self._RTReferencedStudySequence) == len(self._dataset.RTReferencedStudySequence):
                return self._RTReferencedStudySequence
            else:
                return [RTReferencedStudySequenceItem(x) for x in self._dataset.RTReferencedStudySequence]
        return None

    @RTReferencedStudySequence.setter
    def RTReferencedStudySequence(self, value: Optional[List[RTReferencedStudySequenceItem]]):
        if value is None:
            self._RTReferencedStudySequence = []
            if "RTReferencedStudySequence" in self._dataset:
                del self._dataset.RTReferencedStudySequence
        elif not isinstance(value, list) or not all(isinstance(item, RTReferencedStudySequenceItem) for item in value):
            raise ValueError("RTReferencedStudySequence must be a list of RTReferencedStudySequenceItem objects")
        else:
            self._RTReferencedStudySequence = value
            if "RTReferencedStudySequence" not in self._dataset:
                self._dataset.RTReferencedStudySequence = pydicom.Sequence()
            self._dataset.RTReferencedStudySequence.clear()
            self._dataset.RTReferencedStudySequence.extend([item.to_dataset() for item in value])

    def add_RTReferencedStudy(self, item: RTReferencedStudySequenceItem):
        if not isinstance(item, RTReferencedStudySequenceItem):
            raise ValueError("Item must be an instance of RTReferencedStudySequenceItem")
        self._RTReferencedStudySequence.append(item)
        if "RTReferencedStudySequence" not in self._dataset:
            self._dataset.RTReferencedStudySequence = pydicom.Sequence()
        self._dataset.RTReferencedStudySequence.append(item.to_dataset())
