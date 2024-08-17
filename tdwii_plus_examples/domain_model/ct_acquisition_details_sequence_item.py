from decimal import Decimal
from typing import Any, List, Optional

import pydicom


class CTAcquisitionDetailsSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def DataCollectionDiameter(self) -> Optional[Decimal]:
        if "DataCollectionDiameter" in self._dataset:
            return self._dataset.DataCollectionDiameter
        return None

    @DataCollectionDiameter.setter
    def DataCollectionDiameter(self, value: Optional[Decimal]):
        if value is None:
            if "DataCollectionDiameter" in self._dataset:
                del self._dataset.DataCollectionDiameter
        else:
            self._dataset.DataCollectionDiameter = value

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
    def RevolutionTime(self) -> Optional[float]:
        if "RevolutionTime" in self._dataset:
            return self._dataset.RevolutionTime
        return None

    @RevolutionTime.setter
    def RevolutionTime(self, value: Optional[float]):
        if value is None:
            if "RevolutionTime" in self._dataset:
                del self._dataset.RevolutionTime
        else:
            self._dataset.RevolutionTime = value

    @property
    def SingleCollimationWidth(self) -> Optional[float]:
        if "SingleCollimationWidth" in self._dataset:
            return self._dataset.SingleCollimationWidth
        return None

    @SingleCollimationWidth.setter
    def SingleCollimationWidth(self, value: Optional[float]):
        if value is None:
            if "SingleCollimationWidth" in self._dataset:
                del self._dataset.SingleCollimationWidth
        else:
            self._dataset.SingleCollimationWidth = value

    @property
    def TotalCollimationWidth(self) -> Optional[float]:
        if "TotalCollimationWidth" in self._dataset:
            return self._dataset.TotalCollimationWidth
        return None

    @TotalCollimationWidth.setter
    def TotalCollimationWidth(self, value: Optional[float]):
        if value is None:
            if "TotalCollimationWidth" in self._dataset:
                del self._dataset.TotalCollimationWidth
        else:
            self._dataset.TotalCollimationWidth = value

    @property
    def ReferencedPathIndex(self) -> Optional[List[int]]:
        if "ReferencedPathIndex" in self._dataset:
            return self._dataset.ReferencedPathIndex
        return None

    @ReferencedPathIndex.setter
    def ReferencedPathIndex(self, value: Optional[List[int]]):
        if value is None:
            if "ReferencedPathIndex" in self._dataset:
                del self._dataset.ReferencedPathIndex
        else:
            self._dataset.ReferencedPathIndex = value
