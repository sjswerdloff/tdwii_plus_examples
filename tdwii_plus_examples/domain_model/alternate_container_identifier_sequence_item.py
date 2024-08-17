from typing import Any, List, Optional

import pydicom

from .issuer_of_the_container_identifier_sequence_item import (
    IssuerOfTheContainerIdentifierSequenceItem,
)


class AlternateContainerIdentifierSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._IssuerOfTheContainerIdentifierSequence: List[IssuerOfTheContainerIdentifierSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ContainerIdentifier(self) -> Optional[str]:
        if "ContainerIdentifier" in self._dataset:
            return self._dataset.ContainerIdentifier
        return None

    @ContainerIdentifier.setter
    def ContainerIdentifier(self, value: Optional[str]):
        if value is None:
            if "ContainerIdentifier" in self._dataset:
                del self._dataset.ContainerIdentifier
        else:
            self._dataset.ContainerIdentifier = value

    @property
    def IssuerOfTheContainerIdentifierSequence(self) -> Optional[List[IssuerOfTheContainerIdentifierSequenceItem]]:
        if "IssuerOfTheContainerIdentifierSequence" in self._dataset:
            if len(self._IssuerOfTheContainerIdentifierSequence) == len(self._dataset.IssuerOfTheContainerIdentifierSequence):
                return self._IssuerOfTheContainerIdentifierSequence
            else:
                return [
                    IssuerOfTheContainerIdentifierSequenceItem(x) for x in self._dataset.IssuerOfTheContainerIdentifierSequence
                ]
        return None

    @IssuerOfTheContainerIdentifierSequence.setter
    def IssuerOfTheContainerIdentifierSequence(self, value: Optional[List[IssuerOfTheContainerIdentifierSequenceItem]]):
        if value is None:
            self._IssuerOfTheContainerIdentifierSequence = []
            if "IssuerOfTheContainerIdentifierSequence" in self._dataset:
                del self._dataset.IssuerOfTheContainerIdentifierSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, IssuerOfTheContainerIdentifierSequenceItem) for item in value
        ):
            raise ValueError(
                f"IssuerOfTheContainerIdentifierSequence must be a list of IssuerOfTheContainerIdentifierSequenceItem objects"
            )
        else:
            self._IssuerOfTheContainerIdentifierSequence = value
            if "IssuerOfTheContainerIdentifierSequence" not in self._dataset:
                self._dataset.IssuerOfTheContainerIdentifierSequence = pydicom.Sequence()
            self._dataset.IssuerOfTheContainerIdentifierSequence.clear()
            self._dataset.IssuerOfTheContainerIdentifierSequence.extend([item.to_dataset() for item in value])

    def add_IssuerOfTheContainerIdentifier(self, item: IssuerOfTheContainerIdentifierSequenceItem):
        if not isinstance(item, IssuerOfTheContainerIdentifierSequenceItem):
            raise ValueError(f"Item must be an instance of IssuerOfTheContainerIdentifierSequenceItem")
        self._IssuerOfTheContainerIdentifierSequence.append(item)
        if "IssuerOfTheContainerIdentifierSequence" not in self._dataset:
            self._dataset.IssuerOfTheContainerIdentifierSequence = pydicom.Sequence()
        self._dataset.IssuerOfTheContainerIdentifierSequence.append(item.to_dataset())
