from typing import Any, List, Optional  # noqa

import pydicom

from .referenced_structured_context_sequence_item import (
    ReferencedStructuredContextSequenceItem,
)
from .text_object_sequence_item import TextObjectSequenceItem


class VolumetricAnnotationSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._TextObjectSequence: List[TextObjectSequenceItem] = []
        self._ReferencedStructuredContextSequence: List[ReferencedStructuredContextSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def GraphicLayer(self) -> Optional[str]:
        if "GraphicLayer" in self._dataset:
            return self._dataset.GraphicLayer
        return None

    @GraphicLayer.setter
    def GraphicLayer(self, value: Optional[str]):
        if value is None:
            if "GraphicLayer" in self._dataset:
                del self._dataset.GraphicLayer
        else:
            self._dataset.GraphicLayer = value

    @property
    def TextObjectSequence(self) -> Optional[List[TextObjectSequenceItem]]:
        if "TextObjectSequence" in self._dataset:
            if len(self._TextObjectSequence) == len(self._dataset.TextObjectSequence):
                return self._TextObjectSequence
            else:
                return [TextObjectSequenceItem(x) for x in self._dataset.TextObjectSequence]
        return None

    @TextObjectSequence.setter
    def TextObjectSequence(self, value: Optional[List[TextObjectSequenceItem]]):
        if value is None:
            self._TextObjectSequence = []
            if "TextObjectSequence" in self._dataset:
                del self._dataset.TextObjectSequence
        elif not isinstance(value, list) or not all(isinstance(item, TextObjectSequenceItem) for item in value):
            raise ValueError("TextObjectSequence must be a list of TextObjectSequenceItem objects")
        else:
            self._TextObjectSequence = value
            if "TextObjectSequence" not in self._dataset:
                self._dataset.TextObjectSequence = pydicom.Sequence()
            self._dataset.TextObjectSequence.clear()
            self._dataset.TextObjectSequence.extend([item.to_dataset() for item in value])

    def add_TextObject(self, item: TextObjectSequenceItem):
        if not isinstance(item, TextObjectSequenceItem):
            raise ValueError("Item must be an instance of TextObjectSequenceItem")
        self._TextObjectSequence.append(item)
        if "TextObjectSequence" not in self._dataset:
            self._dataset.TextObjectSequence = pydicom.Sequence()
        self._dataset.TextObjectSequence.append(item.to_dataset())

    @property
    def GraphicData(self) -> Optional[List[float]]:
        if "GraphicData" in self._dataset:
            return self._dataset.GraphicData
        return None

    @GraphicData.setter
    def GraphicData(self, value: Optional[List[float]]):
        if value is None:
            if "GraphicData" in self._dataset:
                del self._dataset.GraphicData
        else:
            self._dataset.GraphicData = value

    @property
    def GraphicType(self) -> Optional[str]:
        if "GraphicType" in self._dataset:
            return self._dataset.GraphicType
        return None

    @GraphicType.setter
    def GraphicType(self, value: Optional[str]):
        if value is None:
            if "GraphicType" in self._dataset:
                del self._dataset.GraphicType
        else:
            self._dataset.GraphicType = value

    @property
    def ReferencedStructuredContextSequence(self) -> Optional[List[ReferencedStructuredContextSequenceItem]]:
        if "ReferencedStructuredContextSequence" in self._dataset:
            if len(self._ReferencedStructuredContextSequence) == len(self._dataset.ReferencedStructuredContextSequence):
                return self._ReferencedStructuredContextSequence
            else:
                return [ReferencedStructuredContextSequenceItem(x) for x in self._dataset.ReferencedStructuredContextSequence]
        return None

    @ReferencedStructuredContextSequence.setter
    def ReferencedStructuredContextSequence(self, value: Optional[List[ReferencedStructuredContextSequenceItem]]):
        if value is None:
            self._ReferencedStructuredContextSequence = []
            if "ReferencedStructuredContextSequence" in self._dataset:
                del self._dataset.ReferencedStructuredContextSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, ReferencedStructuredContextSequenceItem) for item in value
        ):
            raise ValueError(
                "ReferencedStructuredContextSequence must be a list of ReferencedStructuredContextSequenceItem objects"
            )
        else:
            self._ReferencedStructuredContextSequence = value
            if "ReferencedStructuredContextSequence" not in self._dataset:
                self._dataset.ReferencedStructuredContextSequence = pydicom.Sequence()
            self._dataset.ReferencedStructuredContextSequence.clear()
            self._dataset.ReferencedStructuredContextSequence.extend([item.to_dataset() for item in value])

    def add_ReferencedStructuredContext(self, item: ReferencedStructuredContextSequenceItem):
        if not isinstance(item, ReferencedStructuredContextSequenceItem):
            raise ValueError("Item must be an instance of ReferencedStructuredContextSequenceItem")
        self._ReferencedStructuredContextSequence.append(item)
        if "ReferencedStructuredContextSequence" not in self._dataset:
            self._dataset.ReferencedStructuredContextSequence = pydicom.Sequence()
        self._dataset.ReferencedStructuredContextSequence.append(item.to_dataset())

    @property
    def AnnotationClipping(self) -> Optional[str]:
        if "AnnotationClipping" in self._dataset:
            return self._dataset.AnnotationClipping
        return None

    @AnnotationClipping.setter
    def AnnotationClipping(self, value: Optional[str]):
        if value is None:
            if "AnnotationClipping" in self._dataset:
                del self._dataset.AnnotationClipping
        else:
            self._dataset.AnnotationClipping = value
