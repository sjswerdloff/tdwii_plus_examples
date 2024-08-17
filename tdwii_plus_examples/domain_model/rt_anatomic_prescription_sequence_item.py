from typing import Any, List, Optional  # noqa

import pydicom

from .code_sequence_item import CodeSequenceItem
from .conceptual_volume_sequence_item import ConceptualVolumeSequenceItem


class RTAnatomicPrescriptionSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._ConceptualVolumeSequence: List[ConceptualVolumeSequenceItem] = []
        self._TherapeuticRoleCategoryCodeSequence: List[CodeSequenceItem] = []
        self._TherapeuticRoleTypeCodeSequence: List[CodeSequenceItem] = []
        self._ConceptualVolumeCategoryCodeSequence: List[CodeSequenceItem] = []
        self._ConceptualVolumeTypeCodeSequence: List[CodeSequenceItem] = []
        self._ConceptualVolumeTypeModifierCodeSequence: List[CodeSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

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
    def ConceptualVolumeDescription(self) -> Optional[str]:
        if "ConceptualVolumeDescription" in self._dataset:
            return self._dataset.ConceptualVolumeDescription
        return None

    @ConceptualVolumeDescription.setter
    def ConceptualVolumeDescription(self, value: Optional[str]):
        if value is None:
            if "ConceptualVolumeDescription" in self._dataset:
                del self._dataset.ConceptualVolumeDescription
        else:
            self._dataset.ConceptualVolumeDescription = value

    @property
    def ConceptualVolumeSequence(self) -> Optional[List[ConceptualVolumeSequenceItem]]:
        if "ConceptualVolumeSequence" in self._dataset:
            if len(self._ConceptualVolumeSequence) == len(self._dataset.ConceptualVolumeSequence):
                return self._ConceptualVolumeSequence
            else:
                return [ConceptualVolumeSequenceItem(x) for x in self._dataset.ConceptualVolumeSequence]
        return None

    @ConceptualVolumeSequence.setter
    def ConceptualVolumeSequence(self, value: Optional[List[ConceptualVolumeSequenceItem]]):
        if value is None:
            self._ConceptualVolumeSequence = []
            if "ConceptualVolumeSequence" in self._dataset:
                del self._dataset.ConceptualVolumeSequence
        elif not isinstance(value, list) or not all(isinstance(item, ConceptualVolumeSequenceItem) for item in value):
            raise ValueError("ConceptualVolumeSequence must be a list of ConceptualVolumeSequenceItem objects")
        else:
            self._ConceptualVolumeSequence = value
            if "ConceptualVolumeSequence" not in self._dataset:
                self._dataset.ConceptualVolumeSequence = pydicom.Sequence()
            self._dataset.ConceptualVolumeSequence.clear()
            self._dataset.ConceptualVolumeSequence.extend([item.to_dataset() for item in value])

    def add_ConceptualVolume(self, item: ConceptualVolumeSequenceItem):
        if not isinstance(item, ConceptualVolumeSequenceItem):
            raise ValueError("Item must be an instance of ConceptualVolumeSequenceItem")
        self._ConceptualVolumeSequence.append(item)
        if "ConceptualVolumeSequence" not in self._dataset:
            self._dataset.ConceptualVolumeSequence = pydicom.Sequence()
        self._dataset.ConceptualVolumeSequence.append(item.to_dataset())

    @property
    def EntityLabel(self) -> Optional[str]:
        if "EntityLabel" in self._dataset:
            return self._dataset.EntityLabel
        return None

    @EntityLabel.setter
    def EntityLabel(self, value: Optional[str]):
        if value is None:
            if "EntityLabel" in self._dataset:
                del self._dataset.EntityLabel
        else:
            self._dataset.EntityLabel = value

    @property
    def EntityName(self) -> Optional[str]:
        if "EntityName" in self._dataset:
            return self._dataset.EntityName
        return None

    @EntityName.setter
    def EntityName(self, value: Optional[str]):
        if value is None:
            if "EntityName" in self._dataset:
                del self._dataset.EntityName
        else:
            self._dataset.EntityName = value

    @property
    def EntityDescription(self) -> Optional[str]:
        if "EntityDescription" in self._dataset:
            return self._dataset.EntityDescription
        return None

    @EntityDescription.setter
    def EntityDescription(self, value: Optional[str]):
        if value is None:
            if "EntityDescription" in self._dataset:
                del self._dataset.EntityDescription
        else:
            self._dataset.EntityDescription = value

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
            raise ValueError("TherapeuticRoleCategoryCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._TherapeuticRoleCategoryCodeSequence = value
            if "TherapeuticRoleCategoryCodeSequence" not in self._dataset:
                self._dataset.TherapeuticRoleCategoryCodeSequence = pydicom.Sequence()
            self._dataset.TherapeuticRoleCategoryCodeSequence.clear()
            self._dataset.TherapeuticRoleCategoryCodeSequence.extend([item.to_dataset() for item in value])

    def add_TherapeuticRoleCategoryCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
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
            raise ValueError("TherapeuticRoleTypeCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._TherapeuticRoleTypeCodeSequence = value
            if "TherapeuticRoleTypeCodeSequence" not in self._dataset:
                self._dataset.TherapeuticRoleTypeCodeSequence = pydicom.Sequence()
            self._dataset.TherapeuticRoleTypeCodeSequence.clear()
            self._dataset.TherapeuticRoleTypeCodeSequence.extend([item.to_dataset() for item in value])

    def add_TherapeuticRoleTypeCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._TherapeuticRoleTypeCodeSequence.append(item)
        if "TherapeuticRoleTypeCodeSequence" not in self._dataset:
            self._dataset.TherapeuticRoleTypeCodeSequence = pydicom.Sequence()
        self._dataset.TherapeuticRoleTypeCodeSequence.append(item.to_dataset())

    @property
    def ConceptualVolumeOptimizationPrecedence(self) -> Optional[int]:
        if "ConceptualVolumeOptimizationPrecedence" in self._dataset:
            return self._dataset.ConceptualVolumeOptimizationPrecedence
        return None

    @ConceptualVolumeOptimizationPrecedence.setter
    def ConceptualVolumeOptimizationPrecedence(self, value: Optional[int]):
        if value is None:
            if "ConceptualVolumeOptimizationPrecedence" in self._dataset:
                del self._dataset.ConceptualVolumeOptimizationPrecedence
        else:
            self._dataset.ConceptualVolumeOptimizationPrecedence = value

    @property
    def ConceptualVolumeCategoryCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "ConceptualVolumeCategoryCodeSequence" in self._dataset:
            if len(self._ConceptualVolumeCategoryCodeSequence) == len(self._dataset.ConceptualVolumeCategoryCodeSequence):
                return self._ConceptualVolumeCategoryCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.ConceptualVolumeCategoryCodeSequence]
        return None

    @ConceptualVolumeCategoryCodeSequence.setter
    def ConceptualVolumeCategoryCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._ConceptualVolumeCategoryCodeSequence = []
            if "ConceptualVolumeCategoryCodeSequence" in self._dataset:
                del self._dataset.ConceptualVolumeCategoryCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("ConceptualVolumeCategoryCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._ConceptualVolumeCategoryCodeSequence = value
            if "ConceptualVolumeCategoryCodeSequence" not in self._dataset:
                self._dataset.ConceptualVolumeCategoryCodeSequence = pydicom.Sequence()
            self._dataset.ConceptualVolumeCategoryCodeSequence.clear()
            self._dataset.ConceptualVolumeCategoryCodeSequence.extend([item.to_dataset() for item in value])

    def add_ConceptualVolumeCategoryCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._ConceptualVolumeCategoryCodeSequence.append(item)
        if "ConceptualVolumeCategoryCodeSequence" not in self._dataset:
            self._dataset.ConceptualVolumeCategoryCodeSequence = pydicom.Sequence()
        self._dataset.ConceptualVolumeCategoryCodeSequence.append(item.to_dataset())

    @property
    def ConceptualVolumeBlockingConstraint(self) -> Optional[str]:
        if "ConceptualVolumeBlockingConstraint" in self._dataset:
            return self._dataset.ConceptualVolumeBlockingConstraint
        return None

    @ConceptualVolumeBlockingConstraint.setter
    def ConceptualVolumeBlockingConstraint(self, value: Optional[str]):
        if value is None:
            if "ConceptualVolumeBlockingConstraint" in self._dataset:
                del self._dataset.ConceptualVolumeBlockingConstraint
        else:
            self._dataset.ConceptualVolumeBlockingConstraint = value

    @property
    def ConceptualVolumeTypeCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "ConceptualVolumeTypeCodeSequence" in self._dataset:
            if len(self._ConceptualVolumeTypeCodeSequence) == len(self._dataset.ConceptualVolumeTypeCodeSequence):
                return self._ConceptualVolumeTypeCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.ConceptualVolumeTypeCodeSequence]
        return None

    @ConceptualVolumeTypeCodeSequence.setter
    def ConceptualVolumeTypeCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._ConceptualVolumeTypeCodeSequence = []
            if "ConceptualVolumeTypeCodeSequence" in self._dataset:
                del self._dataset.ConceptualVolumeTypeCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("ConceptualVolumeTypeCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._ConceptualVolumeTypeCodeSequence = value
            if "ConceptualVolumeTypeCodeSequence" not in self._dataset:
                self._dataset.ConceptualVolumeTypeCodeSequence = pydicom.Sequence()
            self._dataset.ConceptualVolumeTypeCodeSequence.clear()
            self._dataset.ConceptualVolumeTypeCodeSequence.extend([item.to_dataset() for item in value])

    def add_ConceptualVolumeTypeCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._ConceptualVolumeTypeCodeSequence.append(item)
        if "ConceptualVolumeTypeCodeSequence" not in self._dataset:
            self._dataset.ConceptualVolumeTypeCodeSequence = pydicom.Sequence()
        self._dataset.ConceptualVolumeTypeCodeSequence.append(item.to_dataset())

    @property
    def ConceptualVolumeTypeModifierCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "ConceptualVolumeTypeModifierCodeSequence" in self._dataset:
            if len(self._ConceptualVolumeTypeModifierCodeSequence) == len(
                self._dataset.ConceptualVolumeTypeModifierCodeSequence
            ):
                return self._ConceptualVolumeTypeModifierCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.ConceptualVolumeTypeModifierCodeSequence]
        return None

    @ConceptualVolumeTypeModifierCodeSequence.setter
    def ConceptualVolumeTypeModifierCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._ConceptualVolumeTypeModifierCodeSequence = []
            if "ConceptualVolumeTypeModifierCodeSequence" in self._dataset:
                del self._dataset.ConceptualVolumeTypeModifierCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("ConceptualVolumeTypeModifierCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._ConceptualVolumeTypeModifierCodeSequence = value
            if "ConceptualVolumeTypeModifierCodeSequence" not in self._dataset:
                self._dataset.ConceptualVolumeTypeModifierCodeSequence = pydicom.Sequence()
            self._dataset.ConceptualVolumeTypeModifierCodeSequence.clear()
            self._dataset.ConceptualVolumeTypeModifierCodeSequence.extend([item.to_dataset() for item in value])

    def add_ConceptualVolumeTypeModifierCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._ConceptualVolumeTypeModifierCodeSequence.append(item)
        if "ConceptualVolumeTypeModifierCodeSequence" not in self._dataset:
            self._dataset.ConceptualVolumeTypeModifierCodeSequence = pydicom.Sequence()
        self._dataset.ConceptualVolumeTypeModifierCodeSequence.append(item.to_dataset())
