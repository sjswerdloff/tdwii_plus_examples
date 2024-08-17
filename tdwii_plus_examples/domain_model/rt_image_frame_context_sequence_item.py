from typing import Any, List, Optional  # noqa

import pydicom

from .rt_image_scope_sequence_item import RTImageScopeSequenceItem


class RTImageFrameContextSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._RTImageScopeSequence: List[RTImageScopeSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def RTImageScopeSequence(self) -> Optional[List[RTImageScopeSequenceItem]]:
        if "RTImageScopeSequence" in self._dataset:
            if len(self._RTImageScopeSequence) == len(self._dataset.RTImageScopeSequence):
                return self._RTImageScopeSequence
            else:
                return [RTImageScopeSequenceItem(x) for x in self._dataset.RTImageScopeSequence]
        return None

    @RTImageScopeSequence.setter
    def RTImageScopeSequence(self, value: Optional[List[RTImageScopeSequenceItem]]):
        if value is None:
            self._RTImageScopeSequence = []
            if "RTImageScopeSequence" in self._dataset:
                del self._dataset.RTImageScopeSequence
        elif not isinstance(value, list) or not all(isinstance(item, RTImageScopeSequenceItem) for item in value):
            raise ValueError("RTImageScopeSequence must be a list of RTImageScopeSequenceItem objects")
        else:
            self._RTImageScopeSequence = value
            if "RTImageScopeSequence" not in self._dataset:
                self._dataset.RTImageScopeSequence = pydicom.Sequence()
            self._dataset.RTImageScopeSequence.clear()
            self._dataset.RTImageScopeSequence.extend([item.to_dataset() for item in value])

    def add_RTImageScope(self, item: RTImageScopeSequenceItem):
        if not isinstance(item, RTImageScopeSequenceItem):
            raise ValueError("Item must be an instance of RTImageScopeSequenceItem")
        self._RTImageScopeSequence.append(item)
        if "RTImageScopeSequence" not in self._dataset:
            self._dataset.RTImageScopeSequence = pydicom.Sequence()
        self._dataset.RTImageScopeSequence.append(item.to_dataset())

    @property
    def RTRadiationSetDeliveryNumber(self) -> Optional[int]:
        if "RTRadiationSetDeliveryNumber" in self._dataset:
            return self._dataset.RTRadiationSetDeliveryNumber
        return None

    @RTRadiationSetDeliveryNumber.setter
    def RTRadiationSetDeliveryNumber(self, value: Optional[int]):
        if value is None:
            if "RTRadiationSetDeliveryNumber" in self._dataset:
                del self._dataset.RTRadiationSetDeliveryNumber
        else:
            self._dataset.RTRadiationSetDeliveryNumber = value

    @property
    def ClinicalFractionNumber(self) -> Optional[int]:
        if "ClinicalFractionNumber" in self._dataset:
            return self._dataset.ClinicalFractionNumber
        return None

    @ClinicalFractionNumber.setter
    def ClinicalFractionNumber(self, value: Optional[int]):
        if value is None:
            if "ClinicalFractionNumber" in self._dataset:
                del self._dataset.ClinicalFractionNumber
        else:
            self._dataset.ClinicalFractionNumber = value
