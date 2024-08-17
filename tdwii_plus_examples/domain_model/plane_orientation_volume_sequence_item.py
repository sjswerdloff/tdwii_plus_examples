from typing import Any, List, Optional

import pydicom


class PlaneOrientationVolumeSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ImageOrientationVolume(self) -> Optional[List[float]]:
        if "ImageOrientationVolume" in self._dataset:
            return self._dataset.ImageOrientationVolume
        return None

    @ImageOrientationVolume.setter
    def ImageOrientationVolume(self, value: Optional[List[float]]):
        if value is None:
            if "ImageOrientationVolume" in self._dataset:
                del self._dataset.ImageOrientationVolume
        else:
            self._dataset.ImageOrientationVolume = value
