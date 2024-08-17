from typing import Any, List, Optional

import pydicom

from .device_position_parameter_sequence_item import DevicePositionParameterSequenceItem


class ImageReceptorPositionSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._DevicePositionParameterSequence: List[DevicePositionParameterSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def DevicePositionToEquipmentMappingMatrix(self) -> Optional[List[float]]:
        if "DevicePositionToEquipmentMappingMatrix" in self._dataset:
            return self._dataset.DevicePositionToEquipmentMappingMatrix
        return None

    @DevicePositionToEquipmentMappingMatrix.setter
    def DevicePositionToEquipmentMappingMatrix(self, value: Optional[List[float]]):
        if value is None:
            if "DevicePositionToEquipmentMappingMatrix" in self._dataset:
                del self._dataset.DevicePositionToEquipmentMappingMatrix
        else:
            self._dataset.DevicePositionToEquipmentMappingMatrix = value

    @property
    def DevicePositionParameterSequence(self) -> Optional[List[DevicePositionParameterSequenceItem]]:
        if "DevicePositionParameterSequence" in self._dataset:
            if len(self._DevicePositionParameterSequence) == len(self._dataset.DevicePositionParameterSequence):
                return self._DevicePositionParameterSequence
            else:
                return [DevicePositionParameterSequenceItem(x) for x in self._dataset.DevicePositionParameterSequence]
        return None

    @DevicePositionParameterSequence.setter
    def DevicePositionParameterSequence(self, value: Optional[List[DevicePositionParameterSequenceItem]]):
        if value is None:
            self._DevicePositionParameterSequence = []
            if "DevicePositionParameterSequence" in self._dataset:
                del self._dataset.DevicePositionParameterSequence
        elif not isinstance(value, list) or not all(isinstance(item, DevicePositionParameterSequenceItem) for item in value):
            raise ValueError(f"DevicePositionParameterSequence must be a list of DevicePositionParameterSequenceItem objects")
        else:
            self._DevicePositionParameterSequence = value
            if "DevicePositionParameterSequence" not in self._dataset:
                self._dataset.DevicePositionParameterSequence = pydicom.Sequence()
            self._dataset.DevicePositionParameterSequence.clear()
            self._dataset.DevicePositionParameterSequence.extend([item.to_dataset() for item in value])

    def add_DevicePositionParameter(self, item: DevicePositionParameterSequenceItem):
        if not isinstance(item, DevicePositionParameterSequenceItem):
            raise ValueError(f"Item must be an instance of DevicePositionParameterSequenceItem")
        self._DevicePositionParameterSequence.append(item)
        if "DevicePositionParameterSequence" not in self._dataset:
            self._dataset.DevicePositionParameterSequence = pydicom.Sequence()
        self._dataset.DevicePositionParameterSequence.append(item.to_dataset())

    @property
    def ReferencedDefinedDeviceIndex(self) -> Optional[int]:
        if "ReferencedDefinedDeviceIndex" in self._dataset:
            return self._dataset.ReferencedDefinedDeviceIndex
        return None

    @ReferencedDefinedDeviceIndex.setter
    def ReferencedDefinedDeviceIndex(self, value: Optional[int]):
        if value is None:
            if "ReferencedDefinedDeviceIndex" in self._dataset:
                del self._dataset.ReferencedDefinedDeviceIndex
        else:
            self._dataset.ReferencedDefinedDeviceIndex = value
