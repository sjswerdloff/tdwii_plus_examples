from typing import Any, List, Optional  # noqa

import pydicom

from .code_sequence_item import CodeSequenceItem
from .deformable_registration_grid_sequence_item import (
    DeformableRegistrationGridSequenceItem,
)
from .post_deformation_matrix_registration_sequence_item import (
    PostDeformationMatrixRegistrationSequenceItem,
)
from .pre_deformation_matrix_registration_sequence_item import (
    PreDeformationMatrixRegistrationSequenceItem,
)
from .referenced_image_sequence_item import ReferencedImageSequenceItem
from .used_fiducials_sequence_item import UsedFiducialsSequenceItem


class DeformableRegistrationSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._ReferencedImageSequence: List[ReferencedImageSequenceItem] = []
        self._DeformableRegistrationGridSequence: List[DeformableRegistrationGridSequenceItem] = []
        self._PreDeformationMatrixRegistrationSequence: List[PreDeformationMatrixRegistrationSequenceItem] = []
        self._PostDeformationMatrixRegistrationSequence: List[PostDeformationMatrixRegistrationSequenceItem] = []
        self._RegistrationTypeCodeSequence: List[CodeSequenceItem] = []
        self._UsedFiducialsSequence: List[UsedFiducialsSequenceItem] = []

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
    def SourceFrameOfReferenceUID(self) -> Optional[str]:
        if "SourceFrameOfReferenceUID" in self._dataset:
            return self._dataset.SourceFrameOfReferenceUID
        return None

    @SourceFrameOfReferenceUID.setter
    def SourceFrameOfReferenceUID(self, value: Optional[str]):
        if value is None:
            if "SourceFrameOfReferenceUID" in self._dataset:
                del self._dataset.SourceFrameOfReferenceUID
        else:
            self._dataset.SourceFrameOfReferenceUID = value

    @property
    def DeformableRegistrationGridSequence(self) -> Optional[List[DeformableRegistrationGridSequenceItem]]:
        if "DeformableRegistrationGridSequence" in self._dataset:
            if len(self._DeformableRegistrationGridSequence) == len(self._dataset.DeformableRegistrationGridSequence):
                return self._DeformableRegistrationGridSequence
            else:
                return [DeformableRegistrationGridSequenceItem(x) for x in self._dataset.DeformableRegistrationGridSequence]
        return None

    @DeformableRegistrationGridSequence.setter
    def DeformableRegistrationGridSequence(self, value: Optional[List[DeformableRegistrationGridSequenceItem]]):
        if value is None:
            self._DeformableRegistrationGridSequence = []
            if "DeformableRegistrationGridSequence" in self._dataset:
                del self._dataset.DeformableRegistrationGridSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, DeformableRegistrationGridSequenceItem) for item in value
        ):
            raise ValueError(
                "DeformableRegistrationGridSequence must be a list of DeformableRegistrationGridSequenceItem objects"
            )
        else:
            self._DeformableRegistrationGridSequence = value
            if "DeformableRegistrationGridSequence" not in self._dataset:
                self._dataset.DeformableRegistrationGridSequence = pydicom.Sequence()
            self._dataset.DeformableRegistrationGridSequence.clear()
            self._dataset.DeformableRegistrationGridSequence.extend([item.to_dataset() for item in value])

    def add_DeformableRegistrationGrid(self, item: DeformableRegistrationGridSequenceItem):
        if not isinstance(item, DeformableRegistrationGridSequenceItem):
            raise ValueError("Item must be an instance of DeformableRegistrationGridSequenceItem")
        self._DeformableRegistrationGridSequence.append(item)
        if "DeformableRegistrationGridSequence" not in self._dataset:
            self._dataset.DeformableRegistrationGridSequence = pydicom.Sequence()
        self._dataset.DeformableRegistrationGridSequence.append(item.to_dataset())

    @property
    def PreDeformationMatrixRegistrationSequence(self) -> Optional[List[PreDeformationMatrixRegistrationSequenceItem]]:
        if "PreDeformationMatrixRegistrationSequence" in self._dataset:
            if len(self._PreDeformationMatrixRegistrationSequence) == len(
                self._dataset.PreDeformationMatrixRegistrationSequence
            ):
                return self._PreDeformationMatrixRegistrationSequence
            else:
                return [
                    PreDeformationMatrixRegistrationSequenceItem(x)
                    for x in self._dataset.PreDeformationMatrixRegistrationSequence
                ]
        return None

    @PreDeformationMatrixRegistrationSequence.setter
    def PreDeformationMatrixRegistrationSequence(self, value: Optional[List[PreDeformationMatrixRegistrationSequenceItem]]):
        if value is None:
            self._PreDeformationMatrixRegistrationSequence = []
            if "PreDeformationMatrixRegistrationSequence" in self._dataset:
                del self._dataset.PreDeformationMatrixRegistrationSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, PreDeformationMatrixRegistrationSequenceItem) for item in value
        ):
            raise ValueError(
                "PreDeformationMatrixRegistrationSequence must be a list of PreDeformationMatrixRegistrationSequenceItem"
                " objects"
            )
        else:
            self._PreDeformationMatrixRegistrationSequence = value
            if "PreDeformationMatrixRegistrationSequence" not in self._dataset:
                self._dataset.PreDeformationMatrixRegistrationSequence = pydicom.Sequence()
            self._dataset.PreDeformationMatrixRegistrationSequence.clear()
            self._dataset.PreDeformationMatrixRegistrationSequence.extend([item.to_dataset() for item in value])

    def add_PreDeformationMatrixRegistration(self, item: PreDeformationMatrixRegistrationSequenceItem):
        if not isinstance(item, PreDeformationMatrixRegistrationSequenceItem):
            raise ValueError("Item must be an instance of PreDeformationMatrixRegistrationSequenceItem")
        self._PreDeformationMatrixRegistrationSequence.append(item)
        if "PreDeformationMatrixRegistrationSequence" not in self._dataset:
            self._dataset.PreDeformationMatrixRegistrationSequence = pydicom.Sequence()
        self._dataset.PreDeformationMatrixRegistrationSequence.append(item.to_dataset())

    @property
    def PostDeformationMatrixRegistrationSequence(self) -> Optional[List[PostDeformationMatrixRegistrationSequenceItem]]:
        if "PostDeformationMatrixRegistrationSequence" in self._dataset:
            if len(self._PostDeformationMatrixRegistrationSequence) == len(
                self._dataset.PostDeformationMatrixRegistrationSequence
            ):
                return self._PostDeformationMatrixRegistrationSequence
            else:
                return [
                    PostDeformationMatrixRegistrationSequenceItem(x)
                    for x in self._dataset.PostDeformationMatrixRegistrationSequence
                ]
        return None

    @PostDeformationMatrixRegistrationSequence.setter
    def PostDeformationMatrixRegistrationSequence(self, value: Optional[List[PostDeformationMatrixRegistrationSequenceItem]]):
        if value is None:
            self._PostDeformationMatrixRegistrationSequence = []
            if "PostDeformationMatrixRegistrationSequence" in self._dataset:
                del self._dataset.PostDeformationMatrixRegistrationSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, PostDeformationMatrixRegistrationSequenceItem) for item in value
        ):
            raise ValueError(
                "PostDeformationMatrixRegistrationSequence must be a list of PostDeformationMatrixRegistrationSequenceItem"
                " objects"
            )
        else:
            self._PostDeformationMatrixRegistrationSequence = value
            if "PostDeformationMatrixRegistrationSequence" not in self._dataset:
                self._dataset.PostDeformationMatrixRegistrationSequence = pydicom.Sequence()
            self._dataset.PostDeformationMatrixRegistrationSequence.clear()
            self._dataset.PostDeformationMatrixRegistrationSequence.extend([item.to_dataset() for item in value])

    def add_PostDeformationMatrixRegistration(self, item: PostDeformationMatrixRegistrationSequenceItem):
        if not isinstance(item, PostDeformationMatrixRegistrationSequenceItem):
            raise ValueError("Item must be an instance of PostDeformationMatrixRegistrationSequenceItem")
        self._PostDeformationMatrixRegistrationSequence.append(item)
        if "PostDeformationMatrixRegistrationSequence" not in self._dataset:
            self._dataset.PostDeformationMatrixRegistrationSequence = pydicom.Sequence()
        self._dataset.PostDeformationMatrixRegistrationSequence.append(item.to_dataset())

    @property
    def RegistrationTypeCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "RegistrationTypeCodeSequence" in self._dataset:
            if len(self._RegistrationTypeCodeSequence) == len(self._dataset.RegistrationTypeCodeSequence):
                return self._RegistrationTypeCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.RegistrationTypeCodeSequence]
        return None

    @RegistrationTypeCodeSequence.setter
    def RegistrationTypeCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._RegistrationTypeCodeSequence = []
            if "RegistrationTypeCodeSequence" in self._dataset:
                del self._dataset.RegistrationTypeCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("RegistrationTypeCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._RegistrationTypeCodeSequence = value
            if "RegistrationTypeCodeSequence" not in self._dataset:
                self._dataset.RegistrationTypeCodeSequence = pydicom.Sequence()
            self._dataset.RegistrationTypeCodeSequence.clear()
            self._dataset.RegistrationTypeCodeSequence.extend([item.to_dataset() for item in value])

    def add_RegistrationTypeCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._RegistrationTypeCodeSequence.append(item)
        if "RegistrationTypeCodeSequence" not in self._dataset:
            self._dataset.RegistrationTypeCodeSequence = pydicom.Sequence()
        self._dataset.RegistrationTypeCodeSequence.append(item.to_dataset())

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
    def FrameOfReferenceTransformationComment(self) -> Optional[str]:
        if "FrameOfReferenceTransformationComment" in self._dataset:
            return self._dataset.FrameOfReferenceTransformationComment
        return None

    @FrameOfReferenceTransformationComment.setter
    def FrameOfReferenceTransformationComment(self, value: Optional[str]):
        if value is None:
            if "FrameOfReferenceTransformationComment" in self._dataset:
                del self._dataset.FrameOfReferenceTransformationComment
        else:
            self._dataset.FrameOfReferenceTransformationComment = value
