from typing import Any, List, Optional  # noqa

import pydicom


class FramePixelShiftSequenceItem:
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
    def SubtractionItemID(self) -> Optional[int]:
        if "SubtractionItemID" in self._dataset:
            return self._dataset.SubtractionItemID
        return None

    @SubtractionItemID.setter
    def SubtractionItemID(self, value: Optional[int]):
        if value is None:
            if "SubtractionItemID" in self._dataset:
                del self._dataset.SubtractionItemID
        else:
            self._dataset.SubtractionItemID = value
