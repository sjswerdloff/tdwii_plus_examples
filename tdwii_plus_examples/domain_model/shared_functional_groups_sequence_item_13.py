from typing import Any, List, Optional  # noqa

import pydicom

from .confocal_microscopy_image_frame_type_sequence_item import (
    ConfocalMicroscopyImageFrameTypeSequenceItem,
)
from .derivation_image_sequence_item import DerivationImageSequenceItem
from .frame_anatomy_sequence_item import FrameAnatomySequenceItem
from .frame_content_sequence_item import FrameContentSequenceItem
from .optical_path_identification_sequence_item import (
    OpticalPathIdentificationSequenceItem,
)
from .pixel_measures_sequence_item import PixelMeasuresSequenceItem
from .plane_position_slide_sequence_item import PlanePositionSlideSequenceItem
from .real_world_value_mapping_sequence_item import RealWorldValueMappingSequenceItem
from .referenced_image_sequence_item import ReferencedImageSequenceItem


class SharedFunctionalGroupsSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._ReferencedImageSequence: List[ReferencedImageSequenceItem] = []
        self._DerivationImageSequence: List[DerivationImageSequenceItem] = []
        self._FrameAnatomySequence: List[FrameAnatomySequenceItem] = []
        self._FrameContentSequence: List[FrameContentSequenceItem] = []
        self._PixelMeasuresSequence: List[PixelMeasuresSequenceItem] = []
        self._RealWorldValueMappingSequence: List[RealWorldValueMappingSequenceItem] = []
        self._ConfocalMicroscopyImageFrameTypeSequence: List[ConfocalMicroscopyImageFrameTypeSequenceItem] = []
        self._OpticalPathIdentificationSequence: List[OpticalPathIdentificationSequenceItem] = []
        self._PlanePositionSlideSequence: List[PlanePositionSlideSequenceItem] = []

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
    def DerivationImageSequence(self) -> Optional[List[DerivationImageSequenceItem]]:
        if "DerivationImageSequence" in self._dataset:
            if len(self._DerivationImageSequence) == len(self._dataset.DerivationImageSequence):
                return self._DerivationImageSequence
            else:
                return [DerivationImageSequenceItem(x) for x in self._dataset.DerivationImageSequence]
        return None

    @DerivationImageSequence.setter
    def DerivationImageSequence(self, value: Optional[List[DerivationImageSequenceItem]]):
        if value is None:
            self._DerivationImageSequence = []
            if "DerivationImageSequence" in self._dataset:
                del self._dataset.DerivationImageSequence
        elif not isinstance(value, list) or not all(isinstance(item, DerivationImageSequenceItem) for item in value):
            raise ValueError("DerivationImageSequence must be a list of DerivationImageSequenceItem objects")
        else:
            self._DerivationImageSequence = value
            if "DerivationImageSequence" not in self._dataset:
                self._dataset.DerivationImageSequence = pydicom.Sequence()
            self._dataset.DerivationImageSequence.clear()
            self._dataset.DerivationImageSequence.extend([item.to_dataset() for item in value])

    def add_DerivationImage(self, item: DerivationImageSequenceItem):
        if not isinstance(item, DerivationImageSequenceItem):
            raise ValueError("Item must be an instance of DerivationImageSequenceItem")
        self._DerivationImageSequence.append(item)
        if "DerivationImageSequence" not in self._dataset:
            self._dataset.DerivationImageSequence = pydicom.Sequence()
        self._dataset.DerivationImageSequence.append(item.to_dataset())

    @property
    def FrameAnatomySequence(self) -> Optional[List[FrameAnatomySequenceItem]]:
        if "FrameAnatomySequence" in self._dataset:
            if len(self._FrameAnatomySequence) == len(self._dataset.FrameAnatomySequence):
                return self._FrameAnatomySequence
            else:
                return [FrameAnatomySequenceItem(x) for x in self._dataset.FrameAnatomySequence]
        return None

    @FrameAnatomySequence.setter
    def FrameAnatomySequence(self, value: Optional[List[FrameAnatomySequenceItem]]):
        if value is None:
            self._FrameAnatomySequence = []
            if "FrameAnatomySequence" in self._dataset:
                del self._dataset.FrameAnatomySequence
        elif not isinstance(value, list) or not all(isinstance(item, FrameAnatomySequenceItem) for item in value):
            raise ValueError("FrameAnatomySequence must be a list of FrameAnatomySequenceItem objects")
        else:
            self._FrameAnatomySequence = value
            if "FrameAnatomySequence" not in self._dataset:
                self._dataset.FrameAnatomySequence = pydicom.Sequence()
            self._dataset.FrameAnatomySequence.clear()
            self._dataset.FrameAnatomySequence.extend([item.to_dataset() for item in value])

    def add_FrameAnatomy(self, item: FrameAnatomySequenceItem):
        if not isinstance(item, FrameAnatomySequenceItem):
            raise ValueError("Item must be an instance of FrameAnatomySequenceItem")
        self._FrameAnatomySequence.append(item)
        if "FrameAnatomySequence" not in self._dataset:
            self._dataset.FrameAnatomySequence = pydicom.Sequence()
        self._dataset.FrameAnatomySequence.append(item.to_dataset())

    @property
    def FrameContentSequence(self) -> Optional[List[FrameContentSequenceItem]]:
        if "FrameContentSequence" in self._dataset:
            if len(self._FrameContentSequence) == len(self._dataset.FrameContentSequence):
                return self._FrameContentSequence
            else:
                return [FrameContentSequenceItem(x) for x in self._dataset.FrameContentSequence]
        return None

    @FrameContentSequence.setter
    def FrameContentSequence(self, value: Optional[List[FrameContentSequenceItem]]):
        if value is None:
            self._FrameContentSequence = []
            if "FrameContentSequence" in self._dataset:
                del self._dataset.FrameContentSequence
        elif not isinstance(value, list) or not all(isinstance(item, FrameContentSequenceItem) for item in value):
            raise ValueError("FrameContentSequence must be a list of FrameContentSequenceItem objects")
        else:
            self._FrameContentSequence = value
            if "FrameContentSequence" not in self._dataset:
                self._dataset.FrameContentSequence = pydicom.Sequence()
            self._dataset.FrameContentSequence.clear()
            self._dataset.FrameContentSequence.extend([item.to_dataset() for item in value])

    def add_FrameContent(self, item: FrameContentSequenceItem):
        if not isinstance(item, FrameContentSequenceItem):
            raise ValueError("Item must be an instance of FrameContentSequenceItem")
        self._FrameContentSequence.append(item)
        if "FrameContentSequence" not in self._dataset:
            self._dataset.FrameContentSequence = pydicom.Sequence()
        self._dataset.FrameContentSequence.append(item.to_dataset())

    @property
    def PixelMeasuresSequence(self) -> Optional[List[PixelMeasuresSequenceItem]]:
        if "PixelMeasuresSequence" in self._dataset:
            if len(self._PixelMeasuresSequence) == len(self._dataset.PixelMeasuresSequence):
                return self._PixelMeasuresSequence
            else:
                return [PixelMeasuresSequenceItem(x) for x in self._dataset.PixelMeasuresSequence]
        return None

    @PixelMeasuresSequence.setter
    def PixelMeasuresSequence(self, value: Optional[List[PixelMeasuresSequenceItem]]):
        if value is None:
            self._PixelMeasuresSequence = []
            if "PixelMeasuresSequence" in self._dataset:
                del self._dataset.PixelMeasuresSequence
        elif not isinstance(value, list) or not all(isinstance(item, PixelMeasuresSequenceItem) for item in value):
            raise ValueError("PixelMeasuresSequence must be a list of PixelMeasuresSequenceItem objects")
        else:
            self._PixelMeasuresSequence = value
            if "PixelMeasuresSequence" not in self._dataset:
                self._dataset.PixelMeasuresSequence = pydicom.Sequence()
            self._dataset.PixelMeasuresSequence.clear()
            self._dataset.PixelMeasuresSequence.extend([item.to_dataset() for item in value])

    def add_PixelMeasures(self, item: PixelMeasuresSequenceItem):
        if not isinstance(item, PixelMeasuresSequenceItem):
            raise ValueError("Item must be an instance of PixelMeasuresSequenceItem")
        self._PixelMeasuresSequence.append(item)
        if "PixelMeasuresSequence" not in self._dataset:
            self._dataset.PixelMeasuresSequence = pydicom.Sequence()
        self._dataset.PixelMeasuresSequence.append(item.to_dataset())

    @property
    def RealWorldValueMappingSequence(self) -> Optional[List[RealWorldValueMappingSequenceItem]]:
        if "RealWorldValueMappingSequence" in self._dataset:
            if len(self._RealWorldValueMappingSequence) == len(self._dataset.RealWorldValueMappingSequence):
                return self._RealWorldValueMappingSequence
            else:
                return [RealWorldValueMappingSequenceItem(x) for x in self._dataset.RealWorldValueMappingSequence]
        return None

    @RealWorldValueMappingSequence.setter
    def RealWorldValueMappingSequence(self, value: Optional[List[RealWorldValueMappingSequenceItem]]):
        if value is None:
            self._RealWorldValueMappingSequence = []
            if "RealWorldValueMappingSequence" in self._dataset:
                del self._dataset.RealWorldValueMappingSequence
        elif not isinstance(value, list) or not all(isinstance(item, RealWorldValueMappingSequenceItem) for item in value):
            raise ValueError("RealWorldValueMappingSequence must be a list of RealWorldValueMappingSequenceItem objects")
        else:
            self._RealWorldValueMappingSequence = value
            if "RealWorldValueMappingSequence" not in self._dataset:
                self._dataset.RealWorldValueMappingSequence = pydicom.Sequence()
            self._dataset.RealWorldValueMappingSequence.clear()
            self._dataset.RealWorldValueMappingSequence.extend([item.to_dataset() for item in value])

    def add_RealWorldValueMapping(self, item: RealWorldValueMappingSequenceItem):
        if not isinstance(item, RealWorldValueMappingSequenceItem):
            raise ValueError("Item must be an instance of RealWorldValueMappingSequenceItem")
        self._RealWorldValueMappingSequence.append(item)
        if "RealWorldValueMappingSequence" not in self._dataset:
            self._dataset.RealWorldValueMappingSequence = pydicom.Sequence()
        self._dataset.RealWorldValueMappingSequence.append(item.to_dataset())

    @property
    def ConfocalMicroscopyImageFrameTypeSequence(self) -> Optional[List[ConfocalMicroscopyImageFrameTypeSequenceItem]]:
        if "ConfocalMicroscopyImageFrameTypeSequence" in self._dataset:
            if len(self._ConfocalMicroscopyImageFrameTypeSequence) == len(
                self._dataset.ConfocalMicroscopyImageFrameTypeSequence
            ):
                return self._ConfocalMicroscopyImageFrameTypeSequence
            else:
                return [
                    ConfocalMicroscopyImageFrameTypeSequenceItem(x)
                    for x in self._dataset.ConfocalMicroscopyImageFrameTypeSequence
                ]
        return None

    @ConfocalMicroscopyImageFrameTypeSequence.setter
    def ConfocalMicroscopyImageFrameTypeSequence(self, value: Optional[List[ConfocalMicroscopyImageFrameTypeSequenceItem]]):
        if value is None:
            self._ConfocalMicroscopyImageFrameTypeSequence = []
            if "ConfocalMicroscopyImageFrameTypeSequence" in self._dataset:
                del self._dataset.ConfocalMicroscopyImageFrameTypeSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, ConfocalMicroscopyImageFrameTypeSequenceItem) for item in value
        ):
            raise ValueError(
                "ConfocalMicroscopyImageFrameTypeSequence must be a list of ConfocalMicroscopyImageFrameTypeSequenceItem"
                " objects"
            )
        else:
            self._ConfocalMicroscopyImageFrameTypeSequence = value
            if "ConfocalMicroscopyImageFrameTypeSequence" not in self._dataset:
                self._dataset.ConfocalMicroscopyImageFrameTypeSequence = pydicom.Sequence()
            self._dataset.ConfocalMicroscopyImageFrameTypeSequence.clear()
            self._dataset.ConfocalMicroscopyImageFrameTypeSequence.extend([item.to_dataset() for item in value])

    def add_ConfocalMicroscopyImageFrameType(self, item: ConfocalMicroscopyImageFrameTypeSequenceItem):
        if not isinstance(item, ConfocalMicroscopyImageFrameTypeSequenceItem):
            raise ValueError("Item must be an instance of ConfocalMicroscopyImageFrameTypeSequenceItem")
        self._ConfocalMicroscopyImageFrameTypeSequence.append(item)
        if "ConfocalMicroscopyImageFrameTypeSequence" not in self._dataset:
            self._dataset.ConfocalMicroscopyImageFrameTypeSequence = pydicom.Sequence()
        self._dataset.ConfocalMicroscopyImageFrameTypeSequence.append(item.to_dataset())

    @property
    def OpticalPathIdentificationSequence(self) -> Optional[List[OpticalPathIdentificationSequenceItem]]:
        if "OpticalPathIdentificationSequence" in self._dataset:
            if len(self._OpticalPathIdentificationSequence) == len(self._dataset.OpticalPathIdentificationSequence):
                return self._OpticalPathIdentificationSequence
            else:
                return [OpticalPathIdentificationSequenceItem(x) for x in self._dataset.OpticalPathIdentificationSequence]
        return None

    @OpticalPathIdentificationSequence.setter
    def OpticalPathIdentificationSequence(self, value: Optional[List[OpticalPathIdentificationSequenceItem]]):
        if value is None:
            self._OpticalPathIdentificationSequence = []
            if "OpticalPathIdentificationSequence" in self._dataset:
                del self._dataset.OpticalPathIdentificationSequence
        elif not isinstance(value, list) or not all(isinstance(item, OpticalPathIdentificationSequenceItem) for item in value):
            raise ValueError(
                "OpticalPathIdentificationSequence must be a list of OpticalPathIdentificationSequenceItem objects"
            )
        else:
            self._OpticalPathIdentificationSequence = value
            if "OpticalPathIdentificationSequence" not in self._dataset:
                self._dataset.OpticalPathIdentificationSequence = pydicom.Sequence()
            self._dataset.OpticalPathIdentificationSequence.clear()
            self._dataset.OpticalPathIdentificationSequence.extend([item.to_dataset() for item in value])

    def add_OpticalPathIdentification(self, item: OpticalPathIdentificationSequenceItem):
        if not isinstance(item, OpticalPathIdentificationSequenceItem):
            raise ValueError("Item must be an instance of OpticalPathIdentificationSequenceItem")
        self._OpticalPathIdentificationSequence.append(item)
        if "OpticalPathIdentificationSequence" not in self._dataset:
            self._dataset.OpticalPathIdentificationSequence = pydicom.Sequence()
        self._dataset.OpticalPathIdentificationSequence.append(item.to_dataset())

    @property
    def PlanePositionSlideSequence(self) -> Optional[List[PlanePositionSlideSequenceItem]]:
        if "PlanePositionSlideSequence" in self._dataset:
            if len(self._PlanePositionSlideSequence) == len(self._dataset.PlanePositionSlideSequence):
                return self._PlanePositionSlideSequence
            else:
                return [PlanePositionSlideSequenceItem(x) for x in self._dataset.PlanePositionSlideSequence]
        return None

    @PlanePositionSlideSequence.setter
    def PlanePositionSlideSequence(self, value: Optional[List[PlanePositionSlideSequenceItem]]):
        if value is None:
            self._PlanePositionSlideSequence = []
            if "PlanePositionSlideSequence" in self._dataset:
                del self._dataset.PlanePositionSlideSequence
        elif not isinstance(value, list) or not all(isinstance(item, PlanePositionSlideSequenceItem) for item in value):
            raise ValueError("PlanePositionSlideSequence must be a list of PlanePositionSlideSequenceItem objects")
        else:
            self._PlanePositionSlideSequence = value
            if "PlanePositionSlideSequence" not in self._dataset:
                self._dataset.PlanePositionSlideSequence = pydicom.Sequence()
            self._dataset.PlanePositionSlideSequence.clear()
            self._dataset.PlanePositionSlideSequence.extend([item.to_dataset() for item in value])

    def add_PlanePositionSlide(self, item: PlanePositionSlideSequenceItem):
        if not isinstance(item, PlanePositionSlideSequenceItem):
            raise ValueError("Item must be an instance of PlanePositionSlideSequenceItem")
        self._PlanePositionSlideSequence.append(item)
        if "PlanePositionSlideSequence" not in self._dataset:
            self._dataset.PlanePositionSlideSequence = pydicom.Sequence()
        self._dataset.PlanePositionSlideSequence.append(item.to_dataset())
