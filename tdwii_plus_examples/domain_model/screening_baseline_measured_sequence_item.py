from typing import Any, List, Optional

import pydicom


class ScreeningBaselineMeasuredSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ScreeningBaselineType(self) -> Optional[str]:
        if "ScreeningBaselineType" in self._dataset:
            return self._dataset.ScreeningBaselineType
        return None

    @ScreeningBaselineType.setter
    def ScreeningBaselineType(self, value: Optional[str]):
        if value is None:
            if "ScreeningBaselineType" in self._dataset:
                del self._dataset.ScreeningBaselineType
        else:
            self._dataset.ScreeningBaselineType = value

    @property
    def ScreeningBaselineValue(self) -> Optional[float]:
        if "ScreeningBaselineValue" in self._dataset:
            return self._dataset.ScreeningBaselineValue
        return None

    @ScreeningBaselineValue.setter
    def ScreeningBaselineValue(self, value: Optional[float]):
        if value is None:
            if "ScreeningBaselineValue" in self._dataset:
                del self._dataset.ScreeningBaselineValue
        else:
            self._dataset.ScreeningBaselineValue = value
