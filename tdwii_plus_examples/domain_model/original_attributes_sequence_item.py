from typing import Any, List, Optional

import pydicom

from .modified_attributes_sequence_item import ModifiedAttributesSequenceItem
from .nonconforming_modified_attributes_sequence_item import (
    NonconformingModifiedAttributesSequenceItem,
)


class OriginalAttributesSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._ModifiedAttributesSequence: List[ModifiedAttributesSequenceItem] = []
        self._NonconformingModifiedAttributesSequence: List[NonconformingModifiedAttributesSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ModifiedAttributesSequence(self) -> Optional[List[ModifiedAttributesSequenceItem]]:
        if "ModifiedAttributesSequence" in self._dataset:
            if len(self._ModifiedAttributesSequence) == len(self._dataset.ModifiedAttributesSequence):
                return self._ModifiedAttributesSequence
            else:
                return [ModifiedAttributesSequenceItem(x) for x in self._dataset.ModifiedAttributesSequence]
        return None

    @ModifiedAttributesSequence.setter
    def ModifiedAttributesSequence(self, value: Optional[List[ModifiedAttributesSequenceItem]]):
        if value is None:
            self._ModifiedAttributesSequence = []
            if "ModifiedAttributesSequence" in self._dataset:
                del self._dataset.ModifiedAttributesSequence
        elif not isinstance(value, list) or not all(isinstance(item, ModifiedAttributesSequenceItem) for item in value):
            raise ValueError(f"ModifiedAttributesSequence must be a list of ModifiedAttributesSequenceItem objects")
        else:
            self._ModifiedAttributesSequence = value
            if "ModifiedAttributesSequence" not in self._dataset:
                self._dataset.ModifiedAttributesSequence = pydicom.Sequence()
            self._dataset.ModifiedAttributesSequence.clear()
            self._dataset.ModifiedAttributesSequence.extend([item.to_dataset() for item in value])

    def add_ModifiedAttributes(self, item: ModifiedAttributesSequenceItem):
        if not isinstance(item, ModifiedAttributesSequenceItem):
            raise ValueError(f"Item must be an instance of ModifiedAttributesSequenceItem")
        self._ModifiedAttributesSequence.append(item)
        if "ModifiedAttributesSequence" not in self._dataset:
            self._dataset.ModifiedAttributesSequence = pydicom.Sequence()
        self._dataset.ModifiedAttributesSequence.append(item.to_dataset())

    @property
    def NonconformingModifiedAttributesSequence(self) -> Optional[List[NonconformingModifiedAttributesSequenceItem]]:
        if "NonconformingModifiedAttributesSequence" in self._dataset:
            if len(self._NonconformingModifiedAttributesSequence) == len(
                self._dataset.NonconformingModifiedAttributesSequence
            ):
                return self._NonconformingModifiedAttributesSequence
            else:
                return [
                    NonconformingModifiedAttributesSequenceItem(x)
                    for x in self._dataset.NonconformingModifiedAttributesSequence
                ]
        return None

    @NonconformingModifiedAttributesSequence.setter
    def NonconformingModifiedAttributesSequence(self, value: Optional[List[NonconformingModifiedAttributesSequenceItem]]):
        if value is None:
            self._NonconformingModifiedAttributesSequence = []
            if "NonconformingModifiedAttributesSequence" in self._dataset:
                del self._dataset.NonconformingModifiedAttributesSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, NonconformingModifiedAttributesSequenceItem) for item in value
        ):
            raise ValueError(
                f"NonconformingModifiedAttributesSequence must be a list of NonconformingModifiedAttributesSequenceItem objects"
            )
        else:
            self._NonconformingModifiedAttributesSequence = value
            if "NonconformingModifiedAttributesSequence" not in self._dataset:
                self._dataset.NonconformingModifiedAttributesSequence = pydicom.Sequence()
            self._dataset.NonconformingModifiedAttributesSequence.clear()
            self._dataset.NonconformingModifiedAttributesSequence.extend([item.to_dataset() for item in value])

    def add_NonconformingModifiedAttributes(self, item: NonconformingModifiedAttributesSequenceItem):
        if not isinstance(item, NonconformingModifiedAttributesSequenceItem):
            raise ValueError(f"Item must be an instance of NonconformingModifiedAttributesSequenceItem")
        self._NonconformingModifiedAttributesSequence.append(item)
        if "NonconformingModifiedAttributesSequence" not in self._dataset:
            self._dataset.NonconformingModifiedAttributesSequence = pydicom.Sequence()
        self._dataset.NonconformingModifiedAttributesSequence.append(item.to_dataset())

    @property
    def AttributeModificationDateTime(self) -> Optional[str]:
        if "AttributeModificationDateTime" in self._dataset:
            return self._dataset.AttributeModificationDateTime
        return None

    @AttributeModificationDateTime.setter
    def AttributeModificationDateTime(self, value: Optional[str]):
        if value is None:
            if "AttributeModificationDateTime" in self._dataset:
                del self._dataset.AttributeModificationDateTime
        else:
            self._dataset.AttributeModificationDateTime = value

    @property
    def ModifyingSystem(self) -> Optional[str]:
        if "ModifyingSystem" in self._dataset:
            return self._dataset.ModifyingSystem
        return None

    @ModifyingSystem.setter
    def ModifyingSystem(self, value: Optional[str]):
        if value is None:
            if "ModifyingSystem" in self._dataset:
                del self._dataset.ModifyingSystem
        else:
            self._dataset.ModifyingSystem = value

    @property
    def SourceOfPreviousValues(self) -> Optional[str]:
        if "SourceOfPreviousValues" in self._dataset:
            return self._dataset.SourceOfPreviousValues
        return None

    @SourceOfPreviousValues.setter
    def SourceOfPreviousValues(self, value: Optional[str]):
        if value is None:
            if "SourceOfPreviousValues" in self._dataset:
                del self._dataset.SourceOfPreviousValues
        else:
            self._dataset.SourceOfPreviousValues = value

    @property
    def ReasonForTheAttributeModification(self) -> Optional[str]:
        if "ReasonForTheAttributeModification" in self._dataset:
            return self._dataset.ReasonForTheAttributeModification
        return None

    @ReasonForTheAttributeModification.setter
    def ReasonForTheAttributeModification(self, value: Optional[str]):
        if value is None:
            if "ReasonForTheAttributeModification" in self._dataset:
                del self._dataset.ReasonForTheAttributeModification
        else:
            self._dataset.ReasonForTheAttributeModification = value
