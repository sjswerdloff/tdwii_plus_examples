from decimal import Decimal
from typing import Any, List, Optional

import pydicom

from .code_sequence_item import CodeSequenceItem


class MeasuredValueSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._MeasurementUnitsCodeSequence: List[CodeSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def MeasurementUnitsCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "MeasurementUnitsCodeSequence" in self._dataset:
            if len(self._MeasurementUnitsCodeSequence) == len(self._dataset.MeasurementUnitsCodeSequence):
                return self._MeasurementUnitsCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.MeasurementUnitsCodeSequence]
        return None

    @MeasurementUnitsCodeSequence.setter
    def MeasurementUnitsCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._MeasurementUnitsCodeSequence = []
            if "MeasurementUnitsCodeSequence" in self._dataset:
                del self._dataset.MeasurementUnitsCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError(f"MeasurementUnitsCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._MeasurementUnitsCodeSequence = value
            if "MeasurementUnitsCodeSequence" not in self._dataset:
                self._dataset.MeasurementUnitsCodeSequence = pydicom.Sequence()
            self._dataset.MeasurementUnitsCodeSequence.clear()
            self._dataset.MeasurementUnitsCodeSequence.extend([item.to_dataset() for item in value])

    def add_MeasurementUnitsCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError(f"Item must be an instance of CodeSequenceItem")
        self._MeasurementUnitsCodeSequence.append(item)
        if "MeasurementUnitsCodeSequence" not in self._dataset:
            self._dataset.MeasurementUnitsCodeSequence = pydicom.Sequence()
        self._dataset.MeasurementUnitsCodeSequence.append(item.to_dataset())

    @property
    def FloatingPointValue(self) -> Optional[List[float]]:
        if "FloatingPointValue" in self._dataset:
            return self._dataset.FloatingPointValue
        return None

    @FloatingPointValue.setter
    def FloatingPointValue(self, value: Optional[List[float]]):
        if value is None:
            if "FloatingPointValue" in self._dataset:
                del self._dataset.FloatingPointValue
        else:
            self._dataset.FloatingPointValue = value

    @property
    def RationalNumeratorValue(self) -> Optional[List[int]]:
        if "RationalNumeratorValue" in self._dataset:
            return self._dataset.RationalNumeratorValue
        return None

    @RationalNumeratorValue.setter
    def RationalNumeratorValue(self, value: Optional[List[int]]):
        if value is None:
            if "RationalNumeratorValue" in self._dataset:
                del self._dataset.RationalNumeratorValue
        else:
            self._dataset.RationalNumeratorValue = value

    @property
    def RationalDenominatorValue(self) -> Optional[List[int]]:
        if "RationalDenominatorValue" in self._dataset:
            return self._dataset.RationalDenominatorValue
        return None

    @RationalDenominatorValue.setter
    def RationalDenominatorValue(self, value: Optional[List[int]]):
        if value is None:
            if "RationalDenominatorValue" in self._dataset:
                del self._dataset.RationalDenominatorValue
        else:
            self._dataset.RationalDenominatorValue = value

    @property
    def NumericValue(self) -> Optional[List[Decimal]]:
        if "NumericValue" in self._dataset:
            return self._dataset.NumericValue
        return None

    @NumericValue.setter
    def NumericValue(self, value: Optional[List[Decimal]]):
        if value is None:
            if "NumericValue" in self._dataset:
                del self._dataset.NumericValue
        else:
            self._dataset.NumericValue = value
