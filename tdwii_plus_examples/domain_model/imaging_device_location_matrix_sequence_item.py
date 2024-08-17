from typing import Any, List, Optional  # noqa

import pydicom

from .image_receptor_position_sequence_item import ImageReceptorPositionSequenceItem
from .imaging_source_position_sequence_item import ImagingSourcePositionSequenceItem


class ImagingDeviceLocationMatrixSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._ImagingSourcePositionSequence: List[ImagingSourcePositionSequenceItem] = []
        self._ImageReceptorPositionSequence: List[ImageReceptorPositionSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ImagingSourcePositionSequence(self) -> Optional[List[ImagingSourcePositionSequenceItem]]:
        if "ImagingSourcePositionSequence" in self._dataset:
            if len(self._ImagingSourcePositionSequence) == len(self._dataset.ImagingSourcePositionSequence):
                return self._ImagingSourcePositionSequence
            else:
                return [ImagingSourcePositionSequenceItem(x) for x in self._dataset.ImagingSourcePositionSequence]
        return None

    @ImagingSourcePositionSequence.setter
    def ImagingSourcePositionSequence(self, value: Optional[List[ImagingSourcePositionSequenceItem]]):
        if value is None:
            self._ImagingSourcePositionSequence = []
            if "ImagingSourcePositionSequence" in self._dataset:
                del self._dataset.ImagingSourcePositionSequence
        elif not isinstance(value, list) or not all(isinstance(item, ImagingSourcePositionSequenceItem) for item in value):
            raise ValueError("ImagingSourcePositionSequence must be a list of ImagingSourcePositionSequenceItem objects")
        else:
            self._ImagingSourcePositionSequence = value
            if "ImagingSourcePositionSequence" not in self._dataset:
                self._dataset.ImagingSourcePositionSequence = pydicom.Sequence()
            self._dataset.ImagingSourcePositionSequence.clear()
            self._dataset.ImagingSourcePositionSequence.extend([item.to_dataset() for item in value])

    def add_ImagingSourcePosition(self, item: ImagingSourcePositionSequenceItem):
        if not isinstance(item, ImagingSourcePositionSequenceItem):
            raise ValueError("Item must be an instance of ImagingSourcePositionSequenceItem")
        self._ImagingSourcePositionSequence.append(item)
        if "ImagingSourcePositionSequence" not in self._dataset:
            self._dataset.ImagingSourcePositionSequence = pydicom.Sequence()
        self._dataset.ImagingSourcePositionSequence.append(item.to_dataset())

    @property
    def ImageReceptorPositionSequence(self) -> Optional[List[ImageReceptorPositionSequenceItem]]:
        if "ImageReceptorPositionSequence" in self._dataset:
            if len(self._ImageReceptorPositionSequence) == len(self._dataset.ImageReceptorPositionSequence):
                return self._ImageReceptorPositionSequence
            else:
                return [ImageReceptorPositionSequenceItem(x) for x in self._dataset.ImageReceptorPositionSequence]
        return None

    @ImageReceptorPositionSequence.setter
    def ImageReceptorPositionSequence(self, value: Optional[List[ImageReceptorPositionSequenceItem]]):
        if value is None:
            self._ImageReceptorPositionSequence = []
            if "ImageReceptorPositionSequence" in self._dataset:
                del self._dataset.ImageReceptorPositionSequence
        elif not isinstance(value, list) or not all(isinstance(item, ImageReceptorPositionSequenceItem) for item in value):
            raise ValueError("ImageReceptorPositionSequence must be a list of ImageReceptorPositionSequenceItem objects")
        else:
            self._ImageReceptorPositionSequence = value
            if "ImageReceptorPositionSequence" not in self._dataset:
                self._dataset.ImageReceptorPositionSequence = pydicom.Sequence()
            self._dataset.ImageReceptorPositionSequence.clear()
            self._dataset.ImageReceptorPositionSequence.extend([item.to_dataset() for item in value])

    def add_ImageReceptorPosition(self, item: ImageReceptorPositionSequenceItem):
        if not isinstance(item, ImageReceptorPositionSequenceItem):
            raise ValueError("Item must be an instance of ImageReceptorPositionSequenceItem")
        self._ImageReceptorPositionSequence.append(item)
        if "ImageReceptorPositionSequence" not in self._dataset:
            self._dataset.ImageReceptorPositionSequence = pydicom.Sequence()
        self._dataset.ImageReceptorPositionSequence.append(item.to_dataset())
