from typing import Any, List, Optional

import pydicom

from .weighting_transfer_function_sequence_item import (
    WeightingTransferFunctionSequenceItem,
)


class PresentationStateCompositorComponentSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._WeightingTransferFunctionSequence: List[WeightingTransferFunctionSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def WeightingTransferFunctionSequence(self) -> Optional[List[WeightingTransferFunctionSequenceItem]]:
        if "WeightingTransferFunctionSequence" in self._dataset:
            if len(self._WeightingTransferFunctionSequence) == len(self._dataset.WeightingTransferFunctionSequence):
                return self._WeightingTransferFunctionSequence
            else:
                return [WeightingTransferFunctionSequenceItem(x) for x in self._dataset.WeightingTransferFunctionSequence]
        return None

    @WeightingTransferFunctionSequence.setter
    def WeightingTransferFunctionSequence(self, value: Optional[List[WeightingTransferFunctionSequenceItem]]):
        if value is None:
            self._WeightingTransferFunctionSequence = []
            if "WeightingTransferFunctionSequence" in self._dataset:
                del self._dataset.WeightingTransferFunctionSequence
        elif not isinstance(value, list) or not all(isinstance(item, WeightingTransferFunctionSequenceItem) for item in value):
            raise ValueError(
                f"WeightingTransferFunctionSequence must be a list of WeightingTransferFunctionSequenceItem objects"
            )
        else:
            self._WeightingTransferFunctionSequence = value
            if "WeightingTransferFunctionSequence" not in self._dataset:
                self._dataset.WeightingTransferFunctionSequence = pydicom.Sequence()
            self._dataset.WeightingTransferFunctionSequence.clear()
            self._dataset.WeightingTransferFunctionSequence.extend([item.to_dataset() for item in value])

    def add_WeightingTransferFunction(self, item: WeightingTransferFunctionSequenceItem):
        if not isinstance(item, WeightingTransferFunctionSequenceItem):
            raise ValueError(f"Item must be an instance of WeightingTransferFunctionSequenceItem")
        self._WeightingTransferFunctionSequence.append(item)
        if "WeightingTransferFunctionSequence" not in self._dataset:
            self._dataset.WeightingTransferFunctionSequence = pydicom.Sequence()
        self._dataset.WeightingTransferFunctionSequence.append(item.to_dataset())
