from typing import Any, List, Optional  # noqa

import pydicom


class DiffusionGradientDirectionSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def DiffusionGradientOrientation(self) -> Optional[List[float]]:
        if "DiffusionGradientOrientation" in self._dataset:
            return self._dataset.DiffusionGradientOrientation
        return None

    @DiffusionGradientOrientation.setter
    def DiffusionGradientOrientation(self, value: Optional[List[float]]):
        if value is None:
            if "DiffusionGradientOrientation" in self._dataset:
                del self._dataset.DiffusionGradientOrientation
        else:
            self._dataset.DiffusionGradientOrientation = value
