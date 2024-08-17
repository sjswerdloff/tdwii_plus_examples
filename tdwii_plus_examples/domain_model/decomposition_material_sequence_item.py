from typing import Any, List, Optional  # noqa

import pydicom

from .code_sequence_item import CodeSequenceItem
from .material_attenuation_sequence_item import MaterialAttenuationSequenceItem


class DecompositionMaterialSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._MaterialCodeSequence: List[CodeSequenceItem] = []
        self._MaterialAttenuationSequence: List[MaterialAttenuationSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def MaterialCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "MaterialCodeSequence" in self._dataset:
            if len(self._MaterialCodeSequence) == len(self._dataset.MaterialCodeSequence):
                return self._MaterialCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.MaterialCodeSequence]
        return None

    @MaterialCodeSequence.setter
    def MaterialCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._MaterialCodeSequence = []
            if "MaterialCodeSequence" in self._dataset:
                del self._dataset.MaterialCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("MaterialCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._MaterialCodeSequence = value
            if "MaterialCodeSequence" not in self._dataset:
                self._dataset.MaterialCodeSequence = pydicom.Sequence()
            self._dataset.MaterialCodeSequence.clear()
            self._dataset.MaterialCodeSequence.extend([item.to_dataset() for item in value])

    def add_MaterialCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._MaterialCodeSequence.append(item)
        if "MaterialCodeSequence" not in self._dataset:
            self._dataset.MaterialCodeSequence = pydicom.Sequence()
        self._dataset.MaterialCodeSequence.append(item.to_dataset())

    @property
    def MaterialAttenuationSequence(self) -> Optional[List[MaterialAttenuationSequenceItem]]:
        if "MaterialAttenuationSequence" in self._dataset:
            if len(self._MaterialAttenuationSequence) == len(self._dataset.MaterialAttenuationSequence):
                return self._MaterialAttenuationSequence
            else:
                return [MaterialAttenuationSequenceItem(x) for x in self._dataset.MaterialAttenuationSequence]
        return None

    @MaterialAttenuationSequence.setter
    def MaterialAttenuationSequence(self, value: Optional[List[MaterialAttenuationSequenceItem]]):
        if value is None:
            self._MaterialAttenuationSequence = []
            if "MaterialAttenuationSequence" in self._dataset:
                del self._dataset.MaterialAttenuationSequence
        elif not isinstance(value, list) or not all(isinstance(item, MaterialAttenuationSequenceItem) for item in value):
            raise ValueError("MaterialAttenuationSequence must be a list of MaterialAttenuationSequenceItem objects")
        else:
            self._MaterialAttenuationSequence = value
            if "MaterialAttenuationSequence" not in self._dataset:
                self._dataset.MaterialAttenuationSequence = pydicom.Sequence()
            self._dataset.MaterialAttenuationSequence.clear()
            self._dataset.MaterialAttenuationSequence.extend([item.to_dataset() for item in value])

    def add_MaterialAttenuation(self, item: MaterialAttenuationSequenceItem):
        if not isinstance(item, MaterialAttenuationSequenceItem):
            raise ValueError("Item must be an instance of MaterialAttenuationSequenceItem")
        self._MaterialAttenuationSequence.append(item)
        if "MaterialAttenuationSequence" not in self._dataset:
            self._dataset.MaterialAttenuationSequence = pydicom.Sequence()
        self._dataset.MaterialAttenuationSequence.append(item.to_dataset())
