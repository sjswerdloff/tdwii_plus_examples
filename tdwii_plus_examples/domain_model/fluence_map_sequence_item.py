from decimal import Decimal
from typing import Any, List, Optional  # noqa

import pydicom


class FluenceMapSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def FluenceDataSource(self) -> Optional[str]:
        if "FluenceDataSource" in self._dataset:
            return self._dataset.FluenceDataSource
        return None

    @FluenceDataSource.setter
    def FluenceDataSource(self, value: Optional[str]):
        if value is None:
            if "FluenceDataSource" in self._dataset:
                del self._dataset.FluenceDataSource
        else:
            self._dataset.FluenceDataSource = value

    @property
    def FluenceDataScale(self) -> Optional[Decimal]:
        if "FluenceDataScale" in self._dataset:
            return self._dataset.FluenceDataScale
        return None

    @FluenceDataScale.setter
    def FluenceDataScale(self, value: Optional[Decimal]):
        if value is None:
            if "FluenceDataScale" in self._dataset:
                del self._dataset.FluenceDataScale
        else:
            self._dataset.FluenceDataScale = value
