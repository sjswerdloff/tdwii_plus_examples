from decimal import Decimal
from typing import Any, List, Optional  # noqa

import pydicom


class PositionerPositionSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def PositionerPrimaryAngle(self) -> Optional[Decimal]:
        if "PositionerPrimaryAngle" in self._dataset:
            return self._dataset.PositionerPrimaryAngle
        return None

    @PositionerPrimaryAngle.setter
    def PositionerPrimaryAngle(self, value: Optional[Decimal]):
        if value is None:
            if "PositionerPrimaryAngle" in self._dataset:
                del self._dataset.PositionerPrimaryAngle
        else:
            self._dataset.PositionerPrimaryAngle = value

    @property
    def PositionerSecondaryAngle(self) -> Optional[Decimal]:
        if "PositionerSecondaryAngle" in self._dataset:
            return self._dataset.PositionerSecondaryAngle
        return None

    @PositionerSecondaryAngle.setter
    def PositionerSecondaryAngle(self, value: Optional[Decimal]):
        if value is None:
            if "PositionerSecondaryAngle" in self._dataset:
                del self._dataset.PositionerSecondaryAngle
        else:
            self._dataset.PositionerSecondaryAngle = value

    @property
    def ColumnAngulationPatient(self) -> Optional[float]:
        if "ColumnAngulationPatient" in self._dataset:
            return self._dataset.ColumnAngulationPatient
        return None

    @ColumnAngulationPatient.setter
    def ColumnAngulationPatient(self, value: Optional[float]):
        if value is None:
            if "ColumnAngulationPatient" in self._dataset:
                del self._dataset.ColumnAngulationPatient
        else:
            self._dataset.ColumnAngulationPatient = value
