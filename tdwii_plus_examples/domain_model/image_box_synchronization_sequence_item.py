from typing import Any, List, Optional

import pydicom


class ImageBoxSynchronizationSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def SynchronizedImageBoxList(self) -> Optional[List[int]]:
        if "SynchronizedImageBoxList" in self._dataset:
            return self._dataset.SynchronizedImageBoxList
        return None

    @SynchronizedImageBoxList.setter
    def SynchronizedImageBoxList(self, value: Optional[List[int]]):
        if value is None:
            if "SynchronizedImageBoxList" in self._dataset:
                del self._dataset.SynchronizedImageBoxList
        else:
            self._dataset.SynchronizedImageBoxList = value

    @property
    def TypeOfSynchronization(self) -> Optional[str]:
        if "TypeOfSynchronization" in self._dataset:
            return self._dataset.TypeOfSynchronization
        return None

    @TypeOfSynchronization.setter
    def TypeOfSynchronization(self, value: Optional[str]):
        if value is None:
            if "TypeOfSynchronization" in self._dataset:
                del self._dataset.TypeOfSynchronization
        else:
            self._dataset.TypeOfSynchronization = value
