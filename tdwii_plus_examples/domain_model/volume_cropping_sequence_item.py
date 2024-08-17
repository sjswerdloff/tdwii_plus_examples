from typing import Any, List, Optional  # noqa

import pydicom

from .oblique_cropping_plane_sequence_item import ObliqueCroppingPlaneSequenceItem
from .referenced_image_sequence_item import ReferencedImageSequenceItem


class VolumeCroppingSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._ReferencedImageSequence: List[ReferencedImageSequenceItem] = []
        self._ObliqueCroppingPlaneSequence: List[ObliqueCroppingPlaneSequenceItem] = []

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
    def VolumeCroppingMethod(self) -> Optional[str]:
        if "VolumeCroppingMethod" in self._dataset:
            return self._dataset.VolumeCroppingMethod
        return None

    @VolumeCroppingMethod.setter
    def VolumeCroppingMethod(self, value: Optional[str]):
        if value is None:
            if "VolumeCroppingMethod" in self._dataset:
                del self._dataset.VolumeCroppingMethod
        else:
            self._dataset.VolumeCroppingMethod = value

    @property
    def BoundingBoxCrop(self) -> Optional[List[float]]:
        if "BoundingBoxCrop" in self._dataset:
            return self._dataset.BoundingBoxCrop
        return None

    @BoundingBoxCrop.setter
    def BoundingBoxCrop(self, value: Optional[List[float]]):
        if value is None:
            if "BoundingBoxCrop" in self._dataset:
                del self._dataset.BoundingBoxCrop
        else:
            self._dataset.BoundingBoxCrop = value

    @property
    def ObliqueCroppingPlaneSequence(self) -> Optional[List[ObliqueCroppingPlaneSequenceItem]]:
        if "ObliqueCroppingPlaneSequence" in self._dataset:
            if len(self._ObliqueCroppingPlaneSequence) == len(self._dataset.ObliqueCroppingPlaneSequence):
                return self._ObliqueCroppingPlaneSequence
            else:
                return [ObliqueCroppingPlaneSequenceItem(x) for x in self._dataset.ObliqueCroppingPlaneSequence]
        return None

    @ObliqueCroppingPlaneSequence.setter
    def ObliqueCroppingPlaneSequence(self, value: Optional[List[ObliqueCroppingPlaneSequenceItem]]):
        if value is None:
            self._ObliqueCroppingPlaneSequence = []
            if "ObliqueCroppingPlaneSequence" in self._dataset:
                del self._dataset.ObliqueCroppingPlaneSequence
        elif not isinstance(value, list) or not all(isinstance(item, ObliqueCroppingPlaneSequenceItem) for item in value):
            raise ValueError("ObliqueCroppingPlaneSequence must be a list of ObliqueCroppingPlaneSequenceItem objects")
        else:
            self._ObliqueCroppingPlaneSequence = value
            if "ObliqueCroppingPlaneSequence" not in self._dataset:
                self._dataset.ObliqueCroppingPlaneSequence = pydicom.Sequence()
            self._dataset.ObliqueCroppingPlaneSequence.clear()
            self._dataset.ObliqueCroppingPlaneSequence.extend([item.to_dataset() for item in value])

    def add_ObliqueCroppingPlane(self, item: ObliqueCroppingPlaneSequenceItem):
        if not isinstance(item, ObliqueCroppingPlaneSequenceItem):
            raise ValueError("Item must be an instance of ObliqueCroppingPlaneSequenceItem")
        self._ObliqueCroppingPlaneSequence.append(item)
        if "ObliqueCroppingPlaneSequence" not in self._dataset:
            self._dataset.ObliqueCroppingPlaneSequence = pydicom.Sequence()
        self._dataset.ObliqueCroppingPlaneSequence.append(item.to_dataset())

    @property
    def CroppingSpecificationNumber(self) -> Optional[int]:
        if "CroppingSpecificationNumber" in self._dataset:
            return self._dataset.CroppingSpecificationNumber
        return None

    @CroppingSpecificationNumber.setter
    def CroppingSpecificationNumber(self, value: Optional[int]):
        if value is None:
            if "CroppingSpecificationNumber" in self._dataset:
                del self._dataset.CroppingSpecificationNumber
        else:
            self._dataset.CroppingSpecificationNumber = value
