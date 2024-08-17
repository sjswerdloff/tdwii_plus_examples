from typing import Any, List, Optional

import pydicom

from .frame_display_sequence_item import FrameDisplaySequenceItem
from .referenced_image_sequence_item import ReferencedImageSequenceItem


class MultiFramePresentationSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._ReferencedImageSequence: List[ReferencedImageSequenceItem] = []
        self._FrameDisplaySequence: List[FrameDisplaySequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ReferencedImageSequence(self) -> Optional[List[ReferencedImageSequenceItem]]:
        if "ReferencedImageSequence" in self._dataset:
            if len(self._ReferencedImageSequence) == len(self._dataset.ReferencedImageSequence):
                return self._ReferencedImageSequence
            else:
                return [ReferencedImageSequenceItem(x) for x in self._dataset.ReferencedImageSequence]
        return None

    @ReferencedImageSequence.setter
    def ReferencedImageSequence(self, value: Optional[List[ReferencedImageSequenceItem]]):
        if value is None:
            self._ReferencedImageSequence = []
            if "ReferencedImageSequence" in self._dataset:
                del self._dataset.ReferencedImageSequence
        elif not isinstance(value, list) or not all(isinstance(item, ReferencedImageSequenceItem) for item in value):
            raise ValueError(f"ReferencedImageSequence must be a list of ReferencedImageSequenceItem objects")
        else:
            self._ReferencedImageSequence = value
            if "ReferencedImageSequence" not in self._dataset:
                self._dataset.ReferencedImageSequence = pydicom.Sequence()
            self._dataset.ReferencedImageSequence.clear()
            self._dataset.ReferencedImageSequence.extend([item.to_dataset() for item in value])

    def add_ReferencedImage(self, item: ReferencedImageSequenceItem):
        if not isinstance(item, ReferencedImageSequenceItem):
            raise ValueError(f"Item must be an instance of ReferencedImageSequenceItem")
        self._ReferencedImageSequence.append(item)
        if "ReferencedImageSequence" not in self._dataset:
            self._dataset.ReferencedImageSequence = pydicom.Sequence()
        self._dataset.ReferencedImageSequence.append(item.to_dataset())

    @property
    def FrameDisplaySequence(self) -> Optional[List[FrameDisplaySequenceItem]]:
        if "FrameDisplaySequence" in self._dataset:
            if len(self._FrameDisplaySequence) == len(self._dataset.FrameDisplaySequence):
                return self._FrameDisplaySequence
            else:
                return [FrameDisplaySequenceItem(x) for x in self._dataset.FrameDisplaySequence]
        return None

    @FrameDisplaySequence.setter
    def FrameDisplaySequence(self, value: Optional[List[FrameDisplaySequenceItem]]):
        if value is None:
            self._FrameDisplaySequence = []
            if "FrameDisplaySequence" in self._dataset:
                del self._dataset.FrameDisplaySequence
        elif not isinstance(value, list) or not all(isinstance(item, FrameDisplaySequenceItem) for item in value):
            raise ValueError(f"FrameDisplaySequence must be a list of FrameDisplaySequenceItem objects")
        else:
            self._FrameDisplaySequence = value
            if "FrameDisplaySequence" not in self._dataset:
                self._dataset.FrameDisplaySequence = pydicom.Sequence()
            self._dataset.FrameDisplaySequence.clear()
            self._dataset.FrameDisplaySequence.extend([item.to_dataset() for item in value])

    def add_FrameDisplay(self, item: FrameDisplaySequenceItem):
        if not isinstance(item, FrameDisplaySequenceItem):
            raise ValueError(f"Item must be an instance of FrameDisplaySequenceItem")
        self._FrameDisplaySequence.append(item)
        if "FrameDisplaySequence" not in self._dataset:
            self._dataset.FrameDisplaySequence = pydicom.Sequence()
        self._dataset.FrameDisplaySequence.append(item.to_dataset())

    @property
    def PreferredPlaybackSequencing(self) -> Optional[int]:
        if "PreferredPlaybackSequencing" in self._dataset:
            return self._dataset.PreferredPlaybackSequencing
        return None

    @PreferredPlaybackSequencing.setter
    def PreferredPlaybackSequencing(self, value: Optional[int]):
        if value is None:
            if "PreferredPlaybackSequencing" in self._dataset:
                del self._dataset.PreferredPlaybackSequencing
        else:
            self._dataset.PreferredPlaybackSequencing = value
