from typing import Any, List, Optional  # noqa

import pydicom

from .conceptual_volume_sequence_item import ConceptualVolumeSequenceItem


class RadiationDoseIdentificationSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._ConceptualVolumeSequence: List[ConceptualVolumeSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def RadiationDoseIdentificationIndex(self) -> Optional[int]:
        if "RadiationDoseIdentificationIndex" in self._dataset:
            return self._dataset.RadiationDoseIdentificationIndex
        return None

    @RadiationDoseIdentificationIndex.setter
    def RadiationDoseIdentificationIndex(self, value: Optional[int]):
        if value is None:
            if "RadiationDoseIdentificationIndex" in self._dataset:
                del self._dataset.RadiationDoseIdentificationIndex
        else:
            self._dataset.RadiationDoseIdentificationIndex = value

    @property
    def ReferencedRadiationDoseIdentificationIndex(self) -> Optional[int]:
        if "ReferencedRadiationDoseIdentificationIndex" in self._dataset:
            return self._dataset.ReferencedRadiationDoseIdentificationIndex
        return None

    @ReferencedRadiationDoseIdentificationIndex.setter
    def ReferencedRadiationDoseIdentificationIndex(self, value: Optional[int]):
        if value is None:
            if "ReferencedRadiationDoseIdentificationIndex" in self._dataset:
                del self._dataset.ReferencedRadiationDoseIdentificationIndex
        else:
            self._dataset.ReferencedRadiationDoseIdentificationIndex = value

    @property
    def RadiationDoseIdentificationLabel(self) -> Optional[str]:
        if "RadiationDoseIdentificationLabel" in self._dataset:
            return self._dataset.RadiationDoseIdentificationLabel
        return None

    @RadiationDoseIdentificationLabel.setter
    def RadiationDoseIdentificationLabel(self, value: Optional[str]):
        if value is None:
            if "RadiationDoseIdentificationLabel" in self._dataset:
                del self._dataset.RadiationDoseIdentificationLabel
        else:
            self._dataset.RadiationDoseIdentificationLabel = value

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
