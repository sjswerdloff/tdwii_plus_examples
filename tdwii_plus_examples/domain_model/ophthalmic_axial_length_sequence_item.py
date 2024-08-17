from typing import Any, List, Optional

import pydicom

from .code_sequence_item import CodeSequenceItem
from .referenced_sop_sequence_item import ReferencedSOPSequenceItem


class OphthalmicAxialLengthSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._ReferencedSOPSequence: List[ReferencedSOPSequenceItem] = []
        self._SourceOfOphthalmicAxialLengthCodeSequence: List[CodeSequenceItem] = []
        self._OphthalmicUltrasoundMethodCodeSequence: List[CodeSequenceItem] = []
        self._OphthalmicAxialLengthSelectionMethodCodeSequence: List[CodeSequenceItem] = []

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
            raise ValueError(f"ReferencedSOPSequence must be a list of ReferencedSOPSequenceItem objects")
        else:
            self._ReferencedSOPSequence = value
            if "ReferencedSOPSequence" not in self._dataset:
                self._dataset.ReferencedSOPSequence = pydicom.Sequence()
            self._dataset.ReferencedSOPSequence.clear()
            self._dataset.ReferencedSOPSequence.extend([item.to_dataset() for item in value])

    def add_ReferencedSOP(self, item: ReferencedSOPSequenceItem):
        if not isinstance(item, ReferencedSOPSequenceItem):
            raise ValueError(f"Item must be an instance of ReferencedSOPSequenceItem")
        self._ReferencedSOPSequence.append(item)
        if "ReferencedSOPSequence" not in self._dataset:
            self._dataset.ReferencedSOPSequence = pydicom.Sequence()
        self._dataset.ReferencedSOPSequence.append(item.to_dataset())

    @property
    def OphthalmicAxialLength(self) -> Optional[float]:
        if "OphthalmicAxialLength" in self._dataset:
            return self._dataset.OphthalmicAxialLength
        return None

    @OphthalmicAxialLength.setter
    def OphthalmicAxialLength(self, value: Optional[float]):
        if value is None:
            if "OphthalmicAxialLength" in self._dataset:
                del self._dataset.OphthalmicAxialLength
        else:
            self._dataset.OphthalmicAxialLength = value

    @property
    def SourceOfOphthalmicAxialLengthCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "SourceOfOphthalmicAxialLengthCodeSequence" in self._dataset:
            if len(self._SourceOfOphthalmicAxialLengthCodeSequence) == len(
                self._dataset.SourceOfOphthalmicAxialLengthCodeSequence
            ):
                return self._SourceOfOphthalmicAxialLengthCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.SourceOfOphthalmicAxialLengthCodeSequence]
        return None

    @SourceOfOphthalmicAxialLengthCodeSequence.setter
    def SourceOfOphthalmicAxialLengthCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._SourceOfOphthalmicAxialLengthCodeSequence = []
            if "SourceOfOphthalmicAxialLengthCodeSequence" in self._dataset:
                del self._dataset.SourceOfOphthalmicAxialLengthCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError(f"SourceOfOphthalmicAxialLengthCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._SourceOfOphthalmicAxialLengthCodeSequence = value
            if "SourceOfOphthalmicAxialLengthCodeSequence" not in self._dataset:
                self._dataset.SourceOfOphthalmicAxialLengthCodeSequence = pydicom.Sequence()
            self._dataset.SourceOfOphthalmicAxialLengthCodeSequence.clear()
            self._dataset.SourceOfOphthalmicAxialLengthCodeSequence.extend([item.to_dataset() for item in value])

    def add_SourceOfOphthalmicAxialLengthCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError(f"Item must be an instance of CodeSequenceItem")
        self._SourceOfOphthalmicAxialLengthCodeSequence.append(item)
        if "SourceOfOphthalmicAxialLengthCodeSequence" not in self._dataset:
            self._dataset.SourceOfOphthalmicAxialLengthCodeSequence = pydicom.Sequence()
        self._dataset.SourceOfOphthalmicAxialLengthCodeSequence.append(item.to_dataset())

    @property
    def OphthalmicUltrasoundMethodCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "OphthalmicUltrasoundMethodCodeSequence" in self._dataset:
            if len(self._OphthalmicUltrasoundMethodCodeSequence) == len(self._dataset.OphthalmicUltrasoundMethodCodeSequence):
                return self._OphthalmicUltrasoundMethodCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.OphthalmicUltrasoundMethodCodeSequence]
        return None

    @OphthalmicUltrasoundMethodCodeSequence.setter
    def OphthalmicUltrasoundMethodCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._OphthalmicUltrasoundMethodCodeSequence = []
            if "OphthalmicUltrasoundMethodCodeSequence" in self._dataset:
                del self._dataset.OphthalmicUltrasoundMethodCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError(f"OphthalmicUltrasoundMethodCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._OphthalmicUltrasoundMethodCodeSequence = value
            if "OphthalmicUltrasoundMethodCodeSequence" not in self._dataset:
                self._dataset.OphthalmicUltrasoundMethodCodeSequence = pydicom.Sequence()
            self._dataset.OphthalmicUltrasoundMethodCodeSequence.clear()
            self._dataset.OphthalmicUltrasoundMethodCodeSequence.extend([item.to_dataset() for item in value])

    def add_OphthalmicUltrasoundMethodCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError(f"Item must be an instance of CodeSequenceItem")
        self._OphthalmicUltrasoundMethodCodeSequence.append(item)
        if "OphthalmicUltrasoundMethodCodeSequence" not in self._dataset:
            self._dataset.OphthalmicUltrasoundMethodCodeSequence = pydicom.Sequence()
        self._dataset.OphthalmicUltrasoundMethodCodeSequence.append(item.to_dataset())

    @property
    def OphthalmicAxialLengthSelectionMethodCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "OphthalmicAxialLengthSelectionMethodCodeSequence" in self._dataset:
            if len(self._OphthalmicAxialLengthSelectionMethodCodeSequence) == len(
                self._dataset.OphthalmicAxialLengthSelectionMethodCodeSequence
            ):
                return self._OphthalmicAxialLengthSelectionMethodCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.OphthalmicAxialLengthSelectionMethodCodeSequence]
        return None

    @OphthalmicAxialLengthSelectionMethodCodeSequence.setter
    def OphthalmicAxialLengthSelectionMethodCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._OphthalmicAxialLengthSelectionMethodCodeSequence = []
            if "OphthalmicAxialLengthSelectionMethodCodeSequence" in self._dataset:
                del self._dataset.OphthalmicAxialLengthSelectionMethodCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError(f"OphthalmicAxialLengthSelectionMethodCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._OphthalmicAxialLengthSelectionMethodCodeSequence = value
            if "OphthalmicAxialLengthSelectionMethodCodeSequence" not in self._dataset:
                self._dataset.OphthalmicAxialLengthSelectionMethodCodeSequence = pydicom.Sequence()
            self._dataset.OphthalmicAxialLengthSelectionMethodCodeSequence.clear()
            self._dataset.OphthalmicAxialLengthSelectionMethodCodeSequence.extend([item.to_dataset() for item in value])

    def add_OphthalmicAxialLengthSelectionMethodCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError(f"Item must be an instance of CodeSequenceItem")
        self._OphthalmicAxialLengthSelectionMethodCodeSequence.append(item)
        if "OphthalmicAxialLengthSelectionMethodCodeSequence" not in self._dataset:
            self._dataset.OphthalmicAxialLengthSelectionMethodCodeSequence = pydicom.Sequence()
        self._dataset.OphthalmicAxialLengthSelectionMethodCodeSequence.append(item.to_dataset())
