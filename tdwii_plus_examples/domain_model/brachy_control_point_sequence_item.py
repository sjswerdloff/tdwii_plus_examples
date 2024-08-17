from decimal import Decimal
from typing import Any, List, Optional  # noqa

import pydicom

from .brachy_referenced_dose_reference_sequence_item import (
    BrachyReferencedDoseReferenceSequenceItem,
)


class BrachyControlPointSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._BrachyReferencedDoseReferenceSequence: List[BrachyReferencedDoseReferenceSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ControlPointIndex(self) -> Optional[int]:
        if "ControlPointIndex" in self._dataset:
            return self._dataset.ControlPointIndex
        return None

    @ControlPointIndex.setter
    def ControlPointIndex(self, value: Optional[int]):
        if value is None:
            if "ControlPointIndex" in self._dataset:
                del self._dataset.ControlPointIndex
        else:
            self._dataset.ControlPointIndex = value

    @property
    def ControlPointRelativePosition(self) -> Optional[Decimal]:
        if "ControlPointRelativePosition" in self._dataset:
            return self._dataset.ControlPointRelativePosition
        return None

    @ControlPointRelativePosition.setter
    def ControlPointRelativePosition(self, value: Optional[Decimal]):
        if value is None:
            if "ControlPointRelativePosition" in self._dataset:
                del self._dataset.ControlPointRelativePosition
        else:
            self._dataset.ControlPointRelativePosition = value

    @property
    def ControlPoint3DPosition(self) -> Optional[List[Decimal]]:
        if "ControlPoint3DPosition" in self._dataset:
            return self._dataset.ControlPoint3DPosition
        return None

    @ControlPoint3DPosition.setter
    def ControlPoint3DPosition(self, value: Optional[List[Decimal]]):
        if value is None:
            if "ControlPoint3DPosition" in self._dataset:
                del self._dataset.ControlPoint3DPosition
        else:
            self._dataset.ControlPoint3DPosition = value

    @property
    def CumulativeTimeWeight(self) -> Optional[Decimal]:
        if "CumulativeTimeWeight" in self._dataset:
            return self._dataset.CumulativeTimeWeight
        return None

    @CumulativeTimeWeight.setter
    def CumulativeTimeWeight(self, value: Optional[Decimal]):
        if value is None:
            if "CumulativeTimeWeight" in self._dataset:
                del self._dataset.CumulativeTimeWeight
        else:
            self._dataset.CumulativeTimeWeight = value

    @property
    def ControlPointOrientation(self) -> Optional[List[float]]:
        if "ControlPointOrientation" in self._dataset:
            return self._dataset.ControlPointOrientation
        return None

    @ControlPointOrientation.setter
    def ControlPointOrientation(self, value: Optional[List[float]]):
        if value is None:
            if "ControlPointOrientation" in self._dataset:
                del self._dataset.ControlPointOrientation
        else:
            self._dataset.ControlPointOrientation = value

    @property
    def BrachyReferencedDoseReferenceSequence(self) -> Optional[List[BrachyReferencedDoseReferenceSequenceItem]]:
        if "BrachyReferencedDoseReferenceSequence" in self._dataset:
            if len(self._BrachyReferencedDoseReferenceSequence) == len(self._dataset.BrachyReferencedDoseReferenceSequence):
                return self._BrachyReferencedDoseReferenceSequence
            else:
                return [
                    BrachyReferencedDoseReferenceSequenceItem(x) for x in self._dataset.BrachyReferencedDoseReferenceSequence
                ]
        return None

    @BrachyReferencedDoseReferenceSequence.setter
    def BrachyReferencedDoseReferenceSequence(self, value: Optional[List[BrachyReferencedDoseReferenceSequenceItem]]):
        if value is None:
            self._BrachyReferencedDoseReferenceSequence = []
            if "BrachyReferencedDoseReferenceSequence" in self._dataset:
                del self._dataset.BrachyReferencedDoseReferenceSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, BrachyReferencedDoseReferenceSequenceItem) for item in value
        ):
            raise ValueError(
                "BrachyReferencedDoseReferenceSequence must be a list of BrachyReferencedDoseReferenceSequenceItem objects"
            )
        else:
            self._BrachyReferencedDoseReferenceSequence = value
            if "BrachyReferencedDoseReferenceSequence" not in self._dataset:
                self._dataset.BrachyReferencedDoseReferenceSequence = pydicom.Sequence()
            self._dataset.BrachyReferencedDoseReferenceSequence.clear()
            self._dataset.BrachyReferencedDoseReferenceSequence.extend([item.to_dataset() for item in value])

    def add_BrachyReferencedDoseReference(self, item: BrachyReferencedDoseReferenceSequenceItem):
        if not isinstance(item, BrachyReferencedDoseReferenceSequenceItem):
            raise ValueError("Item must be an instance of BrachyReferencedDoseReferenceSequenceItem")
        self._BrachyReferencedDoseReferenceSequence.append(item)
        if "BrachyReferencedDoseReferenceSequence" not in self._dataset:
            self._dataset.BrachyReferencedDoseReferenceSequence = pydicom.Sequence()
        self._dataset.BrachyReferencedDoseReferenceSequence.append(item.to_dataset())
