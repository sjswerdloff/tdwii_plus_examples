from typing import Any, List, Optional  # noqa

import pydicom

from .code_sequence_item import CodeSequenceItem
from .segment_characteristics_sequence_item import SegmentCharacteristicsSequenceItem
from .segmented_rt_accessory_device_sequence_item import (
    SegmentedRTAccessoryDeviceSequenceItem,
)


class RTSegmentAnnotationSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._SegmentedRTAccessoryDeviceSequence: List[SegmentedRTAccessoryDeviceSequenceItem] = []
        self._SegmentCharacteristicsSequence: List[SegmentCharacteristicsSequenceItem] = []
        self._SegmentAnnotationCategoryCodeSequence: List[CodeSequenceItem] = []
        self._SegmentAnnotationTypeCodeSequence: List[CodeSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

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
    def RecommendedPresentationOpacity(self) -> Optional[float]:
        if "RecommendedPresentationOpacity" in self._dataset:
            return self._dataset.RecommendedPresentationOpacity
        return None

    @RecommendedPresentationOpacity.setter
    def RecommendedPresentationOpacity(self, value: Optional[float]):
        if value is None:
            if "RecommendedPresentationOpacity" in self._dataset:
                del self._dataset.RecommendedPresentationOpacity
        else:
            self._dataset.RecommendedPresentationOpacity = value

    @property
    def RecommendedPresentationType(self) -> Optional[str]:
        if "RecommendedPresentationType" in self._dataset:
            return self._dataset.RecommendedPresentationType
        return None

    @RecommendedPresentationType.setter
    def RecommendedPresentationType(self, value: Optional[str]):
        if value is None:
            if "RecommendedPresentationType" in self._dataset:
                del self._dataset.RecommendedPresentationType
        else:
            self._dataset.RecommendedPresentationType = value

    @property
    def SegmentationCreationTemplateLabel(self) -> Optional[str]:
        if "SegmentationCreationTemplateLabel" in self._dataset:
            return self._dataset.SegmentationCreationTemplateLabel
        return None

    @SegmentationCreationTemplateLabel.setter
    def SegmentationCreationTemplateLabel(self, value: Optional[str]):
        if value is None:
            if "SegmentationCreationTemplateLabel" in self._dataset:
                del self._dataset.SegmentationCreationTemplateLabel
        else:
            self._dataset.SegmentationCreationTemplateLabel = value

    @property
    def ReferencedSegmentReferenceIndex(self) -> Optional[int]:
        if "ReferencedSegmentReferenceIndex" in self._dataset:
            return self._dataset.ReferencedSegmentReferenceIndex
        return None

    @ReferencedSegmentReferenceIndex.setter
    def ReferencedSegmentReferenceIndex(self, value: Optional[int]):
        if value is None:
            if "ReferencedSegmentReferenceIndex" in self._dataset:
                del self._dataset.ReferencedSegmentReferenceIndex
        else:
            self._dataset.ReferencedSegmentReferenceIndex = value

    @property
    def SegmentedRTAccessoryDeviceSequence(self) -> Optional[List[SegmentedRTAccessoryDeviceSequenceItem]]:
        if "SegmentedRTAccessoryDeviceSequence" in self._dataset:
            if len(self._SegmentedRTAccessoryDeviceSequence) == len(self._dataset.SegmentedRTAccessoryDeviceSequence):
                return self._SegmentedRTAccessoryDeviceSequence
            else:
                return [SegmentedRTAccessoryDeviceSequenceItem(x) for x in self._dataset.SegmentedRTAccessoryDeviceSequence]
        return None

    @SegmentedRTAccessoryDeviceSequence.setter
    def SegmentedRTAccessoryDeviceSequence(self, value: Optional[List[SegmentedRTAccessoryDeviceSequenceItem]]):
        if value is None:
            self._SegmentedRTAccessoryDeviceSequence = []
            if "SegmentedRTAccessoryDeviceSequence" in self._dataset:
                del self._dataset.SegmentedRTAccessoryDeviceSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, SegmentedRTAccessoryDeviceSequenceItem) for item in value
        ):
            raise ValueError(
                "SegmentedRTAccessoryDeviceSequence must be a list of SegmentedRTAccessoryDeviceSequenceItem objects"
            )
        else:
            self._SegmentedRTAccessoryDeviceSequence = value
            if "SegmentedRTAccessoryDeviceSequence" not in self._dataset:
                self._dataset.SegmentedRTAccessoryDeviceSequence = pydicom.Sequence()
            self._dataset.SegmentedRTAccessoryDeviceSequence.clear()
            self._dataset.SegmentedRTAccessoryDeviceSequence.extend([item.to_dataset() for item in value])

    def add_SegmentedRTAccessoryDevice(self, item: SegmentedRTAccessoryDeviceSequenceItem):
        if not isinstance(item, SegmentedRTAccessoryDeviceSequenceItem):
            raise ValueError("Item must be an instance of SegmentedRTAccessoryDeviceSequenceItem")
        self._SegmentedRTAccessoryDeviceSequence.append(item)
        if "SegmentedRTAccessoryDeviceSequence" not in self._dataset:
            self._dataset.SegmentedRTAccessoryDeviceSequence = pydicom.Sequence()
        self._dataset.SegmentedRTAccessoryDeviceSequence.append(item.to_dataset())

    @property
    def SegmentCharacteristicsSequence(self) -> Optional[List[SegmentCharacteristicsSequenceItem]]:
        if "SegmentCharacteristicsSequence" in self._dataset:
            if len(self._SegmentCharacteristicsSequence) == len(self._dataset.SegmentCharacteristicsSequence):
                return self._SegmentCharacteristicsSequence
            else:
                return [SegmentCharacteristicsSequenceItem(x) for x in self._dataset.SegmentCharacteristicsSequence]
        return None

    @SegmentCharacteristicsSequence.setter
    def SegmentCharacteristicsSequence(self, value: Optional[List[SegmentCharacteristicsSequenceItem]]):
        if value is None:
            self._SegmentCharacteristicsSequence = []
            if "SegmentCharacteristicsSequence" in self._dataset:
                del self._dataset.SegmentCharacteristicsSequence
        elif not isinstance(value, list) or not all(isinstance(item, SegmentCharacteristicsSequenceItem) for item in value):
            raise ValueError("SegmentCharacteristicsSequence must be a list of SegmentCharacteristicsSequenceItem objects")
        else:
            self._SegmentCharacteristicsSequence = value
            if "SegmentCharacteristicsSequence" not in self._dataset:
                self._dataset.SegmentCharacteristicsSequence = pydicom.Sequence()
            self._dataset.SegmentCharacteristicsSequence.clear()
            self._dataset.SegmentCharacteristicsSequence.extend([item.to_dataset() for item in value])

    def add_SegmentCharacteristics(self, item: SegmentCharacteristicsSequenceItem):
        if not isinstance(item, SegmentCharacteristicsSequenceItem):
            raise ValueError("Item must be an instance of SegmentCharacteristicsSequenceItem")
        self._SegmentCharacteristicsSequence.append(item)
        if "SegmentCharacteristicsSequence" not in self._dataset:
            self._dataset.SegmentCharacteristicsSequence = pydicom.Sequence()
        self._dataset.SegmentCharacteristicsSequence.append(item.to_dataset())

    @property
    def SegmentCharacteristicsPrecedence(self) -> Optional[int]:
        if "SegmentCharacteristicsPrecedence" in self._dataset:
            return self._dataset.SegmentCharacteristicsPrecedence
        return None

    @SegmentCharacteristicsPrecedence.setter
    def SegmentCharacteristicsPrecedence(self, value: Optional[int]):
        if value is None:
            if "SegmentCharacteristicsPrecedence" in self._dataset:
                del self._dataset.SegmentCharacteristicsPrecedence
        else:
            self._dataset.SegmentCharacteristicsPrecedence = value

    @property
    def SegmentAnnotationCategoryCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "SegmentAnnotationCategoryCodeSequence" in self._dataset:
            if len(self._SegmentAnnotationCategoryCodeSequence) == len(self._dataset.SegmentAnnotationCategoryCodeSequence):
                return self._SegmentAnnotationCategoryCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.SegmentAnnotationCategoryCodeSequence]
        return None

    @SegmentAnnotationCategoryCodeSequence.setter
    def SegmentAnnotationCategoryCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._SegmentAnnotationCategoryCodeSequence = []
            if "SegmentAnnotationCategoryCodeSequence" in self._dataset:
                del self._dataset.SegmentAnnotationCategoryCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("SegmentAnnotationCategoryCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._SegmentAnnotationCategoryCodeSequence = value
            if "SegmentAnnotationCategoryCodeSequence" not in self._dataset:
                self._dataset.SegmentAnnotationCategoryCodeSequence = pydicom.Sequence()
            self._dataset.SegmentAnnotationCategoryCodeSequence.clear()
            self._dataset.SegmentAnnotationCategoryCodeSequence.extend([item.to_dataset() for item in value])

    def add_SegmentAnnotationCategoryCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._SegmentAnnotationCategoryCodeSequence.append(item)
        if "SegmentAnnotationCategoryCodeSequence" not in self._dataset:
            self._dataset.SegmentAnnotationCategoryCodeSequence = pydicom.Sequence()
        self._dataset.SegmentAnnotationCategoryCodeSequence.append(item.to_dataset())

    @property
    def SegmentAnnotationTypeCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "SegmentAnnotationTypeCodeSequence" in self._dataset:
            if len(self._SegmentAnnotationTypeCodeSequence) == len(self._dataset.SegmentAnnotationTypeCodeSequence):
                return self._SegmentAnnotationTypeCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.SegmentAnnotationTypeCodeSequence]
        return None

    @SegmentAnnotationTypeCodeSequence.setter
    def SegmentAnnotationTypeCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._SegmentAnnotationTypeCodeSequence = []
            if "SegmentAnnotationTypeCodeSequence" in self._dataset:
                del self._dataset.SegmentAnnotationTypeCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("SegmentAnnotationTypeCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._SegmentAnnotationTypeCodeSequence = value
            if "SegmentAnnotationTypeCodeSequence" not in self._dataset:
                self._dataset.SegmentAnnotationTypeCodeSequence = pydicom.Sequence()
            self._dataset.SegmentAnnotationTypeCodeSequence.clear()
            self._dataset.SegmentAnnotationTypeCodeSequence.extend([item.to_dataset() for item in value])

    def add_SegmentAnnotationTypeCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._SegmentAnnotationTypeCodeSequence.append(item)
        if "SegmentAnnotationTypeCodeSequence" not in self._dataset:
            self._dataset.SegmentAnnotationTypeCodeSequence = pydicom.Sequence()
        self._dataset.SegmentAnnotationTypeCodeSequence.append(item.to_dataset())

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
    def EntityLongLabel(self) -> Optional[str]:
        if "EntityLongLabel" in self._dataset:
            return self._dataset.EntityLongLabel
        return None

    @EntityLongLabel.setter
    def EntityLongLabel(self, value: Optional[str]):
        if value is None:
            if "EntityLongLabel" in self._dataset:
                del self._dataset.EntityLongLabel
        else:
            self._dataset.EntityLongLabel = value

    @property
    def RTSegmentAnnotationIndex(self) -> Optional[int]:
        if "RTSegmentAnnotationIndex" in self._dataset:
            return self._dataset.RTSegmentAnnotationIndex
        return None

    @RTSegmentAnnotationIndex.setter
    def RTSegmentAnnotationIndex(self, value: Optional[int]):
        if value is None:
            if "RTSegmentAnnotationIndex" in self._dataset:
                del self._dataset.RTSegmentAnnotationIndex
        else:
            self._dataset.RTSegmentAnnotationIndex = value
