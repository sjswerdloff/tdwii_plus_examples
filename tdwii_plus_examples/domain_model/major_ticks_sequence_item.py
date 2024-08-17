from typing import Any, List, Optional

import pydicom


class MajorTicksSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def TickPosition(self) -> Optional[float]:
        if "TickPosition" in self._dataset:
            return self._dataset.TickPosition
        return None

    @TickPosition.setter
    def TickPosition(self, value: Optional[float]):
        if value is None:
            if "TickPosition" in self._dataset:
                del self._dataset.TickPosition
        else:
            self._dataset.TickPosition = value

    @property
    def TickLabel(self) -> Optional[str]:
        if "TickLabel" in self._dataset:
            return self._dataset.TickLabel
        return None

    @TickLabel.setter
    def TickLabel(self, value: Optional[str]):
        if value is None:
            if "TickLabel" in self._dataset:
                del self._dataset.TickLabel
        else:
            self._dataset.TickLabel = value
