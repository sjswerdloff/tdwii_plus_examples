from typing import Any, List, Optional  # noqa

import pydicom

from .code_sequence_item import CodeSequenceItem
from .matrix_sequence_item import MatrixSequenceItem


class MatrixRegistrationSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._MatrixSequence: List[MatrixSequenceItem] = []
        self._RegistrationTypeCodeSequence: List[CodeSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def MatrixSequence(self) -> Optional[List[MatrixSequenceItem]]:
        if "MatrixSequence" in self._dataset:
            if len(self._MatrixSequence) == len(self._dataset.MatrixSequence):
                return self._MatrixSequence
            else:
                return [MatrixSequenceItem(x) for x in self._dataset.MatrixSequence]
        return None

    @MatrixSequence.setter
    def MatrixSequence(self, value: Optional[List[MatrixSequenceItem]]):
        if value is None:
            self._MatrixSequence = []
            if "MatrixSequence" in self._dataset:
                del self._dataset.MatrixSequence
        elif not isinstance(value, list) or not all(isinstance(item, MatrixSequenceItem) for item in value):
            raise ValueError("MatrixSequence must be a list of MatrixSequenceItem objects")
        else:
            self._MatrixSequence = value
            if "MatrixSequence" not in self._dataset:
                self._dataset.MatrixSequence = pydicom.Sequence()
            self._dataset.MatrixSequence.clear()
            self._dataset.MatrixSequence.extend([item.to_dataset() for item in value])

    def add_Matrix(self, item: MatrixSequenceItem):
        if not isinstance(item, MatrixSequenceItem):
            raise ValueError("Item must be an instance of MatrixSequenceItem")
        self._MatrixSequence.append(item)
        if "MatrixSequence" not in self._dataset:
            self._dataset.MatrixSequence = pydicom.Sequence()
        self._dataset.MatrixSequence.append(item.to_dataset())

    @property
    def RegistrationTypeCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "RegistrationTypeCodeSequence" in self._dataset:
            if len(self._RegistrationTypeCodeSequence) == len(self._dataset.RegistrationTypeCodeSequence):
                return self._RegistrationTypeCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.RegistrationTypeCodeSequence]
        return None

    @RegistrationTypeCodeSequence.setter
    def RegistrationTypeCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._RegistrationTypeCodeSequence = []
            if "RegistrationTypeCodeSequence" in self._dataset:
                del self._dataset.RegistrationTypeCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("RegistrationTypeCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._RegistrationTypeCodeSequence = value
            if "RegistrationTypeCodeSequence" not in self._dataset:
                self._dataset.RegistrationTypeCodeSequence = pydicom.Sequence()
            self._dataset.RegistrationTypeCodeSequence.clear()
            self._dataset.RegistrationTypeCodeSequence.extend([item.to_dataset() for item in value])

    def add_RegistrationTypeCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._RegistrationTypeCodeSequence.append(item)
        if "RegistrationTypeCodeSequence" not in self._dataset:
            self._dataset.RegistrationTypeCodeSequence = pydicom.Sequence()
        self._dataset.RegistrationTypeCodeSequence.append(item.to_dataset())

    @property
    def FrameOfReferenceTransformationComment(self) -> Optional[str]:
        if "FrameOfReferenceTransformationComment" in self._dataset:
            return self._dataset.FrameOfReferenceTransformationComment
        return None

    @FrameOfReferenceTransformationComment.setter
    def FrameOfReferenceTransformationComment(self, value: Optional[str]):
        if value is None:
            if "FrameOfReferenceTransformationComment" in self._dataset:
                del self._dataset.FrameOfReferenceTransformationComment
        else:
            self._dataset.FrameOfReferenceTransformationComment = value
