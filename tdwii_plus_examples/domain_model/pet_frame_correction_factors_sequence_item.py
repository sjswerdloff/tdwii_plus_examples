from decimal import Decimal
from typing import Any, List, Optional

import pydicom


class PETFrameCorrectionFactorsSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def PrimaryPromptsCountsAccumulated(self) -> Optional[int]:
        if "PrimaryPromptsCountsAccumulated" in self._dataset:
            return self._dataset.PrimaryPromptsCountsAccumulated
        return None

    @PrimaryPromptsCountsAccumulated.setter
    def PrimaryPromptsCountsAccumulated(self, value: Optional[int]):
        if value is None:
            if "PrimaryPromptsCountsAccumulated" in self._dataset:
                del self._dataset.PrimaryPromptsCountsAccumulated
        else:
            self._dataset.PrimaryPromptsCountsAccumulated = value

    @property
    def SliceSensitivityFactor(self) -> Optional[Decimal]:
        if "SliceSensitivityFactor" in self._dataset:
            return self._dataset.SliceSensitivityFactor
        return None

    @SliceSensitivityFactor.setter
    def SliceSensitivityFactor(self, value: Optional[Decimal]):
        if value is None:
            if "SliceSensitivityFactor" in self._dataset:
                del self._dataset.SliceSensitivityFactor
        else:
            self._dataset.SliceSensitivityFactor = value

    @property
    def DecayFactor(self) -> Optional[Decimal]:
        if "DecayFactor" in self._dataset:
            return self._dataset.DecayFactor
        return None

    @DecayFactor.setter
    def DecayFactor(self, value: Optional[Decimal]):
        if value is None:
            if "DecayFactor" in self._dataset:
                del self._dataset.DecayFactor
        else:
            self._dataset.DecayFactor = value

    @property
    def ScatterFractionFactor(self) -> Optional[Decimal]:
        if "ScatterFractionFactor" in self._dataset:
            return self._dataset.ScatterFractionFactor
        return None

    @ScatterFractionFactor.setter
    def ScatterFractionFactor(self, value: Optional[Decimal]):
        if value is None:
            if "ScatterFractionFactor" in self._dataset:
                del self._dataset.ScatterFractionFactor
        else:
            self._dataset.ScatterFractionFactor = value

    @property
    def DeadTimeFactor(self) -> Optional[Decimal]:
        if "DeadTimeFactor" in self._dataset:
            return self._dataset.DeadTimeFactor
        return None

    @DeadTimeFactor.setter
    def DeadTimeFactor(self, value: Optional[Decimal]):
        if value is None:
            if "DeadTimeFactor" in self._dataset:
                del self._dataset.DeadTimeFactor
        else:
            self._dataset.DeadTimeFactor = value
