from decimal import Decimal
from typing import Any, List, Optional  # noqa

import pydicom


class ChannelDisplaySequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ChannelOffset(self) -> Optional[Decimal]:
        if "ChannelOffset" in self._dataset:
            return self._dataset.ChannelOffset
        return None

    @ChannelOffset.setter
    def ChannelOffset(self, value: Optional[Decimal]):
        if value is None:
            if "ChannelOffset" in self._dataset:
                del self._dataset.ChannelOffset
        else:
            self._dataset.ChannelOffset = value

    @property
    def ChannelRecommendedDisplayCIELabValue(self) -> Optional[List[int]]:
        if "ChannelRecommendedDisplayCIELabValue" in self._dataset:
            return self._dataset.ChannelRecommendedDisplayCIELabValue
        return None

    @ChannelRecommendedDisplayCIELabValue.setter
    def ChannelRecommendedDisplayCIELabValue(self, value: Optional[List[int]]):
        if value is None:
            if "ChannelRecommendedDisplayCIELabValue" in self._dataset:
                del self._dataset.ChannelRecommendedDisplayCIELabValue
        else:
            self._dataset.ChannelRecommendedDisplayCIELabValue = value

    @property
    def ChannelPosition(self) -> Optional[float]:
        if "ChannelPosition" in self._dataset:
            return self._dataset.ChannelPosition
        return None

    @ChannelPosition.setter
    def ChannelPosition(self, value: Optional[float]):
        if value is None:
            if "ChannelPosition" in self._dataset:
                del self._dataset.ChannelPosition
        else:
            self._dataset.ChannelPosition = value

    @property
    def DisplayShadingFlag(self) -> Optional[str]:
        if "DisplayShadingFlag" in self._dataset:
            return self._dataset.DisplayShadingFlag
        return None

    @DisplayShadingFlag.setter
    def DisplayShadingFlag(self, value: Optional[str]):
        if value is None:
            if "DisplayShadingFlag" in self._dataset:
                del self._dataset.DisplayShadingFlag
        else:
            self._dataset.DisplayShadingFlag = value

    @property
    def FractionalChannelDisplayScale(self) -> Optional[float]:
        if "FractionalChannelDisplayScale" in self._dataset:
            return self._dataset.FractionalChannelDisplayScale
        return None

    @FractionalChannelDisplayScale.setter
    def FractionalChannelDisplayScale(self, value: Optional[float]):
        if value is None:
            if "FractionalChannelDisplayScale" in self._dataset:
                del self._dataset.FractionalChannelDisplayScale
        else:
            self._dataset.FractionalChannelDisplayScale = value

    @property
    def AbsoluteChannelDisplayScale(self) -> Optional[float]:
        if "AbsoluteChannelDisplayScale" in self._dataset:
            return self._dataset.AbsoluteChannelDisplayScale
        return None

    @AbsoluteChannelDisplayScale.setter
    def AbsoluteChannelDisplayScale(self, value: Optional[float]):
        if value is None:
            if "AbsoluteChannelDisplayScale" in self._dataset:
                del self._dataset.AbsoluteChannelDisplayScale
        else:
            self._dataset.AbsoluteChannelDisplayScale = value

    @property
    def ReferencedWaveformChannels(self) -> Optional[List[int]]:
        if "ReferencedWaveformChannels" in self._dataset:
            return self._dataset.ReferencedWaveformChannels
        return None

    @ReferencedWaveformChannels.setter
    def ReferencedWaveformChannels(self, value: Optional[List[int]]):
        if value is None:
            if "ReferencedWaveformChannels" in self._dataset:
                del self._dataset.ReferencedWaveformChannels
        else:
            self._dataset.ReferencedWaveformChannels = value
