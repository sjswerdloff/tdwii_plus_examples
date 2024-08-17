from typing import Any, List, Optional  # noqa

import pydicom

from .code_sequence_item import CodeSequenceItem
from .override_sequence_item import OverrideSequenceItem
from .treatment_tolerance_violation_attribute_sequence_item import (
    TreatmentToleranceViolationAttributeSequenceItem,
)


class TreatmentToleranceViolationSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._OverrideSequence: List[OverrideSequenceItem] = []
        self._TreatmentToleranceViolationAttributeSequence: List[TreatmentToleranceViolationAttributeSequenceItem] = []
        self._TreatmentToleranceViolationTypeCodeSequence: List[CodeSequenceItem] = []
        self._TreatmentToleranceViolationCauseCodeSequence: List[CodeSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def OverrideSequence(self) -> Optional[List[OverrideSequenceItem]]:
        if "OverrideSequence" in self._dataset:
            if len(self._OverrideSequence) == len(self._dataset.OverrideSequence):
                return self._OverrideSequence
            else:
                return [OverrideSequenceItem(x) for x in self._dataset.OverrideSequence]
        return None

    @OverrideSequence.setter
    def OverrideSequence(self, value: Optional[List[OverrideSequenceItem]]):
        if value is None:
            self._OverrideSequence = []
            if "OverrideSequence" in self._dataset:
                del self._dataset.OverrideSequence
        elif not isinstance(value, list) or not all(isinstance(item, OverrideSequenceItem) for item in value):
            raise ValueError("OverrideSequence must be a list of OverrideSequenceItem objects")
        else:
            self._OverrideSequence = value
            if "OverrideSequence" not in self._dataset:
                self._dataset.OverrideSequence = pydicom.Sequence()
            self._dataset.OverrideSequence.clear()
            self._dataset.OverrideSequence.extend([item.to_dataset() for item in value])

    def add_Override(self, item: OverrideSequenceItem):
        if not isinstance(item, OverrideSequenceItem):
            raise ValueError("Item must be an instance of OverrideSequenceItem")
        self._OverrideSequence.append(item)
        if "OverrideSequence" not in self._dataset:
            self._dataset.OverrideSequence = pydicom.Sequence()
        self._dataset.OverrideSequence.append(item.to_dataset())

    @property
    def TreatmentToleranceViolationCategory(self) -> Optional[str]:
        if "TreatmentToleranceViolationCategory" in self._dataset:
            return self._dataset.TreatmentToleranceViolationCategory
        return None

    @TreatmentToleranceViolationCategory.setter
    def TreatmentToleranceViolationCategory(self, value: Optional[str]):
        if value is None:
            if "TreatmentToleranceViolationCategory" in self._dataset:
                del self._dataset.TreatmentToleranceViolationCategory
        else:
            self._dataset.TreatmentToleranceViolationCategory = value

    @property
    def TreatmentToleranceViolationAttributeSequence(self) -> Optional[List[TreatmentToleranceViolationAttributeSequenceItem]]:
        if "TreatmentToleranceViolationAttributeSequence" in self._dataset:
            if len(self._TreatmentToleranceViolationAttributeSequence) == len(
                self._dataset.TreatmentToleranceViolationAttributeSequence
            ):
                return self._TreatmentToleranceViolationAttributeSequence
            else:
                return [
                    TreatmentToleranceViolationAttributeSequenceItem(x)
                    for x in self._dataset.TreatmentToleranceViolationAttributeSequence
                ]
        return None

    @TreatmentToleranceViolationAttributeSequence.setter
    def TreatmentToleranceViolationAttributeSequence(
        self, value: Optional[List[TreatmentToleranceViolationAttributeSequenceItem]]
    ):
        if value is None:
            self._TreatmentToleranceViolationAttributeSequence = []
            if "TreatmentToleranceViolationAttributeSequence" in self._dataset:
                del self._dataset.TreatmentToleranceViolationAttributeSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, TreatmentToleranceViolationAttributeSequenceItem) for item in value
        ):
            raise ValueError(
                "TreatmentToleranceViolationAttributeSequence must be a list of"
                " TreatmentToleranceViolationAttributeSequenceItem objects"
            )
        else:
            self._TreatmentToleranceViolationAttributeSequence = value
            if "TreatmentToleranceViolationAttributeSequence" not in self._dataset:
                self._dataset.TreatmentToleranceViolationAttributeSequence = pydicom.Sequence()
            self._dataset.TreatmentToleranceViolationAttributeSequence.clear()
            self._dataset.TreatmentToleranceViolationAttributeSequence.extend([item.to_dataset() for item in value])

    def add_TreatmentToleranceViolationAttribute(self, item: TreatmentToleranceViolationAttributeSequenceItem):
        if not isinstance(item, TreatmentToleranceViolationAttributeSequenceItem):
            raise ValueError("Item must be an instance of TreatmentToleranceViolationAttributeSequenceItem")
        self._TreatmentToleranceViolationAttributeSequence.append(item)
        if "TreatmentToleranceViolationAttributeSequence" not in self._dataset:
            self._dataset.TreatmentToleranceViolationAttributeSequence = pydicom.Sequence()
        self._dataset.TreatmentToleranceViolationAttributeSequence.append(item.to_dataset())

    @property
    def TreatmentToleranceViolationDescription(self) -> Optional[str]:
        if "TreatmentToleranceViolationDescription" in self._dataset:
            return self._dataset.TreatmentToleranceViolationDescription
        return None

    @TreatmentToleranceViolationDescription.setter
    def TreatmentToleranceViolationDescription(self, value: Optional[str]):
        if value is None:
            if "TreatmentToleranceViolationDescription" in self._dataset:
                del self._dataset.TreatmentToleranceViolationDescription
        else:
            self._dataset.TreatmentToleranceViolationDescription = value

    @property
    def TreatmentToleranceViolationIdentification(self) -> Optional[str]:
        if "TreatmentToleranceViolationIdentification" in self._dataset:
            return self._dataset.TreatmentToleranceViolationIdentification
        return None

    @TreatmentToleranceViolationIdentification.setter
    def TreatmentToleranceViolationIdentification(self, value: Optional[str]):
        if value is None:
            if "TreatmentToleranceViolationIdentification" in self._dataset:
                del self._dataset.TreatmentToleranceViolationIdentification
        else:
            self._dataset.TreatmentToleranceViolationIdentification = value

    @property
    def TreatmentToleranceViolationDateTime(self) -> Optional[str]:
        if "TreatmentToleranceViolationDateTime" in self._dataset:
            return self._dataset.TreatmentToleranceViolationDateTime
        return None

    @TreatmentToleranceViolationDateTime.setter
    def TreatmentToleranceViolationDateTime(self, value: Optional[str]):
        if value is None:
            if "TreatmentToleranceViolationDateTime" in self._dataset:
                del self._dataset.TreatmentToleranceViolationDateTime
        else:
            self._dataset.TreatmentToleranceViolationDateTime = value

    @property
    def TreatmentToleranceViolationTypeCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "TreatmentToleranceViolationTypeCodeSequence" in self._dataset:
            if len(self._TreatmentToleranceViolationTypeCodeSequence) == len(
                self._dataset.TreatmentToleranceViolationTypeCodeSequence
            ):
                return self._TreatmentToleranceViolationTypeCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.TreatmentToleranceViolationTypeCodeSequence]
        return None

    @TreatmentToleranceViolationTypeCodeSequence.setter
    def TreatmentToleranceViolationTypeCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._TreatmentToleranceViolationTypeCodeSequence = []
            if "TreatmentToleranceViolationTypeCodeSequence" in self._dataset:
                del self._dataset.TreatmentToleranceViolationTypeCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("TreatmentToleranceViolationTypeCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._TreatmentToleranceViolationTypeCodeSequence = value
            if "TreatmentToleranceViolationTypeCodeSequence" not in self._dataset:
                self._dataset.TreatmentToleranceViolationTypeCodeSequence = pydicom.Sequence()
            self._dataset.TreatmentToleranceViolationTypeCodeSequence.clear()
            self._dataset.TreatmentToleranceViolationTypeCodeSequence.extend([item.to_dataset() for item in value])

    def add_TreatmentToleranceViolationTypeCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._TreatmentToleranceViolationTypeCodeSequence.append(item)
        if "TreatmentToleranceViolationTypeCodeSequence" not in self._dataset:
            self._dataset.TreatmentToleranceViolationTypeCodeSequence = pydicom.Sequence()
        self._dataset.TreatmentToleranceViolationTypeCodeSequence.append(item.to_dataset())

    @property
    def TreatmentToleranceViolationCauseCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "TreatmentToleranceViolationCauseCodeSequence" in self._dataset:
            if len(self._TreatmentToleranceViolationCauseCodeSequence) == len(
                self._dataset.TreatmentToleranceViolationCauseCodeSequence
            ):
                return self._TreatmentToleranceViolationCauseCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.TreatmentToleranceViolationCauseCodeSequence]
        return None

    @TreatmentToleranceViolationCauseCodeSequence.setter
    def TreatmentToleranceViolationCauseCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._TreatmentToleranceViolationCauseCodeSequence = []
            if "TreatmentToleranceViolationCauseCodeSequence" in self._dataset:
                del self._dataset.TreatmentToleranceViolationCauseCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("TreatmentToleranceViolationCauseCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._TreatmentToleranceViolationCauseCodeSequence = value
            if "TreatmentToleranceViolationCauseCodeSequence" not in self._dataset:
                self._dataset.TreatmentToleranceViolationCauseCodeSequence = pydicom.Sequence()
            self._dataset.TreatmentToleranceViolationCauseCodeSequence.clear()
            self._dataset.TreatmentToleranceViolationCauseCodeSequence.extend([item.to_dataset() for item in value])

    def add_TreatmentToleranceViolationCauseCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._TreatmentToleranceViolationCauseCodeSequence.append(item)
        if "TreatmentToleranceViolationCauseCodeSequence" not in self._dataset:
            self._dataset.TreatmentToleranceViolationCauseCodeSequence = pydicom.Sequence()
        self._dataset.TreatmentToleranceViolationCauseCodeSequence.append(item.to_dataset())
