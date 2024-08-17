from typing import Any, List, Optional  # noqa

import pydicom

from .fiducial_sequence_item import FiducialSequenceItem
from .referenced_image_sequence_item import ReferencedImageSequenceItem


class FiducialSetSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._ReferencedImageSequence: List[ReferencedImageSequenceItem] = []
        self._FiducialSequence: List[FiducialSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ReferencedImageSequence(self) -> Optional[List[ReferencedImageSequenceItem]]:
        if "ReferencedImageSequence" in self._dataset:
            if len(self._ReferencedImageSequence) == len(self._dataset.ReferencedImageSequence):
                return self._ReferencedImageSequence
            else:
                return [ReferencedImageSequenceItem(x) for x in self._dataset.ReferencedImageSequence]
        return None

    @ReferencedImageSequence.setter
    def ReferencedImageSequence(self, value: Optional[List[ReferencedImageSequenceItem]]):
        if value is None:
            self._ReferencedImageSequence = []
            if "ReferencedImageSequence" in self._dataset:
                del self._dataset.ReferencedImageSequence
        elif not isinstance(value, list) or not all(isinstance(item, ReferencedImageSequenceItem) for item in value):
            raise ValueError("ReferencedImageSequence must be a list of ReferencedImageSequenceItem objects")
        else:
            self._ReferencedImageSequence = value
            if "ReferencedImageSequence" not in self._dataset:
                self._dataset.ReferencedImageSequence = pydicom.Sequence()
            self._dataset.ReferencedImageSequence.clear()
            self._dataset.ReferencedImageSequence.extend([item.to_dataset() for item in value])

    def add_ReferencedImage(self, item: ReferencedImageSequenceItem):
        if not isinstance(item, ReferencedImageSequenceItem):
            raise ValueError("Item must be an instance of ReferencedImageSequenceItem")
        self._ReferencedImageSequence.append(item)
        if "ReferencedImageSequence" not in self._dataset:
            self._dataset.ReferencedImageSequence = pydicom.Sequence()
        self._dataset.ReferencedImageSequence.append(item.to_dataset())

    @property
    def FrameOfReferenceUID(self) -> Optional[str]:
        if "FrameOfReferenceUID" in self._dataset:
            return self._dataset.FrameOfReferenceUID
        return None

    @FrameOfReferenceUID.setter
    def FrameOfReferenceUID(self, value: Optional[str]):
        if value is None:
            if "FrameOfReferenceUID" in self._dataset:
                del self._dataset.FrameOfReferenceUID
        else:
            self._dataset.FrameOfReferenceUID = value

    @property
    def FiducialSequence(self) -> Optional[List[FiducialSequenceItem]]:
        if "FiducialSequence" in self._dataset:
            if len(self._FiducialSequence) == len(self._dataset.FiducialSequence):
                return self._FiducialSequence
            else:
                return [FiducialSequenceItem(x) for x in self._dataset.FiducialSequence]
        return None

    @FiducialSequence.setter
    def FiducialSequence(self, value: Optional[List[FiducialSequenceItem]]):
        if value is None:
            self._FiducialSequence = []
            if "FiducialSequence" in self._dataset:
                del self._dataset.FiducialSequence
        elif not isinstance(value, list) or not all(isinstance(item, FiducialSequenceItem) for item in value):
            raise ValueError("FiducialSequence must be a list of FiducialSequenceItem objects")
        else:
            self._FiducialSequence = value
            if "FiducialSequence" not in self._dataset:
                self._dataset.FiducialSequence = pydicom.Sequence()
            self._dataset.FiducialSequence.clear()
            self._dataset.FiducialSequence.extend([item.to_dataset() for item in value])

    def add_Fiducial(self, item: FiducialSequenceItem):
        if not isinstance(item, FiducialSequenceItem):
            raise ValueError("Item must be an instance of FiducialSequenceItem")
        self._FiducialSequence.append(item)
        if "FiducialSequence" not in self._dataset:
            self._dataset.FiducialSequence = pydicom.Sequence()
        self._dataset.FiducialSequence.append(item.to_dataset())
