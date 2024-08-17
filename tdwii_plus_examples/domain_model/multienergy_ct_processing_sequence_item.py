from typing import Any, List, Optional

import pydicom

from .decomposition_algorithm_identification_sequence_item import (
    DecompositionAlgorithmIdentificationSequenceItem,
)
from .decomposition_material_sequence_item import DecompositionMaterialSequenceItem


class MultienergyCTProcessingSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._DecompositionAlgorithmIdentificationSequence: List[DecompositionAlgorithmIdentificationSequenceItem] = []
        self._DecompositionMaterialSequence: List[DecompositionMaterialSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def DecompositionMethod(self) -> Optional[str]:
        if "DecompositionMethod" in self._dataset:
            return self._dataset.DecompositionMethod
        return None

    @DecompositionMethod.setter
    def DecompositionMethod(self, value: Optional[str]):
        if value is None:
            if "DecompositionMethod" in self._dataset:
                del self._dataset.DecompositionMethod
        else:
            self._dataset.DecompositionMethod = value

    @property
    def DecompositionDescription(self) -> Optional[str]:
        if "DecompositionDescription" in self._dataset:
            return self._dataset.DecompositionDescription
        return None

    @DecompositionDescription.setter
    def DecompositionDescription(self, value: Optional[str]):
        if value is None:
            if "DecompositionDescription" in self._dataset:
                del self._dataset.DecompositionDescription
        else:
            self._dataset.DecompositionDescription = value

    @property
    def DecompositionAlgorithmIdentificationSequence(self) -> Optional[List[DecompositionAlgorithmIdentificationSequenceItem]]:
        if "DecompositionAlgorithmIdentificationSequence" in self._dataset:
            if len(self._DecompositionAlgorithmIdentificationSequence) == len(
                self._dataset.DecompositionAlgorithmIdentificationSequence
            ):
                return self._DecompositionAlgorithmIdentificationSequence
            else:
                return [
                    DecompositionAlgorithmIdentificationSequenceItem(x)
                    for x in self._dataset.DecompositionAlgorithmIdentificationSequence
                ]
        return None

    @DecompositionAlgorithmIdentificationSequence.setter
    def DecompositionAlgorithmIdentificationSequence(
        self, value: Optional[List[DecompositionAlgorithmIdentificationSequenceItem]]
    ):
        if value is None:
            self._DecompositionAlgorithmIdentificationSequence = []
            if "DecompositionAlgorithmIdentificationSequence" in self._dataset:
                del self._dataset.DecompositionAlgorithmIdentificationSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, DecompositionAlgorithmIdentificationSequenceItem) for item in value
        ):
            raise ValueError(
                f"DecompositionAlgorithmIdentificationSequence must be a list of DecompositionAlgorithmIdentificationSequenceItem objects"
            )
        else:
            self._DecompositionAlgorithmIdentificationSequence = value
            if "DecompositionAlgorithmIdentificationSequence" not in self._dataset:
                self._dataset.DecompositionAlgorithmIdentificationSequence = pydicom.Sequence()
            self._dataset.DecompositionAlgorithmIdentificationSequence.clear()
            self._dataset.DecompositionAlgorithmIdentificationSequence.extend([item.to_dataset() for item in value])

    def add_DecompositionAlgorithmIdentification(self, item: DecompositionAlgorithmIdentificationSequenceItem):
        if not isinstance(item, DecompositionAlgorithmIdentificationSequenceItem):
            raise ValueError(f"Item must be an instance of DecompositionAlgorithmIdentificationSequenceItem")
        self._DecompositionAlgorithmIdentificationSequence.append(item)
        if "DecompositionAlgorithmIdentificationSequence" not in self._dataset:
            self._dataset.DecompositionAlgorithmIdentificationSequence = pydicom.Sequence()
        self._dataset.DecompositionAlgorithmIdentificationSequence.append(item.to_dataset())

    @property
    def DecompositionMaterialSequence(self) -> Optional[List[DecompositionMaterialSequenceItem]]:
        if "DecompositionMaterialSequence" in self._dataset:
            if len(self._DecompositionMaterialSequence) == len(self._dataset.DecompositionMaterialSequence):
                return self._DecompositionMaterialSequence
            else:
                return [DecompositionMaterialSequenceItem(x) for x in self._dataset.DecompositionMaterialSequence]
        return None

    @DecompositionMaterialSequence.setter
    def DecompositionMaterialSequence(self, value: Optional[List[DecompositionMaterialSequenceItem]]):
        if value is None:
            self._DecompositionMaterialSequence = []
            if "DecompositionMaterialSequence" in self._dataset:
                del self._dataset.DecompositionMaterialSequence
        elif not isinstance(value, list) or not all(isinstance(item, DecompositionMaterialSequenceItem) for item in value):
            raise ValueError(f"DecompositionMaterialSequence must be a list of DecompositionMaterialSequenceItem objects")
        else:
            self._DecompositionMaterialSequence = value
            if "DecompositionMaterialSequence" not in self._dataset:
                self._dataset.DecompositionMaterialSequence = pydicom.Sequence()
            self._dataset.DecompositionMaterialSequence.clear()
            self._dataset.DecompositionMaterialSequence.extend([item.to_dataset() for item in value])

    def add_DecompositionMaterial(self, item: DecompositionMaterialSequenceItem):
        if not isinstance(item, DecompositionMaterialSequenceItem):
            raise ValueError(f"Item must be an instance of DecompositionMaterialSequenceItem")
        self._DecompositionMaterialSequence.append(item)
        if "DecompositionMaterialSequence" not in self._dataset:
            self._dataset.DecompositionMaterialSequence = pydicom.Sequence()
        self._dataset.DecompositionMaterialSequence.append(item.to_dataset())
