from typing import Any, List, Optional  # noqa

import pydicom

from .deidentification_action_sequence_item import DeidentificationActionSequenceItem
from .private_data_element_definition_sequence_item import (
    PrivateDataElementDefinitionSequenceItem,
)


class PrivateDataElementCharacteristicsSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._DeidentificationActionSequence: List[DeidentificationActionSequenceItem] = []
        self._PrivateDataElementDefinitionSequence: List[PrivateDataElementDefinitionSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def PrivateGroupReference(self) -> Optional[int]:
        if "PrivateGroupReference" in self._dataset:
            return self._dataset.PrivateGroupReference
        return None

    @PrivateGroupReference.setter
    def PrivateGroupReference(self, value: Optional[int]):
        if value is None:
            if "PrivateGroupReference" in self._dataset:
                del self._dataset.PrivateGroupReference
        else:
            self._dataset.PrivateGroupReference = value

    @property
    def PrivateCreatorReference(self) -> Optional[str]:
        if "PrivateCreatorReference" in self._dataset:
            return self._dataset.PrivateCreatorReference
        return None

    @PrivateCreatorReference.setter
    def PrivateCreatorReference(self, value: Optional[str]):
        if value is None:
            if "PrivateCreatorReference" in self._dataset:
                del self._dataset.PrivateCreatorReference
        else:
            self._dataset.PrivateCreatorReference = value

    @property
    def BlockIdentifyingInformationStatus(self) -> Optional[str]:
        if "BlockIdentifyingInformationStatus" in self._dataset:
            return self._dataset.BlockIdentifyingInformationStatus
        return None

    @BlockIdentifyingInformationStatus.setter
    def BlockIdentifyingInformationStatus(self, value: Optional[str]):
        if value is None:
            if "BlockIdentifyingInformationStatus" in self._dataset:
                del self._dataset.BlockIdentifyingInformationStatus
        else:
            self._dataset.BlockIdentifyingInformationStatus = value

    @property
    def NonidentifyingPrivateElements(self) -> Optional[List[int]]:
        if "NonidentifyingPrivateElements" in self._dataset:
            return self._dataset.NonidentifyingPrivateElements
        return None

    @NonidentifyingPrivateElements.setter
    def NonidentifyingPrivateElements(self, value: Optional[List[int]]):
        if value is None:
            if "NonidentifyingPrivateElements" in self._dataset:
                del self._dataset.NonidentifyingPrivateElements
        else:
            self._dataset.NonidentifyingPrivateElements = value

    @property
    def DeidentificationActionSequence(self) -> Optional[List[DeidentificationActionSequenceItem]]:
        if "DeidentificationActionSequence" in self._dataset:
            if len(self._DeidentificationActionSequence) == len(self._dataset.DeidentificationActionSequence):
                return self._DeidentificationActionSequence
            else:
                return [DeidentificationActionSequenceItem(x) for x in self._dataset.DeidentificationActionSequence]
        return None

    @DeidentificationActionSequence.setter
    def DeidentificationActionSequence(self, value: Optional[List[DeidentificationActionSequenceItem]]):
        if value is None:
            self._DeidentificationActionSequence = []
            if "DeidentificationActionSequence" in self._dataset:
                del self._dataset.DeidentificationActionSequence
        elif not isinstance(value, list) or not all(isinstance(item, DeidentificationActionSequenceItem) for item in value):
            raise ValueError("DeidentificationActionSequence must be a list of DeidentificationActionSequenceItem objects")
        else:
            self._DeidentificationActionSequence = value
            if "DeidentificationActionSequence" not in self._dataset:
                self._dataset.DeidentificationActionSequence = pydicom.Sequence()
            self._dataset.DeidentificationActionSequence.clear()
            self._dataset.DeidentificationActionSequence.extend([item.to_dataset() for item in value])

    def add_DeidentificationAction(self, item: DeidentificationActionSequenceItem):
        if not isinstance(item, DeidentificationActionSequenceItem):
            raise ValueError("Item must be an instance of DeidentificationActionSequenceItem")
        self._DeidentificationActionSequence.append(item)
        if "DeidentificationActionSequence" not in self._dataset:
            self._dataset.DeidentificationActionSequence = pydicom.Sequence()
        self._dataset.DeidentificationActionSequence.append(item.to_dataset())

    @property
    def PrivateDataElementDefinitionSequence(self) -> Optional[List[PrivateDataElementDefinitionSequenceItem]]:
        if "PrivateDataElementDefinitionSequence" in self._dataset:
            if len(self._PrivateDataElementDefinitionSequence) == len(self._dataset.PrivateDataElementDefinitionSequence):
                return self._PrivateDataElementDefinitionSequence
            else:
                return [
                    PrivateDataElementDefinitionSequenceItem(x) for x in self._dataset.PrivateDataElementDefinitionSequence
                ]
        return None

    @PrivateDataElementDefinitionSequence.setter
    def PrivateDataElementDefinitionSequence(self, value: Optional[List[PrivateDataElementDefinitionSequenceItem]]):
        if value is None:
            self._PrivateDataElementDefinitionSequence = []
            if "PrivateDataElementDefinitionSequence" in self._dataset:
                del self._dataset.PrivateDataElementDefinitionSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, PrivateDataElementDefinitionSequenceItem) for item in value
        ):
            raise ValueError(
                "PrivateDataElementDefinitionSequence must be a list of PrivateDataElementDefinitionSequenceItem objects"
            )
        else:
            self._PrivateDataElementDefinitionSequence = value
            if "PrivateDataElementDefinitionSequence" not in self._dataset:
                self._dataset.PrivateDataElementDefinitionSequence = pydicom.Sequence()
            self._dataset.PrivateDataElementDefinitionSequence.clear()
            self._dataset.PrivateDataElementDefinitionSequence.extend([item.to_dataset() for item in value])

    def add_PrivateDataElementDefinition(self, item: PrivateDataElementDefinitionSequenceItem):
        if not isinstance(item, PrivateDataElementDefinitionSequenceItem):
            raise ValueError("Item must be an instance of PrivateDataElementDefinitionSequenceItem")
        self._PrivateDataElementDefinitionSequence.append(item)
        if "PrivateDataElementDefinitionSequence" not in self._dataset:
            self._dataset.PrivateDataElementDefinitionSequence = pydicom.Sequence()
        self._dataset.PrivateDataElementDefinitionSequence.append(item.to_dataset())
