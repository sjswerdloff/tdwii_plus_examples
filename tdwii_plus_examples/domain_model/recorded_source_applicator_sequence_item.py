from decimal import Decimal
from typing import Any, List, Optional  # noqa

import pydicom


class RecordedSourceApplicatorSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ReferencedSourceApplicatorNumber(self) -> Optional[int]:
        if "ReferencedSourceApplicatorNumber" in self._dataset:
            return self._dataset.ReferencedSourceApplicatorNumber
        return None

    @ReferencedSourceApplicatorNumber.setter
    def ReferencedSourceApplicatorNumber(self, value: Optional[int]):
        if value is None:
            if "ReferencedSourceApplicatorNumber" in self._dataset:
                del self._dataset.ReferencedSourceApplicatorNumber
        else:
            self._dataset.ReferencedSourceApplicatorNumber = value

    @property
    def SourceApplicatorTipLength(self) -> Optional[Decimal]:
        if "SourceApplicatorTipLength" in self._dataset:
            return self._dataset.SourceApplicatorTipLength
        return None

    @SourceApplicatorTipLength.setter
    def SourceApplicatorTipLength(self, value: Optional[Decimal]):
        if value is None:
            if "SourceApplicatorTipLength" in self._dataset:
                del self._dataset.SourceApplicatorTipLength
        else:
            self._dataset.SourceApplicatorTipLength = value

    @property
    def SourceApplicatorID(self) -> Optional[str]:
        if "SourceApplicatorID" in self._dataset:
            return self._dataset.SourceApplicatorID
        return None

    @SourceApplicatorID.setter
    def SourceApplicatorID(self, value: Optional[str]):
        if value is None:
            if "SourceApplicatorID" in self._dataset:
                del self._dataset.SourceApplicatorID
        else:
            self._dataset.SourceApplicatorID = value

    @property
    def SourceApplicatorType(self) -> Optional[str]:
        if "SourceApplicatorType" in self._dataset:
            return self._dataset.SourceApplicatorType
        return None

    @SourceApplicatorType.setter
    def SourceApplicatorType(self, value: Optional[str]):
        if value is None:
            if "SourceApplicatorType" in self._dataset:
                del self._dataset.SourceApplicatorType
        else:
            self._dataset.SourceApplicatorType = value

    @property
    def SourceApplicatorName(self) -> Optional[str]:
        if "SourceApplicatorName" in self._dataset:
            return self._dataset.SourceApplicatorName
        return None

    @SourceApplicatorName.setter
    def SourceApplicatorName(self, value: Optional[str]):
        if value is None:
            if "SourceApplicatorName" in self._dataset:
                del self._dataset.SourceApplicatorName
        else:
            self._dataset.SourceApplicatorName = value

    @property
    def SourceApplicatorLength(self) -> Optional[Decimal]:
        if "SourceApplicatorLength" in self._dataset:
            return self._dataset.SourceApplicatorLength
        return None

    @SourceApplicatorLength.setter
    def SourceApplicatorLength(self, value: Optional[Decimal]):
        if value is None:
            if "SourceApplicatorLength" in self._dataset:
                del self._dataset.SourceApplicatorLength
        else:
            self._dataset.SourceApplicatorLength = value

    @property
    def SourceApplicatorManufacturer(self) -> Optional[str]:
        if "SourceApplicatorManufacturer" in self._dataset:
            return self._dataset.SourceApplicatorManufacturer
        return None

    @SourceApplicatorManufacturer.setter
    def SourceApplicatorManufacturer(self, value: Optional[str]):
        if value is None:
            if "SourceApplicatorManufacturer" in self._dataset:
                del self._dataset.SourceApplicatorManufacturer
        else:
            self._dataset.SourceApplicatorManufacturer = value

    @property
    def SourceApplicatorStepSize(self) -> Optional[Decimal]:
        if "SourceApplicatorStepSize" in self._dataset:
            return self._dataset.SourceApplicatorStepSize
        return None

    @SourceApplicatorStepSize.setter
    def SourceApplicatorStepSize(self, value: Optional[Decimal]):
        if value is None:
            if "SourceApplicatorStepSize" in self._dataset:
                del self._dataset.SourceApplicatorStepSize
        else:
            self._dataset.SourceApplicatorStepSize = value
