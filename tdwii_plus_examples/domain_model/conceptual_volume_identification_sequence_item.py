from typing import Any, List, Optional  # noqa

import pydicom

from .derivation_conceptual_volume_sequence_item import (
    DerivationConceptualVolumeSequenceItem,
)
from .equivalent_conceptual_volumes_sequence_item import (
    EquivalentConceptualVolumesSequenceItem,
)
from .originating_sop_instance_reference_sequence_item import (
    OriginatingSOPInstanceReferenceSequenceItem,
)


class ConceptualVolumeIdentificationSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._OriginatingSOPInstanceReferenceSequence: List[OriginatingSOPInstanceReferenceSequenceItem] = []
        self._EquivalentConceptualVolumesSequence: List[EquivalentConceptualVolumesSequenceItem] = []
        self._DerivationConceptualVolumeSequence: List[DerivationConceptualVolumeSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ConceptualVolumeUID(self) -> Optional[str]:
        if "ConceptualVolumeUID" in self._dataset:
            return self._dataset.ConceptualVolumeUID
        return None

    @ConceptualVolumeUID.setter
    def ConceptualVolumeUID(self, value: Optional[str]):
        if value is None:
            if "ConceptualVolumeUID" in self._dataset:
                del self._dataset.ConceptualVolumeUID
        else:
            self._dataset.ConceptualVolumeUID = value

    @property
    def OriginatingSOPInstanceReferenceSequence(self) -> Optional[List[OriginatingSOPInstanceReferenceSequenceItem]]:
        if "OriginatingSOPInstanceReferenceSequence" in self._dataset:
            if len(self._OriginatingSOPInstanceReferenceSequence) == len(
                self._dataset.OriginatingSOPInstanceReferenceSequence
            ):
                return self._OriginatingSOPInstanceReferenceSequence
            else:
                return [
                    OriginatingSOPInstanceReferenceSequenceItem(x)
                    for x in self._dataset.OriginatingSOPInstanceReferenceSequence
                ]
        return None

    @OriginatingSOPInstanceReferenceSequence.setter
    def OriginatingSOPInstanceReferenceSequence(self, value: Optional[List[OriginatingSOPInstanceReferenceSequenceItem]]):
        if value is None:
            self._OriginatingSOPInstanceReferenceSequence = []
            if "OriginatingSOPInstanceReferenceSequence" in self._dataset:
                del self._dataset.OriginatingSOPInstanceReferenceSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, OriginatingSOPInstanceReferenceSequenceItem) for item in value
        ):
            raise ValueError(
                "OriginatingSOPInstanceReferenceSequence must be a list of OriginatingSOPInstanceReferenceSequenceItem objects"
            )
        else:
            self._OriginatingSOPInstanceReferenceSequence = value
            if "OriginatingSOPInstanceReferenceSequence" not in self._dataset:
                self._dataset.OriginatingSOPInstanceReferenceSequence = pydicom.Sequence()
            self._dataset.OriginatingSOPInstanceReferenceSequence.clear()
            self._dataset.OriginatingSOPInstanceReferenceSequence.extend([item.to_dataset() for item in value])

    def add_OriginatingSOPInstanceReference(self, item: OriginatingSOPInstanceReferenceSequenceItem):
        if not isinstance(item, OriginatingSOPInstanceReferenceSequenceItem):
            raise ValueError("Item must be an instance of OriginatingSOPInstanceReferenceSequenceItem")
        self._OriginatingSOPInstanceReferenceSequence.append(item)
        if "OriginatingSOPInstanceReferenceSequence" not in self._dataset:
            self._dataset.OriginatingSOPInstanceReferenceSequence = pydicom.Sequence()
        self._dataset.OriginatingSOPInstanceReferenceSequence.append(item.to_dataset())

    @property
    def EquivalentConceptualVolumesSequence(self) -> Optional[List[EquivalentConceptualVolumesSequenceItem]]:
        if "EquivalentConceptualVolumesSequence" in self._dataset:
            if len(self._EquivalentConceptualVolumesSequence) == len(self._dataset.EquivalentConceptualVolumesSequence):
                return self._EquivalentConceptualVolumesSequence
            else:
                return [EquivalentConceptualVolumesSequenceItem(x) for x in self._dataset.EquivalentConceptualVolumesSequence]
        return None

    @EquivalentConceptualVolumesSequence.setter
    def EquivalentConceptualVolumesSequence(self, value: Optional[List[EquivalentConceptualVolumesSequenceItem]]):
        if value is None:
            self._EquivalentConceptualVolumesSequence = []
            if "EquivalentConceptualVolumesSequence" in self._dataset:
                del self._dataset.EquivalentConceptualVolumesSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, EquivalentConceptualVolumesSequenceItem) for item in value
        ):
            raise ValueError(
                "EquivalentConceptualVolumesSequence must be a list of EquivalentConceptualVolumesSequenceItem objects"
            )
        else:
            self._EquivalentConceptualVolumesSequence = value
            if "EquivalentConceptualVolumesSequence" not in self._dataset:
                self._dataset.EquivalentConceptualVolumesSequence = pydicom.Sequence()
            self._dataset.EquivalentConceptualVolumesSequence.clear()
            self._dataset.EquivalentConceptualVolumesSequence.extend([item.to_dataset() for item in value])

    def add_EquivalentConceptualVolumes(self, item: EquivalentConceptualVolumesSequenceItem):
        if not isinstance(item, EquivalentConceptualVolumesSequenceItem):
            raise ValueError("Item must be an instance of EquivalentConceptualVolumesSequenceItem")
        self._EquivalentConceptualVolumesSequence.append(item)
        if "EquivalentConceptualVolumesSequence" not in self._dataset:
            self._dataset.EquivalentConceptualVolumesSequence = pydicom.Sequence()
        self._dataset.EquivalentConceptualVolumesSequence.append(item.to_dataset())

    @property
    def DerivationConceptualVolumeSequence(self) -> Optional[List[DerivationConceptualVolumeSequenceItem]]:
        if "DerivationConceptualVolumeSequence" in self._dataset:
            if len(self._DerivationConceptualVolumeSequence) == len(self._dataset.DerivationConceptualVolumeSequence):
                return self._DerivationConceptualVolumeSequence
            else:
                return [DerivationConceptualVolumeSequenceItem(x) for x in self._dataset.DerivationConceptualVolumeSequence]
        return None

    @DerivationConceptualVolumeSequence.setter
    def DerivationConceptualVolumeSequence(self, value: Optional[List[DerivationConceptualVolumeSequenceItem]]):
        if value is None:
            self._DerivationConceptualVolumeSequence = []
            if "DerivationConceptualVolumeSequence" in self._dataset:
                del self._dataset.DerivationConceptualVolumeSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, DerivationConceptualVolumeSequenceItem) for item in value
        ):
            raise ValueError(
                "DerivationConceptualVolumeSequence must be a list of DerivationConceptualVolumeSequenceItem objects"
            )
        else:
            self._DerivationConceptualVolumeSequence = value
            if "DerivationConceptualVolumeSequence" not in self._dataset:
                self._dataset.DerivationConceptualVolumeSequence = pydicom.Sequence()
            self._dataset.DerivationConceptualVolumeSequence.clear()
            self._dataset.DerivationConceptualVolumeSequence.extend([item.to_dataset() for item in value])

    def add_DerivationConceptualVolume(self, item: DerivationConceptualVolumeSequenceItem):
        if not isinstance(item, DerivationConceptualVolumeSequenceItem):
            raise ValueError("Item must be an instance of DerivationConceptualVolumeSequenceItem")
        self._DerivationConceptualVolumeSequence.append(item)
        if "DerivationConceptualVolumeSequence" not in self._dataset:
            self._dataset.DerivationConceptualVolumeSequence = pydicom.Sequence()
        self._dataset.DerivationConceptualVolumeSequence.append(item.to_dataset())
