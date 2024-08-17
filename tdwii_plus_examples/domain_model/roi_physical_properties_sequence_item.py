from decimal import Decimal
from typing import Any, List, Optional  # noqa

import pydicom

from .roi_elemental_composition_sequence_item import ROIElementalCompositionSequenceItem


class ROIPhysicalPropertiesSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._ROIElementalCompositionSequence: List[ROIElementalCompositionSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ROIPhysicalProperty(self) -> Optional[str]:
        if "ROIPhysicalProperty" in self._dataset:
            return self._dataset.ROIPhysicalProperty
        return None

    @ROIPhysicalProperty.setter
    def ROIPhysicalProperty(self, value: Optional[str]):
        if value is None:
            if "ROIPhysicalProperty" in self._dataset:
                del self._dataset.ROIPhysicalProperty
        else:
            self._dataset.ROIPhysicalProperty = value

    @property
    def ROIPhysicalPropertyValue(self) -> Optional[Decimal]:
        if "ROIPhysicalPropertyValue" in self._dataset:
            return self._dataset.ROIPhysicalPropertyValue
        return None

    @ROIPhysicalPropertyValue.setter
    def ROIPhysicalPropertyValue(self, value: Optional[Decimal]):
        if value is None:
            if "ROIPhysicalPropertyValue" in self._dataset:
                del self._dataset.ROIPhysicalPropertyValue
        else:
            self._dataset.ROIPhysicalPropertyValue = value

    @property
    def ROIElementalCompositionSequence(self) -> Optional[List[ROIElementalCompositionSequenceItem]]:
        if "ROIElementalCompositionSequence" in self._dataset:
            if len(self._ROIElementalCompositionSequence) == len(self._dataset.ROIElementalCompositionSequence):
                return self._ROIElementalCompositionSequence
            else:
                return [ROIElementalCompositionSequenceItem(x) for x in self._dataset.ROIElementalCompositionSequence]
        return None

    @ROIElementalCompositionSequence.setter
    def ROIElementalCompositionSequence(self, value: Optional[List[ROIElementalCompositionSequenceItem]]):
        if value is None:
            self._ROIElementalCompositionSequence = []
            if "ROIElementalCompositionSequence" in self._dataset:
                del self._dataset.ROIElementalCompositionSequence
        elif not isinstance(value, list) or not all(isinstance(item, ROIElementalCompositionSequenceItem) for item in value):
            raise ValueError("ROIElementalCompositionSequence must be a list of ROIElementalCompositionSequenceItem objects")
        else:
            self._ROIElementalCompositionSequence = value
            if "ROIElementalCompositionSequence" not in self._dataset:
                self._dataset.ROIElementalCompositionSequence = pydicom.Sequence()
            self._dataset.ROIElementalCompositionSequence.clear()
            self._dataset.ROIElementalCompositionSequence.extend([item.to_dataset() for item in value])

    def add_ROIElementalComposition(self, item: ROIElementalCompositionSequenceItem):
        if not isinstance(item, ROIElementalCompositionSequenceItem):
            raise ValueError("Item must be an instance of ROIElementalCompositionSequenceItem")
        self._ROIElementalCompositionSequence.append(item)
        if "ROIElementalCompositionSequence" not in self._dataset:
            self._dataset.ROIElementalCompositionSequence = pydicom.Sequence()
        self._dataset.ROIElementalCompositionSequence.append(item.to_dataset())
