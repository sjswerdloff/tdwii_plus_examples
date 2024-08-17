from typing import Any, List, Optional  # noqa

import pydicom

from .region_pixel_shift_sequence_item import RegionPixelShiftSequenceItem


class PixelShiftSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._RegionPixelShiftSequence: List[RegionPixelShiftSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def RegionPixelShiftSequence(self) -> Optional[List[RegionPixelShiftSequenceItem]]:
        if "RegionPixelShiftSequence" in self._dataset:
            if len(self._RegionPixelShiftSequence) == len(self._dataset.RegionPixelShiftSequence):
                return self._RegionPixelShiftSequence
            else:
                return [RegionPixelShiftSequenceItem(x) for x in self._dataset.RegionPixelShiftSequence]
        return None

    @RegionPixelShiftSequence.setter
    def RegionPixelShiftSequence(self, value: Optional[List[RegionPixelShiftSequenceItem]]):
        if value is None:
            self._RegionPixelShiftSequence = []
            if "RegionPixelShiftSequence" in self._dataset:
                del self._dataset.RegionPixelShiftSequence
        elif not isinstance(value, list) or not all(isinstance(item, RegionPixelShiftSequenceItem) for item in value):
            raise ValueError("RegionPixelShiftSequence must be a list of RegionPixelShiftSequenceItem objects")
        else:
            self._RegionPixelShiftSequence = value
            if "RegionPixelShiftSequence" not in self._dataset:
                self._dataset.RegionPixelShiftSequence = pydicom.Sequence()
            self._dataset.RegionPixelShiftSequence.clear()
            self._dataset.RegionPixelShiftSequence.extend([item.to_dataset() for item in value])

    def add_RegionPixelShift(self, item: RegionPixelShiftSequenceItem):
        if not isinstance(item, RegionPixelShiftSequenceItem):
            raise ValueError("Item must be an instance of RegionPixelShiftSequenceItem")
        self._RegionPixelShiftSequence.append(item)
        if "RegionPixelShiftSequence" not in self._dataset:
            self._dataset.RegionPixelShiftSequence = pydicom.Sequence()
        self._dataset.RegionPixelShiftSequence.append(item.to_dataset())

    @property
    def PixelShiftFrameRange(self) -> Optional[List[int]]:
        if "PixelShiftFrameRange" in self._dataset:
            return self._dataset.PixelShiftFrameRange
        return None

    @PixelShiftFrameRange.setter
    def PixelShiftFrameRange(self, value: Optional[List[int]]):
        if value is None:
            if "PixelShiftFrameRange" in self._dataset:
                del self._dataset.PixelShiftFrameRange
        else:
            self._dataset.PixelShiftFrameRange = value
