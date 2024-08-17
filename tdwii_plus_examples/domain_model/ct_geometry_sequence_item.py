from decimal import Decimal
from typing import Any, List, Optional

import pydicom


class CTGeometrySequenceItem:
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
    def DistanceSourceToDataCollectionCenter(self) -> Optional[float]:
        if "DistanceSourceToDataCollectionCenter" in self._dataset:
            return self._dataset.DistanceSourceToDataCollectionCenter
        return None

    @DistanceSourceToDataCollectionCenter.setter
    def DistanceSourceToDataCollectionCenter(self, value: Optional[float]):
        if value is None:
            if "DistanceSourceToDataCollectionCenter" in self._dataset:
                del self._dataset.DistanceSourceToDataCollectionCenter
        else:
            self._dataset.DistanceSourceToDataCollectionCenter = value

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
