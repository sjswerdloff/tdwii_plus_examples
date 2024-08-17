from typing import Any, List, Optional

import pydicom


class ContentTemplateSequenceItem:
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
    def MappingResourceUID(self) -> Optional[str]:
        if "MappingResourceUID" in self._dataset:
            return self._dataset.MappingResourceUID
        return None

    @MappingResourceUID.setter
    def MappingResourceUID(self, value: Optional[str]):
        if value is None:
            if "MappingResourceUID" in self._dataset:
                del self._dataset.MappingResourceUID
        else:
            self._dataset.MappingResourceUID = value

    @property
    def TemplateIdentifier(self) -> Optional[str]:
        if "TemplateIdentifier" in self._dataset:
            return self._dataset.TemplateIdentifier
        return None

    @TemplateIdentifier.setter
    def TemplateIdentifier(self, value: Optional[str]):
        if value is None:
            if "TemplateIdentifier" in self._dataset:
                del self._dataset.TemplateIdentifier
        else:
            self._dataset.TemplateIdentifier = value
