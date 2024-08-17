from typing import Any, List, Optional  # noqa

import pydicom

from .code_sequence_item import CodeSequenceItem
from .patient_treatment_preparation_device_sequence_item import (
    PatientTreatmentPreparationDeviceSequenceItem,
)
from .patient_treatment_preparation_procedure_parameter_sequence_item import (
    PatientTreatmentPreparationProcedureParameterSequenceItem,
)


class PatientTreatmentPreparationProcedureSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._PatientTreatmentPreparationDeviceSequence: List[PatientTreatmentPreparationDeviceSequenceItem] = []
        self._PatientTreatmentPreparationProcedureCodeSequence: List[CodeSequenceItem] = []
        self._PatientTreatmentPreparationProcedureParameterSequence: List[
            PatientTreatmentPreparationProcedureParameterSequenceItem
        ] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def PatientTreatmentPreparationProcedureParameterDescription(self) -> Optional[str]:
        if "PatientTreatmentPreparationProcedureParameterDescription" in self._dataset:
            return self._dataset.PatientTreatmentPreparationProcedureParameterDescription
        return None

    @PatientTreatmentPreparationProcedureParameterDescription.setter
    def PatientTreatmentPreparationProcedureParameterDescription(self, value: Optional[str]):
        if value is None:
            if "PatientTreatmentPreparationProcedureParameterDescription" in self._dataset:
                del self._dataset.PatientTreatmentPreparationProcedureParameterDescription
        else:
            self._dataset.PatientTreatmentPreparationProcedureParameterDescription = value

    @property
    def PatientTreatmentPreparationDeviceSequence(self) -> Optional[List[PatientTreatmentPreparationDeviceSequenceItem]]:
        if "PatientTreatmentPreparationDeviceSequence" in self._dataset:
            if len(self._PatientTreatmentPreparationDeviceSequence) == len(
                self._dataset.PatientTreatmentPreparationDeviceSequence
            ):
                return self._PatientTreatmentPreparationDeviceSequence
            else:
                return [
                    PatientTreatmentPreparationDeviceSequenceItem(x)
                    for x in self._dataset.PatientTreatmentPreparationDeviceSequence
                ]
        return None

    @PatientTreatmentPreparationDeviceSequence.setter
    def PatientTreatmentPreparationDeviceSequence(self, value: Optional[List[PatientTreatmentPreparationDeviceSequenceItem]]):
        if value is None:
            self._PatientTreatmentPreparationDeviceSequence = []
            if "PatientTreatmentPreparationDeviceSequence" in self._dataset:
                del self._dataset.PatientTreatmentPreparationDeviceSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, PatientTreatmentPreparationDeviceSequenceItem) for item in value
        ):
            raise ValueError(
                "PatientTreatmentPreparationDeviceSequence must be a list of PatientTreatmentPreparationDeviceSequenceItem"
                " objects"
            )
        else:
            self._PatientTreatmentPreparationDeviceSequence = value
            if "PatientTreatmentPreparationDeviceSequence" not in self._dataset:
                self._dataset.PatientTreatmentPreparationDeviceSequence = pydicom.Sequence()
            self._dataset.PatientTreatmentPreparationDeviceSequence.clear()
            self._dataset.PatientTreatmentPreparationDeviceSequence.extend([item.to_dataset() for item in value])

    def add_PatientTreatmentPreparationDevice(self, item: PatientTreatmentPreparationDeviceSequenceItem):
        if not isinstance(item, PatientTreatmentPreparationDeviceSequenceItem):
            raise ValueError("Item must be an instance of PatientTreatmentPreparationDeviceSequenceItem")
        self._PatientTreatmentPreparationDeviceSequence.append(item)
        if "PatientTreatmentPreparationDeviceSequence" not in self._dataset:
            self._dataset.PatientTreatmentPreparationDeviceSequence = pydicom.Sequence()
        self._dataset.PatientTreatmentPreparationDeviceSequence.append(item.to_dataset())

    @property
    def PatientTreatmentPreparationProcedureCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "PatientTreatmentPreparationProcedureCodeSequence" in self._dataset:
            if len(self._PatientTreatmentPreparationProcedureCodeSequence) == len(
                self._dataset.PatientTreatmentPreparationProcedureCodeSequence
            ):
                return self._PatientTreatmentPreparationProcedureCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.PatientTreatmentPreparationProcedureCodeSequence]
        return None

    @PatientTreatmentPreparationProcedureCodeSequence.setter
    def PatientTreatmentPreparationProcedureCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._PatientTreatmentPreparationProcedureCodeSequence = []
            if "PatientTreatmentPreparationProcedureCodeSequence" in self._dataset:
                del self._dataset.PatientTreatmentPreparationProcedureCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("PatientTreatmentPreparationProcedureCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._PatientTreatmentPreparationProcedureCodeSequence = value
            if "PatientTreatmentPreparationProcedureCodeSequence" not in self._dataset:
                self._dataset.PatientTreatmentPreparationProcedureCodeSequence = pydicom.Sequence()
            self._dataset.PatientTreatmentPreparationProcedureCodeSequence.clear()
            self._dataset.PatientTreatmentPreparationProcedureCodeSequence.extend([item.to_dataset() for item in value])

    def add_PatientTreatmentPreparationProcedureCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._PatientTreatmentPreparationProcedureCodeSequence.append(item)
        if "PatientTreatmentPreparationProcedureCodeSequence" not in self._dataset:
            self._dataset.PatientTreatmentPreparationProcedureCodeSequence = pydicom.Sequence()
        self._dataset.PatientTreatmentPreparationProcedureCodeSequence.append(item.to_dataset())

    @property
    def PatientTreatmentPreparationProcedureParameterSequence(
        self,
    ) -> Optional[List[PatientTreatmentPreparationProcedureParameterSequenceItem]]:
        if "PatientTreatmentPreparationProcedureParameterSequence" in self._dataset:
            if len(self._PatientTreatmentPreparationProcedureParameterSequence) == len(
                self._dataset.PatientTreatmentPreparationProcedureParameterSequence
            ):
                return self._PatientTreatmentPreparationProcedureParameterSequence
            else:
                return [
                    PatientTreatmentPreparationProcedureParameterSequenceItem(x)
                    for x in self._dataset.PatientTreatmentPreparationProcedureParameterSequence
                ]
        return None

    @PatientTreatmentPreparationProcedureParameterSequence.setter
    def PatientTreatmentPreparationProcedureParameterSequence(
        self, value: Optional[List[PatientTreatmentPreparationProcedureParameterSequenceItem]]
    ):
        if value is None:
            self._PatientTreatmentPreparationProcedureParameterSequence = []
            if "PatientTreatmentPreparationProcedureParameterSequence" in self._dataset:
                del self._dataset.PatientTreatmentPreparationProcedureParameterSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, PatientTreatmentPreparationProcedureParameterSequenceItem) for item in value
        ):
            raise ValueError(
                "PatientTreatmentPreparationProcedureParameterSequence must be a list of"
                " PatientTreatmentPreparationProcedureParameterSequenceItem objects"
            )
        else:
            self._PatientTreatmentPreparationProcedureParameterSequence = value
            if "PatientTreatmentPreparationProcedureParameterSequence" not in self._dataset:
                self._dataset.PatientTreatmentPreparationProcedureParameterSequence = pydicom.Sequence()
            self._dataset.PatientTreatmentPreparationProcedureParameterSequence.clear()
            self._dataset.PatientTreatmentPreparationProcedureParameterSequence.extend([item.to_dataset() for item in value])

    def add_PatientTreatmentPreparationProcedureParameter(
        self, item: PatientTreatmentPreparationProcedureParameterSequenceItem
    ):
        if not isinstance(item, PatientTreatmentPreparationProcedureParameterSequenceItem):
            raise ValueError("Item must be an instance of PatientTreatmentPreparationProcedureParameterSequenceItem")
        self._PatientTreatmentPreparationProcedureParameterSequence.append(item)
        if "PatientTreatmentPreparationProcedureParameterSequence" not in self._dataset:
            self._dataset.PatientTreatmentPreparationProcedureParameterSequence = pydicom.Sequence()
        self._dataset.PatientTreatmentPreparationProcedureParameterSequence.append(item.to_dataset())

    @property
    def PatientTreatmentPreparationProcedureIndex(self) -> Optional[int]:
        if "PatientTreatmentPreparationProcedureIndex" in self._dataset:
            return self._dataset.PatientTreatmentPreparationProcedureIndex
        return None

    @PatientTreatmentPreparationProcedureIndex.setter
    def PatientTreatmentPreparationProcedureIndex(self, value: Optional[int]):
        if value is None:
            if "PatientTreatmentPreparationProcedureIndex" in self._dataset:
                del self._dataset.PatientTreatmentPreparationProcedureIndex
        else:
            self._dataset.PatientTreatmentPreparationProcedureIndex = value
