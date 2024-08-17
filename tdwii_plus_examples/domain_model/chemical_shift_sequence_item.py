from typing import Any, List, Optional  # noqa

import pydicom


class ChemicalShiftSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ChemicalShiftMinimumIntegrationLimitInppm(self) -> Optional[float]:
        if "ChemicalShiftMinimumIntegrationLimitInppm" in self._dataset:
            return self._dataset.ChemicalShiftMinimumIntegrationLimitInppm
        return None

    @ChemicalShiftMinimumIntegrationLimitInppm.setter
    def ChemicalShiftMinimumIntegrationLimitInppm(self, value: Optional[float]):
        if value is None:
            if "ChemicalShiftMinimumIntegrationLimitInppm" in self._dataset:
                del self._dataset.ChemicalShiftMinimumIntegrationLimitInppm
        else:
            self._dataset.ChemicalShiftMinimumIntegrationLimitInppm = value

    @property
    def ChemicalShiftMaximumIntegrationLimitInppm(self) -> Optional[float]:
        if "ChemicalShiftMaximumIntegrationLimitInppm" in self._dataset:
            return self._dataset.ChemicalShiftMaximumIntegrationLimitInppm
        return None

    @ChemicalShiftMaximumIntegrationLimitInppm.setter
    def ChemicalShiftMaximumIntegrationLimitInppm(self, value: Optional[float]):
        if value is None:
            if "ChemicalShiftMaximumIntegrationLimitInppm" in self._dataset:
                del self._dataset.ChemicalShiftMaximumIntegrationLimitInppm
        else:
            self._dataset.ChemicalShiftMaximumIntegrationLimitInppm = value
