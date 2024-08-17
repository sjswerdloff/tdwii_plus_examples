from typing import Any, List, Optional

import pydicom


class WADORSRetrievalSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def RetrieveURL(self) -> Optional[str]:
        if "RetrieveURL" in self._dataset:
            return self._dataset.RetrieveURL
        return None

    @RetrieveURL.setter
    def RetrieveURL(self, value: Optional[str]):
        if value is None:
            if "RetrieveURL" in self._dataset:
                del self._dataset.RetrieveURL
        else:
            self._dataset.RetrieveURL = value
