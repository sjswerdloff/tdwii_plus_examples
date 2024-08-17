from typing import Any, List, Optional  # noqa

import pydicom

from .referenced_presentation_state_sequence_item import (
    ReferencedPresentationStateSequenceItem,
)


class ReferencedImageSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._ReferencedPresentationStateSequence: List[ReferencedPresentationStateSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ReferencedSOPClassUID(self) -> Optional[str]:
        if "ReferencedSOPClassUID" in self._dataset:
            return self._dataset.ReferencedSOPClassUID
        return None

    @ReferencedSOPClassUID.setter
    def ReferencedSOPClassUID(self, value: Optional[str]):
        if value is None:
            if "ReferencedSOPClassUID" in self._dataset:
                del self._dataset.ReferencedSOPClassUID
        else:
            self._dataset.ReferencedSOPClassUID = value

    @property
    def ReferencedSOPInstanceUID(self) -> Optional[str]:
        if "ReferencedSOPInstanceUID" in self._dataset:
            return self._dataset.ReferencedSOPInstanceUID
        return None

    @ReferencedSOPInstanceUID.setter
    def ReferencedSOPInstanceUID(self, value: Optional[str]):
        if value is None:
            if "ReferencedSOPInstanceUID" in self._dataset:
                del self._dataset.ReferencedSOPInstanceUID
        else:
            self._dataset.ReferencedSOPInstanceUID = value

    @property
    def ReferencedFrameNumber(self) -> Optional[List[int]]:
        if "ReferencedFrameNumber" in self._dataset:
            return self._dataset.ReferencedFrameNumber
        return None

    @ReferencedFrameNumber.setter
    def ReferencedFrameNumber(self, value: Optional[List[int]]):
        if value is None:
            if "ReferencedFrameNumber" in self._dataset:
                del self._dataset.ReferencedFrameNumber
        else:
            self._dataset.ReferencedFrameNumber = value

    @property
    def ReferencedPresentationStateSequence(self) -> Optional[List[ReferencedPresentationStateSequenceItem]]:
        if "ReferencedPresentationStateSequence" in self._dataset:
            if len(self._ReferencedPresentationStateSequence) == len(self._dataset.ReferencedPresentationStateSequence):
                return self._ReferencedPresentationStateSequence
            else:
                return [ReferencedPresentationStateSequenceItem(x) for x in self._dataset.ReferencedPresentationStateSequence]
        return None

    @ReferencedPresentationStateSequence.setter
    def ReferencedPresentationStateSequence(self, value: Optional[List[ReferencedPresentationStateSequenceItem]]):
        if value is None:
            self._ReferencedPresentationStateSequence = []
            if "ReferencedPresentationStateSequence" in self._dataset:
                del self._dataset.ReferencedPresentationStateSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, ReferencedPresentationStateSequenceItem) for item in value
        ):
            raise ValueError(
                "ReferencedPresentationStateSequence must be a list of ReferencedPresentationStateSequenceItem objects"
            )
        else:
            self._ReferencedPresentationStateSequence = value
            if "ReferencedPresentationStateSequence" not in self._dataset:
                self._dataset.ReferencedPresentationStateSequence = pydicom.Sequence()
            self._dataset.ReferencedPresentationStateSequence.clear()
            self._dataset.ReferencedPresentationStateSequence.extend([item.to_dataset() for item in value])

    def add_ReferencedPresentationState(self, item: ReferencedPresentationStateSequenceItem):
        if not isinstance(item, ReferencedPresentationStateSequenceItem):
            raise ValueError("Item must be an instance of ReferencedPresentationStateSequenceItem")
        self._ReferencedPresentationStateSequence.append(item)
        if "ReferencedPresentationStateSequence" not in self._dataset:
            self._dataset.ReferencedPresentationStateSequence = pydicom.Sequence()
        self._dataset.ReferencedPresentationStateSequence.append(item.to_dataset())

    @property
    def ReferencedSegmentNumber(self) -> Optional[List[int]]:
        if "ReferencedSegmentNumber" in self._dataset:
            return self._dataset.ReferencedSegmentNumber
        return None

    @ReferencedSegmentNumber.setter
    def ReferencedSegmentNumber(self, value: Optional[List[int]]):
        if value is None:
            if "ReferencedSegmentNumber" in self._dataset:
                del self._dataset.ReferencedSegmentNumber
        else:
            self._dataset.ReferencedSegmentNumber = value
