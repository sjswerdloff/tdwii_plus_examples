from typing import Any, List, Optional

import pydicom


class BlockSlabSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def BlockSlabNumber(self) -> Optional[int]:
        if "BlockSlabNumber" in self._dataset:
            return self._dataset.BlockSlabNumber
        return None

    @BlockSlabNumber.setter
    def BlockSlabNumber(self, value: Optional[int]):
        if value is None:
            if "BlockSlabNumber" in self._dataset:
                del self._dataset.BlockSlabNumber
        else:
            self._dataset.BlockSlabNumber = value

    @property
    def RadiationBeamBlockSlabThickness(self) -> Optional[float]:
        if "RadiationBeamBlockSlabThickness" in self._dataset:
            return self._dataset.RadiationBeamBlockSlabThickness
        return None

    @RadiationBeamBlockSlabThickness.setter
    def RadiationBeamBlockSlabThickness(self, value: Optional[float]):
        if value is None:
            if "RadiationBeamBlockSlabThickness" in self._dataset:
                del self._dataset.RadiationBeamBlockSlabThickness
        else:
            self._dataset.RadiationBeamBlockSlabThickness = value

    @property
    def DeviceAlternateIdentifier(self) -> Optional[str]:
        if "DeviceAlternateIdentifier" in self._dataset:
            return self._dataset.DeviceAlternateIdentifier
        return None

    @DeviceAlternateIdentifier.setter
    def DeviceAlternateIdentifier(self, value: Optional[str]):
        if value is None:
            if "DeviceAlternateIdentifier" in self._dataset:
                del self._dataset.DeviceAlternateIdentifier
        else:
            self._dataset.DeviceAlternateIdentifier = value

    @property
    def DeviceAlternateIdentifierType(self) -> Optional[str]:
        if "DeviceAlternateIdentifierType" in self._dataset:
            return self._dataset.DeviceAlternateIdentifierType
        return None

    @DeviceAlternateIdentifierType.setter
    def DeviceAlternateIdentifierType(self, value: Optional[str]):
        if value is None:
            if "DeviceAlternateIdentifierType" in self._dataset:
                del self._dataset.DeviceAlternateIdentifierType
        else:
            self._dataset.DeviceAlternateIdentifierType = value

    @property
    def DeviceAlternateIdentifierFormat(self) -> Optional[str]:
        if "DeviceAlternateIdentifierFormat" in self._dataset:
            return self._dataset.DeviceAlternateIdentifierFormat
        return None

    @DeviceAlternateIdentifierFormat.setter
    def DeviceAlternateIdentifierFormat(self, value: Optional[str]):
        if value is None:
            if "DeviceAlternateIdentifierFormat" in self._dataset:
                del self._dataset.DeviceAlternateIdentifierFormat
        else:
            self._dataset.DeviceAlternateIdentifierFormat = value
