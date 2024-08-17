from decimal import Decimal
from typing import Any, List, Optional

import pydicom


class BeamLimitingDeviceSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def RTBeamLimitingDeviceType(self) -> Optional[str]:
        if "RTBeamLimitingDeviceType" in self._dataset:
            return self._dataset.RTBeamLimitingDeviceType
        return None

    @RTBeamLimitingDeviceType.setter
    def RTBeamLimitingDeviceType(self, value: Optional[str]):
        if value is None:
            if "RTBeamLimitingDeviceType" in self._dataset:
                del self._dataset.RTBeamLimitingDeviceType
        else:
            self._dataset.RTBeamLimitingDeviceType = value

    @property
    def SourceToBeamLimitingDeviceDistance(self) -> Optional[Decimal]:
        if "SourceToBeamLimitingDeviceDistance" in self._dataset:
            return self._dataset.SourceToBeamLimitingDeviceDistance
        return None

    @SourceToBeamLimitingDeviceDistance.setter
    def SourceToBeamLimitingDeviceDistance(self, value: Optional[Decimal]):
        if value is None:
            if "SourceToBeamLimitingDeviceDistance" in self._dataset:
                del self._dataset.SourceToBeamLimitingDeviceDistance
        else:
            self._dataset.SourceToBeamLimitingDeviceDistance = value

    @property
    def NumberOfLeafJawPairs(self) -> Optional[int]:
        if "NumberOfLeafJawPairs" in self._dataset:
            return self._dataset.NumberOfLeafJawPairs
        return None

    @NumberOfLeafJawPairs.setter
    def NumberOfLeafJawPairs(self, value: Optional[int]):
        if value is None:
            if "NumberOfLeafJawPairs" in self._dataset:
                del self._dataset.NumberOfLeafJawPairs
        else:
            self._dataset.NumberOfLeafJawPairs = value

    @property
    def LeafPositionBoundaries(self) -> Optional[List[Decimal]]:
        if "LeafPositionBoundaries" in self._dataset:
            return self._dataset.LeafPositionBoundaries
        return None

    @LeafPositionBoundaries.setter
    def LeafPositionBoundaries(self, value: Optional[List[Decimal]]):
        if value is None:
            if "LeafPositionBoundaries" in self._dataset:
                del self._dataset.LeafPositionBoundaries
        else:
            self._dataset.LeafPositionBoundaries = value

    @property
    def LeafJawPositions(self) -> Optional[List[Decimal]]:
        if "LeafJawPositions" in self._dataset:
            return self._dataset.LeafJawPositions
        return None

    @LeafJawPositions.setter
    def LeafJawPositions(self, value: Optional[List[Decimal]]):
        if value is None:
            if "LeafJawPositions" in self._dataset:
                del self._dataset.LeafJawPositions
        else:
            self._dataset.LeafJawPositions = value
