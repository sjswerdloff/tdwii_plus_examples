from typing import Any, List, Optional  # noqa

import pydicom


class PatientOrientationInFrameSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def PatientOrientation(self) -> Optional[List[str]]:
        if "PatientOrientation" in self._dataset:
            return self._dataset.PatientOrientation
        return None

    @PatientOrientation.setter
    def PatientOrientation(self, value: Optional[List[str]]):
        if value is None:
            if "PatientOrientation" in self._dataset:
                del self._dataset.PatientOrientation
        else:
            self._dataset.PatientOrientation = value
