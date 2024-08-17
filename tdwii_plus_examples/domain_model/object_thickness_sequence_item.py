from typing import Any, List, Optional  # noqa

import pydicom


class ObjectThicknessSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def CalculatedAnatomyThickness(self) -> Optional[float]:
        if "CalculatedAnatomyThickness" in self._dataset:
            return self._dataset.CalculatedAnatomyThickness
        return None

    @CalculatedAnatomyThickness.setter
    def CalculatedAnatomyThickness(self, value: Optional[float]):
        if value is None:
            if "CalculatedAnatomyThickness" in self._dataset:
                del self._dataset.CalculatedAnatomyThickness
        else:
            self._dataset.CalculatedAnatomyThickness = value
