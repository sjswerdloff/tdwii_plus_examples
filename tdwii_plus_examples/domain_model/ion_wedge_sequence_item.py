from decimal import Decimal
from typing import Any, List, Optional  # noqa

import pydicom


class IonWedgeSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def WedgeNumber(self) -> Optional[int]:
        if "WedgeNumber" in self._dataset:
            return self._dataset.WedgeNumber
        return None

    @WedgeNumber.setter
    def WedgeNumber(self, value: Optional[int]):
        if value is None:
            if "WedgeNumber" in self._dataset:
                del self._dataset.WedgeNumber
        else:
            self._dataset.WedgeNumber = value

    @property
    def WedgeType(self) -> Optional[str]:
        if "WedgeType" in self._dataset:
            return self._dataset.WedgeType
        return None

    @WedgeType.setter
    def WedgeType(self, value: Optional[str]):
        if value is None:
            if "WedgeType" in self._dataset:
                del self._dataset.WedgeType
        else:
            self._dataset.WedgeType = value

    @property
    def WedgeID(self) -> Optional[str]:
        if "WedgeID" in self._dataset:
            return self._dataset.WedgeID
        return None

    @WedgeID.setter
    def WedgeID(self, value: Optional[str]):
        if value is None:
            if "WedgeID" in self._dataset:
                del self._dataset.WedgeID
        else:
            self._dataset.WedgeID = value

    @property
    def WedgeAngle(self) -> Optional[int]:
        if "WedgeAngle" in self._dataset:
            return self._dataset.WedgeAngle
        return None

    @WedgeAngle.setter
    def WedgeAngle(self, value: Optional[int]):
        if value is None:
            if "WedgeAngle" in self._dataset:
                del self._dataset.WedgeAngle
        else:
            self._dataset.WedgeAngle = value

    @property
    def WedgeOrientation(self) -> Optional[Decimal]:
        if "WedgeOrientation" in self._dataset:
            return self._dataset.WedgeOrientation
        return None

    @WedgeOrientation.setter
    def WedgeOrientation(self, value: Optional[Decimal]):
        if value is None:
            if "WedgeOrientation" in self._dataset:
                del self._dataset.WedgeOrientation
        else:
            self._dataset.WedgeOrientation = value

    @property
    def IsocenterToWedgeTrayDistance(self) -> Optional[float]:
        if "IsocenterToWedgeTrayDistance" in self._dataset:
            return self._dataset.IsocenterToWedgeTrayDistance
        return None

    @IsocenterToWedgeTrayDistance.setter
    def IsocenterToWedgeTrayDistance(self, value: Optional[float]):
        if value is None:
            if "IsocenterToWedgeTrayDistance" in self._dataset:
                del self._dataset.IsocenterToWedgeTrayDistance
        else:
            self._dataset.IsocenterToWedgeTrayDistance = value

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
