from typing import Any, List, Optional  # noqa

import pydicom


class RTRadiationSalvageRecordControlPointSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def RTControlPointIndex(self) -> Optional[int]:
        if "RTControlPointIndex" in self._dataset:
            return self._dataset.RTControlPointIndex
        return None

    @RTControlPointIndex.setter
    def RTControlPointIndex(self, value: Optional[int]):
        if value is None:
            if "RTControlPointIndex" in self._dataset:
                del self._dataset.RTControlPointIndex
        else:
            self._dataset.RTControlPointIndex = value

    @property
    def ReferencedRadiationGenerationModeIndex(self) -> Optional[int]:
        if "ReferencedRadiationGenerationModeIndex" in self._dataset:
            return self._dataset.ReferencedRadiationGenerationModeIndex
        return None

    @ReferencedRadiationGenerationModeIndex.setter
    def ReferencedRadiationGenerationModeIndex(self, value: Optional[int]):
        if value is None:
            if "ReferencedRadiationGenerationModeIndex" in self._dataset:
                del self._dataset.ReferencedRadiationGenerationModeIndex
        else:
            self._dataset.ReferencedRadiationGenerationModeIndex = value

    @property
    def ReferencedTreatmentPositionIndex(self) -> Optional[int]:
        if "ReferencedTreatmentPositionIndex" in self._dataset:
            return self._dataset.ReferencedTreatmentPositionIndex
        return None

    @ReferencedTreatmentPositionIndex.setter
    def ReferencedTreatmentPositionIndex(self, value: Optional[int]):
        if value is None:
            if "ReferencedTreatmentPositionIndex" in self._dataset:
                del self._dataset.ReferencedTreatmentPositionIndex
        else:
            self._dataset.ReferencedTreatmentPositionIndex = value

    @property
    def CumulativeMeterset(self) -> Optional[float]:
        if "CumulativeMeterset" in self._dataset:
            return self._dataset.CumulativeMeterset
        return None

    @CumulativeMeterset.setter
    def CumulativeMeterset(self, value: Optional[float]):
        if value is None:
            if "CumulativeMeterset" in self._dataset:
                del self._dataset.CumulativeMeterset
        else:
            self._dataset.CumulativeMeterset = value

    @property
    def RecordedRTControlPointDateTime(self) -> Optional[str]:
        if "RecordedRTControlPointDateTime" in self._dataset:
            return self._dataset.RecordedRTControlPointDateTime
        return None

    @RecordedRTControlPointDateTime.setter
    def RecordedRTControlPointDateTime(self, value: Optional[str]):
        if value is None:
            if "RecordedRTControlPointDateTime" in self._dataset:
                del self._dataset.RecordedRTControlPointDateTime
        else:
            self._dataset.RecordedRTControlPointDateTime = value

    @property
    def ReferencedRadiationRTControlPointIndex(self) -> Optional[int]:
        if "ReferencedRadiationRTControlPointIndex" in self._dataset:
            return self._dataset.ReferencedRadiationRTControlPointIndex
        return None

    @ReferencedRadiationRTControlPointIndex.setter
    def ReferencedRadiationRTControlPointIndex(self, value: Optional[int]):
        if value is None:
            if "ReferencedRadiationRTControlPointIndex" in self._dataset:
                del self._dataset.ReferencedRadiationRTControlPointIndex
        else:
            self._dataset.ReferencedRadiationRTControlPointIndex = value
