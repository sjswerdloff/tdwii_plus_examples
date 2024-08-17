from typing import Any, List, Optional  # noqa

import pydicom

from .referenced_rt_radiation_sequence_item import ReferencedRTRadiationSequenceItem


class TreatmentPositionGroupSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._ReferencedRTRadiationSequence: List[ReferencedRTRadiationSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def TreatmentPositionGroupLabel(self) -> Optional[str]:
        if "TreatmentPositionGroupLabel" in self._dataset:
            return self._dataset.TreatmentPositionGroupLabel
        return None

    @TreatmentPositionGroupLabel.setter
    def TreatmentPositionGroupLabel(self, value: Optional[str]):
        if value is None:
            if "TreatmentPositionGroupLabel" in self._dataset:
                del self._dataset.TreatmentPositionGroupLabel
        else:
            self._dataset.TreatmentPositionGroupLabel = value

    @property
    def TreatmentPositionGroupUID(self) -> Optional[str]:
        if "TreatmentPositionGroupUID" in self._dataset:
            return self._dataset.TreatmentPositionGroupUID
        return None

    @TreatmentPositionGroupUID.setter
    def TreatmentPositionGroupUID(self, value: Optional[str]):
        if value is None:
            if "TreatmentPositionGroupUID" in self._dataset:
                del self._dataset.TreatmentPositionGroupUID
        else:
            self._dataset.TreatmentPositionGroupUID = value

    @property
    def ReferencedRTRadiationSequence(self) -> Optional[List[ReferencedRTRadiationSequenceItem]]:
        if "ReferencedRTRadiationSequence" in self._dataset:
            if len(self._ReferencedRTRadiationSequence) == len(self._dataset.ReferencedRTRadiationSequence):
                return self._ReferencedRTRadiationSequence
            else:
                return [ReferencedRTRadiationSequenceItem(x) for x in self._dataset.ReferencedRTRadiationSequence]
        return None

    @ReferencedRTRadiationSequence.setter
    def ReferencedRTRadiationSequence(self, value: Optional[List[ReferencedRTRadiationSequenceItem]]):
        if value is None:
            self._ReferencedRTRadiationSequence = []
            if "ReferencedRTRadiationSequence" in self._dataset:
                del self._dataset.ReferencedRTRadiationSequence
        elif not isinstance(value, list) or not all(isinstance(item, ReferencedRTRadiationSequenceItem) for item in value):
            raise ValueError("ReferencedRTRadiationSequence must be a list of ReferencedRTRadiationSequenceItem objects")
        else:
            self._ReferencedRTRadiationSequence = value
            if "ReferencedRTRadiationSequence" not in self._dataset:
                self._dataset.ReferencedRTRadiationSequence = pydicom.Sequence()
            self._dataset.ReferencedRTRadiationSequence.clear()
            self._dataset.ReferencedRTRadiationSequence.extend([item.to_dataset() for item in value])

    def add_ReferencedRTRadiation(self, item: ReferencedRTRadiationSequenceItem):
        if not isinstance(item, ReferencedRTRadiationSequenceItem):
            raise ValueError("Item must be an instance of ReferencedRTRadiationSequenceItem")
        self._ReferencedRTRadiationSequence.append(item)
        if "ReferencedRTRadiationSequence" not in self._dataset:
            self._dataset.ReferencedRTRadiationSequence = pydicom.Sequence()
        self._dataset.ReferencedRTRadiationSequence.append(item.to_dataset())
