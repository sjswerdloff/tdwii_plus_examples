from typing import Any, List, Optional

import pydicom

from .specimen_preparation_step_content_item_sequence_item import (
    SpecimenPreparationStepContentItemSequenceItem,
)


class SpecimenPreparationSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._SpecimenPreparationStepContentItemSequence: List[SpecimenPreparationStepContentItemSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def SpecimenPreparationStepContentItemSequence(self) -> Optional[List[SpecimenPreparationStepContentItemSequenceItem]]:
        if "SpecimenPreparationStepContentItemSequence" in self._dataset:
            if len(self._SpecimenPreparationStepContentItemSequence) == len(
                self._dataset.SpecimenPreparationStepContentItemSequence
            ):
                return self._SpecimenPreparationStepContentItemSequence
            else:
                return [
                    SpecimenPreparationStepContentItemSequenceItem(x)
                    for x in self._dataset.SpecimenPreparationStepContentItemSequence
                ]
        return None

    @SpecimenPreparationStepContentItemSequence.setter
    def SpecimenPreparationStepContentItemSequence(
        self, value: Optional[List[SpecimenPreparationStepContentItemSequenceItem]]
    ):
        if value is None:
            self._SpecimenPreparationStepContentItemSequence = []
            if "SpecimenPreparationStepContentItemSequence" in self._dataset:
                del self._dataset.SpecimenPreparationStepContentItemSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, SpecimenPreparationStepContentItemSequenceItem) for item in value
        ):
            raise ValueError(
                f"SpecimenPreparationStepContentItemSequence must be a list of SpecimenPreparationStepContentItemSequenceItem objects"
            )
        else:
            self._SpecimenPreparationStepContentItemSequence = value
            if "SpecimenPreparationStepContentItemSequence" not in self._dataset:
                self._dataset.SpecimenPreparationStepContentItemSequence = pydicom.Sequence()
            self._dataset.SpecimenPreparationStepContentItemSequence.clear()
            self._dataset.SpecimenPreparationStepContentItemSequence.extend([item.to_dataset() for item in value])

    def add_SpecimenPreparationStepContentItem(self, item: SpecimenPreparationStepContentItemSequenceItem):
        if not isinstance(item, SpecimenPreparationStepContentItemSequenceItem):
            raise ValueError(f"Item must be an instance of SpecimenPreparationStepContentItemSequenceItem")
        self._SpecimenPreparationStepContentItemSequence.append(item)
        if "SpecimenPreparationStepContentItemSequence" not in self._dataset:
            self._dataset.SpecimenPreparationStepContentItemSequence = pydicom.Sequence()
        self._dataset.SpecimenPreparationStepContentItemSequence.append(item.to_dataset())
