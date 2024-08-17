from decimal import Decimal
from typing import Any, List, Optional

import pydicom


class RotationInformationSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

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
    def TableHeight(self) -> Optional[Decimal]:
        if "TableHeight" in self._dataset:
            return self._dataset.TableHeight
        return None

    @TableHeight.setter
    def TableHeight(self, value: Optional[Decimal]):
        if value is None:
            if "TableHeight" in self._dataset:
                del self._dataset.TableHeight
        else:
            self._dataset.TableHeight = value

    @property
    def TableTraverse(self) -> Optional[Decimal]:
        if "TableTraverse" in self._dataset:
            return self._dataset.TableTraverse
        return None

    @TableTraverse.setter
    def TableTraverse(self, value: Optional[Decimal]):
        if value is None:
            if "TableTraverse" in self._dataset:
                del self._dataset.TableTraverse
        else:
            self._dataset.TableTraverse = value

    @property
    def RotationDirection(self) -> Optional[str]:
        if "RotationDirection" in self._dataset:
            return self._dataset.RotationDirection
        return None

    @RotationDirection.setter
    def RotationDirection(self, value: Optional[str]):
        if value is None:
            if "RotationDirection" in self._dataset:
                del self._dataset.RotationDirection
        else:
            self._dataset.RotationDirection = value

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
    def ScanArc(self) -> Optional[Decimal]:
        if "ScanArc" in self._dataset:
            return self._dataset.ScanArc
        return None

    @ScanArc.setter
    def ScanArc(self, value: Optional[Decimal]):
        if value is None:
            if "ScanArc" in self._dataset:
                del self._dataset.ScanArc
        else:
            self._dataset.ScanArc = value

    @property
    def AngularStep(self) -> Optional[Decimal]:
        if "AngularStep" in self._dataset:
            return self._dataset.AngularStep
        return None

    @AngularStep.setter
    def AngularStep(self, value: Optional[Decimal]):
        if value is None:
            if "AngularStep" in self._dataset:
                del self._dataset.AngularStep
        else:
            self._dataset.AngularStep = value

    @property
    def ActualFrameDuration(self) -> Optional[int]:
        if "ActualFrameDuration" in self._dataset:
            return self._dataset.ActualFrameDuration
        return None

    @ActualFrameDuration.setter
    def ActualFrameDuration(self, value: Optional[int]):
        if value is None:
            if "ActualFrameDuration" in self._dataset:
                del self._dataset.ActualFrameDuration
        else:
            self._dataset.ActualFrameDuration = value

    @property
    def NumberOfFramesInRotation(self) -> Optional[int]:
        if "NumberOfFramesInRotation" in self._dataset:
            return self._dataset.NumberOfFramesInRotation
        return None

    @NumberOfFramesInRotation.setter
    def NumberOfFramesInRotation(self, value: Optional[int]):
        if value is None:
            if "NumberOfFramesInRotation" in self._dataset:
                del self._dataset.NumberOfFramesInRotation
        else:
            self._dataset.NumberOfFramesInRotation = value

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
