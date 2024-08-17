from decimal import Decimal
from typing import Any, List, Optional  # noqa

import pydicom


class ReferencedCalculatedDoseReferenceSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def CalculatedDoseReferenceDoseValue(self) -> Optional[Decimal]:
        if "CalculatedDoseReferenceDoseValue" in self._dataset:
            return self._dataset.CalculatedDoseReferenceDoseValue
        return None

    @CalculatedDoseReferenceDoseValue.setter
    def CalculatedDoseReferenceDoseValue(self, value: Optional[Decimal]):
        if value is None:
            if "CalculatedDoseReferenceDoseValue" in self._dataset:
                del self._dataset.CalculatedDoseReferenceDoseValue
        else:
            self._dataset.CalculatedDoseReferenceDoseValue = value

    @property
    def ReferencedCalculatedDoseReferenceNumber(self) -> Optional[int]:
        if "ReferencedCalculatedDoseReferenceNumber" in self._dataset:
            return self._dataset.ReferencedCalculatedDoseReferenceNumber
        return None

    @ReferencedCalculatedDoseReferenceNumber.setter
    def ReferencedCalculatedDoseReferenceNumber(self, value: Optional[int]):
        if value is None:
            if "ReferencedCalculatedDoseReferenceNumber" in self._dataset:
                del self._dataset.ReferencedCalculatedDoseReferenceNumber
        else:
            self._dataset.ReferencedCalculatedDoseReferenceNumber = value

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
