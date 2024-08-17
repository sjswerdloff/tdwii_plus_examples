from typing import Any, List, Optional

import pydicom


class ImageFilterDetailsSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ImageFilter(self) -> Optional[str]:
        if "ImageFilter" in self._dataset:
            return self._dataset.ImageFilter
        return None

    @ImageFilter.setter
    def ImageFilter(self, value: Optional[str]):
        if value is None:
            if "ImageFilter" in self._dataset:
                del self._dataset.ImageFilter
        else:
            self._dataset.ImageFilter = value

    @property
    def ImageFilterDescription(self) -> Optional[str]:
        if "ImageFilterDescription" in self._dataset:
            return self._dataset.ImageFilterDescription
        return None

    @ImageFilterDescription.setter
    def ImageFilterDescription(self, value: Optional[str]):
        if value is None:
            if "ImageFilterDescription" in self._dataset:
                del self._dataset.ImageFilterDescription
        else:
            self._dataset.ImageFilterDescription = value
