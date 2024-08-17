from typing import Any, List, Optional

import pydicom


class RTImageFrameGeneralContentSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def FrameType(self) -> Optional[List[str]]:
        if "FrameType" in self._dataset:
            return self._dataset.FrameType
        return None

    @FrameType.setter
    def FrameType(self, value: Optional[List[str]]):
        if value is None:
            if "FrameType" in self._dataset:
                del self._dataset.FrameType
        else:
            self._dataset.FrameType = value

    @property
    def StartCumulativeMeterset(self) -> Optional[float]:
        if "StartCumulativeMeterset" in self._dataset:
            return self._dataset.StartCumulativeMeterset
        return None

    @StartCumulativeMeterset.setter
    def StartCumulativeMeterset(self, value: Optional[float]):
        if value is None:
            if "StartCumulativeMeterset" in self._dataset:
                del self._dataset.StartCumulativeMeterset
        else:
            self._dataset.StartCumulativeMeterset = value

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
