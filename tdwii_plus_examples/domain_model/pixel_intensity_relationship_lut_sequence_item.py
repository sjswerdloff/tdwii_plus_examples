from typing import Any, List, Optional  # noqa

import pydicom


class PixelIntensityRelationshipLUTSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def LUTDescriptor(self) -> Optional[List[int]]:
        if "LUTDescriptor" in self._dataset:
            return self._dataset.LUTDescriptor
        return None

    @LUTDescriptor.setter
    def LUTDescriptor(self, value: Optional[List[int]]):
        if value is None:
            if "LUTDescriptor" in self._dataset:
                del self._dataset.LUTDescriptor
        else:
            self._dataset.LUTDescriptor = value

    @property
    def LUTData(self) -> Optional[List[int | bytes]]:
        if "LUTData" in self._dataset:
            return self._dataset.LUTData
        return None

    @LUTData.setter
    def LUTData(self, value: Optional[List[int | bytes]]):
        if value is None:
            if "LUTData" in self._dataset:
                del self._dataset.LUTData
        else:
            self._dataset.LUTData = value

    @property
    def LUTFunction(self) -> Optional[str]:
        if "LUTFunction" in self._dataset:
            return self._dataset.LUTFunction
        return None

    @LUTFunction.setter
    def LUTFunction(self, value: Optional[str]):
        if value is None:
            if "LUTFunction" in self._dataset:
                del self._dataset.LUTFunction
        else:
            self._dataset.LUTFunction = value

    @property
    def LUTFrameRange(self) -> Optional[List[int]]:
        if "LUTFrameRange" in self._dataset:
            return self._dataset.LUTFrameRange
        return None

    @LUTFrameRange.setter
    def LUTFrameRange(self, value: Optional[List[int]]):
        if value is None:
            if "LUTFrameRange" in self._dataset:
                del self._dataset.LUTFrameRange
        else:
            self._dataset.LUTFrameRange = value
