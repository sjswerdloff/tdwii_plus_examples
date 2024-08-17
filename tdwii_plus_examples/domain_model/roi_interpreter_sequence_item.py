from typing import Any, List, Optional

import pydicom

from .code_sequence_item import CodeSequenceItem


class ROIInterpreterSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._InstitutionCodeSequence: List[CodeSequenceItem] = []
        self._InstitutionalDepartmentTypeCodeSequence: List[CodeSequenceItem] = []
        self._PersonIdentificationCodeSequence: List[CodeSequenceItem] = []
        self._OrganizationalRoleCodeSequence: List[CodeSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def StationAETitle(self) -> Optional[str]:
        if "StationAETitle" in self._dataset:
            return self._dataset.StationAETitle
        return None

    @StationAETitle.setter
    def StationAETitle(self, value: Optional[str]):
        if value is None:
            if "StationAETitle" in self._dataset:
                del self._dataset.StationAETitle
        else:
            self._dataset.StationAETitle = value

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
    def InstitutionCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "InstitutionCodeSequence" in self._dataset:
            if len(self._InstitutionCodeSequence) == len(self._dataset.InstitutionCodeSequence):
                return self._InstitutionCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.InstitutionCodeSequence]
        return None

    @InstitutionCodeSequence.setter
    def InstitutionCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._InstitutionCodeSequence = []
            if "InstitutionCodeSequence" in self._dataset:
                del self._dataset.InstitutionCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError(f"InstitutionCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._InstitutionCodeSequence = value
            if "InstitutionCodeSequence" not in self._dataset:
                self._dataset.InstitutionCodeSequence = pydicom.Sequence()
            self._dataset.InstitutionCodeSequence.clear()
            self._dataset.InstitutionCodeSequence.extend([item.to_dataset() for item in value])

    def add_InstitutionCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError(f"Item must be an instance of CodeSequenceItem")
        self._InstitutionCodeSequence.append(item)
        if "InstitutionCodeSequence" not in self._dataset:
            self._dataset.InstitutionCodeSequence = pydicom.Sequence()
        self._dataset.InstitutionCodeSequence.append(item.to_dataset())

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
    def PersonIdentificationCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "PersonIdentificationCodeSequence" in self._dataset:
            if len(self._PersonIdentificationCodeSequence) == len(self._dataset.PersonIdentificationCodeSequence):
                return self._PersonIdentificationCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.PersonIdentificationCodeSequence]
        return None

    @PersonIdentificationCodeSequence.setter
    def PersonIdentificationCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._PersonIdentificationCodeSequence = []
            if "PersonIdentificationCodeSequence" in self._dataset:
                del self._dataset.PersonIdentificationCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError(f"PersonIdentificationCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._PersonIdentificationCodeSequence = value
            if "PersonIdentificationCodeSequence" not in self._dataset:
                self._dataset.PersonIdentificationCodeSequence = pydicom.Sequence()
            self._dataset.PersonIdentificationCodeSequence.clear()
            self._dataset.PersonIdentificationCodeSequence.extend([item.to_dataset() for item in value])

    def add_PersonIdentificationCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError(f"Item must be an instance of CodeSequenceItem")
        self._PersonIdentificationCodeSequence.append(item)
        if "PersonIdentificationCodeSequence" not in self._dataset:
            self._dataset.PersonIdentificationCodeSequence = pydicom.Sequence()
        self._dataset.PersonIdentificationCodeSequence.append(item.to_dataset())

    @property
    def ObserverType(self) -> Optional[str]:
        if "ObserverType" in self._dataset:
            return self._dataset.ObserverType
        return None

    @ObserverType.setter
    def ObserverType(self, value: Optional[str]):
        if value is None:
            if "ObserverType" in self._dataset:
                del self._dataset.ObserverType
        else:
            self._dataset.ObserverType = value

    @property
    def PersonName(self) -> Optional[str]:
        if "PersonName" in self._dataset:
            return self._dataset.PersonName
        return None

    @PersonName.setter
    def PersonName(self, value: Optional[str]):
        if value is None:
            if "PersonName" in self._dataset:
                del self._dataset.PersonName
        else:
            self._dataset.PersonName = value

    @property
    def OrganizationalRoleCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "OrganizationalRoleCodeSequence" in self._dataset:
            if len(self._OrganizationalRoleCodeSequence) == len(self._dataset.OrganizationalRoleCodeSequence):
                return self._OrganizationalRoleCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.OrganizationalRoleCodeSequence]
        return None

    @OrganizationalRoleCodeSequence.setter
    def OrganizationalRoleCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._OrganizationalRoleCodeSequence = []
            if "OrganizationalRoleCodeSequence" in self._dataset:
                del self._dataset.OrganizationalRoleCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError(f"OrganizationalRoleCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._OrganizationalRoleCodeSequence = value
            if "OrganizationalRoleCodeSequence" not in self._dataset:
                self._dataset.OrganizationalRoleCodeSequence = pydicom.Sequence()
            self._dataset.OrganizationalRoleCodeSequence.clear()
            self._dataset.OrganizationalRoleCodeSequence.extend([item.to_dataset() for item in value])

    def add_OrganizationalRoleCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError(f"Item must be an instance of CodeSequenceItem")
        self._OrganizationalRoleCodeSequence.append(item)
        if "OrganizationalRoleCodeSequence" not in self._dataset:
            self._dataset.OrganizationalRoleCodeSequence = pydicom.Sequence()
        self._dataset.OrganizationalRoleCodeSequence.append(item.to_dataset())
