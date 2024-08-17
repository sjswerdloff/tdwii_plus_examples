from typing import Any, List, Optional  # noqa

import pydicom


class PrimaryFluenceModeSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def FluenceMode(self) -> Optional[str]:
        if "FluenceMode" in self._dataset:
            return self._dataset.FluenceMode
        return None

    @FluenceMode.setter
    def FluenceMode(self, value: Optional[str]):
        if value is None:
            if "FluenceMode" in self._dataset:
                del self._dataset.FluenceMode
        else:
            self._dataset.FluenceMode = value

    @property
    def FluenceModeID(self) -> Optional[str]:
        if "FluenceModeID" in self._dataset:
            return self._dataset.FluenceModeID
        return None

    @FluenceModeID.setter
    def FluenceModeID(self, value: Optional[str]):
        if value is None:
            if "FluenceModeID" in self._dataset:
                del self._dataset.FluenceModeID
        else:
            self._dataset.FluenceModeID = value
