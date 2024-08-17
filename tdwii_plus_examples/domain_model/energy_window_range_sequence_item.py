from decimal import Decimal
from typing import Any, List, Optional

import pydicom


class EnergyWindowRangeSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def EnergyWindowLowerLimit(self) -> Optional[Decimal]:
        if "EnergyWindowLowerLimit" in self._dataset:
            return self._dataset.EnergyWindowLowerLimit
        return None

    @EnergyWindowLowerLimit.setter
    def EnergyWindowLowerLimit(self, value: Optional[Decimal]):
        if value is None:
            if "EnergyWindowLowerLimit" in self._dataset:
                del self._dataset.EnergyWindowLowerLimit
        else:
            self._dataset.EnergyWindowLowerLimit = value

    @property
    def EnergyWindowUpperLimit(self) -> Optional[Decimal]:
        if "EnergyWindowUpperLimit" in self._dataset:
            return self._dataset.EnergyWindowUpperLimit
        return None

    @EnergyWindowUpperLimit.setter
    def EnergyWindowUpperLimit(self, value: Optional[Decimal]):
        if value is None:
            if "EnergyWindowUpperLimit" in self._dataset:
                del self._dataset.EnergyWindowUpperLimit
        else:
            self._dataset.EnergyWindowUpperLimit = value
