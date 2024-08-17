from typing import Any, List, Optional  # noqa

import pydicom

from .referenced_control_point_sequence_item import ReferencedControlPointSequenceItem


class ReferencedBeamSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._ReferencedControlPointSequence: List[ReferencedControlPointSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ReferencedBeamNumber(self) -> Optional[int]:
        if "ReferencedBeamNumber" in self._dataset:
            return self._dataset.ReferencedBeamNumber
        return None

    @ReferencedBeamNumber.setter
    def ReferencedBeamNumber(self, value: Optional[int]):
        if value is None:
            if "ReferencedBeamNumber" in self._dataset:
                del self._dataset.ReferencedBeamNumber
        else:
            self._dataset.ReferencedBeamNumber = value

    @property
    def ReferencedControlPointSequence(self) -> Optional[List[ReferencedControlPointSequenceItem]]:
        if "ReferencedControlPointSequence" in self._dataset:
            if len(self._ReferencedControlPointSequence) == len(self._dataset.ReferencedControlPointSequence):
                return self._ReferencedControlPointSequence
            else:
                return [ReferencedControlPointSequenceItem(x) for x in self._dataset.ReferencedControlPointSequence]
        return None

    @ReferencedControlPointSequence.setter
    def ReferencedControlPointSequence(self, value: Optional[List[ReferencedControlPointSequenceItem]]):
        if value is None:
            self._ReferencedControlPointSequence = []
            if "ReferencedControlPointSequence" in self._dataset:
                del self._dataset.ReferencedControlPointSequence
        elif not isinstance(value, list) or not all(isinstance(item, ReferencedControlPointSequenceItem) for item in value):
            raise ValueError("ReferencedControlPointSequence must be a list of ReferencedControlPointSequenceItem objects")
        else:
            self._ReferencedControlPointSequence = value
            if "ReferencedControlPointSequence" not in self._dataset:
                self._dataset.ReferencedControlPointSequence = pydicom.Sequence()
            self._dataset.ReferencedControlPointSequence.clear()
            self._dataset.ReferencedControlPointSequence.extend([item.to_dataset() for item in value])

    def add_ReferencedControlPoint(self, item: ReferencedControlPointSequenceItem):
        if not isinstance(item, ReferencedControlPointSequenceItem):
            raise ValueError("Item must be an instance of ReferencedControlPointSequenceItem")
        self._ReferencedControlPointSequence.append(item)
        if "ReferencedControlPointSequence" not in self._dataset:
            self._dataset.ReferencedControlPointSequence = pydicom.Sequence()
        self._dataset.ReferencedControlPointSequence.append(item.to_dataset())
