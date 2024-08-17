from typing import Any, List, Optional  # noqa

import pydicom

from .derivation_algorithm_sequence_item import DerivationAlgorithmSequenceItem
from .performed_processing_parameters_sequence_item import (
    PerformedProcessingParametersSequenceItem,
)


class MultienergyCTCharacteristicsSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._DerivationAlgorithmSequence: List[DerivationAlgorithmSequenceItem] = []
        self._PerformedProcessingParametersSequence: List[PerformedProcessingParametersSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def MonoenergeticEnergyEquivalent(self) -> Optional[float]:
        if "MonoenergeticEnergyEquivalent" in self._dataset:
            return self._dataset.MonoenergeticEnergyEquivalent
        return None

    @MonoenergeticEnergyEquivalent.setter
    def MonoenergeticEnergyEquivalent(self, value: Optional[float]):
        if value is None:
            if "MonoenergeticEnergyEquivalent" in self._dataset:
                del self._dataset.MonoenergeticEnergyEquivalent
        else:
            self._dataset.MonoenergeticEnergyEquivalent = value

    @property
    def DerivationAlgorithmSequence(self) -> Optional[List[DerivationAlgorithmSequenceItem]]:
        if "DerivationAlgorithmSequence" in self._dataset:
            if len(self._DerivationAlgorithmSequence) == len(self._dataset.DerivationAlgorithmSequence):
                return self._DerivationAlgorithmSequence
            else:
                return [DerivationAlgorithmSequenceItem(x) for x in self._dataset.DerivationAlgorithmSequence]
        return None

    @DerivationAlgorithmSequence.setter
    def DerivationAlgorithmSequence(self, value: Optional[List[DerivationAlgorithmSequenceItem]]):
        if value is None:
            self._DerivationAlgorithmSequence = []
            if "DerivationAlgorithmSequence" in self._dataset:
                del self._dataset.DerivationAlgorithmSequence
        elif not isinstance(value, list) or not all(isinstance(item, DerivationAlgorithmSequenceItem) for item in value):
            raise ValueError("DerivationAlgorithmSequence must be a list of DerivationAlgorithmSequenceItem objects")
        else:
            self._DerivationAlgorithmSequence = value
            if "DerivationAlgorithmSequence" not in self._dataset:
                self._dataset.DerivationAlgorithmSequence = pydicom.Sequence()
            self._dataset.DerivationAlgorithmSequence.clear()
            self._dataset.DerivationAlgorithmSequence.extend([item.to_dataset() for item in value])

    def add_DerivationAlgorithm(self, item: DerivationAlgorithmSequenceItem):
        if not isinstance(item, DerivationAlgorithmSequenceItem):
            raise ValueError("Item must be an instance of DerivationAlgorithmSequenceItem")
        self._DerivationAlgorithmSequence.append(item)
        if "DerivationAlgorithmSequence" not in self._dataset:
            self._dataset.DerivationAlgorithmSequence = pydicom.Sequence()
        self._dataset.DerivationAlgorithmSequence.append(item.to_dataset())

    @property
    def PerformedProcessingParametersSequence(self) -> Optional[List[PerformedProcessingParametersSequenceItem]]:
        if "PerformedProcessingParametersSequence" in self._dataset:
            if len(self._PerformedProcessingParametersSequence) == len(self._dataset.PerformedProcessingParametersSequence):
                return self._PerformedProcessingParametersSequence
            else:
                return [
                    PerformedProcessingParametersSequenceItem(x) for x in self._dataset.PerformedProcessingParametersSequence
                ]
        return None

    @PerformedProcessingParametersSequence.setter
    def PerformedProcessingParametersSequence(self, value: Optional[List[PerformedProcessingParametersSequenceItem]]):
        if value is None:
            self._PerformedProcessingParametersSequence = []
            if "PerformedProcessingParametersSequence" in self._dataset:
                del self._dataset.PerformedProcessingParametersSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, PerformedProcessingParametersSequenceItem) for item in value
        ):
            raise ValueError(
                "PerformedProcessingParametersSequence must be a list of PerformedProcessingParametersSequenceItem objects"
            )
        else:
            self._PerformedProcessingParametersSequence = value
            if "PerformedProcessingParametersSequence" not in self._dataset:
                self._dataset.PerformedProcessingParametersSequence = pydicom.Sequence()
            self._dataset.PerformedProcessingParametersSequence.clear()
            self._dataset.PerformedProcessingParametersSequence.extend([item.to_dataset() for item in value])

    def add_PerformedProcessingParameters(self, item: PerformedProcessingParametersSequenceItem):
        if not isinstance(item, PerformedProcessingParametersSequenceItem):
            raise ValueError("Item must be an instance of PerformedProcessingParametersSequenceItem")
        self._PerformedProcessingParametersSequence.append(item)
        if "PerformedProcessingParametersSequence" not in self._dataset:
            self._dataset.PerformedProcessingParametersSequence = pydicom.Sequence()
        self._dataset.PerformedProcessingParametersSequence.append(item.to_dataset())
