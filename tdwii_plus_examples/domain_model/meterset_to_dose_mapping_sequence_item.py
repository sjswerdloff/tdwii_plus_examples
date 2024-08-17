from typing import Any, List, Optional

import pydicom


class MetersetToDoseMappingSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def RadiationDoseValue(self) -> Optional[float]:
        if "RadiationDoseValue" in self._dataset:
            return self._dataset.RadiationDoseValue
        return None

    @RadiationDoseValue.setter
    def RadiationDoseValue(self, value: Optional[float]):
        if value is None:
            if "RadiationDoseValue" in self._dataset:
                del self._dataset.RadiationDoseValue
        else:
            self._dataset.RadiationDoseValue = value

    @property
    def CumulativeMeterset(self) -> Optional[float]:
        if "CumulativeMeterset" in self._dataset:
            return self._dataset.CumulativeMeterset
        return None

    @CumulativeMeterset.setter
    def CumulativeMeterset(self, value: Optional[float]):
        if value is None:
            if "CumulativeMeterset" in self._dataset:
                del self._dataset.CumulativeMeterset
        else:
            self._dataset.CumulativeMeterset = value
