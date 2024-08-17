from typing import Any, List, Optional

import pydicom


class ModalityLUTSequenceItem:
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
    def LUTExplanation(self) -> Optional[str]:
        if "LUTExplanation" in self._dataset:
            return self._dataset.LUTExplanation
        return None

    @LUTExplanation.setter
    def LUTExplanation(self, value: Optional[str]):
        if value is None:
            if "LUTExplanation" in self._dataset:
                del self._dataset.LUTExplanation
        else:
            self._dataset.LUTExplanation = value

    @property
    def ModalityLUTType(self) -> Optional[str]:
        if "ModalityLUTType" in self._dataset:
            return self._dataset.ModalityLUTType
        return None

    @ModalityLUTType.setter
    def ModalityLUTType(self, value: Optional[str]):
        if value is None:
            if "ModalityLUTType" in self._dataset:
                del self._dataset.ModalityLUTType
        else:
            self._dataset.ModalityLUTType = value

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
