from decimal import Decimal
from typing import Any, List, Optional

import pydicom

from .code_sequence_item import CodeSequenceItem


class WaveformAnnotationSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._MeasurementUnitsCodeSequence: List[CodeSequenceItem] = []
        self._ConceptNameCodeSequence: List[CodeSequenceItem] = []
        self._ConceptCodeSequence: List[CodeSequenceItem] = []

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
    def ReferencedWaveformChannels(self) -> Optional[List[int]]:
        if "ReferencedWaveformChannels" in self._dataset:
            return self._dataset.ReferencedWaveformChannels
        return None

    @ReferencedWaveformChannels.setter
    def ReferencedWaveformChannels(self, value: Optional[List[int]]):
        if value is None:
            if "ReferencedWaveformChannels" in self._dataset:
                del self._dataset.ReferencedWaveformChannels
        else:
            self._dataset.ReferencedWaveformChannels = value

    @property
    def TemporalRangeType(self) -> Optional[str]:
        if "TemporalRangeType" in self._dataset:
            return self._dataset.TemporalRangeType
        return None

    @TemporalRangeType.setter
    def TemporalRangeType(self, value: Optional[str]):
        if value is None:
            if "TemporalRangeType" in self._dataset:
                del self._dataset.TemporalRangeType
        else:
            self._dataset.TemporalRangeType = value

    @property
    def ReferencedSamplePositions(self) -> Optional[List[int]]:
        if "ReferencedSamplePositions" in self._dataset:
            return self._dataset.ReferencedSamplePositions
        return None

    @ReferencedSamplePositions.setter
    def ReferencedSamplePositions(self, value: Optional[List[int]]):
        if value is None:
            if "ReferencedSamplePositions" in self._dataset:
                del self._dataset.ReferencedSamplePositions
        else:
            self._dataset.ReferencedSamplePositions = value

    @property
    def ReferencedTimeOffsets(self) -> Optional[List[Decimal]]:
        if "ReferencedTimeOffsets" in self._dataset:
            return self._dataset.ReferencedTimeOffsets
        return None

    @ReferencedTimeOffsets.setter
    def ReferencedTimeOffsets(self, value: Optional[List[Decimal]]):
        if value is None:
            if "ReferencedTimeOffsets" in self._dataset:
                del self._dataset.ReferencedTimeOffsets
        else:
            self._dataset.ReferencedTimeOffsets = value

    @property
    def ReferencedDateTime(self) -> Optional[List[str]]:
        if "ReferencedDateTime" in self._dataset:
            return self._dataset.ReferencedDateTime
        return None

    @ReferencedDateTime.setter
    def ReferencedDateTime(self, value: Optional[List[str]]):
        if value is None:
            if "ReferencedDateTime" in self._dataset:
                del self._dataset.ReferencedDateTime
        else:
            self._dataset.ReferencedDateTime = value

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
    def AnnotationGroupNumber(self) -> Optional[int]:
        if "AnnotationGroupNumber" in self._dataset:
            return self._dataset.AnnotationGroupNumber
        return None

    @AnnotationGroupNumber.setter
    def AnnotationGroupNumber(self, value: Optional[int]):
        if value is None:
            if "AnnotationGroupNumber" in self._dataset:
                del self._dataset.AnnotationGroupNumber
        else:
            self._dataset.AnnotationGroupNumber = value

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
    def UnformattedTextValue(self) -> Optional[str]:
        if "UnformattedTextValue" in self._dataset:
            return self._dataset.UnformattedTextValue
        return None

    @UnformattedTextValue.setter
    def UnformattedTextValue(self, value: Optional[str]):
        if value is None:
            if "UnformattedTextValue" in self._dataset:
                del self._dataset.UnformattedTextValue
        else:
            self._dataset.UnformattedTextValue = value
