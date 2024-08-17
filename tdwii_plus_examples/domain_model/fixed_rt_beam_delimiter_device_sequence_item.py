from typing import Any, List, Optional

import pydicom


class FixedRTBeamDelimiterDeviceSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def OutlineShapeType(self) -> Optional[str]:
        if "OutlineShapeType" in self._dataset:
            return self._dataset.OutlineShapeType
        return None

    @OutlineShapeType.setter
    def OutlineShapeType(self, value: Optional[str]):
        if value is None:
            if "OutlineShapeType" in self._dataset:
                del self._dataset.OutlineShapeType
        else:
            self._dataset.OutlineShapeType = value

    @property
    def OutlineLeftVerticalEdge(self) -> Optional[float]:
        if "OutlineLeftVerticalEdge" in self._dataset:
            return self._dataset.OutlineLeftVerticalEdge
        return None

    @OutlineLeftVerticalEdge.setter
    def OutlineLeftVerticalEdge(self, value: Optional[float]):
        if value is None:
            if "OutlineLeftVerticalEdge" in self._dataset:
                del self._dataset.OutlineLeftVerticalEdge
        else:
            self._dataset.OutlineLeftVerticalEdge = value

    @property
    def OutlineRightVerticalEdge(self) -> Optional[float]:
        if "OutlineRightVerticalEdge" in self._dataset:
            return self._dataset.OutlineRightVerticalEdge
        return None

    @OutlineRightVerticalEdge.setter
    def OutlineRightVerticalEdge(self, value: Optional[float]):
        if value is None:
            if "OutlineRightVerticalEdge" in self._dataset:
                del self._dataset.OutlineRightVerticalEdge
        else:
            self._dataset.OutlineRightVerticalEdge = value

    @property
    def OutlineUpperHorizontalEdge(self) -> Optional[float]:
        if "OutlineUpperHorizontalEdge" in self._dataset:
            return self._dataset.OutlineUpperHorizontalEdge
        return None

    @OutlineUpperHorizontalEdge.setter
    def OutlineUpperHorizontalEdge(self, value: Optional[float]):
        if value is None:
            if "OutlineUpperHorizontalEdge" in self._dataset:
                del self._dataset.OutlineUpperHorizontalEdge
        else:
            self._dataset.OutlineUpperHorizontalEdge = value

    @property
    def OutlineLowerHorizontalEdge(self) -> Optional[float]:
        if "OutlineLowerHorizontalEdge" in self._dataset:
            return self._dataset.OutlineLowerHorizontalEdge
        return None

    @OutlineLowerHorizontalEdge.setter
    def OutlineLowerHorizontalEdge(self, value: Optional[float]):
        if value is None:
            if "OutlineLowerHorizontalEdge" in self._dataset:
                del self._dataset.OutlineLowerHorizontalEdge
        else:
            self._dataset.OutlineLowerHorizontalEdge = value

    @property
    def CenterOfCircularOutline(self) -> Optional[List[float]]:
        if "CenterOfCircularOutline" in self._dataset:
            return self._dataset.CenterOfCircularOutline
        return None

    @CenterOfCircularOutline.setter
    def CenterOfCircularOutline(self, value: Optional[List[float]]):
        if value is None:
            if "CenterOfCircularOutline" in self._dataset:
                del self._dataset.CenterOfCircularOutline
        else:
            self._dataset.CenterOfCircularOutline = value

    @property
    def DiameterOfCircularOutline(self) -> Optional[float]:
        if "DiameterOfCircularOutline" in self._dataset:
            return self._dataset.DiameterOfCircularOutline
        return None

    @DiameterOfCircularOutline.setter
    def DiameterOfCircularOutline(self, value: Optional[float]):
        if value is None:
            if "DiameterOfCircularOutline" in self._dataset:
                del self._dataset.DiameterOfCircularOutline
        else:
            self._dataset.DiameterOfCircularOutline = value

    @property
    def NumberOfPolygonalVertices(self) -> Optional[int]:
        if "NumberOfPolygonalVertices" in self._dataset:
            return self._dataset.NumberOfPolygonalVertices
        return None

    @NumberOfPolygonalVertices.setter
    def NumberOfPolygonalVertices(self, value: Optional[int]):
        if value is None:
            if "NumberOfPolygonalVertices" in self._dataset:
                del self._dataset.NumberOfPolygonalVertices
        else:
            self._dataset.NumberOfPolygonalVertices = value

    @property
    def VerticesOfThePolygonalOutline(self) -> Optional[bytes]:
        if "VerticesOfThePolygonalOutline" in self._dataset:
            return self._dataset.VerticesOfThePolygonalOutline
        return None

    @VerticesOfThePolygonalOutline.setter
    def VerticesOfThePolygonalOutline(self, value: Optional[bytes]):
        if value is None:
            if "VerticesOfThePolygonalOutline" in self._dataset:
                del self._dataset.VerticesOfThePolygonalOutline
        else:
            self._dataset.VerticesOfThePolygonalOutline = value
