from typing import Any, List, Optional  # noqa

import pydicom


class MaximumCornealCurvatureSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def MaximumCornealCurvature(self) -> Optional[float]:
        if "MaximumCornealCurvature" in self._dataset:
            return self._dataset.MaximumCornealCurvature
        return None

    @MaximumCornealCurvature.setter
    def MaximumCornealCurvature(self, value: Optional[float]):
        if value is None:
            if "MaximumCornealCurvature" in self._dataset:
                del self._dataset.MaximumCornealCurvature
        else:
            self._dataset.MaximumCornealCurvature = value

    @property
    def MaximumCornealCurvatureLocation(self) -> Optional[List[float]]:
        if "MaximumCornealCurvatureLocation" in self._dataset:
            return self._dataset.MaximumCornealCurvatureLocation
        return None

    @MaximumCornealCurvatureLocation.setter
    def MaximumCornealCurvatureLocation(self, value: Optional[List[float]]):
        if value is None:
            if "MaximumCornealCurvatureLocation" in self._dataset:
                del self._dataset.MaximumCornealCurvatureLocation
        else:
            self._dataset.MaximumCornealCurvatureLocation = value
