from typing import Any, List, Optional

import pydicom

from .code_sequence_item import CodeSequenceItem


class EventTimerSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._EventCodeSequence: List[CodeSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def EventTimerNames(self) -> Optional[List[str]]:
        if "EventTimerNames" in self._dataset:
            return self._dataset.EventTimerNames
        return None

    @EventTimerNames.setter
    def EventTimerNames(self, value: Optional[List[str]]):
        if value is None:
            if "EventTimerNames" in self._dataset:
                del self._dataset.EventTimerNames
        else:
            self._dataset.EventTimerNames = value

    @property
    def EventTimeOffset(self) -> Optional[float]:
        if "EventTimeOffset" in self._dataset:
            return self._dataset.EventTimeOffset
        return None

    @EventTimeOffset.setter
    def EventTimeOffset(self, value: Optional[float]):
        if value is None:
            if "EventTimeOffset" in self._dataset:
                del self._dataset.EventTimeOffset
        else:
            self._dataset.EventTimeOffset = value

    @property
    def EventCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "EventCodeSequence" in self._dataset:
            if len(self._EventCodeSequence) == len(self._dataset.EventCodeSequence):
                return self._EventCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.EventCodeSequence]
        return None

    @EventCodeSequence.setter
    def EventCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._EventCodeSequence = []
            if "EventCodeSequence" in self._dataset:
                del self._dataset.EventCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError(f"EventCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._EventCodeSequence = value
            if "EventCodeSequence" not in self._dataset:
                self._dataset.EventCodeSequence = pydicom.Sequence()
            self._dataset.EventCodeSequence.clear()
            self._dataset.EventCodeSequence.extend([item.to_dataset() for item in value])

    def add_EventCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError(f"Item must be an instance of CodeSequenceItem")
        self._EventCodeSequence.append(item)
        if "EventCodeSequence" not in self._dataset:
            self._dataset.EventCodeSequence = pydicom.Sequence()
        self._dataset.EventCodeSequence.append(item.to_dataset())
