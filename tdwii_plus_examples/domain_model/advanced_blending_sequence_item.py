from typing import Any, List, Optional

import pydicom

from .palette_color_lookup_table_sequence_item import (
    PaletteColorLookupTableSequenceItem,
)
from .referenced_image_sequence_item import ReferencedImageSequenceItem
from .referenced_spatial_registration_sequence_item import (
    ReferencedSpatialRegistrationSequenceItem,
)
from .softcopy_voilut_sequence_item import SoftcopyVOILUTSequenceItem
from .threshold_sequence_item import ThresholdSequenceItem


class AdvancedBlendingSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._ReferencedImageSequence: List[ReferencedImageSequenceItem] = []
        self._SoftcopyVOILUTSequence: List[SoftcopyVOILUTSequenceItem] = []
        self._PaletteColorLookupTableSequence: List[PaletteColorLookupTableSequenceItem] = []
        self._ReferencedSpatialRegistrationSequence: List[ReferencedSpatialRegistrationSequenceItem] = []
        self._ThresholdSequence: List[ThresholdSequenceItem] = []

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
    def StudyInstanceUID(self) -> Optional[str]:
        if "StudyInstanceUID" in self._dataset:
            return self._dataset.StudyInstanceUID
        return None

    @StudyInstanceUID.setter
    def StudyInstanceUID(self, value: Optional[str]):
        if value is None:
            if "StudyInstanceUID" in self._dataset:
                del self._dataset.StudyInstanceUID
        else:
            self._dataset.StudyInstanceUID = value

    @property
    def SeriesInstanceUID(self) -> Optional[str]:
        if "SeriesInstanceUID" in self._dataset:
            return self._dataset.SeriesInstanceUID
        return None

    @SeriesInstanceUID.setter
    def SeriesInstanceUID(self, value: Optional[str]):
        if value is None:
            if "SeriesInstanceUID" in self._dataset:
                del self._dataset.SeriesInstanceUID
        else:
            self._dataset.SeriesInstanceUID = value

    @property
    def SoftcopyVOILUTSequence(self) -> Optional[List[SoftcopyVOILUTSequenceItem]]:
        if "SoftcopyVOILUTSequence" in self._dataset:
            if len(self._SoftcopyVOILUTSequence) == len(self._dataset.SoftcopyVOILUTSequence):
                return self._SoftcopyVOILUTSequence
            else:
                return [SoftcopyVOILUTSequenceItem(x) for x in self._dataset.SoftcopyVOILUTSequence]
        return None

    @SoftcopyVOILUTSequence.setter
    def SoftcopyVOILUTSequence(self, value: Optional[List[SoftcopyVOILUTSequenceItem]]):
        if value is None:
            self._SoftcopyVOILUTSequence = []
            if "SoftcopyVOILUTSequence" in self._dataset:
                del self._dataset.SoftcopyVOILUTSequence
        elif not isinstance(value, list) or not all(isinstance(item, SoftcopyVOILUTSequenceItem) for item in value):
            raise ValueError(f"SoftcopyVOILUTSequence must be a list of SoftcopyVOILUTSequenceItem objects")
        else:
            self._SoftcopyVOILUTSequence = value
            if "SoftcopyVOILUTSequence" not in self._dataset:
                self._dataset.SoftcopyVOILUTSequence = pydicom.Sequence()
            self._dataset.SoftcopyVOILUTSequence.clear()
            self._dataset.SoftcopyVOILUTSequence.extend([item.to_dataset() for item in value])

    def add_SoftcopyVOILUT(self, item: SoftcopyVOILUTSequenceItem):
        if not isinstance(item, SoftcopyVOILUTSequenceItem):
            raise ValueError(f"Item must be an instance of SoftcopyVOILUTSequenceItem")
        self._SoftcopyVOILUTSequence.append(item)
        if "SoftcopyVOILUTSequence" not in self._dataset:
            self._dataset.SoftcopyVOILUTSequence = pydicom.Sequence()
        self._dataset.SoftcopyVOILUTSequence.append(item.to_dataset())

    @property
    def PaletteColorLookupTableSequence(self) -> Optional[List[PaletteColorLookupTableSequenceItem]]:
        if "PaletteColorLookupTableSequence" in self._dataset:
            if len(self._PaletteColorLookupTableSequence) == len(self._dataset.PaletteColorLookupTableSequence):
                return self._PaletteColorLookupTableSequence
            else:
                return [PaletteColorLookupTableSequenceItem(x) for x in self._dataset.PaletteColorLookupTableSequence]
        return None

    @PaletteColorLookupTableSequence.setter
    def PaletteColorLookupTableSequence(self, value: Optional[List[PaletteColorLookupTableSequenceItem]]):
        if value is None:
            self._PaletteColorLookupTableSequence = []
            if "PaletteColorLookupTableSequence" in self._dataset:
                del self._dataset.PaletteColorLookupTableSequence
        elif not isinstance(value, list) or not all(isinstance(item, PaletteColorLookupTableSequenceItem) for item in value):
            raise ValueError(f"PaletteColorLookupTableSequence must be a list of PaletteColorLookupTableSequenceItem objects")
        else:
            self._PaletteColorLookupTableSequence = value
            if "PaletteColorLookupTableSequence" not in self._dataset:
                self._dataset.PaletteColorLookupTableSequence = pydicom.Sequence()
            self._dataset.PaletteColorLookupTableSequence.clear()
            self._dataset.PaletteColorLookupTableSequence.extend([item.to_dataset() for item in value])

    def add_PaletteColorLookupTable(self, item: PaletteColorLookupTableSequenceItem):
        if not isinstance(item, PaletteColorLookupTableSequenceItem):
            raise ValueError(f"Item must be an instance of PaletteColorLookupTableSequenceItem")
        self._PaletteColorLookupTableSequence.append(item)
        if "PaletteColorLookupTableSequence" not in self._dataset:
            self._dataset.PaletteColorLookupTableSequence = pydicom.Sequence()
        self._dataset.PaletteColorLookupTableSequence.append(item.to_dataset())

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
                f"ReferencedSpatialRegistrationSequence must be a list of ReferencedSpatialRegistrationSequenceItem objects"
            )
        else:
            self._ReferencedSpatialRegistrationSequence = value
            if "ReferencedSpatialRegistrationSequence" not in self._dataset:
                self._dataset.ReferencedSpatialRegistrationSequence = pydicom.Sequence()
            self._dataset.ReferencedSpatialRegistrationSequence.clear()
            self._dataset.ReferencedSpatialRegistrationSequence.extend([item.to_dataset() for item in value])

    def add_ReferencedSpatialRegistration(self, item: ReferencedSpatialRegistrationSequenceItem):
        if not isinstance(item, ReferencedSpatialRegistrationSequenceItem):
            raise ValueError(f"Item must be an instance of ReferencedSpatialRegistrationSequenceItem")
        self._ReferencedSpatialRegistrationSequence.append(item)
        if "ReferencedSpatialRegistrationSequence" not in self._dataset:
            self._dataset.ReferencedSpatialRegistrationSequence = pydicom.Sequence()
        self._dataset.ReferencedSpatialRegistrationSequence.append(item.to_dataset())

    @property
    def BlendingInputNumber(self) -> Optional[int]:
        if "BlendingInputNumber" in self._dataset:
            return self._dataset.BlendingInputNumber
        return None

    @BlendingInputNumber.setter
    def BlendingInputNumber(self, value: Optional[int]):
        if value is None:
            if "BlendingInputNumber" in self._dataset:
                del self._dataset.BlendingInputNumber
        else:
            self._dataset.BlendingInputNumber = value

    @property
    def TimeSeriesBlending(self) -> Optional[str]:
        if "TimeSeriesBlending" in self._dataset:
            return self._dataset.TimeSeriesBlending
        return None

    @TimeSeriesBlending.setter
    def TimeSeriesBlending(self, value: Optional[str]):
        if value is None:
            if "TimeSeriesBlending" in self._dataset:
                del self._dataset.TimeSeriesBlending
        else:
            self._dataset.TimeSeriesBlending = value

    @property
    def GeometryForDisplay(self) -> Optional[str]:
        if "GeometryForDisplay" in self._dataset:
            return self._dataset.GeometryForDisplay
        return None

    @GeometryForDisplay.setter
    def GeometryForDisplay(self, value: Optional[str]):
        if value is None:
            if "GeometryForDisplay" in self._dataset:
                del self._dataset.GeometryForDisplay
        else:
            self._dataset.GeometryForDisplay = value

    @property
    def ThresholdSequence(self) -> Optional[List[ThresholdSequenceItem]]:
        if "ThresholdSequence" in self._dataset:
            if len(self._ThresholdSequence) == len(self._dataset.ThresholdSequence):
                return self._ThresholdSequence
            else:
                return [ThresholdSequenceItem(x) for x in self._dataset.ThresholdSequence]
        return None

    @ThresholdSequence.setter
    def ThresholdSequence(self, value: Optional[List[ThresholdSequenceItem]]):
        if value is None:
            self._ThresholdSequence = []
            if "ThresholdSequence" in self._dataset:
                del self._dataset.ThresholdSequence
        elif not isinstance(value, list) or not all(isinstance(item, ThresholdSequenceItem) for item in value):
            raise ValueError(f"ThresholdSequence must be a list of ThresholdSequenceItem objects")
        else:
            self._ThresholdSequence = value
            if "ThresholdSequence" not in self._dataset:
                self._dataset.ThresholdSequence = pydicom.Sequence()
            self._dataset.ThresholdSequence.clear()
            self._dataset.ThresholdSequence.extend([item.to_dataset() for item in value])

    def add_Threshold(self, item: ThresholdSequenceItem):
        if not isinstance(item, ThresholdSequenceItem):
            raise ValueError(f"Item must be an instance of ThresholdSequenceItem")
        self._ThresholdSequence.append(item)
        if "ThresholdSequence" not in self._dataset:
            self._dataset.ThresholdSequence = pydicom.Sequence()
        self._dataset.ThresholdSequence.append(item.to_dataset())
