from typing import Any, List, Optional  # noqa

import pydicom


class CodingSchemeResourcesSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def CodingSchemeURLType(self) -> Optional[str]:
        if "CodingSchemeURLType" in self._dataset:
            return self._dataset.CodingSchemeURLType
        return None

    @CodingSchemeURLType.setter
    def CodingSchemeURLType(self, value: Optional[str]):
        if value is None:
            if "CodingSchemeURLType" in self._dataset:
                del self._dataset.CodingSchemeURLType
        else:
            self._dataset.CodingSchemeURLType = value

    @property
    def CodingSchemeURL(self) -> Optional[str]:
        if "CodingSchemeURL" in self._dataset:
            return self._dataset.CodingSchemeURL
        return None

    @CodingSchemeURL.setter
    def CodingSchemeURL(self, value: Optional[str]):
        if value is None:
            if "CodingSchemeURL" in self._dataset:
                del self._dataset.CodingSchemeURL
        else:
            self._dataset.CodingSchemeURL = value
