from typing import Any, List, Optional  # noqa

import pydicom

from .weekday_fraction_pattern_sequence_item import WeekdayFractionPatternSequenceItem


class FractionPatternSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._WeekdayFractionPatternSequence: List[WeekdayFractionPatternSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def NumberOfFractionPatternDigitsPerDay(self) -> Optional[int]:
        if "NumberOfFractionPatternDigitsPerDay" in self._dataset:
            return self._dataset.NumberOfFractionPatternDigitsPerDay
        return None

    @NumberOfFractionPatternDigitsPerDay.setter
    def NumberOfFractionPatternDigitsPerDay(self, value: Optional[int]):
        if value is None:
            if "NumberOfFractionPatternDigitsPerDay" in self._dataset:
                del self._dataset.NumberOfFractionPatternDigitsPerDay
        else:
            self._dataset.NumberOfFractionPatternDigitsPerDay = value

    @property
    def RepeatFractionCycleLength(self) -> Optional[int]:
        if "RepeatFractionCycleLength" in self._dataset:
            return self._dataset.RepeatFractionCycleLength
        return None

    @RepeatFractionCycleLength.setter
    def RepeatFractionCycleLength(self, value: Optional[int]):
        if value is None:
            if "RepeatFractionCycleLength" in self._dataset:
                del self._dataset.RepeatFractionCycleLength
        else:
            self._dataset.RepeatFractionCycleLength = value

    @property
    def MinimumHoursBetweenFractions(self) -> Optional[float]:
        if "MinimumHoursBetweenFractions" in self._dataset:
            return self._dataset.MinimumHoursBetweenFractions
        return None

    @MinimumHoursBetweenFractions.setter
    def MinimumHoursBetweenFractions(self, value: Optional[float]):
        if value is None:
            if "MinimumHoursBetweenFractions" in self._dataset:
                del self._dataset.MinimumHoursBetweenFractions
        else:
            self._dataset.MinimumHoursBetweenFractions = value

    @property
    def IntendedFractionStartTime(self) -> Optional[List[str]]:
        if "IntendedFractionStartTime" in self._dataset:
            return self._dataset.IntendedFractionStartTime
        return None

    @IntendedFractionStartTime.setter
    def IntendedFractionStartTime(self, value: Optional[List[str]]):
        if value is None:
            if "IntendedFractionStartTime" in self._dataset:
                del self._dataset.IntendedFractionStartTime
        else:
            self._dataset.IntendedFractionStartTime = value

    @property
    def WeekdayFractionPatternSequence(self) -> Optional[List[WeekdayFractionPatternSequenceItem]]:
        if "WeekdayFractionPatternSequence" in self._dataset:
            if len(self._WeekdayFractionPatternSequence) == len(self._dataset.WeekdayFractionPatternSequence):
                return self._WeekdayFractionPatternSequence
            else:
                return [WeekdayFractionPatternSequenceItem(x) for x in self._dataset.WeekdayFractionPatternSequence]
        return None

    @WeekdayFractionPatternSequence.setter
    def WeekdayFractionPatternSequence(self, value: Optional[List[WeekdayFractionPatternSequenceItem]]):
        if value is None:
            self._WeekdayFractionPatternSequence = []
            if "WeekdayFractionPatternSequence" in self._dataset:
                del self._dataset.WeekdayFractionPatternSequence
        elif not isinstance(value, list) or not all(isinstance(item, WeekdayFractionPatternSequenceItem) for item in value):
            raise ValueError("WeekdayFractionPatternSequence must be a list of WeekdayFractionPatternSequenceItem objects")
        else:
            self._WeekdayFractionPatternSequence = value
            if "WeekdayFractionPatternSequence" not in self._dataset:
                self._dataset.WeekdayFractionPatternSequence = pydicom.Sequence()
            self._dataset.WeekdayFractionPatternSequence.clear()
            self._dataset.WeekdayFractionPatternSequence.extend([item.to_dataset() for item in value])

    def add_WeekdayFractionPattern(self, item: WeekdayFractionPatternSequenceItem):
        if not isinstance(item, WeekdayFractionPatternSequenceItem):
            raise ValueError("Item must be an instance of WeekdayFractionPatternSequenceItem")
        self._WeekdayFractionPatternSequence.append(item)
        if "WeekdayFractionPatternSequence" not in self._dataset:
            self._dataset.WeekdayFractionPatternSequence = pydicom.Sequence()
        self._dataset.WeekdayFractionPatternSequence.append(item.to_dataset())
