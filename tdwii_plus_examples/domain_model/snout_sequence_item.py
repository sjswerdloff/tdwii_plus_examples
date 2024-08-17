from typing import Any, List, Optional  # noqa

import pydicom


class SnoutSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def AccessoryCode(self) -> Optional[str]:
        if "AccessoryCode" in self._dataset:
            return self._dataset.AccessoryCode
        return None

    @AccessoryCode.setter
    def AccessoryCode(self, value: Optional[str]):
        if value is None:
            if "AccessoryCode" in self._dataset:
                del self._dataset.AccessoryCode
        else:
            self._dataset.AccessoryCode = value

    @property
    def SnoutID(self) -> Optional[str]:
        if "SnoutID" in self._dataset:
            return self._dataset.SnoutID
        return None

    @SnoutID.setter
    def SnoutID(self, value: Optional[str]):
        if value is None:
            if "SnoutID" in self._dataset:
                del self._dataset.SnoutID
        else:
            self._dataset.SnoutID = value
