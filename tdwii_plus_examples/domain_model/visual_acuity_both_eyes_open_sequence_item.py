from typing import Any, List, Optional  # noqa

import pydicom


class VisualAcuityBothEyesOpenSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def VisualAcuityModifiers(self) -> Optional[List[int]]:
        if "VisualAcuityModifiers" in self._dataset:
            return self._dataset.VisualAcuityModifiers
        return None

    @VisualAcuityModifiers.setter
    def VisualAcuityModifiers(self, value: Optional[List[int]]):
        if value is None:
            if "VisualAcuityModifiers" in self._dataset:
                del self._dataset.VisualAcuityModifiers
        else:
            self._dataset.VisualAcuityModifiers = value

    @property
    def DecimalVisualAcuity(self) -> Optional[float]:
        if "DecimalVisualAcuity" in self._dataset:
            return self._dataset.DecimalVisualAcuity
        return None

    @DecimalVisualAcuity.setter
    def DecimalVisualAcuity(self, value: Optional[float]):
        if value is None:
            if "DecimalVisualAcuity" in self._dataset:
                del self._dataset.DecimalVisualAcuity
        else:
            self._dataset.DecimalVisualAcuity = value
