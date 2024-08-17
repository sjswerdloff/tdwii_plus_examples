from typing import Any, List, Optional  # noqa

import pydicom

from .brachy_pulse_control_point_delivered_sequence_item import (
    BrachyPulseControlPointDeliveredSequenceItem,
)


class PulseSpecificBrachyControlPointDeliveredSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._BrachyPulseControlPointDeliveredSequence: List[BrachyPulseControlPointDeliveredSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def SafePositionExitDate(self) -> Optional[str]:
        if "SafePositionExitDate" in self._dataset:
            return self._dataset.SafePositionExitDate
        return None

    @SafePositionExitDate.setter
    def SafePositionExitDate(self, value: Optional[str]):
        if value is None:
            if "SafePositionExitDate" in self._dataset:
                del self._dataset.SafePositionExitDate
        else:
            self._dataset.SafePositionExitDate = value

    @property
    def SafePositionExitTime(self) -> Optional[str]:
        if "SafePositionExitTime" in self._dataset:
            return self._dataset.SafePositionExitTime
        return None

    @SafePositionExitTime.setter
    def SafePositionExitTime(self, value: Optional[str]):
        if value is None:
            if "SafePositionExitTime" in self._dataset:
                del self._dataset.SafePositionExitTime
        else:
            self._dataset.SafePositionExitTime = value

    @property
    def SafePositionReturnDate(self) -> Optional[str]:
        if "SafePositionReturnDate" in self._dataset:
            return self._dataset.SafePositionReturnDate
        return None

    @SafePositionReturnDate.setter
    def SafePositionReturnDate(self, value: Optional[str]):
        if value is None:
            if "SafePositionReturnDate" in self._dataset:
                del self._dataset.SafePositionReturnDate
        else:
            self._dataset.SafePositionReturnDate = value

    @property
    def SafePositionReturnTime(self) -> Optional[str]:
        if "SafePositionReturnTime" in self._dataset:
            return self._dataset.SafePositionReturnTime
        return None

    @SafePositionReturnTime.setter
    def SafePositionReturnTime(self, value: Optional[str]):
        if value is None:
            if "SafePositionReturnTime" in self._dataset:
                del self._dataset.SafePositionReturnTime
        else:
            self._dataset.SafePositionReturnTime = value

    @property
    def PulseNumber(self) -> Optional[int]:
        if "PulseNumber" in self._dataset:
            return self._dataset.PulseNumber
        return None

    @PulseNumber.setter
    def PulseNumber(self, value: Optional[int]):
        if value is None:
            if "PulseNumber" in self._dataset:
                del self._dataset.PulseNumber
        else:
            self._dataset.PulseNumber = value

    @property
    def BrachyPulseControlPointDeliveredSequence(self) -> Optional[List[BrachyPulseControlPointDeliveredSequenceItem]]:
        if "BrachyPulseControlPointDeliveredSequence" in self._dataset:
            if len(self._BrachyPulseControlPointDeliveredSequence) == len(
                self._dataset.BrachyPulseControlPointDeliveredSequence
            ):
                return self._BrachyPulseControlPointDeliveredSequence
            else:
                return [
                    BrachyPulseControlPointDeliveredSequenceItem(x)
                    for x in self._dataset.BrachyPulseControlPointDeliveredSequence
                ]
        return None

    @BrachyPulseControlPointDeliveredSequence.setter
    def BrachyPulseControlPointDeliveredSequence(self, value: Optional[List[BrachyPulseControlPointDeliveredSequenceItem]]):
        if value is None:
            self._BrachyPulseControlPointDeliveredSequence = []
            if "BrachyPulseControlPointDeliveredSequence" in self._dataset:
                del self._dataset.BrachyPulseControlPointDeliveredSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, BrachyPulseControlPointDeliveredSequenceItem) for item in value
        ):
            raise ValueError(
                "BrachyPulseControlPointDeliveredSequence must be a list of BrachyPulseControlPointDeliveredSequenceItem"
                " objects"
            )
        else:
            self._BrachyPulseControlPointDeliveredSequence = value
            if "BrachyPulseControlPointDeliveredSequence" not in self._dataset:
                self._dataset.BrachyPulseControlPointDeliveredSequence = pydicom.Sequence()
            self._dataset.BrachyPulseControlPointDeliveredSequence.clear()
            self._dataset.BrachyPulseControlPointDeliveredSequence.extend([item.to_dataset() for item in value])

    def add_BrachyPulseControlPointDelivered(self, item: BrachyPulseControlPointDeliveredSequenceItem):
        if not isinstance(item, BrachyPulseControlPointDeliveredSequenceItem):
            raise ValueError("Item must be an instance of BrachyPulseControlPointDeliveredSequenceItem")
        self._BrachyPulseControlPointDeliveredSequence.append(item)
        if "BrachyPulseControlPointDeliveredSequence" not in self._dataset:
            self._dataset.BrachyPulseControlPointDeliveredSequence = pydicom.Sequence()
        self._dataset.BrachyPulseControlPointDeliveredSequence.append(item.to_dataset())
