from typing import Any, List, Optional

import pydicom


class CorrectedParameterSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ParameterSequencePointer(self) -> Optional[int]:
        if "ParameterSequencePointer" in self._dataset:
            return self._dataset.ParameterSequencePointer
        return None

    @ParameterSequencePointer.setter
    def ParameterSequencePointer(self, value: Optional[int]):
        if value is None:
            if "ParameterSequencePointer" in self._dataset:
                del self._dataset.ParameterSequencePointer
        else:
            self._dataset.ParameterSequencePointer = value

    @property
    def ParameterItemIndex(self) -> Optional[int]:
        if "ParameterItemIndex" in self._dataset:
            return self._dataset.ParameterItemIndex
        return None

    @ParameterItemIndex.setter
    def ParameterItemIndex(self, value: Optional[int]):
        if value is None:
            if "ParameterItemIndex" in self._dataset:
                del self._dataset.ParameterItemIndex
        else:
            self._dataset.ParameterItemIndex = value

    @property
    def ParameterPointer(self) -> Optional[int]:
        if "ParameterPointer" in self._dataset:
            return self._dataset.ParameterPointer
        return None

    @ParameterPointer.setter
    def ParameterPointer(self, value: Optional[int]):
        if value is None:
            if "ParameterPointer" in self._dataset:
                del self._dataset.ParameterPointer
        else:
            self._dataset.ParameterPointer = value

    @property
    def CorrectionValue(self) -> Optional[float]:
        if "CorrectionValue" in self._dataset:
            return self._dataset.CorrectionValue
        return None

    @CorrectionValue.setter
    def CorrectionValue(self, value: Optional[float]):
        if value is None:
            if "CorrectionValue" in self._dataset:
                del self._dataset.CorrectionValue
        else:
            self._dataset.CorrectionValue = value
