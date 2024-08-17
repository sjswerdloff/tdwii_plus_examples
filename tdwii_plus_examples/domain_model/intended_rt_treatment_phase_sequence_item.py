from typing import Any, List, Optional

import pydicom


class IntendedRTTreatmentPhaseSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def EntityLabel(self) -> Optional[str]:
        if "EntityLabel" in self._dataset:
            return self._dataset.EntityLabel
        return None

    @EntityLabel.setter
    def EntityLabel(self, value: Optional[str]):
        if value is None:
            if "EntityLabel" in self._dataset:
                del self._dataset.EntityLabel
        else:
            self._dataset.EntityLabel = value

    @property
    def EntityName(self) -> Optional[str]:
        if "EntityName" in self._dataset:
            return self._dataset.EntityName
        return None

    @EntityName.setter
    def EntityName(self, value: Optional[str]):
        if value is None:
            if "EntityName" in self._dataset:
                del self._dataset.EntityName
        else:
            self._dataset.EntityName = value

    @property
    def EntityDescription(self) -> Optional[str]:
        if "EntityDescription" in self._dataset:
            return self._dataset.EntityDescription
        return None

    @EntityDescription.setter
    def EntityDescription(self, value: Optional[str]):
        if value is None:
            if "EntityDescription" in self._dataset:
                del self._dataset.EntityDescription
        else:
            self._dataset.EntityDescription = value

    @property
    def RTTreatmentPhaseIndex(self) -> Optional[int]:
        if "RTTreatmentPhaseIndex" in self._dataset:
            return self._dataset.RTTreatmentPhaseIndex
        return None

    @RTTreatmentPhaseIndex.setter
    def RTTreatmentPhaseIndex(self, value: Optional[int]):
        if value is None:
            if "RTTreatmentPhaseIndex" in self._dataset:
                del self._dataset.RTTreatmentPhaseIndex
        else:
            self._dataset.RTTreatmentPhaseIndex = value

    @property
    def RTTreatmentPhaseUID(self) -> Optional[str]:
        if "RTTreatmentPhaseUID" in self._dataset:
            return self._dataset.RTTreatmentPhaseUID
        return None

    @RTTreatmentPhaseUID.setter
    def RTTreatmentPhaseUID(self, value: Optional[str]):
        if value is None:
            if "RTTreatmentPhaseUID" in self._dataset:
                del self._dataset.RTTreatmentPhaseUID
        else:
            self._dataset.RTTreatmentPhaseUID = value

    @property
    def IntendedPhaseStartDate(self) -> Optional[str]:
        if "IntendedPhaseStartDate" in self._dataset:
            return self._dataset.IntendedPhaseStartDate
        return None

    @IntendedPhaseStartDate.setter
    def IntendedPhaseStartDate(self, value: Optional[str]):
        if value is None:
            if "IntendedPhaseStartDate" in self._dataset:
                del self._dataset.IntendedPhaseStartDate
        else:
            self._dataset.IntendedPhaseStartDate = value

    @property
    def IntendedPhaseEndDate(self) -> Optional[str]:
        if "IntendedPhaseEndDate" in self._dataset:
            return self._dataset.IntendedPhaseEndDate
        return None

    @IntendedPhaseEndDate.setter
    def IntendedPhaseEndDate(self, value: Optional[str]):
        if value is None:
            if "IntendedPhaseEndDate" in self._dataset:
                del self._dataset.IntendedPhaseEndDate
        else:
            self._dataset.IntendedPhaseEndDate = value
