from typing import Any, List, Optional

import pydicom


class RecordedBlockSlabSequenceItem:
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
    def BlockSlabNumber(self) -> Optional[int]:
        if "BlockSlabNumber" in self._dataset:
            return self._dataset.BlockSlabNumber
        return None

    @BlockSlabNumber.setter
    def BlockSlabNumber(self, value: Optional[int]):
        if value is None:
            if "BlockSlabNumber" in self._dataset:
                del self._dataset.BlockSlabNumber
        else:
            self._dataset.BlockSlabNumber = value
