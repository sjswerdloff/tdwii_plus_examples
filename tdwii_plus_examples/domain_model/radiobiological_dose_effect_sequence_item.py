from typing import Any, List, Optional

import pydicom

from .code_sequence_item import CodeSequenceItem


class RadiobiologicalDoseEffectSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._EffectiveDoseCalculationMethodCategoryCodeSequence: List[CodeSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def RadiobiologicalDoseEffectFlag(self) -> Optional[str]:
        if "RadiobiologicalDoseEffectFlag" in self._dataset:
            return self._dataset.RadiobiologicalDoseEffectFlag
        return None

    @RadiobiologicalDoseEffectFlag.setter
    def RadiobiologicalDoseEffectFlag(self, value: Optional[str]):
        if value is None:
            if "RadiobiologicalDoseEffectFlag" in self._dataset:
                del self._dataset.RadiobiologicalDoseEffectFlag
        else:
            self._dataset.RadiobiologicalDoseEffectFlag = value

    @property
    def EffectiveDoseCalculationMethodCategoryCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "EffectiveDoseCalculationMethodCategoryCodeSequence" in self._dataset:
            if len(self._EffectiveDoseCalculationMethodCategoryCodeSequence) == len(
                self._dataset.EffectiveDoseCalculationMethodCategoryCodeSequence
            ):
                return self._EffectiveDoseCalculationMethodCategoryCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.EffectiveDoseCalculationMethodCategoryCodeSequence]
        return None

    @EffectiveDoseCalculationMethodCategoryCodeSequence.setter
    def EffectiveDoseCalculationMethodCategoryCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._EffectiveDoseCalculationMethodCategoryCodeSequence = []
            if "EffectiveDoseCalculationMethodCategoryCodeSequence" in self._dataset:
                del self._dataset.EffectiveDoseCalculationMethodCategoryCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError(f"EffectiveDoseCalculationMethodCategoryCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._EffectiveDoseCalculationMethodCategoryCodeSequence = value
            if "EffectiveDoseCalculationMethodCategoryCodeSequence" not in self._dataset:
                self._dataset.EffectiveDoseCalculationMethodCategoryCodeSequence = pydicom.Sequence()
            self._dataset.EffectiveDoseCalculationMethodCategoryCodeSequence.clear()
            self._dataset.EffectiveDoseCalculationMethodCategoryCodeSequence.extend([item.to_dataset() for item in value])

    def add_EffectiveDoseCalculationMethodCategoryCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError(f"Item must be an instance of CodeSequenceItem")
        self._EffectiveDoseCalculationMethodCategoryCodeSequence.append(item)
        if "EffectiveDoseCalculationMethodCategoryCodeSequence" not in self._dataset:
            self._dataset.EffectiveDoseCalculationMethodCategoryCodeSequence = pydicom.Sequence()
        self._dataset.EffectiveDoseCalculationMethodCategoryCodeSequence.append(item.to_dataset())

    @property
    def EffectiveDoseCalculationMethodDescription(self) -> Optional[str]:
        if "EffectiveDoseCalculationMethodDescription" in self._dataset:
            return self._dataset.EffectiveDoseCalculationMethodDescription
        return None

    @EffectiveDoseCalculationMethodDescription.setter
    def EffectiveDoseCalculationMethodDescription(self, value: Optional[str]):
        if value is None:
            if "EffectiveDoseCalculationMethodDescription" in self._dataset:
                del self._dataset.EffectiveDoseCalculationMethodDescription
        else:
            self._dataset.EffectiveDoseCalculationMethodDescription = value
