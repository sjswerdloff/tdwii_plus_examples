from decimal import Decimal
from typing import Any, List, Optional

import pydicom

from .block_slab_sequence_item import BlockSlabSequenceItem


class IonBlockSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._BlockSlabSequence: List[BlockSlabSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def MaterialID(self) -> Optional[str]:
        if "MaterialID" in self._dataset:
            return self._dataset.MaterialID
        return None

    @MaterialID.setter
    def MaterialID(self, value: Optional[str]):
        if value is None:
            if "MaterialID" in self._dataset:
                del self._dataset.MaterialID
        else:
            self._dataset.MaterialID = value

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
    def IsocenterToBlockTrayDistance(self) -> Optional[float]:
        if "IsocenterToBlockTrayDistance" in self._dataset:
            return self._dataset.IsocenterToBlockTrayDistance
        return None

    @IsocenterToBlockTrayDistance.setter
    def IsocenterToBlockTrayDistance(self, value: Optional[float]):
        if value is None:
            if "IsocenterToBlockTrayDistance" in self._dataset:
                del self._dataset.IsocenterToBlockTrayDistance
        else:
            self._dataset.IsocenterToBlockTrayDistance = value

    @property
    def BlockType(self) -> Optional[str]:
        if "BlockType" in self._dataset:
            return self._dataset.BlockType
        return None

    @BlockType.setter
    def BlockType(self, value: Optional[str]):
        if value is None:
            if "BlockType" in self._dataset:
                del self._dataset.BlockType
        else:
            self._dataset.BlockType = value

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
    def BlockDivergence(self) -> Optional[str]:
        if "BlockDivergence" in self._dataset:
            return self._dataset.BlockDivergence
        return None

    @BlockDivergence.setter
    def BlockDivergence(self, value: Optional[str]):
        if value is None:
            if "BlockDivergence" in self._dataset:
                del self._dataset.BlockDivergence
        else:
            self._dataset.BlockDivergence = value

    @property
    def BlockMountingPosition(self) -> Optional[str]:
        if "BlockMountingPosition" in self._dataset:
            return self._dataset.BlockMountingPosition
        return None

    @BlockMountingPosition.setter
    def BlockMountingPosition(self, value: Optional[str]):
        if value is None:
            if "BlockMountingPosition" in self._dataset:
                del self._dataset.BlockMountingPosition
        else:
            self._dataset.BlockMountingPosition = value

    @property
    def BlockNumber(self) -> Optional[int]:
        if "BlockNumber" in self._dataset:
            return self._dataset.BlockNumber
        return None

    @BlockNumber.setter
    def BlockNumber(self, value: Optional[int]):
        if value is None:
            if "BlockNumber" in self._dataset:
                del self._dataset.BlockNumber
        else:
            self._dataset.BlockNumber = value

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
    def BlockThickness(self) -> Optional[Decimal]:
        if "BlockThickness" in self._dataset:
            return self._dataset.BlockThickness
        return None

    @BlockThickness.setter
    def BlockThickness(self, value: Optional[Decimal]):
        if value is None:
            if "BlockThickness" in self._dataset:
                del self._dataset.BlockThickness
        else:
            self._dataset.BlockThickness = value

    @property
    def BlockNumberOfPoints(self) -> Optional[int]:
        if "BlockNumberOfPoints" in self._dataset:
            return self._dataset.BlockNumberOfPoints
        return None

    @BlockNumberOfPoints.setter
    def BlockNumberOfPoints(self, value: Optional[int]):
        if value is None:
            if "BlockNumberOfPoints" in self._dataset:
                del self._dataset.BlockNumberOfPoints
        else:
            self._dataset.BlockNumberOfPoints = value

    @property
    def BlockData(self) -> Optional[List[Decimal]]:
        if "BlockData" in self._dataset:
            return self._dataset.BlockData
        return None

    @BlockData.setter
    def BlockData(self, value: Optional[List[Decimal]]):
        if value is None:
            if "BlockData" in self._dataset:
                del self._dataset.BlockData
        else:
            self._dataset.BlockData = value

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
    def BlockSlabSequence(self) -> Optional[List[BlockSlabSequenceItem]]:
        if "BlockSlabSequence" in self._dataset:
            if len(self._BlockSlabSequence) == len(self._dataset.BlockSlabSequence):
                return self._BlockSlabSequence
            else:
                return [BlockSlabSequenceItem(x) for x in self._dataset.BlockSlabSequence]
        return None

    @BlockSlabSequence.setter
    def BlockSlabSequence(self, value: Optional[List[BlockSlabSequenceItem]]):
        if value is None:
            self._BlockSlabSequence = []
            if "BlockSlabSequence" in self._dataset:
                del self._dataset.BlockSlabSequence
        elif not isinstance(value, list) or not all(isinstance(item, BlockSlabSequenceItem) for item in value):
            raise ValueError(f"BlockSlabSequence must be a list of BlockSlabSequenceItem objects")
        else:
            self._BlockSlabSequence = value
            if "BlockSlabSequence" not in self._dataset:
                self._dataset.BlockSlabSequence = pydicom.Sequence()
            self._dataset.BlockSlabSequence.clear()
            self._dataset.BlockSlabSequence.extend([item.to_dataset() for item in value])

    def add_BlockSlab(self, item: BlockSlabSequenceItem):
        if not isinstance(item, BlockSlabSequenceItem):
            raise ValueError(f"Item must be an instance of BlockSlabSequenceItem")
        self._BlockSlabSequence.append(item)
        if "BlockSlabSequence" not in self._dataset:
            self._dataset.BlockSlabSequence = pydicom.Sequence()
        self._dataset.BlockSlabSequence.append(item.to_dataset())
