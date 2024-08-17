from typing import Any, List, Optional

import pydicom

from .diffusion_b_matrix_sequence_item import DiffusionBMatrixSequenceItem
from .diffusion_gradient_direction_sequence_item import (
    DiffusionGradientDirectionSequenceItem,
)


class MRDiffusionSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._DiffusionGradientDirectionSequence: List[DiffusionGradientDirectionSequenceItem] = []
        self._DiffusionBMatrixSequence: List[DiffusionBMatrixSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def DiffusionDirectionality(self) -> Optional[str]:
        if "DiffusionDirectionality" in self._dataset:
            return self._dataset.DiffusionDirectionality
        return None

    @DiffusionDirectionality.setter
    def DiffusionDirectionality(self, value: Optional[str]):
        if value is None:
            if "DiffusionDirectionality" in self._dataset:
                del self._dataset.DiffusionDirectionality
        else:
            self._dataset.DiffusionDirectionality = value

    @property
    def DiffusionGradientDirectionSequence(self) -> Optional[List[DiffusionGradientDirectionSequenceItem]]:
        if "DiffusionGradientDirectionSequence" in self._dataset:
            if len(self._DiffusionGradientDirectionSequence) == len(self._dataset.DiffusionGradientDirectionSequence):
                return self._DiffusionGradientDirectionSequence
            else:
                return [DiffusionGradientDirectionSequenceItem(x) for x in self._dataset.DiffusionGradientDirectionSequence]
        return None

    @DiffusionGradientDirectionSequence.setter
    def DiffusionGradientDirectionSequence(self, value: Optional[List[DiffusionGradientDirectionSequenceItem]]):
        if value is None:
            self._DiffusionGradientDirectionSequence = []
            if "DiffusionGradientDirectionSequence" in self._dataset:
                del self._dataset.DiffusionGradientDirectionSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, DiffusionGradientDirectionSequenceItem) for item in value
        ):
            raise ValueError(
                f"DiffusionGradientDirectionSequence must be a list of DiffusionGradientDirectionSequenceItem objects"
            )
        else:
            self._DiffusionGradientDirectionSequence = value
            if "DiffusionGradientDirectionSequence" not in self._dataset:
                self._dataset.DiffusionGradientDirectionSequence = pydicom.Sequence()
            self._dataset.DiffusionGradientDirectionSequence.clear()
            self._dataset.DiffusionGradientDirectionSequence.extend([item.to_dataset() for item in value])

    def add_DiffusionGradientDirection(self, item: DiffusionGradientDirectionSequenceItem):
        if not isinstance(item, DiffusionGradientDirectionSequenceItem):
            raise ValueError(f"Item must be an instance of DiffusionGradientDirectionSequenceItem")
        self._DiffusionGradientDirectionSequence.append(item)
        if "DiffusionGradientDirectionSequence" not in self._dataset:
            self._dataset.DiffusionGradientDirectionSequence = pydicom.Sequence()
        self._dataset.DiffusionGradientDirectionSequence.append(item.to_dataset())

    @property
    def DiffusionBValue(self) -> Optional[float]:
        if "DiffusionBValue" in self._dataset:
            return self._dataset.DiffusionBValue
        return None

    @DiffusionBValue.setter
    def DiffusionBValue(self, value: Optional[float]):
        if value is None:
            if "DiffusionBValue" in self._dataset:
                del self._dataset.DiffusionBValue
        else:
            self._dataset.DiffusionBValue = value

    @property
    def DiffusionAnisotropyType(self) -> Optional[str]:
        if "DiffusionAnisotropyType" in self._dataset:
            return self._dataset.DiffusionAnisotropyType
        return None

    @DiffusionAnisotropyType.setter
    def DiffusionAnisotropyType(self, value: Optional[str]):
        if value is None:
            if "DiffusionAnisotropyType" in self._dataset:
                del self._dataset.DiffusionAnisotropyType
        else:
            self._dataset.DiffusionAnisotropyType = value

    @property
    def DiffusionBMatrixSequence(self) -> Optional[List[DiffusionBMatrixSequenceItem]]:
        if "DiffusionBMatrixSequence" in self._dataset:
            if len(self._DiffusionBMatrixSequence) == len(self._dataset.DiffusionBMatrixSequence):
                return self._DiffusionBMatrixSequence
            else:
                return [DiffusionBMatrixSequenceItem(x) for x in self._dataset.DiffusionBMatrixSequence]
        return None

    @DiffusionBMatrixSequence.setter
    def DiffusionBMatrixSequence(self, value: Optional[List[DiffusionBMatrixSequenceItem]]):
        if value is None:
            self._DiffusionBMatrixSequence = []
            if "DiffusionBMatrixSequence" in self._dataset:
                del self._dataset.DiffusionBMatrixSequence
        elif not isinstance(value, list) or not all(isinstance(item, DiffusionBMatrixSequenceItem) for item in value):
            raise ValueError(f"DiffusionBMatrixSequence must be a list of DiffusionBMatrixSequenceItem objects")
        else:
            self._DiffusionBMatrixSequence = value
            if "DiffusionBMatrixSequence" not in self._dataset:
                self._dataset.DiffusionBMatrixSequence = pydicom.Sequence()
            self._dataset.DiffusionBMatrixSequence.clear()
            self._dataset.DiffusionBMatrixSequence.extend([item.to_dataset() for item in value])

    def add_DiffusionBMatrix(self, item: DiffusionBMatrixSequenceItem):
        if not isinstance(item, DiffusionBMatrixSequenceItem):
            raise ValueError(f"Item must be an instance of DiffusionBMatrixSequenceItem")
        self._DiffusionBMatrixSequence.append(item)
        if "DiffusionBMatrixSequence" not in self._dataset:
            self._dataset.DiffusionBMatrixSequence = pydicom.Sequence()
        self._dataset.DiffusionBMatrixSequence.append(item.to_dataset())
