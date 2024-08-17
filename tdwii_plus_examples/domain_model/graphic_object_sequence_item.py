from typing import Any, List, Optional  # noqa

import pydicom

from .fill_style_sequence_item import FillStyleSequenceItem
from .line_style_sequence_item import LineStyleSequenceItem


class GraphicObjectSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._LineStyleSequence: List[LineStyleSequenceItem] = []
        self._FillStyleSequence: List[FillStyleSequenceItem] = []

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
    def GraphicAnnotationUnits(self) -> Optional[str]:
        if "GraphicAnnotationUnits" in self._dataset:
            return self._dataset.GraphicAnnotationUnits
        return None

    @GraphicAnnotationUnits.setter
    def GraphicAnnotationUnits(self, value: Optional[str]):
        if value is None:
            if "GraphicAnnotationUnits" in self._dataset:
                del self._dataset.GraphicAnnotationUnits
        else:
            self._dataset.GraphicAnnotationUnits = value

    @property
    def GraphicDimensions(self) -> Optional[int]:
        if "GraphicDimensions" in self._dataset:
            return self._dataset.GraphicDimensions
        return None

    @GraphicDimensions.setter
    def GraphicDimensions(self, value: Optional[int]):
        if value is None:
            if "GraphicDimensions" in self._dataset:
                del self._dataset.GraphicDimensions
        else:
            self._dataset.GraphicDimensions = value

    @property
    def NumberOfGraphicPoints(self) -> Optional[int]:
        if "NumberOfGraphicPoints" in self._dataset:
            return self._dataset.NumberOfGraphicPoints
        return None

    @NumberOfGraphicPoints.setter
    def NumberOfGraphicPoints(self, value: Optional[int]):
        if value is None:
            if "NumberOfGraphicPoints" in self._dataset:
                del self._dataset.NumberOfGraphicPoints
        else:
            self._dataset.NumberOfGraphicPoints = value

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
    def GraphicFilled(self) -> Optional[str]:
        if "GraphicFilled" in self._dataset:
            return self._dataset.GraphicFilled
        return None

    @GraphicFilled.setter
    def GraphicFilled(self, value: Optional[str]):
        if value is None:
            if "GraphicFilled" in self._dataset:
                del self._dataset.GraphicFilled
        else:
            self._dataset.GraphicFilled = value

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
    def LineStyleSequence(self) -> Optional[List[LineStyleSequenceItem]]:
        if "LineStyleSequence" in self._dataset:
            if len(self._LineStyleSequence) == len(self._dataset.LineStyleSequence):
                return self._LineStyleSequence
            else:
                return [LineStyleSequenceItem(x) for x in self._dataset.LineStyleSequence]
        return None

    @LineStyleSequence.setter
    def LineStyleSequence(self, value: Optional[List[LineStyleSequenceItem]]):
        if value is None:
            self._LineStyleSequence = []
            if "LineStyleSequence" in self._dataset:
                del self._dataset.LineStyleSequence
        elif not isinstance(value, list) or not all(isinstance(item, LineStyleSequenceItem) for item in value):
            raise ValueError("LineStyleSequence must be a list of LineStyleSequenceItem objects")
        else:
            self._LineStyleSequence = value
            if "LineStyleSequence" not in self._dataset:
                self._dataset.LineStyleSequence = pydicom.Sequence()
            self._dataset.LineStyleSequence.clear()
            self._dataset.LineStyleSequence.extend([item.to_dataset() for item in value])

    def add_LineStyle(self, item: LineStyleSequenceItem):
        if not isinstance(item, LineStyleSequenceItem):
            raise ValueError("Item must be an instance of LineStyleSequenceItem")
        self._LineStyleSequence.append(item)
        if "LineStyleSequence" not in self._dataset:
            self._dataset.LineStyleSequence = pydicom.Sequence()
        self._dataset.LineStyleSequence.append(item.to_dataset())

    @property
    def FillStyleSequence(self) -> Optional[List[FillStyleSequenceItem]]:
        if "FillStyleSequence" in self._dataset:
            if len(self._FillStyleSequence) == len(self._dataset.FillStyleSequence):
                return self._FillStyleSequence
            else:
                return [FillStyleSequenceItem(x) for x in self._dataset.FillStyleSequence]
        return None

    @FillStyleSequence.setter
    def FillStyleSequence(self, value: Optional[List[FillStyleSequenceItem]]):
        if value is None:
            self._FillStyleSequence = []
            if "FillStyleSequence" in self._dataset:
                del self._dataset.FillStyleSequence
        elif not isinstance(value, list) or not all(isinstance(item, FillStyleSequenceItem) for item in value):
            raise ValueError("FillStyleSequence must be a list of FillStyleSequenceItem objects")
        else:
            self._FillStyleSequence = value
            if "FillStyleSequence" not in self._dataset:
                self._dataset.FillStyleSequence = pydicom.Sequence()
            self._dataset.FillStyleSequence.clear()
            self._dataset.FillStyleSequence.extend([item.to_dataset() for item in value])

    def add_FillStyle(self, item: FillStyleSequenceItem):
        if not isinstance(item, FillStyleSequenceItem):
            raise ValueError("Item must be an instance of FillStyleSequenceItem")
        self._FillStyleSequence.append(item)
        if "FillStyleSequence" not in self._dataset:
            self._dataset.FillStyleSequence = pydicom.Sequence()
        self._dataset.FillStyleSequence.append(item.to_dataset())

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
