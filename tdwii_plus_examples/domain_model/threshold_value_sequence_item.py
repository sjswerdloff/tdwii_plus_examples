from typing import Any, List, Optional

import pydicom


class ThresholdValueSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ThresholdValue(self) -> Optional[float]:
        if "ThresholdValue" in self._dataset:
            return self._dataset.ThresholdValue
        return None

    @ThresholdValue.setter
    def ThresholdValue(self, value: Optional[float]):
        if value is None:
            if "ThresholdValue" in self._dataset:
                del self._dataset.ThresholdValue
        else:
            self._dataset.ThresholdValue = value
