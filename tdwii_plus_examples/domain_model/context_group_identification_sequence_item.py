from typing import Any, List, Optional

import pydicom


class ContextGroupIdentificationSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def MappingResource(self) -> Optional[str]:
        if "MappingResource" in self._dataset:
            return self._dataset.MappingResource
        return None

    @MappingResource.setter
    def MappingResource(self, value: Optional[str]):
        if value is None:
            if "MappingResource" in self._dataset:
                del self._dataset.MappingResource
        else:
            self._dataset.MappingResource = value

    @property
    def ContextGroupVersion(self) -> Optional[str]:
        if "ContextGroupVersion" in self._dataset:
            return self._dataset.ContextGroupVersion
        return None

    @ContextGroupVersion.setter
    def ContextGroupVersion(self, value: Optional[str]):
        if value is None:
            if "ContextGroupVersion" in self._dataset:
                del self._dataset.ContextGroupVersion
        else:
            self._dataset.ContextGroupVersion = value

    @property
    def ContextIdentifier(self) -> Optional[str]:
        if "ContextIdentifier" in self._dataset:
            return self._dataset.ContextIdentifier
        return None

    @ContextIdentifier.setter
    def ContextIdentifier(self, value: Optional[str]):
        if value is None:
            if "ContextIdentifier" in self._dataset:
                del self._dataset.ContextIdentifier
        else:
            self._dataset.ContextIdentifier = value

    @property
    def ContextUID(self) -> Optional[str]:
        if "ContextUID" in self._dataset:
            return self._dataset.ContextUID
        return None

    @ContextUID.setter
    def ContextUID(self, value: Optional[str]):
        if value is None:
            if "ContextUID" in self._dataset:
                del self._dataset.ContextUID
        else:
            self._dataset.ContextUID = value
