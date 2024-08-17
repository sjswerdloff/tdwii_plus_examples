from decimal import Decimal
from typing import Any, List, Optional  # noqa

import pydicom

from .override_sequence_item import OverrideSequenceItem


class BrachyControlPointDeliveredSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._OverrideSequence: List[OverrideSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def TreatmentControlPointDate(self) -> Optional[str]:
        if "TreatmentControlPointDate" in self._dataset:
            return self._dataset.TreatmentControlPointDate
        return None

    @TreatmentControlPointDate.setter
    def TreatmentControlPointDate(self, value: Optional[str]):
        if value is None:
            if "TreatmentControlPointDate" in self._dataset:
                del self._dataset.TreatmentControlPointDate
        else:
            self._dataset.TreatmentControlPointDate = value

    @property
    def TreatmentControlPointTime(self) -> Optional[str]:
        if "TreatmentControlPointTime" in self._dataset:
            return self._dataset.TreatmentControlPointTime
        return None

    @TreatmentControlPointTime.setter
    def TreatmentControlPointTime(self, value: Optional[str]):
        if value is None:
            if "TreatmentControlPointTime" in self._dataset:
                del self._dataset.TreatmentControlPointTime
        else:
            self._dataset.TreatmentControlPointTime = value

    @property
    def OverrideSequence(self) -> Optional[List[OverrideSequenceItem]]:
        if "OverrideSequence" in self._dataset:
            if len(self._OverrideSequence) == len(self._dataset.OverrideSequence):
                return self._OverrideSequence
            else:
                return [OverrideSequenceItem(x) for x in self._dataset.OverrideSequence]
        return None

    @OverrideSequence.setter
    def OverrideSequence(self, value: Optional[List[OverrideSequenceItem]]):
        if value is None:
            self._OverrideSequence = []
            if "OverrideSequence" in self._dataset:
                del self._dataset.OverrideSequence
        elif not isinstance(value, list) or not all(isinstance(item, OverrideSequenceItem) for item in value):
            raise ValueError("OverrideSequence must be a list of OverrideSequenceItem objects")
        else:
            self._OverrideSequence = value
            if "OverrideSequence" not in self._dataset:
                self._dataset.OverrideSequence = pydicom.Sequence()
            self._dataset.OverrideSequence.clear()
            self._dataset.OverrideSequence.extend([item.to_dataset() for item in value])

    def add_Override(self, item: OverrideSequenceItem):
        if not isinstance(item, OverrideSequenceItem):
            raise ValueError("Item must be an instance of OverrideSequenceItem")
        self._OverrideSequence.append(item)
        if "OverrideSequence" not in self._dataset:
            self._dataset.OverrideSequence = pydicom.Sequence()
        self._dataset.OverrideSequence.append(item.to_dataset())

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
    def ReferencedControlPointIndex(self) -> Optional[int]:
        if "ReferencedControlPointIndex" in self._dataset:
            return self._dataset.ReferencedControlPointIndex
        return None

    @ReferencedControlPointIndex.setter
    def ReferencedControlPointIndex(self, value: Optional[int]):
        if value is None:
            if "ReferencedControlPointIndex" in self._dataset:
                del self._dataset.ReferencedControlPointIndex
        else:
            self._dataset.ReferencedControlPointIndex = value
