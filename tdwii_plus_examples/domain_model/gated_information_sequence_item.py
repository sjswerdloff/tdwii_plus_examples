from decimal import Decimal
from typing import Any, List, Optional

import pydicom

from .data_information_sequence_item import DataInformationSequenceItem


class GatedInformationSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._DataInformationSequence: List[DataInformationSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def TriggerTime(self) -> Optional[Decimal]:
        if "TriggerTime" in self._dataset:
            return self._dataset.TriggerTime
        return None

    @TriggerTime.setter
    def TriggerTime(self, value: Optional[Decimal]):
        if value is None:
            if "TriggerTime" in self._dataset:
                del self._dataset.TriggerTime
        else:
            self._dataset.TriggerTime = value

    @property
    def CardiacFramingType(self) -> Optional[str]:
        if "CardiacFramingType" in self._dataset:
            return self._dataset.CardiacFramingType
        return None

    @CardiacFramingType.setter
    def CardiacFramingType(self, value: Optional[str]):
        if value is None:
            if "CardiacFramingType" in self._dataset:
                del self._dataset.CardiacFramingType
        else:
            self._dataset.CardiacFramingType = value

    @property
    def DataInformationSequence(self) -> Optional[List[DataInformationSequenceItem]]:
        if "DataInformationSequence" in self._dataset:
            if len(self._DataInformationSequence) == len(self._dataset.DataInformationSequence):
                return self._DataInformationSequence
            else:
                return [DataInformationSequenceItem(x) for x in self._dataset.DataInformationSequence]
        return None

    @DataInformationSequence.setter
    def DataInformationSequence(self, value: Optional[List[DataInformationSequenceItem]]):
        if value is None:
            self._DataInformationSequence = []
            if "DataInformationSequence" in self._dataset:
                del self._dataset.DataInformationSequence
        elif not isinstance(value, list) or not all(isinstance(item, DataInformationSequenceItem) for item in value):
            raise ValueError(f"DataInformationSequence must be a list of DataInformationSequenceItem objects")
        else:
            self._DataInformationSequence = value
            if "DataInformationSequence" not in self._dataset:
                self._dataset.DataInformationSequence = pydicom.Sequence()
            self._dataset.DataInformationSequence.clear()
            self._dataset.DataInformationSequence.extend([item.to_dataset() for item in value])

    def add_DataInformation(self, item: DataInformationSequenceItem):
        if not isinstance(item, DataInformationSequenceItem):
            raise ValueError(f"Item must be an instance of DataInformationSequenceItem")
        self._DataInformationSequence.append(item)
        if "DataInformationSequence" not in self._dataset:
            self._dataset.DataInformationSequence = pydicom.Sequence()
        self._dataset.DataInformationSequence.append(item.to_dataset())
