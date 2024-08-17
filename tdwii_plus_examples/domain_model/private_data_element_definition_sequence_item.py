from typing import Any, List, Optional

import pydicom


class PrivateDataElementDefinitionSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def PrivateDataElement(self) -> Optional[int]:
        if "PrivateDataElement" in self._dataset:
            return self._dataset.PrivateDataElement
        return None

    @PrivateDataElement.setter
    def PrivateDataElement(self, value: Optional[int]):
        if value is None:
            if "PrivateDataElement" in self._dataset:
                del self._dataset.PrivateDataElement
        else:
            self._dataset.PrivateDataElement = value

    @property
    def PrivateDataElementValueMultiplicity(self) -> Optional[List[int]]:
        if "PrivateDataElementValueMultiplicity" in self._dataset:
            return self._dataset.PrivateDataElementValueMultiplicity
        return None

    @PrivateDataElementValueMultiplicity.setter
    def PrivateDataElementValueMultiplicity(self, value: Optional[List[int]]):
        if value is None:
            if "PrivateDataElementValueMultiplicity" in self._dataset:
                del self._dataset.PrivateDataElementValueMultiplicity
        else:
            self._dataset.PrivateDataElementValueMultiplicity = value

    @property
    def PrivateDataElementValueRepresentation(self) -> Optional[str]:
        if "PrivateDataElementValueRepresentation" in self._dataset:
            return self._dataset.PrivateDataElementValueRepresentation
        return None

    @PrivateDataElementValueRepresentation.setter
    def PrivateDataElementValueRepresentation(self, value: Optional[str]):
        if value is None:
            if "PrivateDataElementValueRepresentation" in self._dataset:
                del self._dataset.PrivateDataElementValueRepresentation
        else:
            self._dataset.PrivateDataElementValueRepresentation = value

    @property
    def PrivateDataElementNumberOfItems(self) -> Optional[List[int]]:
        if "PrivateDataElementNumberOfItems" in self._dataset:
            return self._dataset.PrivateDataElementNumberOfItems
        return None

    @PrivateDataElementNumberOfItems.setter
    def PrivateDataElementNumberOfItems(self, value: Optional[List[int]]):
        if value is None:
            if "PrivateDataElementNumberOfItems" in self._dataset:
                del self._dataset.PrivateDataElementNumberOfItems
        else:
            self._dataset.PrivateDataElementNumberOfItems = value

    @property
    def PrivateDataElementName(self) -> Optional[str]:
        if "PrivateDataElementName" in self._dataset:
            return self._dataset.PrivateDataElementName
        return None

    @PrivateDataElementName.setter
    def PrivateDataElementName(self, value: Optional[str]):
        if value is None:
            if "PrivateDataElementName" in self._dataset:
                del self._dataset.PrivateDataElementName
        else:
            self._dataset.PrivateDataElementName = value

    @property
    def PrivateDataElementKeyword(self) -> Optional[str]:
        if "PrivateDataElementKeyword" in self._dataset:
            return self._dataset.PrivateDataElementKeyword
        return None

    @PrivateDataElementKeyword.setter
    def PrivateDataElementKeyword(self, value: Optional[str]):
        if value is None:
            if "PrivateDataElementKeyword" in self._dataset:
                del self._dataset.PrivateDataElementKeyword
        else:
            self._dataset.PrivateDataElementKeyword = value

    @property
    def PrivateDataElementDescription(self) -> Optional[str]:
        if "PrivateDataElementDescription" in self._dataset:
            return self._dataset.PrivateDataElementDescription
        return None

    @PrivateDataElementDescription.setter
    def PrivateDataElementDescription(self, value: Optional[str]):
        if value is None:
            if "PrivateDataElementDescription" in self._dataset:
                del self._dataset.PrivateDataElementDescription
        else:
            self._dataset.PrivateDataElementDescription = value

    @property
    def PrivateDataElementEncoding(self) -> Optional[str]:
        if "PrivateDataElementEncoding" in self._dataset:
            return self._dataset.PrivateDataElementEncoding
        return None

    @PrivateDataElementEncoding.setter
    def PrivateDataElementEncoding(self, value: Optional[str]):
        if value is None:
            if "PrivateDataElementEncoding" in self._dataset:
                del self._dataset.PrivateDataElementEncoding
        else:
            self._dataset.PrivateDataElementEncoding = value

    @property
    def RetrieveURI(self) -> Optional[str]:
        if "RetrieveURI" in self._dataset:
            return self._dataset.RetrieveURI
        return None

    @RetrieveURI.setter
    def RetrieveURI(self, value: Optional[str]):
        if value is None:
            if "RetrieveURI" in self._dataset:
                del self._dataset.RetrieveURI
        else:
            self._dataset.RetrieveURI = value
