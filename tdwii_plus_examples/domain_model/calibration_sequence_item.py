from typing import Any, List, Optional  # noqa

import pydicom


class CalibrationSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def CalibrationImage(self) -> Optional[str]:
        if "CalibrationImage" in self._dataset:
            return self._dataset.CalibrationImage
        return None

    @CalibrationImage.setter
    def CalibrationImage(self, value: Optional[str]):
        if value is None:
            if "CalibrationImage" in self._dataset:
                del self._dataset.CalibrationImage
        else:
            self._dataset.CalibrationImage = value
