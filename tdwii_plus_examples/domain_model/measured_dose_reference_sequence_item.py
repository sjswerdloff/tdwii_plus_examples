from decimal import Decimal
from typing import Any, List, Optional  # noqa

import pydicom


class MeasuredDoseReferenceSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def DoseUnits(self) -> Optional[str]:
        if "DoseUnits" in self._dataset:
            return self._dataset.DoseUnits
        return None

    @DoseUnits.setter
    def DoseUnits(self, value: Optional[str]):
        if value is None:
            if "DoseUnits" in self._dataset:
                del self._dataset.DoseUnits
        else:
            self._dataset.DoseUnits = value

    @property
    def MeasuredDoseDescription(self) -> Optional[str]:
        if "MeasuredDoseDescription" in self._dataset:
            return self._dataset.MeasuredDoseDescription
        return None

    @MeasuredDoseDescription.setter
    def MeasuredDoseDescription(self, value: Optional[str]):
        if value is None:
            if "MeasuredDoseDescription" in self._dataset:
                del self._dataset.MeasuredDoseDescription
        else:
            self._dataset.MeasuredDoseDescription = value

    @property
    def MeasuredDoseType(self) -> Optional[str]:
        if "MeasuredDoseType" in self._dataset:
            return self._dataset.MeasuredDoseType
        return None

    @MeasuredDoseType.setter
    def MeasuredDoseType(self, value: Optional[str]):
        if value is None:
            if "MeasuredDoseType" in self._dataset:
                del self._dataset.MeasuredDoseType
        else:
            self._dataset.MeasuredDoseType = value

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
    def MeasuredDoseReferenceNumber(self) -> Optional[int]:
        if "MeasuredDoseReferenceNumber" in self._dataset:
            return self._dataset.MeasuredDoseReferenceNumber
        return None

    @MeasuredDoseReferenceNumber.setter
    def MeasuredDoseReferenceNumber(self, value: Optional[int]):
        if value is None:
            if "MeasuredDoseReferenceNumber" in self._dataset:
                del self._dataset.MeasuredDoseReferenceNumber
        else:
            self._dataset.MeasuredDoseReferenceNumber = value

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
