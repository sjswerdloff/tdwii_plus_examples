from typing import Any, List, Optional  # noqa

import pydicom

from .patient_support_position_parameter_sequence_item import (
    PatientSupportPositionParameterSequenceItem,
)


class PatientSupportPositionDeviceParameterSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._PatientSupportPositionParameterSequence: List[PatientSupportPositionParameterSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

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

    @property
    def PatientSupportPositionParameterSequence(self) -> Optional[List[PatientSupportPositionParameterSequenceItem]]:
        if "PatientSupportPositionParameterSequence" in self._dataset:
            if len(self._PatientSupportPositionParameterSequence) == len(
                self._dataset.PatientSupportPositionParameterSequence
            ):
                return self._PatientSupportPositionParameterSequence
            else:
                return [
                    PatientSupportPositionParameterSequenceItem(x)
                    for x in self._dataset.PatientSupportPositionParameterSequence
                ]
        return None

    @PatientSupportPositionParameterSequence.setter
    def PatientSupportPositionParameterSequence(self, value: Optional[List[PatientSupportPositionParameterSequenceItem]]):
        if value is None:
            self._PatientSupportPositionParameterSequence = []
            if "PatientSupportPositionParameterSequence" in self._dataset:
                del self._dataset.PatientSupportPositionParameterSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, PatientSupportPositionParameterSequenceItem) for item in value
        ):
            raise ValueError(
                "PatientSupportPositionParameterSequence must be a list of PatientSupportPositionParameterSequenceItem objects"
            )
        else:
            self._PatientSupportPositionParameterSequence = value
            if "PatientSupportPositionParameterSequence" not in self._dataset:
                self._dataset.PatientSupportPositionParameterSequence = pydicom.Sequence()
            self._dataset.PatientSupportPositionParameterSequence.clear()
            self._dataset.PatientSupportPositionParameterSequence.extend([item.to_dataset() for item in value])

    def add_PatientSupportPositionParameter(self, item: PatientSupportPositionParameterSequenceItem):
        if not isinstance(item, PatientSupportPositionParameterSequenceItem):
            raise ValueError("Item must be an instance of PatientSupportPositionParameterSequenceItem")
        self._PatientSupportPositionParameterSequence.append(item)
        if "PatientSupportPositionParameterSequence" not in self._dataset:
            self._dataset.PatientSupportPositionParameterSequence = pydicom.Sequence()
        self._dataset.PatientSupportPositionParameterSequence.append(item.to_dataset())

    @property
    def DeviceOrderIndex(self) -> Optional[int]:
        if "DeviceOrderIndex" in self._dataset:
            return self._dataset.DeviceOrderIndex
        return None

    @DeviceOrderIndex.setter
    def DeviceOrderIndex(self, value: Optional[int]):
        if value is None:
            if "DeviceOrderIndex" in self._dataset:
                del self._dataset.DeviceOrderIndex
        else:
            self._dataset.DeviceOrderIndex = value
