from typing import Any, List, Optional

import pydicom


class WeekdayFractionPatternSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def FractionPattern(self) -> Optional[str]:
        if "FractionPattern" in self._dataset:
            return self._dataset.FractionPattern
        return None

    @FractionPattern.setter
    def FractionPattern(self, value: Optional[str]):
        if value is None:
            if "FractionPattern" in self._dataset:
                del self._dataset.FractionPattern
        else:
            self._dataset.FractionPattern = value

    @property
    def IntendedStartDayOfWeek(self) -> Optional[str]:
        if "IntendedStartDayOfWeek" in self._dataset:
            return self._dataset.IntendedStartDayOfWeek
        return None

    @IntendedStartDayOfWeek.setter
    def IntendedStartDayOfWeek(self, value: Optional[str]):
        if value is None:
            if "IntendedStartDayOfWeek" in self._dataset:
                del self._dataset.IntendedStartDayOfWeek
        else:
            self._dataset.IntendedStartDayOfWeek = value
