from typing import Any, List, Optional

import pydicom

from .referenced_rt_plan_sequence_item import ReferencedRTPlanSequenceItem
from .referenced_rt_radiation_sequence_item import ReferencedRTRadiationSequenceItem
from .referenced_rt_radiation_set_sequence_item import (
    ReferencedRTRadiationSetSequenceItem,
)


class RTPatientPositionScopeSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._ReferencedRTRadiationSequence: List[ReferencedRTRadiationSequenceItem] = []
        self._ReferencedRTRadiationSetSequence: List[ReferencedRTRadiationSetSequenceItem] = []
        self._ReferencedRTPlanSequence: List[ReferencedRTPlanSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

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
            raise ValueError(f"ReferencedRTRadiationSequence must be a list of ReferencedRTRadiationSequenceItem objects")
        else:
            self._ReferencedRTRadiationSequence = value
            if "ReferencedRTRadiationSequence" not in self._dataset:
                self._dataset.ReferencedRTRadiationSequence = pydicom.Sequence()
            self._dataset.ReferencedRTRadiationSequence.clear()
            self._dataset.ReferencedRTRadiationSequence.extend([item.to_dataset() for item in value])

    def add_ReferencedRTRadiation(self, item: ReferencedRTRadiationSequenceItem):
        if not isinstance(item, ReferencedRTRadiationSequenceItem):
            raise ValueError(f"Item must be an instance of ReferencedRTRadiationSequenceItem")
        self._ReferencedRTRadiationSequence.append(item)
        if "ReferencedRTRadiationSequence" not in self._dataset:
            self._dataset.ReferencedRTRadiationSequence = pydicom.Sequence()
        self._dataset.ReferencedRTRadiationSequence.append(item.to_dataset())

    @property
    def ReferencedRTRadiationSetSequence(self) -> Optional[List[ReferencedRTRadiationSetSequenceItem]]:
        if "ReferencedRTRadiationSetSequence" in self._dataset:
            if len(self._ReferencedRTRadiationSetSequence) == len(self._dataset.ReferencedRTRadiationSetSequence):
                return self._ReferencedRTRadiationSetSequence
            else:
                return [ReferencedRTRadiationSetSequenceItem(x) for x in self._dataset.ReferencedRTRadiationSetSequence]
        return None

    @ReferencedRTRadiationSetSequence.setter
    def ReferencedRTRadiationSetSequence(self, value: Optional[List[ReferencedRTRadiationSetSequenceItem]]):
        if value is None:
            self._ReferencedRTRadiationSetSequence = []
            if "ReferencedRTRadiationSetSequence" in self._dataset:
                del self._dataset.ReferencedRTRadiationSetSequence
        elif not isinstance(value, list) or not all(isinstance(item, ReferencedRTRadiationSetSequenceItem) for item in value):
            raise ValueError(
                f"ReferencedRTRadiationSetSequence must be a list of ReferencedRTRadiationSetSequenceItem objects"
            )
        else:
            self._ReferencedRTRadiationSetSequence = value
            if "ReferencedRTRadiationSetSequence" not in self._dataset:
                self._dataset.ReferencedRTRadiationSetSequence = pydicom.Sequence()
            self._dataset.ReferencedRTRadiationSetSequence.clear()
            self._dataset.ReferencedRTRadiationSetSequence.extend([item.to_dataset() for item in value])

    def add_ReferencedRTRadiationSet(self, item: ReferencedRTRadiationSetSequenceItem):
        if not isinstance(item, ReferencedRTRadiationSetSequenceItem):
            raise ValueError(f"Item must be an instance of ReferencedRTRadiationSetSequenceItem")
        self._ReferencedRTRadiationSetSequence.append(item)
        if "ReferencedRTRadiationSetSequence" not in self._dataset:
            self._dataset.ReferencedRTRadiationSetSequence = pydicom.Sequence()
        self._dataset.ReferencedRTRadiationSetSequence.append(item.to_dataset())

    @property
    def ReferencedRTPlanSequence(self) -> Optional[List[ReferencedRTPlanSequenceItem]]:
        if "ReferencedRTPlanSequence" in self._dataset:
            if len(self._ReferencedRTPlanSequence) == len(self._dataset.ReferencedRTPlanSequence):
                return self._ReferencedRTPlanSequence
            else:
                return [ReferencedRTPlanSequenceItem(x) for x in self._dataset.ReferencedRTPlanSequence]
        return None

    @ReferencedRTPlanSequence.setter
    def ReferencedRTPlanSequence(self, value: Optional[List[ReferencedRTPlanSequenceItem]]):
        if value is None:
            self._ReferencedRTPlanSequence = []
            if "ReferencedRTPlanSequence" in self._dataset:
                del self._dataset.ReferencedRTPlanSequence
        elif not isinstance(value, list) or not all(isinstance(item, ReferencedRTPlanSequenceItem) for item in value):
            raise ValueError(f"ReferencedRTPlanSequence must be a list of ReferencedRTPlanSequenceItem objects")
        else:
            self._ReferencedRTPlanSequence = value
            if "ReferencedRTPlanSequence" not in self._dataset:
                self._dataset.ReferencedRTPlanSequence = pydicom.Sequence()
            self._dataset.ReferencedRTPlanSequence.clear()
            self._dataset.ReferencedRTPlanSequence.extend([item.to_dataset() for item in value])

    def add_ReferencedRTPlan(self, item: ReferencedRTPlanSequenceItem):
        if not isinstance(item, ReferencedRTPlanSequenceItem):
            raise ValueError(f"Item must be an instance of ReferencedRTPlanSequenceItem")
        self._ReferencedRTPlanSequence.append(item)
        if "ReferencedRTPlanSequence" not in self._dataset:
            self._dataset.ReferencedRTPlanSequence = pydicom.Sequence()
        self._dataset.ReferencedRTPlanSequence.append(item.to_dataset())
