from decimal import Decimal
from typing import Any, List, Optional

import pydicom

from .code_sequence_item import CodeSequenceItem


class DetectorInformationSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._ViewCodeSequence: List[CodeSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def DistanceSourceToDetector(self) -> Optional[Decimal]:
        if "DistanceSourceToDetector" in self._dataset:
            return self._dataset.DistanceSourceToDetector
        return None

    @DistanceSourceToDetector.setter
    def DistanceSourceToDetector(self, value: Optional[Decimal]):
        if value is None:
            if "DistanceSourceToDetector" in self._dataset:
                del self._dataset.DistanceSourceToDetector
        else:
            self._dataset.DistanceSourceToDetector = value

    @property
    def GantryDetectorTilt(self) -> Optional[Decimal]:
        if "GantryDetectorTilt" in self._dataset:
            return self._dataset.GantryDetectorTilt
        return None

    @GantryDetectorTilt.setter
    def GantryDetectorTilt(self, value: Optional[Decimal]):
        if value is None:
            if "GantryDetectorTilt" in self._dataset:
                del self._dataset.GantryDetectorTilt
        else:
            self._dataset.GantryDetectorTilt = value

    @property
    def RadialPosition(self) -> Optional[List[Decimal]]:
        if "RadialPosition" in self._dataset:
            return self._dataset.RadialPosition
        return None

    @RadialPosition.setter
    def RadialPosition(self, value: Optional[List[Decimal]]):
        if value is None:
            if "RadialPosition" in self._dataset:
                del self._dataset.RadialPosition
        else:
            self._dataset.RadialPosition = value

    @property
    def CenterOfRotationOffset(self) -> Optional[Decimal]:
        if "CenterOfRotationOffset" in self._dataset:
            return self._dataset.CenterOfRotationOffset
        return None

    @CenterOfRotationOffset.setter
    def CenterOfRotationOffset(self, value: Optional[Decimal]):
        if value is None:
            if "CenterOfRotationOffset" in self._dataset:
                del self._dataset.CenterOfRotationOffset
        else:
            self._dataset.CenterOfRotationOffset = value

    @property
    def FieldOfViewShape(self) -> Optional[str]:
        if "FieldOfViewShape" in self._dataset:
            return self._dataset.FieldOfViewShape
        return None

    @FieldOfViewShape.setter
    def FieldOfViewShape(self, value: Optional[str]):
        if value is None:
            if "FieldOfViewShape" in self._dataset:
                del self._dataset.FieldOfViewShape
        else:
            self._dataset.FieldOfViewShape = value

    @property
    def FieldOfViewDimensions(self) -> Optional[List[int]]:
        if "FieldOfViewDimensions" in self._dataset:
            return self._dataset.FieldOfViewDimensions
        return None

    @FieldOfViewDimensions.setter
    def FieldOfViewDimensions(self, value: Optional[List[int]]):
        if value is None:
            if "FieldOfViewDimensions" in self._dataset:
                del self._dataset.FieldOfViewDimensions
        else:
            self._dataset.FieldOfViewDimensions = value

    @property
    def CollimatorGridName(self) -> Optional[str]:
        if "CollimatorGridName" in self._dataset:
            return self._dataset.CollimatorGridName
        return None

    @CollimatorGridName.setter
    def CollimatorGridName(self, value: Optional[str]):
        if value is None:
            if "CollimatorGridName" in self._dataset:
                del self._dataset.CollimatorGridName
        else:
            self._dataset.CollimatorGridName = value

    @property
    def CollimatorType(self) -> Optional[str]:
        if "CollimatorType" in self._dataset:
            return self._dataset.CollimatorType
        return None

    @CollimatorType.setter
    def CollimatorType(self, value: Optional[str]):
        if value is None:
            if "CollimatorType" in self._dataset:
                del self._dataset.CollimatorType
        else:
            self._dataset.CollimatorType = value

    @property
    def FocalDistance(self) -> Optional[List[int]]:
        if "FocalDistance" in self._dataset:
            return self._dataset.FocalDistance
        return None

    @FocalDistance.setter
    def FocalDistance(self, value: Optional[List[int]]):
        if value is None:
            if "FocalDistance" in self._dataset:
                del self._dataset.FocalDistance
        else:
            self._dataset.FocalDistance = value

    @property
    def XFocusCenter(self) -> Optional[List[Decimal]]:
        if "XFocusCenter" in self._dataset:
            return self._dataset.XFocusCenter
        return None

    @XFocusCenter.setter
    def XFocusCenter(self, value: Optional[List[Decimal]]):
        if value is None:
            if "XFocusCenter" in self._dataset:
                del self._dataset.XFocusCenter
        else:
            self._dataset.XFocusCenter = value

    @property
    def YFocusCenter(self) -> Optional[List[Decimal]]:
        if "YFocusCenter" in self._dataset:
            return self._dataset.YFocusCenter
        return None

    @YFocusCenter.setter
    def YFocusCenter(self, value: Optional[List[Decimal]]):
        if value is None:
            if "YFocusCenter" in self._dataset:
                del self._dataset.YFocusCenter
        else:
            self._dataset.YFocusCenter = value

    @property
    def ImagePositionPatient(self) -> Optional[List[Decimal]]:
        if "ImagePositionPatient" in self._dataset:
            return self._dataset.ImagePositionPatient
        return None

    @ImagePositionPatient.setter
    def ImagePositionPatient(self, value: Optional[List[Decimal]]):
        if value is None:
            if "ImagePositionPatient" in self._dataset:
                del self._dataset.ImagePositionPatient
        else:
            self._dataset.ImagePositionPatient = value

    @property
    def ImageOrientationPatient(self) -> Optional[List[Decimal]]:
        if "ImageOrientationPatient" in self._dataset:
            return self._dataset.ImageOrientationPatient
        return None

    @ImageOrientationPatient.setter
    def ImageOrientationPatient(self, value: Optional[List[Decimal]]):
        if value is None:
            if "ImageOrientationPatient" in self._dataset:
                del self._dataset.ImageOrientationPatient
        else:
            self._dataset.ImageOrientationPatient = value

    @property
    def ZoomFactor(self) -> Optional[List[Decimal]]:
        if "ZoomFactor" in self._dataset:
            return self._dataset.ZoomFactor
        return None

    @ZoomFactor.setter
    def ZoomFactor(self, value: Optional[List[Decimal]]):
        if value is None:
            if "ZoomFactor" in self._dataset:
                del self._dataset.ZoomFactor
        else:
            self._dataset.ZoomFactor = value

    @property
    def ZoomCenter(self) -> Optional[List[Decimal]]:
        if "ZoomCenter" in self._dataset:
            return self._dataset.ZoomCenter
        return None

    @ZoomCenter.setter
    def ZoomCenter(self, value: Optional[List[Decimal]]):
        if value is None:
            if "ZoomCenter" in self._dataset:
                del self._dataset.ZoomCenter
        else:
            self._dataset.ZoomCenter = value

    @property
    def StartAngle(self) -> Optional[Decimal]:
        if "StartAngle" in self._dataset:
            return self._dataset.StartAngle
        return None

    @StartAngle.setter
    def StartAngle(self, value: Optional[Decimal]):
        if value is None:
            if "StartAngle" in self._dataset:
                del self._dataset.StartAngle
        else:
            self._dataset.StartAngle = value

    @property
    def ViewCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "ViewCodeSequence" in self._dataset:
            if len(self._ViewCodeSequence) == len(self._dataset.ViewCodeSequence):
                return self._ViewCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.ViewCodeSequence]
        return None

    @ViewCodeSequence.setter
    def ViewCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._ViewCodeSequence = []
            if "ViewCodeSequence" in self._dataset:
                del self._dataset.ViewCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError(f"ViewCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._ViewCodeSequence = value
            if "ViewCodeSequence" not in self._dataset:
                self._dataset.ViewCodeSequence = pydicom.Sequence()
            self._dataset.ViewCodeSequence.clear()
            self._dataset.ViewCodeSequence.extend([item.to_dataset() for item in value])

    def add_ViewCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError(f"Item must be an instance of CodeSequenceItem")
        self._ViewCodeSequence.append(item)
        if "ViewCodeSequence" not in self._dataset:
            self._dataset.ViewCodeSequence = pydicom.Sequence()
        self._dataset.ViewCodeSequence.append(item.to_dataset())
