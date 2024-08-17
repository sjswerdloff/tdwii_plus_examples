from typing import Any, List, Optional

import pydicom


class MultiCoilDefinitionSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def MultiCoilElementName(self) -> Optional[str]:
        if "MultiCoilElementName" in self._dataset:
            return self._dataset.MultiCoilElementName
        return None

    @MultiCoilElementName.setter
    def MultiCoilElementName(self, value: Optional[str]):
        if value is None:
            if "MultiCoilElementName" in self._dataset:
                del self._dataset.MultiCoilElementName
        else:
            self._dataset.MultiCoilElementName = value

    @property
    def MultiCoilElementUsed(self) -> Optional[str]:
        if "MultiCoilElementUsed" in self._dataset:
            return self._dataset.MultiCoilElementUsed
        return None

    @MultiCoilElementUsed.setter
    def MultiCoilElementUsed(self, value: Optional[str]):
        if value is None:
            if "MultiCoilElementUsed" in self._dataset:
                del self._dataset.MultiCoilElementUsed
        else:
            self._dataset.MultiCoilElementUsed = value
