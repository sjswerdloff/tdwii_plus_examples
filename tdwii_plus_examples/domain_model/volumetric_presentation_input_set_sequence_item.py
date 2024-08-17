from typing import Any, List, Optional  # noqa

import pydicom

from .referenced_image_sequence_item import ReferencedImageSequenceItem
from .referenced_spatial_registration_sequence_item import (
    ReferencedSpatialRegistrationSequenceItem,
)


class VolumetricPresentationInputSetSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._ReferencedImageSequence: List[ReferencedImageSequenceItem] = []
        self._ReferencedSpatialRegistrationSequence: List[ReferencedSpatialRegistrationSequenceItem] = []

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
    def ReferencedSpatialRegistrationSequence(self) -> Optional[List[ReferencedSpatialRegistrationSequenceItem]]:
        if "ReferencedSpatialRegistrationSequence" in self._dataset:
            if len(self._ReferencedSpatialRegistrationSequence) == len(self._dataset.ReferencedSpatialRegistrationSequence):
                return self._ReferencedSpatialRegistrationSequence
            else:
                return [
                    ReferencedSpatialRegistrationSequenceItem(x) for x in self._dataset.ReferencedSpatialRegistrationSequence
                ]
        return None

    @ReferencedSpatialRegistrationSequence.setter
    def ReferencedSpatialRegistrationSequence(self, value: Optional[List[ReferencedSpatialRegistrationSequenceItem]]):
        if value is None:
            self._ReferencedSpatialRegistrationSequence = []
            if "ReferencedSpatialRegistrationSequence" in self._dataset:
                del self._dataset.ReferencedSpatialRegistrationSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, ReferencedSpatialRegistrationSequenceItem) for item in value
        ):
            raise ValueError(
                "ReferencedSpatialRegistrationSequence must be a list of ReferencedSpatialRegistrationSequenceItem objects"
            )
        else:
            self._ReferencedSpatialRegistrationSequence = value
            if "ReferencedSpatialRegistrationSequence" not in self._dataset:
                self._dataset.ReferencedSpatialRegistrationSequence = pydicom.Sequence()
            self._dataset.ReferencedSpatialRegistrationSequence.clear()
            self._dataset.ReferencedSpatialRegistrationSequence.extend([item.to_dataset() for item in value])

    def add_ReferencedSpatialRegistration(self, item: ReferencedSpatialRegistrationSequenceItem):
        if not isinstance(item, ReferencedSpatialRegistrationSequenceItem):
            raise ValueError("Item must be an instance of ReferencedSpatialRegistrationSequenceItem")
        self._ReferencedSpatialRegistrationSequence.append(item)
        if "ReferencedSpatialRegistrationSequence" not in self._dataset:
            self._dataset.ReferencedSpatialRegistrationSequence = pydicom.Sequence()
        self._dataset.ReferencedSpatialRegistrationSequence.append(item.to_dataset())

    @property
    def PresentationInputType(self) -> Optional[str]:
        if "PresentationInputType" in self._dataset:
            return self._dataset.PresentationInputType
        return None

    @PresentationInputType.setter
    def PresentationInputType(self, value: Optional[str]):
        if value is None:
            if "PresentationInputType" in self._dataset:
                del self._dataset.PresentationInputType
        else:
            self._dataset.PresentationInputType = value

    @property
    def VolumetricPresentationInputSetUID(self) -> Optional[str]:
        if "VolumetricPresentationInputSetUID" in self._dataset:
            return self._dataset.VolumetricPresentationInputSetUID
        return None

    @VolumetricPresentationInputSetUID.setter
    def VolumetricPresentationInputSetUID(self, value: Optional[str]):
        if value is None:
            if "VolumetricPresentationInputSetUID" in self._dataset:
                del self._dataset.VolumetricPresentationInputSetUID
        else:
            self._dataset.VolumetricPresentationInputSetUID = value
