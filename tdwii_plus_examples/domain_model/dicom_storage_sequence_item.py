from typing import Any, List, Optional

import pydicom


class DICOMStorageSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def DestinationAE(self) -> Optional[str]:
        if "DestinationAE" in self._dataset:
            return self._dataset.DestinationAE
        return None

    @DestinationAE.setter
    def DestinationAE(self, value: Optional[str]):
        if value is None:
            if "DestinationAE" in self._dataset:
                del self._dataset.DestinationAE
        else:
            self._dataset.DestinationAE = value
