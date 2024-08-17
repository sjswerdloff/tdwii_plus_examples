from typing import Any, List, Optional

import pydicom


class PrescriptionOverviewSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ReferencedROINumber(self) -> Optional[int]:
        if "ReferencedROINumber" in self._dataset:
            return self._dataset.ReferencedROINumber
        return None

    @ReferencedROINumber.setter
    def ReferencedROINumber(self, value: Optional[int]):
        if value is None:
            if "ReferencedROINumber" in self._dataset:
                del self._dataset.ReferencedROINumber
        else:
            self._dataset.ReferencedROINumber = value

    @property
    def TotalPrescriptionDose(self) -> Optional[float]:
        if "TotalPrescriptionDose" in self._dataset:
            return self._dataset.TotalPrescriptionDose
        return None

    @TotalPrescriptionDose.setter
    def TotalPrescriptionDose(self, value: Optional[float]):
        if value is None:
            if "TotalPrescriptionDose" in self._dataset:
                del self._dataset.TotalPrescriptionDose
        else:
            self._dataset.TotalPrescriptionDose = value

    @property
    def EntityLongLabel(self) -> Optional[str]:
        if "EntityLongLabel" in self._dataset:
            return self._dataset.EntityLongLabel
        return None

    @EntityLongLabel.setter
    def EntityLongLabel(self, value: Optional[str]):
        if value is None:
            if "EntityLongLabel" in self._dataset:
                del self._dataset.EntityLongLabel
        else:
            self._dataset.EntityLongLabel = value
