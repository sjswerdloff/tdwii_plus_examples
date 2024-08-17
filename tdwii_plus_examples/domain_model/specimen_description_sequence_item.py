from typing import Any, List, Optional  # noqa

import pydicom

from .code_sequence_item import CodeSequenceItem
from .issuer_of_the_specimen_identifier_sequence_item import (
    IssuerOfTheSpecimenIdentifierSequenceItem,
)
from .primary_anatomic_structure_sequence_item import (
    PrimaryAnatomicStructureSequenceItem,
)
from .specimen_localization_content_item_sequence_item import (
    SpecimenLocalizationContentItemSequenceItem,
)
from .specimen_preparation_sequence_item import SpecimenPreparationSequenceItem


class SpecimenDescriptionSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._PrimaryAnatomicStructureSequence: List[PrimaryAnatomicStructureSequenceItem] = []
        self._IssuerOfTheSpecimenIdentifierSequence: List[IssuerOfTheSpecimenIdentifierSequenceItem] = []
        self._SpecimenTypeCodeSequence: List[CodeSequenceItem] = []
        self._SpecimenPreparationSequence: List[SpecimenPreparationSequenceItem] = []
        self._SpecimenLocalizationContentItemSequence: List[SpecimenLocalizationContentItemSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def PrimaryAnatomicStructureSequence(self) -> Optional[List[PrimaryAnatomicStructureSequenceItem]]:
        if "PrimaryAnatomicStructureSequence" in self._dataset:
            if len(self._PrimaryAnatomicStructureSequence) == len(self._dataset.PrimaryAnatomicStructureSequence):
                return self._PrimaryAnatomicStructureSequence
            else:
                return [PrimaryAnatomicStructureSequenceItem(x) for x in self._dataset.PrimaryAnatomicStructureSequence]
        return None

    @PrimaryAnatomicStructureSequence.setter
    def PrimaryAnatomicStructureSequence(self, value: Optional[List[PrimaryAnatomicStructureSequenceItem]]):
        if value is None:
            self._PrimaryAnatomicStructureSequence = []
            if "PrimaryAnatomicStructureSequence" in self._dataset:
                del self._dataset.PrimaryAnatomicStructureSequence
        elif not isinstance(value, list) or not all(isinstance(item, PrimaryAnatomicStructureSequenceItem) for item in value):
            raise ValueError("PrimaryAnatomicStructureSequence must be a list of PrimaryAnatomicStructureSequenceItem objects")
        else:
            self._PrimaryAnatomicStructureSequence = value
            if "PrimaryAnatomicStructureSequence" not in self._dataset:
                self._dataset.PrimaryAnatomicStructureSequence = pydicom.Sequence()
            self._dataset.PrimaryAnatomicStructureSequence.clear()
            self._dataset.PrimaryAnatomicStructureSequence.extend([item.to_dataset() for item in value])

    def add_PrimaryAnatomicStructure(self, item: PrimaryAnatomicStructureSequenceItem):
        if not isinstance(item, PrimaryAnatomicStructureSequenceItem):
            raise ValueError("Item must be an instance of PrimaryAnatomicStructureSequenceItem")
        self._PrimaryAnatomicStructureSequence.append(item)
        if "PrimaryAnatomicStructureSequence" not in self._dataset:
            self._dataset.PrimaryAnatomicStructureSequence = pydicom.Sequence()
        self._dataset.PrimaryAnatomicStructureSequence.append(item.to_dataset())

    @property
    def SpecimenIdentifier(self) -> Optional[str]:
        if "SpecimenIdentifier" in self._dataset:
            return self._dataset.SpecimenIdentifier
        return None

    @SpecimenIdentifier.setter
    def SpecimenIdentifier(self, value: Optional[str]):
        if value is None:
            if "SpecimenIdentifier" in self._dataset:
                del self._dataset.SpecimenIdentifier
        else:
            self._dataset.SpecimenIdentifier = value

    @property
    def SpecimenUID(self) -> Optional[str]:
        if "SpecimenUID" in self._dataset:
            return self._dataset.SpecimenUID
        return None

    @SpecimenUID.setter
    def SpecimenUID(self, value: Optional[str]):
        if value is None:
            if "SpecimenUID" in self._dataset:
                del self._dataset.SpecimenUID
        else:
            self._dataset.SpecimenUID = value

    @property
    def IssuerOfTheSpecimenIdentifierSequence(self) -> Optional[List[IssuerOfTheSpecimenIdentifierSequenceItem]]:
        if "IssuerOfTheSpecimenIdentifierSequence" in self._dataset:
            if len(self._IssuerOfTheSpecimenIdentifierSequence) == len(self._dataset.IssuerOfTheSpecimenIdentifierSequence):
                return self._IssuerOfTheSpecimenIdentifierSequence
            else:
                return [
                    IssuerOfTheSpecimenIdentifierSequenceItem(x) for x in self._dataset.IssuerOfTheSpecimenIdentifierSequence
                ]
        return None

    @IssuerOfTheSpecimenIdentifierSequence.setter
    def IssuerOfTheSpecimenIdentifierSequence(self, value: Optional[List[IssuerOfTheSpecimenIdentifierSequenceItem]]):
        if value is None:
            self._IssuerOfTheSpecimenIdentifierSequence = []
            if "IssuerOfTheSpecimenIdentifierSequence" in self._dataset:
                del self._dataset.IssuerOfTheSpecimenIdentifierSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, IssuerOfTheSpecimenIdentifierSequenceItem) for item in value
        ):
            raise ValueError(
                "IssuerOfTheSpecimenIdentifierSequence must be a list of IssuerOfTheSpecimenIdentifierSequenceItem objects"
            )
        else:
            self._IssuerOfTheSpecimenIdentifierSequence = value
            if "IssuerOfTheSpecimenIdentifierSequence" not in self._dataset:
                self._dataset.IssuerOfTheSpecimenIdentifierSequence = pydicom.Sequence()
            self._dataset.IssuerOfTheSpecimenIdentifierSequence.clear()
            self._dataset.IssuerOfTheSpecimenIdentifierSequence.extend([item.to_dataset() for item in value])

    def add_IssuerOfTheSpecimenIdentifier(self, item: IssuerOfTheSpecimenIdentifierSequenceItem):
        if not isinstance(item, IssuerOfTheSpecimenIdentifierSequenceItem):
            raise ValueError("Item must be an instance of IssuerOfTheSpecimenIdentifierSequenceItem")
        self._IssuerOfTheSpecimenIdentifierSequence.append(item)
        if "IssuerOfTheSpecimenIdentifierSequence" not in self._dataset:
            self._dataset.IssuerOfTheSpecimenIdentifierSequence = pydicom.Sequence()
        self._dataset.IssuerOfTheSpecimenIdentifierSequence.append(item.to_dataset())

    @property
    def SpecimenTypeCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "SpecimenTypeCodeSequence" in self._dataset:
            if len(self._SpecimenTypeCodeSequence) == len(self._dataset.SpecimenTypeCodeSequence):
                return self._SpecimenTypeCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.SpecimenTypeCodeSequence]
        return None

    @SpecimenTypeCodeSequence.setter
    def SpecimenTypeCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._SpecimenTypeCodeSequence = []
            if "SpecimenTypeCodeSequence" in self._dataset:
                del self._dataset.SpecimenTypeCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("SpecimenTypeCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._SpecimenTypeCodeSequence = value
            if "SpecimenTypeCodeSequence" not in self._dataset:
                self._dataset.SpecimenTypeCodeSequence = pydicom.Sequence()
            self._dataset.SpecimenTypeCodeSequence.clear()
            self._dataset.SpecimenTypeCodeSequence.extend([item.to_dataset() for item in value])

    def add_SpecimenTypeCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._SpecimenTypeCodeSequence.append(item)
        if "SpecimenTypeCodeSequence" not in self._dataset:
            self._dataset.SpecimenTypeCodeSequence = pydicom.Sequence()
        self._dataset.SpecimenTypeCodeSequence.append(item.to_dataset())

    @property
    def SpecimenShortDescription(self) -> Optional[str]:
        if "SpecimenShortDescription" in self._dataset:
            return self._dataset.SpecimenShortDescription
        return None

    @SpecimenShortDescription.setter
    def SpecimenShortDescription(self, value: Optional[str]):
        if value is None:
            if "SpecimenShortDescription" in self._dataset:
                del self._dataset.SpecimenShortDescription
        else:
            self._dataset.SpecimenShortDescription = value

    @property
    def SpecimenDetailedDescription(self) -> Optional[str]:
        if "SpecimenDetailedDescription" in self._dataset:
            return self._dataset.SpecimenDetailedDescription
        return None

    @SpecimenDetailedDescription.setter
    def SpecimenDetailedDescription(self, value: Optional[str]):
        if value is None:
            if "SpecimenDetailedDescription" in self._dataset:
                del self._dataset.SpecimenDetailedDescription
        else:
            self._dataset.SpecimenDetailedDescription = value

    @property
    def SpecimenPreparationSequence(self) -> Optional[List[SpecimenPreparationSequenceItem]]:
        if "SpecimenPreparationSequence" in self._dataset:
            if len(self._SpecimenPreparationSequence) == len(self._dataset.SpecimenPreparationSequence):
                return self._SpecimenPreparationSequence
            else:
                return [SpecimenPreparationSequenceItem(x) for x in self._dataset.SpecimenPreparationSequence]
        return None

    @SpecimenPreparationSequence.setter
    def SpecimenPreparationSequence(self, value: Optional[List[SpecimenPreparationSequenceItem]]):
        if value is None:
            self._SpecimenPreparationSequence = []
            if "SpecimenPreparationSequence" in self._dataset:
                del self._dataset.SpecimenPreparationSequence
        elif not isinstance(value, list) or not all(isinstance(item, SpecimenPreparationSequenceItem) for item in value):
            raise ValueError("SpecimenPreparationSequence must be a list of SpecimenPreparationSequenceItem objects")
        else:
            self._SpecimenPreparationSequence = value
            if "SpecimenPreparationSequence" not in self._dataset:
                self._dataset.SpecimenPreparationSequence = pydicom.Sequence()
            self._dataset.SpecimenPreparationSequence.clear()
            self._dataset.SpecimenPreparationSequence.extend([item.to_dataset() for item in value])

    def add_SpecimenPreparation(self, item: SpecimenPreparationSequenceItem):
        if not isinstance(item, SpecimenPreparationSequenceItem):
            raise ValueError("Item must be an instance of SpecimenPreparationSequenceItem")
        self._SpecimenPreparationSequence.append(item)
        if "SpecimenPreparationSequence" not in self._dataset:
            self._dataset.SpecimenPreparationSequence = pydicom.Sequence()
        self._dataset.SpecimenPreparationSequence.append(item.to_dataset())

    @property
    def SpecimenLocalizationContentItemSequence(self) -> Optional[List[SpecimenLocalizationContentItemSequenceItem]]:
        if "SpecimenLocalizationContentItemSequence" in self._dataset:
            if len(self._SpecimenLocalizationContentItemSequence) == len(
                self._dataset.SpecimenLocalizationContentItemSequence
            ):
                return self._SpecimenLocalizationContentItemSequence
            else:
                return [
                    SpecimenLocalizationContentItemSequenceItem(x)
                    for x in self._dataset.SpecimenLocalizationContentItemSequence
                ]
        return None

    @SpecimenLocalizationContentItemSequence.setter
    def SpecimenLocalizationContentItemSequence(self, value: Optional[List[SpecimenLocalizationContentItemSequenceItem]]):
        if value is None:
            self._SpecimenLocalizationContentItemSequence = []
            if "SpecimenLocalizationContentItemSequence" in self._dataset:
                del self._dataset.SpecimenLocalizationContentItemSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, SpecimenLocalizationContentItemSequenceItem) for item in value
        ):
            raise ValueError(
                "SpecimenLocalizationContentItemSequence must be a list of SpecimenLocalizationContentItemSequenceItem objects"
            )
        else:
            self._SpecimenLocalizationContentItemSequence = value
            if "SpecimenLocalizationContentItemSequence" not in self._dataset:
                self._dataset.SpecimenLocalizationContentItemSequence = pydicom.Sequence()
            self._dataset.SpecimenLocalizationContentItemSequence.clear()
            self._dataset.SpecimenLocalizationContentItemSequence.extend([item.to_dataset() for item in value])

    def add_SpecimenLocalizationContentItem(self, item: SpecimenLocalizationContentItemSequenceItem):
        if not isinstance(item, SpecimenLocalizationContentItemSequenceItem):
            raise ValueError("Item must be an instance of SpecimenLocalizationContentItemSequenceItem")
        self._SpecimenLocalizationContentItemSequence.append(item)
        if "SpecimenLocalizationContentItemSequence" not in self._dataset:
            self._dataset.SpecimenLocalizationContentItemSequence = pydicom.Sequence()
        self._dataset.SpecimenLocalizationContentItemSequence.append(item.to_dataset())
