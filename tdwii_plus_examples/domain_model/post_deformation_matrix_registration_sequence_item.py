from decimal import Decimal
from typing import Any, List, Optional

import pydicom


class PostDeformationMatrixRegistrationSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def FrameOfReferenceTransformationMatrixType(self) -> Optional[str]:
        if "FrameOfReferenceTransformationMatrixType" in self._dataset:
            return self._dataset.FrameOfReferenceTransformationMatrixType
        return None

    @FrameOfReferenceTransformationMatrixType.setter
    def FrameOfReferenceTransformationMatrixType(self, value: Optional[str]):
        if value is None:
            if "FrameOfReferenceTransformationMatrixType" in self._dataset:
                del self._dataset.FrameOfReferenceTransformationMatrixType
        else:
            self._dataset.FrameOfReferenceTransformationMatrixType = value

    @property
    def FrameOfReferenceTransformationMatrix(self) -> Optional[List[Decimal]]:
        if "FrameOfReferenceTransformationMatrix" in self._dataset:
            return self._dataset.FrameOfReferenceTransformationMatrix
        return None

    @FrameOfReferenceTransformationMatrix.setter
    def FrameOfReferenceTransformationMatrix(self, value: Optional[List[Decimal]]):
        if value is None:
            if "FrameOfReferenceTransformationMatrix" in self._dataset:
                del self._dataset.FrameOfReferenceTransformationMatrix
        else:
            self._dataset.FrameOfReferenceTransformationMatrix = value
