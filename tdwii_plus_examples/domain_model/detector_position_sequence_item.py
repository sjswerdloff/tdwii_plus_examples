from decimal import Decimal
from typing import Any, List, Optional  # noqa

import pydicom


class DetectorPositionSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def DetectorPrimaryAngle(self) -> Optional[Decimal]:
        if "DetectorPrimaryAngle" in self._dataset:
            return self._dataset.DetectorPrimaryAngle
        return None

    @DetectorPrimaryAngle.setter
    def DetectorPrimaryAngle(self, value: Optional[Decimal]):
        if value is None:
            if "DetectorPrimaryAngle" in self._dataset:
                del self._dataset.DetectorPrimaryAngle
        else:
            self._dataset.DetectorPrimaryAngle = value

    @property
    def DetectorSecondaryAngle(self) -> Optional[Decimal]:
        if "DetectorSecondaryAngle" in self._dataset:
            return self._dataset.DetectorSecondaryAngle
        return None

    @DetectorSecondaryAngle.setter
    def DetectorSecondaryAngle(self, value: Optional[Decimal]):
        if value is None:
            if "DetectorSecondaryAngle" in self._dataset:
                del self._dataset.DetectorSecondaryAngle
        else:
            self._dataset.DetectorSecondaryAngle = value
