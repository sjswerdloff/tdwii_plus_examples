from typing import Any, List, Optional  # noqa

import pydicom

from .code_sequence_item import CodeSequenceItem


class DeviceMotionControlSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._DeviceMotionParameterCodeSequence: List[CodeSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def DeviceMotionExecutionMode(self) -> Optional[str]:
        if "DeviceMotionExecutionMode" in self._dataset:
            return self._dataset.DeviceMotionExecutionMode
        return None

    @DeviceMotionExecutionMode.setter
    def DeviceMotionExecutionMode(self, value: Optional[str]):
        if value is None:
            if "DeviceMotionExecutionMode" in self._dataset:
                del self._dataset.DeviceMotionExecutionMode
        else:
            self._dataset.DeviceMotionExecutionMode = value

    @property
    def DeviceMotionObservationMode(self) -> Optional[str]:
        if "DeviceMotionObservationMode" in self._dataset:
            return self._dataset.DeviceMotionObservationMode
        return None

    @DeviceMotionObservationMode.setter
    def DeviceMotionObservationMode(self, value: Optional[str]):
        if value is None:
            if "DeviceMotionObservationMode" in self._dataset:
                del self._dataset.DeviceMotionObservationMode
        else:
            self._dataset.DeviceMotionObservationMode = value

    @property
    def DeviceMotionParameterCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "DeviceMotionParameterCodeSequence" in self._dataset:
            if len(self._DeviceMotionParameterCodeSequence) == len(self._dataset.DeviceMotionParameterCodeSequence):
                return self._DeviceMotionParameterCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.DeviceMotionParameterCodeSequence]
        return None

    @DeviceMotionParameterCodeSequence.setter
    def DeviceMotionParameterCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._DeviceMotionParameterCodeSequence = []
            if "DeviceMotionParameterCodeSequence" in self._dataset:
                del self._dataset.DeviceMotionParameterCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("DeviceMotionParameterCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._DeviceMotionParameterCodeSequence = value
            if "DeviceMotionParameterCodeSequence" not in self._dataset:
                self._dataset.DeviceMotionParameterCodeSequence = pydicom.Sequence()
            self._dataset.DeviceMotionParameterCodeSequence.clear()
            self._dataset.DeviceMotionParameterCodeSequence.extend([item.to_dataset() for item in value])

    def add_DeviceMotionParameterCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._DeviceMotionParameterCodeSequence.append(item)
        if "DeviceMotionParameterCodeSequence" not in self._dataset:
            self._dataset.DeviceMotionParameterCodeSequence = pydicom.Sequence()
        self._dataset.DeviceMotionParameterCodeSequence.append(item.to_dataset())
