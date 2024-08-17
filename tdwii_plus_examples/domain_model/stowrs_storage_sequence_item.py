from typing import Any, List, Optional  # noqa

import pydicom


class STOWRSStorageSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def StorageURL(self) -> Optional[str]:
        if "StorageURL" in self._dataset:
            return self._dataset.StorageURL
        return None

    @StorageURL.setter
    def StorageURL(self, value: Optional[str]):
        if value is None:
            if "StorageURL" in self._dataset:
                del self._dataset.StorageURL
        else:
            self._dataset.StorageURL = value
