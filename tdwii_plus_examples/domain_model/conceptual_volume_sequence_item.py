from typing import Any, List, Optional  # noqa

import pydicom

from .conceptual_volume_constituent_sequence_item import (
    ConceptualVolumeConstituentSequenceItem,
)
from .conceptual_volume_segmentation_reference_sequence_item import (
    ConceptualVolumeSegmentationReferenceSequenceItem,
)
from .derivation_conceptual_volume_sequence_item import (
    DerivationConceptualVolumeSequenceItem,
)
from .equivalent_conceptual_volumes_sequence_item import (
    EquivalentConceptualVolumesSequenceItem,
)
from .originating_sop_instance_reference_sequence_item import (
    OriginatingSOPInstanceReferenceSequenceItem,
)


class ConceptualVolumeSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._OriginatingSOPInstanceReferenceSequence: List[OriginatingSOPInstanceReferenceSequenceItem] = []
        self._ConceptualVolumeConstituentSequence: List[ConceptualVolumeConstituentSequenceItem] = []
        self._EquivalentConceptualVolumesSequence: List[EquivalentConceptualVolumesSequenceItem] = []
        self._ConceptualVolumeSegmentationReferenceSequence: List[ConceptualVolumeSegmentationReferenceSequenceItem] = []
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
    def ConceptualVolumeConstituentSequence(self) -> Optional[List[ConceptualVolumeConstituentSequenceItem]]:
        if "ConceptualVolumeConstituentSequence" in self._dataset:
            if len(self._ConceptualVolumeConstituentSequence) == len(self._dataset.ConceptualVolumeConstituentSequence):
                return self._ConceptualVolumeConstituentSequence
            else:
                return [ConceptualVolumeConstituentSequenceItem(x) for x in self._dataset.ConceptualVolumeConstituentSequence]
        return None

    @ConceptualVolumeConstituentSequence.setter
    def ConceptualVolumeConstituentSequence(self, value: Optional[List[ConceptualVolumeConstituentSequenceItem]]):
        if value is None:
            self._ConceptualVolumeConstituentSequence = []
            if "ConceptualVolumeConstituentSequence" in self._dataset:
                del self._dataset.ConceptualVolumeConstituentSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, ConceptualVolumeConstituentSequenceItem) for item in value
        ):
            raise ValueError(
                "ConceptualVolumeConstituentSequence must be a list of ConceptualVolumeConstituentSequenceItem objects"
            )
        else:
            self._ConceptualVolumeConstituentSequence = value
            if "ConceptualVolumeConstituentSequence" not in self._dataset:
                self._dataset.ConceptualVolumeConstituentSequence = pydicom.Sequence()
            self._dataset.ConceptualVolumeConstituentSequence.clear()
            self._dataset.ConceptualVolumeConstituentSequence.extend([item.to_dataset() for item in value])

    def add_ConceptualVolumeConstituent(self, item: ConceptualVolumeConstituentSequenceItem):
        if not isinstance(item, ConceptualVolumeConstituentSequenceItem):
            raise ValueError("Item must be an instance of ConceptualVolumeConstituentSequenceItem")
        self._ConceptualVolumeConstituentSequence.append(item)
        if "ConceptualVolumeConstituentSequence" not in self._dataset:
            self._dataset.ConceptualVolumeConstituentSequence = pydicom.Sequence()
        self._dataset.ConceptualVolumeConstituentSequence.append(item.to_dataset())

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
    def ConceptualVolumeCombinationExpression(self) -> Optional[str]:
        if "ConceptualVolumeCombinationExpression" in self._dataset:
            return self._dataset.ConceptualVolumeCombinationExpression
        return None

    @ConceptualVolumeCombinationExpression.setter
    def ConceptualVolumeCombinationExpression(self, value: Optional[str]):
        if value is None:
            if "ConceptualVolumeCombinationExpression" in self._dataset:
                del self._dataset.ConceptualVolumeCombinationExpression
        else:
            self._dataset.ConceptualVolumeCombinationExpression = value

    @property
    def ConceptualVolumeCombinationFlag(self) -> Optional[str]:
        if "ConceptualVolumeCombinationFlag" in self._dataset:
            return self._dataset.ConceptualVolumeCombinationFlag
        return None

    @ConceptualVolumeCombinationFlag.setter
    def ConceptualVolumeCombinationFlag(self, value: Optional[str]):
        if value is None:
            if "ConceptualVolumeCombinationFlag" in self._dataset:
                del self._dataset.ConceptualVolumeCombinationFlag
        else:
            self._dataset.ConceptualVolumeCombinationFlag = value

    @property
    def ConceptualVolumeCombinationDescription(self) -> Optional[str]:
        if "ConceptualVolumeCombinationDescription" in self._dataset:
            return self._dataset.ConceptualVolumeCombinationDescription
        return None

    @ConceptualVolumeCombinationDescription.setter
    def ConceptualVolumeCombinationDescription(self, value: Optional[str]):
        if value is None:
            if "ConceptualVolumeCombinationDescription" in self._dataset:
                del self._dataset.ConceptualVolumeCombinationDescription
        else:
            self._dataset.ConceptualVolumeCombinationDescription = value

    @property
    def ConceptualVolumeSegmentationDefinedFlag(self) -> Optional[str]:
        if "ConceptualVolumeSegmentationDefinedFlag" in self._dataset:
            return self._dataset.ConceptualVolumeSegmentationDefinedFlag
        return None

    @ConceptualVolumeSegmentationDefinedFlag.setter
    def ConceptualVolumeSegmentationDefinedFlag(self, value: Optional[str]):
        if value is None:
            if "ConceptualVolumeSegmentationDefinedFlag" in self._dataset:
                del self._dataset.ConceptualVolumeSegmentationDefinedFlag
        else:
            self._dataset.ConceptualVolumeSegmentationDefinedFlag = value

    @property
    def ConceptualVolumeSegmentationReferenceSequence(
        self,
    ) -> Optional[List[ConceptualVolumeSegmentationReferenceSequenceItem]]:
        if "ConceptualVolumeSegmentationReferenceSequence" in self._dataset:
            if len(self._ConceptualVolumeSegmentationReferenceSequence) == len(
                self._dataset.ConceptualVolumeSegmentationReferenceSequence
            ):
                return self._ConceptualVolumeSegmentationReferenceSequence
            else:
                return [
                    ConceptualVolumeSegmentationReferenceSequenceItem(x)
                    for x in self._dataset.ConceptualVolumeSegmentationReferenceSequence
                ]
        return None

    @ConceptualVolumeSegmentationReferenceSequence.setter
    def ConceptualVolumeSegmentationReferenceSequence(
        self, value: Optional[List[ConceptualVolumeSegmentationReferenceSequenceItem]]
    ):
        if value is None:
            self._ConceptualVolumeSegmentationReferenceSequence = []
            if "ConceptualVolumeSegmentationReferenceSequence" in self._dataset:
                del self._dataset.ConceptualVolumeSegmentationReferenceSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, ConceptualVolumeSegmentationReferenceSequenceItem) for item in value
        ):
            raise ValueError(
                "ConceptualVolumeSegmentationReferenceSequence must be a list of"
                " ConceptualVolumeSegmentationReferenceSequenceItem objects"
            )
        else:
            self._ConceptualVolumeSegmentationReferenceSequence = value
            if "ConceptualVolumeSegmentationReferenceSequence" not in self._dataset:
                self._dataset.ConceptualVolumeSegmentationReferenceSequence = pydicom.Sequence()
            self._dataset.ConceptualVolumeSegmentationReferenceSequence.clear()
            self._dataset.ConceptualVolumeSegmentationReferenceSequence.extend([item.to_dataset() for item in value])

    def add_ConceptualVolumeSegmentationReference(self, item: ConceptualVolumeSegmentationReferenceSequenceItem):
        if not isinstance(item, ConceptualVolumeSegmentationReferenceSequenceItem):
            raise ValueError("Item must be an instance of ConceptualVolumeSegmentationReferenceSequenceItem")
        self._ConceptualVolumeSegmentationReferenceSequence.append(item)
        if "ConceptualVolumeSegmentationReferenceSequence" not in self._dataset:
            self._dataset.ConceptualVolumeSegmentationReferenceSequence = pydicom.Sequence()
        self._dataset.ConceptualVolumeSegmentationReferenceSequence.append(item.to_dataset())

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
