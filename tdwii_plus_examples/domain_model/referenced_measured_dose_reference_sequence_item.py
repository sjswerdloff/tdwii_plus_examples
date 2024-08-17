from decimal import Decimal
from typing import Any, List, Optional  # noqa

import pydicom


class ReferencedMeasuredDoseReferenceSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def MeasuredDoseValue(self) -> Optional[Decimal]:
        if "MeasuredDoseValue" in self._dataset:
            return self._dataset.MeasuredDoseValue
        return None

    @MeasuredDoseValue.setter
    def MeasuredDoseValue(self, value: Optional[Decimal]):
        if value is None:
            if "MeasuredDoseValue" in self._dataset:
                del self._dataset.MeasuredDoseValue
        else:
            self._dataset.MeasuredDoseValue = value

    @property
    def ReferencedMeasuredDoseReferenceNumber(self) -> Optional[int]:
        if "ReferencedMeasuredDoseReferenceNumber" in self._dataset:
            return self._dataset.ReferencedMeasuredDoseReferenceNumber
        return None

    @ReferencedMeasuredDoseReferenceNumber.setter
    def ReferencedMeasuredDoseReferenceNumber(self, value: Optional[int]):
        if value is None:
            if "ReferencedMeasuredDoseReferenceNumber" in self._dataset:
                del self._dataset.ReferencedMeasuredDoseReferenceNumber
        else:
            self._dataset.ReferencedMeasuredDoseReferenceNumber = value

    @property
    def ReferencedDoseReferenceNumber(self) -> Optional[int]:
        if "ReferencedDoseReferenceNumber" in self._dataset:
            return self._dataset.ReferencedDoseReferenceNumber
        return None

    @ReferencedDoseReferenceNumber.setter
    def ReferencedDoseReferenceNumber(self, value: Optional[int]):
        if value is None:
            if "ReferencedDoseReferenceNumber" in self._dataset:
                del self._dataset.ReferencedDoseReferenceNumber
        else:
            self._dataset.ReferencedDoseReferenceNumber = value
