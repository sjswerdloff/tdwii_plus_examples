from typing import Any, List, Optional

import pydicom

from .equivalent_conceptual_volume_instance_reference_sequence_item import (
    EquivalentConceptualVolumeInstanceReferenceSequenceItem,
)


class EquivalentConceptualVolumesSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._EquivalentConceptualVolumeInstanceReferenceSequence: List[
            EquivalentConceptualVolumeInstanceReferenceSequenceItem
        ] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def EquivalentConceptualVolumeInstanceReferenceSequence(
        self,
    ) -> Optional[List[EquivalentConceptualVolumeInstanceReferenceSequenceItem]]:
        if "EquivalentConceptualVolumeInstanceReferenceSequence" in self._dataset:
            if len(self._EquivalentConceptualVolumeInstanceReferenceSequence) == len(
                self._dataset.EquivalentConceptualVolumeInstanceReferenceSequence
            ):
                return self._EquivalentConceptualVolumeInstanceReferenceSequence
            else:
                return [
                    EquivalentConceptualVolumeInstanceReferenceSequenceItem(x)
                    for x in self._dataset.EquivalentConceptualVolumeInstanceReferenceSequence
                ]
        return None

    @EquivalentConceptualVolumeInstanceReferenceSequence.setter
    def EquivalentConceptualVolumeInstanceReferenceSequence(
        self, value: Optional[List[EquivalentConceptualVolumeInstanceReferenceSequenceItem]]
    ):
        if value is None:
            self._EquivalentConceptualVolumeInstanceReferenceSequence = []
            if "EquivalentConceptualVolumeInstanceReferenceSequence" in self._dataset:
                del self._dataset.EquivalentConceptualVolumeInstanceReferenceSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, EquivalentConceptualVolumeInstanceReferenceSequenceItem) for item in value
        ):
            raise ValueError(
                f"EquivalentConceptualVolumeInstanceReferenceSequence must be a list of EquivalentConceptualVolumeInstanceReferenceSequenceItem objects"
            )
        else:
            self._EquivalentConceptualVolumeInstanceReferenceSequence = value
            if "EquivalentConceptualVolumeInstanceReferenceSequence" not in self._dataset:
                self._dataset.EquivalentConceptualVolumeInstanceReferenceSequence = pydicom.Sequence()
            self._dataset.EquivalentConceptualVolumeInstanceReferenceSequence.clear()
            self._dataset.EquivalentConceptualVolumeInstanceReferenceSequence.extend([item.to_dataset() for item in value])

    def add_EquivalentConceptualVolumeInstanceReference(self, item: EquivalentConceptualVolumeInstanceReferenceSequenceItem):
        if not isinstance(item, EquivalentConceptualVolumeInstanceReferenceSequenceItem):
            raise ValueError(f"Item must be an instance of EquivalentConceptualVolumeInstanceReferenceSequenceItem")
        self._EquivalentConceptualVolumeInstanceReferenceSequence.append(item)
        if "EquivalentConceptualVolumeInstanceReferenceSequence" not in self._dataset:
            self._dataset.EquivalentConceptualVolumeInstanceReferenceSequence = pydicom.Sequence()
        self._dataset.EquivalentConceptualVolumeInstanceReferenceSequence.append(item.to_dataset())

    @property
    def ReferencedConceptualVolumeUID(self) -> Optional[str]:
        if "ReferencedConceptualVolumeUID" in self._dataset:
            return self._dataset.ReferencedConceptualVolumeUID
        return None

    @ReferencedConceptualVolumeUID.setter
    def ReferencedConceptualVolumeUID(self, value: Optional[str]):
        if value is None:
            if "ReferencedConceptualVolumeUID" in self._dataset:
                del self._dataset.ReferencedConceptualVolumeUID
        else:
            self._dataset.ReferencedConceptualVolumeUID = value
