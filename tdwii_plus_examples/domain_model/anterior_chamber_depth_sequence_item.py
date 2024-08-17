from typing import Any, List, Optional  # noqa

import pydicom

from .code_sequence_item import CodeSequenceItem
from .referenced_sop_sequence_item import ReferencedSOPSequenceItem


class AnteriorChamberDepthSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._ReferencedSOPSequence: List[ReferencedSOPSequenceItem] = []
        self._SourceOfAnteriorChamberDepthDataCodeSequence: List[CodeSequenceItem] = []

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
    def AnteriorChamberDepth(self) -> Optional[float]:
        if "AnteriorChamberDepth" in self._dataset:
            return self._dataset.AnteriorChamberDepth
        return None

    @AnteriorChamberDepth.setter
    def AnteriorChamberDepth(self, value: Optional[float]):
        if value is None:
            if "AnteriorChamberDepth" in self._dataset:
                del self._dataset.AnteriorChamberDepth
        else:
            self._dataset.AnteriorChamberDepth = value

    @property
    def SourceOfAnteriorChamberDepthDataCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "SourceOfAnteriorChamberDepthDataCodeSequence" in self._dataset:
            if len(self._SourceOfAnteriorChamberDepthDataCodeSequence) == len(
                self._dataset.SourceOfAnteriorChamberDepthDataCodeSequence
            ):
                return self._SourceOfAnteriorChamberDepthDataCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.SourceOfAnteriorChamberDepthDataCodeSequence]
        return None

    @SourceOfAnteriorChamberDepthDataCodeSequence.setter
    def SourceOfAnteriorChamberDepthDataCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._SourceOfAnteriorChamberDepthDataCodeSequence = []
            if "SourceOfAnteriorChamberDepthDataCodeSequence" in self._dataset:
                del self._dataset.SourceOfAnteriorChamberDepthDataCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("SourceOfAnteriorChamberDepthDataCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._SourceOfAnteriorChamberDepthDataCodeSequence = value
            if "SourceOfAnteriorChamberDepthDataCodeSequence" not in self._dataset:
                self._dataset.SourceOfAnteriorChamberDepthDataCodeSequence = pydicom.Sequence()
            self._dataset.SourceOfAnteriorChamberDepthDataCodeSequence.clear()
            self._dataset.SourceOfAnteriorChamberDepthDataCodeSequence.extend([item.to_dataset() for item in value])

    def add_SourceOfAnteriorChamberDepthDataCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._SourceOfAnteriorChamberDepthDataCodeSequence.append(item)
        if "SourceOfAnteriorChamberDepthDataCodeSequence" not in self._dataset:
            self._dataset.SourceOfAnteriorChamberDepthDataCodeSequence = pydicom.Sequence()
        self._dataset.SourceOfAnteriorChamberDepthDataCodeSequence.append(item.to_dataset())
