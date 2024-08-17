from typing import Any, List, Optional  # noqa

import pydicom

from .code_sequence_item import CodeSequenceItem


class PhysiciansOfRecordIdentificationSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._InstitutionCodeSequence: List[CodeSequenceItem] = []
        self._InstitutionalDepartmentTypeCodeSequence: List[CodeSequenceItem] = []
        self._PersonIdentificationCodeSequence: List[CodeSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

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
            raise ValueError("InstitutionCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._InstitutionCodeSequence = value
            if "InstitutionCodeSequence" not in self._dataset:
                self._dataset.InstitutionCodeSequence = pydicom.Sequence()
            self._dataset.InstitutionCodeSequence.clear()
            self._dataset.InstitutionCodeSequence.extend([item.to_dataset() for item in value])

    def add_InstitutionCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._InstitutionCodeSequence.append(item)
        if "InstitutionCodeSequence" not in self._dataset:
            self._dataset.InstitutionCodeSequence = pydicom.Sequence()
        self._dataset.InstitutionCodeSequence.append(item.to_dataset())

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
            raise ValueError("InstitutionalDepartmentTypeCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._InstitutionalDepartmentTypeCodeSequence = value
            if "InstitutionalDepartmentTypeCodeSequence" not in self._dataset:
                self._dataset.InstitutionalDepartmentTypeCodeSequence = pydicom.Sequence()
            self._dataset.InstitutionalDepartmentTypeCodeSequence.clear()
            self._dataset.InstitutionalDepartmentTypeCodeSequence.extend([item.to_dataset() for item in value])

    def add_InstitutionalDepartmentTypeCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._InstitutionalDepartmentTypeCodeSequence.append(item)
        if "InstitutionalDepartmentTypeCodeSequence" not in self._dataset:
            self._dataset.InstitutionalDepartmentTypeCodeSequence = pydicom.Sequence()
        self._dataset.InstitutionalDepartmentTypeCodeSequence.append(item.to_dataset())

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
            raise ValueError("PersonIdentificationCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._PersonIdentificationCodeSequence = value
            if "PersonIdentificationCodeSequence" not in self._dataset:
                self._dataset.PersonIdentificationCodeSequence = pydicom.Sequence()
            self._dataset.PersonIdentificationCodeSequence.clear()
            self._dataset.PersonIdentificationCodeSequence.extend([item.to_dataset() for item in value])

    def add_PersonIdentificationCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._PersonIdentificationCodeSequence.append(item)
        if "PersonIdentificationCodeSequence" not in self._dataset:
            self._dataset.PersonIdentificationCodeSequence = pydicom.Sequence()
        self._dataset.PersonIdentificationCodeSequence.append(item.to_dataset())

    @property
    def PersonAddress(self) -> Optional[str]:
        if "PersonAddress" in self._dataset:
            return self._dataset.PersonAddress
        return None

    @PersonAddress.setter
    def PersonAddress(self, value: Optional[str]):
        if value is None:
            if "PersonAddress" in self._dataset:
                del self._dataset.PersonAddress
        else:
            self._dataset.PersonAddress = value

    @property
    def PersonTelephoneNumbers(self) -> Optional[List[str]]:
        if "PersonTelephoneNumbers" in self._dataset:
            return self._dataset.PersonTelephoneNumbers
        return None

    @PersonTelephoneNumbers.setter
    def PersonTelephoneNumbers(self, value: Optional[List[str]]):
        if value is None:
            if "PersonTelephoneNumbers" in self._dataset:
                del self._dataset.PersonTelephoneNumbers
        else:
            self._dataset.PersonTelephoneNumbers = value

    @property
    def PersonTelecomInformation(self) -> Optional[str]:
        if "PersonTelecomInformation" in self._dataset:
            return self._dataset.PersonTelecomInformation
        return None

    @PersonTelecomInformation.setter
    def PersonTelecomInformation(self, value: Optional[str]):
        if value is None:
            if "PersonTelecomInformation" in self._dataset:
                del self._dataset.PersonTelecomInformation
        else:
            self._dataset.PersonTelecomInformation = value
