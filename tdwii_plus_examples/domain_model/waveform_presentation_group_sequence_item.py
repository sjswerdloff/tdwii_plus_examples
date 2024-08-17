from typing import Any, List, Optional  # noqa

import pydicom

from .channel_display_sequence_item import ChannelDisplaySequenceItem


class WaveformPresentationGroupSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._ChannelDisplaySequence: List[ChannelDisplaySequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def PresentationGroupNumber(self) -> Optional[int]:
        if "PresentationGroupNumber" in self._dataset:
            return self._dataset.PresentationGroupNumber
        return None

    @PresentationGroupNumber.setter
    def PresentationGroupNumber(self, value: Optional[int]):
        if value is None:
            if "PresentationGroupNumber" in self._dataset:
                del self._dataset.PresentationGroupNumber
        else:
            self._dataset.PresentationGroupNumber = value

    @property
    def ChannelDisplaySequence(self) -> Optional[List[ChannelDisplaySequenceItem]]:
        if "ChannelDisplaySequence" in self._dataset:
            if len(self._ChannelDisplaySequence) == len(self._dataset.ChannelDisplaySequence):
                return self._ChannelDisplaySequence
            else:
                return [ChannelDisplaySequenceItem(x) for x in self._dataset.ChannelDisplaySequence]
        return None

    @ChannelDisplaySequence.setter
    def ChannelDisplaySequence(self, value: Optional[List[ChannelDisplaySequenceItem]]):
        if value is None:
            self._ChannelDisplaySequence = []
            if "ChannelDisplaySequence" in self._dataset:
                del self._dataset.ChannelDisplaySequence
        elif not isinstance(value, list) or not all(isinstance(item, ChannelDisplaySequenceItem) for item in value):
            raise ValueError("ChannelDisplaySequence must be a list of ChannelDisplaySequenceItem objects")
        else:
            self._ChannelDisplaySequence = value
            if "ChannelDisplaySequence" not in self._dataset:
                self._dataset.ChannelDisplaySequence = pydicom.Sequence()
            self._dataset.ChannelDisplaySequence.clear()
            self._dataset.ChannelDisplaySequence.extend([item.to_dataset() for item in value])

    def add_ChannelDisplay(self, item: ChannelDisplaySequenceItem):
        if not isinstance(item, ChannelDisplaySequenceItem):
            raise ValueError("Item must be an instance of ChannelDisplaySequenceItem")
        self._ChannelDisplaySequence.append(item)
        if "ChannelDisplaySequence" not in self._dataset:
            self._dataset.ChannelDisplaySequence = pydicom.Sequence()
        self._dataset.ChannelDisplaySequence.append(item.to_dataset())
