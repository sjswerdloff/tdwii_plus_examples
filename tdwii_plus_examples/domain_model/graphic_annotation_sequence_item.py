from typing import Any, List, Optional

import pydicom

from .compound_graphic_sequence_item import CompoundGraphicSequenceItem
from .graphic_object_sequence_item import GraphicObjectSequenceItem
from .referenced_image_sequence_item import ReferencedImageSequenceItem
from .text_object_sequence_item import TextObjectSequenceItem


class GraphicAnnotationSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._ReferencedImageSequence: List[ReferencedImageSequenceItem] = []
        self._TextObjectSequence: List[TextObjectSequenceItem] = []
        self._GraphicObjectSequence: List[GraphicObjectSequenceItem] = []
        self._CompoundGraphicSequence: List[CompoundGraphicSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ReferencedImageSequence(self) -> Optional[List[ReferencedImageSequenceItem]]:
        if "ReferencedImageSequence" in self._dataset:
            if len(self._ReferencedImageSequence) == len(self._dataset.ReferencedImageSequence):
                return self._ReferencedImageSequence
            else:
                return [ReferencedImageSequenceItem(x) for x in self._dataset.ReferencedImageSequence]
        return None

    @ReferencedImageSequence.setter
    def ReferencedImageSequence(self, value: Optional[List[ReferencedImageSequenceItem]]):
        if value is None:
            self._ReferencedImageSequence = []
            if "ReferencedImageSequence" in self._dataset:
                del self._dataset.ReferencedImageSequence
        elif not isinstance(value, list) or not all(isinstance(item, ReferencedImageSequenceItem) for item in value):
            raise ValueError(f"ReferencedImageSequence must be a list of ReferencedImageSequenceItem objects")
        else:
            self._ReferencedImageSequence = value
            if "ReferencedImageSequence" not in self._dataset:
                self._dataset.ReferencedImageSequence = pydicom.Sequence()
            self._dataset.ReferencedImageSequence.clear()
            self._dataset.ReferencedImageSequence.extend([item.to_dataset() for item in value])

    def add_ReferencedImage(self, item: ReferencedImageSequenceItem):
        if not isinstance(item, ReferencedImageSequenceItem):
            raise ValueError(f"Item must be an instance of ReferencedImageSequenceItem")
        self._ReferencedImageSequence.append(item)
        if "ReferencedImageSequence" not in self._dataset:
            self._dataset.ReferencedImageSequence = pydicom.Sequence()
        self._dataset.ReferencedImageSequence.append(item.to_dataset())

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
            raise ValueError(f"TextObjectSequence must be a list of TextObjectSequenceItem objects")
        else:
            self._TextObjectSequence = value
            if "TextObjectSequence" not in self._dataset:
                self._dataset.TextObjectSequence = pydicom.Sequence()
            self._dataset.TextObjectSequence.clear()
            self._dataset.TextObjectSequence.extend([item.to_dataset() for item in value])

    def add_TextObject(self, item: TextObjectSequenceItem):
        if not isinstance(item, TextObjectSequenceItem):
            raise ValueError(f"Item must be an instance of TextObjectSequenceItem")
        self._TextObjectSequence.append(item)
        if "TextObjectSequence" not in self._dataset:
            self._dataset.TextObjectSequence = pydicom.Sequence()
        self._dataset.TextObjectSequence.append(item.to_dataset())

    @property
    def GraphicObjectSequence(self) -> Optional[List[GraphicObjectSequenceItem]]:
        if "GraphicObjectSequence" in self._dataset:
            if len(self._GraphicObjectSequence) == len(self._dataset.GraphicObjectSequence):
                return self._GraphicObjectSequence
            else:
                return [GraphicObjectSequenceItem(x) for x in self._dataset.GraphicObjectSequence]
        return None

    @GraphicObjectSequence.setter
    def GraphicObjectSequence(self, value: Optional[List[GraphicObjectSequenceItem]]):
        if value is None:
            self._GraphicObjectSequence = []
            if "GraphicObjectSequence" in self._dataset:
                del self._dataset.GraphicObjectSequence
        elif not isinstance(value, list) or not all(isinstance(item, GraphicObjectSequenceItem) for item in value):
            raise ValueError(f"GraphicObjectSequence must be a list of GraphicObjectSequenceItem objects")
        else:
            self._GraphicObjectSequence = value
            if "GraphicObjectSequence" not in self._dataset:
                self._dataset.GraphicObjectSequence = pydicom.Sequence()
            self._dataset.GraphicObjectSequence.clear()
            self._dataset.GraphicObjectSequence.extend([item.to_dataset() for item in value])

    def add_GraphicObject(self, item: GraphicObjectSequenceItem):
        if not isinstance(item, GraphicObjectSequenceItem):
            raise ValueError(f"Item must be an instance of GraphicObjectSequenceItem")
        self._GraphicObjectSequence.append(item)
        if "GraphicObjectSequence" not in self._dataset:
            self._dataset.GraphicObjectSequence = pydicom.Sequence()
        self._dataset.GraphicObjectSequence.append(item.to_dataset())

    @property
    def CompoundGraphicSequence(self) -> Optional[List[CompoundGraphicSequenceItem]]:
        if "CompoundGraphicSequence" in self._dataset:
            if len(self._CompoundGraphicSequence) == len(self._dataset.CompoundGraphicSequence):
                return self._CompoundGraphicSequence
            else:
                return [CompoundGraphicSequenceItem(x) for x in self._dataset.CompoundGraphicSequence]
        return None

    @CompoundGraphicSequence.setter
    def CompoundGraphicSequence(self, value: Optional[List[CompoundGraphicSequenceItem]]):
        if value is None:
            self._CompoundGraphicSequence = []
            if "CompoundGraphicSequence" in self._dataset:
                del self._dataset.CompoundGraphicSequence
        elif not isinstance(value, list) or not all(isinstance(item, CompoundGraphicSequenceItem) for item in value):
            raise ValueError(f"CompoundGraphicSequence must be a list of CompoundGraphicSequenceItem objects")
        else:
            self._CompoundGraphicSequence = value
            if "CompoundGraphicSequence" not in self._dataset:
                self._dataset.CompoundGraphicSequence = pydicom.Sequence()
            self._dataset.CompoundGraphicSequence.clear()
            self._dataset.CompoundGraphicSequence.extend([item.to_dataset() for item in value])

    def add_CompoundGraphic(self, item: CompoundGraphicSequenceItem):
        if not isinstance(item, CompoundGraphicSequenceItem):
            raise ValueError(f"Item must be an instance of CompoundGraphicSequenceItem")
        self._CompoundGraphicSequence.append(item)
        if "CompoundGraphicSequence" not in self._dataset:
            self._dataset.CompoundGraphicSequence = pydicom.Sequence()
        self._dataset.CompoundGraphicSequence.append(item.to_dataset())
