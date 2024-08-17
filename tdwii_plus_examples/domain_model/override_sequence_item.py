from typing import Any, List, Optional  # noqa

import pydicom

from .operator_identification_sequence_item import OperatorIdentificationSequenceItem


class OverrideSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._OperatorIdentificationSequence: List[OperatorIdentificationSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def OperatorsName(self) -> Optional[List[str]]:
        if "OperatorsName" in self._dataset:
            return self._dataset.OperatorsName
        return None

    @OperatorsName.setter
    def OperatorsName(self, value: Optional[List[str]]):
        if value is None:
            if "OperatorsName" in self._dataset:
                del self._dataset.OperatorsName
        else:
            self._dataset.OperatorsName = value

    @property
    def OperatorIdentificationSequence(self) -> Optional[List[OperatorIdentificationSequenceItem]]:
        if "OperatorIdentificationSequence" in self._dataset:
            if len(self._OperatorIdentificationSequence) == len(self._dataset.OperatorIdentificationSequence):
                return self._OperatorIdentificationSequence
            else:
                return [OperatorIdentificationSequenceItem(x) for x in self._dataset.OperatorIdentificationSequence]
        return None

    @OperatorIdentificationSequence.setter
    def OperatorIdentificationSequence(self, value: Optional[List[OperatorIdentificationSequenceItem]]):
        if value is None:
            self._OperatorIdentificationSequence = []
            if "OperatorIdentificationSequence" in self._dataset:
                del self._dataset.OperatorIdentificationSequence
        elif not isinstance(value, list) or not all(isinstance(item, OperatorIdentificationSequenceItem) for item in value):
            raise ValueError("OperatorIdentificationSequence must be a list of OperatorIdentificationSequenceItem objects")
        else:
            self._OperatorIdentificationSequence = value
            if "OperatorIdentificationSequence" not in self._dataset:
                self._dataset.OperatorIdentificationSequence = pydicom.Sequence()
            self._dataset.OperatorIdentificationSequence.clear()
            self._dataset.OperatorIdentificationSequence.extend([item.to_dataset() for item in value])

    def add_OperatorIdentification(self, item: OperatorIdentificationSequenceItem):
        if not isinstance(item, OperatorIdentificationSequenceItem):
            raise ValueError("Item must be an instance of OperatorIdentificationSequenceItem")
        self._OperatorIdentificationSequence.append(item)
        if "OperatorIdentificationSequence" not in self._dataset:
            self._dataset.OperatorIdentificationSequence = pydicom.Sequence()
        self._dataset.OperatorIdentificationSequence.append(item.to_dataset())

    @property
    def OverrideParameterPointer(self) -> Optional[int]:
        if "OverrideParameterPointer" in self._dataset:
            return self._dataset.OverrideParameterPointer
        return None

    @OverrideParameterPointer.setter
    def OverrideParameterPointer(self, value: Optional[int]):
        if value is None:
            if "OverrideParameterPointer" in self._dataset:
                del self._dataset.OverrideParameterPointer
        else:
            self._dataset.OverrideParameterPointer = value

    @property
    def OverrideReason(self) -> Optional[str]:
        if "OverrideReason" in self._dataset:
            return self._dataset.OverrideReason
        return None

    @OverrideReason.setter
    def OverrideReason(self, value: Optional[str]):
        if value is None:
            if "OverrideReason" in self._dataset:
                del self._dataset.OverrideReason
        else:
            self._dataset.OverrideReason = value
