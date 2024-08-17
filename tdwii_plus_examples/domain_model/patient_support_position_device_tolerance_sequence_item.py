from typing import Any, List, Optional

import pydicom

from .patient_support_position_tolerance_sequence_item import (
    PatientSupportPositionToleranceSequenceItem,
)


class PatientSupportPositionDeviceToleranceSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._PatientSupportPositionToleranceSequence: List[PatientSupportPositionToleranceSequenceItem] = []

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
    def PatientSupportPositionToleranceSequence(self) -> Optional[List[PatientSupportPositionToleranceSequenceItem]]:
        if "PatientSupportPositionToleranceSequence" in self._dataset:
            if len(self._PatientSupportPositionToleranceSequence) == len(
                self._dataset.PatientSupportPositionToleranceSequence
            ):
                return self._PatientSupportPositionToleranceSequence
            else:
                return [
                    PatientSupportPositionToleranceSequenceItem(x)
                    for x in self._dataset.PatientSupportPositionToleranceSequence
                ]
        return None

    @PatientSupportPositionToleranceSequence.setter
    def PatientSupportPositionToleranceSequence(self, value: Optional[List[PatientSupportPositionToleranceSequenceItem]]):
        if value is None:
            self._PatientSupportPositionToleranceSequence = []
            if "PatientSupportPositionToleranceSequence" in self._dataset:
                del self._dataset.PatientSupportPositionToleranceSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, PatientSupportPositionToleranceSequenceItem) for item in value
        ):
            raise ValueError(
                f"PatientSupportPositionToleranceSequence must be a list of PatientSupportPositionToleranceSequenceItem objects"
            )
        else:
            self._PatientSupportPositionToleranceSequence = value
            if "PatientSupportPositionToleranceSequence" not in self._dataset:
                self._dataset.PatientSupportPositionToleranceSequence = pydicom.Sequence()
            self._dataset.PatientSupportPositionToleranceSequence.clear()
            self._dataset.PatientSupportPositionToleranceSequence.extend([item.to_dataset() for item in value])

    def add_PatientSupportPositionTolerance(self, item: PatientSupportPositionToleranceSequenceItem):
        if not isinstance(item, PatientSupportPositionToleranceSequenceItem):
            raise ValueError(f"Item must be an instance of PatientSupportPositionToleranceSequenceItem")
        self._PatientSupportPositionToleranceSequence.append(item)
        if "PatientSupportPositionToleranceSequence" not in self._dataset:
            self._dataset.PatientSupportPositionToleranceSequence = pydicom.Sequence()
        self._dataset.PatientSupportPositionToleranceSequence.append(item.to_dataset())

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
