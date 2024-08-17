from typing import Any, List, Optional  # noqa

import pydicom

from .code_sequence_item import CodeSequenceItem
from .quantity_definition_sequence_item import QuantityDefinitionSequenceItem


class RealWorldValueMappingSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._MeasurementUnitsCodeSequence: List[CodeSequenceItem] = []
        self._QuantityDefinitionSequence: List[QuantityDefinitionSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def LUTExplanation(self) -> Optional[str]:
        if "LUTExplanation" in self._dataset:
            return self._dataset.LUTExplanation
        return None

    @LUTExplanation.setter
    def LUTExplanation(self, value: Optional[str]):
        if value is None:
            if "LUTExplanation" in self._dataset:
                del self._dataset.LUTExplanation
        else:
            self._dataset.LUTExplanation = value

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
    def LUTLabel(self) -> Optional[str]:
        if "LUTLabel" in self._dataset:
            return self._dataset.LUTLabel
        return None

    @LUTLabel.setter
    def LUTLabel(self, value: Optional[str]):
        if value is None:
            if "LUTLabel" in self._dataset:
                del self._dataset.LUTLabel
        else:
            self._dataset.LUTLabel = value

    @property
    def RealWorldValueLastValueMapped(self) -> Optional[int]:
        if "RealWorldValueLastValueMapped" in self._dataset:
            return self._dataset.RealWorldValueLastValueMapped
        return None

    @RealWorldValueLastValueMapped.setter
    def RealWorldValueLastValueMapped(self, value: Optional[int]):
        if value is None:
            if "RealWorldValueLastValueMapped" in self._dataset:
                del self._dataset.RealWorldValueLastValueMapped
        else:
            self._dataset.RealWorldValueLastValueMapped = value

    @property
    def RealWorldValueLUTData(self) -> Optional[List[float]]:
        if "RealWorldValueLUTData" in self._dataset:
            return self._dataset.RealWorldValueLUTData
        return None

    @RealWorldValueLUTData.setter
    def RealWorldValueLUTData(self, value: Optional[List[float]]):
        if value is None:
            if "RealWorldValueLUTData" in self._dataset:
                del self._dataset.RealWorldValueLUTData
        else:
            self._dataset.RealWorldValueLUTData = value

    @property
    def DoubleFloatRealWorldValueLastValueMapped(self) -> Optional[float]:
        if "DoubleFloatRealWorldValueLastValueMapped" in self._dataset:
            return self._dataset.DoubleFloatRealWorldValueLastValueMapped
        return None

    @DoubleFloatRealWorldValueLastValueMapped.setter
    def DoubleFloatRealWorldValueLastValueMapped(self, value: Optional[float]):
        if value is None:
            if "DoubleFloatRealWorldValueLastValueMapped" in self._dataset:
                del self._dataset.DoubleFloatRealWorldValueLastValueMapped
        else:
            self._dataset.DoubleFloatRealWorldValueLastValueMapped = value

    @property
    def DoubleFloatRealWorldValueFirstValueMapped(self) -> Optional[float]:
        if "DoubleFloatRealWorldValueFirstValueMapped" in self._dataset:
            return self._dataset.DoubleFloatRealWorldValueFirstValueMapped
        return None

    @DoubleFloatRealWorldValueFirstValueMapped.setter
    def DoubleFloatRealWorldValueFirstValueMapped(self, value: Optional[float]):
        if value is None:
            if "DoubleFloatRealWorldValueFirstValueMapped" in self._dataset:
                del self._dataset.DoubleFloatRealWorldValueFirstValueMapped
        else:
            self._dataset.DoubleFloatRealWorldValueFirstValueMapped = value

    @property
    def RealWorldValueFirstValueMapped(self) -> Optional[int]:
        if "RealWorldValueFirstValueMapped" in self._dataset:
            return self._dataset.RealWorldValueFirstValueMapped
        return None

    @RealWorldValueFirstValueMapped.setter
    def RealWorldValueFirstValueMapped(self, value: Optional[int]):
        if value is None:
            if "RealWorldValueFirstValueMapped" in self._dataset:
                del self._dataset.RealWorldValueFirstValueMapped
        else:
            self._dataset.RealWorldValueFirstValueMapped = value

    @property
    def QuantityDefinitionSequence(self) -> Optional[List[QuantityDefinitionSequenceItem]]:
        if "QuantityDefinitionSequence" in self._dataset:
            if len(self._QuantityDefinitionSequence) == len(self._dataset.QuantityDefinitionSequence):
                return self._QuantityDefinitionSequence
            else:
                return [QuantityDefinitionSequenceItem(x) for x in self._dataset.QuantityDefinitionSequence]
        return None

    @QuantityDefinitionSequence.setter
    def QuantityDefinitionSequence(self, value: Optional[List[QuantityDefinitionSequenceItem]]):
        if value is None:
            self._QuantityDefinitionSequence = []
            if "QuantityDefinitionSequence" in self._dataset:
                del self._dataset.QuantityDefinitionSequence
        elif not isinstance(value, list) or not all(isinstance(item, QuantityDefinitionSequenceItem) for item in value):
            raise ValueError("QuantityDefinitionSequence must be a list of QuantityDefinitionSequenceItem objects")
        else:
            self._QuantityDefinitionSequence = value
            if "QuantityDefinitionSequence" not in self._dataset:
                self._dataset.QuantityDefinitionSequence = pydicom.Sequence()
            self._dataset.QuantityDefinitionSequence.clear()
            self._dataset.QuantityDefinitionSequence.extend([item.to_dataset() for item in value])

    def add_QuantityDefinition(self, item: QuantityDefinitionSequenceItem):
        if not isinstance(item, QuantityDefinitionSequenceItem):
            raise ValueError("Item must be an instance of QuantityDefinitionSequenceItem")
        self._QuantityDefinitionSequence.append(item)
        if "QuantityDefinitionSequence" not in self._dataset:
            self._dataset.QuantityDefinitionSequence = pydicom.Sequence()
        self._dataset.QuantityDefinitionSequence.append(item.to_dataset())

    @property
    def RealWorldValueIntercept(self) -> Optional[float]:
        if "RealWorldValueIntercept" in self._dataset:
            return self._dataset.RealWorldValueIntercept
        return None

    @RealWorldValueIntercept.setter
    def RealWorldValueIntercept(self, value: Optional[float]):
        if value is None:
            if "RealWorldValueIntercept" in self._dataset:
                del self._dataset.RealWorldValueIntercept
        else:
            self._dataset.RealWorldValueIntercept = value

    @property
    def RealWorldValueSlope(self) -> Optional[float]:
        if "RealWorldValueSlope" in self._dataset:
            return self._dataset.RealWorldValueSlope
        return None

    @RealWorldValueSlope.setter
    def RealWorldValueSlope(self, value: Optional[float]):
        if value is None:
            if "RealWorldValueSlope" in self._dataset:
                del self._dataset.RealWorldValueSlope
        else:
            self._dataset.RealWorldValueSlope = value
