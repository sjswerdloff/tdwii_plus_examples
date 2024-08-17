from typing import Any, List, Optional

import pydicom

from .code_sequence_item import CodeSequenceItem


class SurfacePointsSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._SegmentedPropertyCategoryCodeSequence: List[CodeSequenceItem] = []
        self._SegmentedPropertyTypeCodeSequence: List[CodeSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def SegmentedPropertyCategoryCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "SegmentedPropertyCategoryCodeSequence" in self._dataset:
            if len(self._SegmentedPropertyCategoryCodeSequence) == len(self._dataset.SegmentedPropertyCategoryCodeSequence):
                return self._SegmentedPropertyCategoryCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.SegmentedPropertyCategoryCodeSequence]
        return None

    @SegmentedPropertyCategoryCodeSequence.setter
    def SegmentedPropertyCategoryCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._SegmentedPropertyCategoryCodeSequence = []
            if "SegmentedPropertyCategoryCodeSequence" in self._dataset:
                del self._dataset.SegmentedPropertyCategoryCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError(f"SegmentedPropertyCategoryCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._SegmentedPropertyCategoryCodeSequence = value
            if "SegmentedPropertyCategoryCodeSequence" not in self._dataset:
                self._dataset.SegmentedPropertyCategoryCodeSequence = pydicom.Sequence()
            self._dataset.SegmentedPropertyCategoryCodeSequence.clear()
            self._dataset.SegmentedPropertyCategoryCodeSequence.extend([item.to_dataset() for item in value])

    def add_SegmentedPropertyCategoryCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError(f"Item must be an instance of CodeSequenceItem")
        self._SegmentedPropertyCategoryCodeSequence.append(item)
        if "SegmentedPropertyCategoryCodeSequence" not in self._dataset:
            self._dataset.SegmentedPropertyCategoryCodeSequence = pydicom.Sequence()
        self._dataset.SegmentedPropertyCategoryCodeSequence.append(item.to_dataset())

    @property
    def SegmentedPropertyTypeCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "SegmentedPropertyTypeCodeSequence" in self._dataset:
            if len(self._SegmentedPropertyTypeCodeSequence) == len(self._dataset.SegmentedPropertyTypeCodeSequence):
                return self._SegmentedPropertyTypeCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.SegmentedPropertyTypeCodeSequence]
        return None

    @SegmentedPropertyTypeCodeSequence.setter
    def SegmentedPropertyTypeCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._SegmentedPropertyTypeCodeSequence = []
            if "SegmentedPropertyTypeCodeSequence" in self._dataset:
                del self._dataset.SegmentedPropertyTypeCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError(f"SegmentedPropertyTypeCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._SegmentedPropertyTypeCodeSequence = value
            if "SegmentedPropertyTypeCodeSequence" not in self._dataset:
                self._dataset.SegmentedPropertyTypeCodeSequence = pydicom.Sequence()
            self._dataset.SegmentedPropertyTypeCodeSequence.clear()
            self._dataset.SegmentedPropertyTypeCodeSequence.extend([item.to_dataset() for item in value])

    def add_SegmentedPropertyTypeCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError(f"Item must be an instance of CodeSequenceItem")
        self._SegmentedPropertyTypeCodeSequence.append(item)
        if "SegmentedPropertyTypeCodeSequence" not in self._dataset:
            self._dataset.SegmentedPropertyTypeCodeSequence = pydicom.Sequence()
        self._dataset.SegmentedPropertyTypeCodeSequence.append(item.to_dataset())

    @property
    def NumberOfSurfacePoints(self) -> Optional[int]:
        if "NumberOfSurfacePoints" in self._dataset:
            return self._dataset.NumberOfSurfacePoints
        return None

    @NumberOfSurfacePoints.setter
    def NumberOfSurfacePoints(self, value: Optional[int]):
        if value is None:
            if "NumberOfSurfacePoints" in self._dataset:
                del self._dataset.NumberOfSurfacePoints
        else:
            self._dataset.NumberOfSurfacePoints = value

    @property
    def PointCoordinatesData(self) -> Optional[bytes]:
        if "PointCoordinatesData" in self._dataset:
            return self._dataset.PointCoordinatesData
        return None

    @PointCoordinatesData.setter
    def PointCoordinatesData(self, value: Optional[bytes]):
        if value is None:
            if "PointCoordinatesData" in self._dataset:
                del self._dataset.PointCoordinatesData
        else:
            self._dataset.PointCoordinatesData = value

    @property
    def PointPositionAccuracy(self) -> Optional[List[float]]:
        if "PointPositionAccuracy" in self._dataset:
            return self._dataset.PointPositionAccuracy
        return None

    @PointPositionAccuracy.setter
    def PointPositionAccuracy(self, value: Optional[List[float]]):
        if value is None:
            if "PointPositionAccuracy" in self._dataset:
                del self._dataset.PointPositionAccuracy
        else:
            self._dataset.PointPositionAccuracy = value

    @property
    def MeanPointDistance(self) -> Optional[float]:
        if "MeanPointDistance" in self._dataset:
            return self._dataset.MeanPointDistance
        return None

    @MeanPointDistance.setter
    def MeanPointDistance(self, value: Optional[float]):
        if value is None:
            if "MeanPointDistance" in self._dataset:
                del self._dataset.MeanPointDistance
        else:
            self._dataset.MeanPointDistance = value

    @property
    def MaximumPointDistance(self) -> Optional[float]:
        if "MaximumPointDistance" in self._dataset:
            return self._dataset.MaximumPointDistance
        return None

    @MaximumPointDistance.setter
    def MaximumPointDistance(self, value: Optional[float]):
        if value is None:
            if "MaximumPointDistance" in self._dataset:
                del self._dataset.MaximumPointDistance
        else:
            self._dataset.MaximumPointDistance = value

    @property
    def PointsBoundingBoxCoordinates(self) -> Optional[List[float]]:
        if "PointsBoundingBoxCoordinates" in self._dataset:
            return self._dataset.PointsBoundingBoxCoordinates
        return None

    @PointsBoundingBoxCoordinates.setter
    def PointsBoundingBoxCoordinates(self, value: Optional[List[float]]):
        if value is None:
            if "PointsBoundingBoxCoordinates" in self._dataset:
                del self._dataset.PointsBoundingBoxCoordinates
        else:
            self._dataset.PointsBoundingBoxCoordinates = value

    @property
    def AxisOfRotation(self) -> Optional[List[float]]:
        if "AxisOfRotation" in self._dataset:
            return self._dataset.AxisOfRotation
        return None

    @AxisOfRotation.setter
    def AxisOfRotation(self, value: Optional[List[float]]):
        if value is None:
            if "AxisOfRotation" in self._dataset:
                del self._dataset.AxisOfRotation
        else:
            self._dataset.AxisOfRotation = value

    @property
    def CenterOfRotation(self) -> Optional[List[float]]:
        if "CenterOfRotation" in self._dataset:
            return self._dataset.CenterOfRotation
        return None

    @CenterOfRotation.setter
    def CenterOfRotation(self, value: Optional[List[float]]):
        if value is None:
            if "CenterOfRotation" in self._dataset:
                del self._dataset.CenterOfRotation
        else:
            self._dataset.CenterOfRotation = value
