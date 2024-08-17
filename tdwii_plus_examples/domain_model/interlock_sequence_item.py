from typing import Any, List, Optional  # noqa

import pydicom

from .code_sequence_item import CodeSequenceItem
from .interlock_originating_device_sequence_item import (
    InterlockOriginatingDeviceSequenceItem,
)
from .interlock_resolution_user_sequence_item import InterlockResolutionUserSequenceItem


class InterlockSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._InterlockOriginatingDeviceSequence: List[InterlockOriginatingDeviceSequenceItem] = []
        self._InterlockCodeSequence: List[CodeSequenceItem] = []
        self._InterlockResolutionCodeSequence: List[CodeSequenceItem] = []
        self._InterlockResolutionUserSequence: List[InterlockResolutionUserSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def InterlockDateTime(self) -> Optional[str]:
        if "InterlockDateTime" in self._dataset:
            return self._dataset.InterlockDateTime
        return None

    @InterlockDateTime.setter
    def InterlockDateTime(self, value: Optional[str]):
        if value is None:
            if "InterlockDateTime" in self._dataset:
                del self._dataset.InterlockDateTime
        else:
            self._dataset.InterlockDateTime = value

    @property
    def InterlockDescription(self) -> Optional[str]:
        if "InterlockDescription" in self._dataset:
            return self._dataset.InterlockDescription
        return None

    @InterlockDescription.setter
    def InterlockDescription(self, value: Optional[str]):
        if value is None:
            if "InterlockDescription" in self._dataset:
                del self._dataset.InterlockDescription
        else:
            self._dataset.InterlockDescription = value

    @property
    def InterlockOriginatingDeviceSequence(self) -> Optional[List[InterlockOriginatingDeviceSequenceItem]]:
        if "InterlockOriginatingDeviceSequence" in self._dataset:
            if len(self._InterlockOriginatingDeviceSequence) == len(self._dataset.InterlockOriginatingDeviceSequence):
                return self._InterlockOriginatingDeviceSequence
            else:
                return [InterlockOriginatingDeviceSequenceItem(x) for x in self._dataset.InterlockOriginatingDeviceSequence]
        return None

    @InterlockOriginatingDeviceSequence.setter
    def InterlockOriginatingDeviceSequence(self, value: Optional[List[InterlockOriginatingDeviceSequenceItem]]):
        if value is None:
            self._InterlockOriginatingDeviceSequence = []
            if "InterlockOriginatingDeviceSequence" in self._dataset:
                del self._dataset.InterlockOriginatingDeviceSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, InterlockOriginatingDeviceSequenceItem) for item in value
        ):
            raise ValueError(
                "InterlockOriginatingDeviceSequence must be a list of InterlockOriginatingDeviceSequenceItem objects"
            )
        else:
            self._InterlockOriginatingDeviceSequence = value
            if "InterlockOriginatingDeviceSequence" not in self._dataset:
                self._dataset.InterlockOriginatingDeviceSequence = pydicom.Sequence()
            self._dataset.InterlockOriginatingDeviceSequence.clear()
            self._dataset.InterlockOriginatingDeviceSequence.extend([item.to_dataset() for item in value])

    def add_InterlockOriginatingDevice(self, item: InterlockOriginatingDeviceSequenceItem):
        if not isinstance(item, InterlockOriginatingDeviceSequenceItem):
            raise ValueError("Item must be an instance of InterlockOriginatingDeviceSequenceItem")
        self._InterlockOriginatingDeviceSequence.append(item)
        if "InterlockOriginatingDeviceSequence" not in self._dataset:
            self._dataset.InterlockOriginatingDeviceSequence = pydicom.Sequence()
        self._dataset.InterlockOriginatingDeviceSequence.append(item.to_dataset())

    @property
    def InterlockCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "InterlockCodeSequence" in self._dataset:
            if len(self._InterlockCodeSequence) == len(self._dataset.InterlockCodeSequence):
                return self._InterlockCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.InterlockCodeSequence]
        return None

    @InterlockCodeSequence.setter
    def InterlockCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._InterlockCodeSequence = []
            if "InterlockCodeSequence" in self._dataset:
                del self._dataset.InterlockCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("InterlockCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._InterlockCodeSequence = value
            if "InterlockCodeSequence" not in self._dataset:
                self._dataset.InterlockCodeSequence = pydicom.Sequence()
            self._dataset.InterlockCodeSequence.clear()
            self._dataset.InterlockCodeSequence.extend([item.to_dataset() for item in value])

    def add_InterlockCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._InterlockCodeSequence.append(item)
        if "InterlockCodeSequence" not in self._dataset:
            self._dataset.InterlockCodeSequence = pydicom.Sequence()
        self._dataset.InterlockCodeSequence.append(item.to_dataset())

    @property
    def InterlockResolutionCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "InterlockResolutionCodeSequence" in self._dataset:
            if len(self._InterlockResolutionCodeSequence) == len(self._dataset.InterlockResolutionCodeSequence):
                return self._InterlockResolutionCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.InterlockResolutionCodeSequence]
        return None

    @InterlockResolutionCodeSequence.setter
    def InterlockResolutionCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._InterlockResolutionCodeSequence = []
            if "InterlockResolutionCodeSequence" in self._dataset:
                del self._dataset.InterlockResolutionCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("InterlockResolutionCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._InterlockResolutionCodeSequence = value
            if "InterlockResolutionCodeSequence" not in self._dataset:
                self._dataset.InterlockResolutionCodeSequence = pydicom.Sequence()
            self._dataset.InterlockResolutionCodeSequence.clear()
            self._dataset.InterlockResolutionCodeSequence.extend([item.to_dataset() for item in value])

    def add_InterlockResolutionCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._InterlockResolutionCodeSequence.append(item)
        if "InterlockResolutionCodeSequence" not in self._dataset:
            self._dataset.InterlockResolutionCodeSequence = pydicom.Sequence()
        self._dataset.InterlockResolutionCodeSequence.append(item.to_dataset())

    @property
    def InterlockResolutionUserSequence(self) -> Optional[List[InterlockResolutionUserSequenceItem]]:
        if "InterlockResolutionUserSequence" in self._dataset:
            if len(self._InterlockResolutionUserSequence) == len(self._dataset.InterlockResolutionUserSequence):
                return self._InterlockResolutionUserSequence
            else:
                return [InterlockResolutionUserSequenceItem(x) for x in self._dataset.InterlockResolutionUserSequence]
        return None

    @InterlockResolutionUserSequence.setter
    def InterlockResolutionUserSequence(self, value: Optional[List[InterlockResolutionUserSequenceItem]]):
        if value is None:
            self._InterlockResolutionUserSequence = []
            if "InterlockResolutionUserSequence" in self._dataset:
                del self._dataset.InterlockResolutionUserSequence
        elif not isinstance(value, list) or not all(isinstance(item, InterlockResolutionUserSequenceItem) for item in value):
            raise ValueError("InterlockResolutionUserSequence must be a list of InterlockResolutionUserSequenceItem objects")
        else:
            self._InterlockResolutionUserSequence = value
            if "InterlockResolutionUserSequence" not in self._dataset:
                self._dataset.InterlockResolutionUserSequence = pydicom.Sequence()
            self._dataset.InterlockResolutionUserSequence.clear()
            self._dataset.InterlockResolutionUserSequence.extend([item.to_dataset() for item in value])

    def add_InterlockResolutionUser(self, item: InterlockResolutionUserSequenceItem):
        if not isinstance(item, InterlockResolutionUserSequenceItem):
            raise ValueError("Item must be an instance of InterlockResolutionUserSequenceItem")
        self._InterlockResolutionUserSequence.append(item)
        if "InterlockResolutionUserSequence" not in self._dataset:
            self._dataset.InterlockResolutionUserSequence = pydicom.Sequence()
        self._dataset.InterlockResolutionUserSequence.append(item.to_dataset())

    @property
    def InterlockOriginDescription(self) -> Optional[str]:
        if "InterlockOriginDescription" in self._dataset:
            return self._dataset.InterlockOriginDescription
        return None

    @InterlockOriginDescription.setter
    def InterlockOriginDescription(self, value: Optional[str]):
        if value is None:
            if "InterlockOriginDescription" in self._dataset:
                del self._dataset.InterlockOriginDescription
        else:
            self._dataset.InterlockOriginDescription = value
