from typing import Any, List, Optional

import pydicom

from .anatomic_region_sequence_item import AnatomicRegionSequenceItem
from .code_sequence_item import CodeSequenceItem
from .primary_anatomic_structure_sequence_item import (
    PrimaryAnatomicStructureSequenceItem,
)
from .related_rtroi_observations_sequence_item import (
    RelatedRTROIObservationsSequenceItem,
)
from .roi_interpreter_sequence_item import ROIInterpreterSequenceItem
from .roi_physical_properties_sequence_item import ROIPhysicalPropertiesSequenceItem
from .rt_related_roi_sequence_item import RTRelatedROISequenceItem


class RTROIObservationsSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._AnatomicRegionSequence: List[AnatomicRegionSequenceItem] = []
        self._PrimaryAnatomicStructureSequence: List[PrimaryAnatomicStructureSequenceItem] = []
        self._SegmentedPropertyCategoryCodeSequence: List[CodeSequenceItem] = []
        self._RTRelatedROISequence: List[RTRelatedROISequenceItem] = []
        self._ROIInterpreterSequence: List[ROIInterpreterSequenceItem] = []
        self._ROIObservationContextCodeSequence: List[CodeSequenceItem] = []
        self._RTROIIdentificationCodeSequence: List[CodeSequenceItem] = []
        self._RelatedRTROIObservationsSequence: List[RelatedRTROIObservationsSequenceItem] = []
        self._ROIPhysicalPropertiesSequence: List[ROIPhysicalPropertiesSequenceItem] = []
        self._TherapeuticRoleCategoryCodeSequence: List[CodeSequenceItem] = []
        self._TherapeuticRoleTypeCodeSequence: List[CodeSequenceItem] = []

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
            raise ValueError(f"SegmentedPropertyCategoryCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._SegmentedPropertyCategoryCodeSequence = value
            if "SegmentedPropertyCategoryCodeSequence" not in self._dataset:
                self._dataset.SegmentedPropertyCategoryCodeSequence = pydicom.Sequence()
            self._dataset.SegmentedPropertyCategoryCodeSequence.clear()
            self._dataset.SegmentedPropertyCategoryCodeSequence.extend([item.to_dataset() for item in value])

    def add_SegmentedPropertyCategoryCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError(f"Item must be an instance of CodeSequenceItem")
        self._SegmentedPropertyCategoryCodeSequence.append(item)
        if "SegmentedPropertyCategoryCodeSequence" not in self._dataset:
            self._dataset.SegmentedPropertyCategoryCodeSequence = pydicom.Sequence()
        self._dataset.SegmentedPropertyCategoryCodeSequence.append(item.to_dataset())

    @property
    def ROIObservationDateTime(self) -> Optional[str]:
        if "ROIObservationDateTime" in self._dataset:
            return self._dataset.ROIObservationDateTime
        return None

    @ROIObservationDateTime.setter
    def ROIObservationDateTime(self, value: Optional[str]):
        if value is None:
            if "ROIObservationDateTime" in self._dataset:
                del self._dataset.ROIObservationDateTime
        else:
            self._dataset.ROIObservationDateTime = value

    @property
    def RTRelatedROISequence(self) -> Optional[List[RTRelatedROISequenceItem]]:
        if "RTRelatedROISequence" in self._dataset:
            if len(self._RTRelatedROISequence) == len(self._dataset.RTRelatedROISequence):
                return self._RTRelatedROISequence
            else:
                return [RTRelatedROISequenceItem(x) for x in self._dataset.RTRelatedROISequence]
        return None

    @RTRelatedROISequence.setter
    def RTRelatedROISequence(self, value: Optional[List[RTRelatedROISequenceItem]]):
        if value is None:
            self._RTRelatedROISequence = []
            if "RTRelatedROISequence" in self._dataset:
                del self._dataset.RTRelatedROISequence
        elif not isinstance(value, list) or not all(isinstance(item, RTRelatedROISequenceItem) for item in value):
            raise ValueError(f"RTRelatedROISequence must be a list of RTRelatedROISequenceItem objects")
        else:
            self._RTRelatedROISequence = value
            if "RTRelatedROISequence" not in self._dataset:
                self._dataset.RTRelatedROISequence = pydicom.Sequence()
            self._dataset.RTRelatedROISequence.clear()
            self._dataset.RTRelatedROISequence.extend([item.to_dataset() for item in value])

    def add_RTRelatedROI(self, item: RTRelatedROISequenceItem):
        if not isinstance(item, RTRelatedROISequenceItem):
            raise ValueError(f"Item must be an instance of RTRelatedROISequenceItem")
        self._RTRelatedROISequence.append(item)
        if "RTRelatedROISequence" not in self._dataset:
            self._dataset.RTRelatedROISequence = pydicom.Sequence()
        self._dataset.RTRelatedROISequence.append(item.to_dataset())

    @property
    def ROIInterpreterSequence(self) -> Optional[List[ROIInterpreterSequenceItem]]:
        if "ROIInterpreterSequence" in self._dataset:
            if len(self._ROIInterpreterSequence) == len(self._dataset.ROIInterpreterSequence):
                return self._ROIInterpreterSequence
            else:
                return [ROIInterpreterSequenceItem(x) for x in self._dataset.ROIInterpreterSequence]
        return None

    @ROIInterpreterSequence.setter
    def ROIInterpreterSequence(self, value: Optional[List[ROIInterpreterSequenceItem]]):
        if value is None:
            self._ROIInterpreterSequence = []
            if "ROIInterpreterSequence" in self._dataset:
                del self._dataset.ROIInterpreterSequence
        elif not isinstance(value, list) or not all(isinstance(item, ROIInterpreterSequenceItem) for item in value):
            raise ValueError(f"ROIInterpreterSequence must be a list of ROIInterpreterSequenceItem objects")
        else:
            self._ROIInterpreterSequence = value
            if "ROIInterpreterSequence" not in self._dataset:
                self._dataset.ROIInterpreterSequence = pydicom.Sequence()
            self._dataset.ROIInterpreterSequence.clear()
            self._dataset.ROIInterpreterSequence.extend([item.to_dataset() for item in value])

    def add_ROIInterpreter(self, item: ROIInterpreterSequenceItem):
        if not isinstance(item, ROIInterpreterSequenceItem):
            raise ValueError(f"Item must be an instance of ROIInterpreterSequenceItem")
        self._ROIInterpreterSequence.append(item)
        if "ROIInterpreterSequence" not in self._dataset:
            self._dataset.ROIInterpreterSequence = pydicom.Sequence()
        self._dataset.ROIInterpreterSequence.append(item.to_dataset())

    @property
    def ROIObservationContextCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "ROIObservationContextCodeSequence" in self._dataset:
            if len(self._ROIObservationContextCodeSequence) == len(self._dataset.ROIObservationContextCodeSequence):
                return self._ROIObservationContextCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.ROIObservationContextCodeSequence]
        return None

    @ROIObservationContextCodeSequence.setter
    def ROIObservationContextCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._ROIObservationContextCodeSequence = []
            if "ROIObservationContextCodeSequence" in self._dataset:
                del self._dataset.ROIObservationContextCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError(f"ROIObservationContextCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._ROIObservationContextCodeSequence = value
            if "ROIObservationContextCodeSequence" not in self._dataset:
                self._dataset.ROIObservationContextCodeSequence = pydicom.Sequence()
            self._dataset.ROIObservationContextCodeSequence.clear()
            self._dataset.ROIObservationContextCodeSequence.extend([item.to_dataset() for item in value])

    def add_ROIObservationContextCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError(f"Item must be an instance of CodeSequenceItem")
        self._ROIObservationContextCodeSequence.append(item)
        if "ROIObservationContextCodeSequence" not in self._dataset:
            self._dataset.ROIObservationContextCodeSequence = pydicom.Sequence()
        self._dataset.ROIObservationContextCodeSequence.append(item.to_dataset())

    @property
    def ObservationNumber(self) -> Optional[int]:
        if "ObservationNumber" in self._dataset:
            return self._dataset.ObservationNumber
        return None

    @ObservationNumber.setter
    def ObservationNumber(self, value: Optional[int]):
        if value is None:
            if "ObservationNumber" in self._dataset:
                del self._dataset.ObservationNumber
        else:
            self._dataset.ObservationNumber = value

    @property
    def ReferencedROINumber(self) -> Optional[int]:
        if "ReferencedROINumber" in self._dataset:
            return self._dataset.ReferencedROINumber
        return None

    @ReferencedROINumber.setter
    def ReferencedROINumber(self, value: Optional[int]):
        if value is None:
            if "ReferencedROINumber" in self._dataset:
                del self._dataset.ReferencedROINumber
        else:
            self._dataset.ReferencedROINumber = value

    @property
    def RTROIIdentificationCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "RTROIIdentificationCodeSequence" in self._dataset:
            if len(self._RTROIIdentificationCodeSequence) == len(self._dataset.RTROIIdentificationCodeSequence):
                return self._RTROIIdentificationCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.RTROIIdentificationCodeSequence]
        return None

    @RTROIIdentificationCodeSequence.setter
    def RTROIIdentificationCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._RTROIIdentificationCodeSequence = []
            if "RTROIIdentificationCodeSequence" in self._dataset:
                del self._dataset.RTROIIdentificationCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError(f"RTROIIdentificationCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._RTROIIdentificationCodeSequence = value
            if "RTROIIdentificationCodeSequence" not in self._dataset:
                self._dataset.RTROIIdentificationCodeSequence = pydicom.Sequence()
            self._dataset.RTROIIdentificationCodeSequence.clear()
            self._dataset.RTROIIdentificationCodeSequence.extend([item.to_dataset() for item in value])

    def add_RTROIIdentificationCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError(f"Item must be an instance of CodeSequenceItem")
        self._RTROIIdentificationCodeSequence.append(item)
        if "RTROIIdentificationCodeSequence" not in self._dataset:
            self._dataset.RTROIIdentificationCodeSequence = pydicom.Sequence()
        self._dataset.RTROIIdentificationCodeSequence.append(item.to_dataset())

    @property
    def RelatedRTROIObservationsSequence(self) -> Optional[List[RelatedRTROIObservationsSequenceItem]]:
        if "RelatedRTROIObservationsSequence" in self._dataset:
            if len(self._RelatedRTROIObservationsSequence) == len(self._dataset.RelatedRTROIObservationsSequence):
                return self._RelatedRTROIObservationsSequence
            else:
                return [RelatedRTROIObservationsSequenceItem(x) for x in self._dataset.RelatedRTROIObservationsSequence]
        return None

    @RelatedRTROIObservationsSequence.setter
    def RelatedRTROIObservationsSequence(self, value: Optional[List[RelatedRTROIObservationsSequenceItem]]):
        if value is None:
            self._RelatedRTROIObservationsSequence = []
            if "RelatedRTROIObservationsSequence" in self._dataset:
                del self._dataset.RelatedRTROIObservationsSequence
        elif not isinstance(value, list) or not all(isinstance(item, RelatedRTROIObservationsSequenceItem) for item in value):
            raise ValueError(
                f"RelatedRTROIObservationsSequence must be a list of RelatedRTROIObservationsSequenceItem objects"
            )
        else:
            self._RelatedRTROIObservationsSequence = value
            if "RelatedRTROIObservationsSequence" not in self._dataset:
                self._dataset.RelatedRTROIObservationsSequence = pydicom.Sequence()
            self._dataset.RelatedRTROIObservationsSequence.clear()
            self._dataset.RelatedRTROIObservationsSequence.extend([item.to_dataset() for item in value])

    def add_RelatedRTROIObservations(self, item: RelatedRTROIObservationsSequenceItem):
        if not isinstance(item, RelatedRTROIObservationsSequenceItem):
            raise ValueError(f"Item must be an instance of RelatedRTROIObservationsSequenceItem")
        self._RelatedRTROIObservationsSequence.append(item)
        if "RelatedRTROIObservationsSequence" not in self._dataset:
            self._dataset.RelatedRTROIObservationsSequence = pydicom.Sequence()
        self._dataset.RelatedRTROIObservationsSequence.append(item.to_dataset())

    @property
    def RTROIInterpretedType(self) -> Optional[str]:
        if "RTROIInterpretedType" in self._dataset:
            return self._dataset.RTROIInterpretedType
        return None

    @RTROIInterpretedType.setter
    def RTROIInterpretedType(self, value: Optional[str]):
        if value is None:
            if "RTROIInterpretedType" in self._dataset:
                del self._dataset.RTROIInterpretedType
        else:
            self._dataset.RTROIInterpretedType = value

    @property
    def ROIInterpreter(self) -> Optional[str]:
        if "ROIInterpreter" in self._dataset:
            return self._dataset.ROIInterpreter
        return None

    @ROIInterpreter.setter
    def ROIInterpreter(self, value: Optional[str]):
        if value is None:
            if "ROIInterpreter" in self._dataset:
                del self._dataset.ROIInterpreter
        else:
            self._dataset.ROIInterpreter = value

    @property
    def ROIPhysicalPropertiesSequence(self) -> Optional[List[ROIPhysicalPropertiesSequenceItem]]:
        if "ROIPhysicalPropertiesSequence" in self._dataset:
            if len(self._ROIPhysicalPropertiesSequence) == len(self._dataset.ROIPhysicalPropertiesSequence):
                return self._ROIPhysicalPropertiesSequence
            else:
                return [ROIPhysicalPropertiesSequenceItem(x) for x in self._dataset.ROIPhysicalPropertiesSequence]
        return None

    @ROIPhysicalPropertiesSequence.setter
    def ROIPhysicalPropertiesSequence(self, value: Optional[List[ROIPhysicalPropertiesSequenceItem]]):
        if value is None:
            self._ROIPhysicalPropertiesSequence = []
            if "ROIPhysicalPropertiesSequence" in self._dataset:
                del self._dataset.ROIPhysicalPropertiesSequence
        elif not isinstance(value, list) or not all(isinstance(item, ROIPhysicalPropertiesSequenceItem) for item in value):
            raise ValueError(f"ROIPhysicalPropertiesSequence must be a list of ROIPhysicalPropertiesSequenceItem objects")
        else:
            self._ROIPhysicalPropertiesSequence = value
            if "ROIPhysicalPropertiesSequence" not in self._dataset:
                self._dataset.ROIPhysicalPropertiesSequence = pydicom.Sequence()
            self._dataset.ROIPhysicalPropertiesSequence.clear()
            self._dataset.ROIPhysicalPropertiesSequence.extend([item.to_dataset() for item in value])

    def add_ROIPhysicalProperties(self, item: ROIPhysicalPropertiesSequenceItem):
        if not isinstance(item, ROIPhysicalPropertiesSequenceItem):
            raise ValueError(f"Item must be an instance of ROIPhysicalPropertiesSequenceItem")
        self._ROIPhysicalPropertiesSequence.append(item)
        if "ROIPhysicalPropertiesSequence" not in self._dataset:
            self._dataset.ROIPhysicalPropertiesSequence = pydicom.Sequence()
        self._dataset.ROIPhysicalPropertiesSequence.append(item.to_dataset())

    @property
    def MaterialID(self) -> Optional[str]:
        if "MaterialID" in self._dataset:
            return self._dataset.MaterialID
        return None

    @MaterialID.setter
    def MaterialID(self, value: Optional[str]):
        if value is None:
            if "MaterialID" in self._dataset:
                del self._dataset.MaterialID
        else:
            self._dataset.MaterialID = value

    @property
    def TherapeuticRoleCategoryCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "TherapeuticRoleCategoryCodeSequence" in self._dataset:
            if len(self._TherapeuticRoleCategoryCodeSequence) == len(self._dataset.TherapeuticRoleCategoryCodeSequence):
                return self._TherapeuticRoleCategoryCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.TherapeuticRoleCategoryCodeSequence]
        return None

    @TherapeuticRoleCategoryCodeSequence.setter
    def TherapeuticRoleCategoryCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._TherapeuticRoleCategoryCodeSequence = []
            if "TherapeuticRoleCategoryCodeSequence" in self._dataset:
                del self._dataset.TherapeuticRoleCategoryCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError(f"TherapeuticRoleCategoryCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._TherapeuticRoleCategoryCodeSequence = value
            if "TherapeuticRoleCategoryCodeSequence" not in self._dataset:
                self._dataset.TherapeuticRoleCategoryCodeSequence = pydicom.Sequence()
            self._dataset.TherapeuticRoleCategoryCodeSequence.clear()
            self._dataset.TherapeuticRoleCategoryCodeSequence.extend([item.to_dataset() for item in value])

    def add_TherapeuticRoleCategoryCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError(f"Item must be an instance of CodeSequenceItem")
        self._TherapeuticRoleCategoryCodeSequence.append(item)
        if "TherapeuticRoleCategoryCodeSequence" not in self._dataset:
            self._dataset.TherapeuticRoleCategoryCodeSequence = pydicom.Sequence()
        self._dataset.TherapeuticRoleCategoryCodeSequence.append(item.to_dataset())

    @property
    def TherapeuticRoleTypeCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "TherapeuticRoleTypeCodeSequence" in self._dataset:
            if len(self._TherapeuticRoleTypeCodeSequence) == len(self._dataset.TherapeuticRoleTypeCodeSequence):
                return self._TherapeuticRoleTypeCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.TherapeuticRoleTypeCodeSequence]
        return None

    @TherapeuticRoleTypeCodeSequence.setter
    def TherapeuticRoleTypeCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._TherapeuticRoleTypeCodeSequence = []
            if "TherapeuticRoleTypeCodeSequence" in self._dataset:
                del self._dataset.TherapeuticRoleTypeCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError(f"TherapeuticRoleTypeCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._TherapeuticRoleTypeCodeSequence = value
            if "TherapeuticRoleTypeCodeSequence" not in self._dataset:
                self._dataset.TherapeuticRoleTypeCodeSequence = pydicom.Sequence()
            self._dataset.TherapeuticRoleTypeCodeSequence.clear()
            self._dataset.TherapeuticRoleTypeCodeSequence.extend([item.to_dataset() for item in value])

    def add_TherapeuticRoleTypeCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError(f"Item must be an instance of CodeSequenceItem")
        self._TherapeuticRoleTypeCodeSequence.append(item)
        if "TherapeuticRoleTypeCodeSequence" not in self._dataset:
            self._dataset.TherapeuticRoleTypeCodeSequence = pydicom.Sequence()
        self._dataset.TherapeuticRoleTypeCodeSequence.append(item.to_dataset())
