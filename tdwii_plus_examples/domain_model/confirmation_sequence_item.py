from typing import Any, List, Optional  # noqa

import pydicom

from .asserter_identification_sequence_item import AsserterIdentificationSequenceItem
from .code_sequence_item import CodeSequenceItem
from .pertinent_documents_sequence_item import PertinentDocumentsSequenceItem
from .related_assertion_sequence_item import RelatedAssertionSequenceItem


class ConfirmationSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._PertinentDocumentsSequence: List[PertinentDocumentsSequenceItem] = []
        self._AssertionCodeSequence: List[CodeSequenceItem] = []
        self._AsserterIdentificationSequence: List[AsserterIdentificationSequenceItem] = []
        self._RelatedAssertionSequence: List[RelatedAssertionSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def PertinentDocumentsSequence(self) -> Optional[List[PertinentDocumentsSequenceItem]]:
        if "PertinentDocumentsSequence" in self._dataset:
            if len(self._PertinentDocumentsSequence) == len(self._dataset.PertinentDocumentsSequence):
                return self._PertinentDocumentsSequence
            else:
                return [PertinentDocumentsSequenceItem(x) for x in self._dataset.PertinentDocumentsSequence]
        return None

    @PertinentDocumentsSequence.setter
    def PertinentDocumentsSequence(self, value: Optional[List[PertinentDocumentsSequenceItem]]):
        if value is None:
            self._PertinentDocumentsSequence = []
            if "PertinentDocumentsSequence" in self._dataset:
                del self._dataset.PertinentDocumentsSequence
        elif not isinstance(value, list) or not all(isinstance(item, PertinentDocumentsSequenceItem) for item in value):
            raise ValueError("PertinentDocumentsSequence must be a list of PertinentDocumentsSequenceItem objects")
        else:
            self._PertinentDocumentsSequence = value
            if "PertinentDocumentsSequence" not in self._dataset:
                self._dataset.PertinentDocumentsSequence = pydicom.Sequence()
            self._dataset.PertinentDocumentsSequence.clear()
            self._dataset.PertinentDocumentsSequence.extend([item.to_dataset() for item in value])

    def add_PertinentDocuments(self, item: PertinentDocumentsSequenceItem):
        if not isinstance(item, PertinentDocumentsSequenceItem):
            raise ValueError("Item must be an instance of PertinentDocumentsSequenceItem")
        self._PertinentDocumentsSequence.append(item)
        if "PertinentDocumentsSequence" not in self._dataset:
            self._dataset.PertinentDocumentsSequence = pydicom.Sequence()
        self._dataset.PertinentDocumentsSequence.append(item.to_dataset())

    @property
    def AssertionCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "AssertionCodeSequence" in self._dataset:
            if len(self._AssertionCodeSequence) == len(self._dataset.AssertionCodeSequence):
                return self._AssertionCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.AssertionCodeSequence]
        return None

    @AssertionCodeSequence.setter
    def AssertionCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._AssertionCodeSequence = []
            if "AssertionCodeSequence" in self._dataset:
                del self._dataset.AssertionCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("AssertionCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._AssertionCodeSequence = value
            if "AssertionCodeSequence" not in self._dataset:
                self._dataset.AssertionCodeSequence = pydicom.Sequence()
            self._dataset.AssertionCodeSequence.clear()
            self._dataset.AssertionCodeSequence.extend([item.to_dataset() for item in value])

    def add_AssertionCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._AssertionCodeSequence.append(item)
        if "AssertionCodeSequence" not in self._dataset:
            self._dataset.AssertionCodeSequence = pydicom.Sequence()
        self._dataset.AssertionCodeSequence.append(item.to_dataset())

    @property
    def AssertionUID(self) -> Optional[str]:
        if "AssertionUID" in self._dataset:
            return self._dataset.AssertionUID
        return None

    @AssertionUID.setter
    def AssertionUID(self, value: Optional[str]):
        if value is None:
            if "AssertionUID" in self._dataset:
                del self._dataset.AssertionUID
        else:
            self._dataset.AssertionUID = value

    @property
    def AsserterIdentificationSequence(self) -> Optional[List[AsserterIdentificationSequenceItem]]:
        if "AsserterIdentificationSequence" in self._dataset:
            if len(self._AsserterIdentificationSequence) == len(self._dataset.AsserterIdentificationSequence):
                return self._AsserterIdentificationSequence
            else:
                return [AsserterIdentificationSequenceItem(x) for x in self._dataset.AsserterIdentificationSequence]
        return None

    @AsserterIdentificationSequence.setter
    def AsserterIdentificationSequence(self, value: Optional[List[AsserterIdentificationSequenceItem]]):
        if value is None:
            self._AsserterIdentificationSequence = []
            if "AsserterIdentificationSequence" in self._dataset:
                del self._dataset.AsserterIdentificationSequence
        elif not isinstance(value, list) or not all(isinstance(item, AsserterIdentificationSequenceItem) for item in value):
            raise ValueError("AsserterIdentificationSequence must be a list of AsserterIdentificationSequenceItem objects")
        else:
            self._AsserterIdentificationSequence = value
            if "AsserterIdentificationSequence" not in self._dataset:
                self._dataset.AsserterIdentificationSequence = pydicom.Sequence()
            self._dataset.AsserterIdentificationSequence.clear()
            self._dataset.AsserterIdentificationSequence.extend([item.to_dataset() for item in value])

    def add_AsserterIdentification(self, item: AsserterIdentificationSequenceItem):
        if not isinstance(item, AsserterIdentificationSequenceItem):
            raise ValueError("Item must be an instance of AsserterIdentificationSequenceItem")
        self._AsserterIdentificationSequence.append(item)
        if "AsserterIdentificationSequence" not in self._dataset:
            self._dataset.AsserterIdentificationSequence = pydicom.Sequence()
        self._dataset.AsserterIdentificationSequence.append(item.to_dataset())

    @property
    def AssertionDateTime(self) -> Optional[str]:
        if "AssertionDateTime" in self._dataset:
            return self._dataset.AssertionDateTime
        return None

    @AssertionDateTime.setter
    def AssertionDateTime(self, value: Optional[str]):
        if value is None:
            if "AssertionDateTime" in self._dataset:
                del self._dataset.AssertionDateTime
        else:
            self._dataset.AssertionDateTime = value

    @property
    def AssertionExpirationDateTime(self) -> Optional[str]:
        if "AssertionExpirationDateTime" in self._dataset:
            return self._dataset.AssertionExpirationDateTime
        return None

    @AssertionExpirationDateTime.setter
    def AssertionExpirationDateTime(self, value: Optional[str]):
        if value is None:
            if "AssertionExpirationDateTime" in self._dataset:
                del self._dataset.AssertionExpirationDateTime
        else:
            self._dataset.AssertionExpirationDateTime = value

    @property
    def AssertionComments(self) -> Optional[str]:
        if "AssertionComments" in self._dataset:
            return self._dataset.AssertionComments
        return None

    @AssertionComments.setter
    def AssertionComments(self, value: Optional[str]):
        if value is None:
            if "AssertionComments" in self._dataset:
                del self._dataset.AssertionComments
        else:
            self._dataset.AssertionComments = value

    @property
    def RelatedAssertionSequence(self) -> Optional[List[RelatedAssertionSequenceItem]]:
        if "RelatedAssertionSequence" in self._dataset:
            if len(self._RelatedAssertionSequence) == len(self._dataset.RelatedAssertionSequence):
                return self._RelatedAssertionSequence
            else:
                return [RelatedAssertionSequenceItem(x) for x in self._dataset.RelatedAssertionSequence]
        return None

    @RelatedAssertionSequence.setter
    def RelatedAssertionSequence(self, value: Optional[List[RelatedAssertionSequenceItem]]):
        if value is None:
            self._RelatedAssertionSequence = []
            if "RelatedAssertionSequence" in self._dataset:
                del self._dataset.RelatedAssertionSequence
        elif not isinstance(value, list) or not all(isinstance(item, RelatedAssertionSequenceItem) for item in value):
            raise ValueError("RelatedAssertionSequence must be a list of RelatedAssertionSequenceItem objects")
        else:
            self._RelatedAssertionSequence = value
            if "RelatedAssertionSequence" not in self._dataset:
                self._dataset.RelatedAssertionSequence = pydicom.Sequence()
            self._dataset.RelatedAssertionSequence.clear()
            self._dataset.RelatedAssertionSequence.extend([item.to_dataset() for item in value])

    def add_RelatedAssertion(self, item: RelatedAssertionSequenceItem):
        if not isinstance(item, RelatedAssertionSequenceItem):
            raise ValueError("Item must be an instance of RelatedAssertionSequenceItem")
        self._RelatedAssertionSequence.append(item)
        if "RelatedAssertionSequence" not in self._dataset:
            self._dataset.RelatedAssertionSequence = pydicom.Sequence()
        self._dataset.RelatedAssertionSequence.append(item.to_dataset())
