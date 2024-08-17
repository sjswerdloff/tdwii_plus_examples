from decimal import Decimal
from typing import Any, List, Optional  # noqa

import pydicom


class ReferencedBrachyApplicationSetupSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ReferencedDoseReferenceUID(self) -> Optional[str]:
        if "ReferencedDoseReferenceUID" in self._dataset:
            return self._dataset.ReferencedDoseReferenceUID
        return None

    @ReferencedDoseReferenceUID.setter
    def ReferencedDoseReferenceUID(self, value: Optional[str]):
        if value is None:
            if "ReferencedDoseReferenceUID" in self._dataset:
                del self._dataset.ReferencedDoseReferenceUID
        else:
            self._dataset.ReferencedDoseReferenceUID = value

    @property
    def BrachyApplicationSetupDoseSpecificationPoint(self) -> Optional[List[Decimal]]:
        if "BrachyApplicationSetupDoseSpecificationPoint" in self._dataset:
            return self._dataset.BrachyApplicationSetupDoseSpecificationPoint
        return None

    @BrachyApplicationSetupDoseSpecificationPoint.setter
    def BrachyApplicationSetupDoseSpecificationPoint(self, value: Optional[List[Decimal]]):
        if value is None:
            if "BrachyApplicationSetupDoseSpecificationPoint" in self._dataset:
                del self._dataset.BrachyApplicationSetupDoseSpecificationPoint
        else:
            self._dataset.BrachyApplicationSetupDoseSpecificationPoint = value

    @property
    def BrachyApplicationSetupDose(self) -> Optional[Decimal]:
        if "BrachyApplicationSetupDose" in self._dataset:
            return self._dataset.BrachyApplicationSetupDose
        return None

    @BrachyApplicationSetupDose.setter
    def BrachyApplicationSetupDose(self, value: Optional[Decimal]):
        if value is None:
            if "BrachyApplicationSetupDose" in self._dataset:
                del self._dataset.BrachyApplicationSetupDose
        else:
            self._dataset.BrachyApplicationSetupDose = value

    @property
    def ReferencedBrachyApplicationSetupNumber(self) -> Optional[int]:
        if "ReferencedBrachyApplicationSetupNumber" in self._dataset:
            return self._dataset.ReferencedBrachyApplicationSetupNumber
        return None

    @ReferencedBrachyApplicationSetupNumber.setter
    def ReferencedBrachyApplicationSetupNumber(self, value: Optional[int]):
        if value is None:
            if "ReferencedBrachyApplicationSetupNumber" in self._dataset:
                del self._dataset.ReferencedBrachyApplicationSetupNumber
        else:
            self._dataset.ReferencedBrachyApplicationSetupNumber = value
