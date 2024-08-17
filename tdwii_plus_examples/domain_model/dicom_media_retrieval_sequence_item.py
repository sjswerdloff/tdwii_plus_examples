from typing import Any, List, Optional

import pydicom


class DICOMMediaRetrievalSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def StorageMediaFileSetID(self) -> Optional[str]:
        if "StorageMediaFileSetID" in self._dataset:
            return self._dataset.StorageMediaFileSetID
        return None

    @StorageMediaFileSetID.setter
    def StorageMediaFileSetID(self, value: Optional[str]):
        if value is None:
            if "StorageMediaFileSetID" in self._dataset:
                del self._dataset.StorageMediaFileSetID
        else:
            self._dataset.StorageMediaFileSetID = value

    @property
    def StorageMediaFileSetUID(self) -> Optional[str]:
        if "StorageMediaFileSetUID" in self._dataset:
            return self._dataset.StorageMediaFileSetUID
        return None

    @StorageMediaFileSetUID.setter
    def StorageMediaFileSetUID(self, value: Optional[str]):
        if value is None:
            if "StorageMediaFileSetUID" in self._dataset:
                del self._dataset.StorageMediaFileSetUID
        else:
            self._dataset.StorageMediaFileSetUID = value
