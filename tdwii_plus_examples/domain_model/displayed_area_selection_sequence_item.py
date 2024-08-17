from decimal import Decimal
from typing import Any, List, Optional  # noqa

import pydicom

from .referenced_image_sequence_item import ReferencedImageSequenceItem


class DisplayedAreaSelectionSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._ReferencedImageSequence: List[ReferencedImageSequenceItem] = []

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
    def PixelOriginInterpretation(self) -> Optional[str]:
        if "PixelOriginInterpretation" in self._dataset:
            return self._dataset.PixelOriginInterpretation
        return None

    @PixelOriginInterpretation.setter
    def PixelOriginInterpretation(self, value: Optional[str]):
        if value is None:
            if "PixelOriginInterpretation" in self._dataset:
                del self._dataset.PixelOriginInterpretation
        else:
            self._dataset.PixelOriginInterpretation = value

    @property
    def DisplayedAreaTopLeftHandCorner(self) -> Optional[List[int]]:
        if "DisplayedAreaTopLeftHandCorner" in self._dataset:
            return self._dataset.DisplayedAreaTopLeftHandCorner
        return None

    @DisplayedAreaTopLeftHandCorner.setter
    def DisplayedAreaTopLeftHandCorner(self, value: Optional[List[int]]):
        if value is None:
            if "DisplayedAreaTopLeftHandCorner" in self._dataset:
                del self._dataset.DisplayedAreaTopLeftHandCorner
        else:
            self._dataset.DisplayedAreaTopLeftHandCorner = value

    @property
    def DisplayedAreaBottomRightHandCorner(self) -> Optional[List[int]]:
        if "DisplayedAreaBottomRightHandCorner" in self._dataset:
            return self._dataset.DisplayedAreaBottomRightHandCorner
        return None

    @DisplayedAreaBottomRightHandCorner.setter
    def DisplayedAreaBottomRightHandCorner(self, value: Optional[List[int]]):
        if value is None:
            if "DisplayedAreaBottomRightHandCorner" in self._dataset:
                del self._dataset.DisplayedAreaBottomRightHandCorner
        else:
            self._dataset.DisplayedAreaBottomRightHandCorner = value

    @property
    def PresentationSizeMode(self) -> Optional[str]:
        if "PresentationSizeMode" in self._dataset:
            return self._dataset.PresentationSizeMode
        return None

    @PresentationSizeMode.setter
    def PresentationSizeMode(self, value: Optional[str]):
        if value is None:
            if "PresentationSizeMode" in self._dataset:
                del self._dataset.PresentationSizeMode
        else:
            self._dataset.PresentationSizeMode = value

    @property
    def PresentationPixelSpacing(self) -> Optional[List[Decimal]]:
        if "PresentationPixelSpacing" in self._dataset:
            return self._dataset.PresentationPixelSpacing
        return None

    @PresentationPixelSpacing.setter
    def PresentationPixelSpacing(self, value: Optional[List[Decimal]]):
        if value is None:
            if "PresentationPixelSpacing" in self._dataset:
                del self._dataset.PresentationPixelSpacing
        else:
            self._dataset.PresentationPixelSpacing = value

    @property
    def PresentationPixelAspectRatio(self) -> Optional[List[int]]:
        if "PresentationPixelAspectRatio" in self._dataset:
            return self._dataset.PresentationPixelAspectRatio
        return None

    @PresentationPixelAspectRatio.setter
    def PresentationPixelAspectRatio(self, value: Optional[List[int]]):
        if value is None:
            if "PresentationPixelAspectRatio" in self._dataset:
                del self._dataset.PresentationPixelAspectRatio
        else:
            self._dataset.PresentationPixelAspectRatio = value

    @property
    def PresentationPixelMagnificationRatio(self) -> Optional[float]:
        if "PresentationPixelMagnificationRatio" in self._dataset:
            return self._dataset.PresentationPixelMagnificationRatio
        return None

    @PresentationPixelMagnificationRatio.setter
    def PresentationPixelMagnificationRatio(self, value: Optional[float]):
        if value is None:
            if "PresentationPixelMagnificationRatio" in self._dataset:
                del self._dataset.PresentationPixelMagnificationRatio
        else:
            self._dataset.PresentationPixelMagnificationRatio = value
