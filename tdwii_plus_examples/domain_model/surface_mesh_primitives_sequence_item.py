from typing import Any, List, Optional  # noqa

import pydicom

from .facet_sequence_item import FacetSequenceItem
from .line_sequence_item import LineSequenceItem
from .triangle_fan_sequence_item import TriangleFanSequenceItem
from .triangle_strip_sequence_item import TriangleStripSequenceItem


class SurfaceMeshPrimitivesSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._TriangleStripSequence: List[TriangleStripSequenceItem] = []
        self._TriangleFanSequence: List[TriangleFanSequenceItem] = []
        self._LineSequence: List[LineSequenceItem] = []
        self._FacetSequence: List[FacetSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def TriangleStripSequence(self) -> Optional[List[TriangleStripSequenceItem]]:
        if "TriangleStripSequence" in self._dataset:
            if len(self._TriangleStripSequence) == len(self._dataset.TriangleStripSequence):
                return self._TriangleStripSequence
            else:
                return [TriangleStripSequenceItem(x) for x in self._dataset.TriangleStripSequence]
        return None

    @TriangleStripSequence.setter
    def TriangleStripSequence(self, value: Optional[List[TriangleStripSequenceItem]]):
        if value is None:
            self._TriangleStripSequence = []
            if "TriangleStripSequence" in self._dataset:
                del self._dataset.TriangleStripSequence
        elif not isinstance(value, list) or not all(isinstance(item, TriangleStripSequenceItem) for item in value):
            raise ValueError("TriangleStripSequence must be a list of TriangleStripSequenceItem objects")
        else:
            self._TriangleStripSequence = value
            if "TriangleStripSequence" not in self._dataset:
                self._dataset.TriangleStripSequence = pydicom.Sequence()
            self._dataset.TriangleStripSequence.clear()
            self._dataset.TriangleStripSequence.extend([item.to_dataset() for item in value])

    def add_TriangleStrip(self, item: TriangleStripSequenceItem):
        if not isinstance(item, TriangleStripSequenceItem):
            raise ValueError("Item must be an instance of TriangleStripSequenceItem")
        self._TriangleStripSequence.append(item)
        if "TriangleStripSequence" not in self._dataset:
            self._dataset.TriangleStripSequence = pydicom.Sequence()
        self._dataset.TriangleStripSequence.append(item.to_dataset())

    @property
    def TriangleFanSequence(self) -> Optional[List[TriangleFanSequenceItem]]:
        if "TriangleFanSequence" in self._dataset:
            if len(self._TriangleFanSequence) == len(self._dataset.TriangleFanSequence):
                return self._TriangleFanSequence
            else:
                return [TriangleFanSequenceItem(x) for x in self._dataset.TriangleFanSequence]
        return None

    @TriangleFanSequence.setter
    def TriangleFanSequence(self, value: Optional[List[TriangleFanSequenceItem]]):
        if value is None:
            self._TriangleFanSequence = []
            if "TriangleFanSequence" in self._dataset:
                del self._dataset.TriangleFanSequence
        elif not isinstance(value, list) or not all(isinstance(item, TriangleFanSequenceItem) for item in value):
            raise ValueError("TriangleFanSequence must be a list of TriangleFanSequenceItem objects")
        else:
            self._TriangleFanSequence = value
            if "TriangleFanSequence" not in self._dataset:
                self._dataset.TriangleFanSequence = pydicom.Sequence()
            self._dataset.TriangleFanSequence.clear()
            self._dataset.TriangleFanSequence.extend([item.to_dataset() for item in value])

    def add_TriangleFan(self, item: TriangleFanSequenceItem):
        if not isinstance(item, TriangleFanSequenceItem):
            raise ValueError("Item must be an instance of TriangleFanSequenceItem")
        self._TriangleFanSequence.append(item)
        if "TriangleFanSequence" not in self._dataset:
            self._dataset.TriangleFanSequence = pydicom.Sequence()
        self._dataset.TriangleFanSequence.append(item.to_dataset())

    @property
    def LineSequence(self) -> Optional[List[LineSequenceItem]]:
        if "LineSequence" in self._dataset:
            if len(self._LineSequence) == len(self._dataset.LineSequence):
                return self._LineSequence
            else:
                return [LineSequenceItem(x) for x in self._dataset.LineSequence]
        return None

    @LineSequence.setter
    def LineSequence(self, value: Optional[List[LineSequenceItem]]):
        if value is None:
            self._LineSequence = []
            if "LineSequence" in self._dataset:
                del self._dataset.LineSequence
        elif not isinstance(value, list) or not all(isinstance(item, LineSequenceItem) for item in value):
            raise ValueError("LineSequence must be a list of LineSequenceItem objects")
        else:
            self._LineSequence = value
            if "LineSequence" not in self._dataset:
                self._dataset.LineSequence = pydicom.Sequence()
            self._dataset.LineSequence.clear()
            self._dataset.LineSequence.extend([item.to_dataset() for item in value])

    def add_Line(self, item: LineSequenceItem):
        if not isinstance(item, LineSequenceItem):
            raise ValueError("Item must be an instance of LineSequenceItem")
        self._LineSequence.append(item)
        if "LineSequence" not in self._dataset:
            self._dataset.LineSequence = pydicom.Sequence()
        self._dataset.LineSequence.append(item.to_dataset())

    @property
    def FacetSequence(self) -> Optional[List[FacetSequenceItem]]:
        if "FacetSequence" in self._dataset:
            if len(self._FacetSequence) == len(self._dataset.FacetSequence):
                return self._FacetSequence
            else:
                return [FacetSequenceItem(x) for x in self._dataset.FacetSequence]
        return None

    @FacetSequence.setter
    def FacetSequence(self, value: Optional[List[FacetSequenceItem]]):
        if value is None:
            self._FacetSequence = []
            if "FacetSequence" in self._dataset:
                del self._dataset.FacetSequence
        elif not isinstance(value, list) or not all(isinstance(item, FacetSequenceItem) for item in value):
            raise ValueError("FacetSequence must be a list of FacetSequenceItem objects")
        else:
            self._FacetSequence = value
            if "FacetSequence" not in self._dataset:
                self._dataset.FacetSequence = pydicom.Sequence()
            self._dataset.FacetSequence.clear()
            self._dataset.FacetSequence.extend([item.to_dataset() for item in value])

    def add_Facet(self, item: FacetSequenceItem):
        if not isinstance(item, FacetSequenceItem):
            raise ValueError("Item must be an instance of FacetSequenceItem")
        self._FacetSequence.append(item)
        if "FacetSequence" not in self._dataset:
            self._dataset.FacetSequence = pydicom.Sequence()
        self._dataset.FacetSequence.append(item.to_dataset())

    @property
    def LongTrianglePointIndexList(self) -> Optional[bytes]:
        if "LongTrianglePointIndexList" in self._dataset:
            return self._dataset.LongTrianglePointIndexList
        return None

    @LongTrianglePointIndexList.setter
    def LongTrianglePointIndexList(self, value: Optional[bytes]):
        if value is None:
            if "LongTrianglePointIndexList" in self._dataset:
                del self._dataset.LongTrianglePointIndexList
        else:
            self._dataset.LongTrianglePointIndexList = value

    @property
    def LongEdgePointIndexList(self) -> Optional[bytes]:
        if "LongEdgePointIndexList" in self._dataset:
            return self._dataset.LongEdgePointIndexList
        return None

    @LongEdgePointIndexList.setter
    def LongEdgePointIndexList(self, value: Optional[bytes]):
        if value is None:
            if "LongEdgePointIndexList" in self._dataset:
                del self._dataset.LongEdgePointIndexList
        else:
            self._dataset.LongEdgePointIndexList = value

    @property
    def LongVertexPointIndexList(self) -> Optional[bytes]:
        if "LongVertexPointIndexList" in self._dataset:
            return self._dataset.LongVertexPointIndexList
        return None

    @LongVertexPointIndexList.setter
    def LongVertexPointIndexList(self, value: Optional[bytes]):
        if value is None:
            if "LongVertexPointIndexList" in self._dataset:
                del self._dataset.LongVertexPointIndexList
        else:
            self._dataset.LongVertexPointIndexList = value
