from decimal import Decimal
from typing import Any, List, Optional

import pydicom


class CalculatedDoseReferenceSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def CalculatedDoseReferenceNumber(self) -> Optional[int]:
        if "CalculatedDoseReferenceNumber" in self._dataset:
            return self._dataset.CalculatedDoseReferenceNumber
        return None

    @CalculatedDoseReferenceNumber.setter
    def CalculatedDoseReferenceNumber(self, value: Optional[int]):
        if value is None:
            if "CalculatedDoseReferenceNumber" in self._dataset:
                del self._dataset.CalculatedDoseReferenceNumber
        else:
            self._dataset.CalculatedDoseReferenceNumber = value

    @property
    def CalculatedDoseReferenceDescription(self) -> Optional[str]:
        if "CalculatedDoseReferenceDescription" in self._dataset:
            return self._dataset.CalculatedDoseReferenceDescription
        return None

    @CalculatedDoseReferenceDescription.setter
    def CalculatedDoseReferenceDescription(self, value: Optional[str]):
        if value is None:
            if "CalculatedDoseReferenceDescription" in self._dataset:
                del self._dataset.CalculatedDoseReferenceDescription
        else:
            self._dataset.CalculatedDoseReferenceDescription = value

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
