from typing import Any, List, Optional

import pydicom


class GeneralAccessorySequenceItem:
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
    def GeneralAccessoryID(self) -> Optional[str]:
        if "GeneralAccessoryID" in self._dataset:
            return self._dataset.GeneralAccessoryID
        return None

    @GeneralAccessoryID.setter
    def GeneralAccessoryID(self, value: Optional[str]):
        if value is None:
            if "GeneralAccessoryID" in self._dataset:
                del self._dataset.GeneralAccessoryID
        else:
            self._dataset.GeneralAccessoryID = value

    @property
    def GeneralAccessoryDescription(self) -> Optional[str]:
        if "GeneralAccessoryDescription" in self._dataset:
            return self._dataset.GeneralAccessoryDescription
        return None

    @GeneralAccessoryDescription.setter
    def GeneralAccessoryDescription(self, value: Optional[str]):
        if value is None:
            if "GeneralAccessoryDescription" in self._dataset:
                del self._dataset.GeneralAccessoryDescription
        else:
            self._dataset.GeneralAccessoryDescription = value

    @property
    def GeneralAccessoryType(self) -> Optional[str]:
        if "GeneralAccessoryType" in self._dataset:
            return self._dataset.GeneralAccessoryType
        return None

    @GeneralAccessoryType.setter
    def GeneralAccessoryType(self, value: Optional[str]):
        if value is None:
            if "GeneralAccessoryType" in self._dataset:
                del self._dataset.GeneralAccessoryType
        else:
            self._dataset.GeneralAccessoryType = value

    @property
    def GeneralAccessoryNumber(self) -> Optional[int]:
        if "GeneralAccessoryNumber" in self._dataset:
            return self._dataset.GeneralAccessoryNumber
        return None

    @GeneralAccessoryNumber.setter
    def GeneralAccessoryNumber(self, value: Optional[int]):
        if value is None:
            if "GeneralAccessoryNumber" in self._dataset:
                del self._dataset.GeneralAccessoryNumber
        else:
            self._dataset.GeneralAccessoryNumber = value
