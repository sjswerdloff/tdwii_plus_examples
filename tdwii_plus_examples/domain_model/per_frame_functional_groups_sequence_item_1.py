from typing import Any, List, Optional  # noqa

import pydicom

from .contrast_bolus_usage_sequence_item import ContrastBolusUsageSequenceItem
from .derivation_image_sequence_item import DerivationImageSequenceItem
from .frame_anatomy_sequence_item import FrameAnatomySequenceItem
from .frame_content_sequence_item import FrameContentSequenceItem
from .frame_voilut_sequence_item import FrameVOILUTSequenceItem
from .pixel_measures_sequence_item import PixelMeasuresSequenceItem
from .pixel_value_transformation_sequence_item import (
    PixelValueTransformationSequenceItem,
)
from .plane_orientation_sequence_item import PlaneOrientationSequenceItem
from .plane_position_sequence_item import PlanePositionSequenceItem
from .real_world_value_mapping_sequence_item import RealWorldValueMappingSequenceItem
from .referenced_image_sequence_item import ReferencedImageSequenceItem
from .x_ray3_d_frame_type_sequence_item import XRay3DFrameTypeSequenceItem


class PerFrameFunctionalGroupsSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._ReferencedImageSequence: List[ReferencedImageSequenceItem] = []
        self._DerivationImageSequence: List[DerivationImageSequenceItem] = []
        self._ContrastBolusUsageSequence: List[ContrastBolusUsageSequenceItem] = []
        self._XRay3DFrameTypeSequence: List[XRay3DFrameTypeSequenceItem] = []
        self._FrameAnatomySequence: List[FrameAnatomySequenceItem] = []
        self._FrameContentSequence: List[FrameContentSequenceItem] = []
        self._PlanePositionSequence: List[PlanePositionSequenceItem] = []
        self._PlaneOrientationSequence: List[PlaneOrientationSequenceItem] = []
        self._PixelMeasuresSequence: List[PixelMeasuresSequenceItem] = []
        self._FrameVOILUTSequence: List[FrameVOILUTSequenceItem] = []
        self._PixelValueTransformationSequence: List[PixelValueTransformationSequenceItem] = []
        self._RealWorldValueMappingSequence: List[RealWorldValueMappingSequenceItem] = []

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
    def ContrastBolusUsageSequence(self) -> Optional[List[ContrastBolusUsageSequenceItem]]:
        if "ContrastBolusUsageSequence" in self._dataset:
            if len(self._ContrastBolusUsageSequence) == len(self._dataset.ContrastBolusUsageSequence):
                return self._ContrastBolusUsageSequence
            else:
                return [ContrastBolusUsageSequenceItem(x) for x in self._dataset.ContrastBolusUsageSequence]
        return None

    @ContrastBolusUsageSequence.setter
    def ContrastBolusUsageSequence(self, value: Optional[List[ContrastBolusUsageSequenceItem]]):
        if value is None:
            self._ContrastBolusUsageSequence = []
            if "ContrastBolusUsageSequence" in self._dataset:
                del self._dataset.ContrastBolusUsageSequence
        elif not isinstance(value, list) or not all(isinstance(item, ContrastBolusUsageSequenceItem) for item in value):
            raise ValueError("ContrastBolusUsageSequence must be a list of ContrastBolusUsageSequenceItem objects")
        else:
            self._ContrastBolusUsageSequence = value
            if "ContrastBolusUsageSequence" not in self._dataset:
                self._dataset.ContrastBolusUsageSequence = pydicom.Sequence()
            self._dataset.ContrastBolusUsageSequence.clear()
            self._dataset.ContrastBolusUsageSequence.extend([item.to_dataset() for item in value])

    def add_ContrastBolusUsage(self, item: ContrastBolusUsageSequenceItem):
        if not isinstance(item, ContrastBolusUsageSequenceItem):
            raise ValueError("Item must be an instance of ContrastBolusUsageSequenceItem")
        self._ContrastBolusUsageSequence.append(item)
        if "ContrastBolusUsageSequence" not in self._dataset:
            self._dataset.ContrastBolusUsageSequence = pydicom.Sequence()
        self._dataset.ContrastBolusUsageSequence.append(item.to_dataset())

    @property
    def XRay3DFrameTypeSequence(self) -> Optional[List[XRay3DFrameTypeSequenceItem]]:
        if "XRay3DFrameTypeSequence" in self._dataset:
            if len(self._XRay3DFrameTypeSequence) == len(self._dataset.XRay3DFrameTypeSequence):
                return self._XRay3DFrameTypeSequence
            else:
                return [XRay3DFrameTypeSequenceItem(x) for x in self._dataset.XRay3DFrameTypeSequence]
        return None

    @XRay3DFrameTypeSequence.setter
    def XRay3DFrameTypeSequence(self, value: Optional[List[XRay3DFrameTypeSequenceItem]]):
        if value is None:
            self._XRay3DFrameTypeSequence = []
            if "XRay3DFrameTypeSequence" in self._dataset:
                del self._dataset.XRay3DFrameTypeSequence
        elif not isinstance(value, list) or not all(isinstance(item, XRay3DFrameTypeSequenceItem) for item in value):
            raise ValueError("XRay3DFrameTypeSequence must be a list of XRay3DFrameTypeSequenceItem objects")
        else:
            self._XRay3DFrameTypeSequence = value
            if "XRay3DFrameTypeSequence" not in self._dataset:
                self._dataset.XRay3DFrameTypeSequence = pydicom.Sequence()
            self._dataset.XRay3DFrameTypeSequence.clear()
            self._dataset.XRay3DFrameTypeSequence.extend([item.to_dataset() for item in value])

    def add_XRay3DFrameType(self, item: XRay3DFrameTypeSequenceItem):
        if not isinstance(item, XRay3DFrameTypeSequenceItem):
            raise ValueError("Item must be an instance of XRay3DFrameTypeSequenceItem")
        self._XRay3DFrameTypeSequence.append(item)
        if "XRay3DFrameTypeSequence" not in self._dataset:
            self._dataset.XRay3DFrameTypeSequence = pydicom.Sequence()
        self._dataset.XRay3DFrameTypeSequence.append(item.to_dataset())

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
    def FrameVOILUTSequence(self) -> Optional[List[FrameVOILUTSequenceItem]]:
        if "FrameVOILUTSequence" in self._dataset:
            if len(self._FrameVOILUTSequence) == len(self._dataset.FrameVOILUTSequence):
                return self._FrameVOILUTSequence
            else:
                return [FrameVOILUTSequenceItem(x) for x in self._dataset.FrameVOILUTSequence]
        return None

    @FrameVOILUTSequence.setter
    def FrameVOILUTSequence(self, value: Optional[List[FrameVOILUTSequenceItem]]):
        if value is None:
            self._FrameVOILUTSequence = []
            if "FrameVOILUTSequence" in self._dataset:
                del self._dataset.FrameVOILUTSequence
        elif not isinstance(value, list) or not all(isinstance(item, FrameVOILUTSequenceItem) for item in value):
            raise ValueError("FrameVOILUTSequence must be a list of FrameVOILUTSequenceItem objects")
        else:
            self._FrameVOILUTSequence = value
            if "FrameVOILUTSequence" not in self._dataset:
                self._dataset.FrameVOILUTSequence = pydicom.Sequence()
            self._dataset.FrameVOILUTSequence.clear()
            self._dataset.FrameVOILUTSequence.extend([item.to_dataset() for item in value])

    def add_FrameVOILUT(self, item: FrameVOILUTSequenceItem):
        if not isinstance(item, FrameVOILUTSequenceItem):
            raise ValueError("Item must be an instance of FrameVOILUTSequenceItem")
        self._FrameVOILUTSequence.append(item)
        if "FrameVOILUTSequence" not in self._dataset:
            self._dataset.FrameVOILUTSequence = pydicom.Sequence()
        self._dataset.FrameVOILUTSequence.append(item.to_dataset())

    @property
    def PixelValueTransformationSequence(self) -> Optional[List[PixelValueTransformationSequenceItem]]:
        if "PixelValueTransformationSequence" in self._dataset:
            if len(self._PixelValueTransformationSequence) == len(self._dataset.PixelValueTransformationSequence):
                return self._PixelValueTransformationSequence
            else:
                return [PixelValueTransformationSequenceItem(x) for x in self._dataset.PixelValueTransformationSequence]
        return None

    @PixelValueTransformationSequence.setter
    def PixelValueTransformationSequence(self, value: Optional[List[PixelValueTransformationSequenceItem]]):
        if value is None:
            self._PixelValueTransformationSequence = []
            if "PixelValueTransformationSequence" in self._dataset:
                del self._dataset.PixelValueTransformationSequence
        elif not isinstance(value, list) or not all(isinstance(item, PixelValueTransformationSequenceItem) for item in value):
            raise ValueError("PixelValueTransformationSequence must be a list of PixelValueTransformationSequenceItem objects")
        else:
            self._PixelValueTransformationSequence = value
            if "PixelValueTransformationSequence" not in self._dataset:
                self._dataset.PixelValueTransformationSequence = pydicom.Sequence()
            self._dataset.PixelValueTransformationSequence.clear()
            self._dataset.PixelValueTransformationSequence.extend([item.to_dataset() for item in value])

    def add_PixelValueTransformation(self, item: PixelValueTransformationSequenceItem):
        if not isinstance(item, PixelValueTransformationSequenceItem):
            raise ValueError("Item must be an instance of PixelValueTransformationSequenceItem")
        self._PixelValueTransformationSequence.append(item)
        if "PixelValueTransformationSequence" not in self._dataset:
            self._dataset.PixelValueTransformationSequence = pydicom.Sequence()
        self._dataset.PixelValueTransformationSequence.append(item.to_dataset())

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
