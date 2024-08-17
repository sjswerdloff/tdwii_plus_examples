from typing import Any, List, Optional

import pydicom

from .omitted_channel_sequence_item import OmittedChannelSequenceItem


class OmittedApplicationSetupSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._OmittedChannelSequence: List[OmittedChannelSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def OmittedChannelSequence(self) -> Optional[List[OmittedChannelSequenceItem]]:
        if "OmittedChannelSequence" in self._dataset:
            if len(self._OmittedChannelSequence) == len(self._dataset.OmittedChannelSequence):
                return self._OmittedChannelSequence
            else:
                return [OmittedChannelSequenceItem(x) for x in self._dataset.OmittedChannelSequence]
        return None

    @OmittedChannelSequence.setter
    def OmittedChannelSequence(self, value: Optional[List[OmittedChannelSequenceItem]]):
        if value is None:
            self._OmittedChannelSequence = []
            if "OmittedChannelSequence" in self._dataset:
                del self._dataset.OmittedChannelSequence
        elif not isinstance(value, list) or not all(isinstance(item, OmittedChannelSequenceItem) for item in value):
            raise ValueError(f"OmittedChannelSequence must be a list of OmittedChannelSequenceItem objects")
        else:
            self._OmittedChannelSequence = value
            if "OmittedChannelSequence" not in self._dataset:
                self._dataset.OmittedChannelSequence = pydicom.Sequence()
            self._dataset.OmittedChannelSequence.clear()
            self._dataset.OmittedChannelSequence.extend([item.to_dataset() for item in value])

    def add_OmittedChannel(self, item: OmittedChannelSequenceItem):
        if not isinstance(item, OmittedChannelSequenceItem):
            raise ValueError(f"Item must be an instance of OmittedChannelSequenceItem")
        self._OmittedChannelSequence.append(item)
        if "OmittedChannelSequence" not in self._dataset:
            self._dataset.OmittedChannelSequence = pydicom.Sequence()
        self._dataset.OmittedChannelSequence.append(item.to_dataset())

    @property
    def ReferencedBrachyApplicationSetupNumber(self) -> Optional[int]:
        if "ReferencedBrachyApplicationSetupNumber" in self._dataset:
            return self._dataset.ReferencedBrachyApplicationSetupNumber
        return None

    @ReferencedBrachyApplicationSetupNumber.setter
    def ReferencedBrachyApplicationSetupNumber(self, value: Optional[int]):
        if value is None:
            if "ReferencedBrachyApplicationSetupNumber" in self._dataset:
                del self._dataset.ReferencedBrachyApplicationSetupNumber
        else:
            self._dataset.ReferencedBrachyApplicationSetupNumber = value
