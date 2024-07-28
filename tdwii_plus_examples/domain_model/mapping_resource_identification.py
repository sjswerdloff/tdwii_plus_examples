from typing import Optional

from pydicom.dataset import Dataset


class MappingResourceIdentification:
    def __init__(self):
        self._dataset = Dataset()

    @property
    def mapping_resource_name(self) -> Optional[str]:
        return self._dataset.get("MappingResourceName")

    @mapping_resource_name.setter
    def mapping_resource_name(self, value: Optional[str]):
        if value is not None:
            self._dataset.MappingResourceName = value
        elif "MappingResourceName" in self._dataset:
            del self._dataset.MappingResourceName

    @property
    def mapping_resource_identifier(self) -> Optional[str]:
        return self._dataset.get("MappingResourceIdentifier")

    @mapping_resource_identifier.setter
    def mapping_resource_identifier(self, value: Optional[str]):
        if value is not None:
            self._dataset.MappingResourceIdentifier = value
        elif "MappingResourceIdentifier" in self._dataset:
            del self._dataset.MappingResourceIdentifier

    @property
    def mapping_resource_uid(self) -> Optional[str]:
        return self._dataset.get("MappingResourceUID")

    @mapping_resource_uid.setter
    def mapping_resource_uid(self, value: Optional[str]):
        if value is not None:
            self._dataset.MappingResourceUID = value
        elif "MappingResourceUID" in self._dataset:
            del self._dataset.MappingResourceUID

    @property
    def mapping_resource_version(self) -> Optional[str]:
        return self._dataset.get("MappingResourceVersion")

    @mapping_resource_version.setter
    def mapping_resource_version(self, value: Optional[str]):
        if value is not None:
            self._dataset.MappingResourceVersion = value
        elif "MappingResourceVersion" in self._dataset:
            del self._dataset.MappingResourceVersion

    def validate(self) -> Optional[str]:
        if self.mapping_resource_name is None or self.mapping_resource_name == "":
            return "Mapping Resource Name (Type 1) is missing or empty"
        if self.mapping_resource_identifier is None or self.mapping_resource_identifier == "":
            return "Mapping Resource Identifier (Type 1) is missing or empty"
        return None

    def to_dataset(self) -> Dataset:
        return self._dataset

    @classmethod
    def from_dataset(cls, dataset: Dataset) -> "MappingResourceIdentification":
        item = cls()
        item._dataset = dataset
        return item
