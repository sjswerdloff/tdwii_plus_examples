from typing import Any, List, Optional  # noqa

import pydicom

from .coding_scheme_resources_sequence_item import CodingSchemeResourcesSequenceItem


class CodingSchemeIdentificationSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._CodingSchemeResourcesSequence: List[CodingSchemeResourcesSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

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
    def CodingSchemeResourcesSequence(self) -> Optional[List[CodingSchemeResourcesSequenceItem]]:
        if "CodingSchemeResourcesSequence" in self._dataset:
            if len(self._CodingSchemeResourcesSequence) == len(self._dataset.CodingSchemeResourcesSequence):
                return self._CodingSchemeResourcesSequence
            else:
                return [CodingSchemeResourcesSequenceItem(x) for x in self._dataset.CodingSchemeResourcesSequence]
        return None

    @CodingSchemeResourcesSequence.setter
    def CodingSchemeResourcesSequence(self, value: Optional[List[CodingSchemeResourcesSequenceItem]]):
        if value is None:
            self._CodingSchemeResourcesSequence = []
            if "CodingSchemeResourcesSequence" in self._dataset:
                del self._dataset.CodingSchemeResourcesSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodingSchemeResourcesSequenceItem) for item in value):
            raise ValueError("CodingSchemeResourcesSequence must be a list of CodingSchemeResourcesSequenceItem objects")
        else:
            self._CodingSchemeResourcesSequence = value
            if "CodingSchemeResourcesSequence" not in self._dataset:
                self._dataset.CodingSchemeResourcesSequence = pydicom.Sequence()
            self._dataset.CodingSchemeResourcesSequence.clear()
            self._dataset.CodingSchemeResourcesSequence.extend([item.to_dataset() for item in value])

    def add_CodingSchemeResources(self, item: CodingSchemeResourcesSequenceItem):
        if not isinstance(item, CodingSchemeResourcesSequenceItem):
            raise ValueError("Item must be an instance of CodingSchemeResourcesSequenceItem")
        self._CodingSchemeResourcesSequence.append(item)
        if "CodingSchemeResourcesSequence" not in self._dataset:
            self._dataset.CodingSchemeResourcesSequence = pydicom.Sequence()
        self._dataset.CodingSchemeResourcesSequence.append(item.to_dataset())

    @property
    def CodingSchemeUID(self) -> Optional[str]:
        if "CodingSchemeUID" in self._dataset:
            return self._dataset.CodingSchemeUID
        return None

    @CodingSchemeUID.setter
    def CodingSchemeUID(self, value: Optional[str]):
        if value is None:
            if "CodingSchemeUID" in self._dataset:
                del self._dataset.CodingSchemeUID
        else:
            self._dataset.CodingSchemeUID = value

    @property
    def CodingSchemeRegistry(self) -> Optional[str]:
        if "CodingSchemeRegistry" in self._dataset:
            return self._dataset.CodingSchemeRegistry
        return None

    @CodingSchemeRegistry.setter
    def CodingSchemeRegistry(self, value: Optional[str]):
        if value is None:
            if "CodingSchemeRegistry" in self._dataset:
                del self._dataset.CodingSchemeRegistry
        else:
            self._dataset.CodingSchemeRegistry = value

    @property
    def CodingSchemeExternalID(self) -> Optional[str]:
        if "CodingSchemeExternalID" in self._dataset:
            return self._dataset.CodingSchemeExternalID
        return None

    @CodingSchemeExternalID.setter
    def CodingSchemeExternalID(self, value: Optional[str]):
        if value is None:
            if "CodingSchemeExternalID" in self._dataset:
                del self._dataset.CodingSchemeExternalID
        else:
            self._dataset.CodingSchemeExternalID = value

    @property
    def CodingSchemeName(self) -> Optional[str]:
        if "CodingSchemeName" in self._dataset:
            return self._dataset.CodingSchemeName
        return None

    @CodingSchemeName.setter
    def CodingSchemeName(self, value: Optional[str]):
        if value is None:
            if "CodingSchemeName" in self._dataset:
                del self._dataset.CodingSchemeName
        else:
            self._dataset.CodingSchemeName = value

    @property
    def CodingSchemeResponsibleOrganization(self) -> Optional[str]:
        if "CodingSchemeResponsibleOrganization" in self._dataset:
            return self._dataset.CodingSchemeResponsibleOrganization
        return None

    @CodingSchemeResponsibleOrganization.setter
    def CodingSchemeResponsibleOrganization(self, value: Optional[str]):
        if value is None:
            if "CodingSchemeResponsibleOrganization" in self._dataset:
                del self._dataset.CodingSchemeResponsibleOrganization
        else:
            self._dataset.CodingSchemeResponsibleOrganization = value
