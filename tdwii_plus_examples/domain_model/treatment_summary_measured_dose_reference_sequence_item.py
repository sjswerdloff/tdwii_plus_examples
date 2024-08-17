from decimal import Decimal
from typing import Any, List, Optional

import pydicom


class TreatmentSummaryMeasuredDoseReferenceSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def CumulativeDoseToDoseReference(self) -> Optional[Decimal]:
        if "CumulativeDoseToDoseReference" in self._dataset:
            return self._dataset.CumulativeDoseToDoseReference
        return None

    @CumulativeDoseToDoseReference.setter
    def CumulativeDoseToDoseReference(self, value: Optional[Decimal]):
        if value is None:
            if "CumulativeDoseToDoseReference" in self._dataset:
                del self._dataset.CumulativeDoseToDoseReference
        else:
            self._dataset.CumulativeDoseToDoseReference = value

    @property
    def DoseReferenceDescription(self) -> Optional[str]:
        if "DoseReferenceDescription" in self._dataset:
            return self._dataset.DoseReferenceDescription
        return None

    @DoseReferenceDescription.setter
    def DoseReferenceDescription(self, value: Optional[str]):
        if value is None:
            if "DoseReferenceDescription" in self._dataset:
                del self._dataset.DoseReferenceDescription
        else:
            self._dataset.DoseReferenceDescription = value

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
