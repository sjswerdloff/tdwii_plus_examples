from typing import Any, List, Optional

import pydicom

from .attribute_tolerance_values_sequence_item import (
    AttributeToleranceValuesSequenceItem,
)
from .patient_support_position_device_tolerance_sequence_item import (
    PatientSupportPositionDeviceToleranceSequenceItem,
)


class RTToleranceSetSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._AttributeToleranceValuesSequence: List[AttributeToleranceValuesSequenceItem] = []
        self._PatientSupportPositionDeviceToleranceSequence: List[PatientSupportPositionDeviceToleranceSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def RTToleranceSetLabel(self) -> Optional[str]:
        if "RTToleranceSetLabel" in self._dataset:
            return self._dataset.RTToleranceSetLabel
        return None

    @RTToleranceSetLabel.setter
    def RTToleranceSetLabel(self, value: Optional[str]):
        if value is None:
            if "RTToleranceSetLabel" in self._dataset:
                del self._dataset.RTToleranceSetLabel
        else:
            self._dataset.RTToleranceSetLabel = value

    @property
    def AttributeToleranceValuesSequence(self) -> Optional[List[AttributeToleranceValuesSequenceItem]]:
        if "AttributeToleranceValuesSequence" in self._dataset:
            if len(self._AttributeToleranceValuesSequence) == len(self._dataset.AttributeToleranceValuesSequence):
                return self._AttributeToleranceValuesSequence
            else:
                return [AttributeToleranceValuesSequenceItem(x) for x in self._dataset.AttributeToleranceValuesSequence]
        return None

    @AttributeToleranceValuesSequence.setter
    def AttributeToleranceValuesSequence(self, value: Optional[List[AttributeToleranceValuesSequenceItem]]):
        if value is None:
            self._AttributeToleranceValuesSequence = []
            if "AttributeToleranceValuesSequence" in self._dataset:
                del self._dataset.AttributeToleranceValuesSequence
        elif not isinstance(value, list) or not all(isinstance(item, AttributeToleranceValuesSequenceItem) for item in value):
            raise ValueError(
                f"AttributeToleranceValuesSequence must be a list of AttributeToleranceValuesSequenceItem objects"
            )
        else:
            self._AttributeToleranceValuesSequence = value
            if "AttributeToleranceValuesSequence" not in self._dataset:
                self._dataset.AttributeToleranceValuesSequence = pydicom.Sequence()
            self._dataset.AttributeToleranceValuesSequence.clear()
            self._dataset.AttributeToleranceValuesSequence.extend([item.to_dataset() for item in value])

    def add_AttributeToleranceValues(self, item: AttributeToleranceValuesSequenceItem):
        if not isinstance(item, AttributeToleranceValuesSequenceItem):
            raise ValueError(f"Item must be an instance of AttributeToleranceValuesSequenceItem")
        self._AttributeToleranceValuesSequence.append(item)
        if "AttributeToleranceValuesSequence" not in self._dataset:
            self._dataset.AttributeToleranceValuesSequence = pydicom.Sequence()
        self._dataset.AttributeToleranceValuesSequence.append(item.to_dataset())

    @property
    def PatientSupportPositionSpecificationMethod(self) -> Optional[str]:
        if "PatientSupportPositionSpecificationMethod" in self._dataset:
            return self._dataset.PatientSupportPositionSpecificationMethod
        return None

    @PatientSupportPositionSpecificationMethod.setter
    def PatientSupportPositionSpecificationMethod(self, value: Optional[str]):
        if value is None:
            if "PatientSupportPositionSpecificationMethod" in self._dataset:
                del self._dataset.PatientSupportPositionSpecificationMethod
        else:
            self._dataset.PatientSupportPositionSpecificationMethod = value

    @property
    def PatientSupportPositionDeviceToleranceSequence(
        self,
    ) -> Optional[List[PatientSupportPositionDeviceToleranceSequenceItem]]:
        if "PatientSupportPositionDeviceToleranceSequence" in self._dataset:
            if len(self._PatientSupportPositionDeviceToleranceSequence) == len(
                self._dataset.PatientSupportPositionDeviceToleranceSequence
            ):
                return self._PatientSupportPositionDeviceToleranceSequence
            else:
                return [
                    PatientSupportPositionDeviceToleranceSequenceItem(x)
                    for x in self._dataset.PatientSupportPositionDeviceToleranceSequence
                ]
        return None

    @PatientSupportPositionDeviceToleranceSequence.setter
    def PatientSupportPositionDeviceToleranceSequence(
        self, value: Optional[List[PatientSupportPositionDeviceToleranceSequenceItem]]
    ):
        if value is None:
            self._PatientSupportPositionDeviceToleranceSequence = []
            if "PatientSupportPositionDeviceToleranceSequence" in self._dataset:
                del self._dataset.PatientSupportPositionDeviceToleranceSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, PatientSupportPositionDeviceToleranceSequenceItem) for item in value
        ):
            raise ValueError(
                f"PatientSupportPositionDeviceToleranceSequence must be a list of PatientSupportPositionDeviceToleranceSequenceItem objects"
            )
        else:
            self._PatientSupportPositionDeviceToleranceSequence = value
            if "PatientSupportPositionDeviceToleranceSequence" not in self._dataset:
                self._dataset.PatientSupportPositionDeviceToleranceSequence = pydicom.Sequence()
            self._dataset.PatientSupportPositionDeviceToleranceSequence.clear()
            self._dataset.PatientSupportPositionDeviceToleranceSequence.extend([item.to_dataset() for item in value])

    def add_PatientSupportPositionDeviceTolerance(self, item: PatientSupportPositionDeviceToleranceSequenceItem):
        if not isinstance(item, PatientSupportPositionDeviceToleranceSequenceItem):
            raise ValueError(f"Item must be an instance of PatientSupportPositionDeviceToleranceSequenceItem")
        self._PatientSupportPositionDeviceToleranceSequence.append(item)
        if "PatientSupportPositionDeviceToleranceSequence" not in self._dataset:
            self._dataset.PatientSupportPositionDeviceToleranceSequence = pydicom.Sequence()
        self._dataset.PatientSupportPositionDeviceToleranceSequence.append(item.to_dataset())
