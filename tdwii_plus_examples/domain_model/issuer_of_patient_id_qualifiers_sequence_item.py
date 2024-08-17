from typing import Any, List, Optional  # noqa

import pydicom

from .assigning_facility_sequence_item import AssigningFacilitySequenceItem
from .code_sequence_item import CodeSequenceItem


class IssuerOfPatientIDQualifiersSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._AssigningFacilitySequence: List[AssigningFacilitySequenceItem] = []
        self._AssigningJurisdictionCodeSequence: List[CodeSequenceItem] = []
        self._AssigningAgencyOrDepartmentCodeSequence: List[CodeSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def UniversalEntityID(self) -> Optional[str]:
        if "UniversalEntityID" in self._dataset:
            return self._dataset.UniversalEntityID
        return None

    @UniversalEntityID.setter
    def UniversalEntityID(self, value: Optional[str]):
        if value is None:
            if "UniversalEntityID" in self._dataset:
                del self._dataset.UniversalEntityID
        else:
            self._dataset.UniversalEntityID = value

    @property
    def UniversalEntityIDType(self) -> Optional[str]:
        if "UniversalEntityIDType" in self._dataset:
            return self._dataset.UniversalEntityIDType
        return None

    @UniversalEntityIDType.setter
    def UniversalEntityIDType(self, value: Optional[str]):
        if value is None:
            if "UniversalEntityIDType" in self._dataset:
                del self._dataset.UniversalEntityIDType
        else:
            self._dataset.UniversalEntityIDType = value

    @property
    def IdentifierTypeCode(self) -> Optional[str]:
        if "IdentifierTypeCode" in self._dataset:
            return self._dataset.IdentifierTypeCode
        return None

    @IdentifierTypeCode.setter
    def IdentifierTypeCode(self, value: Optional[str]):
        if value is None:
            if "IdentifierTypeCode" in self._dataset:
                del self._dataset.IdentifierTypeCode
        else:
            self._dataset.IdentifierTypeCode = value

    @property
    def AssigningFacilitySequence(self) -> Optional[List[AssigningFacilitySequenceItem]]:
        if "AssigningFacilitySequence" in self._dataset:
            if len(self._AssigningFacilitySequence) == len(self._dataset.AssigningFacilitySequence):
                return self._AssigningFacilitySequence
            else:
                return [AssigningFacilitySequenceItem(x) for x in self._dataset.AssigningFacilitySequence]
        return None

    @AssigningFacilitySequence.setter
    def AssigningFacilitySequence(self, value: Optional[List[AssigningFacilitySequenceItem]]):
        if value is None:
            self._AssigningFacilitySequence = []
            if "AssigningFacilitySequence" in self._dataset:
                del self._dataset.AssigningFacilitySequence
        elif not isinstance(value, list) or not all(isinstance(item, AssigningFacilitySequenceItem) for item in value):
            raise ValueError("AssigningFacilitySequence must be a list of AssigningFacilitySequenceItem objects")
        else:
            self._AssigningFacilitySequence = value
            if "AssigningFacilitySequence" not in self._dataset:
                self._dataset.AssigningFacilitySequence = pydicom.Sequence()
            self._dataset.AssigningFacilitySequence.clear()
            self._dataset.AssigningFacilitySequence.extend([item.to_dataset() for item in value])

    def add_AssigningFacility(self, item: AssigningFacilitySequenceItem):
        if not isinstance(item, AssigningFacilitySequenceItem):
            raise ValueError("Item must be an instance of AssigningFacilitySequenceItem")
        self._AssigningFacilitySequence.append(item)
        if "AssigningFacilitySequence" not in self._dataset:
            self._dataset.AssigningFacilitySequence = pydicom.Sequence()
        self._dataset.AssigningFacilitySequence.append(item.to_dataset())

    @property
    def AssigningJurisdictionCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "AssigningJurisdictionCodeSequence" in self._dataset:
            if len(self._AssigningJurisdictionCodeSequence) == len(self._dataset.AssigningJurisdictionCodeSequence):
                return self._AssigningJurisdictionCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.AssigningJurisdictionCodeSequence]
        return None

    @AssigningJurisdictionCodeSequence.setter
    def AssigningJurisdictionCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._AssigningJurisdictionCodeSequence = []
            if "AssigningJurisdictionCodeSequence" in self._dataset:
                del self._dataset.AssigningJurisdictionCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("AssigningJurisdictionCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._AssigningJurisdictionCodeSequence = value
            if "AssigningJurisdictionCodeSequence" not in self._dataset:
                self._dataset.AssigningJurisdictionCodeSequence = pydicom.Sequence()
            self._dataset.AssigningJurisdictionCodeSequence.clear()
            self._dataset.AssigningJurisdictionCodeSequence.extend([item.to_dataset() for item in value])

    def add_AssigningJurisdictionCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._AssigningJurisdictionCodeSequence.append(item)
        if "AssigningJurisdictionCodeSequence" not in self._dataset:
            self._dataset.AssigningJurisdictionCodeSequence = pydicom.Sequence()
        self._dataset.AssigningJurisdictionCodeSequence.append(item.to_dataset())

    @property
    def AssigningAgencyOrDepartmentCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "AssigningAgencyOrDepartmentCodeSequence" in self._dataset:
            if len(self._AssigningAgencyOrDepartmentCodeSequence) == len(
                self._dataset.AssigningAgencyOrDepartmentCodeSequence
            ):
                return self._AssigningAgencyOrDepartmentCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.AssigningAgencyOrDepartmentCodeSequence]
        return None

    @AssigningAgencyOrDepartmentCodeSequence.setter
    def AssigningAgencyOrDepartmentCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._AssigningAgencyOrDepartmentCodeSequence = []
            if "AssigningAgencyOrDepartmentCodeSequence" in self._dataset:
                del self._dataset.AssigningAgencyOrDepartmentCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("AssigningAgencyOrDepartmentCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._AssigningAgencyOrDepartmentCodeSequence = value
            if "AssigningAgencyOrDepartmentCodeSequence" not in self._dataset:
                self._dataset.AssigningAgencyOrDepartmentCodeSequence = pydicom.Sequence()
            self._dataset.AssigningAgencyOrDepartmentCodeSequence.clear()
            self._dataset.AssigningAgencyOrDepartmentCodeSequence.extend([item.to_dataset() for item in value])

    def add_AssigningAgencyOrDepartmentCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._AssigningAgencyOrDepartmentCodeSequence.append(item)
        if "AssigningAgencyOrDepartmentCodeSequence" not in self._dataset:
            self._dataset.AssigningAgencyOrDepartmentCodeSequence = pydicom.Sequence()
        self._dataset.AssigningAgencyOrDepartmentCodeSequence.append(item.to_dataset())
