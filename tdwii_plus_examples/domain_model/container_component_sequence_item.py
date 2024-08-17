from typing import Any, List, Optional  # noqa

import pydicom

from .code_sequence_item import CodeSequenceItem


class ContainerComponentSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._ContainerComponentTypeCodeSequence: List[CodeSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def Manufacturer(self) -> Optional[str]:
        if "Manufacturer" in self._dataset:
            return self._dataset.Manufacturer
        return None

    @Manufacturer.setter
    def Manufacturer(self, value: Optional[str]):
        if value is None:
            if "Manufacturer" in self._dataset:
                del self._dataset.Manufacturer
        else:
            self._dataset.Manufacturer = value

    @property
    def ManufacturerModelName(self) -> Optional[str]:
        if "ManufacturerModelName" in self._dataset:
            return self._dataset.ManufacturerModelName
        return None

    @ManufacturerModelName.setter
    def ManufacturerModelName(self, value: Optional[str]):
        if value is None:
            if "ManufacturerModelName" in self._dataset:
                del self._dataset.ManufacturerModelName
        else:
            self._dataset.ManufacturerModelName = value

    @property
    def ContainerComponentTypeCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "ContainerComponentTypeCodeSequence" in self._dataset:
            if len(self._ContainerComponentTypeCodeSequence) == len(self._dataset.ContainerComponentTypeCodeSequence):
                return self._ContainerComponentTypeCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.ContainerComponentTypeCodeSequence]
        return None

    @ContainerComponentTypeCodeSequence.setter
    def ContainerComponentTypeCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._ContainerComponentTypeCodeSequence = []
            if "ContainerComponentTypeCodeSequence" in self._dataset:
                del self._dataset.ContainerComponentTypeCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("ContainerComponentTypeCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._ContainerComponentTypeCodeSequence = value
            if "ContainerComponentTypeCodeSequence" not in self._dataset:
                self._dataset.ContainerComponentTypeCodeSequence = pydicom.Sequence()
            self._dataset.ContainerComponentTypeCodeSequence.clear()
            self._dataset.ContainerComponentTypeCodeSequence.extend([item.to_dataset() for item in value])

    def add_ContainerComponentTypeCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._ContainerComponentTypeCodeSequence.append(item)
        if "ContainerComponentTypeCodeSequence" not in self._dataset:
            self._dataset.ContainerComponentTypeCodeSequence = pydicom.Sequence()
        self._dataset.ContainerComponentTypeCodeSequence.append(item.to_dataset())

    @property
    def ContainerComponentThickness(self) -> Optional[float]:
        if "ContainerComponentThickness" in self._dataset:
            return self._dataset.ContainerComponentThickness
        return None

    @ContainerComponentThickness.setter
    def ContainerComponentThickness(self, value: Optional[float]):
        if value is None:
            if "ContainerComponentThickness" in self._dataset:
                del self._dataset.ContainerComponentThickness
        else:
            self._dataset.ContainerComponentThickness = value

    @property
    def ContainerComponentWidth(self) -> Optional[float]:
        if "ContainerComponentWidth" in self._dataset:
            return self._dataset.ContainerComponentWidth
        return None

    @ContainerComponentWidth.setter
    def ContainerComponentWidth(self, value: Optional[float]):
        if value is None:
            if "ContainerComponentWidth" in self._dataset:
                del self._dataset.ContainerComponentWidth
        else:
            self._dataset.ContainerComponentWidth = value

    @property
    def ContainerComponentMaterial(self) -> Optional[str]:
        if "ContainerComponentMaterial" in self._dataset:
            return self._dataset.ContainerComponentMaterial
        return None

    @ContainerComponentMaterial.setter
    def ContainerComponentMaterial(self, value: Optional[str]):
        if value is None:
            if "ContainerComponentMaterial" in self._dataset:
                del self._dataset.ContainerComponentMaterial
        else:
            self._dataset.ContainerComponentMaterial = value

    @property
    def ContainerComponentID(self) -> Optional[str]:
        if "ContainerComponentID" in self._dataset:
            return self._dataset.ContainerComponentID
        return None

    @ContainerComponentID.setter
    def ContainerComponentID(self, value: Optional[str]):
        if value is None:
            if "ContainerComponentID" in self._dataset:
                del self._dataset.ContainerComponentID
        else:
            self._dataset.ContainerComponentID = value

    @property
    def ContainerComponentLength(self) -> Optional[float]:
        if "ContainerComponentLength" in self._dataset:
            return self._dataset.ContainerComponentLength
        return None

    @ContainerComponentLength.setter
    def ContainerComponentLength(self, value: Optional[float]):
        if value is None:
            if "ContainerComponentLength" in self._dataset:
                del self._dataset.ContainerComponentLength
        else:
            self._dataset.ContainerComponentLength = value

    @property
    def ContainerComponentDiameter(self) -> Optional[float]:
        if "ContainerComponentDiameter" in self._dataset:
            return self._dataset.ContainerComponentDiameter
        return None

    @ContainerComponentDiameter.setter
    def ContainerComponentDiameter(self, value: Optional[float]):
        if value is None:
            if "ContainerComponentDiameter" in self._dataset:
                del self._dataset.ContainerComponentDiameter
        else:
            self._dataset.ContainerComponentDiameter = value

    @property
    def ContainerComponentDescription(self) -> Optional[str]:
        if "ContainerComponentDescription" in self._dataset:
            return self._dataset.ContainerComponentDescription
        return None

    @ContainerComponentDescription.setter
    def ContainerComponentDescription(self, value: Optional[str]):
        if value is None:
            if "ContainerComponentDescription" in self._dataset:
                del self._dataset.ContainerComponentDescription
        else:
            self._dataset.ContainerComponentDescription = value
