from typing import Any, List, Optional

import pydicom

from .fill_style_sequence_item import FillStyleSequenceItem
from .line_style_sequence_item import LineStyleSequenceItem
from .major_ticks_sequence_item import MajorTicksSequenceItem
from .text_style_sequence_item import TextStyleSequenceItem


class CompoundGraphicSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._TextStyleSequence: List[TextStyleSequenceItem] = []
        self._LineStyleSequence: List[LineStyleSequenceItem] = []
        self._FillStyleSequence: List[FillStyleSequenceItem] = []
        self._MajorTicksSequence: List[MajorTicksSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

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
    def RotationAngle(self) -> Optional[float]:
        if "RotationAngle" in self._dataset:
            return self._dataset.RotationAngle
        return None

    @RotationAngle.setter
    def RotationAngle(self, value: Optional[float]):
        if value is None:
            if "RotationAngle" in self._dataset:
                del self._dataset.RotationAngle
        else:
            self._dataset.RotationAngle = value

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
            raise ValueError(f"LineStyleSequence must be a list of LineStyleSequenceItem objects")
        else:
            self._LineStyleSequence = value
            if "LineStyleSequence" not in self._dataset:
                self._dataset.LineStyleSequence = pydicom.Sequence()
            self._dataset.LineStyleSequence.clear()
            self._dataset.LineStyleSequence.extend([item.to_dataset() for item in value])

    def add_LineStyle(self, item: LineStyleSequenceItem):
        if not isinstance(item, LineStyleSequenceItem):
            raise ValueError(f"Item must be an instance of LineStyleSequenceItem")
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
            raise ValueError(f"FillStyleSequence must be a list of FillStyleSequenceItem objects")
        else:
            self._FillStyleSequence = value
            if "FillStyleSequence" not in self._dataset:
                self._dataset.FillStyleSequence = pydicom.Sequence()
            self._dataset.FillStyleSequence.clear()
            self._dataset.FillStyleSequence.extend([item.to_dataset() for item in value])

    def add_FillStyle(self, item: FillStyleSequenceItem):
        if not isinstance(item, FillStyleSequenceItem):
            raise ValueError(f"Item must be an instance of FillStyleSequenceItem")
        self._FillStyleSequence.append(item)
        if "FillStyleSequence" not in self._dataset:
            self._dataset.FillStyleSequence = pydicom.Sequence()
        self._dataset.FillStyleSequence.append(item.to_dataset())

    @property
    def GapLength(self) -> Optional[float]:
        if "GapLength" in self._dataset:
            return self._dataset.GapLength
        return None

    @GapLength.setter
    def GapLength(self, value: Optional[float]):
        if value is None:
            if "GapLength" in self._dataset:
                del self._dataset.GapLength
        else:
            self._dataset.GapLength = value

    @property
    def DiameterOfVisibility(self) -> Optional[float]:
        if "DiameterOfVisibility" in self._dataset:
            return self._dataset.DiameterOfVisibility
        return None

    @DiameterOfVisibility.setter
    def DiameterOfVisibility(self, value: Optional[float]):
        if value is None:
            if "DiameterOfVisibility" in self._dataset:
                del self._dataset.DiameterOfVisibility
        else:
            self._dataset.DiameterOfVisibility = value

    @property
    def RotationPoint(self) -> Optional[List[float]]:
        if "RotationPoint" in self._dataset:
            return self._dataset.RotationPoint
        return None

    @RotationPoint.setter
    def RotationPoint(self, value: Optional[List[float]]):
        if value is None:
            if "RotationPoint" in self._dataset:
                del self._dataset.RotationPoint
        else:
            self._dataset.RotationPoint = value

    @property
    def TickAlignment(self) -> Optional[str]:
        if "TickAlignment" in self._dataset:
            return self._dataset.TickAlignment
        return None

    @TickAlignment.setter
    def TickAlignment(self, value: Optional[str]):
        if value is None:
            if "TickAlignment" in self._dataset:
                del self._dataset.TickAlignment
        else:
            self._dataset.TickAlignment = value

    @property
    def ShowTickLabel(self) -> Optional[str]:
        if "ShowTickLabel" in self._dataset:
            return self._dataset.ShowTickLabel
        return None

    @ShowTickLabel.setter
    def ShowTickLabel(self, value: Optional[str]):
        if value is None:
            if "ShowTickLabel" in self._dataset:
                del self._dataset.ShowTickLabel
        else:
            self._dataset.ShowTickLabel = value

    @property
    def TickLabelAlignment(self) -> Optional[str]:
        if "TickLabelAlignment" in self._dataset:
            return self._dataset.TickLabelAlignment
        return None

    @TickLabelAlignment.setter
    def TickLabelAlignment(self, value: Optional[str]):
        if value is None:
            if "TickLabelAlignment" in self._dataset:
                del self._dataset.TickLabelAlignment
        else:
            self._dataset.TickLabelAlignment = value

    @property
    def CompoundGraphicUnits(self) -> Optional[str]:
        if "CompoundGraphicUnits" in self._dataset:
            return self._dataset.CompoundGraphicUnits
        return None

    @CompoundGraphicUnits.setter
    def CompoundGraphicUnits(self, value: Optional[str]):
        if value is None:
            if "CompoundGraphicUnits" in self._dataset:
                del self._dataset.CompoundGraphicUnits
        else:
            self._dataset.CompoundGraphicUnits = value

    @property
    def MajorTicksSequence(self) -> Optional[List[MajorTicksSequenceItem]]:
        if "MajorTicksSequence" in self._dataset:
            if len(self._MajorTicksSequence) == len(self._dataset.MajorTicksSequence):
                return self._MajorTicksSequence
            else:
                return [MajorTicksSequenceItem(x) for x in self._dataset.MajorTicksSequence]
        return None

    @MajorTicksSequence.setter
    def MajorTicksSequence(self, value: Optional[List[MajorTicksSequenceItem]]):
        if value is None:
            self._MajorTicksSequence = []
            if "MajorTicksSequence" in self._dataset:
                del self._dataset.MajorTicksSequence
        elif not isinstance(value, list) or not all(isinstance(item, MajorTicksSequenceItem) for item in value):
            raise ValueError(f"MajorTicksSequence must be a list of MajorTicksSequenceItem objects")
        else:
            self._MajorTicksSequence = value
            if "MajorTicksSequence" not in self._dataset:
                self._dataset.MajorTicksSequence = pydicom.Sequence()
            self._dataset.MajorTicksSequence.clear()
            self._dataset.MajorTicksSequence.extend([item.to_dataset() for item in value])

    def add_MajorTicks(self, item: MajorTicksSequenceItem):
        if not isinstance(item, MajorTicksSequenceItem):
            raise ValueError(f"Item must be an instance of MajorTicksSequenceItem")
        self._MajorTicksSequence.append(item)
        if "MajorTicksSequence" not in self._dataset:
            self._dataset.MajorTicksSequence = pydicom.Sequence()
        self._dataset.MajorTicksSequence.append(item.to_dataset())

    @property
    def CompoundGraphicType(self) -> Optional[str]:
        if "CompoundGraphicType" in self._dataset:
            return self._dataset.CompoundGraphicType
        return None

    @CompoundGraphicType.setter
    def CompoundGraphicType(self, value: Optional[str]):
        if value is None:
            if "CompoundGraphicType" in self._dataset:
                del self._dataset.CompoundGraphicType
        else:
            self._dataset.CompoundGraphicType = value

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
