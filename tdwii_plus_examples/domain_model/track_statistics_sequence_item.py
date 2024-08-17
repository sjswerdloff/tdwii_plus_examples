from typing import Any, List, Optional  # noqa

import pydicom

from .code_sequence_item import CodeSequenceItem


class TrackStatisticsSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._MeasurementUnitsCodeSequence: List[CodeSequenceItem] = []
        self._ConceptNameCodeSequence: List[CodeSequenceItem] = []
        self._ModifierCodeSequence: List[CodeSequenceItem] = []

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
    def ModifierCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "ModifierCodeSequence" in self._dataset:
            if len(self._ModifierCodeSequence) == len(self._dataset.ModifierCodeSequence):
                return self._ModifierCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.ModifierCodeSequence]
        return None

    @ModifierCodeSequence.setter
    def ModifierCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._ModifierCodeSequence = []
            if "ModifierCodeSequence" in self._dataset:
                del self._dataset.ModifierCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("ModifierCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._ModifierCodeSequence = value
            if "ModifierCodeSequence" not in self._dataset:
                self._dataset.ModifierCodeSequence = pydicom.Sequence()
            self._dataset.ModifierCodeSequence.clear()
            self._dataset.ModifierCodeSequence.extend([item.to_dataset() for item in value])

    def add_ModifierCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._ModifierCodeSequence.append(item)
        if "ModifierCodeSequence" not in self._dataset:
            self._dataset.ModifierCodeSequence = pydicom.Sequence()
        self._dataset.ModifierCodeSequence.append(item.to_dataset())

    @property
    def FloatingPointValues(self) -> Optional[bytes]:
        if "FloatingPointValues" in self._dataset:
            return self._dataset.FloatingPointValues
        return None

    @FloatingPointValues.setter
    def FloatingPointValues(self, value: Optional[bytes]):
        if value is None:
            if "FloatingPointValues" in self._dataset:
                del self._dataset.FloatingPointValues
        else:
            self._dataset.FloatingPointValues = value