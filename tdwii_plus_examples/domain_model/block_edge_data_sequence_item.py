from typing import Any, List, Optional  # noqa

import pydicom


class BlockEdgeDataSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def BlockEdgeData(self) -> Optional[bytes]:
        if "BlockEdgeData" in self._dataset:
            return self._dataset.BlockEdgeData
        return None

    @BlockEdgeData.setter
    def BlockEdgeData(self, value: Optional[bytes]):
        if value is None:
            if "BlockEdgeData" in self._dataset:
                del self._dataset.BlockEdgeData
        else:
            self._dataset.BlockEdgeData = value
