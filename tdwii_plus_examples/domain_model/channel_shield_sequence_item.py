from decimal import Decimal
from typing import Any, List, Optional  # noqa

import pydicom


class ChannelShieldSequenceItem:
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
    def ChannelShieldNumber(self) -> Optional[int]:
        if "ChannelShieldNumber" in self._dataset:
            return self._dataset.ChannelShieldNumber
        return None

    @ChannelShieldNumber.setter
    def ChannelShieldNumber(self, value: Optional[int]):
        if value is None:
            if "ChannelShieldNumber" in self._dataset:
                del self._dataset.ChannelShieldNumber
        else:
            self._dataset.ChannelShieldNumber = value

    @property
    def ChannelShieldID(self) -> Optional[str]:
        if "ChannelShieldID" in self._dataset:
            return self._dataset.ChannelShieldID
        return None

    @ChannelShieldID.setter
    def ChannelShieldID(self, value: Optional[str]):
        if value is None:
            if "ChannelShieldID" in self._dataset:
                del self._dataset.ChannelShieldID
        else:
            self._dataset.ChannelShieldID = value

    @property
    def ChannelShieldName(self) -> Optional[str]:
        if "ChannelShieldName" in self._dataset:
            return self._dataset.ChannelShieldName
        return None

    @ChannelShieldName.setter
    def ChannelShieldName(self, value: Optional[str]):
        if value is None:
            if "ChannelShieldName" in self._dataset:
                del self._dataset.ChannelShieldName
        else:
            self._dataset.ChannelShieldName = value

    @property
    def ChannelShieldNominalThickness(self) -> Optional[Decimal]:
        if "ChannelShieldNominalThickness" in self._dataset:
            return self._dataset.ChannelShieldNominalThickness
        return None

    @ChannelShieldNominalThickness.setter
    def ChannelShieldNominalThickness(self, value: Optional[Decimal]):
        if value is None:
            if "ChannelShieldNominalThickness" in self._dataset:
                del self._dataset.ChannelShieldNominalThickness
        else:
            self._dataset.ChannelShieldNominalThickness = value

    @property
    def ChannelShieldNominalTransmission(self) -> Optional[Decimal]:
        if "ChannelShieldNominalTransmission" in self._dataset:
            return self._dataset.ChannelShieldNominalTransmission
        return None

    @ChannelShieldNominalTransmission.setter
    def ChannelShieldNominalTransmission(self, value: Optional[Decimal]):
        if value is None:
            if "ChannelShieldNominalTransmission" in self._dataset:
                del self._dataset.ChannelShieldNominalTransmission
        else:
            self._dataset.ChannelShieldNominalTransmission = value
