from decimal import Decimal
from typing import Any, List, Optional

import pydicom

from .time_slot_information_sequence_item import TimeSlotInformationSequenceItem


class DataInformationSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._TimeSlotInformationSequence: List[TimeSlotInformationSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def NominalInterval(self) -> Optional[int]:
        if "NominalInterval" in self._dataset:
            return self._dataset.NominalInterval
        return None

    @NominalInterval.setter
    def NominalInterval(self, value: Optional[int]):
        if value is None:
            if "NominalInterval" in self._dataset:
                del self._dataset.NominalInterval
        else:
            self._dataset.NominalInterval = value

    @property
    def FrameTime(self) -> Optional[Decimal]:
        if "FrameTime" in self._dataset:
            return self._dataset.FrameTime
        return None

    @FrameTime.setter
    def FrameTime(self, value: Optional[Decimal]):
        if value is None:
            if "FrameTime" in self._dataset:
                del self._dataset.FrameTime
        else:
            self._dataset.FrameTime = value

    @property
    def LowRRValue(self) -> Optional[int]:
        if "LowRRValue" in self._dataset:
            return self._dataset.LowRRValue
        return None

    @LowRRValue.setter
    def LowRRValue(self, value: Optional[int]):
        if value is None:
            if "LowRRValue" in self._dataset:
                del self._dataset.LowRRValue
        else:
            self._dataset.LowRRValue = value

    @property
    def HighRRValue(self) -> Optional[int]:
        if "HighRRValue" in self._dataset:
            return self._dataset.HighRRValue
        return None

    @HighRRValue.setter
    def HighRRValue(self, value: Optional[int]):
        if value is None:
            if "HighRRValue" in self._dataset:
                del self._dataset.HighRRValue
        else:
            self._dataset.HighRRValue = value

    @property
    def IntervalsAcquired(self) -> Optional[int]:
        if "IntervalsAcquired" in self._dataset:
            return self._dataset.IntervalsAcquired
        return None

    @IntervalsAcquired.setter
    def IntervalsAcquired(self, value: Optional[int]):
        if value is None:
            if "IntervalsAcquired" in self._dataset:
                del self._dataset.IntervalsAcquired
        else:
            self._dataset.IntervalsAcquired = value

    @property
    def IntervalsRejected(self) -> Optional[int]:
        if "IntervalsRejected" in self._dataset:
            return self._dataset.IntervalsRejected
        return None

    @IntervalsRejected.setter
    def IntervalsRejected(self, value: Optional[int]):
        if value is None:
            if "IntervalsRejected" in self._dataset:
                del self._dataset.IntervalsRejected
        else:
            self._dataset.IntervalsRejected = value

    @property
    def TimeSlotInformationSequence(self) -> Optional[List[TimeSlotInformationSequenceItem]]:
        if "TimeSlotInformationSequence" in self._dataset:
            if len(self._TimeSlotInformationSequence) == len(self._dataset.TimeSlotInformationSequence):
                return self._TimeSlotInformationSequence
            else:
                return [TimeSlotInformationSequenceItem(x) for x in self._dataset.TimeSlotInformationSequence]
        return None

    @TimeSlotInformationSequence.setter
    def TimeSlotInformationSequence(self, value: Optional[List[TimeSlotInformationSequenceItem]]):
        if value is None:
            self._TimeSlotInformationSequence = []
            if "TimeSlotInformationSequence" in self._dataset:
                del self._dataset.TimeSlotInformationSequence
        elif not isinstance(value, list) or not all(isinstance(item, TimeSlotInformationSequenceItem) for item in value):
            raise ValueError(f"TimeSlotInformationSequence must be a list of TimeSlotInformationSequenceItem objects")
        else:
            self._TimeSlotInformationSequence = value
            if "TimeSlotInformationSequence" not in self._dataset:
                self._dataset.TimeSlotInformationSequence = pydicom.Sequence()
            self._dataset.TimeSlotInformationSequence.clear()
            self._dataset.TimeSlotInformationSequence.extend([item.to_dataset() for item in value])

    def add_TimeSlotInformation(self, item: TimeSlotInformationSequenceItem):
        if not isinstance(item, TimeSlotInformationSequenceItem):
            raise ValueError(f"Item must be an instance of TimeSlotInformationSequenceItem")
        self._TimeSlotInformationSequence.append(item)
        if "TimeSlotInformationSequence" not in self._dataset:
            self._dataset.TimeSlotInformationSequence = pydicom.Sequence()
        self._dataset.TimeSlotInformationSequence.append(item.to_dataset())
