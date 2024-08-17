from decimal import Decimal
from typing import Any, List, Optional

import pydicom

from .code_sequence_item import CodeSequenceItem
from .operator_identification_sequence_item import OperatorIdentificationSequenceItem
from .udi_sequence_item import UDISequenceItem


class ContributingEquipmentSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._InstitutionalDepartmentTypeCodeSequence: List[CodeSequenceItem] = []
        self._OperatorIdentificationSequence: List[OperatorIdentificationSequenceItem] = []
        self._UDISequence: List[UDISequenceItem] = []
        self._PurposeOfReferenceCodeSequence: List[CodeSequenceItem] = []

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
    def StationName(self) -> Optional[str]:
        if "StationName" in self._dataset:
            return self._dataset.StationName
        return None

    @StationName.setter
    def StationName(self, value: Optional[str]):
        if value is None:
            if "StationName" in self._dataset:
                del self._dataset.StationName
        else:
            self._dataset.StationName = value

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
    def InstitutionalDepartmentTypeCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "InstitutionalDepartmentTypeCodeSequence" in self._dataset:
            if len(self._InstitutionalDepartmentTypeCodeSequence) == len(
                self._dataset.InstitutionalDepartmentTypeCodeSequence
            ):
                return self._InstitutionalDepartmentTypeCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.InstitutionalDepartmentTypeCodeSequence]
        return None

    @InstitutionalDepartmentTypeCodeSequence.setter
    def InstitutionalDepartmentTypeCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._InstitutionalDepartmentTypeCodeSequence = []
            if "InstitutionalDepartmentTypeCodeSequence" in self._dataset:
                del self._dataset.InstitutionalDepartmentTypeCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError(f"InstitutionalDepartmentTypeCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._InstitutionalDepartmentTypeCodeSequence = value
            if "InstitutionalDepartmentTypeCodeSequence" not in self._dataset:
                self._dataset.InstitutionalDepartmentTypeCodeSequence = pydicom.Sequence()
            self._dataset.InstitutionalDepartmentTypeCodeSequence.clear()
            self._dataset.InstitutionalDepartmentTypeCodeSequence.extend([item.to_dataset() for item in value])

    def add_InstitutionalDepartmentTypeCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError(f"Item must be an instance of CodeSequenceItem")
        self._InstitutionalDepartmentTypeCodeSequence.append(item)
        if "InstitutionalDepartmentTypeCodeSequence" not in self._dataset:
            self._dataset.InstitutionalDepartmentTypeCodeSequence = pydicom.Sequence()
        self._dataset.InstitutionalDepartmentTypeCodeSequence.append(item.to_dataset())

    @property
    def OperatorsName(self) -> Optional[List[str]]:
        if "OperatorsName" in self._dataset:
            return self._dataset.OperatorsName
        return None

    @OperatorsName.setter
    def OperatorsName(self, value: Optional[List[str]]):
        if value is None:
            if "OperatorsName" in self._dataset:
                del self._dataset.OperatorsName
        else:
            self._dataset.OperatorsName = value

    @property
    def OperatorIdentificationSequence(self) -> Optional[List[OperatorIdentificationSequenceItem]]:
        if "OperatorIdentificationSequence" in self._dataset:
            if len(self._OperatorIdentificationSequence) == len(self._dataset.OperatorIdentificationSequence):
                return self._OperatorIdentificationSequence
            else:
                return [OperatorIdentificationSequenceItem(x) for x in self._dataset.OperatorIdentificationSequence]
        return None

    @OperatorIdentificationSequence.setter
    def OperatorIdentificationSequence(self, value: Optional[List[OperatorIdentificationSequenceItem]]):
        if value is None:
            self._OperatorIdentificationSequence = []
            if "OperatorIdentificationSequence" in self._dataset:
                del self._dataset.OperatorIdentificationSequence
        elif not isinstance(value, list) or not all(isinstance(item, OperatorIdentificationSequenceItem) for item in value):
            raise ValueError(f"OperatorIdentificationSequence must be a list of OperatorIdentificationSequenceItem objects")
        else:
            self._OperatorIdentificationSequence = value
            if "OperatorIdentificationSequence" not in self._dataset:
                self._dataset.OperatorIdentificationSequence = pydicom.Sequence()
            self._dataset.OperatorIdentificationSequence.clear()
            self._dataset.OperatorIdentificationSequence.extend([item.to_dataset() for item in value])

    def add_OperatorIdentification(self, item: OperatorIdentificationSequenceItem):
        if not isinstance(item, OperatorIdentificationSequenceItem):
            raise ValueError(f"Item must be an instance of OperatorIdentificationSequenceItem")
        self._OperatorIdentificationSequence.append(item)
        if "OperatorIdentificationSequence" not in self._dataset:
            self._dataset.OperatorIdentificationSequence = pydicom.Sequence()
        self._dataset.OperatorIdentificationSequence.append(item.to_dataset())

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
    def DeviceUID(self) -> Optional[str]:
        if "DeviceUID" in self._dataset:
            return self._dataset.DeviceUID
        return None

    @DeviceUID.setter
    def DeviceUID(self, value: Optional[str]):
        if value is None:
            if "DeviceUID" in self._dataset:
                del self._dataset.DeviceUID
        else:
            self._dataset.DeviceUID = value

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
    def SpatialResolution(self) -> Optional[Decimal]:
        if "SpatialResolution" in self._dataset:
            return self._dataset.SpatialResolution
        return None

    @SpatialResolution.setter
    def SpatialResolution(self, value: Optional[Decimal]):
        if value is None:
            if "SpatialResolution" in self._dataset:
                del self._dataset.SpatialResolution
        else:
            self._dataset.SpatialResolution = value

    @property
    def DateOfLastCalibration(self) -> Optional[List[str]]:
        if "DateOfLastCalibration" in self._dataset:
            return self._dataset.DateOfLastCalibration
        return None

    @DateOfLastCalibration.setter
    def DateOfLastCalibration(self, value: Optional[List[str]]):
        if value is None:
            if "DateOfLastCalibration" in self._dataset:
                del self._dataset.DateOfLastCalibration
        else:
            self._dataset.DateOfLastCalibration = value

    @property
    def TimeOfLastCalibration(self) -> Optional[List[str]]:
        if "TimeOfLastCalibration" in self._dataset:
            return self._dataset.TimeOfLastCalibration
        return None

    @TimeOfLastCalibration.setter
    def TimeOfLastCalibration(self, value: Optional[List[str]]):
        if value is None:
            if "TimeOfLastCalibration" in self._dataset:
                del self._dataset.TimeOfLastCalibration
        else:
            self._dataset.TimeOfLastCalibration = value

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
    def ContributionDateTime(self) -> Optional[str]:
        if "ContributionDateTime" in self._dataset:
            return self._dataset.ContributionDateTime
        return None

    @ContributionDateTime.setter
    def ContributionDateTime(self, value: Optional[str]):
        if value is None:
            if "ContributionDateTime" in self._dataset:
                del self._dataset.ContributionDateTime
        else:
            self._dataset.ContributionDateTime = value

    @property
    def ContributionDescription(self) -> Optional[str]:
        if "ContributionDescription" in self._dataset:
            return self._dataset.ContributionDescription
        return None

    @ContributionDescription.setter
    def ContributionDescription(self, value: Optional[str]):
        if value is None:
            if "ContributionDescription" in self._dataset:
                del self._dataset.ContributionDescription
        else:
            self._dataset.ContributionDescription = value

    @property
    def PurposeOfReferenceCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "PurposeOfReferenceCodeSequence" in self._dataset:
            if len(self._PurposeOfReferenceCodeSequence) == len(self._dataset.PurposeOfReferenceCodeSequence):
                return self._PurposeOfReferenceCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.PurposeOfReferenceCodeSequence]
        return None

    @PurposeOfReferenceCodeSequence.setter
    def PurposeOfReferenceCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._PurposeOfReferenceCodeSequence = []
            if "PurposeOfReferenceCodeSequence" in self._dataset:
                del self._dataset.PurposeOfReferenceCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError(f"PurposeOfReferenceCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._PurposeOfReferenceCodeSequence = value
            if "PurposeOfReferenceCodeSequence" not in self._dataset:
                self._dataset.PurposeOfReferenceCodeSequence = pydicom.Sequence()
            self._dataset.PurposeOfReferenceCodeSequence.clear()
            self._dataset.PurposeOfReferenceCodeSequence.extend([item.to_dataset() for item in value])

    def add_PurposeOfReferenceCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError(f"Item must be an instance of CodeSequenceItem")
        self._PurposeOfReferenceCodeSequence.append(item)
        if "PurposeOfReferenceCodeSequence" not in self._dataset:
            self._dataset.PurposeOfReferenceCodeSequence = pydicom.Sequence()
        self._dataset.PurposeOfReferenceCodeSequence.append(item.to_dataset())
