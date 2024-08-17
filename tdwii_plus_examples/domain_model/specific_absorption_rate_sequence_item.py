from typing import Any, List, Optional

import pydicom


class SpecificAbsorptionRateSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def SpecificAbsorptionRateDefinition(self) -> Optional[str]:
        if "SpecificAbsorptionRateDefinition" in self._dataset:
            return self._dataset.SpecificAbsorptionRateDefinition
        return None

    @SpecificAbsorptionRateDefinition.setter
    def SpecificAbsorptionRateDefinition(self, value: Optional[str]):
        if value is None:
            if "SpecificAbsorptionRateDefinition" in self._dataset:
                del self._dataset.SpecificAbsorptionRateDefinition
        else:
            self._dataset.SpecificAbsorptionRateDefinition = value

    @property
    def SpecificAbsorptionRateValue(self) -> Optional[float]:
        if "SpecificAbsorptionRateValue" in self._dataset:
            return self._dataset.SpecificAbsorptionRateValue
        return None

    @SpecificAbsorptionRateValue.setter
    def SpecificAbsorptionRateValue(self, value: Optional[float]):
        if value is None:
            if "SpecificAbsorptionRateValue" in self._dataset:
                del self._dataset.SpecificAbsorptionRateValue
        else:
            self._dataset.SpecificAbsorptionRateValue = value
