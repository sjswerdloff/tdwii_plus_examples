from typing import Any, List, Optional  # noqa

import pydicom


class ExcitationWavelengthSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ExcitationWavelength(self) -> Optional[float]:
        if "ExcitationWavelength" in self._dataset:
            return self._dataset.ExcitationWavelength
        return None

    @ExcitationWavelength.setter
    def ExcitationWavelength(self, value: Optional[float]):
        if value is None:
            if "ExcitationWavelength" in self._dataset:
                del self._dataset.ExcitationWavelength
        else:
            self._dataset.ExcitationWavelength = value
