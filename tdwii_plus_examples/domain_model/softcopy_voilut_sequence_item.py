from decimal import Decimal
from typing import Any, List, Optional  # noqa

import pydicom

from .referenced_image_sequence_item import ReferencedImageSequenceItem
from .voilut_sequence_item import VOILUTSequenceItem


class SoftcopyVOILUTSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._ReferencedImageSequence: List[ReferencedImageSequenceItem] = []
        self._VOILUTSequence: List[VOILUTSequenceItem] = []

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
    def WindowCenter(self) -> Optional[List[Decimal]]:
        if "WindowCenter" in self._dataset:
            return self._dataset.WindowCenter
        return None

    @WindowCenter.setter
    def WindowCenter(self, value: Optional[List[Decimal]]):
        if value is None:
            if "WindowCenter" in self._dataset:
                del self._dataset.WindowCenter
        else:
            self._dataset.WindowCenter = value

    @property
    def WindowWidth(self) -> Optional[List[Decimal]]:
        if "WindowWidth" in self._dataset:
            return self._dataset.WindowWidth
        return None

    @WindowWidth.setter
    def WindowWidth(self, value: Optional[List[Decimal]]):
        if value is None:
            if "WindowWidth" in self._dataset:
                del self._dataset.WindowWidth
        else:
            self._dataset.WindowWidth = value

    @property
    def WindowCenterWidthExplanation(self) -> Optional[List[str]]:
        if "WindowCenterWidthExplanation" in self._dataset:
            return self._dataset.WindowCenterWidthExplanation
        return None

    @WindowCenterWidthExplanation.setter
    def WindowCenterWidthExplanation(self, value: Optional[List[str]]):
        if value is None:
            if "WindowCenterWidthExplanation" in self._dataset:
                del self._dataset.WindowCenterWidthExplanation
        else:
            self._dataset.WindowCenterWidthExplanation = value

    @property
    def VOILUTFunction(self) -> Optional[str]:
        if "VOILUTFunction" in self._dataset:
            return self._dataset.VOILUTFunction
        return None

    @VOILUTFunction.setter
    def VOILUTFunction(self, value: Optional[str]):
        if value is None:
            if "VOILUTFunction" in self._dataset:
                del self._dataset.VOILUTFunction
        else:
            self._dataset.VOILUTFunction = value

    @property
    def VOILUTSequence(self) -> Optional[List[VOILUTSequenceItem]]:
        if "VOILUTSequence" in self._dataset:
            if len(self._VOILUTSequence) == len(self._dataset.VOILUTSequence):
                return self._VOILUTSequence
            else:
                return [VOILUTSequenceItem(x) for x in self._dataset.VOILUTSequence]
        return None

    @VOILUTSequence.setter
    def VOILUTSequence(self, value: Optional[List[VOILUTSequenceItem]]):
        if value is None:
            self._VOILUTSequence = []
            if "VOILUTSequence" in self._dataset:
                del self._dataset.VOILUTSequence
        elif not isinstance(value, list) or not all(isinstance(item, VOILUTSequenceItem) for item in value):
            raise ValueError("VOILUTSequence must be a list of VOILUTSequenceItem objects")
        else:
            self._VOILUTSequence = value
            if "VOILUTSequence" not in self._dataset:
                self._dataset.VOILUTSequence = pydicom.Sequence()
            self._dataset.VOILUTSequence.clear()
            self._dataset.VOILUTSequence.extend([item.to_dataset() for item in value])

    def add_VOILUT(self, item: VOILUTSequenceItem):
        if not isinstance(item, VOILUTSequenceItem):
            raise ValueError("Item must be an instance of VOILUTSequenceItem")
        self._VOILUTSequence.append(item)
        if "VOILUTSequence" not in self._dataset:
            self._dataset.VOILUTSequence = pydicom.Sequence()
        self._dataset.VOILUTSequence.append(item.to_dataset())
