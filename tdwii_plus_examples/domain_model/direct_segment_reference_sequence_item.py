from typing import Any, List, Optional

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
from .referenced_sop_sequence_item import ReferencedSOPSequenceItem


class DirectSegmentReferenceSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._ReferencedSOPSequence: List[ReferencedSOPSequenceItem] = []
        self._OriginatingSOPInstanceReferenceSequence: List[OriginatingSOPInstanceReferenceSequenceItem] = []
        self._EquivalentConceptualVolumesSequence: List[EquivalentConceptualVolumesSequenceItem] = []
        self._DerivationConceptualVolumeSequence: List[DerivationConceptualVolumeSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ReferencedSOPSequence(self) -> Optional[List[ReferencedSOPSequenceItem]]:
        if "ReferencedSOPSequence" in self._dataset:
            if len(self._ReferencedSOPSequence) == len(self._dataset.ReferencedSOPSequence):
                return self._ReferencedSOPSequence
            else:
                return [ReferencedSOPSequenceItem(x) for x in self._dataset.ReferencedSOPSequence]
        return None

    @ReferencedSOPSequence.setter
    def ReferencedSOPSequence(self, value: Optional[List[ReferencedSOPSequenceItem]]):
        if value is None:
            self._ReferencedSOPSequence = []
            if "ReferencedSOPSequence" in self._dataset:
                del self._dataset.ReferencedSOPSequence
        elif not isinstance(value, list) or not all(isinstance(item, ReferencedSOPSequenceItem) for item in value):
            raise ValueError(f"ReferencedSOPSequence must be a list of ReferencedSOPSequenceItem objects")
        else:
            self._ReferencedSOPSequence = value
            if "ReferencedSOPSequence" not in self._dataset:
                self._dataset.ReferencedSOPSequence = pydicom.Sequence()
            self._dataset.ReferencedSOPSequence.clear()
            self._dataset.ReferencedSOPSequence.extend([item.to_dataset() for item in value])

    def add_ReferencedSOP(self, item: ReferencedSOPSequenceItem):
        if not isinstance(item, ReferencedSOPSequenceItem):
            raise ValueError(f"Item must be an instance of ReferencedSOPSequenceItem")
        self._ReferencedSOPSequence.append(item)
        if "ReferencedSOPSequence" not in self._dataset:
            self._dataset.ReferencedSOPSequence = pydicom.Sequence()
        self._dataset.ReferencedSOPSequence.append(item.to_dataset())

    @property
    def ReferencedSegmentNumber(self) -> Optional[List[int]]:
        if "ReferencedSegmentNumber" in self._dataset:
            return self._dataset.ReferencedSegmentNumber
        return None

    @ReferencedSegmentNumber.setter
    def ReferencedSegmentNumber(self, value: Optional[List[int]]):
        if value is None:
            if "ReferencedSegmentNumber" in self._dataset:
                del self._dataset.ReferencedSegmentNumber
        else:
            self._dataset.ReferencedSegmentNumber = value

    @property
    def ReferencedSurfaceNumber(self) -> Optional[int]:
        if "ReferencedSurfaceNumber" in self._dataset:
            return self._dataset.ReferencedSurfaceNumber
        return None

    @ReferencedSurfaceNumber.setter
    def ReferencedSurfaceNumber(self, value: Optional[int]):
        if value is None:
            if "ReferencedSurfaceNumber" in self._dataset:
                del self._dataset.ReferencedSurfaceNumber
        else:
            self._dataset.ReferencedSurfaceNumber = value

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
                f"OriginatingSOPInstanceReferenceSequence must be a list of OriginatingSOPInstanceReferenceSequenceItem objects"
            )
        else:
            self._OriginatingSOPInstanceReferenceSequence = value
            if "OriginatingSOPInstanceReferenceSequence" not in self._dataset:
                self._dataset.OriginatingSOPInstanceReferenceSequence = pydicom.Sequence()
            self._dataset.OriginatingSOPInstanceReferenceSequence.clear()
            self._dataset.OriginatingSOPInstanceReferenceSequence.extend([item.to_dataset() for item in value])

    def add_OriginatingSOPInstanceReference(self, item: OriginatingSOPInstanceReferenceSequenceItem):
        if not isinstance(item, OriginatingSOPInstanceReferenceSequenceItem):
            raise ValueError(f"Item must be an instance of OriginatingSOPInstanceReferenceSequenceItem")
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
                f"EquivalentConceptualVolumesSequence must be a list of EquivalentConceptualVolumesSequenceItem objects"
            )
        else:
            self._EquivalentConceptualVolumesSequence = value
            if "EquivalentConceptualVolumesSequence" not in self._dataset:
                self._dataset.EquivalentConceptualVolumesSequence = pydicom.Sequence()
            self._dataset.EquivalentConceptualVolumesSequence.clear()
            self._dataset.EquivalentConceptualVolumesSequence.extend([item.to_dataset() for item in value])

    def add_EquivalentConceptualVolumes(self, item: EquivalentConceptualVolumesSequenceItem):
        if not isinstance(item, EquivalentConceptualVolumesSequenceItem):
            raise ValueError(f"Item must be an instance of EquivalentConceptualVolumesSequenceItem")
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
                f"DerivationConceptualVolumeSequence must be a list of DerivationConceptualVolumeSequenceItem objects"
            )
        else:
            self._DerivationConceptualVolumeSequence = value
            if "DerivationConceptualVolumeSequence" not in self._dataset:
                self._dataset.DerivationConceptualVolumeSequence = pydicom.Sequence()
            self._dataset.DerivationConceptualVolumeSequence.clear()
            self._dataset.DerivationConceptualVolumeSequence.extend([item.to_dataset() for item in value])

    def add_DerivationConceptualVolume(self, item: DerivationConceptualVolumeSequenceItem):
        if not isinstance(item, DerivationConceptualVolumeSequenceItem):
            raise ValueError(f"Item must be an instance of DerivationConceptualVolumeSequenceItem")
        self._DerivationConceptualVolumeSequence.append(item)
        if "DerivationConceptualVolumeSequence" not in self._dataset:
            self._dataset.DerivationConceptualVolumeSequence = pydicom.Sequence()
        self._dataset.DerivationConceptualVolumeSequence.append(item.to_dataset())

    @property
    def ReferencedFiducialsUID(self) -> Optional[str]:
        if "ReferencedFiducialsUID" in self._dataset:
            return self._dataset.ReferencedFiducialsUID
        return None

    @ReferencedFiducialsUID.setter
    def ReferencedFiducialsUID(self, value: Optional[str]):
        if value is None:
            if "ReferencedFiducialsUID" in self._dataset:
                del self._dataset.ReferencedFiducialsUID
        else:
            self._dataset.ReferencedFiducialsUID = value
