from typing import Any, List, Optional

import pydicom


class CalibrationDataSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def SyringeCounts(self) -> Optional[int]:
        if "SyringeCounts" in self._dataset:
            return self._dataset.SyringeCounts
        return None

    @SyringeCounts.setter
    def SyringeCounts(self, value: Optional[int]):
        if value is None:
            if "SyringeCounts" in self._dataset:
                del self._dataset.SyringeCounts
        else:
            self._dataset.SyringeCounts = value

    @property
    def ResidualSyringeCounts(self) -> Optional[int]:
        if "ResidualSyringeCounts" in self._dataset:
            return self._dataset.ResidualSyringeCounts
        return None

    @ResidualSyringeCounts.setter
    def ResidualSyringeCounts(self, value: Optional[int]):
        if value is None:
            if "ResidualSyringeCounts" in self._dataset:
                del self._dataset.ResidualSyringeCounts
        else:
            self._dataset.ResidualSyringeCounts = value

    @property
    def EnergyWindowNumber(self) -> Optional[int]:
        if "EnergyWindowNumber" in self._dataset:
            return self._dataset.EnergyWindowNumber
        return None

    @EnergyWindowNumber.setter
    def EnergyWindowNumber(self, value: Optional[int]):
        if value is None:
            if "EnergyWindowNumber" in self._dataset:
                del self._dataset.EnergyWindowNumber
        else:
            self._dataset.EnergyWindowNumber = value
