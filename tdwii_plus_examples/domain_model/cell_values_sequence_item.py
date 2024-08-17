from decimal import Decimal
from typing import Any, List, Optional  # noqa

import pydicom

from .code_sequence_item import CodeSequenceItem


class CellValuesSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._MeasurementUnitsCodeSequence: List[CodeSequenceItem] = []
        self._ConceptCodeSequence: List[CodeSequenceItem] = []
        self._NumericValueQualifierCodeSequence: List[CodeSequenceItem] = []

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
            raise ValueError("ConceptCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._ConceptCodeSequence = value
            if "ConceptCodeSequence" not in self._dataset:
                self._dataset.ConceptCodeSequence = pydicom.Sequence()
            self._dataset.ConceptCodeSequence.clear()
            self._dataset.ConceptCodeSequence.extend([item.to_dataset() for item in value])

    def add_ConceptCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._ConceptCodeSequence.append(item)
        if "ConceptCodeSequence" not in self._dataset:
            self._dataset.ConceptCodeSequence = pydicom.Sequence()
        self._dataset.ConceptCodeSequence.append(item.to_dataset())

    @property
    def NumericValueQualifierCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "NumericValueQualifierCodeSequence" in self._dataset:
            if len(self._NumericValueQualifierCodeSequence) == len(self._dataset.NumericValueQualifierCodeSequence):
                return self._NumericValueQualifierCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.NumericValueQualifierCodeSequence]
        return None

    @NumericValueQualifierCodeSequence.setter
    def NumericValueQualifierCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._NumericValueQualifierCodeSequence = []
            if "NumericValueQualifierCodeSequence" in self._dataset:
                del self._dataset.NumericValueQualifierCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("NumericValueQualifierCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._NumericValueQualifierCodeSequence = value
            if "NumericValueQualifierCodeSequence" not in self._dataset:
                self._dataset.NumericValueQualifierCodeSequence = pydicom.Sequence()
            self._dataset.NumericValueQualifierCodeSequence.clear()
            self._dataset.NumericValueQualifierCodeSequence.extend([item.to_dataset() for item in value])

    def add_NumericValueQualifierCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._NumericValueQualifierCodeSequence.append(item)
        if "NumericValueQualifierCodeSequence" not in self._dataset:
            self._dataset.NumericValueQualifierCodeSequence = pydicom.Sequence()
        self._dataset.NumericValueQualifierCodeSequence.append(item.to_dataset())

    @property
    def TableRowNumber(self) -> Optional[int]:
        if "TableRowNumber" in self._dataset:
            return self._dataset.TableRowNumber
        return None

    @TableRowNumber.setter
    def TableRowNumber(self, value: Optional[int]):
        if value is None:
            if "TableRowNumber" in self._dataset:
                del self._dataset.TableRowNumber
        else:
            self._dataset.TableRowNumber = value

    @property
    def TableColumnNumber(self) -> Optional[int]:
        if "TableColumnNumber" in self._dataset:
            return self._dataset.TableColumnNumber
        return None

    @TableColumnNumber.setter
    def TableColumnNumber(self, value: Optional[int]):
        if value is None:
            if "TableColumnNumber" in self._dataset:
                del self._dataset.TableColumnNumber
        else:
            self._dataset.TableColumnNumber = value

    @property
    def ReferencedContentItemIdentifier(self) -> Optional[List[int]]:
        if "ReferencedContentItemIdentifier" in self._dataset:
            return self._dataset.ReferencedContentItemIdentifier
        return None

    @ReferencedContentItemIdentifier.setter
    def ReferencedContentItemIdentifier(self, value: Optional[List[int]]):
        if value is None:
            if "ReferencedContentItemIdentifier" in self._dataset:
                del self._dataset.ReferencedContentItemIdentifier
        else:
            self._dataset.ReferencedContentItemIdentifier = value

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
    def SelectorDTValue(self) -> Optional[List[str]]:
        if "SelectorDTValue" in self._dataset:
            return self._dataset.SelectorDTValue
        return None

    @SelectorDTValue.setter
    def SelectorDTValue(self, value: Optional[List[str]]):
        if value is None:
            if "SelectorDTValue" in self._dataset:
                del self._dataset.SelectorDTValue
        else:
            self._dataset.SelectorDTValue = value

    @property
    def SelectorISValue(self) -> Optional[List[int]]:
        if "SelectorISValue" in self._dataset:
            return self._dataset.SelectorISValue
        return None

    @SelectorISValue.setter
    def SelectorISValue(self, value: Optional[List[int]]):
        if value is None:
            if "SelectorISValue" in self._dataset:
                del self._dataset.SelectorISValue
        else:
            self._dataset.SelectorISValue = value

    @property
    def SelectorUCValue(self) -> Optional[List[str]]:
        if "SelectorUCValue" in self._dataset:
            return self._dataset.SelectorUCValue
        return None

    @SelectorUCValue.setter
    def SelectorUCValue(self, value: Optional[List[str]]):
        if value is None:
            if "SelectorUCValue" in self._dataset:
                del self._dataset.SelectorUCValue
        else:
            self._dataset.SelectorUCValue = value

    @property
    def SelectorDSValue(self) -> Optional[List[Decimal]]:
        if "SelectorDSValue" in self._dataset:
            return self._dataset.SelectorDSValue
        return None

    @SelectorDSValue.setter
    def SelectorDSValue(self, value: Optional[List[Decimal]]):
        if value is None:
            if "SelectorDSValue" in self._dataset:
                del self._dataset.SelectorDSValue
        else:
            self._dataset.SelectorDSValue = value

    @property
    def SelectorFDValue(self) -> Optional[List[float]]:
        if "SelectorFDValue" in self._dataset:
            return self._dataset.SelectorFDValue
        return None

    @SelectorFDValue.setter
    def SelectorFDValue(self, value: Optional[List[float]]):
        if value is None:
            if "SelectorFDValue" in self._dataset:
                del self._dataset.SelectorFDValue
        else:
            self._dataset.SelectorFDValue = value

    @property
    def SelectorFLValue(self) -> Optional[List[float]]:
        if "SelectorFLValue" in self._dataset:
            return self._dataset.SelectorFLValue
        return None

    @SelectorFLValue.setter
    def SelectorFLValue(self, value: Optional[List[float]]):
        if value is None:
            if "SelectorFLValue" in self._dataset:
                del self._dataset.SelectorFLValue
        else:
            self._dataset.SelectorFLValue = value

    @property
    def SelectorULValue(self) -> Optional[List[int]]:
        if "SelectorULValue" in self._dataset:
            return self._dataset.SelectorULValue
        return None

    @SelectorULValue.setter
    def SelectorULValue(self, value: Optional[List[int]]):
        if value is None:
            if "SelectorULValue" in self._dataset:
                del self._dataset.SelectorULValue
        else:
            self._dataset.SelectorULValue = value

    @property
    def SelectorUSValue(self) -> Optional[List[int]]:
        if "SelectorUSValue" in self._dataset:
            return self._dataset.SelectorUSValue
        return None

    @SelectorUSValue.setter
    def SelectorUSValue(self, value: Optional[List[int]]):
        if value is None:
            if "SelectorUSValue" in self._dataset:
                del self._dataset.SelectorUSValue
        else:
            self._dataset.SelectorUSValue = value

    @property
    def SelectorSLValue(self) -> Optional[List[int]]:
        if "SelectorSLValue" in self._dataset:
            return self._dataset.SelectorSLValue
        return None

    @SelectorSLValue.setter
    def SelectorSLValue(self, value: Optional[List[int]]):
        if value is None:
            if "SelectorSLValue" in self._dataset:
                del self._dataset.SelectorSLValue
        else:
            self._dataset.SelectorSLValue = value

    @property
    def SelectorSSValue(self) -> Optional[List[int]]:
        if "SelectorSSValue" in self._dataset:
            return self._dataset.SelectorSSValue
        return None

    @SelectorSSValue.setter
    def SelectorSSValue(self, value: Optional[List[int]]):
        if value is None:
            if "SelectorSSValue" in self._dataset:
                del self._dataset.SelectorSSValue
        else:
            self._dataset.SelectorSSValue = value

    @property
    def SelectorSVValue(self) -> Optional[List[int]]:
        if "SelectorSVValue" in self._dataset:
            return self._dataset.SelectorSVValue
        return None

    @SelectorSVValue.setter
    def SelectorSVValue(self, value: Optional[List[int]]):
        if value is None:
            if "SelectorSVValue" in self._dataset:
                del self._dataset.SelectorSVValue
        else:
            self._dataset.SelectorSVValue = value

    @property
    def SelectorUVValue(self) -> Optional[List[int]]:
        if "SelectorUVValue" in self._dataset:
            return self._dataset.SelectorUVValue
        return None

    @SelectorUVValue.setter
    def SelectorUVValue(self, value: Optional[List[int]]):
        if value is None:
            if "SelectorUVValue" in self._dataset:
                del self._dataset.SelectorUVValue
        else:
            self._dataset.SelectorUVValue = value
