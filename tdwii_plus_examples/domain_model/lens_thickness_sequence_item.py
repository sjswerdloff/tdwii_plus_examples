from typing import Any, List, Optional  # noqa

import pydicom

from .code_sequence_item import CodeSequenceItem
from .referenced_sop_sequence_item import ReferencedSOPSequenceItem


class LensThicknessSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._ReferencedSOPSequence: List[ReferencedSOPSequenceItem] = []
        self._SourceOfLensThicknessDataCodeSequence: List[CodeSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ReferencedSOPSequence(self) -> Optional[List[ReferencedSOPSequenceItem]]:
        if "ReferencedSOPSequence" in self._dataset:
            if len(self._ReferencedSOPSequence) == len(self._dataset.ReferencedSOPSequence):
                return self._ReferencedSOPSequence
            else:
                return [ReferencedSOPSequenceItem(x) for x in self._dataset.ReferencedSOPSequence]
        return None

    @ReferencedSOPSequence.setter
    def ReferencedSOPSequence(self, value: Optional[List[ReferencedSOPSequenceItem]]):
        if value is None:
            self._ReferencedSOPSequence = []
            if "ReferencedSOPSequence" in self._dataset:
                del self._dataset.ReferencedSOPSequence
        elif not isinstance(value, list) or not all(isinstance(item, ReferencedSOPSequenceItem) for item in value):
            raise ValueError("ReferencedSOPSequence must be a list of ReferencedSOPSequenceItem objects")
        else:
            self._ReferencedSOPSequence = value
            if "ReferencedSOPSequence" not in self._dataset:
                self._dataset.ReferencedSOPSequence = pydicom.Sequence()
            self._dataset.ReferencedSOPSequence.clear()
            self._dataset.ReferencedSOPSequence.extend([item.to_dataset() for item in value])

    def add_ReferencedSOP(self, item: ReferencedSOPSequenceItem):
        if not isinstance(item, ReferencedSOPSequenceItem):
            raise ValueError("Item must be an instance of ReferencedSOPSequenceItem")
        self._ReferencedSOPSequence.append(item)
        if "ReferencedSOPSequence" not in self._dataset:
            self._dataset.ReferencedSOPSequence = pydicom.Sequence()
        self._dataset.ReferencedSOPSequence.append(item.to_dataset())

    @property
    def LensThickness(self) -> Optional[float]:
        if "LensThickness" in self._dataset:
            return self._dataset.LensThickness
        return None

    @LensThickness.setter
    def LensThickness(self, value: Optional[float]):
        if value is None:
            if "LensThickness" in self._dataset:
                del self._dataset.LensThickness
        else:
            self._dataset.LensThickness = value

    @property
    def SourceOfLensThicknessDataCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "SourceOfLensThicknessDataCodeSequence" in self._dataset:
            if len(self._SourceOfLensThicknessDataCodeSequence) == len(self._dataset.SourceOfLensThicknessDataCodeSequence):
                return self._SourceOfLensThicknessDataCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.SourceOfLensThicknessDataCodeSequence]
        return None

    @SourceOfLensThicknessDataCodeSequence.setter
    def SourceOfLensThicknessDataCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._SourceOfLensThicknessDataCodeSequence = []
            if "SourceOfLensThicknessDataCodeSequence" in self._dataset:
                del self._dataset.SourceOfLensThicknessDataCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("SourceOfLensThicknessDataCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._SourceOfLensThicknessDataCodeSequence = value
            if "SourceOfLensThicknessDataCodeSequence" not in self._dataset:
                self._dataset.SourceOfLensThicknessDataCodeSequence = pydicom.Sequence()
            self._dataset.SourceOfLensThicknessDataCodeSequence.clear()
            self._dataset.SourceOfLensThicknessDataCodeSequence.extend([item.to_dataset() for item in value])

    def add_SourceOfLensThicknessDataCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._SourceOfLensThicknessDataCodeSequence.append(item)
        if "SourceOfLensThicknessDataCodeSequence" not in self._dataset:
            self._dataset.SourceOfLensThicknessDataCodeSequence = pydicom.Sequence()
        self._dataset.SourceOfLensThicknessDataCodeSequence.append(item.to_dataset())
