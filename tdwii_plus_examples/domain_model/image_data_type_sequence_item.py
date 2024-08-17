from typing import Any, List, Optional

import pydicom


class ImageDataTypeSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def DataType(self) -> Optional[str]:
        if "DataType" in self._dataset:
            return self._dataset.DataType
        return None

    @DataType.setter
    def DataType(self, value: Optional[str]):
        if value is None:
            if "DataType" in self._dataset:
                del self._dataset.DataType
        else:
            self._dataset.DataType = value

    @property
    def AliasedDataType(self) -> Optional[str]:
        if "AliasedDataType" in self._dataset:
            return self._dataset.AliasedDataType
        return None

    @AliasedDataType.setter
    def AliasedDataType(self, value: Optional[str]):
        if value is None:
            if "AliasedDataType" in self._dataset:
                del self._dataset.AliasedDataType
        else:
            self._dataset.AliasedDataType = value

    @property
    def ZeroVelocityPixelValue(self) -> Optional[int]:
        if "ZeroVelocityPixelValue" in self._dataset:
            return self._dataset.ZeroVelocityPixelValue
        return None

    @ZeroVelocityPixelValue.setter
    def ZeroVelocityPixelValue(self, value: Optional[int]):
        if value is None:
            if "ZeroVelocityPixelValue" in self._dataset:
                del self._dataset.ZeroVelocityPixelValue
        else:
            self._dataset.ZeroVelocityPixelValue = value
