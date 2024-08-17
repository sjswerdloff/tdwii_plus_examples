from decimal import Decimal
from typing import Any, List, Optional  # noqa

import pydicom

from .code_sequence_item import CodeSequenceItem


class DeviceSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._EquivalentCodeSequence: List[CodeSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def Manufacturer(self) -> Optional[str]:
        if "Manufacturer" in self._dataset:
            return self._dataset.Manufacturer
        return None

    @Manufacturer.setter
    def Manufacturer(self, value: Optional[str]):
        if value is None:
            if "Manufacturer" in self._dataset:
                del self._dataset.Manufacturer
        else:
            self._dataset.Manufacturer = value

    @property
    def CodeValue(self) -> Optional[str]:
        if "CodeValue" in self._dataset:
            return self._dataset.CodeValue
        return None

    @CodeValue.setter
    def CodeValue(self, value: Optional[str]):
        if value is None:
            if "CodeValue" in self._dataset:
                del self._dataset.CodeValue
        else:
            self._dataset.CodeValue = value

    @property
    def CodingSchemeDesignator(self) -> Optional[str]:
        if "CodingSchemeDesignator" in self._dataset:
            return self._dataset.CodingSchemeDesignator
        return None

    @CodingSchemeDesignator.setter
    def CodingSchemeDesignator(self, value: Optional[str]):
        if value is None:
            if "CodingSchemeDesignator" in self._dataset:
                del self._dataset.CodingSchemeDesignator
        else:
            self._dataset.CodingSchemeDesignator = value

    @property
    def CodingSchemeVersion(self) -> Optional[str]:
        if "CodingSchemeVersion" in self._dataset:
            return self._dataset.CodingSchemeVersion
        return None

    @CodingSchemeVersion.setter
    def CodingSchemeVersion(self, value: Optional[str]):
        if value is None:
            if "CodingSchemeVersion" in self._dataset:
                del self._dataset.CodingSchemeVersion
        else:
            self._dataset.CodingSchemeVersion = value

    @property
    def CodeMeaning(self) -> Optional[str]:
        if "CodeMeaning" in self._dataset:
            return self._dataset.CodeMeaning
        return None

    @CodeMeaning.setter
    def CodeMeaning(self, value: Optional[str]):
        if value is None:
            if "CodeMeaning" in self._dataset:
                del self._dataset.CodeMeaning
        else:
            self._dataset.CodeMeaning = value

    @property
    def MappingResource(self) -> Optional[str]:
        if "MappingResource" in self._dataset:
            return self._dataset.MappingResource
        return None

    @MappingResource.setter
    def MappingResource(self, value: Optional[str]):
        if value is None:
            if "MappingResource" in self._dataset:
                del self._dataset.MappingResource
        else:
            self._dataset.MappingResource = value

    @property
    def ContextGroupVersion(self) -> Optional[str]:
        if "ContextGroupVersion" in self._dataset:
            return self._dataset.ContextGroupVersion
        return None

    @ContextGroupVersion.setter
    def ContextGroupVersion(self, value: Optional[str]):
        if value is None:
            if "ContextGroupVersion" in self._dataset:
                del self._dataset.ContextGroupVersion
        else:
            self._dataset.ContextGroupVersion = value

    @property
    def ContextGroupLocalVersion(self) -> Optional[str]:
        if "ContextGroupLocalVersion" in self._dataset:
            return self._dataset.ContextGroupLocalVersion
        return None

    @ContextGroupLocalVersion.setter
    def ContextGroupLocalVersion(self, value: Optional[str]):
        if value is None:
            if "ContextGroupLocalVersion" in self._dataset:
                del self._dataset.ContextGroupLocalVersion
        else:
            self._dataset.ContextGroupLocalVersion = value

    @property
    def ContextGroupExtensionFlag(self) -> Optional[str]:
        if "ContextGroupExtensionFlag" in self._dataset:
            return self._dataset.ContextGroupExtensionFlag
        return None

    @ContextGroupExtensionFlag.setter
    def ContextGroupExtensionFlag(self, value: Optional[str]):
        if value is None:
            if "ContextGroupExtensionFlag" in self._dataset:
                del self._dataset.ContextGroupExtensionFlag
        else:
            self._dataset.ContextGroupExtensionFlag = value

    @property
    def ContextGroupExtensionCreatorUID(self) -> Optional[str]:
        if "ContextGroupExtensionCreatorUID" in self._dataset:
            return self._dataset.ContextGroupExtensionCreatorUID
        return None

    @ContextGroupExtensionCreatorUID.setter
    def ContextGroupExtensionCreatorUID(self, value: Optional[str]):
        if value is None:
            if "ContextGroupExtensionCreatorUID" in self._dataset:
                del self._dataset.ContextGroupExtensionCreatorUID
        else:
            self._dataset.ContextGroupExtensionCreatorUID = value

    @property
    def ContextIdentifier(self) -> Optional[str]:
        if "ContextIdentifier" in self._dataset:
            return self._dataset.ContextIdentifier
        return None

    @ContextIdentifier.setter
    def ContextIdentifier(self, value: Optional[str]):
        if value is None:
            if "ContextIdentifier" in self._dataset:
                del self._dataset.ContextIdentifier
        else:
            self._dataset.ContextIdentifier = value

    @property
    def ContextUID(self) -> Optional[str]:
        if "ContextUID" in self._dataset:
            return self._dataset.ContextUID
        return None

    @ContextUID.setter
    def ContextUID(self, value: Optional[str]):
        if value is None:
            if "ContextUID" in self._dataset:
                del self._dataset.ContextUID
        else:
            self._dataset.ContextUID = value

    @property
    def MappingResourceUID(self) -> Optional[str]:
        if "MappingResourceUID" in self._dataset:
            return self._dataset.MappingResourceUID
        return None

    @MappingResourceUID.setter
    def MappingResourceUID(self, value: Optional[str]):
        if value is None:
            if "MappingResourceUID" in self._dataset:
                del self._dataset.MappingResourceUID
        else:
            self._dataset.MappingResourceUID = value

    @property
    def LongCodeValue(self) -> Optional[str]:
        if "LongCodeValue" in self._dataset:
            return self._dataset.LongCodeValue
        return None

    @LongCodeValue.setter
    def LongCodeValue(self, value: Optional[str]):
        if value is None:
            if "LongCodeValue" in self._dataset:
                del self._dataset.LongCodeValue
        else:
            self._dataset.LongCodeValue = value

    @property
    def URNCodeValue(self) -> Optional[str]:
        if "URNCodeValue" in self._dataset:
            return self._dataset.URNCodeValue
        return None

    @URNCodeValue.setter
    def URNCodeValue(self, value: Optional[str]):
        if value is None:
            if "URNCodeValue" in self._dataset:
                del self._dataset.URNCodeValue
        else:
            self._dataset.URNCodeValue = value

    @property
    def EquivalentCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "EquivalentCodeSequence" in self._dataset:
            if len(self._EquivalentCodeSequence) == len(self._dataset.EquivalentCodeSequence):
                return self._EquivalentCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.EquivalentCodeSequence]
        return None

    @EquivalentCodeSequence.setter
    def EquivalentCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._EquivalentCodeSequence = []
            if "EquivalentCodeSequence" in self._dataset:
                del self._dataset.EquivalentCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("EquivalentCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._EquivalentCodeSequence = value
            if "EquivalentCodeSequence" not in self._dataset:
                self._dataset.EquivalentCodeSequence = pydicom.Sequence()
            self._dataset.EquivalentCodeSequence.clear()
            self._dataset.EquivalentCodeSequence.extend([item.to_dataset() for item in value])

    def add_EquivalentCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._EquivalentCodeSequence.append(item)
        if "EquivalentCodeSequence" not in self._dataset:
            self._dataset.EquivalentCodeSequence = pydicom.Sequence()
        self._dataset.EquivalentCodeSequence.append(item.to_dataset())

    @property
    def MappingResourceName(self) -> Optional[str]:
        if "MappingResourceName" in self._dataset:
            return self._dataset.MappingResourceName
        return None

    @MappingResourceName.setter
    def MappingResourceName(self, value: Optional[str]):
        if value is None:
            if "MappingResourceName" in self._dataset:
                del self._dataset.MappingResourceName
        else:
            self._dataset.MappingResourceName = value

    @property
    def ManufacturerModelName(self) -> Optional[str]:
        if "ManufacturerModelName" in self._dataset:
            return self._dataset.ManufacturerModelName
        return None

    @ManufacturerModelName.setter
    def ManufacturerModelName(self, value: Optional[str]):
        if value is None:
            if "ManufacturerModelName" in self._dataset:
                del self._dataset.ManufacturerModelName
        else:
            self._dataset.ManufacturerModelName = value

    @property
    def DeviceSerialNumber(self) -> Optional[str]:
        if "DeviceSerialNumber" in self._dataset:
            return self._dataset.DeviceSerialNumber
        return None

    @DeviceSerialNumber.setter
    def DeviceSerialNumber(self, value: Optional[str]):
        if value is None:
            if "DeviceSerialNumber" in self._dataset:
                del self._dataset.DeviceSerialNumber
        else:
            self._dataset.DeviceSerialNumber = value

    @property
    def DeviceID(self) -> Optional[str]:
        if "DeviceID" in self._dataset:
            return self._dataset.DeviceID
        return None

    @DeviceID.setter
    def DeviceID(self, value: Optional[str]):
        if value is None:
            if "DeviceID" in self._dataset:
                del self._dataset.DeviceID
        else:
            self._dataset.DeviceID = value

    @property
    def DateOfManufacture(self) -> Optional[str]:
        if "DateOfManufacture" in self._dataset:
            return self._dataset.DateOfManufacture
        return None

    @DateOfManufacture.setter
    def DateOfManufacture(self, value: Optional[str]):
        if value is None:
            if "DateOfManufacture" in self._dataset:
                del self._dataset.DateOfManufacture
        else:
            self._dataset.DateOfManufacture = value

    @property
    def DeviceLength(self) -> Optional[Decimal]:
        if "DeviceLength" in self._dataset:
            return self._dataset.DeviceLength
        return None

    @DeviceLength.setter
    def DeviceLength(self, value: Optional[Decimal]):
        if value is None:
            if "DeviceLength" in self._dataset:
                del self._dataset.DeviceLength
        else:
            self._dataset.DeviceLength = value

    @property
    def DeviceDiameter(self) -> Optional[Decimal]:
        if "DeviceDiameter" in self._dataset:
            return self._dataset.DeviceDiameter
        return None

    @DeviceDiameter.setter
    def DeviceDiameter(self, value: Optional[Decimal]):
        if value is None:
            if "DeviceDiameter" in self._dataset:
                del self._dataset.DeviceDiameter
        else:
            self._dataset.DeviceDiameter = value

    @property
    def DeviceDiameterUnits(self) -> Optional[str]:
        if "DeviceDiameterUnits" in self._dataset:
            return self._dataset.DeviceDiameterUnits
        return None

    @DeviceDiameterUnits.setter
    def DeviceDiameterUnits(self, value: Optional[str]):
        if value is None:
            if "DeviceDiameterUnits" in self._dataset:
                del self._dataset.DeviceDiameterUnits
        else:
            self._dataset.DeviceDiameterUnits = value

    @property
    def DeviceVolume(self) -> Optional[Decimal]:
        if "DeviceVolume" in self._dataset:
            return self._dataset.DeviceVolume
        return None

    @DeviceVolume.setter
    def DeviceVolume(self, value: Optional[Decimal]):
        if value is None:
            if "DeviceVolume" in self._dataset:
                del self._dataset.DeviceVolume
        else:
            self._dataset.DeviceVolume = value

    @property
    def InterMarkerDistance(self) -> Optional[Decimal]:
        if "InterMarkerDistance" in self._dataset:
            return self._dataset.InterMarkerDistance
        return None

    @InterMarkerDistance.setter
    def InterMarkerDistance(self, value: Optional[Decimal]):
        if value is None:
            if "InterMarkerDistance" in self._dataset:
                del self._dataset.InterMarkerDistance
        else:
            self._dataset.InterMarkerDistance = value

    @property
    def DeviceDescription(self) -> Optional[str]:
        if "DeviceDescription" in self._dataset:
            return self._dataset.DeviceDescription
        return None

    @DeviceDescription.setter
    def DeviceDescription(self, value: Optional[str]):
        if value is None:
            if "DeviceDescription" in self._dataset:
                del self._dataset.DeviceDescription
        else:
            self._dataset.DeviceDescription = value
