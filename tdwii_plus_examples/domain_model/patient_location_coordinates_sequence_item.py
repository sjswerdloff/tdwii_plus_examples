from typing import Any, List, Optional

import pydicom

from .code_sequence_item import CodeSequenceItem


class PatientLocationCoordinatesSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._PatientLocationCoordinatesCodeSequence: List[CodeSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ThreeDPointCoordinates(self) -> Optional[List[float]]:
        if "ThreeDPointCoordinates" in self._dataset:
            return self._dataset.ThreeDPointCoordinates
        return None

    @ThreeDPointCoordinates.setter
    def ThreeDPointCoordinates(self, value: Optional[List[float]]):
        if value is None:
            if "ThreeDPointCoordinates" in self._dataset:
                del self._dataset.ThreeDPointCoordinates
        else:
            self._dataset.ThreeDPointCoordinates = value

    @property
    def PatientLocationCoordinatesCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "PatientLocationCoordinatesCodeSequence" in self._dataset:
            if len(self._PatientLocationCoordinatesCodeSequence) == len(self._dataset.PatientLocationCoordinatesCodeSequence):
                return self._PatientLocationCoordinatesCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.PatientLocationCoordinatesCodeSequence]
        return None

    @PatientLocationCoordinatesCodeSequence.setter
    def PatientLocationCoordinatesCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._PatientLocationCoordinatesCodeSequence = []
            if "PatientLocationCoordinatesCodeSequence" in self._dataset:
                del self._dataset.PatientLocationCoordinatesCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError(f"PatientLocationCoordinatesCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._PatientLocationCoordinatesCodeSequence = value
            if "PatientLocationCoordinatesCodeSequence" not in self._dataset:
                self._dataset.PatientLocationCoordinatesCodeSequence = pydicom.Sequence()
            self._dataset.PatientLocationCoordinatesCodeSequence.clear()
            self._dataset.PatientLocationCoordinatesCodeSequence.extend([item.to_dataset() for item in value])

    def add_PatientLocationCoordinatesCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError(f"Item must be an instance of CodeSequenceItem")
        self._PatientLocationCoordinatesCodeSequence.append(item)
        if "PatientLocationCoordinatesCodeSequence" not in self._dataset:
            self._dataset.PatientLocationCoordinatesCodeSequence = pydicom.Sequence()
        self._dataset.PatientLocationCoordinatesCodeSequence.append(item.to_dataset())
