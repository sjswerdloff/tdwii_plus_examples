from typing import Any, List, Optional

import pydicom


class OpticalPathIdentificationSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def OpticalPathIdentifier(self) -> Optional[str]:
        if "OpticalPathIdentifier" in self._dataset:
            return self._dataset.OpticalPathIdentifier
        return None

    @OpticalPathIdentifier.setter
    def OpticalPathIdentifier(self, value: Optional[str]):
        if value is None:
            if "OpticalPathIdentifier" in self._dataset:
                del self._dataset.OpticalPathIdentifier
        else:
            self._dataset.OpticalPathIdentifier = value
