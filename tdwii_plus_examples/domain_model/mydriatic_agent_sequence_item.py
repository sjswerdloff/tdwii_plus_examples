from decimal import Decimal
from typing import Any, List, Optional

import pydicom

from .code_sequence_item import CodeSequenceItem
from .mydriatic_agent_concentration_units_sequence_item import (
    MydriaticAgentConcentrationUnitsSequenceItem,
)


class MydriaticAgentSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._MydriaticAgentCodeSequence: List[CodeSequenceItem] = []
        self._MydriaticAgentConcentrationUnitsSequence: List[MydriaticAgentConcentrationUnitsSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def MydriaticAgentCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "MydriaticAgentCodeSequence" in self._dataset:
            if len(self._MydriaticAgentCodeSequence) == len(self._dataset.MydriaticAgentCodeSequence):
                return self._MydriaticAgentCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.MydriaticAgentCodeSequence]
        return None

    @MydriaticAgentCodeSequence.setter
    def MydriaticAgentCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._MydriaticAgentCodeSequence = []
            if "MydriaticAgentCodeSequence" in self._dataset:
                del self._dataset.MydriaticAgentCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError(f"MydriaticAgentCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._MydriaticAgentCodeSequence = value
            if "MydriaticAgentCodeSequence" not in self._dataset:
                self._dataset.MydriaticAgentCodeSequence = pydicom.Sequence()
            self._dataset.MydriaticAgentCodeSequence.clear()
            self._dataset.MydriaticAgentCodeSequence.extend([item.to_dataset() for item in value])

    def add_MydriaticAgentCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError(f"Item must be an instance of CodeSequenceItem")
        self._MydriaticAgentCodeSequence.append(item)
        if "MydriaticAgentCodeSequence" not in self._dataset:
            self._dataset.MydriaticAgentCodeSequence = pydicom.Sequence()
        self._dataset.MydriaticAgentCodeSequence.append(item.to_dataset())

    @property
    def MydriaticAgentConcentrationUnitsSequence(self) -> Optional[List[MydriaticAgentConcentrationUnitsSequenceItem]]:
        if "MydriaticAgentConcentrationUnitsSequence" in self._dataset:
            if len(self._MydriaticAgentConcentrationUnitsSequence) == len(
                self._dataset.MydriaticAgentConcentrationUnitsSequence
            ):
                return self._MydriaticAgentConcentrationUnitsSequence
            else:
                return [
                    MydriaticAgentConcentrationUnitsSequenceItem(x)
                    for x in self._dataset.MydriaticAgentConcentrationUnitsSequence
                ]
        return None

    @MydriaticAgentConcentrationUnitsSequence.setter
    def MydriaticAgentConcentrationUnitsSequence(self, value: Optional[List[MydriaticAgentConcentrationUnitsSequenceItem]]):
        if value is None:
            self._MydriaticAgentConcentrationUnitsSequence = []
            if "MydriaticAgentConcentrationUnitsSequence" in self._dataset:
                del self._dataset.MydriaticAgentConcentrationUnitsSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, MydriaticAgentConcentrationUnitsSequenceItem) for item in value
        ):
            raise ValueError(
                f"MydriaticAgentConcentrationUnitsSequence must be a list of MydriaticAgentConcentrationUnitsSequenceItem objects"
            )
        else:
            self._MydriaticAgentConcentrationUnitsSequence = value
            if "MydriaticAgentConcentrationUnitsSequence" not in self._dataset:
                self._dataset.MydriaticAgentConcentrationUnitsSequence = pydicom.Sequence()
            self._dataset.MydriaticAgentConcentrationUnitsSequence.clear()
            self._dataset.MydriaticAgentConcentrationUnitsSequence.extend([item.to_dataset() for item in value])

    def add_MydriaticAgentConcentrationUnits(self, item: MydriaticAgentConcentrationUnitsSequenceItem):
        if not isinstance(item, MydriaticAgentConcentrationUnitsSequenceItem):
            raise ValueError(f"Item must be an instance of MydriaticAgentConcentrationUnitsSequenceItem")
        self._MydriaticAgentConcentrationUnitsSequence.append(item)
        if "MydriaticAgentConcentrationUnitsSequence" not in self._dataset:
            self._dataset.MydriaticAgentConcentrationUnitsSequence = pydicom.Sequence()
        self._dataset.MydriaticAgentConcentrationUnitsSequence.append(item.to_dataset())

    @property
    def MydriaticAgentConcentration(self) -> Optional[Decimal]:
        if "MydriaticAgentConcentration" in self._dataset:
            return self._dataset.MydriaticAgentConcentration
        return None

    @MydriaticAgentConcentration.setter
    def MydriaticAgentConcentration(self, value: Optional[Decimal]):
        if value is None:
            if "MydriaticAgentConcentration" in self._dataset:
                del self._dataset.MydriaticAgentConcentration
        else:
            self._dataset.MydriaticAgentConcentration = value
