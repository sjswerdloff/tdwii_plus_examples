from decimal import Decimal
from typing import Any, List, Optional

import pydicom


class TimeSlotInformationSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def TimeSlotTime(self) -> Optional[Decimal]:
        if "TimeSlotTime" in self._dataset:
            return self._dataset.TimeSlotTime
        return None

    @TimeSlotTime.setter
    def TimeSlotTime(self, value: Optional[Decimal]):
        if value is None:
            if "TimeSlotTime" in self._dataset:
                del self._dataset.TimeSlotTime
        else:
            self._dataset.TimeSlotTime = value
