from typing import Any, List, Optional

import pydicom


class ExcludedIntervalsSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ExclusionStartDateTime(self) -> Optional[str]:
        if "ExclusionStartDateTime" in self._dataset:
            return self._dataset.ExclusionStartDateTime
        return None

    @ExclusionStartDateTime.setter
    def ExclusionStartDateTime(self, value: Optional[str]):
        if value is None:
            if "ExclusionStartDateTime" in self._dataset:
                del self._dataset.ExclusionStartDateTime
        else:
            self._dataset.ExclusionStartDateTime = value

    @property
    def ExclusionDuration(self) -> Optional[float]:
        if "ExclusionDuration" in self._dataset:
            return self._dataset.ExclusionDuration
        return None

    @ExclusionDuration.setter
    def ExclusionDuration(self, value: Optional[float]):
        if value is None:
            if "ExclusionDuration" in self._dataset:
                del self._dataset.ExclusionDuration
        else:
            self._dataset.ExclusionDuration = value
