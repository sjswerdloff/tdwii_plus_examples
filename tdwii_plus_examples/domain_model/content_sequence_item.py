from decimal import Decimal
from typing import Any, List, Optional  # noqa

import pydicom

from .code_sequence_item import CodeSequenceItem
from .content_template_sequence_item import ContentTemplateSequenceItem
from .measured_value_sequence_item import MeasuredValueSequenceItem
from .referenced_sop_sequence_item import ReferencedSOPSequenceItem
from .tabulated_values_sequence_item import TabulatedValuesSequenceItem


class ContentSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._ReferencedSOPSequence: List[ReferencedSOPSequenceItem] = []
        self._ConceptNameCodeSequence: List[CodeSequenceItem] = []
        self._ConceptCodeSequence: List[CodeSequenceItem] = []
        self._MeasuredValueSequence: List[MeasuredValueSequenceItem] = []
        self._NumericValueQualifierCodeSequence: List[CodeSequenceItem] = []
        self._ContentTemplateSequence: List[ContentTemplateSequenceItem] = []
        self._TabulatedValuesSequence: List[TabulatedValuesSequenceItem] = []

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
            raise ValueError("ReferencedSOPSequence must be a list of ReferencedSOPSequenceItem objects")
        else:
            self._ReferencedSOPSequence = value
            if "ReferencedSOPSequence" not in self._dataset:
                self._dataset.ReferencedSOPSequence = pydicom.Sequence()
            self._dataset.ReferencedSOPSequence.clear()
            self._dataset.ReferencedSOPSequence.extend([item.to_dataset() for item in value])

    def add_ReferencedSOP(self, item: ReferencedSOPSequenceItem):
        if not isinstance(item, ReferencedSOPSequenceItem):
            raise ValueError("Item must be an instance of ReferencedSOPSequenceItem")
        self._ReferencedSOPSequence.append(item)
        if "ReferencedSOPSequence" not in self._dataset:
            self._dataset.ReferencedSOPSequence = pydicom.Sequence()
        self._dataset.ReferencedSOPSequence.append(item.to_dataset())

    @property
    def RelationshipType(self) -> Optional[str]:
        if "RelationshipType" in self._dataset:
            return self._dataset.RelationshipType
        return None

    @RelationshipType.setter
    def RelationshipType(self, value: Optional[str]):
        if value is None:
            if "RelationshipType" in self._dataset:
                del self._dataset.RelationshipType
        else:
            self._dataset.RelationshipType = value

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
            raise ValueError("ConceptNameCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._ConceptNameCodeSequence = value
            if "ConceptNameCodeSequence" not in self._dataset:
                self._dataset.ConceptNameCodeSequence = pydicom.Sequence()
            self._dataset.ConceptNameCodeSequence.clear()
            self._dataset.ConceptNameCodeSequence.extend([item.to_dataset() for item in value])

    def add_ConceptNameCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._ConceptNameCodeSequence.append(item)
        if "ConceptNameCodeSequence" not in self._dataset:
            self._dataset.ConceptNameCodeSequence = pydicom.Sequence()
        self._dataset.ConceptNameCodeSequence.append(item.to_dataset())

    @property
    def ContinuityOfContent(self) -> Optional[str]:
        if "ContinuityOfContent" in self._dataset:
            return self._dataset.ContinuityOfContent
        return None

    @ContinuityOfContent.setter
    def ContinuityOfContent(self, value: Optional[str]):
        if value is None:
            if "ContinuityOfContent" in self._dataset:
                del self._dataset.ContinuityOfContent
        else:
            self._dataset.ContinuityOfContent = value

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
    def MeasuredValueSequence(self) -> Optional[List[MeasuredValueSequenceItem]]:
        if "MeasuredValueSequence" in self._dataset:
            if len(self._MeasuredValueSequence) == len(self._dataset.MeasuredValueSequence):
                return self._MeasuredValueSequence
            else:
                return [MeasuredValueSequenceItem(x) for x in self._dataset.MeasuredValueSequence]
        return None

    @MeasuredValueSequence.setter
    def MeasuredValueSequence(self, value: Optional[List[MeasuredValueSequenceItem]]):
        if value is None:
            self._MeasuredValueSequence = []
            if "MeasuredValueSequence" in self._dataset:
                del self._dataset.MeasuredValueSequence
        elif not isinstance(value, list) or not all(isinstance(item, MeasuredValueSequenceItem) for item in value):
            raise ValueError("MeasuredValueSequence must be a list of MeasuredValueSequenceItem objects")
        else:
            self._MeasuredValueSequence = value
            if "MeasuredValueSequence" not in self._dataset:
                self._dataset.MeasuredValueSequence = pydicom.Sequence()
            self._dataset.MeasuredValueSequence.clear()
            self._dataset.MeasuredValueSequence.extend([item.to_dataset() for item in value])

    def add_MeasuredValue(self, item: MeasuredValueSequenceItem):
        if not isinstance(item, MeasuredValueSequenceItem):
            raise ValueError("Item must be an instance of MeasuredValueSequenceItem")
        self._MeasuredValueSequence.append(item)
        if "MeasuredValueSequence" not in self._dataset:
            self._dataset.MeasuredValueSequence = pydicom.Sequence()
        self._dataset.MeasuredValueSequence.append(item.to_dataset())

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
    def ContentTemplateSequence(self) -> Optional[List[ContentTemplateSequenceItem]]:
        if "ContentTemplateSequence" in self._dataset:
            if len(self._ContentTemplateSequence) == len(self._dataset.ContentTemplateSequence):
                return self._ContentTemplateSequence
            else:
                return [ContentTemplateSequenceItem(x) for x in self._dataset.ContentTemplateSequence]
        return None

    @ContentTemplateSequence.setter
    def ContentTemplateSequence(self, value: Optional[List[ContentTemplateSequenceItem]]):
        if value is None:
            self._ContentTemplateSequence = []
            if "ContentTemplateSequence" in self._dataset:
                del self._dataset.ContentTemplateSequence
        elif not isinstance(value, list) or not all(isinstance(item, ContentTemplateSequenceItem) for item in value):
            raise ValueError("ContentTemplateSequence must be a list of ContentTemplateSequenceItem objects")
        else:
            self._ContentTemplateSequence = value
            if "ContentTemplateSequence" not in self._dataset:
                self._dataset.ContentTemplateSequence = pydicom.Sequence()
            self._dataset.ContentTemplateSequence.clear()
            self._dataset.ContentTemplateSequence.extend([item.to_dataset() for item in value])

    def add_ContentTemplate(self, item: ContentTemplateSequenceItem):
        if not isinstance(item, ContentTemplateSequenceItem):
            raise ValueError("Item must be an instance of ContentTemplateSequenceItem")
        self._ContentTemplateSequence.append(item)
        if "ContentTemplateSequence" not in self._dataset:
            self._dataset.ContentTemplateSequence = pydicom.Sequence()
        self._dataset.ContentTemplateSequence.append(item.to_dataset())

    @property
    def TabulatedValuesSequence(self) -> Optional[List[TabulatedValuesSequenceItem]]:
        if "TabulatedValuesSequence" in self._dataset:
            if len(self._TabulatedValuesSequence) == len(self._dataset.TabulatedValuesSequence):
                return self._TabulatedValuesSequence
            else:
                return [TabulatedValuesSequenceItem(x) for x in self._dataset.TabulatedValuesSequence]
        return None

    @TabulatedValuesSequence.setter
    def TabulatedValuesSequence(self, value: Optional[List[TabulatedValuesSequenceItem]]):
        if value is None:
            self._TabulatedValuesSequence = []
            if "TabulatedValuesSequence" in self._dataset:
                del self._dataset.TabulatedValuesSequence
        elif not isinstance(value, list) or not all(isinstance(item, TabulatedValuesSequenceItem) for item in value):
            raise ValueError("TabulatedValuesSequence must be a list of TabulatedValuesSequenceItem objects")
        else:
            self._TabulatedValuesSequence = value
            if "TabulatedValuesSequence" not in self._dataset:
                self._dataset.TabulatedValuesSequence = pydicom.Sequence()
            self._dataset.TabulatedValuesSequence.clear()
            self._dataset.TabulatedValuesSequence.extend([item.to_dataset() for item in value])

    def add_TabulatedValues(self, item: TabulatedValuesSequenceItem):
        if not isinstance(item, TabulatedValuesSequenceItem):
            raise ValueError("Item must be an instance of TabulatedValuesSequenceItem")
        self._TabulatedValuesSequence.append(item)
        if "TabulatedValuesSequence" not in self._dataset:
            self._dataset.TabulatedValuesSequence = pydicom.Sequence()
        self._dataset.TabulatedValuesSequence.append(item.to_dataset())

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
    def PixelOriginInterpretation(self) -> Optional[str]:
        if "PixelOriginInterpretation" in self._dataset:
            return self._dataset.PixelOriginInterpretation
        return None

    @PixelOriginInterpretation.setter
    def PixelOriginInterpretation(self, value: Optional[str]):
        if value is None:
            if "PixelOriginInterpretation" in self._dataset:
                del self._dataset.PixelOriginInterpretation
        else:
            self._dataset.PixelOriginInterpretation = value

    @property
    def GraphicData(self) -> Optional[List[float]]:
        if "GraphicData" in self._dataset:
            return self._dataset.GraphicData
        return None

    @GraphicData.setter
    def GraphicData(self, value: Optional[List[float]]):
        if value is None:
            if "GraphicData" in self._dataset:
                del self._dataset.GraphicData
        else:
            self._dataset.GraphicData = value

    @property
    def GraphicType(self) -> Optional[str]:
        if "GraphicType" in self._dataset:
            return self._dataset.GraphicType
        return None

    @GraphicType.setter
    def GraphicType(self, value: Optional[str]):
        if value is None:
            if "GraphicType" in self._dataset:
                del self._dataset.GraphicType
        else:
            self._dataset.GraphicType = value

    @property
    def FiducialUID(self) -> Optional[str]:
        if "FiducialUID" in self._dataset:
            return self._dataset.FiducialUID
        return None

    @FiducialUID.setter
    def FiducialUID(self, value: Optional[str]):
        if value is None:
            if "FiducialUID" in self._dataset:
                del self._dataset.FiducialUID
        else:
            self._dataset.FiducialUID = value

    @property
    def ReferencedFrameOfReferenceUID(self) -> Optional[str]:
        if "ReferencedFrameOfReferenceUID" in self._dataset:
            return self._dataset.ReferencedFrameOfReferenceUID
        return None

    @ReferencedFrameOfReferenceUID.setter
    def ReferencedFrameOfReferenceUID(self, value: Optional[str]):
        if value is None:
            if "ReferencedFrameOfReferenceUID" in self._dataset:
                del self._dataset.ReferencedFrameOfReferenceUID
        else:
            self._dataset.ReferencedFrameOfReferenceUID = value
