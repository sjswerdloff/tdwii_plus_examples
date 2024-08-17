from typing import Any, List, Optional

import pydicom

from .flow_identifier_sequence_item import FlowIdentifierSequenceItem


class RealTimeBulkDataFlowSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._FlowIdentifierSequence: List[FlowIdentifierSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def FlowIdentifierSequence(self) -> Optional[List[FlowIdentifierSequenceItem]]:
        if "FlowIdentifierSequence" in self._dataset:
            if len(self._FlowIdentifierSequence) == len(self._dataset.FlowIdentifierSequence):
                return self._FlowIdentifierSequence
            else:
                return [FlowIdentifierSequenceItem(x) for x in self._dataset.FlowIdentifierSequence]
        return None

    @FlowIdentifierSequence.setter
    def FlowIdentifierSequence(self, value: Optional[List[FlowIdentifierSequenceItem]]):
        if value is None:
            self._FlowIdentifierSequence = []
            if "FlowIdentifierSequence" in self._dataset:
                del self._dataset.FlowIdentifierSequence
        elif not isinstance(value, list) or not all(isinstance(item, FlowIdentifierSequenceItem) for item in value):
            raise ValueError(f"FlowIdentifierSequence must be a list of FlowIdentifierSequenceItem objects")
        else:
            self._FlowIdentifierSequence = value
            if "FlowIdentifierSequence" not in self._dataset:
                self._dataset.FlowIdentifierSequence = pydicom.Sequence()
            self._dataset.FlowIdentifierSequence.clear()
            self._dataset.FlowIdentifierSequence.extend([item.to_dataset() for item in value])

    def add_FlowIdentifier(self, item: FlowIdentifierSequenceItem):
        if not isinstance(item, FlowIdentifierSequenceItem):
            raise ValueError(f"Item must be an instance of FlowIdentifierSequenceItem")
        self._FlowIdentifierSequence.append(item)
        if "FlowIdentifierSequence" not in self._dataset:
            self._dataset.FlowIdentifierSequence = pydicom.Sequence()
        self._dataset.FlowIdentifierSequence.append(item.to_dataset())

    @property
    def SourceIdentifier(self) -> Optional[bytes]:
        if "SourceIdentifier" in self._dataset:
            return self._dataset.SourceIdentifier
        return None

    @SourceIdentifier.setter
    def SourceIdentifier(self, value: Optional[bytes]):
        if value is None:
            if "SourceIdentifier" in self._dataset:
                del self._dataset.SourceIdentifier
        else:
            self._dataset.SourceIdentifier = value
