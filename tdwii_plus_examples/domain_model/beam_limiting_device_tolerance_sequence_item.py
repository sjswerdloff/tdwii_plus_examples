from decimal import Decimal
from typing import Any, List, Optional

import pydicom


class BeamLimitingDeviceToleranceSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def BeamLimitingDevicePositionTolerance(self) -> Optional[Decimal]:
        if "BeamLimitingDevicePositionTolerance" in self._dataset:
            return self._dataset.BeamLimitingDevicePositionTolerance
        return None

    @BeamLimitingDevicePositionTolerance.setter
    def BeamLimitingDevicePositionTolerance(self, value: Optional[Decimal]):
        if value is None:
            if "BeamLimitingDevicePositionTolerance" in self._dataset:
                del self._dataset.BeamLimitingDevicePositionTolerance
        else:
            self._dataset.BeamLimitingDevicePositionTolerance = value

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
