from decimal import Decimal
from typing import Any, List, Optional

import pydicom

from .patient_location_coordinates_sequence_item import (
    PatientLocationCoordinatesSequenceItem,
)
from .patient_support_position_sequence_item import PatientSupportPositionSequenceItem


class TreatmentPositionSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._PatientLocationCoordinatesSequence: List[PatientLocationCoordinatesSequenceItem] = []
        self._PatientSupportPositionSequence: List[PatientSupportPositionSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ImageToEquipmentMappingMatrix(self) -> Optional[List[Decimal]]:
        if "ImageToEquipmentMappingMatrix" in self._dataset:
            return self._dataset.ImageToEquipmentMappingMatrix
        return None

    @ImageToEquipmentMappingMatrix.setter
    def ImageToEquipmentMappingMatrix(self, value: Optional[List[Decimal]]):
        if value is None:
            if "ImageToEquipmentMappingMatrix" in self._dataset:
                del self._dataset.ImageToEquipmentMappingMatrix
        else:
            self._dataset.ImageToEquipmentMappingMatrix = value

    @property
    def FrameOfReferenceTransformationComment(self) -> Optional[str]:
        if "FrameOfReferenceTransformationComment" in self._dataset:
            return self._dataset.FrameOfReferenceTransformationComment
        return None

    @FrameOfReferenceTransformationComment.setter
    def FrameOfReferenceTransformationComment(self, value: Optional[str]):
        if value is None:
            if "FrameOfReferenceTransformationComment" in self._dataset:
                del self._dataset.FrameOfReferenceTransformationComment
        else:
            self._dataset.FrameOfReferenceTransformationComment = value

    @property
    def PatientLocationCoordinatesSequence(self) -> Optional[List[PatientLocationCoordinatesSequenceItem]]:
        if "PatientLocationCoordinatesSequence" in self._dataset:
            if len(self._PatientLocationCoordinatesSequence) == len(self._dataset.PatientLocationCoordinatesSequence):
                return self._PatientLocationCoordinatesSequence
            else:
                return [PatientLocationCoordinatesSequenceItem(x) for x in self._dataset.PatientLocationCoordinatesSequence]
        return None

    @PatientLocationCoordinatesSequence.setter
    def PatientLocationCoordinatesSequence(self, value: Optional[List[PatientLocationCoordinatesSequenceItem]]):
        if value is None:
            self._PatientLocationCoordinatesSequence = []
            if "PatientLocationCoordinatesSequence" in self._dataset:
                del self._dataset.PatientLocationCoordinatesSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, PatientLocationCoordinatesSequenceItem) for item in value
        ):
            raise ValueError(
                f"PatientLocationCoordinatesSequence must be a list of PatientLocationCoordinatesSequenceItem objects"
            )
        else:
            self._PatientLocationCoordinatesSequence = value
            if "PatientLocationCoordinatesSequence" not in self._dataset:
                self._dataset.PatientLocationCoordinatesSequence = pydicom.Sequence()
            self._dataset.PatientLocationCoordinatesSequence.clear()
            self._dataset.PatientLocationCoordinatesSequence.extend([item.to_dataset() for item in value])

    def add_PatientLocationCoordinates(self, item: PatientLocationCoordinatesSequenceItem):
        if not isinstance(item, PatientLocationCoordinatesSequenceItem):
            raise ValueError(f"Item must be an instance of PatientLocationCoordinatesSequenceItem")
        self._PatientLocationCoordinatesSequence.append(item)
        if "PatientLocationCoordinatesSequence" not in self._dataset:
            self._dataset.PatientLocationCoordinatesSequence = pydicom.Sequence()
        self._dataset.PatientLocationCoordinatesSequence.append(item.to_dataset())

    @property
    def PatientSupportPositionSequence(self) -> Optional[List[PatientSupportPositionSequenceItem]]:
        if "PatientSupportPositionSequence" in self._dataset:
            if len(self._PatientSupportPositionSequence) == len(self._dataset.PatientSupportPositionSequence):
                return self._PatientSupportPositionSequence
            else:
                return [PatientSupportPositionSequenceItem(x) for x in self._dataset.PatientSupportPositionSequence]
        return None

    @PatientSupportPositionSequence.setter
    def PatientSupportPositionSequence(self, value: Optional[List[PatientSupportPositionSequenceItem]]):
        if value is None:
            self._PatientSupportPositionSequence = []
            if "PatientSupportPositionSequence" in self._dataset:
                del self._dataset.PatientSupportPositionSequence
        elif not isinstance(value, list) or not all(isinstance(item, PatientSupportPositionSequenceItem) for item in value):
            raise ValueError(f"PatientSupportPositionSequence must be a list of PatientSupportPositionSequenceItem objects")
        else:
            self._PatientSupportPositionSequence = value
            if "PatientSupportPositionSequence" not in self._dataset:
                self._dataset.PatientSupportPositionSequence = pydicom.Sequence()
            self._dataset.PatientSupportPositionSequence.clear()
            self._dataset.PatientSupportPositionSequence.extend([item.to_dataset() for item in value])

    def add_PatientSupportPosition(self, item: PatientSupportPositionSequenceItem):
        if not isinstance(item, PatientSupportPositionSequenceItem):
            raise ValueError(f"Item must be an instance of PatientSupportPositionSequenceItem")
        self._PatientSupportPositionSequence.append(item)
        if "PatientSupportPositionSequence" not in self._dataset:
            self._dataset.PatientSupportPositionSequence = pydicom.Sequence()
        self._dataset.PatientSupportPositionSequence.append(item.to_dataset())

    @property
    def TreatmentPositionIndex(self) -> Optional[int]:
        if "TreatmentPositionIndex" in self._dataset:
            return self._dataset.TreatmentPositionIndex
        return None

    @TreatmentPositionIndex.setter
    def TreatmentPositionIndex(self, value: Optional[int]):
        if value is None:
            if "TreatmentPositionIndex" in self._dataset:
                del self._dataset.TreatmentPositionIndex
        else:
            self._dataset.TreatmentPositionIndex = value
