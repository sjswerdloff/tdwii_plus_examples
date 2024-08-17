from typing import Any, List, Optional

import pydicom

from .anatomic_region_sequence_item import AnatomicRegionSequenceItem
from .annotation_group_algorithm_identification_sequence_item import (
    AnnotationGroupAlgorithmIdentificationSequenceItem,
)
from .code_sequence_item import CodeSequenceItem
from .measurements_sequence_item import MeasurementsSequenceItem
from .primary_anatomic_structure_sequence_item import (
    PrimaryAnatomicStructureSequenceItem,
)


class AnnotationGroupSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._AnatomicRegionSequence: List[AnatomicRegionSequenceItem] = []
        self._PrimaryAnatomicStructureSequence: List[PrimaryAnatomicStructureSequenceItem] = []
        self._MeasurementsSequence: List[MeasurementsSequenceItem] = []
        self._AnnotationGroupAlgorithmIdentificationSequence: List[AnnotationGroupAlgorithmIdentificationSequenceItem] = []
        self._AnnotationPropertyCategoryCodeSequence: List[CodeSequenceItem] = []
        self._AnnotationPropertyTypeCodeSequence: List[CodeSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def AnatomicRegionSequence(self) -> Optional[List[AnatomicRegionSequenceItem]]:
        if "AnatomicRegionSequence" in self._dataset:
            if len(self._AnatomicRegionSequence) == len(self._dataset.AnatomicRegionSequence):
                return self._AnatomicRegionSequence
            else:
                return [AnatomicRegionSequenceItem(x) for x in self._dataset.AnatomicRegionSequence]
        return None

    @AnatomicRegionSequence.setter
    def AnatomicRegionSequence(self, value: Optional[List[AnatomicRegionSequenceItem]]):
        if value is None:
            self._AnatomicRegionSequence = []
            if "AnatomicRegionSequence" in self._dataset:
                del self._dataset.AnatomicRegionSequence
        elif not isinstance(value, list) or not all(isinstance(item, AnatomicRegionSequenceItem) for item in value):
            raise ValueError(f"AnatomicRegionSequence must be a list of AnatomicRegionSequenceItem objects")
        else:
            self._AnatomicRegionSequence = value
            if "AnatomicRegionSequence" not in self._dataset:
                self._dataset.AnatomicRegionSequence = pydicom.Sequence()
            self._dataset.AnatomicRegionSequence.clear()
            self._dataset.AnatomicRegionSequence.extend([item.to_dataset() for item in value])

    def add_AnatomicRegion(self, item: AnatomicRegionSequenceItem):
        if not isinstance(item, AnatomicRegionSequenceItem):
            raise ValueError(f"Item must be an instance of AnatomicRegionSequenceItem")
        self._AnatomicRegionSequence.append(item)
        if "AnatomicRegionSequence" not in self._dataset:
            self._dataset.AnatomicRegionSequence = pydicom.Sequence()
        self._dataset.AnatomicRegionSequence.append(item.to_dataset())

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
            raise ValueError(
                f"PrimaryAnatomicStructureSequence must be a list of PrimaryAnatomicStructureSequenceItem objects"
            )
        else:
            self._PrimaryAnatomicStructureSequence = value
            if "PrimaryAnatomicStructureSequence" not in self._dataset:
                self._dataset.PrimaryAnatomicStructureSequence = pydicom.Sequence()
            self._dataset.PrimaryAnatomicStructureSequence.clear()
            self._dataset.PrimaryAnatomicStructureSequence.extend([item.to_dataset() for item in value])

    def add_PrimaryAnatomicStructure(self, item: PrimaryAnatomicStructureSequenceItem):
        if not isinstance(item, PrimaryAnatomicStructureSequenceItem):
            raise ValueError(f"Item must be an instance of PrimaryAnatomicStructureSequenceItem")
        self._PrimaryAnatomicStructureSequence.append(item)
        if "PrimaryAnatomicStructureSequence" not in self._dataset:
            self._dataset.PrimaryAnatomicStructureSequence = pydicom.Sequence()
        self._dataset.PrimaryAnatomicStructureSequence.append(item.to_dataset())

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
    def RecommendedDisplayCIELabValue(self) -> Optional[List[int]]:
        if "RecommendedDisplayCIELabValue" in self._dataset:
            return self._dataset.RecommendedDisplayCIELabValue
        return None

    @RecommendedDisplayCIELabValue.setter
    def RecommendedDisplayCIELabValue(self, value: Optional[List[int]]):
        if value is None:
            if "RecommendedDisplayCIELabValue" in self._dataset:
                del self._dataset.RecommendedDisplayCIELabValue
        else:
            self._dataset.RecommendedDisplayCIELabValue = value

    @property
    def PointCoordinatesData(self) -> Optional[bytes]:
        if "PointCoordinatesData" in self._dataset:
            return self._dataset.PointCoordinatesData
        return None

    @PointCoordinatesData.setter
    def PointCoordinatesData(self, value: Optional[bytes]):
        if value is None:
            if "PointCoordinatesData" in self._dataset:
                del self._dataset.PointCoordinatesData
        else:
            self._dataset.PointCoordinatesData = value

    @property
    def DoublePointCoordinatesData(self) -> Optional[bytes]:
        if "DoublePointCoordinatesData" in self._dataset:
            return self._dataset.DoublePointCoordinatesData
        return None

    @DoublePointCoordinatesData.setter
    def DoublePointCoordinatesData(self, value: Optional[bytes]):
        if value is None:
            if "DoublePointCoordinatesData" in self._dataset:
                del self._dataset.DoublePointCoordinatesData
        else:
            self._dataset.DoublePointCoordinatesData = value

    @property
    def LongPrimitivePointIndexList(self) -> Optional[bytes]:
        if "LongPrimitivePointIndexList" in self._dataset:
            return self._dataset.LongPrimitivePointIndexList
        return None

    @LongPrimitivePointIndexList.setter
    def LongPrimitivePointIndexList(self, value: Optional[bytes]):
        if value is None:
            if "LongPrimitivePointIndexList" in self._dataset:
                del self._dataset.LongPrimitivePointIndexList
        else:
            self._dataset.LongPrimitivePointIndexList = value

    @property
    def MeasurementsSequence(self) -> Optional[List[MeasurementsSequenceItem]]:
        if "MeasurementsSequence" in self._dataset:
            if len(self._MeasurementsSequence) == len(self._dataset.MeasurementsSequence):
                return self._MeasurementsSequence
            else:
                return [MeasurementsSequenceItem(x) for x in self._dataset.MeasurementsSequence]
        return None

    @MeasurementsSequence.setter
    def MeasurementsSequence(self, value: Optional[List[MeasurementsSequenceItem]]):
        if value is None:
            self._MeasurementsSequence = []
            if "MeasurementsSequence" in self._dataset:
                del self._dataset.MeasurementsSequence
        elif not isinstance(value, list) or not all(isinstance(item, MeasurementsSequenceItem) for item in value):
            raise ValueError(f"MeasurementsSequence must be a list of MeasurementsSequenceItem objects")
        else:
            self._MeasurementsSequence = value
            if "MeasurementsSequence" not in self._dataset:
                self._dataset.MeasurementsSequence = pydicom.Sequence()
            self._dataset.MeasurementsSequence.clear()
            self._dataset.MeasurementsSequence.extend([item.to_dataset() for item in value])

    def add_Measurements(self, item: MeasurementsSequenceItem):
        if not isinstance(item, MeasurementsSequenceItem):
            raise ValueError(f"Item must be an instance of MeasurementsSequenceItem")
        self._MeasurementsSequence.append(item)
        if "MeasurementsSequence" not in self._dataset:
            self._dataset.MeasurementsSequence = pydicom.Sequence()
        self._dataset.MeasurementsSequence.append(item.to_dataset())

    @property
    def AnnotationGroupUID(self) -> Optional[str]:
        if "AnnotationGroupUID" in self._dataset:
            return self._dataset.AnnotationGroupUID
        return None

    @AnnotationGroupUID.setter
    def AnnotationGroupUID(self, value: Optional[str]):
        if value is None:
            if "AnnotationGroupUID" in self._dataset:
                del self._dataset.AnnotationGroupUID
        else:
            self._dataset.AnnotationGroupUID = value

    @property
    def AnnotationGroupLabel(self) -> Optional[str]:
        if "AnnotationGroupLabel" in self._dataset:
            return self._dataset.AnnotationGroupLabel
        return None

    @AnnotationGroupLabel.setter
    def AnnotationGroupLabel(self, value: Optional[str]):
        if value is None:
            if "AnnotationGroupLabel" in self._dataset:
                del self._dataset.AnnotationGroupLabel
        else:
            self._dataset.AnnotationGroupLabel = value

    @property
    def AnnotationGroupDescription(self) -> Optional[str]:
        if "AnnotationGroupDescription" in self._dataset:
            return self._dataset.AnnotationGroupDescription
        return None

    @AnnotationGroupDescription.setter
    def AnnotationGroupDescription(self, value: Optional[str]):
        if value is None:
            if "AnnotationGroupDescription" in self._dataset:
                del self._dataset.AnnotationGroupDescription
        else:
            self._dataset.AnnotationGroupDescription = value

    @property
    def AnnotationGroupGenerationType(self) -> Optional[str]:
        if "AnnotationGroupGenerationType" in self._dataset:
            return self._dataset.AnnotationGroupGenerationType
        return None

    @AnnotationGroupGenerationType.setter
    def AnnotationGroupGenerationType(self, value: Optional[str]):
        if value is None:
            if "AnnotationGroupGenerationType" in self._dataset:
                del self._dataset.AnnotationGroupGenerationType
        else:
            self._dataset.AnnotationGroupGenerationType = value

    @property
    def AnnotationGroupAlgorithmIdentificationSequence(
        self,
    ) -> Optional[List[AnnotationGroupAlgorithmIdentificationSequenceItem]]:
        if "AnnotationGroupAlgorithmIdentificationSequence" in self._dataset:
            if len(self._AnnotationGroupAlgorithmIdentificationSequence) == len(
                self._dataset.AnnotationGroupAlgorithmIdentificationSequence
            ):
                return self._AnnotationGroupAlgorithmIdentificationSequence
            else:
                return [
                    AnnotationGroupAlgorithmIdentificationSequenceItem(x)
                    for x in self._dataset.AnnotationGroupAlgorithmIdentificationSequence
                ]
        return None

    @AnnotationGroupAlgorithmIdentificationSequence.setter
    def AnnotationGroupAlgorithmIdentificationSequence(
        self, value: Optional[List[AnnotationGroupAlgorithmIdentificationSequenceItem]]
    ):
        if value is None:
            self._AnnotationGroupAlgorithmIdentificationSequence = []
            if "AnnotationGroupAlgorithmIdentificationSequence" in self._dataset:
                del self._dataset.AnnotationGroupAlgorithmIdentificationSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, AnnotationGroupAlgorithmIdentificationSequenceItem) for item in value
        ):
            raise ValueError(
                f"AnnotationGroupAlgorithmIdentificationSequence must be a list of AnnotationGroupAlgorithmIdentificationSequenceItem objects"
            )
        else:
            self._AnnotationGroupAlgorithmIdentificationSequence = value
            if "AnnotationGroupAlgorithmIdentificationSequence" not in self._dataset:
                self._dataset.AnnotationGroupAlgorithmIdentificationSequence = pydicom.Sequence()
            self._dataset.AnnotationGroupAlgorithmIdentificationSequence.clear()
            self._dataset.AnnotationGroupAlgorithmIdentificationSequence.extend([item.to_dataset() for item in value])

    def add_AnnotationGroupAlgorithmIdentification(self, item: AnnotationGroupAlgorithmIdentificationSequenceItem):
        if not isinstance(item, AnnotationGroupAlgorithmIdentificationSequenceItem):
            raise ValueError(f"Item must be an instance of AnnotationGroupAlgorithmIdentificationSequenceItem")
        self._AnnotationGroupAlgorithmIdentificationSequence.append(item)
        if "AnnotationGroupAlgorithmIdentificationSequence" not in self._dataset:
            self._dataset.AnnotationGroupAlgorithmIdentificationSequence = pydicom.Sequence()
        self._dataset.AnnotationGroupAlgorithmIdentificationSequence.append(item.to_dataset())

    @property
    def AnnotationPropertyCategoryCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "AnnotationPropertyCategoryCodeSequence" in self._dataset:
            if len(self._AnnotationPropertyCategoryCodeSequence) == len(self._dataset.AnnotationPropertyCategoryCodeSequence):
                return self._AnnotationPropertyCategoryCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.AnnotationPropertyCategoryCodeSequence]
        return None

    @AnnotationPropertyCategoryCodeSequence.setter
    def AnnotationPropertyCategoryCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._AnnotationPropertyCategoryCodeSequence = []
            if "AnnotationPropertyCategoryCodeSequence" in self._dataset:
                del self._dataset.AnnotationPropertyCategoryCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError(f"AnnotationPropertyCategoryCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._AnnotationPropertyCategoryCodeSequence = value
            if "AnnotationPropertyCategoryCodeSequence" not in self._dataset:
                self._dataset.AnnotationPropertyCategoryCodeSequence = pydicom.Sequence()
            self._dataset.AnnotationPropertyCategoryCodeSequence.clear()
            self._dataset.AnnotationPropertyCategoryCodeSequence.extend([item.to_dataset() for item in value])

    def add_AnnotationPropertyCategoryCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError(f"Item must be an instance of CodeSequenceItem")
        self._AnnotationPropertyCategoryCodeSequence.append(item)
        if "AnnotationPropertyCategoryCodeSequence" not in self._dataset:
            self._dataset.AnnotationPropertyCategoryCodeSequence = pydicom.Sequence()
        self._dataset.AnnotationPropertyCategoryCodeSequence.append(item.to_dataset())

    @property
    def AnnotationPropertyTypeCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "AnnotationPropertyTypeCodeSequence" in self._dataset:
            if len(self._AnnotationPropertyTypeCodeSequence) == len(self._dataset.AnnotationPropertyTypeCodeSequence):
                return self._AnnotationPropertyTypeCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.AnnotationPropertyTypeCodeSequence]
        return None

    @AnnotationPropertyTypeCodeSequence.setter
    def AnnotationPropertyTypeCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._AnnotationPropertyTypeCodeSequence = []
            if "AnnotationPropertyTypeCodeSequence" in self._dataset:
                del self._dataset.AnnotationPropertyTypeCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError(f"AnnotationPropertyTypeCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._AnnotationPropertyTypeCodeSequence = value
            if "AnnotationPropertyTypeCodeSequence" not in self._dataset:
                self._dataset.AnnotationPropertyTypeCodeSequence = pydicom.Sequence()
            self._dataset.AnnotationPropertyTypeCodeSequence.clear()
            self._dataset.AnnotationPropertyTypeCodeSequence.extend([item.to_dataset() for item in value])

    def add_AnnotationPropertyTypeCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError(f"Item must be an instance of CodeSequenceItem")
        self._AnnotationPropertyTypeCodeSequence.append(item)
        if "AnnotationPropertyTypeCodeSequence" not in self._dataset:
            self._dataset.AnnotationPropertyTypeCodeSequence = pydicom.Sequence()
        self._dataset.AnnotationPropertyTypeCodeSequence.append(item.to_dataset())

    @property
    def NumberOfAnnotations(self) -> Optional[int]:
        if "NumberOfAnnotations" in self._dataset:
            return self._dataset.NumberOfAnnotations
        return None

    @NumberOfAnnotations.setter
    def NumberOfAnnotations(self, value: Optional[int]):
        if value is None:
            if "NumberOfAnnotations" in self._dataset:
                del self._dataset.NumberOfAnnotations
        else:
            self._dataset.NumberOfAnnotations = value

    @property
    def AnnotationAppliesToAllOpticalPaths(self) -> Optional[str]:
        if "AnnotationAppliesToAllOpticalPaths" in self._dataset:
            return self._dataset.AnnotationAppliesToAllOpticalPaths
        return None

    @AnnotationAppliesToAllOpticalPaths.setter
    def AnnotationAppliesToAllOpticalPaths(self, value: Optional[str]):
        if value is None:
            if "AnnotationAppliesToAllOpticalPaths" in self._dataset:
                del self._dataset.AnnotationAppliesToAllOpticalPaths
        else:
            self._dataset.AnnotationAppliesToAllOpticalPaths = value

    @property
    def ReferencedOpticalPathIdentifier(self) -> Optional[List[str]]:
        if "ReferencedOpticalPathIdentifier" in self._dataset:
            return self._dataset.ReferencedOpticalPathIdentifier
        return None

    @ReferencedOpticalPathIdentifier.setter
    def ReferencedOpticalPathIdentifier(self, value: Optional[List[str]]):
        if value is None:
            if "ReferencedOpticalPathIdentifier" in self._dataset:
                del self._dataset.ReferencedOpticalPathIdentifier
        else:
            self._dataset.ReferencedOpticalPathIdentifier = value

    @property
    def AnnotationAppliesToAllZPlanes(self) -> Optional[str]:
        if "AnnotationAppliesToAllZPlanes" in self._dataset:
            return self._dataset.AnnotationAppliesToAllZPlanes
        return None

    @AnnotationAppliesToAllZPlanes.setter
    def AnnotationAppliesToAllZPlanes(self, value: Optional[str]):
        if value is None:
            if "AnnotationAppliesToAllZPlanes" in self._dataset:
                del self._dataset.AnnotationAppliesToAllZPlanes
        else:
            self._dataset.AnnotationAppliesToAllZPlanes = value

    @property
    def CommonZCoordinateValue(self) -> Optional[List[float]]:
        if "CommonZCoordinateValue" in self._dataset:
            return self._dataset.CommonZCoordinateValue
        return None

    @CommonZCoordinateValue.setter
    def CommonZCoordinateValue(self, value: Optional[List[float]]):
        if value is None:
            if "CommonZCoordinateValue" in self._dataset:
                del self._dataset.CommonZCoordinateValue
        else:
            self._dataset.CommonZCoordinateValue = value

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
