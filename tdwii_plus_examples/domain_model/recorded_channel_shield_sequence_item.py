from typing import Any, List, Optional  # noqa

import pydicom


class RecordedChannelShieldSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ReferencedChannelShieldNumber(self) -> Optional[int]:
        if "ReferencedChannelShieldNumber" in self._dataset:
            return self._dataset.ReferencedChannelShieldNumber
        return None

    @ReferencedChannelShieldNumber.setter
    def ReferencedChannelShieldNumber(self, value: Optional[int]):
        if value is None:
            if "ReferencedChannelShieldNumber" in self._dataset:
                del self._dataset.ReferencedChannelShieldNumber
        else:
            self._dataset.ReferencedChannelShieldNumber = value

    @property
    def ChannelShieldID(self) -> Optional[str]:
        if "ChannelShieldID" in self._dataset:
            return self._dataset.ChannelShieldID
        return None

    @ChannelShieldID.setter
    def ChannelShieldID(self, value: Optional[str]):
        if value is None:
            if "ChannelShieldID" in self._dataset:
                del self._dataset.ChannelShieldID
        else:
            self._dataset.ChannelShieldID = value

    @property
    def ChannelShieldName(self) -> Optional[str]:
        if "ChannelShieldName" in self._dataset:
            return self._dataset.ChannelShieldName
        return None

    @ChannelShieldName.setter
    def ChannelShieldName(self, value: Optional[str]):
        if value is None:
            if "ChannelShieldName" in self._dataset:
                del self._dataset.ChannelShieldName
        else:
            self._dataset.ChannelShieldName = value
