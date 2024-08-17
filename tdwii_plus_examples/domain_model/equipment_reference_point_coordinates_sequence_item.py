from typing import Any, List, Optional  # noqa

import pydicom

from .code_sequence_item import CodeSequenceItem


class EquipmentReferencePointCoordinatesSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._EquipmentReferencePointCodeSequence: List[CodeSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ThreeDPointCoordinates(self) -> Optional[List[float]]:
        if "ThreeDPointCoordinates" in self._dataset:
            return self._dataset.ThreeDPointCoordinates
        return None

    @ThreeDPointCoordinates.setter
    def ThreeDPointCoordinates(self, value: Optional[List[float]]):
        if value is None:
            if "ThreeDPointCoordinates" in self._dataset:
                del self._dataset.ThreeDPointCoordinates
        else:
            self._dataset.ThreeDPointCoordinates = value

    @property
    def EquipmentReferencePointCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "EquipmentReferencePointCodeSequence" in self._dataset:
            if len(self._EquipmentReferencePointCodeSequence) == len(self._dataset.EquipmentReferencePointCodeSequence):
                return self._EquipmentReferencePointCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.EquipmentReferencePointCodeSequence]
        return None

    @EquipmentReferencePointCodeSequence.setter
    def EquipmentReferencePointCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._EquipmentReferencePointCodeSequence = []
            if "EquipmentReferencePointCodeSequence" in self._dataset:
                del self._dataset.EquipmentReferencePointCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("EquipmentReferencePointCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._EquipmentReferencePointCodeSequence = value
            if "EquipmentReferencePointCodeSequence" not in self._dataset:
                self._dataset.EquipmentReferencePointCodeSequence = pydicom.Sequence()
            self._dataset.EquipmentReferencePointCodeSequence.clear()
            self._dataset.EquipmentReferencePointCodeSequence.extend([item.to_dataset() for item in value])

    def add_EquipmentReferencePointCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._EquipmentReferencePointCodeSequence.append(item)
        if "EquipmentReferencePointCodeSequence" not in self._dataset:
            self._dataset.EquipmentReferencePointCodeSequence = pydicom.Sequence()
        self._dataset.EquipmentReferencePointCodeSequence.append(item.to_dataset())
