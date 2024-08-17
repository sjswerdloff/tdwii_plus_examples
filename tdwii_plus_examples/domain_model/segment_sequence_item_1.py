from typing import Any, List, Optional  # noqa

import pydicom

from .anatomic_region_sequence_item import AnatomicRegionSequenceItem
from .code_sequence_item import CodeSequenceItem
from .definition_source_sequence_item import DefinitionSourceSequenceItem
from .primary_anatomic_structure_sequence_item import (
    PrimaryAnatomicStructureSequenceItem,
)
from .segmentation_algorithm_identification_sequence_item import (
    SegmentationAlgorithmIdentificationSequenceItem,
)


class SegmentSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._DefinitionSourceSequence: List[DefinitionSourceSequenceItem] = []
        self._AnatomicRegionSequence: List[AnatomicRegionSequenceItem] = []
        self._PrimaryAnatomicStructureSequence: List[PrimaryAnatomicStructureSequenceItem] = []
        self._SegmentedPropertyCategoryCodeSequence: List[CodeSequenceItem] = []
        self._SegmentationAlgorithmIdentificationSequence: List[SegmentationAlgorithmIdentificationSequenceItem] = []
        self._SegmentedPropertyTypeCodeSequence: List[CodeSequenceItem] = []
        self._ContentCreatorIdentificationCodeSequence: List[CodeSequenceItem] = []

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
            raise ValueError("AnatomicRegionSequence must be a list of AnatomicRegionSequenceItem objects")
        else:
            self._AnatomicRegionSequence = value
            if "AnatomicRegionSequence" not in self._dataset:
                self._dataset.AnatomicRegionSequence = pydicom.Sequence()
            self._dataset.AnatomicRegionSequence.clear()
            self._dataset.AnatomicRegionSequence.extend([item.to_dataset() for item in value])

    def add_AnatomicRegion(self, item: AnatomicRegionSequenceItem):
        if not isinstance(item, AnatomicRegionSequenceItem):
            raise ValueError("Item must be an instance of AnatomicRegionSequenceItem")
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
            raise ValueError("PrimaryAnatomicStructureSequence must be a list of PrimaryAnatomicStructureSequenceItem objects")
        else:
            self._PrimaryAnatomicStructureSequence = value
            if "PrimaryAnatomicStructureSequence" not in self._dataset:
                self._dataset.PrimaryAnatomicStructureSequence = pydicom.Sequence()
            self._dataset.PrimaryAnatomicStructureSequence.clear()
            self._dataset.PrimaryAnatomicStructureSequence.extend([item.to_dataset() for item in value])

    def add_PrimaryAnatomicStructure(self, item: PrimaryAnatomicStructureSequenceItem):
        if not isinstance(item, PrimaryAnatomicStructureSequenceItem):
            raise ValueError("Item must be an instance of PrimaryAnatomicStructureSequenceItem")
        self._PrimaryAnatomicStructureSequence.append(item)
        if "PrimaryAnatomicStructureSequence" not in self._dataset:
            self._dataset.PrimaryAnatomicStructureSequence = pydicom.Sequence()
        self._dataset.PrimaryAnatomicStructureSequence.append(item.to_dataset())

    @property
    def SegmentedPropertyCategoryCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "SegmentedPropertyCategoryCodeSequence" in self._dataset:
            if len(self._SegmentedPropertyCategoryCodeSequence) == len(self._dataset.SegmentedPropertyCategoryCodeSequence):
                return self._SegmentedPropertyCategoryCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.SegmentedPropertyCategoryCodeSequence]
        return None

    @SegmentedPropertyCategoryCodeSequence.setter
    def SegmentedPropertyCategoryCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._SegmentedPropertyCategoryCodeSequence = []
            if "SegmentedPropertyCategoryCodeSequence" in self._dataset:
                del self._dataset.SegmentedPropertyCategoryCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("SegmentedPropertyCategoryCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._SegmentedPropertyCategoryCodeSequence = value
            if "SegmentedPropertyCategoryCodeSequence" not in self._dataset:
                self._dataset.SegmentedPropertyCategoryCodeSequence = pydicom.Sequence()
            self._dataset.SegmentedPropertyCategoryCodeSequence.clear()
            self._dataset.SegmentedPropertyCategoryCodeSequence.extend([item.to_dataset() for item in value])

    def add_SegmentedPropertyCategoryCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._SegmentedPropertyCategoryCodeSequence.append(item)
        if "SegmentedPropertyCategoryCodeSequence" not in self._dataset:
            self._dataset.SegmentedPropertyCategoryCodeSequence = pydicom.Sequence()
        self._dataset.SegmentedPropertyCategoryCodeSequence.append(item.to_dataset())

    @property
    def SegmentNumber(self) -> Optional[int]:
        if "SegmentNumber" in self._dataset:
            return self._dataset.SegmentNumber
        return None

    @SegmentNumber.setter
    def SegmentNumber(self, value: Optional[int]):
        if value is None:
            if "SegmentNumber" in self._dataset:
                del self._dataset.SegmentNumber
        else:
            self._dataset.SegmentNumber = value

    @property
    def SegmentLabel(self) -> Optional[str]:
        if "SegmentLabel" in self._dataset:
            return self._dataset.SegmentLabel
        return None

    @SegmentLabel.setter
    def SegmentLabel(self, value: Optional[str]):
        if value is None:
            if "SegmentLabel" in self._dataset:
                del self._dataset.SegmentLabel
        else:
            self._dataset.SegmentLabel = value

    @property
    def SegmentDescription(self) -> Optional[str]:
        if "SegmentDescription" in self._dataset:
            return self._dataset.SegmentDescription
        return None

    @SegmentDescription.setter
    def SegmentDescription(self, value: Optional[str]):
        if value is None:
            if "SegmentDescription" in self._dataset:
                del self._dataset.SegmentDescription
        else:
            self._dataset.SegmentDescription = value

    @property
    def SegmentationAlgorithmIdentificationSequence(self) -> Optional[List[SegmentationAlgorithmIdentificationSequenceItem]]:
        if "SegmentationAlgorithmIdentificationSequence" in self._dataset:
            if len(self._SegmentationAlgorithmIdentificationSequence) == len(
                self._dataset.SegmentationAlgorithmIdentificationSequence
            ):
                return self._SegmentationAlgorithmIdentificationSequence
            else:
                return [
                    SegmentationAlgorithmIdentificationSequenceItem(x)
                    for x in self._dataset.SegmentationAlgorithmIdentificationSequence
                ]
        return None

    @SegmentationAlgorithmIdentificationSequence.setter
    def SegmentationAlgorithmIdentificationSequence(
        self, value: Optional[List[SegmentationAlgorithmIdentificationSequenceItem]]
    ):
        if value is None:
            self._SegmentationAlgorithmIdentificationSequence = []
            if "SegmentationAlgorithmIdentificationSequence" in self._dataset:
                del self._dataset.SegmentationAlgorithmIdentificationSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, SegmentationAlgorithmIdentificationSequenceItem) for item in value
        ):
            raise ValueError(
                "SegmentationAlgorithmIdentificationSequence must be a list of SegmentationAlgorithmIdentificationSequenceItem"
                " objects"
            )
        else:
            self._SegmentationAlgorithmIdentificationSequence = value
            if "SegmentationAlgorithmIdentificationSequence" not in self._dataset:
                self._dataset.SegmentationAlgorithmIdentificationSequence = pydicom.Sequence()
            self._dataset.SegmentationAlgorithmIdentificationSequence.clear()
            self._dataset.SegmentationAlgorithmIdentificationSequence.extend([item.to_dataset() for item in value])

    def add_SegmentationAlgorithmIdentification(self, item: SegmentationAlgorithmIdentificationSequenceItem):
        if not isinstance(item, SegmentationAlgorithmIdentificationSequenceItem):
            raise ValueError("Item must be an instance of SegmentationAlgorithmIdentificationSequenceItem")
        self._SegmentationAlgorithmIdentificationSequence.append(item)
        if "SegmentationAlgorithmIdentificationSequence" not in self._dataset:
            self._dataset.SegmentationAlgorithmIdentificationSequence = pydicom.Sequence()
        self._dataset.SegmentationAlgorithmIdentificationSequence.append(item.to_dataset())

    @property
    def SegmentAlgorithmType(self) -> Optional[str]:
        if "SegmentAlgorithmType" in self._dataset:
            return self._dataset.SegmentAlgorithmType
        return None

    @SegmentAlgorithmType.setter
    def SegmentAlgorithmType(self, value: Optional[str]):
        if value is None:
            if "SegmentAlgorithmType" in self._dataset:
                del self._dataset.SegmentAlgorithmType
        else:
            self._dataset.SegmentAlgorithmType = value

    @property
    def SegmentAlgorithmName(self) -> Optional[List[str]]:
        if "SegmentAlgorithmName" in self._dataset:
            return self._dataset.SegmentAlgorithmName
        return None

    @SegmentAlgorithmName.setter
    def SegmentAlgorithmName(self, value: Optional[List[str]]):
        if value is None:
            if "SegmentAlgorithmName" in self._dataset:
                del self._dataset.SegmentAlgorithmName
        else:
            self._dataset.SegmentAlgorithmName = value

    @property
    def RecommendedDisplayGrayscaleValue(self) -> Optional[int]:
        if "RecommendedDisplayGrayscaleValue" in self._dataset:
            return self._dataset.RecommendedDisplayGrayscaleValue
        return None

    @RecommendedDisplayGrayscaleValue.setter
    def RecommendedDisplayGrayscaleValue(self, value: Optional[int]):
        if value is None:
            if "RecommendedDisplayGrayscaleValue" in self._dataset:
                del self._dataset.RecommendedDisplayGrayscaleValue
        else:
            self._dataset.RecommendedDisplayGrayscaleValue = value

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
    def SegmentedPropertyTypeCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "SegmentedPropertyTypeCodeSequence" in self._dataset:
            if len(self._SegmentedPropertyTypeCodeSequence) == len(self._dataset.SegmentedPropertyTypeCodeSequence):
                return self._SegmentedPropertyTypeCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.SegmentedPropertyTypeCodeSequence]
        return None

    @SegmentedPropertyTypeCodeSequence.setter
    def SegmentedPropertyTypeCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._SegmentedPropertyTypeCodeSequence = []
            if "SegmentedPropertyTypeCodeSequence" in self._dataset:
                del self._dataset.SegmentedPropertyTypeCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("SegmentedPropertyTypeCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._SegmentedPropertyTypeCodeSequence = value
            if "SegmentedPropertyTypeCodeSequence" not in self._dataset:
                self._dataset.SegmentedPropertyTypeCodeSequence = pydicom.Sequence()
            self._dataset.SegmentedPropertyTypeCodeSequence.clear()
            self._dataset.SegmentedPropertyTypeCodeSequence.extend([item.to_dataset() for item in value])

    def add_SegmentedPropertyTypeCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._SegmentedPropertyTypeCodeSequence.append(item)
        if "SegmentedPropertyTypeCodeSequence" not in self._dataset:
            self._dataset.SegmentedPropertyTypeCodeSequence = pydicom.Sequence()
        self._dataset.SegmentedPropertyTypeCodeSequence.append(item.to_dataset())

    @property
    def TrackingID(self) -> Optional[str]:
        if "TrackingID" in self._dataset:
            return self._dataset.TrackingID
        return None

    @TrackingID.setter
    def TrackingID(self, value: Optional[str]):
        if value is None:
            if "TrackingID" in self._dataset:
                del self._dataset.TrackingID
        else:
            self._dataset.TrackingID = value

    @property
    def TrackingUID(self) -> Optional[str]:
        if "TrackingUID" in self._dataset:
            return self._dataset.TrackingUID
        return None

    @TrackingUID.setter
    def TrackingUID(self, value: Optional[str]):
        if value is None:
            if "TrackingUID" in self._dataset:
                del self._dataset.TrackingUID
        else:
            self._dataset.TrackingUID = value

    @property
    def ContentCreatorName(self) -> Optional[str]:
        if "ContentCreatorName" in self._dataset:
            return self._dataset.ContentCreatorName
        return None

    @ContentCreatorName.setter
    def ContentCreatorName(self, value: Optional[str]):
        if value is None:
            if "ContentCreatorName" in self._dataset:
                del self._dataset.ContentCreatorName
        else:
            self._dataset.ContentCreatorName = value

    @property
    def ContentCreatorIdentificationCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "ContentCreatorIdentificationCodeSequence" in self._dataset:
            if len(self._ContentCreatorIdentificationCodeSequence) == len(
                self._dataset.ContentCreatorIdentificationCodeSequence
            ):
                return self._ContentCreatorIdentificationCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.ContentCreatorIdentificationCodeSequence]
        return None

    @ContentCreatorIdentificationCodeSequence.setter
    def ContentCreatorIdentificationCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._ContentCreatorIdentificationCodeSequence = []
            if "ContentCreatorIdentificationCodeSequence" in self._dataset:
                del self._dataset.ContentCreatorIdentificationCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("ContentCreatorIdentificationCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._ContentCreatorIdentificationCodeSequence = value
            if "ContentCreatorIdentificationCodeSequence" not in self._dataset:
                self._dataset.ContentCreatorIdentificationCodeSequence = pydicom.Sequence()
            self._dataset.ContentCreatorIdentificationCodeSequence.clear()
            self._dataset.ContentCreatorIdentificationCodeSequence.extend([item.to_dataset() for item in value])

    def add_ContentCreatorIdentificationCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._ContentCreatorIdentificationCodeSequence.append(item)
        if "ContentCreatorIdentificationCodeSequence" not in self._dataset:
            self._dataset.ContentCreatorIdentificationCodeSequence = pydicom.Sequence()
        self._dataset.ContentCreatorIdentificationCodeSequence.append(item.to_dataset())
