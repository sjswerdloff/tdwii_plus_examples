from typing import Any, List, Optional

import pydicom

from .blending_display_input_sequence_item import BlendingDisplayInputSequenceItem


class BlendingDisplaySequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._BlendingDisplayInputSequence: List[BlendingDisplayInputSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def RelativeOpacity(self) -> Optional[float]:
        if "RelativeOpacity" in self._dataset:
            return self._dataset.RelativeOpacity
        return None

    @RelativeOpacity.setter
    def RelativeOpacity(self, value: Optional[float]):
        if value is None:
            if "RelativeOpacity" in self._dataset:
                del self._dataset.RelativeOpacity
        else:
            self._dataset.RelativeOpacity = value

    @property
    def BlendingInputNumber(self) -> Optional[int]:
        if "BlendingInputNumber" in self._dataset:
            return self._dataset.BlendingInputNumber
        return None

    @BlendingInputNumber.setter
    def BlendingInputNumber(self, value: Optional[int]):
        if value is None:
            if "BlendingInputNumber" in self._dataset:
                del self._dataset.BlendingInputNumber
        else:
            self._dataset.BlendingInputNumber = value

    @property
    def BlendingDisplayInputSequence(self) -> Optional[List[BlendingDisplayInputSequenceItem]]:
        if "BlendingDisplayInputSequence" in self._dataset:
            if len(self._BlendingDisplayInputSequence) == len(self._dataset.BlendingDisplayInputSequence):
                return self._BlendingDisplayInputSequence
            else:
                return [BlendingDisplayInputSequenceItem(x) for x in self._dataset.BlendingDisplayInputSequence]
        return None

    @BlendingDisplayInputSequence.setter
    def BlendingDisplayInputSequence(self, value: Optional[List[BlendingDisplayInputSequenceItem]]):
        if value is None:
            self._BlendingDisplayInputSequence = []
            if "BlendingDisplayInputSequence" in self._dataset:
                del self._dataset.BlendingDisplayInputSequence
        elif not isinstance(value, list) or not all(isinstance(item, BlendingDisplayInputSequenceItem) for item in value):
            raise ValueError(f"BlendingDisplayInputSequence must be a list of BlendingDisplayInputSequenceItem objects")
        else:
            self._BlendingDisplayInputSequence = value
            if "BlendingDisplayInputSequence" not in self._dataset:
                self._dataset.BlendingDisplayInputSequence = pydicom.Sequence()
            self._dataset.BlendingDisplayInputSequence.clear()
            self._dataset.BlendingDisplayInputSequence.extend([item.to_dataset() for item in value])

    def add_BlendingDisplayInput(self, item: BlendingDisplayInputSequenceItem):
        if not isinstance(item, BlendingDisplayInputSequenceItem):
            raise ValueError(f"Item must be an instance of BlendingDisplayInputSequenceItem")
        self._BlendingDisplayInputSequence.append(item)
        if "BlendingDisplayInputSequence" not in self._dataset:
            self._dataset.BlendingDisplayInputSequence = pydicom.Sequence()
        self._dataset.BlendingDisplayInputSequence.append(item.to_dataset())

    @property
    def BlendingMode(self) -> Optional[str]:
        if "BlendingMode" in self._dataset:
            return self._dataset.BlendingMode
        return None

    @BlendingMode.setter
    def BlendingMode(self, value: Optional[str]):
        if value is None:
            if "BlendingMode" in self._dataset:
                del self._dataset.BlendingMode
        else:
            self._dataset.BlendingMode = value
