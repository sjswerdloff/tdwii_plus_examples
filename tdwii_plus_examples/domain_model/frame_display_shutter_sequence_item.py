from typing import Any, List, Optional  # noqa

import pydicom

from .referenced_image_sequence_item import ReferencedImageSequenceItem


class FrameDisplayShutterSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._ReferencedImageSequence: List[ReferencedImageSequenceItem] = []

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
            raise ValueError("ReferencedImageSequence must be a list of ReferencedImageSequenceItem objects")
        else:
            self._ReferencedImageSequence = value
            if "ReferencedImageSequence" not in self._dataset:
                self._dataset.ReferencedImageSequence = pydicom.Sequence()
            self._dataset.ReferencedImageSequence.clear()
            self._dataset.ReferencedImageSequence.extend([item.to_dataset() for item in value])

    def add_ReferencedImage(self, item: ReferencedImageSequenceItem):
        if not isinstance(item, ReferencedImageSequenceItem):
            raise ValueError("Item must be an instance of ReferencedImageSequenceItem")
        self._ReferencedImageSequence.append(item)
        if "ReferencedImageSequence" not in self._dataset:
            self._dataset.ReferencedImageSequence = pydicom.Sequence()
        self._dataset.ReferencedImageSequence.append(item.to_dataset())

    @property
    def ShutterShape(self) -> Optional[List[str]]:
        if "ShutterShape" in self._dataset:
            return self._dataset.ShutterShape
        return None

    @ShutterShape.setter
    def ShutterShape(self, value: Optional[List[str]]):
        if value is None:
            if "ShutterShape" in self._dataset:
                del self._dataset.ShutterShape
        else:
            self._dataset.ShutterShape = value

    @property
    def ShutterLeftVerticalEdge(self) -> Optional[int]:
        if "ShutterLeftVerticalEdge" in self._dataset:
            return self._dataset.ShutterLeftVerticalEdge
        return None

    @ShutterLeftVerticalEdge.setter
    def ShutterLeftVerticalEdge(self, value: Optional[int]):
        if value is None:
            if "ShutterLeftVerticalEdge" in self._dataset:
                del self._dataset.ShutterLeftVerticalEdge
        else:
            self._dataset.ShutterLeftVerticalEdge = value

    @property
    def ShutterRightVerticalEdge(self) -> Optional[int]:
        if "ShutterRightVerticalEdge" in self._dataset:
            return self._dataset.ShutterRightVerticalEdge
        return None

    @ShutterRightVerticalEdge.setter
    def ShutterRightVerticalEdge(self, value: Optional[int]):
        if value is None:
            if "ShutterRightVerticalEdge" in self._dataset:
                del self._dataset.ShutterRightVerticalEdge
        else:
            self._dataset.ShutterRightVerticalEdge = value

    @property
    def ShutterUpperHorizontalEdge(self) -> Optional[int]:
        if "ShutterUpperHorizontalEdge" in self._dataset:
            return self._dataset.ShutterUpperHorizontalEdge
        return None

    @ShutterUpperHorizontalEdge.setter
    def ShutterUpperHorizontalEdge(self, value: Optional[int]):
        if value is None:
            if "ShutterUpperHorizontalEdge" in self._dataset:
                del self._dataset.ShutterUpperHorizontalEdge
        else:
            self._dataset.ShutterUpperHorizontalEdge = value

    @property
    def ShutterLowerHorizontalEdge(self) -> Optional[int]:
        if "ShutterLowerHorizontalEdge" in self._dataset:
            return self._dataset.ShutterLowerHorizontalEdge
        return None

    @ShutterLowerHorizontalEdge.setter
    def ShutterLowerHorizontalEdge(self, value: Optional[int]):
        if value is None:
            if "ShutterLowerHorizontalEdge" in self._dataset:
                del self._dataset.ShutterLowerHorizontalEdge
        else:
            self._dataset.ShutterLowerHorizontalEdge = value

    @property
    def CenterOfCircularShutter(self) -> Optional[List[int]]:
        if "CenterOfCircularShutter" in self._dataset:
            return self._dataset.CenterOfCircularShutter
        return None

    @CenterOfCircularShutter.setter
    def CenterOfCircularShutter(self, value: Optional[List[int]]):
        if value is None:
            if "CenterOfCircularShutter" in self._dataset:
                del self._dataset.CenterOfCircularShutter
        else:
            self._dataset.CenterOfCircularShutter = value

    @property
    def RadiusOfCircularShutter(self) -> Optional[int]:
        if "RadiusOfCircularShutter" in self._dataset:
            return self._dataset.RadiusOfCircularShutter
        return None

    @RadiusOfCircularShutter.setter
    def RadiusOfCircularShutter(self, value: Optional[int]):
        if value is None:
            if "RadiusOfCircularShutter" in self._dataset:
                del self._dataset.RadiusOfCircularShutter
        else:
            self._dataset.RadiusOfCircularShutter = value

    @property
    def VerticesOfThePolygonalShutter(self) -> Optional[List[int]]:
        if "VerticesOfThePolygonalShutter" in self._dataset:
            return self._dataset.VerticesOfThePolygonalShutter
        return None

    @VerticesOfThePolygonalShutter.setter
    def VerticesOfThePolygonalShutter(self, value: Optional[List[int]]):
        if value is None:
            if "VerticesOfThePolygonalShutter" in self._dataset:
                del self._dataset.VerticesOfThePolygonalShutter
        else:
            self._dataset.VerticesOfThePolygonalShutter = value

    @property
    def ShutterPresentationValue(self) -> Optional[int]:
        if "ShutterPresentationValue" in self._dataset:
            return self._dataset.ShutterPresentationValue
        return None

    @ShutterPresentationValue.setter
    def ShutterPresentationValue(self, value: Optional[int]):
        if value is None:
            if "ShutterPresentationValue" in self._dataset:
                del self._dataset.ShutterPresentationValue
        else:
            self._dataset.ShutterPresentationValue = value

    @property
    def ShutterPresentationColorCIELabValue(self) -> Optional[List[int]]:
        if "ShutterPresentationColorCIELabValue" in self._dataset:
            return self._dataset.ShutterPresentationColorCIELabValue
        return None

    @ShutterPresentationColorCIELabValue.setter
    def ShutterPresentationColorCIELabValue(self, value: Optional[List[int]]):
        if value is None:
            if "ShutterPresentationColorCIELabValue" in self._dataset:
                del self._dataset.ShutterPresentationColorCIELabValue
        else:
            self._dataset.ShutterPresentationColorCIELabValue = value
