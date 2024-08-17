from typing import Any, List, Optional

import pydicom

from .multi_coil_definition_sequence_item import MultiCoilDefinitionSequenceItem


class MRReceiveCoilSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._MultiCoilDefinitionSequence: List[MultiCoilDefinitionSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ReceiveCoilName(self) -> Optional[str]:
        if "ReceiveCoilName" in self._dataset:
            return self._dataset.ReceiveCoilName
        return None

    @ReceiveCoilName.setter
    def ReceiveCoilName(self, value: Optional[str]):
        if value is None:
            if "ReceiveCoilName" in self._dataset:
                del self._dataset.ReceiveCoilName
        else:
            self._dataset.ReceiveCoilName = value

    @property
    def ReceiveCoilManufacturerName(self) -> Optional[str]:
        if "ReceiveCoilManufacturerName" in self._dataset:
            return self._dataset.ReceiveCoilManufacturerName
        return None

    @ReceiveCoilManufacturerName.setter
    def ReceiveCoilManufacturerName(self, value: Optional[str]):
        if value is None:
            if "ReceiveCoilManufacturerName" in self._dataset:
                del self._dataset.ReceiveCoilManufacturerName
        else:
            self._dataset.ReceiveCoilManufacturerName = value

    @property
    def ReceiveCoilType(self) -> Optional[str]:
        if "ReceiveCoilType" in self._dataset:
            return self._dataset.ReceiveCoilType
        return None

    @ReceiveCoilType.setter
    def ReceiveCoilType(self, value: Optional[str]):
        if value is None:
            if "ReceiveCoilType" in self._dataset:
                del self._dataset.ReceiveCoilType
        else:
            self._dataset.ReceiveCoilType = value

    @property
    def QuadratureReceiveCoil(self) -> Optional[str]:
        if "QuadratureReceiveCoil" in self._dataset:
            return self._dataset.QuadratureReceiveCoil
        return None

    @QuadratureReceiveCoil.setter
    def QuadratureReceiveCoil(self, value: Optional[str]):
        if value is None:
            if "QuadratureReceiveCoil" in self._dataset:
                del self._dataset.QuadratureReceiveCoil
        else:
            self._dataset.QuadratureReceiveCoil = value

    @property
    def MultiCoilDefinitionSequence(self) -> Optional[List[MultiCoilDefinitionSequenceItem]]:
        if "MultiCoilDefinitionSequence" in self._dataset:
            if len(self._MultiCoilDefinitionSequence) == len(self._dataset.MultiCoilDefinitionSequence):
                return self._MultiCoilDefinitionSequence
            else:
                return [MultiCoilDefinitionSequenceItem(x) for x in self._dataset.MultiCoilDefinitionSequence]
        return None

    @MultiCoilDefinitionSequence.setter
    def MultiCoilDefinitionSequence(self, value: Optional[List[MultiCoilDefinitionSequenceItem]]):
        if value is None:
            self._MultiCoilDefinitionSequence = []
            if "MultiCoilDefinitionSequence" in self._dataset:
                del self._dataset.MultiCoilDefinitionSequence
        elif not isinstance(value, list) or not all(isinstance(item, MultiCoilDefinitionSequenceItem) for item in value):
            raise ValueError(f"MultiCoilDefinitionSequence must be a list of MultiCoilDefinitionSequenceItem objects")
        else:
            self._MultiCoilDefinitionSequence = value
            if "MultiCoilDefinitionSequence" not in self._dataset:
                self._dataset.MultiCoilDefinitionSequence = pydicom.Sequence()
            self._dataset.MultiCoilDefinitionSequence.clear()
            self._dataset.MultiCoilDefinitionSequence.extend([item.to_dataset() for item in value])

    def add_MultiCoilDefinition(self, item: MultiCoilDefinitionSequenceItem):
        if not isinstance(item, MultiCoilDefinitionSequenceItem):
            raise ValueError(f"Item must be an instance of MultiCoilDefinitionSequenceItem")
        self._MultiCoilDefinitionSequence.append(item)
        if "MultiCoilDefinitionSequence" not in self._dataset:
            self._dataset.MultiCoilDefinitionSequence = pydicom.Sequence()
        self._dataset.MultiCoilDefinitionSequence.append(item.to_dataset())

    @property
    def MultiCoilConfiguration(self) -> Optional[str]:
        if "MultiCoilConfiguration" in self._dataset:
            return self._dataset.MultiCoilConfiguration
        return None

    @MultiCoilConfiguration.setter
    def MultiCoilConfiguration(self, value: Optional[str]):
        if value is None:
            if "MultiCoilConfiguration" in self._dataset:
                del self._dataset.MultiCoilConfiguration
        else:
            self._dataset.MultiCoilConfiguration = value
