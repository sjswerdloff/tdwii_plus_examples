from typing import Optional

from pydicom.dataset import Dataset


class ContextGroupIdentification:
    def __init__(self):
        self._dataset = Dataset()

    @property
    def context_identifier(self) -> str:
        return self._dataset.get("ContextIdentifier", "")

    @context_identifier.setter
    def context_identifier(self, value: str):
        self._dataset.ContextIdentifier = value

    @property
    def context_uid(self) -> str:
        return self._dataset.get("ContextUID", "")

    @context_uid.setter
    def context_uid(self, value: str):
        self._dataset.ContextUID = value

    @property
    def context_group_version(self) -> Optional[str]:
        return self._dataset.get("ContextGroupVersion")

    @context_group_version.setter
    def context_group_version(self, value: Optional[str]):
        if value is not None:
            self._dataset.ContextGroupVersion = value

    @property
    def context_group_extension_flag(self) -> Optional[str]:
        return self._dataset.get("ContextGroupExtensionFlag")

    @context_group_extension_flag.setter
    def context_group_extension_flag(self, value: Optional[str]):
        if value is not None:
            self._dataset.ContextGroupExtensionFlag = value

    @property
    def context_group_local_version(self) -> Optional[str]:
        return self._dataset.get("ContextGroupLocalVersion")

    @context_group_local_version.setter
    def context_group_local_version(self, value: Optional[str]):
        if value is not None:
            self._dataset.ContextGroupLocalVersion = value

    @property
    def context_group_extension_creator_uid(self) -> Optional[str]:
        return self._dataset.get("ContextGroupExtensionCreatorUID")

    @context_group_extension_creator_uid.setter
    def context_group_extension_creator_uid(self, value: Optional[str]):
        if value is not None:
            self._dataset.ContextGroupExtensionCreatorUID = value

    def validate(self) -> Optional[str]:
        if not self.context_identifier:
            return "Context Identifier (Type 1) is missing"
        if not self.context_uid:
            return "Context UID (Type 1) is missing"
        return None

    def to_dataset(self) -> Dataset:
        return self._dataset

    @classmethod
    def from_dataset(cls, dataset: Dataset) -> "ContextGroupIdentification":
        item = cls()
        item._dataset = dataset
        return item
