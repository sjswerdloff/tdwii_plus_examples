from typing import Any, List, Optional  # noqa

import pydicom


class BeamLimitingDeviceLeafPairsSequenceItem:
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
