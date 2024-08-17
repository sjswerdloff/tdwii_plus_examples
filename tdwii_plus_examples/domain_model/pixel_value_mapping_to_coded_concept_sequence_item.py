from typing import Any, List, Optional  # noqa

import pydicom

from .code_sequence_item import CodeSequenceItem


class PixelValueMappingToCodedConceptSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._PixelValueMappingCodeSequence: List[CodeSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def MappedPixelValue(self) -> Optional[int]:
        if "MappedPixelValue" in self._dataset:
            return self._dataset.MappedPixelValue
        return None

    @MappedPixelValue.setter
    def MappedPixelValue(self, value: Optional[int]):
        if value is None:
            if "MappedPixelValue" in self._dataset:
                del self._dataset.MappedPixelValue
        else:
            self._dataset.MappedPixelValue = value

    @property
    def PixelValueMappingExplanation(self) -> Optional[str]:
        if "PixelValueMappingExplanation" in self._dataset:
            return self._dataset.PixelValueMappingExplanation
        return None

    @PixelValueMappingExplanation.setter
    def PixelValueMappingExplanation(self, value: Optional[str]):
        if value is None:
            if "PixelValueMappingExplanation" in self._dataset:
                del self._dataset.PixelValueMappingExplanation
        else:
            self._dataset.PixelValueMappingExplanation = value

    @property
    def PixelValueMappingCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "PixelValueMappingCodeSequence" in self._dataset:
            if len(self._PixelValueMappingCodeSequence) == len(self._dataset.PixelValueMappingCodeSequence):
                return self._PixelValueMappingCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.PixelValueMappingCodeSequence]
        return None

    @PixelValueMappingCodeSequence.setter
    def PixelValueMappingCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._PixelValueMappingCodeSequence = []
            if "PixelValueMappingCodeSequence" in self._dataset:
                del self._dataset.PixelValueMappingCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("PixelValueMappingCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._PixelValueMappingCodeSequence = value
            if "PixelValueMappingCodeSequence" not in self._dataset:
                self._dataset.PixelValueMappingCodeSequence = pydicom.Sequence()
            self._dataset.PixelValueMappingCodeSequence.clear()
            self._dataset.PixelValueMappingCodeSequence.extend([item.to_dataset() for item in value])

    def add_PixelValueMappingCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._PixelValueMappingCodeSequence.append(item)
        if "PixelValueMappingCodeSequence" not in self._dataset:
            self._dataset.PixelValueMappingCodeSequence = pydicom.Sequence()
        self._dataset.PixelValueMappingCodeSequence.append(item.to_dataset())
