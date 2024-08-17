from typing import Any, List, Optional  # noqa

import pydicom


class StoredValueColorRangeSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def MinimumStoredValueMapped(self) -> Optional[float]:
        if "MinimumStoredValueMapped" in self._dataset:
            return self._dataset.MinimumStoredValueMapped
        return None

    @MinimumStoredValueMapped.setter
    def MinimumStoredValueMapped(self, value: Optional[float]):
        if value is None:
            if "MinimumStoredValueMapped" in self._dataset:
                del self._dataset.MinimumStoredValueMapped
        else:
            self._dataset.MinimumStoredValueMapped = value

    @property
    def MaximumStoredValueMapped(self) -> Optional[float]:
        if "MaximumStoredValueMapped" in self._dataset:
            return self._dataset.MaximumStoredValueMapped
        return None

    @MaximumStoredValueMapped.setter
    def MaximumStoredValueMapped(self, value: Optional[float]):
        if value is None:
            if "MaximumStoredValueMapped" in self._dataset:
                del self._dataset.MaximumStoredValueMapped
        else:
            self._dataset.MaximumStoredValueMapped = value
