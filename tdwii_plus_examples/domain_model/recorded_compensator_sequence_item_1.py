from typing import Any, List, Optional  # noqa

import pydicom


class RecordedCompensatorSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def CompensatorID(self) -> Optional[str]:
        if "CompensatorID" in self._dataset:
            return self._dataset.CompensatorID
        return None

    @CompensatorID.setter
    def CompensatorID(self, value: Optional[str]):
        if value is None:
            if "CompensatorID" in self._dataset:
                del self._dataset.CompensatorID
        else:
            self._dataset.CompensatorID = value

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
    def ReferencedCompensatorNumber(self) -> Optional[int]:
        if "ReferencedCompensatorNumber" in self._dataset:
            return self._dataset.ReferencedCompensatorNumber
        return None

    @ReferencedCompensatorNumber.setter
    def ReferencedCompensatorNumber(self, value: Optional[int]):
        if value is None:
            if "ReferencedCompensatorNumber" in self._dataset:
                del self._dataset.ReferencedCompensatorNumber
        else:
            self._dataset.ReferencedCompensatorNumber = value
