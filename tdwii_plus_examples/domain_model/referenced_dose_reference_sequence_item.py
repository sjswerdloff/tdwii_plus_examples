from decimal import Decimal
from typing import Any, List, Optional

import pydicom


class ReferencedDoseReferenceSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def CumulativeDoseReferenceCoefficient(self) -> Optional[Decimal]:
        if "CumulativeDoseReferenceCoefficient" in self._dataset:
            return self._dataset.CumulativeDoseReferenceCoefficient
        return None

    @CumulativeDoseReferenceCoefficient.setter
    def CumulativeDoseReferenceCoefficient(self, value: Optional[Decimal]):
        if value is None:
            if "CumulativeDoseReferenceCoefficient" in self._dataset:
                del self._dataset.CumulativeDoseReferenceCoefficient
        else:
            self._dataset.CumulativeDoseReferenceCoefficient = value

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
