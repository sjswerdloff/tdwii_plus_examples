from decimal import Decimal
from typing import Any, List, Optional  # noqa

import pydicom

from .code_sequence_item import CodeSequenceItem
from .conceptual_volume_identification_sequence_item import (
    ConceptualVolumeIdentificationSequenceItem,
)
from .definition_source_sequence_item import DefinitionSourceSequenceItem
from .roi_creator_sequence_item import ROICreatorSequenceItem
from .roi_derivation_algorithm_identification_sequence_item import (
    ROIDerivationAlgorithmIdentificationSequenceItem,
)


class StructureSetROISequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._DefinitionSourceSequence: List[DefinitionSourceSequenceItem] = []
        self._DerivationCodeSequence: List[CodeSequenceItem] = []
        self._ROIDerivationAlgorithmIdentificationSequence: List[ROIDerivationAlgorithmIdentificationSequenceItem] = []
        self._ROICreatorSequence: List[ROICreatorSequenceItem] = []
        self._RTProtocolCodeSequence: List[CodeSequenceItem] = []
        self._ConceptualVolumeIdentificationSequence: List[ConceptualVolumeIdentificationSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def DefinitionSourceSequence(self) -> Optional[List[DefinitionSourceSequenceItem]]:
        if "DefinitionSourceSequence" in self._dataset:
            if len(self._DefinitionSourceSequence) == len(self._dataset.DefinitionSourceSequence):
                return self._DefinitionSourceSequence
            else:
                return [DefinitionSourceSequenceItem(x) for x in self._dataset.DefinitionSourceSequence]
        return None

    @DefinitionSourceSequence.setter
    def DefinitionSourceSequence(self, value: Optional[List[DefinitionSourceSequenceItem]]):
        if value is None:
            self._DefinitionSourceSequence = []
            if "DefinitionSourceSequence" in self._dataset:
                del self._dataset.DefinitionSourceSequence
        elif not isinstance(value, list) or not all(isinstance(item, DefinitionSourceSequenceItem) for item in value):
            raise ValueError("DefinitionSourceSequence must be a list of DefinitionSourceSequenceItem objects")
        else:
            self._DefinitionSourceSequence = value
            if "DefinitionSourceSequence" not in self._dataset:
                self._dataset.DefinitionSourceSequence = pydicom.Sequence()
            self._dataset.DefinitionSourceSequence.clear()
            self._dataset.DefinitionSourceSequence.extend([item.to_dataset() for item in value])

    def add_DefinitionSource(self, item: DefinitionSourceSequenceItem):
        if not isinstance(item, DefinitionSourceSequenceItem):
            raise ValueError("Item must be an instance of DefinitionSourceSequenceItem")
        self._DefinitionSourceSequence.append(item)
        if "DefinitionSourceSequence" not in self._dataset:
            self._dataset.DefinitionSourceSequence = pydicom.Sequence()
        self._dataset.DefinitionSourceSequence.append(item.to_dataset())

    @property
    def DerivationCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "DerivationCodeSequence" in self._dataset:
            if len(self._DerivationCodeSequence) == len(self._dataset.DerivationCodeSequence):
                return self._DerivationCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.DerivationCodeSequence]
        return None

    @DerivationCodeSequence.setter
    def DerivationCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._DerivationCodeSequence = []
            if "DerivationCodeSequence" in self._dataset:
                del self._dataset.DerivationCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("DerivationCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._DerivationCodeSequence = value
            if "DerivationCodeSequence" not in self._dataset:
                self._dataset.DerivationCodeSequence = pydicom.Sequence()
            self._dataset.DerivationCodeSequence.clear()
            self._dataset.DerivationCodeSequence.extend([item.to_dataset() for item in value])

    def add_DerivationCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._DerivationCodeSequence.append(item)
        if "DerivationCodeSequence" not in self._dataset:
            self._dataset.DerivationCodeSequence = pydicom.Sequence()
        self._dataset.DerivationCodeSequence.append(item.to_dataset())

    @property
    def ROINumber(self) -> Optional[int]:
        if "ROINumber" in self._dataset:
            return self._dataset.ROINumber
        return None

    @ROINumber.setter
    def ROINumber(self, value: Optional[int]):
        if value is None:
            if "ROINumber" in self._dataset:
                del self._dataset.ROINumber
        else:
            self._dataset.ROINumber = value

    @property
    def ReferencedFrameOfReferenceUID(self) -> Optional[str]:
        if "ReferencedFrameOfReferenceUID" in self._dataset:
            return self._dataset.ReferencedFrameOfReferenceUID
        return None

    @ReferencedFrameOfReferenceUID.setter
    def ReferencedFrameOfReferenceUID(self, value: Optional[str]):
        if value is None:
            if "ReferencedFrameOfReferenceUID" in self._dataset:
                del self._dataset.ReferencedFrameOfReferenceUID
        else:
            self._dataset.ReferencedFrameOfReferenceUID = value

    @property
    def ROIName(self) -> Optional[str]:
        if "ROIName" in self._dataset:
            return self._dataset.ROIName
        return None

    @ROIName.setter
    def ROIName(self, value: Optional[str]):
        if value is None:
            if "ROIName" in self._dataset:
                del self._dataset.ROIName
        else:
            self._dataset.ROIName = value

    @property
    def ROIDescription(self) -> Optional[str]:
        if "ROIDescription" in self._dataset:
            return self._dataset.ROIDescription
        return None

    @ROIDescription.setter
    def ROIDescription(self, value: Optional[str]):
        if value is None:
            if "ROIDescription" in self._dataset:
                del self._dataset.ROIDescription
        else:
            self._dataset.ROIDescription = value

    @property
    def ROIVolume(self) -> Optional[Decimal]:
        if "ROIVolume" in self._dataset:
            return self._dataset.ROIVolume
        return None

    @ROIVolume.setter
    def ROIVolume(self, value: Optional[Decimal]):
        if value is None:
            if "ROIVolume" in self._dataset:
                del self._dataset.ROIVolume
        else:
            self._dataset.ROIVolume = value

    @property
    def ROIDateTime(self) -> Optional[str]:
        if "ROIDateTime" in self._dataset:
            return self._dataset.ROIDateTime
        return None

    @ROIDateTime.setter
    def ROIDateTime(self, value: Optional[str]):
        if value is None:
            if "ROIDateTime" in self._dataset:
                del self._dataset.ROIDateTime
        else:
            self._dataset.ROIDateTime = value

    @property
    def ROIGenerationAlgorithm(self) -> Optional[str]:
        if "ROIGenerationAlgorithm" in self._dataset:
            return self._dataset.ROIGenerationAlgorithm
        return None

    @ROIGenerationAlgorithm.setter
    def ROIGenerationAlgorithm(self, value: Optional[str]):
        if value is None:
            if "ROIGenerationAlgorithm" in self._dataset:
                del self._dataset.ROIGenerationAlgorithm
        else:
            self._dataset.ROIGenerationAlgorithm = value

    @property
    def ROIDerivationAlgorithmIdentificationSequence(self) -> Optional[List[ROIDerivationAlgorithmIdentificationSequenceItem]]:
        if "ROIDerivationAlgorithmIdentificationSequence" in self._dataset:
            if len(self._ROIDerivationAlgorithmIdentificationSequence) == len(
                self._dataset.ROIDerivationAlgorithmIdentificationSequence
            ):
                return self._ROIDerivationAlgorithmIdentificationSequence
            else:
                return [
                    ROIDerivationAlgorithmIdentificationSequenceItem(x)
                    for x in self._dataset.ROIDerivationAlgorithmIdentificationSequence
                ]
        return None

    @ROIDerivationAlgorithmIdentificationSequence.setter
    def ROIDerivationAlgorithmIdentificationSequence(
        self, value: Optional[List[ROIDerivationAlgorithmIdentificationSequenceItem]]
    ):
        if value is None:
            self._ROIDerivationAlgorithmIdentificationSequence = []
            if "ROIDerivationAlgorithmIdentificationSequence" in self._dataset:
                del self._dataset.ROIDerivationAlgorithmIdentificationSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, ROIDerivationAlgorithmIdentificationSequenceItem) for item in value
        ):
            raise ValueError(
                "ROIDerivationAlgorithmIdentificationSequence must be a list of"
                " ROIDerivationAlgorithmIdentificationSequenceItem objects"
            )
        else:
            self._ROIDerivationAlgorithmIdentificationSequence = value
            if "ROIDerivationAlgorithmIdentificationSequence" not in self._dataset:
                self._dataset.ROIDerivationAlgorithmIdentificationSequence = pydicom.Sequence()
            self._dataset.ROIDerivationAlgorithmIdentificationSequence.clear()
            self._dataset.ROIDerivationAlgorithmIdentificationSequence.extend([item.to_dataset() for item in value])

    def add_ROIDerivationAlgorithmIdentification(self, item: ROIDerivationAlgorithmIdentificationSequenceItem):
        if not isinstance(item, ROIDerivationAlgorithmIdentificationSequenceItem):
            raise ValueError("Item must be an instance of ROIDerivationAlgorithmIdentificationSequenceItem")
        self._ROIDerivationAlgorithmIdentificationSequence.append(item)
        if "ROIDerivationAlgorithmIdentificationSequence" not in self._dataset:
            self._dataset.ROIDerivationAlgorithmIdentificationSequence = pydicom.Sequence()
        self._dataset.ROIDerivationAlgorithmIdentificationSequence.append(item.to_dataset())

    @property
    def ROIGenerationDescription(self) -> Optional[str]:
        if "ROIGenerationDescription" in self._dataset:
            return self._dataset.ROIGenerationDescription
        return None

    @ROIGenerationDescription.setter
    def ROIGenerationDescription(self, value: Optional[str]):
        if value is None:
            if "ROIGenerationDescription" in self._dataset:
                del self._dataset.ROIGenerationDescription
        else:
            self._dataset.ROIGenerationDescription = value

    @property
    def ROICreatorSequence(self) -> Optional[List[ROICreatorSequenceItem]]:
        if "ROICreatorSequence" in self._dataset:
            if len(self._ROICreatorSequence) == len(self._dataset.ROICreatorSequence):
                return self._ROICreatorSequence
            else:
                return [ROICreatorSequenceItem(x) for x in self._dataset.ROICreatorSequence]
        return None

    @ROICreatorSequence.setter
    def ROICreatorSequence(self, value: Optional[List[ROICreatorSequenceItem]]):
        if value is None:
            self._ROICreatorSequence = []
            if "ROICreatorSequence" in self._dataset:
                del self._dataset.ROICreatorSequence
        elif not isinstance(value, list) or not all(isinstance(item, ROICreatorSequenceItem) for item in value):
            raise ValueError("ROICreatorSequence must be a list of ROICreatorSequenceItem objects")
        else:
            self._ROICreatorSequence = value
            if "ROICreatorSequence" not in self._dataset:
                self._dataset.ROICreatorSequence = pydicom.Sequence()
            self._dataset.ROICreatorSequence.clear()
            self._dataset.ROICreatorSequence.extend([item.to_dataset() for item in value])

    def add_ROICreator(self, item: ROICreatorSequenceItem):
        if not isinstance(item, ROICreatorSequenceItem):
            raise ValueError("Item must be an instance of ROICreatorSequenceItem")
        self._ROICreatorSequence.append(item)
        if "ROICreatorSequence" not in self._dataset:
            self._dataset.ROICreatorSequence = pydicom.Sequence()
        self._dataset.ROICreatorSequence.append(item.to_dataset())

    @property
    def RTProtocolCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "RTProtocolCodeSequence" in self._dataset:
            if len(self._RTProtocolCodeSequence) == len(self._dataset.RTProtocolCodeSequence):
                return self._RTProtocolCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.RTProtocolCodeSequence]
        return None

    @RTProtocolCodeSequence.setter
    def RTProtocolCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._RTProtocolCodeSequence = []
            if "RTProtocolCodeSequence" in self._dataset:
                del self._dataset.RTProtocolCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("RTProtocolCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._RTProtocolCodeSequence = value
            if "RTProtocolCodeSequence" not in self._dataset:
                self._dataset.RTProtocolCodeSequence = pydicom.Sequence()
            self._dataset.RTProtocolCodeSequence.clear()
            self._dataset.RTProtocolCodeSequence.extend([item.to_dataset() for item in value])

    def add_RTProtocolCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._RTProtocolCodeSequence.append(item)
        if "RTProtocolCodeSequence" not in self._dataset:
            self._dataset.RTProtocolCodeSequence = pydicom.Sequence()
        self._dataset.RTProtocolCodeSequence.append(item.to_dataset())

    @property
    def ConceptualVolumeIdentificationSequence(self) -> Optional[List[ConceptualVolumeIdentificationSequenceItem]]:
        if "ConceptualVolumeIdentificationSequence" in self._dataset:
            if len(self._ConceptualVolumeIdentificationSequence) == len(self._dataset.ConceptualVolumeIdentificationSequence):
                return self._ConceptualVolumeIdentificationSequence
            else:
                return [
                    ConceptualVolumeIdentificationSequenceItem(x) for x in self._dataset.ConceptualVolumeIdentificationSequence
                ]
        return None

    @ConceptualVolumeIdentificationSequence.setter
    def ConceptualVolumeIdentificationSequence(self, value: Optional[List[ConceptualVolumeIdentificationSequenceItem]]):
        if value is None:
            self._ConceptualVolumeIdentificationSequence = []
            if "ConceptualVolumeIdentificationSequence" in self._dataset:
                del self._dataset.ConceptualVolumeIdentificationSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, ConceptualVolumeIdentificationSequenceItem) for item in value
        ):
            raise ValueError(
                "ConceptualVolumeIdentificationSequence must be a list of ConceptualVolumeIdentificationSequenceItem objects"
            )
        else:
            self._ConceptualVolumeIdentificationSequence = value
            if "ConceptualVolumeIdentificationSequence" not in self._dataset:
                self._dataset.ConceptualVolumeIdentificationSequence = pydicom.Sequence()
            self._dataset.ConceptualVolumeIdentificationSequence.clear()
            self._dataset.ConceptualVolumeIdentificationSequence.extend([item.to_dataset() for item in value])

    def add_ConceptualVolumeIdentification(self, item: ConceptualVolumeIdentificationSequenceItem):
        if not isinstance(item, ConceptualVolumeIdentificationSequenceItem):
            raise ValueError("Item must be an instance of ConceptualVolumeIdentificationSequenceItem")
        self._ConceptualVolumeIdentificationSequence.append(item)
        if "ConceptualVolumeIdentificationSequence" not in self._dataset:
            self._dataset.ConceptualVolumeIdentificationSequence = pydicom.Sequence()
        self._dataset.ConceptualVolumeIdentificationSequence.append(item.to_dataset())
