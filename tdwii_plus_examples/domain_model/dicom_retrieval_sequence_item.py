from typing import Any, List, Optional

import pydicom


class DICOMRetrievalSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def RetrieveAETitle(self) -> Optional[List[str]]:
        if "RetrieveAETitle" in self._dataset:
            return self._dataset.RetrieveAETitle
        return None

    @RetrieveAETitle.setter
    def RetrieveAETitle(self, value: Optional[List[str]]):
        if value is None:
            if "RetrieveAETitle" in self._dataset:
                del self._dataset.RetrieveAETitle
        else:
            self._dataset.RetrieveAETitle = value
