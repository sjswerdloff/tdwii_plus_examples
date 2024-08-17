from typing import Any, List, Optional

import pydicom


class RangeModulatorSequenceItem:
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
    def RangeModulatorNumber(self) -> Optional[int]:
        if "RangeModulatorNumber" in self._dataset:
            return self._dataset.RangeModulatorNumber
        return None

    @RangeModulatorNumber.setter
    def RangeModulatorNumber(self, value: Optional[int]):
        if value is None:
            if "RangeModulatorNumber" in self._dataset:
                del self._dataset.RangeModulatorNumber
        else:
            self._dataset.RangeModulatorNumber = value

    @property
    def RangeModulatorID(self) -> Optional[str]:
        if "RangeModulatorID" in self._dataset:
            return self._dataset.RangeModulatorID
        return None

    @RangeModulatorID.setter
    def RangeModulatorID(self, value: Optional[str]):
        if value is None:
            if "RangeModulatorID" in self._dataset:
                del self._dataset.RangeModulatorID
        else:
            self._dataset.RangeModulatorID = value

    @property
    def RangeModulatorType(self) -> Optional[str]:
        if "RangeModulatorType" in self._dataset:
            return self._dataset.RangeModulatorType
        return None

    @RangeModulatorType.setter
    def RangeModulatorType(self, value: Optional[str]):
        if value is None:
            if "RangeModulatorType" in self._dataset:
                del self._dataset.RangeModulatorType
        else:
            self._dataset.RangeModulatorType = value

    @property
    def RangeModulatorDescription(self) -> Optional[str]:
        if "RangeModulatorDescription" in self._dataset:
            return self._dataset.RangeModulatorDescription
        return None

    @RangeModulatorDescription.setter
    def RangeModulatorDescription(self, value: Optional[str]):
        if value is None:
            if "RangeModulatorDescription" in self._dataset:
                del self._dataset.RangeModulatorDescription
        else:
            self._dataset.RangeModulatorDescription = value

    @property
    def BeamCurrentModulationID(self) -> Optional[str]:
        if "BeamCurrentModulationID" in self._dataset:
            return self._dataset.BeamCurrentModulationID
        return None

    @BeamCurrentModulationID.setter
    def BeamCurrentModulationID(self, value: Optional[str]):
        if value is None:
            if "BeamCurrentModulationID" in self._dataset:
                del self._dataset.BeamCurrentModulationID
        else:
            self._dataset.BeamCurrentModulationID = value
