from typing import Any, List, Optional

import pydicom

from .code_sequence_item import CodeSequenceItem


class PatientTreatmentOrientationSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._PatientOrientationCodeSequence: List[CodeSequenceItem] = []
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
