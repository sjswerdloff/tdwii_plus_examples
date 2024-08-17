from typing import Any, List, Optional

import pydicom

from .conceptual_volume_constituent_segmentation_reference_sequence_item import (
    ConceptualVolumeConstituentSegmentationReferenceSequenceItem,
)


class SourceConceptualVolumeSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._ConceptualVolumeConstituentSegmentationReferenceSequence: List[
            ConceptualVolumeConstituentSegmentationReferenceSequenceItem
        ] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ConceptualVolumeConstituentIndex(self) -> Optional[int]:
        if "ConceptualVolumeConstituentIndex" in self._dataset:
            return self._dataset.ConceptualVolumeConstituentIndex
        return None

    @ConceptualVolumeConstituentIndex.setter
    def ConceptualVolumeConstituentIndex(self, value: Optional[int]):
        if value is None:
            if "ConceptualVolumeConstituentIndex" in self._dataset:
                del self._dataset.ConceptualVolumeConstituentIndex
        else:
            self._dataset.ConceptualVolumeConstituentIndex = value

    @property
    def ConceptualVolumeConstituentSegmentationReferenceSequence(
        self,
    ) -> Optional[List[ConceptualVolumeConstituentSegmentationReferenceSequenceItem]]:
        if "ConceptualVolumeConstituentSegmentationReferenceSequence" in self._dataset:
            if len(self._ConceptualVolumeConstituentSegmentationReferenceSequence) == len(
                self._dataset.ConceptualVolumeConstituentSegmentationReferenceSequence
            ):
                return self._ConceptualVolumeConstituentSegmentationReferenceSequence
            else:
                return [
                    ConceptualVolumeConstituentSegmentationReferenceSequenceItem(x)
                    for x in self._dataset.ConceptualVolumeConstituentSegmentationReferenceSequence
                ]
        return None

    @ConceptualVolumeConstituentSegmentationReferenceSequence.setter
    def ConceptualVolumeConstituentSegmentationReferenceSequence(
        self, value: Optional[List[ConceptualVolumeConstituentSegmentationReferenceSequenceItem]]
    ):
        if value is None:
            self._ConceptualVolumeConstituentSegmentationReferenceSequence = []
            if "ConceptualVolumeConstituentSegmentationReferenceSequence" in self._dataset:
                del self._dataset.ConceptualVolumeConstituentSegmentationReferenceSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, ConceptualVolumeConstituentSegmentationReferenceSequenceItem) for item in value
        ):
            raise ValueError(
                f"ConceptualVolumeConstituentSegmentationReferenceSequence must be a list of ConceptualVolumeConstituentSegmentationReferenceSequenceItem objects"
            )
        else:
            self._ConceptualVolumeConstituentSegmentationReferenceSequence = value
            if "ConceptualVolumeConstituentSegmentationReferenceSequence" not in self._dataset:
                self._dataset.ConceptualVolumeConstituentSegmentationReferenceSequence = pydicom.Sequence()
            self._dataset.ConceptualVolumeConstituentSegmentationReferenceSequence.clear()
            self._dataset.ConceptualVolumeConstituentSegmentationReferenceSequence.extend(
                [item.to_dataset() for item in value]
            )

    def add_ConceptualVolumeConstituentSegmentationReference(
        self, item: ConceptualVolumeConstituentSegmentationReferenceSequenceItem
    ):
        if not isinstance(item, ConceptualVolumeConstituentSegmentationReferenceSequenceItem):
            raise ValueError(f"Item must be an instance of ConceptualVolumeConstituentSegmentationReferenceSequenceItem")
        self._ConceptualVolumeConstituentSegmentationReferenceSequence.append(item)
        if "ConceptualVolumeConstituentSegmentationReferenceSequence" not in self._dataset:
            self._dataset.ConceptualVolumeConstituentSegmentationReferenceSequence = pydicom.Sequence()
        self._dataset.ConceptualVolumeConstituentSegmentationReferenceSequence.append(item.to_dataset())

    @property
    def SourceConceptualVolumeUID(self) -> Optional[str]:
        if "SourceConceptualVolumeUID" in self._dataset:
            return self._dataset.SourceConceptualVolumeUID
        return None

    @SourceConceptualVolumeUID.setter
    def SourceConceptualVolumeUID(self, value: Optional[str]):
        if value is None:
            if "SourceConceptualVolumeUID" in self._dataset:
                del self._dataset.SourceConceptualVolumeUID
        else:
            self._dataset.SourceConceptualVolumeUID = value
