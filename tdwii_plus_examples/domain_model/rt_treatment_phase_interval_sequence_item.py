from typing import Any, List, Optional  # noqa

import pydicom


class RTTreatmentPhaseIntervalSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def BasisRTTreatmentPhaseIndex(self) -> Optional[int]:
        if "BasisRTTreatmentPhaseIndex" in self._dataset:
            return self._dataset.BasisRTTreatmentPhaseIndex
        return None

    @BasisRTTreatmentPhaseIndex.setter
    def BasisRTTreatmentPhaseIndex(self, value: Optional[int]):
        if value is None:
            if "BasisRTTreatmentPhaseIndex" in self._dataset:
                del self._dataset.BasisRTTreatmentPhaseIndex
        else:
            self._dataset.BasisRTTreatmentPhaseIndex = value

    @property
    def RelatedRTTreatmentPhaseIndex(self) -> Optional[int]:
        if "RelatedRTTreatmentPhaseIndex" in self._dataset:
            return self._dataset.RelatedRTTreatmentPhaseIndex
        return None

    @RelatedRTTreatmentPhaseIndex.setter
    def RelatedRTTreatmentPhaseIndex(self, value: Optional[int]):
        if value is None:
            if "RelatedRTTreatmentPhaseIndex" in self._dataset:
                del self._dataset.RelatedRTTreatmentPhaseIndex
        else:
            self._dataset.RelatedRTTreatmentPhaseIndex = value

    @property
    def TemporalRelationshipIntervalAnchor(self) -> Optional[str]:
        if "TemporalRelationshipIntervalAnchor" in self._dataset:
            return self._dataset.TemporalRelationshipIntervalAnchor
        return None

    @TemporalRelationshipIntervalAnchor.setter
    def TemporalRelationshipIntervalAnchor(self, value: Optional[str]):
        if value is None:
            if "TemporalRelationshipIntervalAnchor" in self._dataset:
                del self._dataset.TemporalRelationshipIntervalAnchor
        else:
            self._dataset.TemporalRelationshipIntervalAnchor = value

    @property
    def MinimumNumberOfIntervalDays(self) -> Optional[float]:
        if "MinimumNumberOfIntervalDays" in self._dataset:
            return self._dataset.MinimumNumberOfIntervalDays
        return None

    @MinimumNumberOfIntervalDays.setter
    def MinimumNumberOfIntervalDays(self, value: Optional[float]):
        if value is None:
            if "MinimumNumberOfIntervalDays" in self._dataset:
                del self._dataset.MinimumNumberOfIntervalDays
        else:
            self._dataset.MinimumNumberOfIntervalDays = value

    @property
    def MaximumNumberOfIntervalDays(self) -> Optional[float]:
        if "MaximumNumberOfIntervalDays" in self._dataset:
            return self._dataset.MaximumNumberOfIntervalDays
        return None

    @MaximumNumberOfIntervalDays.setter
    def MaximumNumberOfIntervalDays(self, value: Optional[float]):
        if value is None:
            if "MaximumNumberOfIntervalDays" in self._dataset:
                del self._dataset.MaximumNumberOfIntervalDays
        else:
            self._dataset.MaximumNumberOfIntervalDays = value
