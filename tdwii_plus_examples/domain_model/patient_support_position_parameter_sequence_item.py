from decimal import Decimal
from typing import Any, List, Optional

import pydicom

from .code_sequence_item import CodeSequenceItem
from .referenced_sop_sequence_item import ReferencedSOPSequenceItem


class PatientSupportPositionParameterSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._ReferencedSOPSequence: List[ReferencedSOPSequenceItem] = []
        self._MeasurementUnitsCodeSequence: List[CodeSequenceItem] = []
        self._ConceptNameCodeSequence: List[CodeSequenceItem] = []
        self._ConceptCodeSequence: List[CodeSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ReferencedSOPSequence(self) -> Optional[List[ReferencedSOPSequenceItem]]:
        if "ReferencedSOPSequence" in self._dataset:
            if len(self._ReferencedSOPSequence) == len(self._dataset.ReferencedSOPSequence):
                return self._ReferencedSOPSequence
            else:
                return [ReferencedSOPSequenceItem(x) for x in self._dataset.ReferencedSOPSequence]
        return None

    @ReferencedSOPSequence.setter
    def ReferencedSOPSequence(self, value: Optional[List[ReferencedSOPSequenceItem]]):
        if value is None:
            self._ReferencedSOPSequence = []
            if "ReferencedSOPSequence" in self._dataset:
                del self._dataset.ReferencedSOPSequence
        elif not isinstance(value, list) or not all(isinstance(item, ReferencedSOPSequenceItem) for item in value):
            raise ValueError(f"ReferencedSOPSequence must be a list of ReferencedSOPSequenceItem objects")
        else:
            self._ReferencedSOPSequence = value
            if "ReferencedSOPSequence" not in self._dataset:
                self._dataset.ReferencedSOPSequence = pydicom.Sequence()
            self._dataset.ReferencedSOPSequence.clear()
            self._dataset.ReferencedSOPSequence.extend([item.to_dataset() for item in value])

    def add_ReferencedSOP(self, item: ReferencedSOPSequenceItem):
        if not isinstance(item, ReferencedSOPSequenceItem):
            raise ValueError(f"Item must be an instance of ReferencedSOPSequenceItem")
        self._ReferencedSOPSequence.append(item)
        if "ReferencedSOPSequence" not in self._dataset:
            self._dataset.ReferencedSOPSequence = pydicom.Sequence()
        self._dataset.ReferencedSOPSequence.append(item.to_dataset())

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
            raise ValueError(f"MeasurementUnitsCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._MeasurementUnitsCodeSequence = value
            if "MeasurementUnitsCodeSequence" not in self._dataset:
                self._dataset.MeasurementUnitsCodeSequence = pydicom.Sequence()
            self._dataset.MeasurementUnitsCodeSequence.clear()
            self._dataset.MeasurementUnitsCodeSequence.extend([item.to_dataset() for item in value])

    def add_MeasurementUnitsCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError(f"Item must be an instance of CodeSequenceItem")
        self._MeasurementUnitsCodeSequence.append(item)
        if "MeasurementUnitsCodeSequence" not in self._dataset:
            self._dataset.MeasurementUnitsCodeSequence = pydicom.Sequence()
        self._dataset.MeasurementUnitsCodeSequence.append(item.to_dataset())

    @property
    def ObservationDateTime(self) -> Optional[str]:
        if "ObservationDateTime" in self._dataset:
            return self._dataset.ObservationDateTime
        return None

    @ObservationDateTime.setter
    def ObservationDateTime(self, value: Optional[str]):
        if value is None:
            if "ObservationDateTime" in self._dataset:
                del self._dataset.ObservationDateTime
        else:
            self._dataset.ObservationDateTime = value

    @property
    def ObservationStartDateTime(self) -> Optional[str]:
        if "ObservationStartDateTime" in self._dataset:
            return self._dataset.ObservationStartDateTime
        return None

    @ObservationStartDateTime.setter
    def ObservationStartDateTime(self, value: Optional[str]):
        if value is None:
            if "ObservationStartDateTime" in self._dataset:
                del self._dataset.ObservationStartDateTime
        else:
            self._dataset.ObservationStartDateTime = value

    @property
    def ValueType(self) -> Optional[str]:
        if "ValueType" in self._dataset:
            return self._dataset.ValueType
        return None

    @ValueType.setter
    def ValueType(self, value: Optional[str]):
        if value is None:
            if "ValueType" in self._dataset:
                del self._dataset.ValueType
        else:
            self._dataset.ValueType = value

    @property
    def ConceptNameCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "ConceptNameCodeSequence" in self._dataset:
            if len(self._ConceptNameCodeSequence) == len(self._dataset.ConceptNameCodeSequence):
                return self._ConceptNameCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.ConceptNameCodeSequence]
        return None

    @ConceptNameCodeSequence.setter
    def ConceptNameCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._ConceptNameCodeSequence = []
            if "ConceptNameCodeSequence" in self._dataset:
                del self._dataset.ConceptNameCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError(f"ConceptNameCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._ConceptNameCodeSequence = value
            if "ConceptNameCodeSequence" not in self._dataset:
                self._dataset.ConceptNameCodeSequence = pydicom.Sequence()
            self._dataset.ConceptNameCodeSequence.clear()
            self._dataset.ConceptNameCodeSequence.extend([item.to_dataset() for item in value])

    def add_ConceptNameCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError(f"Item must be an instance of CodeSequenceItem")
        self._ConceptNameCodeSequence.append(item)
        if "ConceptNameCodeSequence" not in self._dataset:
            self._dataset.ConceptNameCodeSequence = pydicom.Sequence()
        self._dataset.ConceptNameCodeSequence.append(item.to_dataset())

    @property
    def DateTime(self) -> Optional[str]:
        if "DateTime" in self._dataset:
            return self._dataset.DateTime
        return None

    @DateTime.setter
    def DateTime(self, value: Optional[str]):
        if value is None:
            if "DateTime" in self._dataset:
                del self._dataset.DateTime
        else:
            self._dataset.DateTime = value

    @property
    def Date(self) -> Optional[str]:
        if "Date" in self._dataset:
            return self._dataset.Date
        return None

    @Date.setter
    def Date(self, value: Optional[str]):
        if value is None:
            if "Date" in self._dataset:
                del self._dataset.Date
        else:
            self._dataset.Date = value

    @property
    def Time(self) -> Optional[str]:
        if "Time" in self._dataset:
            return self._dataset.Time
        return None

    @Time.setter
    def Time(self, value: Optional[str]):
        if value is None:
            if "Time" in self._dataset:
                del self._dataset.Time
        else:
            self._dataset.Time = value

    @property
    def PersonName(self) -> Optional[str]:
        if "PersonName" in self._dataset:
            return self._dataset.PersonName
        return None

    @PersonName.setter
    def PersonName(self, value: Optional[str]):
        if value is None:
            if "PersonName" in self._dataset:
                del self._dataset.PersonName
        else:
            self._dataset.PersonName = value

    @property
    def UID(self) -> Optional[str]:
        if "UID" in self._dataset:
            return self._dataset.UID
        return None

    @UID.setter
    def UID(self, value: Optional[str]):
        if value is None:
            if "UID" in self._dataset:
                del self._dataset.UID
        else:
            self._dataset.UID = value

    @property
    def TextValue(self) -> Optional[str]:
        if "TextValue" in self._dataset:
            return self._dataset.TextValue
        return None

    @TextValue.setter
    def TextValue(self, value: Optional[str]):
        if value is None:
            if "TextValue" in self._dataset:
                del self._dataset.TextValue
        else:
            self._dataset.TextValue = value

    @property
    def FloatingPointValue(self) -> Optional[List[float]]:
        if "FloatingPointValue" in self._dataset:
            return self._dataset.FloatingPointValue
        return None

    @FloatingPointValue.setter
    def FloatingPointValue(self, value: Optional[List[float]]):
        if value is None:
            if "FloatingPointValue" in self._dataset:
                del self._dataset.FloatingPointValue
        else:
            self._dataset.FloatingPointValue = value

    @property
    def RationalNumeratorValue(self) -> Optional[List[int]]:
        if "RationalNumeratorValue" in self._dataset:
            return self._dataset.RationalNumeratorValue
        return None

    @RationalNumeratorValue.setter
    def RationalNumeratorValue(self, value: Optional[List[int]]):
        if value is None:
            if "RationalNumeratorValue" in self._dataset:
                del self._dataset.RationalNumeratorValue
        else:
            self._dataset.RationalNumeratorValue = value

    @property
    def RationalDenominatorValue(self) -> Optional[List[int]]:
        if "RationalDenominatorValue" in self._dataset:
            return self._dataset.RationalDenominatorValue
        return None

    @RationalDenominatorValue.setter
    def RationalDenominatorValue(self, value: Optional[List[int]]):
        if value is None:
            if "RationalDenominatorValue" in self._dataset:
                del self._dataset.RationalDenominatorValue
        else:
            self._dataset.RationalDenominatorValue = value

    @property
    def ConceptCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "ConceptCodeSequence" in self._dataset:
            if len(self._ConceptCodeSequence) == len(self._dataset.ConceptCodeSequence):
                return self._ConceptCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.ConceptCodeSequence]
        return None

    @ConceptCodeSequence.setter
    def ConceptCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._ConceptCodeSequence = []
            if "ConceptCodeSequence" in self._dataset:
                del self._dataset.ConceptCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError(f"ConceptCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._ConceptCodeSequence = value
            if "ConceptCodeSequence" not in self._dataset:
                self._dataset.ConceptCodeSequence = pydicom.Sequence()
            self._dataset.ConceptCodeSequence.clear()
            self._dataset.ConceptCodeSequence.extend([item.to_dataset() for item in value])

    def add_ConceptCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError(f"Item must be an instance of CodeSequenceItem")
        self._ConceptCodeSequence.append(item)
        if "ConceptCodeSequence" not in self._dataset:
            self._dataset.ConceptCodeSequence = pydicom.Sequence()
        self._dataset.ConceptCodeSequence.append(item.to_dataset())

    @property
    def NumericValue(self) -> Optional[List[Decimal]]:
        if "NumericValue" in self._dataset:
            return self._dataset.NumericValue
        return None

    @NumericValue.setter
    def NumericValue(self, value: Optional[List[Decimal]]):
        if value is None:
            if "NumericValue" in self._dataset:
                del self._dataset.NumericValue
        else:
            self._dataset.NumericValue = value

    @property
    def PatientSupportPositionParameterOrderIndex(self) -> Optional[int]:
        if "PatientSupportPositionParameterOrderIndex" in self._dataset:
            return self._dataset.PatientSupportPositionParameterOrderIndex
        return None

    @PatientSupportPositionParameterOrderIndex.setter
    def PatientSupportPositionParameterOrderIndex(self, value: Optional[int]):
        if value is None:
            if "PatientSupportPositionParameterOrderIndex" in self._dataset:
                del self._dataset.PatientSupportPositionParameterOrderIndex
        else:
            self._dataset.PatientSupportPositionParameterOrderIndex = value
