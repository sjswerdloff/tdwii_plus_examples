from typing import Any, List, Optional  # noqa

import pydicom

from .code_sequence_item import CodeSequenceItem


class DigitalFilterCharacteristicsSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._DigitalFilterTypeCodeSequence: List[CodeSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def DigitalFilterOrder(self) -> Optional[int]:
        if "DigitalFilterOrder" in self._dataset:
            return self._dataset.DigitalFilterOrder
        return None

    @DigitalFilterOrder.setter
    def DigitalFilterOrder(self, value: Optional[int]):
        if value is None:
            if "DigitalFilterOrder" in self._dataset:
                del self._dataset.DigitalFilterOrder
        else:
            self._dataset.DigitalFilterOrder = value

    @property
    def DigitalFilterTypeCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "DigitalFilterTypeCodeSequence" in self._dataset:
            if len(self._DigitalFilterTypeCodeSequence) == len(self._dataset.DigitalFilterTypeCodeSequence):
                return self._DigitalFilterTypeCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.DigitalFilterTypeCodeSequence]
        return None

    @DigitalFilterTypeCodeSequence.setter
    def DigitalFilterTypeCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._DigitalFilterTypeCodeSequence = []
            if "DigitalFilterTypeCodeSequence" in self._dataset:
                del self._dataset.DigitalFilterTypeCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("DigitalFilterTypeCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._DigitalFilterTypeCodeSequence = value
            if "DigitalFilterTypeCodeSequence" not in self._dataset:
                self._dataset.DigitalFilterTypeCodeSequence = pydicom.Sequence()
            self._dataset.DigitalFilterTypeCodeSequence.clear()
            self._dataset.DigitalFilterTypeCodeSequence.extend([item.to_dataset() for item in value])

    def add_DigitalFilterTypeCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._DigitalFilterTypeCodeSequence.append(item)
        if "DigitalFilterTypeCodeSequence" not in self._dataset:
            self._dataset.DigitalFilterTypeCodeSequence = pydicom.Sequence()
        self._dataset.DigitalFilterTypeCodeSequence.append(item.to_dataset())
