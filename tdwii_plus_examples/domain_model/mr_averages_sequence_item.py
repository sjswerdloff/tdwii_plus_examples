from decimal import Decimal
from typing import Any, List, Optional

import pydicom


class MRAveragesSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def NumberOfAverages(self) -> Optional[Decimal]:
        if "NumberOfAverages" in self._dataset:
            return self._dataset.NumberOfAverages
        return None

    @NumberOfAverages.setter
    def NumberOfAverages(self, value: Optional[Decimal]):
        if value is None:
            if "NumberOfAverages" in self._dataset:
                del self._dataset.NumberOfAverages
        else:
            self._dataset.NumberOfAverages = value
