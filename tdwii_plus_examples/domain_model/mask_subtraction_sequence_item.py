from typing import Any, List, Optional  # noqa

import pydicom

from .pixel_intensity_relationship_lut_sequence_item import (
    PixelIntensityRelationshipLUTSequenceItem,
)
from .pixel_shift_sequence_item import PixelShiftSequenceItem
from .referenced_image_sequence_item import ReferencedImageSequenceItem


class MaskSubtractionSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._ReferencedImageSequence: List[ReferencedImageSequenceItem] = []
        self._PixelIntensityRelationshipLUTSequence: List[PixelIntensityRelationshipLUTSequenceItem] = []
        self._PixelShiftSequence: List[PixelShiftSequenceItem] = []

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
    def MaskOperation(self) -> Optional[str]:
        if "MaskOperation" in self._dataset:
            return self._dataset.MaskOperation
        return None

    @MaskOperation.setter
    def MaskOperation(self, value: Optional[str]):
        if value is None:
            if "MaskOperation" in self._dataset:
                del self._dataset.MaskOperation
        else:
            self._dataset.MaskOperation = value

    @property
    def ApplicableFrameRange(self) -> Optional[List[int]]:
        if "ApplicableFrameRange" in self._dataset:
            return self._dataset.ApplicableFrameRange
        return None

    @ApplicableFrameRange.setter
    def ApplicableFrameRange(self, value: Optional[List[int]]):
        if value is None:
            if "ApplicableFrameRange" in self._dataset:
                del self._dataset.ApplicableFrameRange
        else:
            self._dataset.ApplicableFrameRange = value

    @property
    def MaskFrameNumbers(self) -> Optional[List[int]]:
        if "MaskFrameNumbers" in self._dataset:
            return self._dataset.MaskFrameNumbers
        return None

    @MaskFrameNumbers.setter
    def MaskFrameNumbers(self, value: Optional[List[int]]):
        if value is None:
            if "MaskFrameNumbers" in self._dataset:
                del self._dataset.MaskFrameNumbers
        else:
            self._dataset.MaskFrameNumbers = value

    @property
    def ContrastFrameAveraging(self) -> Optional[int]:
        if "ContrastFrameAveraging" in self._dataset:
            return self._dataset.ContrastFrameAveraging
        return None

    @ContrastFrameAveraging.setter
    def ContrastFrameAveraging(self, value: Optional[int]):
        if value is None:
            if "ContrastFrameAveraging" in self._dataset:
                del self._dataset.ContrastFrameAveraging
        else:
            self._dataset.ContrastFrameAveraging = value

    @property
    def TIDOffset(self) -> Optional[int]:
        if "TIDOffset" in self._dataset:
            return self._dataset.TIDOffset
        return None

    @TIDOffset.setter
    def TIDOffset(self, value: Optional[int]):
        if value is None:
            if "TIDOffset" in self._dataset:
                del self._dataset.TIDOffset
        else:
            self._dataset.TIDOffset = value

    @property
    def PixelIntensityRelationshipLUTSequence(self) -> Optional[List[PixelIntensityRelationshipLUTSequenceItem]]:
        if "PixelIntensityRelationshipLUTSequence" in self._dataset:
            if len(self._PixelIntensityRelationshipLUTSequence) == len(self._dataset.PixelIntensityRelationshipLUTSequence):
                return self._PixelIntensityRelationshipLUTSequence
            else:
                return [
                    PixelIntensityRelationshipLUTSequenceItem(x) for x in self._dataset.PixelIntensityRelationshipLUTSequence
                ]
        return None

    @PixelIntensityRelationshipLUTSequence.setter
    def PixelIntensityRelationshipLUTSequence(self, value: Optional[List[PixelIntensityRelationshipLUTSequenceItem]]):
        if value is None:
            self._PixelIntensityRelationshipLUTSequence = []
            if "PixelIntensityRelationshipLUTSequence" in self._dataset:
                del self._dataset.PixelIntensityRelationshipLUTSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, PixelIntensityRelationshipLUTSequenceItem) for item in value
        ):
            raise ValueError(
                "PixelIntensityRelationshipLUTSequence must be a list of PixelIntensityRelationshipLUTSequenceItem objects"
            )
        else:
            self._PixelIntensityRelationshipLUTSequence = value
            if "PixelIntensityRelationshipLUTSequence" not in self._dataset:
                self._dataset.PixelIntensityRelationshipLUTSequence = pydicom.Sequence()
            self._dataset.PixelIntensityRelationshipLUTSequence.clear()
            self._dataset.PixelIntensityRelationshipLUTSequence.extend([item.to_dataset() for item in value])

    def add_PixelIntensityRelationshipLUT(self, item: PixelIntensityRelationshipLUTSequenceItem):
        if not isinstance(item, PixelIntensityRelationshipLUTSequenceItem):
            raise ValueError("Item must be an instance of PixelIntensityRelationshipLUTSequenceItem")
        self._PixelIntensityRelationshipLUTSequence.append(item)
        if "PixelIntensityRelationshipLUTSequence" not in self._dataset:
            self._dataset.PixelIntensityRelationshipLUTSequence = pydicom.Sequence()
        self._dataset.PixelIntensityRelationshipLUTSequence.append(item.to_dataset())

    @property
    def PixelShiftSequence(self) -> Optional[List[PixelShiftSequenceItem]]:
        if "PixelShiftSequence" in self._dataset:
            if len(self._PixelShiftSequence) == len(self._dataset.PixelShiftSequence):
                return self._PixelShiftSequence
            else:
                return [PixelShiftSequenceItem(x) for x in self._dataset.PixelShiftSequence]
        return None

    @PixelShiftSequence.setter
    def PixelShiftSequence(self, value: Optional[List[PixelShiftSequenceItem]]):
        if value is None:
            self._PixelShiftSequence = []
            if "PixelShiftSequence" in self._dataset:
                del self._dataset.PixelShiftSequence
        elif not isinstance(value, list) or not all(isinstance(item, PixelShiftSequenceItem) for item in value):
            raise ValueError("PixelShiftSequence must be a list of PixelShiftSequenceItem objects")
        else:
            self._PixelShiftSequence = value
            if "PixelShiftSequence" not in self._dataset:
                self._dataset.PixelShiftSequence = pydicom.Sequence()
            self._dataset.PixelShiftSequence.clear()
            self._dataset.PixelShiftSequence.extend([item.to_dataset() for item in value])

    def add_PixelShift(self, item: PixelShiftSequenceItem):
        if not isinstance(item, PixelShiftSequenceItem):
            raise ValueError("Item must be an instance of PixelShiftSequenceItem")
        self._PixelShiftSequence.append(item)
        if "PixelShiftSequence" not in self._dataset:
            self._dataset.PixelShiftSequence = pydicom.Sequence()
        self._dataset.PixelShiftSequence.append(item.to_dataset())
