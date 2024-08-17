from decimal import Decimal
from typing import Any, List, Optional  # noqa

import pydicom

from .code_sequence_item import CodeSequenceItem
from .definition_source_sequence_item import DefinitionSourceSequenceItem
from .graphic_coordinates_data_sequence_item import GraphicCoordinatesDataSequenceItem


class FiducialSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._DefinitionSourceSequence: List[DefinitionSourceSequenceItem] = []
        self._FiducialIdentifierCodeSequence: List[CodeSequenceItem] = []
        self._GraphicCoordinatesDataSequence: List[GraphicCoordinatesDataSequenceItem] = []
        self._FiducialsPropertyCategoryCodeSequence: List[CodeSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def DefinitionSourceSequence(self) -> Optional[List[DefinitionSourceSequenceItem]]:
        if "DefinitionSourceSequence" in self._dataset:
            if len(self._DefinitionSourceSequence) == len(self._dataset.DefinitionSourceSequence):
                return self._DefinitionSourceSequence
            else:
                return [DefinitionSourceSequenceItem(x) for x in self._dataset.DefinitionSourceSequence]
        return None

    @DefinitionSourceSequence.setter
    def DefinitionSourceSequence(self, value: Optional[List[DefinitionSourceSequenceItem]]):
        if value is None:
            self._DefinitionSourceSequence = []
            if "DefinitionSourceSequence" in self._dataset:
                del self._dataset.DefinitionSourceSequence
        elif not isinstance(value, list) or not all(isinstance(item, DefinitionSourceSequenceItem) for item in value):
            raise ValueError("DefinitionSourceSequence must be a list of DefinitionSourceSequenceItem objects")
        else:
            self._DefinitionSourceSequence = value
            if "DefinitionSourceSequence" not in self._dataset:
                self._dataset.DefinitionSourceSequence = pydicom.Sequence()
            self._dataset.DefinitionSourceSequence.clear()
            self._dataset.DefinitionSourceSequence.extend([item.to_dataset() for item in value])

    def add_DefinitionSource(self, item: DefinitionSourceSequenceItem):
        if not isinstance(item, DefinitionSourceSequenceItem):
            raise ValueError("Item must be an instance of DefinitionSourceSequenceItem")
        self._DefinitionSourceSequence.append(item)
        if "DefinitionSourceSequence" not in self._dataset:
            self._dataset.DefinitionSourceSequence = pydicom.Sequence()
        self._dataset.DefinitionSourceSequence.append(item.to_dataset())

    @property
    def ShapeType(self) -> Optional[str]:
        if "ShapeType" in self._dataset:
            return self._dataset.ShapeType
        return None

    @ShapeType.setter
    def ShapeType(self, value: Optional[str]):
        if value is None:
            if "ShapeType" in self._dataset:
                del self._dataset.ShapeType
        else:
            self._dataset.ShapeType = value

    @property
    def FiducialDescription(self) -> Optional[str]:
        if "FiducialDescription" in self._dataset:
            return self._dataset.FiducialDescription
        return None

    @FiducialDescription.setter
    def FiducialDescription(self, value: Optional[str]):
        if value is None:
            if "FiducialDescription" in self._dataset:
                del self._dataset.FiducialDescription
        else:
            self._dataset.FiducialDescription = value

    @property
    def FiducialIdentifier(self) -> Optional[str]:
        if "FiducialIdentifier" in self._dataset:
            return self._dataset.FiducialIdentifier
        return None

    @FiducialIdentifier.setter
    def FiducialIdentifier(self, value: Optional[str]):
        if value is None:
            if "FiducialIdentifier" in self._dataset:
                del self._dataset.FiducialIdentifier
        else:
            self._dataset.FiducialIdentifier = value

    @property
    def FiducialIdentifierCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "FiducialIdentifierCodeSequence" in self._dataset:
            if len(self._FiducialIdentifierCodeSequence) == len(self._dataset.FiducialIdentifierCodeSequence):
                return self._FiducialIdentifierCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.FiducialIdentifierCodeSequence]
        return None

    @FiducialIdentifierCodeSequence.setter
    def FiducialIdentifierCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._FiducialIdentifierCodeSequence = []
            if "FiducialIdentifierCodeSequence" in self._dataset:
                del self._dataset.FiducialIdentifierCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("FiducialIdentifierCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._FiducialIdentifierCodeSequence = value
            if "FiducialIdentifierCodeSequence" not in self._dataset:
                self._dataset.FiducialIdentifierCodeSequence = pydicom.Sequence()
            self._dataset.FiducialIdentifierCodeSequence.clear()
            self._dataset.FiducialIdentifierCodeSequence.extend([item.to_dataset() for item in value])

    def add_FiducialIdentifierCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._FiducialIdentifierCodeSequence.append(item)
        if "FiducialIdentifierCodeSequence" not in self._dataset:
            self._dataset.FiducialIdentifierCodeSequence = pydicom.Sequence()
        self._dataset.FiducialIdentifierCodeSequence.append(item.to_dataset())

    @property
    def ContourUncertaintyRadius(self) -> Optional[float]:
        if "ContourUncertaintyRadius" in self._dataset:
            return self._dataset.ContourUncertaintyRadius
        return None

    @ContourUncertaintyRadius.setter
    def ContourUncertaintyRadius(self, value: Optional[float]):
        if value is None:
            if "ContourUncertaintyRadius" in self._dataset:
                del self._dataset.ContourUncertaintyRadius
        else:
            self._dataset.ContourUncertaintyRadius = value

    @property
    def GraphicCoordinatesDataSequence(self) -> Optional[List[GraphicCoordinatesDataSequenceItem]]:
        if "GraphicCoordinatesDataSequence" in self._dataset:
            if len(self._GraphicCoordinatesDataSequence) == len(self._dataset.GraphicCoordinatesDataSequence):
                return self._GraphicCoordinatesDataSequence
            else:
                return [GraphicCoordinatesDataSequenceItem(x) for x in self._dataset.GraphicCoordinatesDataSequence]
        return None

    @GraphicCoordinatesDataSequence.setter
    def GraphicCoordinatesDataSequence(self, value: Optional[List[GraphicCoordinatesDataSequenceItem]]):
        if value is None:
            self._GraphicCoordinatesDataSequence = []
            if "GraphicCoordinatesDataSequence" in self._dataset:
                del self._dataset.GraphicCoordinatesDataSequence
        elif not isinstance(value, list) or not all(isinstance(item, GraphicCoordinatesDataSequenceItem) for item in value):
            raise ValueError("GraphicCoordinatesDataSequence must be a list of GraphicCoordinatesDataSequenceItem objects")
        else:
            self._GraphicCoordinatesDataSequence = value
            if "GraphicCoordinatesDataSequence" not in self._dataset:
                self._dataset.GraphicCoordinatesDataSequence = pydicom.Sequence()
            self._dataset.GraphicCoordinatesDataSequence.clear()
            self._dataset.GraphicCoordinatesDataSequence.extend([item.to_dataset() for item in value])

    def add_GraphicCoordinatesData(self, item: GraphicCoordinatesDataSequenceItem):
        if not isinstance(item, GraphicCoordinatesDataSequenceItem):
            raise ValueError("Item must be an instance of GraphicCoordinatesDataSequenceItem")
        self._GraphicCoordinatesDataSequence.append(item)
        if "GraphicCoordinatesDataSequence" not in self._dataset:
            self._dataset.GraphicCoordinatesDataSequence = pydicom.Sequence()
        self._dataset.GraphicCoordinatesDataSequence.append(item.to_dataset())

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
    def FiducialsPropertyCategoryCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "FiducialsPropertyCategoryCodeSequence" in self._dataset:
            if len(self._FiducialsPropertyCategoryCodeSequence) == len(self._dataset.FiducialsPropertyCategoryCodeSequence):
                return self._FiducialsPropertyCategoryCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.FiducialsPropertyCategoryCodeSequence]
        return None

    @FiducialsPropertyCategoryCodeSequence.setter
    def FiducialsPropertyCategoryCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._FiducialsPropertyCategoryCodeSequence = []
            if "FiducialsPropertyCategoryCodeSequence" in self._dataset:
                del self._dataset.FiducialsPropertyCategoryCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("FiducialsPropertyCategoryCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._FiducialsPropertyCategoryCodeSequence = value
            if "FiducialsPropertyCategoryCodeSequence" not in self._dataset:
                self._dataset.FiducialsPropertyCategoryCodeSequence = pydicom.Sequence()
            self._dataset.FiducialsPropertyCategoryCodeSequence.clear()
            self._dataset.FiducialsPropertyCategoryCodeSequence.extend([item.to_dataset() for item in value])

    def add_FiducialsPropertyCategoryCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._FiducialsPropertyCategoryCodeSequence.append(item)
        if "FiducialsPropertyCategoryCodeSequence" not in self._dataset:
            self._dataset.FiducialsPropertyCategoryCodeSequence = pydicom.Sequence()
        self._dataset.FiducialsPropertyCategoryCodeSequence.append(item.to_dataset())

    @property
    def NumberOfContourPoints(self) -> Optional[int]:
        if "NumberOfContourPoints" in self._dataset:
            return self._dataset.NumberOfContourPoints
        return None

    @NumberOfContourPoints.setter
    def NumberOfContourPoints(self, value: Optional[int]):
        if value is None:
            if "NumberOfContourPoints" in self._dataset:
                del self._dataset.NumberOfContourPoints
        else:
            self._dataset.NumberOfContourPoints = value

    @property
    def ContourData(self) -> Optional[List[Decimal]]:
        if "ContourData" in self._dataset:
            return self._dataset.ContourData
        return None

    @ContourData.setter
    def ContourData(self, value: Optional[List[Decimal]]):
        if value is None:
            if "ContourData" in self._dataset:
                del self._dataset.ContourData
        else:
            self._dataset.ContourData = value
