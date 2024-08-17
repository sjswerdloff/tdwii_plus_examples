from typing import Any, List, Optional

import pydicom

from .code_sequence_item import CodeSequenceItem
from .referenced_sop_sequence_item import ReferencedSOPSequenceItem


class CornealSizeSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._ReferencedSOPSequence: List[ReferencedSOPSequenceItem] = []
        self._SourceOfCornealSizeDataCodeSequence: List[CodeSequenceItem] = []

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
            raise ValueError(f"ReferencedSOPSequence must be a list of ReferencedSOPSequenceItem objects")
        else:
            self._ReferencedSOPSequence = value
            if "ReferencedSOPSequence" not in self._dataset:
                self._dataset.ReferencedSOPSequence = pydicom.Sequence()
            self._dataset.ReferencedSOPSequence.clear()
            self._dataset.ReferencedSOPSequence.extend([item.to_dataset() for item in value])

    def add_ReferencedSOP(self, item: ReferencedSOPSequenceItem):
        if not isinstance(item, ReferencedSOPSequenceItem):
            raise ValueError(f"Item must be an instance of ReferencedSOPSequenceItem")
        self._ReferencedSOPSequence.append(item)
        if "ReferencedSOPSequence" not in self._dataset:
            self._dataset.ReferencedSOPSequence = pydicom.Sequence()
        self._dataset.ReferencedSOPSequence.append(item.to_dataset())

    @property
    def SourceOfCornealSizeDataCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "SourceOfCornealSizeDataCodeSequence" in self._dataset:
            if len(self._SourceOfCornealSizeDataCodeSequence) == len(self._dataset.SourceOfCornealSizeDataCodeSequence):
                return self._SourceOfCornealSizeDataCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.SourceOfCornealSizeDataCodeSequence]
        return None

    @SourceOfCornealSizeDataCodeSequence.setter
    def SourceOfCornealSizeDataCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._SourceOfCornealSizeDataCodeSequence = []
            if "SourceOfCornealSizeDataCodeSequence" in self._dataset:
                del self._dataset.SourceOfCornealSizeDataCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError(f"SourceOfCornealSizeDataCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._SourceOfCornealSizeDataCodeSequence = value
            if "SourceOfCornealSizeDataCodeSequence" not in self._dataset:
                self._dataset.SourceOfCornealSizeDataCodeSequence = pydicom.Sequence()
            self._dataset.SourceOfCornealSizeDataCodeSequence.clear()
            self._dataset.SourceOfCornealSizeDataCodeSequence.extend([item.to_dataset() for item in value])

    def add_SourceOfCornealSizeDataCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError(f"Item must be an instance of CodeSequenceItem")
        self._SourceOfCornealSizeDataCodeSequence.append(item)
        if "SourceOfCornealSizeDataCodeSequence" not in self._dataset:
            self._dataset.SourceOfCornealSizeDataCodeSequence = pydicom.Sequence()
        self._dataset.SourceOfCornealSizeDataCodeSequence.append(item.to_dataset())

    @property
    def CornealSize(self) -> Optional[float]:
        if "CornealSize" in self._dataset:
            return self._dataset.CornealSize
        return None

    @CornealSize.setter
    def CornealSize(self, value: Optional[float]):
        if value is None:
            if "CornealSize" in self._dataset:
                del self._dataset.CornealSize
        else:
            self._dataset.CornealSize = value
