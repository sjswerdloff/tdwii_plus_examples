from typing import Any, List, Optional

import pydicom

from .referenced_beam_sequence_item import ReferencedBeamSequenceItem
from .referenced_brachy_application_setup_sequence_item import (
    ReferencedBrachyApplicationSetupSequenceItem,
)


class ReferencedFractionGroupSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._ReferencedBeamSequence: List[ReferencedBeamSequenceItem] = []
        self._ReferencedBrachyApplicationSetupSequence: List[ReferencedBrachyApplicationSetupSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ReferencedBeamSequence(self) -> Optional[List[ReferencedBeamSequenceItem]]:
        if "ReferencedBeamSequence" in self._dataset:
            if len(self._ReferencedBeamSequence) == len(self._dataset.ReferencedBeamSequence):
                return self._ReferencedBeamSequence
            else:
                return [ReferencedBeamSequenceItem(x) for x in self._dataset.ReferencedBeamSequence]
        return None

    @ReferencedBeamSequence.setter
    def ReferencedBeamSequence(self, value: Optional[List[ReferencedBeamSequenceItem]]):
        if value is None:
            self._ReferencedBeamSequence = []
            if "ReferencedBeamSequence" in self._dataset:
                del self._dataset.ReferencedBeamSequence
        elif not isinstance(value, list) or not all(isinstance(item, ReferencedBeamSequenceItem) for item in value):
            raise ValueError(f"ReferencedBeamSequence must be a list of ReferencedBeamSequenceItem objects")
        else:
            self._ReferencedBeamSequence = value
            if "ReferencedBeamSequence" not in self._dataset:
                self._dataset.ReferencedBeamSequence = pydicom.Sequence()
            self._dataset.ReferencedBeamSequence.clear()
            self._dataset.ReferencedBeamSequence.extend([item.to_dataset() for item in value])

    def add_ReferencedBeam(self, item: ReferencedBeamSequenceItem):
        if not isinstance(item, ReferencedBeamSequenceItem):
            raise ValueError(f"Item must be an instance of ReferencedBeamSequenceItem")
        self._ReferencedBeamSequence.append(item)
        if "ReferencedBeamSequence" not in self._dataset:
            self._dataset.ReferencedBeamSequence = pydicom.Sequence()
        self._dataset.ReferencedBeamSequence.append(item.to_dataset())

    @property
    def ReferencedBrachyApplicationSetupSequence(self) -> Optional[List[ReferencedBrachyApplicationSetupSequenceItem]]:
        if "ReferencedBrachyApplicationSetupSequence" in self._dataset:
            if len(self._ReferencedBrachyApplicationSetupSequence) == len(
                self._dataset.ReferencedBrachyApplicationSetupSequence
            ):
                return self._ReferencedBrachyApplicationSetupSequence
            else:
                return [
                    ReferencedBrachyApplicationSetupSequenceItem(x)
                    for x in self._dataset.ReferencedBrachyApplicationSetupSequence
                ]
        return None

    @ReferencedBrachyApplicationSetupSequence.setter
    def ReferencedBrachyApplicationSetupSequence(self, value: Optional[List[ReferencedBrachyApplicationSetupSequenceItem]]):
        if value is None:
            self._ReferencedBrachyApplicationSetupSequence = []
            if "ReferencedBrachyApplicationSetupSequence" in self._dataset:
                del self._dataset.ReferencedBrachyApplicationSetupSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, ReferencedBrachyApplicationSetupSequenceItem) for item in value
        ):
            raise ValueError(
                f"ReferencedBrachyApplicationSetupSequence must be a list of ReferencedBrachyApplicationSetupSequenceItem objects"
            )
        else:
            self._ReferencedBrachyApplicationSetupSequence = value
            if "ReferencedBrachyApplicationSetupSequence" not in self._dataset:
                self._dataset.ReferencedBrachyApplicationSetupSequence = pydicom.Sequence()
            self._dataset.ReferencedBrachyApplicationSetupSequence.clear()
            self._dataset.ReferencedBrachyApplicationSetupSequence.extend([item.to_dataset() for item in value])

    def add_ReferencedBrachyApplicationSetup(self, item: ReferencedBrachyApplicationSetupSequenceItem):
        if not isinstance(item, ReferencedBrachyApplicationSetupSequenceItem):
            raise ValueError(f"Item must be an instance of ReferencedBrachyApplicationSetupSequenceItem")
        self._ReferencedBrachyApplicationSetupSequence.append(item)
        if "ReferencedBrachyApplicationSetupSequence" not in self._dataset:
            self._dataset.ReferencedBrachyApplicationSetupSequence = pydicom.Sequence()
        self._dataset.ReferencedBrachyApplicationSetupSequence.append(item.to_dataset())

    @property
    def ReferencedFractionGroupNumber(self) -> Optional[int]:
        if "ReferencedFractionGroupNumber" in self._dataset:
            return self._dataset.ReferencedFractionGroupNumber
        return None

    @ReferencedFractionGroupNumber.setter
    def ReferencedFractionGroupNumber(self, value: Optional[int]):
        if value is None:
            if "ReferencedFractionGroupNumber" in self._dataset:
                del self._dataset.ReferencedFractionGroupNumber
        else:
            self._dataset.ReferencedFractionGroupNumber = value
