from decimal import Decimal
from typing import Any, List, Optional

import pydicom


class AnalogFilterCharacteristicsSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def AnalogFilterRollOff(self) -> Optional[Decimal]:
        if "AnalogFilterRollOff" in self._dataset:
            return self._dataset.AnalogFilterRollOff
        return None

    @AnalogFilterRollOff.setter
    def AnalogFilterRollOff(self, value: Optional[Decimal]):
        if value is None:
            if "AnalogFilterRollOff" in self._dataset:
                del self._dataset.AnalogFilterRollOff
        else:
            self._dataset.AnalogFilterRollOff = value

    @property
    def AnalogFilterType(self) -> Optional[list]:
        if "AnalogFilterType" in self._dataset:
            return self._dataset.AnalogFilterType
        return None

    @AnalogFilterType.setter
    def AnalogFilterType(self, value: Optional[list]):
        if value is None:
            if "AnalogFilterType" in self._dataset:
                del self._dataset.AnalogFilterType
        else:
            self._dataset.AnalogFilterType = value
