from typing import Any, List, Optional  # noqa

import pydicom


class TestPointNormalsSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def DataSetName(self) -> Optional[str]:
        if "DataSetName" in self._dataset:
            return self._dataset.DataSetName
        return None

    @DataSetName.setter
    def DataSetName(self, value: Optional[str]):
        if value is None:
            if "DataSetName" in self._dataset:
                del self._dataset.DataSetName
        else:
            self._dataset.DataSetName = value

    @property
    def DataSetVersion(self) -> Optional[str]:
        if "DataSetVersion" in self._dataset:
            return self._dataset.DataSetVersion
        return None

    @DataSetVersion.setter
    def DataSetVersion(self, value: Optional[str]):
        if value is None:
            if "DataSetVersion" in self._dataset:
                del self._dataset.DataSetVersion
        else:
            self._dataset.DataSetVersion = value

    @property
    def DataSetSource(self) -> Optional[str]:
        if "DataSetSource" in self._dataset:
            return self._dataset.DataSetSource
        return None

    @DataSetSource.setter
    def DataSetSource(self, value: Optional[str]):
        if value is None:
            if "DataSetSource" in self._dataset:
                del self._dataset.DataSetSource
        else:
            self._dataset.DataSetSource = value

    @property
    def DataSetDescription(self) -> Optional[str]:
        if "DataSetDescription" in self._dataset:
            return self._dataset.DataSetDescription
        return None

    @DataSetDescription.setter
    def DataSetDescription(self, value: Optional[str]):
        if value is None:
            if "DataSetDescription" in self._dataset:
                del self._dataset.DataSetDescription
        else:
            self._dataset.DataSetDescription = value
