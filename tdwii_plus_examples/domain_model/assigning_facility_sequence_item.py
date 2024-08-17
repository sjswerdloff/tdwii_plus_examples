from typing import Any, List, Optional  # noqa

import pydicom


class AssigningFacilitySequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def LocalNamespaceEntityID(self) -> Optional[str]:
        if "LocalNamespaceEntityID" in self._dataset:
            return self._dataset.LocalNamespaceEntityID
        return None

    @LocalNamespaceEntityID.setter
    def LocalNamespaceEntityID(self, value: Optional[str]):
        if value is None:
            if "LocalNamespaceEntityID" in self._dataset:
                del self._dataset.LocalNamespaceEntityID
        else:
            self._dataset.LocalNamespaceEntityID = value

    @property
    def UniversalEntityID(self) -> Optional[str]:
        if "UniversalEntityID" in self._dataset:
            return self._dataset.UniversalEntityID
        return None

    @UniversalEntityID.setter
    def UniversalEntityID(self, value: Optional[str]):
        if value is None:
            if "UniversalEntityID" in self._dataset:
                del self._dataset.UniversalEntityID
        else:
            self._dataset.UniversalEntityID = value

    @property
    def UniversalEntityIDType(self) -> Optional[str]:
        if "UniversalEntityIDType" in self._dataset:
            return self._dataset.UniversalEntityIDType
        return None

    @UniversalEntityIDType.setter
    def UniversalEntityIDType(self, value: Optional[str]):
        if value is None:
            if "UniversalEntityIDType" in self._dataset:
                del self._dataset.UniversalEntityIDType
        else:
            self._dataset.UniversalEntityIDType = value
