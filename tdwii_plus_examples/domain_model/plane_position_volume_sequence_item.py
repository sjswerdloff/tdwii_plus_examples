from typing import Any, List, Optional

import pydicom


class PlanePositionVolumeSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ImagePositionVolume(self) -> Optional[List[float]]:
        if "ImagePositionVolume" in self._dataset:
            return self._dataset.ImagePositionVolume
        return None

    @ImagePositionVolume.setter
    def ImagePositionVolume(self, value: Optional[List[float]]):
        if value is None:
            if "ImagePositionVolume" in self._dataset:
                del self._dataset.ImagePositionVolume
        else:
            self._dataset.ImagePositionVolume = value
