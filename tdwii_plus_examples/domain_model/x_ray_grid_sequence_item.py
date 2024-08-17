from typing import Any, List, Optional

import pydicom


class XRayGridSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def Grid(self) -> Optional[List[str]]:
        if "Grid" in self._dataset:
            return self._dataset.Grid
        return None

    @Grid.setter
    def Grid(self, value: Optional[List[str]]):
        if value is None:
            if "Grid" in self._dataset:
                del self._dataset.Grid
        else:
            self._dataset.Grid = value
