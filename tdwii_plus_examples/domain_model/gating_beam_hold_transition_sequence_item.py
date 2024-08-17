from typing import Any, List, Optional

import pydicom

from .beam_hold_originating_device_sequence_item import (
    BeamHoldOriginatingDeviceSequenceItem,
)


class GatingBeamHoldTransitionSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._BeamHoldOriginatingDeviceSequence: List[BeamHoldOriginatingDeviceSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def BeamHoldTransition(self) -> Optional[str]:
        if "BeamHoldTransition" in self._dataset:
            return self._dataset.BeamHoldTransition
        return None

    @BeamHoldTransition.setter
    def BeamHoldTransition(self, value: Optional[str]):
        if value is None:
            if "BeamHoldTransition" in self._dataset:
                del self._dataset.BeamHoldTransition
        else:
            self._dataset.BeamHoldTransition = value

    @property
    def BeamHoldTransitionDateTime(self) -> Optional[str]:
        if "BeamHoldTransitionDateTime" in self._dataset:
            return self._dataset.BeamHoldTransitionDateTime
        return None

    @BeamHoldTransitionDateTime.setter
    def BeamHoldTransitionDateTime(self, value: Optional[str]):
        if value is None:
            if "BeamHoldTransitionDateTime" in self._dataset:
                del self._dataset.BeamHoldTransitionDateTime
        else:
            self._dataset.BeamHoldTransitionDateTime = value

    @property
    def BeamHoldOriginatingDeviceSequence(self) -> Optional[List[BeamHoldOriginatingDeviceSequenceItem]]:
        if "BeamHoldOriginatingDeviceSequence" in self._dataset:
            if len(self._BeamHoldOriginatingDeviceSequence) == len(self._dataset.BeamHoldOriginatingDeviceSequence):
                return self._BeamHoldOriginatingDeviceSequence
            else:
                return [BeamHoldOriginatingDeviceSequenceItem(x) for x in self._dataset.BeamHoldOriginatingDeviceSequence]
        return None

    @BeamHoldOriginatingDeviceSequence.setter
    def BeamHoldOriginatingDeviceSequence(self, value: Optional[List[BeamHoldOriginatingDeviceSequenceItem]]):
        if value is None:
            self._BeamHoldOriginatingDeviceSequence = []
            if "BeamHoldOriginatingDeviceSequence" in self._dataset:
                del self._dataset.BeamHoldOriginatingDeviceSequence
        elif not isinstance(value, list) or not all(isinstance(item, BeamHoldOriginatingDeviceSequenceItem) for item in value):
            raise ValueError(
                f"BeamHoldOriginatingDeviceSequence must be a list of BeamHoldOriginatingDeviceSequenceItem objects"
            )
        else:
            self._BeamHoldOriginatingDeviceSequence = value
            if "BeamHoldOriginatingDeviceSequence" not in self._dataset:
                self._dataset.BeamHoldOriginatingDeviceSequence = pydicom.Sequence()
            self._dataset.BeamHoldOriginatingDeviceSequence.clear()
            self._dataset.BeamHoldOriginatingDeviceSequence.extend([item.to_dataset() for item in value])

    def add_BeamHoldOriginatingDevice(self, item: BeamHoldOriginatingDeviceSequenceItem):
        if not isinstance(item, BeamHoldOriginatingDeviceSequenceItem):
            raise ValueError(f"Item must be an instance of BeamHoldOriginatingDeviceSequenceItem")
        self._BeamHoldOriginatingDeviceSequence.append(item)
        if "BeamHoldOriginatingDeviceSequence" not in self._dataset:
            self._dataset.BeamHoldOriginatingDeviceSequence = pydicom.Sequence()
        self._dataset.BeamHoldOriginatingDeviceSequence.append(item.to_dataset())

    @property
    def BeamHoldTransitionTriggerSource(self) -> Optional[str]:
        if "BeamHoldTransitionTriggerSource" in self._dataset:
            return self._dataset.BeamHoldTransitionTriggerSource
        return None

    @BeamHoldTransitionTriggerSource.setter
    def BeamHoldTransitionTriggerSource(self, value: Optional[str]):
        if value is None:
            if "BeamHoldTransitionTriggerSource" in self._dataset:
                del self._dataset.BeamHoldTransitionTriggerSource
        else:
            self._dataset.BeamHoldTransitionTriggerSource = value
