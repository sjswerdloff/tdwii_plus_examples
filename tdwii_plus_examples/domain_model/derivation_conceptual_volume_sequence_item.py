from typing import Any, List, Optional  # noqa

import pydicom

from .conceptual_volume_derivation_algorithm_sequence_item import (
    ConceptualVolumeDerivationAlgorithmSequenceItem,
)
from .source_conceptual_volume_sequence_item import SourceConceptualVolumeSequenceItem


class DerivationConceptualVolumeSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._ConceptualVolumeDerivationAlgorithmSequence: List[ConceptualVolumeDerivationAlgorithmSequenceItem] = []
        self._SourceConceptualVolumeSequence: List[SourceConceptualVolumeSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def DerivationDescription(self) -> Optional[str]:
        if "DerivationDescription" in self._dataset:
            return self._dataset.DerivationDescription
        return None

    @DerivationDescription.setter
    def DerivationDescription(self, value: Optional[str]):
        if value is None:
            if "DerivationDescription" in self._dataset:
                del self._dataset.DerivationDescription
        else:
            self._dataset.DerivationDescription = value

    @property
    def ConceptualVolumeDerivationAlgorithmSequence(self) -> Optional[List[ConceptualVolumeDerivationAlgorithmSequenceItem]]:
        if "ConceptualVolumeDerivationAlgorithmSequence" in self._dataset:
            if len(self._ConceptualVolumeDerivationAlgorithmSequence) == len(
                self._dataset.ConceptualVolumeDerivationAlgorithmSequence
            ):
                return self._ConceptualVolumeDerivationAlgorithmSequence
            else:
                return [
                    ConceptualVolumeDerivationAlgorithmSequenceItem(x)
                    for x in self._dataset.ConceptualVolumeDerivationAlgorithmSequence
                ]
        return None

    @ConceptualVolumeDerivationAlgorithmSequence.setter
    def ConceptualVolumeDerivationAlgorithmSequence(
        self, value: Optional[List[ConceptualVolumeDerivationAlgorithmSequenceItem]]
    ):
        if value is None:
            self._ConceptualVolumeDerivationAlgorithmSequence = []
            if "ConceptualVolumeDerivationAlgorithmSequence" in self._dataset:
                del self._dataset.ConceptualVolumeDerivationAlgorithmSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, ConceptualVolumeDerivationAlgorithmSequenceItem) for item in value
        ):
            raise ValueError(
                "ConceptualVolumeDerivationAlgorithmSequence must be a list of ConceptualVolumeDerivationAlgorithmSequenceItem"
                " objects"
            )
        else:
            self._ConceptualVolumeDerivationAlgorithmSequence = value
            if "ConceptualVolumeDerivationAlgorithmSequence" not in self._dataset:
                self._dataset.ConceptualVolumeDerivationAlgorithmSequence = pydicom.Sequence()
            self._dataset.ConceptualVolumeDerivationAlgorithmSequence.clear()
            self._dataset.ConceptualVolumeDerivationAlgorithmSequence.extend([item.to_dataset() for item in value])

    def add_ConceptualVolumeDerivationAlgorithm(self, item: ConceptualVolumeDerivationAlgorithmSequenceItem):
        if not isinstance(item, ConceptualVolumeDerivationAlgorithmSequenceItem):
            raise ValueError("Item must be an instance of ConceptualVolumeDerivationAlgorithmSequenceItem")
        self._ConceptualVolumeDerivationAlgorithmSequence.append(item)
        if "ConceptualVolumeDerivationAlgorithmSequence" not in self._dataset:
            self._dataset.ConceptualVolumeDerivationAlgorithmSequence = pydicom.Sequence()
        self._dataset.ConceptualVolumeDerivationAlgorithmSequence.append(item.to_dataset())

    @property
    def SourceConceptualVolumeSequence(self) -> Optional[List[SourceConceptualVolumeSequenceItem]]:
        if "SourceConceptualVolumeSequence" in self._dataset:
            if len(self._SourceConceptualVolumeSequence) == len(self._dataset.SourceConceptualVolumeSequence):
                return self._SourceConceptualVolumeSequence
            else:
                return [SourceConceptualVolumeSequenceItem(x) for x in self._dataset.SourceConceptualVolumeSequence]
        return None

    @SourceConceptualVolumeSequence.setter
    def SourceConceptualVolumeSequence(self, value: Optional[List[SourceConceptualVolumeSequenceItem]]):
        if value is None:
            self._SourceConceptualVolumeSequence = []
            if "SourceConceptualVolumeSequence" in self._dataset:
                del self._dataset.SourceConceptualVolumeSequence
        elif not isinstance(value, list) or not all(isinstance(item, SourceConceptualVolumeSequenceItem) for item in value):
            raise ValueError("SourceConceptualVolumeSequence must be a list of SourceConceptualVolumeSequenceItem objects")
        else:
            self._SourceConceptualVolumeSequence = value
            if "SourceConceptualVolumeSequence" not in self._dataset:
                self._dataset.SourceConceptualVolumeSequence = pydicom.Sequence()
            self._dataset.SourceConceptualVolumeSequence.clear()
            self._dataset.SourceConceptualVolumeSequence.extend([item.to_dataset() for item in value])

    def add_SourceConceptualVolume(self, item: SourceConceptualVolumeSequenceItem):
        if not isinstance(item, SourceConceptualVolumeSequenceItem):
            raise ValueError("Item must be an instance of SourceConceptualVolumeSequenceItem")
        self._SourceConceptualVolumeSequence.append(item)
        if "SourceConceptualVolumeSequence" not in self._dataset:
            self._dataset.SourceConceptualVolumeSequence = pydicom.Sequence()
        self._dataset.SourceConceptualVolumeSequence.append(item.to_dataset())
