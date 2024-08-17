from typing import Any, List, Optional

import pydicom

from .referenced_first_frame_sequence_item import ReferencedFirstFrameSequenceItem
from .referenced_image_sequence_item import ReferencedImageSequenceItem
from .referenced_instance_sequence_item import ReferencedInstanceSequenceItem
from .referenced_presentation_state_sequence_item import (
    ReferencedPresentationStateSequenceItem,
)
from .referenced_stereometric_instance_sequence_item import (
    ReferencedStereometricInstanceSequenceItem,
)


class StructuredDisplayImageBoxSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._ReferencedStereometricInstanceSequence: List[ReferencedStereometricInstanceSequenceItem] = []
        self._ReferencedImageSequence: List[ReferencedImageSequenceItem] = []
        self._ReferencedInstanceSequence: List[ReferencedInstanceSequenceItem] = []
        self._ReferencedPresentationStateSequence: List[ReferencedPresentationStateSequenceItem] = []
        self._ReferencedFirstFrameSequence: List[ReferencedFirstFrameSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ReferencedStereometricInstanceSequence(self) -> Optional[List[ReferencedStereometricInstanceSequenceItem]]:
        if "ReferencedStereometricInstanceSequence" in self._dataset:
            if len(self._ReferencedStereometricInstanceSequence) == len(self._dataset.ReferencedStereometricInstanceSequence):
                return self._ReferencedStereometricInstanceSequence
            else:
                return [
                    ReferencedStereometricInstanceSequenceItem(x) for x in self._dataset.ReferencedStereometricInstanceSequence
                ]
        return None

    @ReferencedStereometricInstanceSequence.setter
    def ReferencedStereometricInstanceSequence(self, value: Optional[List[ReferencedStereometricInstanceSequenceItem]]):
        if value is None:
            self._ReferencedStereometricInstanceSequence = []
            if "ReferencedStereometricInstanceSequence" in self._dataset:
                del self._dataset.ReferencedStereometricInstanceSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, ReferencedStereometricInstanceSequenceItem) for item in value
        ):
            raise ValueError(
                f"ReferencedStereometricInstanceSequence must be a list of ReferencedStereometricInstanceSequenceItem objects"
            )
        else:
            self._ReferencedStereometricInstanceSequence = value
            if "ReferencedStereometricInstanceSequence" not in self._dataset:
                self._dataset.ReferencedStereometricInstanceSequence = pydicom.Sequence()
            self._dataset.ReferencedStereometricInstanceSequence.clear()
            self._dataset.ReferencedStereometricInstanceSequence.extend([item.to_dataset() for item in value])

    def add_ReferencedStereometricInstance(self, item: ReferencedStereometricInstanceSequenceItem):
        if not isinstance(item, ReferencedStereometricInstanceSequenceItem):
            raise ValueError(f"Item must be an instance of ReferencedStereometricInstanceSequenceItem")
        self._ReferencedStereometricInstanceSequence.append(item)
        if "ReferencedStereometricInstanceSequence" not in self._dataset:
            self._dataset.ReferencedStereometricInstanceSequence = pydicom.Sequence()
        self._dataset.ReferencedStereometricInstanceSequence.append(item.to_dataset())

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
            raise ValueError(f"ReferencedImageSequence must be a list of ReferencedImageSequenceItem objects")
        else:
            self._ReferencedImageSequence = value
            if "ReferencedImageSequence" not in self._dataset:
                self._dataset.ReferencedImageSequence = pydicom.Sequence()
            self._dataset.ReferencedImageSequence.clear()
            self._dataset.ReferencedImageSequence.extend([item.to_dataset() for item in value])

    def add_ReferencedImage(self, item: ReferencedImageSequenceItem):
        if not isinstance(item, ReferencedImageSequenceItem):
            raise ValueError(f"Item must be an instance of ReferencedImageSequenceItem")
        self._ReferencedImageSequence.append(item)
        if "ReferencedImageSequence" not in self._dataset:
            self._dataset.ReferencedImageSequence = pydicom.Sequence()
        self._dataset.ReferencedImageSequence.append(item.to_dataset())

    @property
    def ReferencedInstanceSequence(self) -> Optional[List[ReferencedInstanceSequenceItem]]:
        if "ReferencedInstanceSequence" in self._dataset:
            if len(self._ReferencedInstanceSequence) == len(self._dataset.ReferencedInstanceSequence):
                return self._ReferencedInstanceSequence
            else:
                return [ReferencedInstanceSequenceItem(x) for x in self._dataset.ReferencedInstanceSequence]
        return None

    @ReferencedInstanceSequence.setter
    def ReferencedInstanceSequence(self, value: Optional[List[ReferencedInstanceSequenceItem]]):
        if value is None:
            self._ReferencedInstanceSequence = []
            if "ReferencedInstanceSequence" in self._dataset:
                del self._dataset.ReferencedInstanceSequence
        elif not isinstance(value, list) or not all(isinstance(item, ReferencedInstanceSequenceItem) for item in value):
            raise ValueError(f"ReferencedInstanceSequence must be a list of ReferencedInstanceSequenceItem objects")
        else:
            self._ReferencedInstanceSequence = value
            if "ReferencedInstanceSequence" not in self._dataset:
                self._dataset.ReferencedInstanceSequence = pydicom.Sequence()
            self._dataset.ReferencedInstanceSequence.clear()
            self._dataset.ReferencedInstanceSequence.extend([item.to_dataset() for item in value])

    def add_ReferencedInstance(self, item: ReferencedInstanceSequenceItem):
        if not isinstance(item, ReferencedInstanceSequenceItem):
            raise ValueError(f"Item must be an instance of ReferencedInstanceSequenceItem")
        self._ReferencedInstanceSequence.append(item)
        if "ReferencedInstanceSequence" not in self._dataset:
            self._dataset.ReferencedInstanceSequence = pydicom.Sequence()
        self._dataset.ReferencedInstanceSequence.append(item.to_dataset())

    @property
    def StartTrim(self) -> Optional[int]:
        if "StartTrim" in self._dataset:
            return self._dataset.StartTrim
        return None

    @StartTrim.setter
    def StartTrim(self, value: Optional[int]):
        if value is None:
            if "StartTrim" in self._dataset:
                del self._dataset.StartTrim
        else:
            self._dataset.StartTrim = value

    @property
    def StopTrim(self) -> Optional[int]:
        if "StopTrim" in self._dataset:
            return self._dataset.StopTrim
        return None

    @StopTrim.setter
    def StopTrim(self, value: Optional[int]):
        if value is None:
            if "StopTrim" in self._dataset:
                del self._dataset.StopTrim
        else:
            self._dataset.StopTrim = value

    @property
    def RecommendedDisplayFrameRate(self) -> Optional[int]:
        if "RecommendedDisplayFrameRate" in self._dataset:
            return self._dataset.RecommendedDisplayFrameRate
        return None

    @RecommendedDisplayFrameRate.setter
    def RecommendedDisplayFrameRate(self, value: Optional[int]):
        if value is None:
            if "RecommendedDisplayFrameRate" in self._dataset:
                del self._dataset.RecommendedDisplayFrameRate
        else:
            self._dataset.RecommendedDisplayFrameRate = value

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
                f"ReferencedPresentationStateSequence must be a list of ReferencedPresentationStateSequenceItem objects"
            )
        else:
            self._ReferencedPresentationStateSequence = value
            if "ReferencedPresentationStateSequence" not in self._dataset:
                self._dataset.ReferencedPresentationStateSequence = pydicom.Sequence()
            self._dataset.ReferencedPresentationStateSequence.clear()
            self._dataset.ReferencedPresentationStateSequence.extend([item.to_dataset() for item in value])

    def add_ReferencedPresentationState(self, item: ReferencedPresentationStateSequenceItem):
        if not isinstance(item, ReferencedPresentationStateSequenceItem):
            raise ValueError(f"Item must be an instance of ReferencedPresentationStateSequenceItem")
        self._ReferencedPresentationStateSequence.append(item)
        if "ReferencedPresentationStateSequence" not in self._dataset:
            self._dataset.ReferencedPresentationStateSequence = pydicom.Sequence()
        self._dataset.ReferencedPresentationStateSequence.append(item.to_dataset())

    @property
    def InitialCineRunState(self) -> Optional[str]:
        if "InitialCineRunState" in self._dataset:
            return self._dataset.InitialCineRunState
        return None

    @InitialCineRunState.setter
    def InitialCineRunState(self, value: Optional[str]):
        if value is None:
            if "InitialCineRunState" in self._dataset:
                del self._dataset.InitialCineRunState
        else:
            self._dataset.InitialCineRunState = value

    @property
    def PreferredPlaybackSequencing(self) -> Optional[int]:
        if "PreferredPlaybackSequencing" in self._dataset:
            return self._dataset.PreferredPlaybackSequencing
        return None

    @PreferredPlaybackSequencing.setter
    def PreferredPlaybackSequencing(self, value: Optional[int]):
        if value is None:
            if "PreferredPlaybackSequencing" in self._dataset:
                del self._dataset.PreferredPlaybackSequencing
        else:
            self._dataset.PreferredPlaybackSequencing = value

    @property
    def DisplayEnvironmentSpatialPosition(self) -> Optional[List[float]]:
        if "DisplayEnvironmentSpatialPosition" in self._dataset:
            return self._dataset.DisplayEnvironmentSpatialPosition
        return None

    @DisplayEnvironmentSpatialPosition.setter
    def DisplayEnvironmentSpatialPosition(self, value: Optional[List[float]]):
        if value is None:
            if "DisplayEnvironmentSpatialPosition" in self._dataset:
                del self._dataset.DisplayEnvironmentSpatialPosition
        else:
            self._dataset.DisplayEnvironmentSpatialPosition = value

    @property
    def ImageBoxNumber(self) -> Optional[int]:
        if "ImageBoxNumber" in self._dataset:
            return self._dataset.ImageBoxNumber
        return None

    @ImageBoxNumber.setter
    def ImageBoxNumber(self, value: Optional[int]):
        if value is None:
            if "ImageBoxNumber" in self._dataset:
                del self._dataset.ImageBoxNumber
        else:
            self._dataset.ImageBoxNumber = value

    @property
    def ImageBoxLayoutType(self) -> Optional[str]:
        if "ImageBoxLayoutType" in self._dataset:
            return self._dataset.ImageBoxLayoutType
        return None

    @ImageBoxLayoutType.setter
    def ImageBoxLayoutType(self, value: Optional[str]):
        if value is None:
            if "ImageBoxLayoutType" in self._dataset:
                del self._dataset.ImageBoxLayoutType
        else:
            self._dataset.ImageBoxLayoutType = value

    @property
    def ImageBoxTileHorizontalDimension(self) -> Optional[int]:
        if "ImageBoxTileHorizontalDimension" in self._dataset:
            return self._dataset.ImageBoxTileHorizontalDimension
        return None

    @ImageBoxTileHorizontalDimension.setter
    def ImageBoxTileHorizontalDimension(self, value: Optional[int]):
        if value is None:
            if "ImageBoxTileHorizontalDimension" in self._dataset:
                del self._dataset.ImageBoxTileHorizontalDimension
        else:
            self._dataset.ImageBoxTileHorizontalDimension = value

    @property
    def ImageBoxTileVerticalDimension(self) -> Optional[int]:
        if "ImageBoxTileVerticalDimension" in self._dataset:
            return self._dataset.ImageBoxTileVerticalDimension
        return None

    @ImageBoxTileVerticalDimension.setter
    def ImageBoxTileVerticalDimension(self, value: Optional[int]):
        if value is None:
            if "ImageBoxTileVerticalDimension" in self._dataset:
                del self._dataset.ImageBoxTileVerticalDimension
        else:
            self._dataset.ImageBoxTileVerticalDimension = value

    @property
    def ImageBoxOverlapPriority(self) -> Optional[int]:
        if "ImageBoxOverlapPriority" in self._dataset:
            return self._dataset.ImageBoxOverlapPriority
        return None

    @ImageBoxOverlapPriority.setter
    def ImageBoxOverlapPriority(self, value: Optional[int]):
        if value is None:
            if "ImageBoxOverlapPriority" in self._dataset:
                del self._dataset.ImageBoxOverlapPriority
        else:
            self._dataset.ImageBoxOverlapPriority = value

    @property
    def CineRelativeToRealTime(self) -> Optional[float]:
        if "CineRelativeToRealTime" in self._dataset:
            return self._dataset.CineRelativeToRealTime
        return None

    @CineRelativeToRealTime.setter
    def CineRelativeToRealTime(self, value: Optional[float]):
        if value is None:
            if "CineRelativeToRealTime" in self._dataset:
                del self._dataset.CineRelativeToRealTime
        else:
            self._dataset.CineRelativeToRealTime = value

    @property
    def ReferencedFirstFrameSequence(self) -> Optional[List[ReferencedFirstFrameSequenceItem]]:
        if "ReferencedFirstFrameSequence" in self._dataset:
            if len(self._ReferencedFirstFrameSequence) == len(self._dataset.ReferencedFirstFrameSequence):
                return self._ReferencedFirstFrameSequence
            else:
                return [ReferencedFirstFrameSequenceItem(x) for x in self._dataset.ReferencedFirstFrameSequence]
        return None

    @ReferencedFirstFrameSequence.setter
    def ReferencedFirstFrameSequence(self, value: Optional[List[ReferencedFirstFrameSequenceItem]]):
        if value is None:
            self._ReferencedFirstFrameSequence = []
            if "ReferencedFirstFrameSequence" in self._dataset:
                del self._dataset.ReferencedFirstFrameSequence
        elif not isinstance(value, list) or not all(isinstance(item, ReferencedFirstFrameSequenceItem) for item in value):
            raise ValueError(f"ReferencedFirstFrameSequence must be a list of ReferencedFirstFrameSequenceItem objects")
        else:
            self._ReferencedFirstFrameSequence = value
            if "ReferencedFirstFrameSequence" not in self._dataset:
                self._dataset.ReferencedFirstFrameSequence = pydicom.Sequence()
            self._dataset.ReferencedFirstFrameSequence.clear()
            self._dataset.ReferencedFirstFrameSequence.extend([item.to_dataset() for item in value])

    def add_ReferencedFirstFrame(self, item: ReferencedFirstFrameSequenceItem):
        if not isinstance(item, ReferencedFirstFrameSequenceItem):
            raise ValueError(f"Item must be an instance of ReferencedFirstFrameSequenceItem")
        self._ReferencedFirstFrameSequence.append(item)
        if "ReferencedFirstFrameSequence" not in self._dataset:
            self._dataset.ReferencedFirstFrameSequence = pydicom.Sequence()
        self._dataset.ReferencedFirstFrameSequence.append(item.to_dataset())

    @property
    def DisplaySetHorizontalJustification(self) -> Optional[str]:
        if "DisplaySetHorizontalJustification" in self._dataset:
            return self._dataset.DisplaySetHorizontalJustification
        return None

    @DisplaySetHorizontalJustification.setter
    def DisplaySetHorizontalJustification(self, value: Optional[str]):
        if value is None:
            if "DisplaySetHorizontalJustification" in self._dataset:
                del self._dataset.DisplaySetHorizontalJustification
        else:
            self._dataset.DisplaySetHorizontalJustification = value

    @property
    def DisplaySetVerticalJustification(self) -> Optional[str]:
        if "DisplaySetVerticalJustification" in self._dataset:
            return self._dataset.DisplaySetVerticalJustification
        return None

    @DisplaySetVerticalJustification.setter
    def DisplaySetVerticalJustification(self, value: Optional[str]):
        if value is None:
            if "DisplaySetVerticalJustification" in self._dataset:
                del self._dataset.DisplaySetVerticalJustification
        else:
            self._dataset.DisplaySetVerticalJustification = value
