from typing import Any, List, Optional  # noqa

import pydicom


class SpecimenReferenceSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def SpecimenUID(self) -> Optional[str]:
        if "SpecimenUID" in self._dataset:
            return self._dataset.SpecimenUID
        return None

    @SpecimenUID.setter
    def SpecimenUID(self, value: Optional[str]):
        if value is None:
            if "SpecimenUID" in self._dataset:
                del self._dataset.SpecimenUID
        else:
            self._dataset.SpecimenUID = value
