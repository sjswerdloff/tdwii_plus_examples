from typing import Any, List, Optional  # noqa

import pydicom

from .patient_support_position_device_parameter_sequence_item import (
    PatientSupportPositionDeviceParameterSequenceItem,
)


class PatientSupportPositionSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._PatientSupportPositionDeviceParameterSequence: List[PatientSupportPositionDeviceParameterSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

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
    def PatientSupportPositionDeviceParameterSequence(
        self,
    ) -> Optional[List[PatientSupportPositionDeviceParameterSequenceItem]]:
        if "PatientSupportPositionDeviceParameterSequence" in self._dataset:
            if len(self._PatientSupportPositionDeviceParameterSequence) == len(
                self._dataset.PatientSupportPositionDeviceParameterSequence
            ):
                return self._PatientSupportPositionDeviceParameterSequence
            else:
                return [
                    PatientSupportPositionDeviceParameterSequenceItem(x)
                    for x in self._dataset.PatientSupportPositionDeviceParameterSequence
                ]
        return None

    @PatientSupportPositionDeviceParameterSequence.setter
    def PatientSupportPositionDeviceParameterSequence(
        self, value: Optional[List[PatientSupportPositionDeviceParameterSequenceItem]]
    ):
        if value is None:
            self._PatientSupportPositionDeviceParameterSequence = []
            if "PatientSupportPositionDeviceParameterSequence" in self._dataset:
                del self._dataset.PatientSupportPositionDeviceParameterSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, PatientSupportPositionDeviceParameterSequenceItem) for item in value
        ):
            raise ValueError(
                "PatientSupportPositionDeviceParameterSequence must be a list of"
                " PatientSupportPositionDeviceParameterSequenceItem objects"
            )
        else:
            self._PatientSupportPositionDeviceParameterSequence = value
            if "PatientSupportPositionDeviceParameterSequence" not in self._dataset:
                self._dataset.PatientSupportPositionDeviceParameterSequence = pydicom.Sequence()
            self._dataset.PatientSupportPositionDeviceParameterSequence.clear()
            self._dataset.PatientSupportPositionDeviceParameterSequence.extend([item.to_dataset() for item in value])

    def add_PatientSupportPositionDeviceParameter(self, item: PatientSupportPositionDeviceParameterSequenceItem):
        if not isinstance(item, PatientSupportPositionDeviceParameterSequenceItem):
            raise ValueError("Item must be an instance of PatientSupportPositionDeviceParameterSequenceItem")
        self._PatientSupportPositionDeviceParameterSequence.append(item)
        if "PatientSupportPositionDeviceParameterSequence" not in self._dataset:
            self._dataset.PatientSupportPositionDeviceParameterSequence = pydicom.Sequence()
        self._dataset.PatientSupportPositionDeviceParameterSequence.append(item.to_dataset())
