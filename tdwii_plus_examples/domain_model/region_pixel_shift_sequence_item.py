from typing import Any, List, Optional

import pydicom


class RegionPixelShiftSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def MaskSubPixelShift(self) -> Optional[List[float]]:
        if "MaskSubPixelShift" in self._dataset:
            return self._dataset.MaskSubPixelShift
        return None

    @MaskSubPixelShift.setter
    def MaskSubPixelShift(self, value: Optional[List[float]]):
        if value is None:
            if "MaskSubPixelShift" in self._dataset:
                del self._dataset.MaskSubPixelShift
        else:
            self._dataset.MaskSubPixelShift = value

    @property
    def VerticesOfTheRegion(self) -> Optional[List[int]]:
        if "VerticesOfTheRegion" in self._dataset:
            return self._dataset.VerticesOfTheRegion
        return None

    @VerticesOfTheRegion.setter
    def VerticesOfTheRegion(self, value: Optional[List[int]]):
        if value is None:
            if "VerticesOfTheRegion" in self._dataset:
                del self._dataset.VerticesOfTheRegion
        else:
            self._dataset.VerticesOfTheRegion = value
