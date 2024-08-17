from typing import Any, List, Optional

import pydicom

from .referenced_rt_prescription_sequence_item import (
    ReferencedRTPrescriptionSequenceItem,
)


class ReferencedRTPhysicianIntentSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._ReferencedRTPrescriptionSequence: List[ReferencedRTPrescriptionSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ReferencedSOPClassUID(self) -> Optional[str]:
        if "ReferencedSOPClassUID" in self._dataset:
            return self._dataset.ReferencedSOPClassUID
        return None

    @ReferencedSOPClassUID.setter
    def ReferencedSOPClassUID(self, value: Optional[str]):
        if value is None:
            if "ReferencedSOPClassUID" in self._dataset:
                del self._dataset.ReferencedSOPClassUID
        else:
            self._dataset.ReferencedSOPClassUID = value

    @property
    def ReferencedSOPInstanceUID(self) -> Optional[str]:
        if "ReferencedSOPInstanceUID" in self._dataset:
            return self._dataset.ReferencedSOPInstanceUID
        return None

    @ReferencedSOPInstanceUID.setter
    def ReferencedSOPInstanceUID(self, value: Optional[str]):
        if value is None:
            if "ReferencedSOPInstanceUID" in self._dataset:
                del self._dataset.ReferencedSOPInstanceUID
        else:
            self._dataset.ReferencedSOPInstanceUID = value

    @property
    def ReferencedRTPrescriptionSequence(self) -> Optional[List[ReferencedRTPrescriptionSequenceItem]]:
        if "ReferencedRTPrescriptionSequence" in self._dataset:
            if len(self._ReferencedRTPrescriptionSequence) == len(self._dataset.ReferencedRTPrescriptionSequence):
                return self._ReferencedRTPrescriptionSequence
            else:
                return [ReferencedRTPrescriptionSequenceItem(x) for x in self._dataset.ReferencedRTPrescriptionSequence]
        return None

    @ReferencedRTPrescriptionSequence.setter
    def ReferencedRTPrescriptionSequence(self, value: Optional[List[ReferencedRTPrescriptionSequenceItem]]):
        if value is None:
            self._ReferencedRTPrescriptionSequence = []
            if "ReferencedRTPrescriptionSequence" in self._dataset:
                del self._dataset.ReferencedRTPrescriptionSequence
        elif not isinstance(value, list) or not all(isinstance(item, ReferencedRTPrescriptionSequenceItem) for item in value):
            raise ValueError(
                f"ReferencedRTPrescriptionSequence must be a list of ReferencedRTPrescriptionSequenceItem objects"
            )
        else:
            self._ReferencedRTPrescriptionSequence = value
            if "ReferencedRTPrescriptionSequence" not in self._dataset:
                self._dataset.ReferencedRTPrescriptionSequence = pydicom.Sequence()
            self._dataset.ReferencedRTPrescriptionSequence.clear()
            self._dataset.ReferencedRTPrescriptionSequence.extend([item.to_dataset() for item in value])

    def add_ReferencedRTPrescription(self, item: ReferencedRTPrescriptionSequenceItem):
        if not isinstance(item, ReferencedRTPrescriptionSequenceItem):
            raise ValueError(f"Item must be an instance of ReferencedRTPrescriptionSequenceItem")
        self._ReferencedRTPrescriptionSequence.append(item)
        if "ReferencedRTPrescriptionSequence" not in self._dataset:
            self._dataset.ReferencedRTPrescriptionSequence = pydicom.Sequence()
        self._dataset.ReferencedRTPrescriptionSequence.append(item.to_dataset())
