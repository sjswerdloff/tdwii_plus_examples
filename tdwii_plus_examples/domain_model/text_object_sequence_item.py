from typing import Any, List, Optional

import pydicom

from .text_style_sequence_item import TextStyleSequenceItem


class TextObjectSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._TextStyleSequence: List[TextStyleSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def TrackingID(self) -> Optional[str]:
        if "TrackingID" in self._dataset:
            return self._dataset.TrackingID
        return None

    @TrackingID.setter
    def TrackingID(self, value: Optional[str]):
        if value is None:
            if "TrackingID" in self._dataset:
                del self._dataset.TrackingID
        else:
            self._dataset.TrackingID = value

    @property
    def TrackingUID(self) -> Optional[str]:
        if "TrackingUID" in self._dataset:
            return self._dataset.TrackingUID
        return None

    @TrackingUID.setter
    def TrackingUID(self, value: Optional[str]):
        if value is None:
            if "TrackingUID" in self._dataset:
                del self._dataset.TrackingUID
        else:
            self._dataset.TrackingUID = value

    @property
    def BoundingBoxAnnotationUnits(self) -> Optional[str]:
        if "BoundingBoxAnnotationUnits" in self._dataset:
            return self._dataset.BoundingBoxAnnotationUnits
        return None

    @BoundingBoxAnnotationUnits.setter
    def BoundingBoxAnnotationUnits(self, value: Optional[str]):
        if value is None:
            if "BoundingBoxAnnotationUnits" in self._dataset:
                del self._dataset.BoundingBoxAnnotationUnits
        else:
            self._dataset.BoundingBoxAnnotationUnits = value

    @property
    def AnchorPointAnnotationUnits(self) -> Optional[str]:
        if "AnchorPointAnnotationUnits" in self._dataset:
            return self._dataset.AnchorPointAnnotationUnits
        return None

    @AnchorPointAnnotationUnits.setter
    def AnchorPointAnnotationUnits(self, value: Optional[str]):
        if value is None:
            if "AnchorPointAnnotationUnits" in self._dataset:
                del self._dataset.AnchorPointAnnotationUnits
        else:
            self._dataset.AnchorPointAnnotationUnits = value

    @property
    def UnformattedTextValue(self) -> Optional[str]:
        if "UnformattedTextValue" in self._dataset:
            return self._dataset.UnformattedTextValue
        return None

    @UnformattedTextValue.setter
    def UnformattedTextValue(self, value: Optional[str]):
        if value is None:
            if "UnformattedTextValue" in self._dataset:
                del self._dataset.UnformattedTextValue
        else:
            self._dataset.UnformattedTextValue = value

    @property
    def BoundingBoxTopLeftHandCorner(self) -> Optional[List[float]]:
        if "BoundingBoxTopLeftHandCorner" in self._dataset:
            return self._dataset.BoundingBoxTopLeftHandCorner
        return None

    @BoundingBoxTopLeftHandCorner.setter
    def BoundingBoxTopLeftHandCorner(self, value: Optional[List[float]]):
        if value is None:
            if "BoundingBoxTopLeftHandCorner" in self._dataset:
                del self._dataset.BoundingBoxTopLeftHandCorner
        else:
            self._dataset.BoundingBoxTopLeftHandCorner = value

    @property
    def BoundingBoxBottomRightHandCorner(self) -> Optional[List[float]]:
        if "BoundingBoxBottomRightHandCorner" in self._dataset:
            return self._dataset.BoundingBoxBottomRightHandCorner
        return None

    @BoundingBoxBottomRightHandCorner.setter
    def BoundingBoxBottomRightHandCorner(self, value: Optional[List[float]]):
        if value is None:
            if "BoundingBoxBottomRightHandCorner" in self._dataset:
                del self._dataset.BoundingBoxBottomRightHandCorner
        else:
            self._dataset.BoundingBoxBottomRightHandCorner = value

    @property
    def BoundingBoxTextHorizontalJustification(self) -> Optional[str]:
        if "BoundingBoxTextHorizontalJustification" in self._dataset:
            return self._dataset.BoundingBoxTextHorizontalJustification
        return None

    @BoundingBoxTextHorizontalJustification.setter
    def BoundingBoxTextHorizontalJustification(self, value: Optional[str]):
        if value is None:
            if "BoundingBoxTextHorizontalJustification" in self._dataset:
                del self._dataset.BoundingBoxTextHorizontalJustification
        else:
            self._dataset.BoundingBoxTextHorizontalJustification = value

    @property
    def AnchorPoint(self) -> Optional[List[float]]:
        if "AnchorPoint" in self._dataset:
            return self._dataset.AnchorPoint
        return None

    @AnchorPoint.setter
    def AnchorPoint(self, value: Optional[List[float]]):
        if value is None:
            if "AnchorPoint" in self._dataset:
                del self._dataset.AnchorPoint
        else:
            self._dataset.AnchorPoint = value

    @property
    def AnchorPointVisibility(self) -> Optional[str]:
        if "AnchorPointVisibility" in self._dataset:
            return self._dataset.AnchorPointVisibility
        return None

    @AnchorPointVisibility.setter
    def AnchorPointVisibility(self, value: Optional[str]):
        if value is None:
            if "AnchorPointVisibility" in self._dataset:
                del self._dataset.AnchorPointVisibility
        else:
            self._dataset.AnchorPointVisibility = value

    @property
    def CompoundGraphicInstanceID(self) -> Optional[int]:
        if "CompoundGraphicInstanceID" in self._dataset:
            return self._dataset.CompoundGraphicInstanceID
        return None

    @CompoundGraphicInstanceID.setter
    def CompoundGraphicInstanceID(self, value: Optional[int]):
        if value is None:
            if "CompoundGraphicInstanceID" in self._dataset:
                del self._dataset.CompoundGraphicInstanceID
        else:
            self._dataset.CompoundGraphicInstanceID = value

    @property
    def TextStyleSequence(self) -> Optional[List[TextStyleSequenceItem]]:
        if "TextStyleSequence" in self._dataset:
            if len(self._TextStyleSequence) == len(self._dataset.TextStyleSequence):
                return self._TextStyleSequence
            else:
                return [TextStyleSequenceItem(x) for x in self._dataset.TextStyleSequence]
        return None

    @TextStyleSequence.setter
    def TextStyleSequence(self, value: Optional[List[TextStyleSequenceItem]]):
        if value is None:
            self._TextStyleSequence = []
            if "TextStyleSequence" in self._dataset:
                del self._dataset.TextStyleSequence
        elif not isinstance(value, list) or not all(isinstance(item, TextStyleSequenceItem) for item in value):
            raise ValueError(f"TextStyleSequence must be a list of TextStyleSequenceItem objects")
        else:
            self._TextStyleSequence = value
            if "TextStyleSequence" not in self._dataset:
                self._dataset.TextStyleSequence = pydicom.Sequence()
            self._dataset.TextStyleSequence.clear()
            self._dataset.TextStyleSequence.extend([item.to_dataset() for item in value])

    def add_TextStyle(self, item: TextStyleSequenceItem):
        if not isinstance(item, TextStyleSequenceItem):
            raise ValueError(f"Item must be an instance of TextStyleSequenceItem")
        self._TextStyleSequence.append(item)
        if "TextStyleSequence" not in self._dataset:
            self._dataset.TextStyleSequence = pydicom.Sequence()
        self._dataset.TextStyleSequence.append(item.to_dataset())

    @property
    def GraphicGroupID(self) -> Optional[int]:
        if "GraphicGroupID" in self._dataset:
            return self._dataset.GraphicGroupID
        return None

    @GraphicGroupID.setter
    def GraphicGroupID(self, value: Optional[int]):
        if value is None:
            if "GraphicGroupID" in self._dataset:
                del self._dataset.GraphicGroupID
        else:
            self._dataset.GraphicGroupID = value
