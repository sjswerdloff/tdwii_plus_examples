from typing import Any, List, Optional

import pydicom


class TemporalPositionSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def TemporalPositionTimeOffset(self) -> Optional[float]:
        if "TemporalPositionTimeOffset" in self._dataset:
            return self._dataset.TemporalPositionTimeOffset
        return None

    @TemporalPositionTimeOffset.setter
    def TemporalPositionTimeOffset(self, value: Optional[float]):
        if value is None:
            if "TemporalPositionTimeOffset" in self._dataset:
                del self._dataset.TemporalPositionTimeOffset
        else:
            self._dataset.TemporalPositionTimeOffset = value
