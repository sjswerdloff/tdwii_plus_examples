from typing import Any, List, Optional  # noqa

import pydicom


class ReferencedRTTreatmentPhaseSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ReferencedRTTreatmentPhaseIndex(self) -> Optional[int]:
        if "ReferencedRTTreatmentPhaseIndex" in self._dataset:
            return self._dataset.ReferencedRTTreatmentPhaseIndex
        return None

    @ReferencedRTTreatmentPhaseIndex.setter
    def ReferencedRTTreatmentPhaseIndex(self, value: Optional[int]):
        if value is None:
            if "ReferencedRTTreatmentPhaseIndex" in self._dataset:
                del self._dataset.ReferencedRTTreatmentPhaseIndex
        else:
            self._dataset.ReferencedRTTreatmentPhaseIndex = value
