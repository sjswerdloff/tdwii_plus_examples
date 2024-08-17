from decimal import Decimal
from typing import Any, List, Optional  # noqa

import pydicom


class XRayGeometrySequenceItem:
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
    def DistanceSourceToIsocenter(self) -> Optional[float]:
        if "DistanceSourceToIsocenter" in self._dataset:
            return self._dataset.DistanceSourceToIsocenter
        return None

    @DistanceSourceToIsocenter.setter
    def DistanceSourceToIsocenter(self, value: Optional[float]):
        if value is None:
            if "DistanceSourceToIsocenter" in self._dataset:
                del self._dataset.DistanceSourceToIsocenter
        else:
            self._dataset.DistanceSourceToIsocenter = value
