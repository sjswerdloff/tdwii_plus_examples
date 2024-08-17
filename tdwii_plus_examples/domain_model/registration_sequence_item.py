from typing import Any, List, Optional  # noqa

import pydicom

from .matrix_registration_sequence_item import MatrixRegistrationSequenceItem
from .referenced_image_sequence_item import ReferencedImageSequenceItem
from .used_fiducials_sequence_item import UsedFiducialsSequenceItem
from .used_rt_structure_set_roi_sequence_item import UsedRTStructureSetROISequenceItem
from .used_segments_sequence_item import UsedSegmentsSequenceItem


class RegistrationSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._ReferencedImageSequence: List[ReferencedImageSequenceItem] = []
        self._UsedSegmentsSequence: List[UsedSegmentsSequenceItem] = []
        self._MatrixRegistrationSequence: List[MatrixRegistrationSequenceItem] = []
        self._UsedFiducialsSequence: List[UsedFiducialsSequenceItem] = []
        self._UsedRTStructureSetROISequence: List[UsedRTStructureSetROISequenceItem] = []

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
    def UsedSegmentsSequence(self) -> Optional[List[UsedSegmentsSequenceItem]]:
        if "UsedSegmentsSequence" in self._dataset:
            if len(self._UsedSegmentsSequence) == len(self._dataset.UsedSegmentsSequence):
                return self._UsedSegmentsSequence
            else:
                return [UsedSegmentsSequenceItem(x) for x in self._dataset.UsedSegmentsSequence]
        return None

    @UsedSegmentsSequence.setter
    def UsedSegmentsSequence(self, value: Optional[List[UsedSegmentsSequenceItem]]):
        if value is None:
            self._UsedSegmentsSequence = []
            if "UsedSegmentsSequence" in self._dataset:
                del self._dataset.UsedSegmentsSequence
        elif not isinstance(value, list) or not all(isinstance(item, UsedSegmentsSequenceItem) for item in value):
            raise ValueError("UsedSegmentsSequence must be a list of UsedSegmentsSequenceItem objects")
        else:
            self._UsedSegmentsSequence = value
            if "UsedSegmentsSequence" not in self._dataset:
                self._dataset.UsedSegmentsSequence = pydicom.Sequence()
            self._dataset.UsedSegmentsSequence.clear()
            self._dataset.UsedSegmentsSequence.extend([item.to_dataset() for item in value])

    def add_UsedSegments(self, item: UsedSegmentsSequenceItem):
        if not isinstance(item, UsedSegmentsSequenceItem):
            raise ValueError("Item must be an instance of UsedSegmentsSequenceItem")
        self._UsedSegmentsSequence.append(item)
        if "UsedSegmentsSequence" not in self._dataset:
            self._dataset.UsedSegmentsSequence = pydicom.Sequence()
        self._dataset.UsedSegmentsSequence.append(item.to_dataset())

    @property
    def MatrixRegistrationSequence(self) -> Optional[List[MatrixRegistrationSequenceItem]]:
        if "MatrixRegistrationSequence" in self._dataset:
            if len(self._MatrixRegistrationSequence) == len(self._dataset.MatrixRegistrationSequence):
                return self._MatrixRegistrationSequence
            else:
                return [MatrixRegistrationSequenceItem(x) for x in self._dataset.MatrixRegistrationSequence]
        return None

    @MatrixRegistrationSequence.setter
    def MatrixRegistrationSequence(self, value: Optional[List[MatrixRegistrationSequenceItem]]):
        if value is None:
            self._MatrixRegistrationSequence = []
            if "MatrixRegistrationSequence" in self._dataset:
                del self._dataset.MatrixRegistrationSequence
        elif not isinstance(value, list) or not all(isinstance(item, MatrixRegistrationSequenceItem) for item in value):
            raise ValueError("MatrixRegistrationSequence must be a list of MatrixRegistrationSequenceItem objects")
        else:
            self._MatrixRegistrationSequence = value
            if "MatrixRegistrationSequence" not in self._dataset:
                self._dataset.MatrixRegistrationSequence = pydicom.Sequence()
            self._dataset.MatrixRegistrationSequence.clear()
            self._dataset.MatrixRegistrationSequence.extend([item.to_dataset() for item in value])

    def add_MatrixRegistration(self, item: MatrixRegistrationSequenceItem):
        if not isinstance(item, MatrixRegistrationSequenceItem):
            raise ValueError("Item must be an instance of MatrixRegistrationSequenceItem")
        self._MatrixRegistrationSequence.append(item)
        if "MatrixRegistrationSequence" not in self._dataset:
            self._dataset.MatrixRegistrationSequence = pydicom.Sequence()
        self._dataset.MatrixRegistrationSequence.append(item.to_dataset())

    @property
    def UsedFiducialsSequence(self) -> Optional[List[UsedFiducialsSequenceItem]]:
        if "UsedFiducialsSequence" in self._dataset:
            if len(self._UsedFiducialsSequence) == len(self._dataset.UsedFiducialsSequence):
                return self._UsedFiducialsSequence
            else:
                return [UsedFiducialsSequenceItem(x) for x in self._dataset.UsedFiducialsSequence]
        return None

    @UsedFiducialsSequence.setter
    def UsedFiducialsSequence(self, value: Optional[List[UsedFiducialsSequenceItem]]):
        if value is None:
            self._UsedFiducialsSequence = []
            if "UsedFiducialsSequence" in self._dataset:
                del self._dataset.UsedFiducialsSequence
        elif not isinstance(value, list) or not all(isinstance(item, UsedFiducialsSequenceItem) for item in value):
            raise ValueError("UsedFiducialsSequence must be a list of UsedFiducialsSequenceItem objects")
        else:
            self._UsedFiducialsSequence = value
            if "UsedFiducialsSequence" not in self._dataset:
                self._dataset.UsedFiducialsSequence = pydicom.Sequence()
            self._dataset.UsedFiducialsSequence.clear()
            self._dataset.UsedFiducialsSequence.extend([item.to_dataset() for item in value])

    def add_UsedFiducials(self, item: UsedFiducialsSequenceItem):
        if not isinstance(item, UsedFiducialsSequenceItem):
            raise ValueError("Item must be an instance of UsedFiducialsSequenceItem")
        self._UsedFiducialsSequence.append(item)
        if "UsedFiducialsSequence" not in self._dataset:
            self._dataset.UsedFiducialsSequence = pydicom.Sequence()
        self._dataset.UsedFiducialsSequence.append(item.to_dataset())

    @property
    def UsedRTStructureSetROISequence(self) -> Optional[List[UsedRTStructureSetROISequenceItem]]:
        if "UsedRTStructureSetROISequence" in self._dataset:
            if len(self._UsedRTStructureSetROISequence) == len(self._dataset.UsedRTStructureSetROISequence):
                return self._UsedRTStructureSetROISequence
            else:
                return [UsedRTStructureSetROISequenceItem(x) for x in self._dataset.UsedRTStructureSetROISequence]
        return None

    @UsedRTStructureSetROISequence.setter
    def UsedRTStructureSetROISequence(self, value: Optional[List[UsedRTStructureSetROISequenceItem]]):
        if value is None:
            self._UsedRTStructureSetROISequence = []
            if "UsedRTStructureSetROISequence" in self._dataset:
                del self._dataset.UsedRTStructureSetROISequence
        elif not isinstance(value, list) or not all(isinstance(item, UsedRTStructureSetROISequenceItem) for item in value):
            raise ValueError("UsedRTStructureSetROISequence must be a list of UsedRTStructureSetROISequenceItem objects")
        else:
            self._UsedRTStructureSetROISequence = value
            if "UsedRTStructureSetROISequence" not in self._dataset:
                self._dataset.UsedRTStructureSetROISequence = pydicom.Sequence()
            self._dataset.UsedRTStructureSetROISequence.clear()
            self._dataset.UsedRTStructureSetROISequence.extend([item.to_dataset() for item in value])

    def add_UsedRTStructureSetROI(self, item: UsedRTStructureSetROISequenceItem):
        if not isinstance(item, UsedRTStructureSetROISequenceItem):
            raise ValueError("Item must be an instance of UsedRTStructureSetROISequenceItem")
        self._UsedRTStructureSetROISequence.append(item)
        if "UsedRTStructureSetROISequence" not in self._dataset:
            self._dataset.UsedRTStructureSetROISequence = pydicom.Sequence()
        self._dataset.UsedRTStructureSetROISequence.append(item.to_dataset())
