from typing import Any, List, Optional  # noqa

import pydicom

from .derivation_image_sequence_item import DerivationImageSequenceItem
from .frame_content_sequence_item import FrameContentSequenceItem
from .pixel_measures_sequence_item import PixelMeasuresSequenceItem
from .plane_orientation_sequence_item import PlaneOrientationSequenceItem
from .plane_position_sequence_item import PlanePositionSequenceItem
from .plane_position_slide_sequence_item import PlanePositionSlideSequenceItem
from .segment_identification_sequence_item import SegmentIdentificationSequenceItem


class PerFrameFunctionalGroupsSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._DerivationImageSequence: List[DerivationImageSequenceItem] = []
        self._FrameContentSequence: List[FrameContentSequenceItem] = []
        self._PlanePositionSequence: List[PlanePositionSequenceItem] = []
        self._PlaneOrientationSequence: List[PlaneOrientationSequenceItem] = []
        self._PixelMeasuresSequence: List[PixelMeasuresSequenceItem] = []
        self._PlanePositionSlideSequence: List[PlanePositionSlideSequenceItem] = []
        self._SegmentIdentificationSequence: List[SegmentIdentificationSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

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
    def PlanePositionSequence(self) -> Optional[List[PlanePositionSequenceItem]]:
        if "PlanePositionSequence" in self._dataset:
            if len(self._PlanePositionSequence) == len(self._dataset.PlanePositionSequence):
                return self._PlanePositionSequence
            else:
                return [PlanePositionSequenceItem(x) for x in self._dataset.PlanePositionSequence]
        return None

    @PlanePositionSequence.setter
    def PlanePositionSequence(self, value: Optional[List[PlanePositionSequenceItem]]):
        if value is None:
            self._PlanePositionSequence = []
            if "PlanePositionSequence" in self._dataset:
                del self._dataset.PlanePositionSequence
        elif not isinstance(value, list) or not all(isinstance(item, PlanePositionSequenceItem) for item in value):
            raise ValueError("PlanePositionSequence must be a list of PlanePositionSequenceItem objects")
        else:
            self._PlanePositionSequence = value
            if "PlanePositionSequence" not in self._dataset:
                self._dataset.PlanePositionSequence = pydicom.Sequence()
            self._dataset.PlanePositionSequence.clear()
            self._dataset.PlanePositionSequence.extend([item.to_dataset() for item in value])

    def add_PlanePosition(self, item: PlanePositionSequenceItem):
        if not isinstance(item, PlanePositionSequenceItem):
            raise ValueError("Item must be an instance of PlanePositionSequenceItem")
        self._PlanePositionSequence.append(item)
        if "PlanePositionSequence" not in self._dataset:
            self._dataset.PlanePositionSequence = pydicom.Sequence()
        self._dataset.PlanePositionSequence.append(item.to_dataset())

    @property
    def PlaneOrientationSequence(self) -> Optional[List[PlaneOrientationSequenceItem]]:
        if "PlaneOrientationSequence" in self._dataset:
            if len(self._PlaneOrientationSequence) == len(self._dataset.PlaneOrientationSequence):
                return self._PlaneOrientationSequence
            else:
                return [PlaneOrientationSequenceItem(x) for x in self._dataset.PlaneOrientationSequence]
        return None

    @PlaneOrientationSequence.setter
    def PlaneOrientationSequence(self, value: Optional[List[PlaneOrientationSequenceItem]]):
        if value is None:
            self._PlaneOrientationSequence = []
            if "PlaneOrientationSequence" in self._dataset:
                del self._dataset.PlaneOrientationSequence
        elif not isinstance(value, list) or not all(isinstance(item, PlaneOrientationSequenceItem) for item in value):
            raise ValueError("PlaneOrientationSequence must be a list of PlaneOrientationSequenceItem objects")
        else:
            self._PlaneOrientationSequence = value
            if "PlaneOrientationSequence" not in self._dataset:
                self._dataset.PlaneOrientationSequence = pydicom.Sequence()
            self._dataset.PlaneOrientationSequence.clear()
            self._dataset.PlaneOrientationSequence.extend([item.to_dataset() for item in value])

    def add_PlaneOrientation(self, item: PlaneOrientationSequenceItem):
        if not isinstance(item, PlaneOrientationSequenceItem):
            raise ValueError("Item must be an instance of PlaneOrientationSequenceItem")
        self._PlaneOrientationSequence.append(item)
        if "PlaneOrientationSequence" not in self._dataset:
            self._dataset.PlaneOrientationSequence = pydicom.Sequence()
        self._dataset.PlaneOrientationSequence.append(item.to_dataset())

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

    @property
    def SegmentIdentificationSequence(self) -> Optional[List[SegmentIdentificationSequenceItem]]:
        if "SegmentIdentificationSequence" in self._dataset:
            if len(self._SegmentIdentificationSequence) == len(self._dataset.SegmentIdentificationSequence):
                return self._SegmentIdentificationSequence
            else:
                return [SegmentIdentificationSequenceItem(x) for x in self._dataset.SegmentIdentificationSequence]
        return None

    @SegmentIdentificationSequence.setter
    def SegmentIdentificationSequence(self, value: Optional[List[SegmentIdentificationSequenceItem]]):
        if value is None:
            self._SegmentIdentificationSequence = []
            if "SegmentIdentificationSequence" in self._dataset:
                del self._dataset.SegmentIdentificationSequence
        elif not isinstance(value, list) or not all(isinstance(item, SegmentIdentificationSequenceItem) for item in value):
            raise ValueError("SegmentIdentificationSequence must be a list of SegmentIdentificationSequenceItem objects")
        else:
            self._SegmentIdentificationSequence = value
            if "SegmentIdentificationSequence" not in self._dataset:
                self._dataset.SegmentIdentificationSequence = pydicom.Sequence()
            self._dataset.SegmentIdentificationSequence.clear()
            self._dataset.SegmentIdentificationSequence.extend([item.to_dataset() for item in value])

    def add_SegmentIdentification(self, item: SegmentIdentificationSequenceItem):
        if not isinstance(item, SegmentIdentificationSequenceItem):
            raise ValueError("Item must be an instance of SegmentIdentificationSequenceItem")
        self._SegmentIdentificationSequence.append(item)
        if "SegmentIdentificationSequence" not in self._dataset:
            self._dataset.SegmentIdentificationSequence = pydicom.Sequence()
        self._dataset.SegmentIdentificationSequence.append(item.to_dataset())
