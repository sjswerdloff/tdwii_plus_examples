from typing import Any, List, Optional

import pydicom

from .rt_beam_limiting_device_opening_sequence_item import (
    RTBeamLimitingDeviceOpeningSequenceItem,
)


class ImagingApertureSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._RTBeamLimitingDeviceOpeningSequence: List[RTBeamLimitingDeviceOpeningSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def RTBeamLimitingDeviceOpeningSequence(self) -> Optional[List[RTBeamLimitingDeviceOpeningSequenceItem]]:
        if "RTBeamLimitingDeviceOpeningSequence" in self._dataset:
            if len(self._RTBeamLimitingDeviceOpeningSequence) == len(self._dataset.RTBeamLimitingDeviceOpeningSequence):
                return self._RTBeamLimitingDeviceOpeningSequence
            else:
                return [RTBeamLimitingDeviceOpeningSequenceItem(x) for x in self._dataset.RTBeamLimitingDeviceOpeningSequence]
        return None

    @RTBeamLimitingDeviceOpeningSequence.setter
    def RTBeamLimitingDeviceOpeningSequence(self, value: Optional[List[RTBeamLimitingDeviceOpeningSequenceItem]]):
        if value is None:
            self._RTBeamLimitingDeviceOpeningSequence = []
            if "RTBeamLimitingDeviceOpeningSequence" in self._dataset:
                del self._dataset.RTBeamLimitingDeviceOpeningSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, RTBeamLimitingDeviceOpeningSequenceItem) for item in value
        ):
            raise ValueError(
                f"RTBeamLimitingDeviceOpeningSequence must be a list of RTBeamLimitingDeviceOpeningSequenceItem objects"
            )
        else:
            self._RTBeamLimitingDeviceOpeningSequence = value
            if "RTBeamLimitingDeviceOpeningSequence" not in self._dataset:
                self._dataset.RTBeamLimitingDeviceOpeningSequence = pydicom.Sequence()
            self._dataset.RTBeamLimitingDeviceOpeningSequence.clear()
            self._dataset.RTBeamLimitingDeviceOpeningSequence.extend([item.to_dataset() for item in value])

    def add_RTBeamLimitingDeviceOpening(self, item: RTBeamLimitingDeviceOpeningSequenceItem):
        if not isinstance(item, RTBeamLimitingDeviceOpeningSequenceItem):
            raise ValueError(f"Item must be an instance of RTBeamLimitingDeviceOpeningSequenceItem")
        self._RTBeamLimitingDeviceOpeningSequence.append(item)
        if "RTBeamLimitingDeviceOpeningSequence" not in self._dataset:
            self._dataset.RTBeamLimitingDeviceOpeningSequence = pydicom.Sequence()
        self._dataset.RTBeamLimitingDeviceOpeningSequence.append(item.to_dataset())
