from typing import Any, List, Optional  # noqa

import pydicom

from .code_sequence_item import CodeSequenceItem
from .constraint_value_sequence_item import ConstraintValueSequenceItem
from .recommended_default_value_sequence_item import RecommendedDefaultValueSequenceItem


class ParametersSpecificationSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._MeasurementUnitsCodeSequence: List[CodeSequenceItem] = []
        self._ConstraintValueSequence: List[ConstraintValueSequenceItem] = []
        self._RecommendedDefaultValueSequence: List[RecommendedDefaultValueSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def MeasurementUnitsCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "MeasurementUnitsCodeSequence" in self._dataset:
            if len(self._MeasurementUnitsCodeSequence) == len(self._dataset.MeasurementUnitsCodeSequence):
                return self._MeasurementUnitsCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.MeasurementUnitsCodeSequence]
        return None

    @MeasurementUnitsCodeSequence.setter
    def MeasurementUnitsCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._MeasurementUnitsCodeSequence = []
            if "MeasurementUnitsCodeSequence" in self._dataset:
                del self._dataset.MeasurementUnitsCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("MeasurementUnitsCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._MeasurementUnitsCodeSequence = value
            if "MeasurementUnitsCodeSequence" not in self._dataset:
                self._dataset.MeasurementUnitsCodeSequence = pydicom.Sequence()
            self._dataset.MeasurementUnitsCodeSequence.clear()
            self._dataset.MeasurementUnitsCodeSequence.extend([item.to_dataset() for item in value])

    def add_MeasurementUnitsCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._MeasurementUnitsCodeSequence.append(item)
        if "MeasurementUnitsCodeSequence" not in self._dataset:
            self._dataset.MeasurementUnitsCodeSequence = pydicom.Sequence()
        self._dataset.MeasurementUnitsCodeSequence.append(item.to_dataset())

    @property
    def SelectorAttribute(self) -> Optional[int]:
        if "SelectorAttribute" in self._dataset:
            return self._dataset.SelectorAttribute
        return None

    @SelectorAttribute.setter
    def SelectorAttribute(self, value: Optional[int]):
        if value is None:
            if "SelectorAttribute" in self._dataset:
                del self._dataset.SelectorAttribute
        else:
            self._dataset.SelectorAttribute = value

    @property
    def SelectorValueNumber(self) -> Optional[int]:
        if "SelectorValueNumber" in self._dataset:
            return self._dataset.SelectorValueNumber
        return None

    @SelectorValueNumber.setter
    def SelectorValueNumber(self, value: Optional[int]):
        if value is None:
            if "SelectorValueNumber" in self._dataset:
                del self._dataset.SelectorValueNumber
        else:
            self._dataset.SelectorValueNumber = value

    @property
    def SelectorAttributeVR(self) -> Optional[str]:
        if "SelectorAttributeVR" in self._dataset:
            return self._dataset.SelectorAttributeVR
        return None

    @SelectorAttributeVR.setter
    def SelectorAttributeVR(self, value: Optional[str]):
        if value is None:
            if "SelectorAttributeVR" in self._dataset:
                del self._dataset.SelectorAttributeVR
        else:
            self._dataset.SelectorAttributeVR = value

    @property
    def SelectorSequencePointer(self) -> Optional[List[int]]:
        if "SelectorSequencePointer" in self._dataset:
            return self._dataset.SelectorSequencePointer
        return None

    @SelectorSequencePointer.setter
    def SelectorSequencePointer(self, value: Optional[List[int]]):
        if value is None:
            if "SelectorSequencePointer" in self._dataset:
                del self._dataset.SelectorSequencePointer
        else:
            self._dataset.SelectorSequencePointer = value

    @property
    def SelectorSequencePointerPrivateCreator(self) -> Optional[List[str]]:
        if "SelectorSequencePointerPrivateCreator" in self._dataset:
            return self._dataset.SelectorSequencePointerPrivateCreator
        return None

    @SelectorSequencePointerPrivateCreator.setter
    def SelectorSequencePointerPrivateCreator(self, value: Optional[List[str]]):
        if value is None:
            if "SelectorSequencePointerPrivateCreator" in self._dataset:
                del self._dataset.SelectorSequencePointerPrivateCreator
        else:
            self._dataset.SelectorSequencePointerPrivateCreator = value

    @property
    def SelectorAttributePrivateCreator(self) -> Optional[str]:
        if "SelectorAttributePrivateCreator" in self._dataset:
            return self._dataset.SelectorAttributePrivateCreator
        return None

    @SelectorAttributePrivateCreator.setter
    def SelectorAttributePrivateCreator(self, value: Optional[str]):
        if value is None:
            if "SelectorAttributePrivateCreator" in self._dataset:
                del self._dataset.SelectorAttributePrivateCreator
        else:
            self._dataset.SelectorAttributePrivateCreator = value

    @property
    def SelectorSequencePointerItems(self) -> Optional[List[int]]:
        if "SelectorSequencePointerItems" in self._dataset:
            return self._dataset.SelectorSequencePointerItems
        return None

    @SelectorSequencePointerItems.setter
    def SelectorSequencePointerItems(self, value: Optional[List[int]]):
        if value is None:
            if "SelectorSequencePointerItems" in self._dataset:
                del self._dataset.SelectorSequencePointerItems
        else:
            self._dataset.SelectorSequencePointerItems = value

    @property
    def SelectorAttributeName(self) -> Optional[str]:
        if "SelectorAttributeName" in self._dataset:
            return self._dataset.SelectorAttributeName
        return None

    @SelectorAttributeName.setter
    def SelectorAttributeName(self, value: Optional[str]):
        if value is None:
            if "SelectorAttributeName" in self._dataset:
                del self._dataset.SelectorAttributeName
        else:
            self._dataset.SelectorAttributeName = value

    @property
    def SelectorAttributeKeyword(self) -> Optional[str]:
        if "SelectorAttributeKeyword" in self._dataset:
            return self._dataset.SelectorAttributeKeyword
        return None

    @SelectorAttributeKeyword.setter
    def SelectorAttributeKeyword(self, value: Optional[str]):
        if value is None:
            if "SelectorAttributeKeyword" in self._dataset:
                del self._dataset.SelectorAttributeKeyword
        else:
            self._dataset.SelectorAttributeKeyword = value

    @property
    def ConstraintType(self) -> Optional[str]:
        if "ConstraintType" in self._dataset:
            return self._dataset.ConstraintType
        return None

    @ConstraintType.setter
    def ConstraintType(self, value: Optional[str]):
        if value is None:
            if "ConstraintType" in self._dataset:
                del self._dataset.ConstraintType
        else:
            self._dataset.ConstraintType = value

    @property
    def SpecificationSelectionGuidance(self) -> Optional[str]:
        if "SpecificationSelectionGuidance" in self._dataset:
            return self._dataset.SpecificationSelectionGuidance
        return None

    @SpecificationSelectionGuidance.setter
    def SpecificationSelectionGuidance(self, value: Optional[str]):
        if value is None:
            if "SpecificationSelectionGuidance" in self._dataset:
                del self._dataset.SpecificationSelectionGuidance
        else:
            self._dataset.SpecificationSelectionGuidance = value

    @property
    def ConstraintValueSequence(self) -> Optional[List[ConstraintValueSequenceItem]]:
        if "ConstraintValueSequence" in self._dataset:
            if len(self._ConstraintValueSequence) == len(self._dataset.ConstraintValueSequence):
                return self._ConstraintValueSequence
            else:
                return [ConstraintValueSequenceItem(x) for x in self._dataset.ConstraintValueSequence]
        return None

    @ConstraintValueSequence.setter
    def ConstraintValueSequence(self, value: Optional[List[ConstraintValueSequenceItem]]):
        if value is None:
            self._ConstraintValueSequence = []
            if "ConstraintValueSequence" in self._dataset:
                del self._dataset.ConstraintValueSequence
        elif not isinstance(value, list) or not all(isinstance(item, ConstraintValueSequenceItem) for item in value):
            raise ValueError("ConstraintValueSequence must be a list of ConstraintValueSequenceItem objects")
        else:
            self._ConstraintValueSequence = value
            if "ConstraintValueSequence" not in self._dataset:
                self._dataset.ConstraintValueSequence = pydicom.Sequence()
            self._dataset.ConstraintValueSequence.clear()
            self._dataset.ConstraintValueSequence.extend([item.to_dataset() for item in value])

    def add_ConstraintValue(self, item: ConstraintValueSequenceItem):
        if not isinstance(item, ConstraintValueSequenceItem):
            raise ValueError("Item must be an instance of ConstraintValueSequenceItem")
        self._ConstraintValueSequence.append(item)
        if "ConstraintValueSequence" not in self._dataset:
            self._dataset.ConstraintValueSequence = pydicom.Sequence()
        self._dataset.ConstraintValueSequence.append(item.to_dataset())

    @property
    def RecommendedDefaultValueSequence(self) -> Optional[List[RecommendedDefaultValueSequenceItem]]:
        if "RecommendedDefaultValueSequence" in self._dataset:
            if len(self._RecommendedDefaultValueSequence) == len(self._dataset.RecommendedDefaultValueSequence):
                return self._RecommendedDefaultValueSequence
            else:
                return [RecommendedDefaultValueSequenceItem(x) for x in self._dataset.RecommendedDefaultValueSequence]
        return None

    @RecommendedDefaultValueSequence.setter
    def RecommendedDefaultValueSequence(self, value: Optional[List[RecommendedDefaultValueSequenceItem]]):
        if value is None:
            self._RecommendedDefaultValueSequence = []
            if "RecommendedDefaultValueSequence" in self._dataset:
                del self._dataset.RecommendedDefaultValueSequence
        elif not isinstance(value, list) or not all(isinstance(item, RecommendedDefaultValueSequenceItem) for item in value):
            raise ValueError("RecommendedDefaultValueSequence must be a list of RecommendedDefaultValueSequenceItem objects")
        else:
            self._RecommendedDefaultValueSequence = value
            if "RecommendedDefaultValueSequence" not in self._dataset:
                self._dataset.RecommendedDefaultValueSequence = pydicom.Sequence()
            self._dataset.RecommendedDefaultValueSequence.clear()
            self._dataset.RecommendedDefaultValueSequence.extend([item.to_dataset() for item in value])

    def add_RecommendedDefaultValue(self, item: RecommendedDefaultValueSequenceItem):
        if not isinstance(item, RecommendedDefaultValueSequenceItem):
            raise ValueError("Item must be an instance of RecommendedDefaultValueSequenceItem")
        self._RecommendedDefaultValueSequence.append(item)
        if "RecommendedDefaultValueSequence" not in self._dataset:
            self._dataset.RecommendedDefaultValueSequence = pydicom.Sequence()
        self._dataset.RecommendedDefaultValueSequence.append(item.to_dataset())

    @property
    def ConstraintViolationSignificance(self) -> Optional[str]:
        if "ConstraintViolationSignificance" in self._dataset:
            return self._dataset.ConstraintViolationSignificance
        return None

    @ConstraintViolationSignificance.setter
    def ConstraintViolationSignificance(self, value: Optional[str]):
        if value is None:
            if "ConstraintViolationSignificance" in self._dataset:
                del self._dataset.ConstraintViolationSignificance
        else:
            self._dataset.ConstraintViolationSignificance = value

    @property
    def ConstraintViolationCondition(self) -> Optional[str]:
        if "ConstraintViolationCondition" in self._dataset:
            return self._dataset.ConstraintViolationCondition
        return None

    @ConstraintViolationCondition.setter
    def ConstraintViolationCondition(self, value: Optional[str]):
        if value is None:
            if "ConstraintViolationCondition" in self._dataset:
                del self._dataset.ConstraintViolationCondition
        else:
            self._dataset.ConstraintViolationCondition = value
