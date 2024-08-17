from typing import Any, List, Optional  # noqa

import pydicom


class ReferencedBolusSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ReferencedROINumber(self) -> Optional[int]:
        if "ReferencedROINumber" in self._dataset:
            return self._dataset.ReferencedROINumber
        return None

    @ReferencedROINumber.setter
    def ReferencedROINumber(self, value: Optional[int]):
        if value is None:
            if "ReferencedROINumber" in self._dataset:
                del self._dataset.ReferencedROINumber
        else:
            self._dataset.ReferencedROINumber = value

    @property
    def BolusID(self) -> Optional[str]:
        if "BolusID" in self._dataset:
            return self._dataset.BolusID
        return None

    @BolusID.setter
    def BolusID(self, value: Optional[str]):
        if value is None:
            if "BolusID" in self._dataset:
                del self._dataset.BolusID
        else:
            self._dataset.BolusID = value

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
