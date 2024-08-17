from typing import Any, List, Optional  # noqa

import pydicom


class ChannelDeliveryOrderSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ReferencedChannelNumber(self) -> Optional[int]:
        if "ReferencedChannelNumber" in self._dataset:
            return self._dataset.ReferencedChannelNumber
        return None

    @ReferencedChannelNumber.setter
    def ReferencedChannelNumber(self, value: Optional[int]):
        if value is None:
            if "ReferencedChannelNumber" in self._dataset:
                del self._dataset.ReferencedChannelNumber
        else:
            self._dataset.ReferencedChannelNumber = value

    @property
    def ChannelDeliveryOrderIndex(self) -> Optional[int]:
        if "ChannelDeliveryOrderIndex" in self._dataset:
            return self._dataset.ChannelDeliveryOrderIndex
        return None

    @ChannelDeliveryOrderIndex.setter
    def ChannelDeliveryOrderIndex(self, value: Optional[int]):
        if value is None:
            if "ChannelDeliveryOrderIndex" in self._dataset:
                del self._dataset.ChannelDeliveryOrderIndex
        else:
            self._dataset.ChannelDeliveryOrderIndex = value
