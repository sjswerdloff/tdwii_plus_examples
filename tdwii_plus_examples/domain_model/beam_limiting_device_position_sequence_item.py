from decimal import Decimal
from typing import Any, List, Optional

import pydicom


class BeamLimitingDevicePositionSequenceItem:
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
