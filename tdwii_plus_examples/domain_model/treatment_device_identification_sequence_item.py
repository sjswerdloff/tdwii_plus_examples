from typing import Any, List, Optional

import pydicom

from .code_sequence_item import CodeSequenceItem
from .udi_sequence_item import UDISequenceItem


class TreatmentDeviceIdentificationSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._UDISequence: List[UDISequenceItem] = []
        self._DeviceTypeCodeSequence: List[CodeSequenceItem] = []

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
    def InstitutionName(self) -> Optional[str]:
        if "InstitutionName" in self._dataset:
            return self._dataset.InstitutionName
        return None

    @InstitutionName.setter
    def InstitutionName(self, value: Optional[str]):
        if value is None:
            if "InstitutionName" in self._dataset:
                del self._dataset.InstitutionName
        else:
            self._dataset.InstitutionName = value

    @property
    def InstitutionAddress(self) -> Optional[str]:
        if "InstitutionAddress" in self._dataset:
            return self._dataset.InstitutionAddress
        return None

    @InstitutionAddress.setter
    def InstitutionAddress(self, value: Optional[str]):
        if value is None:
            if "InstitutionAddress" in self._dataset:
                del self._dataset.InstitutionAddress
        else:
            self._dataset.InstitutionAddress = value

    @property
    def InstitutionalDepartmentName(self) -> Optional[str]:
        if "InstitutionalDepartmentName" in self._dataset:
            return self._dataset.InstitutionalDepartmentName
        return None

    @InstitutionalDepartmentName.setter
    def InstitutionalDepartmentName(self, value: Optional[str]):
        if value is None:
            if "InstitutionalDepartmentName" in self._dataset:
                del self._dataset.InstitutionalDepartmentName
        else:
            self._dataset.InstitutionalDepartmentName = value

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
    def UDISequence(self) -> Optional[List[UDISequenceItem]]:
        if "UDISequence" in self._dataset:
            if len(self._UDISequence) == len(self._dataset.UDISequence):
                return self._UDISequence
            else:
                return [UDISequenceItem(x) for x in self._dataset.UDISequence]
        return None

    @UDISequence.setter
    def UDISequence(self, value: Optional[List[UDISequenceItem]]):
        if value is None:
            self._UDISequence = []
            if "UDISequence" in self._dataset:
                del self._dataset.UDISequence
        elif not isinstance(value, list) or not all(isinstance(item, UDISequenceItem) for item in value):
            raise ValueError(f"UDISequence must be a list of UDISequenceItem objects")
        else:
            self._UDISequence = value
            if "UDISequence" not in self._dataset:
                self._dataset.UDISequence = pydicom.Sequence()
            self._dataset.UDISequence.clear()
            self._dataset.UDISequence.extend([item.to_dataset() for item in value])

    def add_UDI(self, item: UDISequenceItem):
        if not isinstance(item, UDISequenceItem):
            raise ValueError(f"Item must be an instance of UDISequenceItem")
        self._UDISequence.append(item)
        if "UDISequence" not in self._dataset:
            self._dataset.UDISequence = pydicom.Sequence()
        self._dataset.UDISequence.append(item.to_dataset())

    @property
    def ManufacturerDeviceClassUID(self) -> Optional[List[str]]:
        if "ManufacturerDeviceClassUID" in self._dataset:
            return self._dataset.ManufacturerDeviceClassUID
        return None

    @ManufacturerDeviceClassUID.setter
    def ManufacturerDeviceClassUID(self, value: Optional[List[str]]):
        if value is None:
            if "ManufacturerDeviceClassUID" in self._dataset:
                del self._dataset.ManufacturerDeviceClassUID
        else:
            self._dataset.ManufacturerDeviceClassUID = value

    @property
    def SoftwareVersions(self) -> Optional[List[str]]:
        if "SoftwareVersions" in self._dataset:
            return self._dataset.SoftwareVersions
        return None

    @SoftwareVersions.setter
    def SoftwareVersions(self, value: Optional[List[str]]):
        if value is None:
            if "SoftwareVersions" in self._dataset:
                del self._dataset.SoftwareVersions
        else:
            self._dataset.SoftwareVersions = value

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
    def DateOfInstallation(self) -> Optional[str]:
        if "DateOfInstallation" in self._dataset:
            return self._dataset.DateOfInstallation
        return None

    @DateOfInstallation.setter
    def DateOfInstallation(self, value: Optional[str]):
        if value is None:
            if "DateOfInstallation" in self._dataset:
                del self._dataset.DateOfInstallation
        else:
            self._dataset.DateOfInstallation = value

    @property
    def LongDeviceDescription(self) -> Optional[str]:
        if "LongDeviceDescription" in self._dataset:
            return self._dataset.LongDeviceDescription
        return None

    @LongDeviceDescription.setter
    def LongDeviceDescription(self, value: Optional[str]):
        if value is None:
            if "LongDeviceDescription" in self._dataset:
                del self._dataset.LongDeviceDescription
        else:
            self._dataset.LongDeviceDescription = value

    @property
    def ManufacturerModelVersion(self) -> Optional[str]:
        if "ManufacturerModelVersion" in self._dataset:
            return self._dataset.ManufacturerModelVersion
        return None

    @ManufacturerModelVersion.setter
    def ManufacturerModelVersion(self, value: Optional[str]):
        if value is None:
            if "ManufacturerModelVersion" in self._dataset:
                del self._dataset.ManufacturerModelVersion
        else:
            self._dataset.ManufacturerModelVersion = value

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

    @property
    def DeviceLabel(self) -> Optional[str]:
        if "DeviceLabel" in self._dataset:
            return self._dataset.DeviceLabel
        return None

    @DeviceLabel.setter
    def DeviceLabel(self, value: Optional[str]):
        if value is None:
            if "DeviceLabel" in self._dataset:
                del self._dataset.DeviceLabel
        else:
            self._dataset.DeviceLabel = value

    @property
    def DeviceTypeCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "DeviceTypeCodeSequence" in self._dataset:
            if len(self._DeviceTypeCodeSequence) == len(self._dataset.DeviceTypeCodeSequence):
                return self._DeviceTypeCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.DeviceTypeCodeSequence]
        return None

    @DeviceTypeCodeSequence.setter
    def DeviceTypeCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._DeviceTypeCodeSequence = []
            if "DeviceTypeCodeSequence" in self._dataset:
                del self._dataset.DeviceTypeCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError(f"DeviceTypeCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._DeviceTypeCodeSequence = value
            if "DeviceTypeCodeSequence" not in self._dataset:
                self._dataset.DeviceTypeCodeSequence = pydicom.Sequence()
            self._dataset.DeviceTypeCodeSequence.clear()
            self._dataset.DeviceTypeCodeSequence.extend([item.to_dataset() for item in value])

    def add_DeviceTypeCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError(f"Item must be an instance of CodeSequenceItem")
        self._DeviceTypeCodeSequence.append(item)
        if "DeviceTypeCodeSequence" not in self._dataset:
            self._dataset.DeviceTypeCodeSequence = pydicom.Sequence()
        self._dataset.DeviceTypeCodeSequence.append(item.to_dataset())

    @property
    def ManufacturerDeviceIdentifier(self) -> Optional[str]:
        if "ManufacturerDeviceIdentifier" in self._dataset:
            return self._dataset.ManufacturerDeviceIdentifier
        return None

    @ManufacturerDeviceIdentifier.setter
    def ManufacturerDeviceIdentifier(self, value: Optional[str]):
        if value is None:
            if "ManufacturerDeviceIdentifier" in self._dataset:
                del self._dataset.ManufacturerDeviceIdentifier
        else:
            self._dataset.ManufacturerDeviceIdentifier = value
