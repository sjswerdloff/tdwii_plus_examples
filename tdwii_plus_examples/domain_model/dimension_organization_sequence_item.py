from typing import Any, List, Optional  # noqa

import pydicom


class DimensionOrganizationSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def DimensionOrganizationUID(self) -> Optional[str]:
        if "DimensionOrganizationUID" in self._dataset:
            return self._dataset.DimensionOrganizationUID
        return None

    @DimensionOrganizationUID.setter
    def DimensionOrganizationUID(self, value: Optional[str]):
        if value is None:
            if "DimensionOrganizationUID" in self._dataset:
                del self._dataset.DimensionOrganizationUID
        else:
            self._dataset.DimensionOrganizationUID = value
