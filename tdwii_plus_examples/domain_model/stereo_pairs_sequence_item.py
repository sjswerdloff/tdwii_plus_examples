from typing import Any, List, Optional  # noqa

import pydicom

from .left_image_sequence_item import LeftImageSequenceItem
from .right_image_sequence_item import RightImageSequenceItem


class StereoPairsSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._LeftImageSequence: List[LeftImageSequenceItem] = []
        self._RightImageSequence: List[RightImageSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def StereoBaselineAngle(self) -> Optional[float]:
        if "StereoBaselineAngle" in self._dataset:
            return self._dataset.StereoBaselineAngle
        return None

    @StereoBaselineAngle.setter
    def StereoBaselineAngle(self, value: Optional[float]):
        if value is None:
            if "StereoBaselineAngle" in self._dataset:
                del self._dataset.StereoBaselineAngle
        else:
            self._dataset.StereoBaselineAngle = value

    @property
    def StereoBaselineDisplacement(self) -> Optional[float]:
        if "StereoBaselineDisplacement" in self._dataset:
            return self._dataset.StereoBaselineDisplacement
        return None

    @StereoBaselineDisplacement.setter
    def StereoBaselineDisplacement(self, value: Optional[float]):
        if value is None:
            if "StereoBaselineDisplacement" in self._dataset:
                del self._dataset.StereoBaselineDisplacement
        else:
            self._dataset.StereoBaselineDisplacement = value

    @property
    def StereoHorizontalPixelOffset(self) -> Optional[float]:
        if "StereoHorizontalPixelOffset" in self._dataset:
            return self._dataset.StereoHorizontalPixelOffset
        return None

    @StereoHorizontalPixelOffset.setter
    def StereoHorizontalPixelOffset(self, value: Optional[float]):
        if value is None:
            if "StereoHorizontalPixelOffset" in self._dataset:
                del self._dataset.StereoHorizontalPixelOffset
        else:
            self._dataset.StereoHorizontalPixelOffset = value

    @property
    def StereoVerticalPixelOffset(self) -> Optional[float]:
        if "StereoVerticalPixelOffset" in self._dataset:
            return self._dataset.StereoVerticalPixelOffset
        return None

    @StereoVerticalPixelOffset.setter
    def StereoVerticalPixelOffset(self, value: Optional[float]):
        if value is None:
            if "StereoVerticalPixelOffset" in self._dataset:
                del self._dataset.StereoVerticalPixelOffset
        else:
            self._dataset.StereoVerticalPixelOffset = value

    @property
    def StereoRotation(self) -> Optional[float]:
        if "StereoRotation" in self._dataset:
            return self._dataset.StereoRotation
        return None

    @StereoRotation.setter
    def StereoRotation(self, value: Optional[float]):
        if value is None:
            if "StereoRotation" in self._dataset:
                del self._dataset.StereoRotation
        else:
            self._dataset.StereoRotation = value

    @property
    def LeftImageSequence(self) -> Optional[List[LeftImageSequenceItem]]:
        if "LeftImageSequence" in self._dataset:
            if len(self._LeftImageSequence) == len(self._dataset.LeftImageSequence):
                return self._LeftImageSequence
            else:
                return [LeftImageSequenceItem(x) for x in self._dataset.LeftImageSequence]
        return None

    @LeftImageSequence.setter
    def LeftImageSequence(self, value: Optional[List[LeftImageSequenceItem]]):
        if value is None:
            self._LeftImageSequence = []
            if "LeftImageSequence" in self._dataset:
                del self._dataset.LeftImageSequence
        elif not isinstance(value, list) or not all(isinstance(item, LeftImageSequenceItem) for item in value):
            raise ValueError("LeftImageSequence must be a list of LeftImageSequenceItem objects")
        else:
            self._LeftImageSequence = value
            if "LeftImageSequence" not in self._dataset:
                self._dataset.LeftImageSequence = pydicom.Sequence()
            self._dataset.LeftImageSequence.clear()
            self._dataset.LeftImageSequence.extend([item.to_dataset() for item in value])

    def add_LeftImage(self, item: LeftImageSequenceItem):
        if not isinstance(item, LeftImageSequenceItem):
            raise ValueError("Item must be an instance of LeftImageSequenceItem")
        self._LeftImageSequence.append(item)
        if "LeftImageSequence" not in self._dataset:
            self._dataset.LeftImageSequence = pydicom.Sequence()
        self._dataset.LeftImageSequence.append(item.to_dataset())

    @property
    def RightImageSequence(self) -> Optional[List[RightImageSequenceItem]]:
        if "RightImageSequence" in self._dataset:
            if len(self._RightImageSequence) == len(self._dataset.RightImageSequence):
                return self._RightImageSequence
            else:
                return [RightImageSequenceItem(x) for x in self._dataset.RightImageSequence]
        return None

    @RightImageSequence.setter
    def RightImageSequence(self, value: Optional[List[RightImageSequenceItem]]):
        if value is None:
            self._RightImageSequence = []
            if "RightImageSequence" in self._dataset:
                del self._dataset.RightImageSequence
        elif not isinstance(value, list) or not all(isinstance(item, RightImageSequenceItem) for item in value):
            raise ValueError("RightImageSequence must be a list of RightImageSequenceItem objects")
        else:
            self._RightImageSequence = value
            if "RightImageSequence" not in self._dataset:
                self._dataset.RightImageSequence = pydicom.Sequence()
            self._dataset.RightImageSequence.clear()
            self._dataset.RightImageSequence.extend([item.to_dataset() for item in value])

    def add_RightImage(self, item: RightImageSequenceItem):
        if not isinstance(item, RightImageSequenceItem):
            raise ValueError("Item must be an instance of RightImageSequenceItem")
        self._RightImageSequence.append(item)
        if "RightImageSequence" not in self._dataset:
            self._dataset.RightImageSequence = pydicom.Sequence()
        self._dataset.RightImageSequence.append(item.to_dataset())
