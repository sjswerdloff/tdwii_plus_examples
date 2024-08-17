from typing import Any, List, Optional

import pydicom


class MRTransmitCoilSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def TransmitCoilName(self) -> Optional[str]:
        if "TransmitCoilName" in self._dataset:
            return self._dataset.TransmitCoilName
        return None

    @TransmitCoilName.setter
    def TransmitCoilName(self, value: Optional[str]):
        if value is None:
            if "TransmitCoilName" in self._dataset:
                del self._dataset.TransmitCoilName
        else:
            self._dataset.TransmitCoilName = value

    @property
    def TransmitCoilManufacturerName(self) -> Optional[str]:
        if "TransmitCoilManufacturerName" in self._dataset:
            return self._dataset.TransmitCoilManufacturerName
        return None

    @TransmitCoilManufacturerName.setter
    def TransmitCoilManufacturerName(self, value: Optional[str]):
        if value is None:
            if "TransmitCoilManufacturerName" in self._dataset:
                del self._dataset.TransmitCoilManufacturerName
        else:
            self._dataset.TransmitCoilManufacturerName = value

    @property
    def TransmitCoilType(self) -> Optional[str]:
        if "TransmitCoilType" in self._dataset:
            return self._dataset.TransmitCoilType
        return None

    @TransmitCoilType.setter
    def TransmitCoilType(self, value: Optional[str]):
        if value is None:
            if "TransmitCoilType" in self._dataset:
                del self._dataset.TransmitCoilType
        else:
            self._dataset.TransmitCoilType = value
