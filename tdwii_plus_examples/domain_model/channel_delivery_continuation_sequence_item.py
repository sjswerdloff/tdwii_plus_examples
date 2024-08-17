from decimal import Decimal
from typing import Any, List, Optional

import pydicom


class ChannelDeliveryContinuationSequenceItem:
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
    def StartCumulativeTimeWeight(self) -> Optional[Decimal]:
        if "StartCumulativeTimeWeight" in self._dataset:
            return self._dataset.StartCumulativeTimeWeight
        return None

    @StartCumulativeTimeWeight.setter
    def StartCumulativeTimeWeight(self, value: Optional[Decimal]):
        if value is None:
            if "StartCumulativeTimeWeight" in self._dataset:
                del self._dataset.StartCumulativeTimeWeight
        else:
            self._dataset.StartCumulativeTimeWeight = value

    @property
    def EndCumulativeTimeWeight(self) -> Optional[Decimal]:
        if "EndCumulativeTimeWeight" in self._dataset:
            return self._dataset.EndCumulativeTimeWeight
        return None

    @EndCumulativeTimeWeight.setter
    def EndCumulativeTimeWeight(self, value: Optional[Decimal]):
        if value is None:
            if "EndCumulativeTimeWeight" in self._dataset:
                del self._dataset.EndCumulativeTimeWeight
        else:
            self._dataset.EndCumulativeTimeWeight = value
