from typing import Any, List, Optional

import pydicom

from .referenced_beam_sequence_item import ReferencedBeamSequenceItem


class ReferencedTreatmentRecordSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._ReferencedBeamSequence: List[ReferencedBeamSequenceItem] = []

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
    def ReferencedBeamSequence(self) -> Optional[List[ReferencedBeamSequenceItem]]:
        if "ReferencedBeamSequence" in self._dataset:
            if len(self._ReferencedBeamSequence) == len(self._dataset.ReferencedBeamSequence):
                return self._ReferencedBeamSequence
            else:
                return [ReferencedBeamSequenceItem(x) for x in self._dataset.ReferencedBeamSequence]
        return None

    @ReferencedBeamSequence.setter
    def ReferencedBeamSequence(self, value: Optional[List[ReferencedBeamSequenceItem]]):
        if value is None:
            self._ReferencedBeamSequence = []
            if "ReferencedBeamSequence" in self._dataset:
                del self._dataset.ReferencedBeamSequence
        elif not isinstance(value, list) or not all(isinstance(item, ReferencedBeamSequenceItem) for item in value):
            raise ValueError(f"ReferencedBeamSequence must be a list of ReferencedBeamSequenceItem objects")
        else:
            self._ReferencedBeamSequence = value
            if "ReferencedBeamSequence" not in self._dataset:
                self._dataset.ReferencedBeamSequence = pydicom.Sequence()
            self._dataset.ReferencedBeamSequence.clear()
            self._dataset.ReferencedBeamSequence.extend([item.to_dataset() for item in value])

    def add_ReferencedBeam(self, item: ReferencedBeamSequenceItem):
        if not isinstance(item, ReferencedBeamSequenceItem):
            raise ValueError(f"Item must be an instance of ReferencedBeamSequenceItem")
        self._ReferencedBeamSequence.append(item)
        if "ReferencedBeamSequence" not in self._dataset:
            self._dataset.ReferencedBeamSequence = pydicom.Sequence()
        self._dataset.ReferencedBeamSequence.append(item.to_dataset())
