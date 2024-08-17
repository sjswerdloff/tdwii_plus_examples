from decimal import Decimal
from typing import Any, List, Optional  # noqa

import pydicom

from .modality_lut_sequence_item import ModalityLUTSequenceItem
from .referenced_image_sequence_item import ReferencedImageSequenceItem


class VariableModalityLUTSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._ReferencedImageSequence: List[ReferencedImageSequenceItem] = []
        self._ModalityLUTSequence: List[ModalityLUTSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ReferencedImageSequence(self) -> Optional[List[ReferencedImageSequenceItem]]:
        if "ReferencedImageSequence" in self._dataset:
            if len(self._ReferencedImageSequence) == len(self._dataset.ReferencedImageSequence):
                return self._ReferencedImageSequence
            else:
                return [ReferencedImageSequenceItem(x) for x in self._dataset.ReferencedImageSequence]
        return None

    @ReferencedImageSequence.setter
    def ReferencedImageSequence(self, value: Optional[List[ReferencedImageSequenceItem]]):
        if value is None:
            self._ReferencedImageSequence = []
            if "ReferencedImageSequence" in self._dataset:
                del self._dataset.ReferencedImageSequence
        elif not isinstance(value, list) or not all(isinstance(item, ReferencedImageSequenceItem) for item in value):
            raise ValueError("ReferencedImageSequence must be a list of ReferencedImageSequenceItem objects")
        else:
            self._ReferencedImageSequence = value
            if "ReferencedImageSequence" not in self._dataset:
                self._dataset.ReferencedImageSequence = pydicom.Sequence()
            self._dataset.ReferencedImageSequence.clear()
            self._dataset.ReferencedImageSequence.extend([item.to_dataset() for item in value])

    def add_ReferencedImage(self, item: ReferencedImageSequenceItem):
        if not isinstance(item, ReferencedImageSequenceItem):
            raise ValueError("Item must be an instance of ReferencedImageSequenceItem")
        self._ReferencedImageSequence.append(item)
        if "ReferencedImageSequence" not in self._dataset:
            self._dataset.ReferencedImageSequence = pydicom.Sequence()
        self._dataset.ReferencedImageSequence.append(item.to_dataset())

    @property
    def RescaleIntercept(self) -> Optional[Decimal]:
        if "RescaleIntercept" in self._dataset:
            return self._dataset.RescaleIntercept
        return None

    @RescaleIntercept.setter
    def RescaleIntercept(self, value: Optional[Decimal]):
        if value is None:
            if "RescaleIntercept" in self._dataset:
                del self._dataset.RescaleIntercept
        else:
            self._dataset.RescaleIntercept = value

    @property
    def RescaleSlope(self) -> Optional[Decimal]:
        if "RescaleSlope" in self._dataset:
            return self._dataset.RescaleSlope
        return None

    @RescaleSlope.setter
    def RescaleSlope(self, value: Optional[Decimal]):
        if value is None:
            if "RescaleSlope" in self._dataset:
                del self._dataset.RescaleSlope
        else:
            self._dataset.RescaleSlope = value

    @property
    def RescaleType(self) -> Optional[str]:
        if "RescaleType" in self._dataset:
            return self._dataset.RescaleType
        return None

    @RescaleType.setter
    def RescaleType(self, value: Optional[str]):
        if value is None:
            if "RescaleType" in self._dataset:
                del self._dataset.RescaleType
        else:
            self._dataset.RescaleType = value

    @property
    def ModalityLUTSequence(self) -> Optional[List[ModalityLUTSequenceItem]]:
        if "ModalityLUTSequence" in self._dataset:
            if len(self._ModalityLUTSequence) == len(self._dataset.ModalityLUTSequence):
                return self._ModalityLUTSequence
            else:
                return [ModalityLUTSequenceItem(x) for x in self._dataset.ModalityLUTSequence]
        return None

    @ModalityLUTSequence.setter
    def ModalityLUTSequence(self, value: Optional[List[ModalityLUTSequenceItem]]):
        if value is None:
            self._ModalityLUTSequence = []
            if "ModalityLUTSequence" in self._dataset:
                del self._dataset.ModalityLUTSequence
        elif not isinstance(value, list) or not all(isinstance(item, ModalityLUTSequenceItem) for item in value):
            raise ValueError("ModalityLUTSequence must be a list of ModalityLUTSequenceItem objects")
        else:
            self._ModalityLUTSequence = value
            if "ModalityLUTSequence" not in self._dataset:
                self._dataset.ModalityLUTSequence = pydicom.Sequence()
            self._dataset.ModalityLUTSequence.clear()
            self._dataset.ModalityLUTSequence.extend([item.to_dataset() for item in value])

    def add_ModalityLUT(self, item: ModalityLUTSequenceItem):
        if not isinstance(item, ModalityLUTSequenceItem):
            raise ValueError("Item must be an instance of ModalityLUTSequenceItem")
        self._ModalityLUTSequence.append(item)
        if "ModalityLUTSequence" not in self._dataset:
            self._dataset.ModalityLUTSequence = pydicom.Sequence()
        self._dataset.ModalityLUTSequence.append(item.to_dataset())
