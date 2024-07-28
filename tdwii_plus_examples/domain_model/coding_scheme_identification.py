from typing import Optional

from pydicom.dataset import Dataset


class CodingSchemeIdentification:
    def __init__(self):
        self._dataset = Dataset()

    @property
    def coding_scheme_designator(self) -> str:
        return self._dataset.get("CodingSchemeDesignator", "")

    @coding_scheme_designator.setter
    def coding_scheme_designator(self, value: str):
        self._dataset.CodingSchemeDesignator = value

    @property
    def coding_scheme_registry(self) -> Optional[str]:
        return self._dataset.get("CodingSchemeRegistry")

    @coding_scheme_registry.setter
    def coding_scheme_registry(self, value: Optional[str]):
        if value is not None:
            self._dataset.CodingSchemeRegistry = value

    @property
    def coding_scheme_uid(self) -> Optional[str]:
        return self._dataset.get("CodingSchemeUID")

    @coding_scheme_uid.setter
    def coding_scheme_uid(self, value: Optional[str]):
        if value is not None:
            self._dataset.CodingSchemeUID = value

    @property
    def coding_scheme_external_id(self) -> Optional[str]:
        return self._dataset.get("CodingSchemeExternalID")

    @coding_scheme_external_id.setter
    def coding_scheme_external_id(self, value: Optional[str]):
        if value is not None:
            self._dataset.CodingSchemeExternalID = value

    @property
    def coding_scheme_name(self) -> Optional[str]:
        return self._dataset.get("CodingSchemeName")

    @coding_scheme_name.setter
    def coding_scheme_name(self, value: Optional[str]):
        if value is not None:
            self._dataset.CodingSchemeName = value

    @property
    def coding_scheme_version(self) -> Optional[str]:
        return self._dataset.get("CodingSchemeVersion")

    @coding_scheme_version.setter
    def coding_scheme_version(self, value: Optional[str]):
        if value is not None:
            self._dataset.CodingSchemeVersion = value

    @property
    def responsible_organization(self) -> Optional[str]:
        return self._dataset.get("ResponsibleOrganization")

    @responsible_organization.setter
    def responsible_organization(self, value: Optional[str]):
        if value is not None:
            self._dataset.ResponsibleOrganization = value

    def validate(self) -> Optional[str]:
        if not self.coding_scheme_designator:
            return "Coding Scheme Designator (Type 1) is missing"
        return None

    def to_dataset(self) -> Dataset:
        return self._dataset

    @classmethod
    def from_dataset(cls, dataset: Dataset) -> "CodingSchemeIdentification":
        item = cls()
        item._dataset = dataset
        return item
