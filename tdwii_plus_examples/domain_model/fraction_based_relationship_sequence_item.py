from typing import Any, List, Optional

import pydicom


class FractionBasedRelationshipSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ReferencedRTPrescriptionIndex(self) -> Optional[int]:
        if "ReferencedRTPrescriptionIndex" in self._dataset:
            return self._dataset.ReferencedRTPrescriptionIndex
        return None

    @ReferencedRTPrescriptionIndex.setter
    def ReferencedRTPrescriptionIndex(self, value: Optional[int]):
        if value is None:
            if "ReferencedRTPrescriptionIndex" in self._dataset:
                del self._dataset.ReferencedRTPrescriptionIndex
        else:
            self._dataset.ReferencedRTPrescriptionIndex = value

    @property
    def NumberOfIntervalFractions(self) -> Optional[int]:
        if "NumberOfIntervalFractions" in self._dataset:
            return self._dataset.NumberOfIntervalFractions
        return None

    @NumberOfIntervalFractions.setter
    def NumberOfIntervalFractions(self, value: Optional[int]):
        if value is None:
            if "NumberOfIntervalFractions" in self._dataset:
                del self._dataset.NumberOfIntervalFractions
        else:
            self._dataset.NumberOfIntervalFractions = value

    @property
    def FractionBasedRelationshipIntervalAnchor(self) -> Optional[str]:
        if "FractionBasedRelationshipIntervalAnchor" in self._dataset:
            return self._dataset.FractionBasedRelationshipIntervalAnchor
        return None

    @FractionBasedRelationshipIntervalAnchor.setter
    def FractionBasedRelationshipIntervalAnchor(self, value: Optional[str]):
        if value is None:
            if "FractionBasedRelationshipIntervalAnchor" in self._dataset:
                del self._dataset.FractionBasedRelationshipIntervalAnchor
        else:
            self._dataset.FractionBasedRelationshipIntervalAnchor = value
