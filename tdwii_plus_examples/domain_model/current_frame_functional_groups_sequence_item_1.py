from typing import Any, List, Optional

import pydicom

from .time_of_frame_group_sequence_item import TimeOfFrameGroupSequenceItem


class CurrentFrameFunctionalGroupsSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._TimeOfFrameGroupSequence: List[TimeOfFrameGroupSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def TimeOfFrameGroupSequence(self) -> Optional[List[TimeOfFrameGroupSequenceItem]]:
        if "TimeOfFrameGroupSequence" in self._dataset:
            if len(self._TimeOfFrameGroupSequence) == len(self._dataset.TimeOfFrameGroupSequence):
                return self._TimeOfFrameGroupSequence
            else:
                return [TimeOfFrameGroupSequenceItem(x) for x in self._dataset.TimeOfFrameGroupSequence]
        return None

    @TimeOfFrameGroupSequence.setter
    def TimeOfFrameGroupSequence(self, value: Optional[List[TimeOfFrameGroupSequenceItem]]):
        if value is None:
            self._TimeOfFrameGroupSequence = []
            if "TimeOfFrameGroupSequence" in self._dataset:
                del self._dataset.TimeOfFrameGroupSequence
        elif not isinstance(value, list) or not all(isinstance(item, TimeOfFrameGroupSequenceItem) for item in value):
            raise ValueError(f"TimeOfFrameGroupSequence must be a list of TimeOfFrameGroupSequenceItem objects")
        else:
            self._TimeOfFrameGroupSequence = value
            if "TimeOfFrameGroupSequence" not in self._dataset:
                self._dataset.TimeOfFrameGroupSequence = pydicom.Sequence()
            self._dataset.TimeOfFrameGroupSequence.clear()
            self._dataset.TimeOfFrameGroupSequence.extend([item.to_dataset() for item in value])

    def add_TimeOfFrameGroup(self, item: TimeOfFrameGroupSequenceItem):
        if not isinstance(item, TimeOfFrameGroupSequenceItem):
            raise ValueError(f"Item must be an instance of TimeOfFrameGroupSequenceItem")
        self._TimeOfFrameGroupSequence.append(item)
        if "TimeOfFrameGroupSequence" not in self._dataset:
            self._dataset.TimeOfFrameGroupSequence = pydicom.Sequence()
        self._dataset.TimeOfFrameGroupSequence.append(item.to_dataset())
