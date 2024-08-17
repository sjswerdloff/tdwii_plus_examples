from typing import Any, List, Optional

import pydicom

from .code_sequence_item import CodeSequenceItem
from .rt_patient_position_displacement_sequence_item import (
    RTPatientPositionDisplacementSequenceItem,
)
from .rt_patient_position_sequence_item import RTPatientPositionSequenceItem


class RTDeliveryStartPatientPositionSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._PatientOrientationCodeSequence: List[CodeSequenceItem] = []
        self._RTPatientPositionDisplacementSequence: List[RTPatientPositionDisplacementSequenceItem] = []
        self._RTPatientPositionSequence: List[RTPatientPositionSequenceItem] = []
        self._PatientEquipmentRelationshipCodeSequence: List[CodeSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def PatientOrientationCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "PatientOrientationCodeSequence" in self._dataset:
            if len(self._PatientOrientationCodeSequence) == len(self._dataset.PatientOrientationCodeSequence):
                return self._PatientOrientationCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.PatientOrientationCodeSequence]
        return None

    @PatientOrientationCodeSequence.setter
    def PatientOrientationCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._PatientOrientationCodeSequence = []
            if "PatientOrientationCodeSequence" in self._dataset:
                del self._dataset.PatientOrientationCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError(f"PatientOrientationCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._PatientOrientationCodeSequence = value
            if "PatientOrientationCodeSequence" not in self._dataset:
                self._dataset.PatientOrientationCodeSequence = pydicom.Sequence()
            self._dataset.PatientOrientationCodeSequence.clear()
            self._dataset.PatientOrientationCodeSequence.extend([item.to_dataset() for item in value])

    def add_PatientOrientationCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError(f"Item must be an instance of CodeSequenceItem")
        self._PatientOrientationCodeSequence.append(item)
        if "PatientOrientationCodeSequence" not in self._dataset:
            self._dataset.PatientOrientationCodeSequence = pydicom.Sequence()
        self._dataset.PatientOrientationCodeSequence.append(item.to_dataset())

    @property
    def RTPatientPositionDisplacementSequence(self) -> Optional[List[RTPatientPositionDisplacementSequenceItem]]:
        if "RTPatientPositionDisplacementSequence" in self._dataset:
            if len(self._RTPatientPositionDisplacementSequence) == len(self._dataset.RTPatientPositionDisplacementSequence):
                return self._RTPatientPositionDisplacementSequence
            else:
                return [
                    RTPatientPositionDisplacementSequenceItem(x) for x in self._dataset.RTPatientPositionDisplacementSequence
                ]
        return None

    @RTPatientPositionDisplacementSequence.setter
    def RTPatientPositionDisplacementSequence(self, value: Optional[List[RTPatientPositionDisplacementSequenceItem]]):
        if value is None:
            self._RTPatientPositionDisplacementSequence = []
            if "RTPatientPositionDisplacementSequence" in self._dataset:
                del self._dataset.RTPatientPositionDisplacementSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, RTPatientPositionDisplacementSequenceItem) for item in value
        ):
            raise ValueError(
                f"RTPatientPositionDisplacementSequence must be a list of RTPatientPositionDisplacementSequenceItem objects"
            )
        else:
            self._RTPatientPositionDisplacementSequence = value
            if "RTPatientPositionDisplacementSequence" not in self._dataset:
                self._dataset.RTPatientPositionDisplacementSequence = pydicom.Sequence()
            self._dataset.RTPatientPositionDisplacementSequence.clear()
            self._dataset.RTPatientPositionDisplacementSequence.extend([item.to_dataset() for item in value])

    def add_RTPatientPositionDisplacement(self, item: RTPatientPositionDisplacementSequenceItem):
        if not isinstance(item, RTPatientPositionDisplacementSequenceItem):
            raise ValueError(f"Item must be an instance of RTPatientPositionDisplacementSequenceItem")
        self._RTPatientPositionDisplacementSequence.append(item)
        if "RTPatientPositionDisplacementSequence" not in self._dataset:
            self._dataset.RTPatientPositionDisplacementSequence = pydicom.Sequence()
        self._dataset.RTPatientPositionDisplacementSequence.append(item.to_dataset())

    @property
    def RTPatientPositionSequence(self) -> Optional[List[RTPatientPositionSequenceItem]]:
        if "RTPatientPositionSequence" in self._dataset:
            if len(self._RTPatientPositionSequence) == len(self._dataset.RTPatientPositionSequence):
                return self._RTPatientPositionSequence
            else:
                return [RTPatientPositionSequenceItem(x) for x in self._dataset.RTPatientPositionSequence]
        return None

    @RTPatientPositionSequence.setter
    def RTPatientPositionSequence(self, value: Optional[List[RTPatientPositionSequenceItem]]):
        if value is None:
            self._RTPatientPositionSequence = []
            if "RTPatientPositionSequence" in self._dataset:
                del self._dataset.RTPatientPositionSequence
        elif not isinstance(value, list) or not all(isinstance(item, RTPatientPositionSequenceItem) for item in value):
            raise ValueError(f"RTPatientPositionSequence must be a list of RTPatientPositionSequenceItem objects")
        else:
            self._RTPatientPositionSequence = value
            if "RTPatientPositionSequence" not in self._dataset:
                self._dataset.RTPatientPositionSequence = pydicom.Sequence()
            self._dataset.RTPatientPositionSequence.clear()
            self._dataset.RTPatientPositionSequence.extend([item.to_dataset() for item in value])

    def add_RTPatientPosition(self, item: RTPatientPositionSequenceItem):
        if not isinstance(item, RTPatientPositionSequenceItem):
            raise ValueError(f"Item must be an instance of RTPatientPositionSequenceItem")
        self._RTPatientPositionSequence.append(item)
        if "RTPatientPositionSequence" not in self._dataset:
            self._dataset.RTPatientPositionSequence = pydicom.Sequence()
        self._dataset.RTPatientPositionSequence.append(item.to_dataset())

    @property
    def PatientEquipmentRelationshipCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "PatientEquipmentRelationshipCodeSequence" in self._dataset:
            if len(self._PatientEquipmentRelationshipCodeSequence) == len(
                self._dataset.PatientEquipmentRelationshipCodeSequence
            ):
                return self._PatientEquipmentRelationshipCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.PatientEquipmentRelationshipCodeSequence]
        return None

    @PatientEquipmentRelationshipCodeSequence.setter
    def PatientEquipmentRelationshipCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._PatientEquipmentRelationshipCodeSequence = []
            if "PatientEquipmentRelationshipCodeSequence" in self._dataset:
                del self._dataset.PatientEquipmentRelationshipCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError(f"PatientEquipmentRelationshipCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._PatientEquipmentRelationshipCodeSequence = value
            if "PatientEquipmentRelationshipCodeSequence" not in self._dataset:
                self._dataset.PatientEquipmentRelationshipCodeSequence = pydicom.Sequence()
            self._dataset.PatientEquipmentRelationshipCodeSequence.clear()
            self._dataset.PatientEquipmentRelationshipCodeSequence.extend([item.to_dataset() for item in value])

    def add_PatientEquipmentRelationshipCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError(f"Item must be an instance of CodeSequenceItem")
        self._PatientEquipmentRelationshipCodeSequence.append(item)
        if "PatientEquipmentRelationshipCodeSequence" not in self._dataset:
            self._dataset.PatientEquipmentRelationshipCodeSequence = pydicom.Sequence()
        self._dataset.PatientEquipmentRelationshipCodeSequence.append(item.to_dataset())
