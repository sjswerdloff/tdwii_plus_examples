from typing import Any, List, Optional

import pydicom

from .code_sequence_item import CodeSequenceItem


class PatientPhysiologicalStateSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._PatientPhysiologicalStateCodeSequence: List[CodeSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def PatientPhysiologicalStateCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "PatientPhysiologicalStateCodeSequence" in self._dataset:
            if len(self._PatientPhysiologicalStateCodeSequence) == len(self._dataset.PatientPhysiologicalStateCodeSequence):
                return self._PatientPhysiologicalStateCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.PatientPhysiologicalStateCodeSequence]
        return None

    @PatientPhysiologicalStateCodeSequence.setter
    def PatientPhysiologicalStateCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._PatientPhysiologicalStateCodeSequence = []
            if "PatientPhysiologicalStateCodeSequence" in self._dataset:
                del self._dataset.PatientPhysiologicalStateCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError(f"PatientPhysiologicalStateCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._PatientPhysiologicalStateCodeSequence = value
            if "PatientPhysiologicalStateCodeSequence" not in self._dataset:
                self._dataset.PatientPhysiologicalStateCodeSequence = pydicom.Sequence()
            self._dataset.PatientPhysiologicalStateCodeSequence.clear()
            self._dataset.PatientPhysiologicalStateCodeSequence.extend([item.to_dataset() for item in value])

    def add_PatientPhysiologicalStateCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError(f"Item must be an instance of CodeSequenceItem")
        self._PatientPhysiologicalStateCodeSequence.append(item)
        if "PatientPhysiologicalStateCodeSequence" not in self._dataset:
            self._dataset.PatientPhysiologicalStateCodeSequence = pydicom.Sequence()
        self._dataset.PatientPhysiologicalStateCodeSequence.append(item.to_dataset())
