from typing import Any, List, Optional  # noqa

import pydicom

from .code_sequence_item import CodeSequenceItem
from .measurement_values_sequence_item import MeasurementValuesSequenceItem


class MeasurementsSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._MeasurementUnitsCodeSequence: List[CodeSequenceItem] = []
        self._ConceptNameCodeSequence: List[CodeSequenceItem] = []
        self._MeasurementValuesSequence: List[MeasurementValuesSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def MeasurementUnitsCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "MeasurementUnitsCodeSequence" in self._dataset:
            if len(self._MeasurementUnitsCodeSequence) == len(self._dataset.MeasurementUnitsCodeSequence):
                return self._MeasurementUnitsCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.MeasurementUnitsCodeSequence]
        return None

    @MeasurementUnitsCodeSequence.setter
    def MeasurementUnitsCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._MeasurementUnitsCodeSequence = []
            if "MeasurementUnitsCodeSequence" in self._dataset:
                del self._dataset.MeasurementUnitsCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("MeasurementUnitsCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._MeasurementUnitsCodeSequence = value
            if "MeasurementUnitsCodeSequence" not in self._dataset:
                self._dataset.MeasurementUnitsCodeSequence = pydicom.Sequence()
            self._dataset.MeasurementUnitsCodeSequence.clear()
            self._dataset.MeasurementUnitsCodeSequence.extend([item.to_dataset() for item in value])

    def add_MeasurementUnitsCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._MeasurementUnitsCodeSequence.append(item)
        if "MeasurementUnitsCodeSequence" not in self._dataset:
            self._dataset.MeasurementUnitsCodeSequence = pydicom.Sequence()
        self._dataset.MeasurementUnitsCodeSequence.append(item.to_dataset())

    @property
    def ConceptNameCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "ConceptNameCodeSequence" in self._dataset:
            if len(self._ConceptNameCodeSequence) == len(self._dataset.ConceptNameCodeSequence):
                return self._ConceptNameCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.ConceptNameCodeSequence]
        return None

    @ConceptNameCodeSequence.setter
    def ConceptNameCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._ConceptNameCodeSequence = []
            if "ConceptNameCodeSequence" in self._dataset:
                del self._dataset.ConceptNameCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("ConceptNameCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._ConceptNameCodeSequence = value
            if "ConceptNameCodeSequence" not in self._dataset:
                self._dataset.ConceptNameCodeSequence = pydicom.Sequence()
            self._dataset.ConceptNameCodeSequence.clear()
            self._dataset.ConceptNameCodeSequence.extend([item.to_dataset() for item in value])

    def add_ConceptNameCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._ConceptNameCodeSequence.append(item)
        if "ConceptNameCodeSequence" not in self._dataset:
            self._dataset.ConceptNameCodeSequence = pydicom.Sequence()
        self._dataset.ConceptNameCodeSequence.append(item.to_dataset())

    @property
    def MeasurementValuesSequence(self) -> Optional[List[MeasurementValuesSequenceItem]]:
        if "MeasurementValuesSequence" in self._dataset:
            if len(self._MeasurementValuesSequence) == len(self._dataset.MeasurementValuesSequence):
                return self._MeasurementValuesSequence
            else:
                return [MeasurementValuesSequenceItem(x) for x in self._dataset.MeasurementValuesSequence]
        return None

    @MeasurementValuesSequence.setter
    def MeasurementValuesSequence(self, value: Optional[List[MeasurementValuesSequenceItem]]):
        if value is None:
            self._MeasurementValuesSequence = []
            if "MeasurementValuesSequence" in self._dataset:
                del self._dataset.MeasurementValuesSequence
        elif not isinstance(value, list) or not all(isinstance(item, MeasurementValuesSequenceItem) for item in value):
            raise ValueError("MeasurementValuesSequence must be a list of MeasurementValuesSequenceItem objects")
        else:
            self._MeasurementValuesSequence = value
            if "MeasurementValuesSequence" not in self._dataset:
                self._dataset.MeasurementValuesSequence = pydicom.Sequence()
            self._dataset.MeasurementValuesSequence.clear()
            self._dataset.MeasurementValuesSequence.extend([item.to_dataset() for item in value])

    def add_MeasurementValues(self, item: MeasurementValuesSequenceItem):
        if not isinstance(item, MeasurementValuesSequenceItem):
            raise ValueError("Item must be an instance of MeasurementValuesSequenceItem")
        self._MeasurementValuesSequence.append(item)
        if "MeasurementValuesSequence" not in self._dataset:
            self._dataset.MeasurementValuesSequence = pydicom.Sequence()
        self._dataset.MeasurementValuesSequence.append(item.to_dataset())
