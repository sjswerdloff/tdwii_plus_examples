from typing import Any, List, Optional

import pydicom

from .recorded_block_slab_sequence_item import RecordedBlockSlabSequenceItem


class RecordedBlockSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._RecordedBlockSlabSequence: List[RecordedBlockSlabSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def RecordedBlockSlabSequence(self) -> Optional[List[RecordedBlockSlabSequenceItem]]:
        if "RecordedBlockSlabSequence" in self._dataset:
            if len(self._RecordedBlockSlabSequence) == len(self._dataset.RecordedBlockSlabSequence):
                return self._RecordedBlockSlabSequence
            else:
                return [RecordedBlockSlabSequenceItem(x) for x in self._dataset.RecordedBlockSlabSequence]
        return None

    @RecordedBlockSlabSequence.setter
    def RecordedBlockSlabSequence(self, value: Optional[List[RecordedBlockSlabSequenceItem]]):
        if value is None:
            self._RecordedBlockSlabSequence = []
            if "RecordedBlockSlabSequence" in self._dataset:
                del self._dataset.RecordedBlockSlabSequence
        elif not isinstance(value, list) or not all(isinstance(item, RecordedBlockSlabSequenceItem) for item in value):
            raise ValueError(f"RecordedBlockSlabSequence must be a list of RecordedBlockSlabSequenceItem objects")
        else:
            self._RecordedBlockSlabSequence = value
            if "RecordedBlockSlabSequence" not in self._dataset:
                self._dataset.RecordedBlockSlabSequence = pydicom.Sequence()
            self._dataset.RecordedBlockSlabSequence.clear()
            self._dataset.RecordedBlockSlabSequence.extend([item.to_dataset() for item in value])

    def add_RecordedBlockSlab(self, item: RecordedBlockSlabSequenceItem):
        if not isinstance(item, RecordedBlockSlabSequenceItem):
            raise ValueError(f"Item must be an instance of RecordedBlockSlabSequenceItem")
        self._RecordedBlockSlabSequence.append(item)
        if "RecordedBlockSlabSequence" not in self._dataset:
            self._dataset.RecordedBlockSlabSequence = pydicom.Sequence()
        self._dataset.RecordedBlockSlabSequence.append(item.to_dataset())

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
    def NumberOfBlockSlabItems(self) -> Optional[int]:
        if "NumberOfBlockSlabItems" in self._dataset:
            return self._dataset.NumberOfBlockSlabItems
        return None

    @NumberOfBlockSlabItems.setter
    def NumberOfBlockSlabItems(self, value: Optional[int]):
        if value is None:
            if "NumberOfBlockSlabItems" in self._dataset:
                del self._dataset.NumberOfBlockSlabItems
        else:
            self._dataset.NumberOfBlockSlabItems = value

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
