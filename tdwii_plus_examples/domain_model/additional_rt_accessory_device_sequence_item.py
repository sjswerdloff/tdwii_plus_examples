from typing import Any, List, Optional

import pydicom

from .device_specific_acquisition_parameter_sequence_item import (
    DeviceSpecificAcquisitionParameterSequenceItem,
)


class AdditionalRTAccessoryDeviceSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._DeviceSpecificAcquisitionParameterSequence: List[DeviceSpecificAcquisitionParameterSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def DeviceSpecificAcquisitionParameterSequence(self) -> Optional[List[DeviceSpecificAcquisitionParameterSequenceItem]]:
        if "DeviceSpecificAcquisitionParameterSequence" in self._dataset:
            if len(self._DeviceSpecificAcquisitionParameterSequence) == len(
                self._dataset.DeviceSpecificAcquisitionParameterSequence
            ):
                return self._DeviceSpecificAcquisitionParameterSequence
            else:
                return [
                    DeviceSpecificAcquisitionParameterSequenceItem(x)
                    for x in self._dataset.DeviceSpecificAcquisitionParameterSequence
                ]
        return None

    @DeviceSpecificAcquisitionParameterSequence.setter
    def DeviceSpecificAcquisitionParameterSequence(
        self, value: Optional[List[DeviceSpecificAcquisitionParameterSequenceItem]]
    ):
        if value is None:
            self._DeviceSpecificAcquisitionParameterSequence = []
            if "DeviceSpecificAcquisitionParameterSequence" in self._dataset:
                del self._dataset.DeviceSpecificAcquisitionParameterSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, DeviceSpecificAcquisitionParameterSequenceItem) for item in value
        ):
            raise ValueError(
                f"DeviceSpecificAcquisitionParameterSequence must be a list of DeviceSpecificAcquisitionParameterSequenceItem objects"
            )
        else:
            self._DeviceSpecificAcquisitionParameterSequence = value
            if "DeviceSpecificAcquisitionParameterSequence" not in self._dataset:
                self._dataset.DeviceSpecificAcquisitionParameterSequence = pydicom.Sequence()
            self._dataset.DeviceSpecificAcquisitionParameterSequence.clear()
            self._dataset.DeviceSpecificAcquisitionParameterSequence.extend([item.to_dataset() for item in value])

    def add_DeviceSpecificAcquisitionParameter(self, item: DeviceSpecificAcquisitionParameterSequenceItem):
        if not isinstance(item, DeviceSpecificAcquisitionParameterSequenceItem):
            raise ValueError(f"Item must be an instance of DeviceSpecificAcquisitionParameterSequenceItem")
        self._DeviceSpecificAcquisitionParameterSequence.append(item)
        if "DeviceSpecificAcquisitionParameterSequence" not in self._dataset:
            self._dataset.DeviceSpecificAcquisitionParameterSequence = pydicom.Sequence()
        self._dataset.DeviceSpecificAcquisitionParameterSequence.append(item.to_dataset())

    @property
    def ReferencedDeviceIndex(self) -> Optional[int]:
        if "ReferencedDeviceIndex" in self._dataset:
            return self._dataset.ReferencedDeviceIndex
        return None

    @ReferencedDeviceIndex.setter
    def ReferencedDeviceIndex(self, value: Optional[int]):
        if value is None:
            if "ReferencedDeviceIndex" in self._dataset:
                del self._dataset.ReferencedDeviceIndex
        else:
            self._dataset.ReferencedDeviceIndex = value
