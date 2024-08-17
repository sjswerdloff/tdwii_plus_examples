from typing import Any, List, Optional

import pydicom


class FractionStatusSummarySequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def TreatmentTerminationStatus(self) -> Optional[str]:
        if "TreatmentTerminationStatus" in self._dataset:
            return self._dataset.TreatmentTerminationStatus
        return None

    @TreatmentTerminationStatus.setter
    def TreatmentTerminationStatus(self, value: Optional[str]):
        if value is None:
            if "TreatmentTerminationStatus" in self._dataset:
                del self._dataset.TreatmentTerminationStatus
        else:
            self._dataset.TreatmentTerminationStatus = value

    @property
    def ReferencedFractionNumber(self) -> Optional[int]:
        if "ReferencedFractionNumber" in self._dataset:
            return self._dataset.ReferencedFractionNumber
        return None

    @ReferencedFractionNumber.setter
    def ReferencedFractionNumber(self, value: Optional[int]):
        if value is None:
            if "ReferencedFractionNumber" in self._dataset:
                del self._dataset.ReferencedFractionNumber
        else:
            self._dataset.ReferencedFractionNumber = value

    @property
    def TreatmentDate(self) -> Optional[str]:
        if "TreatmentDate" in self._dataset:
            return self._dataset.TreatmentDate
        return None

    @TreatmentDate.setter
    def TreatmentDate(self, value: Optional[str]):
        if value is None:
            if "TreatmentDate" in self._dataset:
                del self._dataset.TreatmentDate
        else:
            self._dataset.TreatmentDate = value

    @property
    def TreatmentTime(self) -> Optional[str]:
        if "TreatmentTime" in self._dataset:
            return self._dataset.TreatmentTime
        return None

    @TreatmentTime.setter
    def TreatmentTime(self, value: Optional[str]):
        if value is None:
            if "TreatmentTime" in self._dataset:
                del self._dataset.TreatmentTime
        else:
            self._dataset.TreatmentTime = value
