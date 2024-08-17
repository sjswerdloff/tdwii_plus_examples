from typing import Any, List, Optional  # noqa

import pydicom


class RecordedBlockSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def BlockTrayID(self) -> Optional[str]:
        if "BlockTrayID" in self._dataset:
            return self._dataset.BlockTrayID
        return None

    @BlockTrayID.setter
    def BlockTrayID(self, value: Optional[str]):
        if value is None:
            if "BlockTrayID" in self._dataset:
                del self._dataset.BlockTrayID
        else:
            self._dataset.BlockTrayID = value

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
    def BlockName(self) -> Optional[str]:
        if "BlockName" in self._dataset:
            return self._dataset.BlockName
        return None

    @BlockName.setter
    def BlockName(self, value: Optional[str]):
        if value is None:
            if "BlockName" in self._dataset:
                del self._dataset.BlockName
        else:
            self._dataset.BlockName = value

    @property
    def TrayAccessoryCode(self) -> Optional[str]:
        if "TrayAccessoryCode" in self._dataset:
            return self._dataset.TrayAccessoryCode
        return None

    @TrayAccessoryCode.setter
    def TrayAccessoryCode(self, value: Optional[str]):
        if value is None:
            if "TrayAccessoryCode" in self._dataset:
                del self._dataset.TrayAccessoryCode
        else:
            self._dataset.TrayAccessoryCode = value

    @property
    def ReferencedBlockNumber(self) -> Optional[int]:
        if "ReferencedBlockNumber" in self._dataset:
            return self._dataset.ReferencedBlockNumber
        return None

    @ReferencedBlockNumber.setter
    def ReferencedBlockNumber(self, value: Optional[int]):
        if value is None:
            if "ReferencedBlockNumber" in self._dataset:
                del self._dataset.ReferencedBlockNumber
        else:
            self._dataset.ReferencedBlockNumber = value
