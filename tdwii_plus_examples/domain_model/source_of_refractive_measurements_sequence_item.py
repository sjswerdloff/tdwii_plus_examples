from typing import Any, List, Optional  # noqa

import pydicom

from .code_sequence_item import CodeSequenceItem
from .referenced_sop_sequence_item import ReferencedSOPSequenceItem


class SourceOfRefractiveMeasurementsSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._ReferencedSOPSequence: List[ReferencedSOPSequenceItem] = []
        self._SourceOfRefractiveMeasurementsCodeSequence: List[CodeSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ReferencedSOPSequence(self) -> Optional[List[ReferencedSOPSequenceItem]]:
        if "ReferencedSOPSequence" in self._dataset:
            if len(self._ReferencedSOPSequence) == len(self._dataset.ReferencedSOPSequence):
                return self._ReferencedSOPSequence
            else:
                return [ReferencedSOPSequenceItem(x) for x in self._dataset.ReferencedSOPSequence]
        return None

    @ReferencedSOPSequence.setter
    def ReferencedSOPSequence(self, value: Optional[List[ReferencedSOPSequenceItem]]):
        if value is None:
            self._ReferencedSOPSequence = []
            if "ReferencedSOPSequence" in self._dataset:
                del self._dataset.ReferencedSOPSequence
        elif not isinstance(value, list) or not all(isinstance(item, ReferencedSOPSequenceItem) for item in value):
            raise ValueError("ReferencedSOPSequence must be a list of ReferencedSOPSequenceItem objects")
        else:
            self._ReferencedSOPSequence = value
            if "ReferencedSOPSequence" not in self._dataset:
                self._dataset.ReferencedSOPSequence = pydicom.Sequence()
            self._dataset.ReferencedSOPSequence.clear()
            self._dataset.ReferencedSOPSequence.extend([item.to_dataset() for item in value])

    def add_ReferencedSOP(self, item: ReferencedSOPSequenceItem):
        if not isinstance(item, ReferencedSOPSequenceItem):
            raise ValueError("Item must be an instance of ReferencedSOPSequenceItem")
        self._ReferencedSOPSequence.append(item)
        if "ReferencedSOPSequence" not in self._dataset:
            self._dataset.ReferencedSOPSequence = pydicom.Sequence()
        self._dataset.ReferencedSOPSequence.append(item.to_dataset())

    @property
    def SourceOfRefractiveMeasurementsCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "SourceOfRefractiveMeasurementsCodeSequence" in self._dataset:
            if len(self._SourceOfRefractiveMeasurementsCodeSequence) == len(
                self._dataset.SourceOfRefractiveMeasurementsCodeSequence
            ):
                return self._SourceOfRefractiveMeasurementsCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.SourceOfRefractiveMeasurementsCodeSequence]
        return None

    @SourceOfRefractiveMeasurementsCodeSequence.setter
    def SourceOfRefractiveMeasurementsCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._SourceOfRefractiveMeasurementsCodeSequence = []
            if "SourceOfRefractiveMeasurementsCodeSequence" in self._dataset:
                del self._dataset.SourceOfRefractiveMeasurementsCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("SourceOfRefractiveMeasurementsCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._SourceOfRefractiveMeasurementsCodeSequence = value
            if "SourceOfRefractiveMeasurementsCodeSequence" not in self._dataset:
                self._dataset.SourceOfRefractiveMeasurementsCodeSequence = pydicom.Sequence()
            self._dataset.SourceOfRefractiveMeasurementsCodeSequence.clear()
            self._dataset.SourceOfRefractiveMeasurementsCodeSequence.extend([item.to_dataset() for item in value])

    def add_SourceOfRefractiveMeasurementsCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._SourceOfRefractiveMeasurementsCodeSequence.append(item)
        if "SourceOfRefractiveMeasurementsCodeSequence" not in self._dataset:
            self._dataset.SourceOfRefractiveMeasurementsCodeSequence = pydicom.Sequence()
        self._dataset.SourceOfRefractiveMeasurementsCodeSequence.append(item.to_dataset())
