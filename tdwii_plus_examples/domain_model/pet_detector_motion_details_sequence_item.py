from typing import Any, List, Optional  # noqa

import pydicom


class PETDetectorMotionDetailsSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def RotationDirection(self) -> Optional[str]:
        if "RotationDirection" in self._dataset:
            return self._dataset.RotationDirection
        return None

    @RotationDirection.setter
    def RotationDirection(self, value: Optional[str]):
        if value is None:
            if "RotationDirection" in self._dataset:
                del self._dataset.RotationDirection
        else:
            self._dataset.RotationDirection = value

    @property
    def RevolutionTime(self) -> Optional[float]:
        if "RevolutionTime" in self._dataset:
            return self._dataset.RevolutionTime
        return None

    @RevolutionTime.setter
    def RevolutionTime(self, value: Optional[float]):
        if value is None:
            if "RevolutionTime" in self._dataset:
                del self._dataset.RevolutionTime
        else:
            self._dataset.RevolutionTime = value
