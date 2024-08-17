from typing import Any, List, Optional

import pydicom

from .code_sequence_item import CodeSequenceItem
from .conceptual_volume_sequence_item import ConceptualVolumeSequenceItem
from .patient_support_displacement_sequence_item import (
    PatientSupportDisplacementSequenceItem,
)


class RTPatientPositionDisplacementSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._PatientSupportDisplacementSequence: List[PatientSupportDisplacementSequenceItem] = []
        self._DisplacementReferenceLocationCodeSequence: List[CodeSequenceItem] = []
        self._ConceptualVolumeSequence: List[ConceptualVolumeSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def DisplacementReferenceLabel(self) -> Optional[str]:
        if "DisplacementReferenceLabel" in self._dataset:
            return self._dataset.DisplacementReferenceLabel
        return None

    @DisplacementReferenceLabel.setter
    def DisplacementReferenceLabel(self, value: Optional[str]):
        if value is None:
            if "DisplacementReferenceLabel" in self._dataset:
                del self._dataset.DisplacementReferenceLabel
        else:
            self._dataset.DisplacementReferenceLabel = value

    @property
    def DisplacementMatrix(self) -> Optional[List[float]]:
        if "DisplacementMatrix" in self._dataset:
            return self._dataset.DisplacementMatrix
        return None

    @DisplacementMatrix.setter
    def DisplacementMatrix(self, value: Optional[List[float]]):
        if value is None:
            if "DisplacementMatrix" in self._dataset:
                del self._dataset.DisplacementMatrix
        else:
            self._dataset.DisplacementMatrix = value

    @property
    def PatientSupportDisplacementSequence(self) -> Optional[List[PatientSupportDisplacementSequenceItem]]:
        if "PatientSupportDisplacementSequence" in self._dataset:
            if len(self._PatientSupportDisplacementSequence) == len(self._dataset.PatientSupportDisplacementSequence):
                return self._PatientSupportDisplacementSequence
            else:
                return [PatientSupportDisplacementSequenceItem(x) for x in self._dataset.PatientSupportDisplacementSequence]
        return None

    @PatientSupportDisplacementSequence.setter
    def PatientSupportDisplacementSequence(self, value: Optional[List[PatientSupportDisplacementSequenceItem]]):
        if value is None:
            self._PatientSupportDisplacementSequence = []
            if "PatientSupportDisplacementSequence" in self._dataset:
                del self._dataset.PatientSupportDisplacementSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, PatientSupportDisplacementSequenceItem) for item in value
        ):
            raise ValueError(
                f"PatientSupportDisplacementSequence must be a list of PatientSupportDisplacementSequenceItem objects"
            )
        else:
            self._PatientSupportDisplacementSequence = value
            if "PatientSupportDisplacementSequence" not in self._dataset:
                self._dataset.PatientSupportDisplacementSequence = pydicom.Sequence()
            self._dataset.PatientSupportDisplacementSequence.clear()
            self._dataset.PatientSupportDisplacementSequence.extend([item.to_dataset() for item in value])

    def add_PatientSupportDisplacement(self, item: PatientSupportDisplacementSequenceItem):
        if not isinstance(item, PatientSupportDisplacementSequenceItem):
            raise ValueError(f"Item must be an instance of PatientSupportDisplacementSequenceItem")
        self._PatientSupportDisplacementSequence.append(item)
        if "PatientSupportDisplacementSequence" not in self._dataset:
            self._dataset.PatientSupportDisplacementSequence = pydicom.Sequence()
        self._dataset.PatientSupportDisplacementSequence.append(item.to_dataset())

    @property
    def DisplacementReferenceLocationCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "DisplacementReferenceLocationCodeSequence" in self._dataset:
            if len(self._DisplacementReferenceLocationCodeSequence) == len(
                self._dataset.DisplacementReferenceLocationCodeSequence
            ):
                return self._DisplacementReferenceLocationCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.DisplacementReferenceLocationCodeSequence]
        return None

    @DisplacementReferenceLocationCodeSequence.setter
    def DisplacementReferenceLocationCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._DisplacementReferenceLocationCodeSequence = []
            if "DisplacementReferenceLocationCodeSequence" in self._dataset:
                del self._dataset.DisplacementReferenceLocationCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError(f"DisplacementReferenceLocationCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._DisplacementReferenceLocationCodeSequence = value
            if "DisplacementReferenceLocationCodeSequence" not in self._dataset:
                self._dataset.DisplacementReferenceLocationCodeSequence = pydicom.Sequence()
            self._dataset.DisplacementReferenceLocationCodeSequence.clear()
            self._dataset.DisplacementReferenceLocationCodeSequence.extend([item.to_dataset() for item in value])

    def add_DisplacementReferenceLocationCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError(f"Item must be an instance of CodeSequenceItem")
        self._DisplacementReferenceLocationCodeSequence.append(item)
        if "DisplacementReferenceLocationCodeSequence" not in self._dataset:
            self._dataset.DisplacementReferenceLocationCodeSequence = pydicom.Sequence()
        self._dataset.DisplacementReferenceLocationCodeSequence.append(item.to_dataset())

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
            raise ValueError(f"ConceptualVolumeSequence must be a list of ConceptualVolumeSequenceItem objects")
        else:
            self._ConceptualVolumeSequence = value
            if "ConceptualVolumeSequence" not in self._dataset:
                self._dataset.ConceptualVolumeSequence = pydicom.Sequence()
            self._dataset.ConceptualVolumeSequence.clear()
            self._dataset.ConceptualVolumeSequence.extend([item.to_dataset() for item in value])

    def add_ConceptualVolume(self, item: ConceptualVolumeSequenceItem):
        if not isinstance(item, ConceptualVolumeSequenceItem):
            raise ValueError(f"Item must be an instance of ConceptualVolumeSequenceItem")
        self._ConceptualVolumeSequence.append(item)
        if "ConceptualVolumeSequence" not in self._dataset:
            self._dataset.ConceptualVolumeSequence = pydicom.Sequence()
        self._dataset.ConceptualVolumeSequence.append(item.to_dataset())
