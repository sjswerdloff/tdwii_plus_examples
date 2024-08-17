from typing import Any, List, Optional

import pydicom

from .camera_position_group_sequence_item import CameraPositionGroupSequenceItem
from .frame_content_sequence_item import FrameContentSequenceItem
from .frame_usefulness_group_sequence_item import FrameUsefulnessGroupSequenceItem
from .time_of_frame_group_sequence_item import TimeOfFrameGroupSequenceItem


class CurrentFrameFunctionalGroupsSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._FrameContentSequence: List[FrameContentSequenceItem] = []
        self._FrameUsefulnessGroupSequence: List[FrameUsefulnessGroupSequenceItem] = []
        self._CameraPositionGroupSequence: List[CameraPositionGroupSequenceItem] = []
        self._TimeOfFrameGroupSequence: List[TimeOfFrameGroupSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def FrameContentSequence(self) -> Optional[List[FrameContentSequenceItem]]:
        if "FrameContentSequence" in self._dataset:
            if len(self._FrameContentSequence) == len(self._dataset.FrameContentSequence):
                return self._FrameContentSequence
            else:
                return [FrameContentSequenceItem(x) for x in self._dataset.FrameContentSequence]
        return None

    @FrameContentSequence.setter
    def FrameContentSequence(self, value: Optional[List[FrameContentSequenceItem]]):
        if value is None:
            self._FrameContentSequence = []
            if "FrameContentSequence" in self._dataset:
                del self._dataset.FrameContentSequence
        elif not isinstance(value, list) or not all(isinstance(item, FrameContentSequenceItem) for item in value):
            raise ValueError(f"FrameContentSequence must be a list of FrameContentSequenceItem objects")
        else:
            self._FrameContentSequence = value
            if "FrameContentSequence" not in self._dataset:
                self._dataset.FrameContentSequence = pydicom.Sequence()
            self._dataset.FrameContentSequence.clear()
            self._dataset.FrameContentSequence.extend([item.to_dataset() for item in value])

    def add_FrameContent(self, item: FrameContentSequenceItem):
        if not isinstance(item, FrameContentSequenceItem):
            raise ValueError(f"Item must be an instance of FrameContentSequenceItem")
        self._FrameContentSequence.append(item)
        if "FrameContentSequence" not in self._dataset:
            self._dataset.FrameContentSequence = pydicom.Sequence()
        self._dataset.FrameContentSequence.append(item.to_dataset())

    @property
    def FrameUsefulnessGroupSequence(self) -> Optional[List[FrameUsefulnessGroupSequenceItem]]:
        if "FrameUsefulnessGroupSequence" in self._dataset:
            if len(self._FrameUsefulnessGroupSequence) == len(self._dataset.FrameUsefulnessGroupSequence):
                return self._FrameUsefulnessGroupSequence
            else:
                return [FrameUsefulnessGroupSequenceItem(x) for x in self._dataset.FrameUsefulnessGroupSequence]
        return None

    @FrameUsefulnessGroupSequence.setter
    def FrameUsefulnessGroupSequence(self, value: Optional[List[FrameUsefulnessGroupSequenceItem]]):
        if value is None:
            self._FrameUsefulnessGroupSequence = []
            if "FrameUsefulnessGroupSequence" in self._dataset:
                del self._dataset.FrameUsefulnessGroupSequence
        elif not isinstance(value, list) or not all(isinstance(item, FrameUsefulnessGroupSequenceItem) for item in value):
            raise ValueError(f"FrameUsefulnessGroupSequence must be a list of FrameUsefulnessGroupSequenceItem objects")
        else:
            self._FrameUsefulnessGroupSequence = value
            if "FrameUsefulnessGroupSequence" not in self._dataset:
                self._dataset.FrameUsefulnessGroupSequence = pydicom.Sequence()
            self._dataset.FrameUsefulnessGroupSequence.clear()
            self._dataset.FrameUsefulnessGroupSequence.extend([item.to_dataset() for item in value])

    def add_FrameUsefulnessGroup(self, item: FrameUsefulnessGroupSequenceItem):
        if not isinstance(item, FrameUsefulnessGroupSequenceItem):
            raise ValueError(f"Item must be an instance of FrameUsefulnessGroupSequenceItem")
        self._FrameUsefulnessGroupSequence.append(item)
        if "FrameUsefulnessGroupSequence" not in self._dataset:
            self._dataset.FrameUsefulnessGroupSequence = pydicom.Sequence()
        self._dataset.FrameUsefulnessGroupSequence.append(item.to_dataset())

    @property
    def CameraPositionGroupSequence(self) -> Optional[List[CameraPositionGroupSequenceItem]]:
        if "CameraPositionGroupSequence" in self._dataset:
            if len(self._CameraPositionGroupSequence) == len(self._dataset.CameraPositionGroupSequence):
                return self._CameraPositionGroupSequence
            else:
                return [CameraPositionGroupSequenceItem(x) for x in self._dataset.CameraPositionGroupSequence]
        return None

    @CameraPositionGroupSequence.setter
    def CameraPositionGroupSequence(self, value: Optional[List[CameraPositionGroupSequenceItem]]):
        if value is None:
            self._CameraPositionGroupSequence = []
            if "CameraPositionGroupSequence" in self._dataset:
                del self._dataset.CameraPositionGroupSequence
        elif not isinstance(value, list) or not all(isinstance(item, CameraPositionGroupSequenceItem) for item in value):
            raise ValueError(f"CameraPositionGroupSequence must be a list of CameraPositionGroupSequenceItem objects")
        else:
            self._CameraPositionGroupSequence = value
            if "CameraPositionGroupSequence" not in self._dataset:
                self._dataset.CameraPositionGroupSequence = pydicom.Sequence()
            self._dataset.CameraPositionGroupSequence.clear()
            self._dataset.CameraPositionGroupSequence.extend([item.to_dataset() for item in value])

    def add_CameraPositionGroup(self, item: CameraPositionGroupSequenceItem):
        if not isinstance(item, CameraPositionGroupSequenceItem):
            raise ValueError(f"Item must be an instance of CameraPositionGroupSequenceItem")
        self._CameraPositionGroupSequence.append(item)
        if "CameraPositionGroupSequence" not in self._dataset:
            self._dataset.CameraPositionGroupSequence = pydicom.Sequence()
        self._dataset.CameraPositionGroupSequence.append(item.to_dataset())

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
