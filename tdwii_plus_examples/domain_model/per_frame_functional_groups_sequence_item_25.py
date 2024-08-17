from typing import Any, List, Optional  # noqa

import pydicom

from .cardiac_synchronization_sequence_item import CardiacSynchronizationSequenceItem
from .contrast_bolus_usage_sequence_item import ContrastBolusUsageSequenceItem
from .derivation_image_sequence_item import DerivationImageSequenceItem
from .frame_content_sequence_item import FrameContentSequenceItem
from .frame_voilut_sequence_item import FrameVOILUTSequenceItem
from .pixel_measures_sequence_item import PixelMeasuresSequenceItem
from .plane_orientation_sequence_item import PlaneOrientationSequenceItem
from .plane_position_sequence_item import PlanePositionSequenceItem
from .real_world_value_mapping_sequence_item import RealWorldValueMappingSequenceItem
from .referenced_image_sequence_item import ReferencedImageSequenceItem
from .respiratory_synchronization_sequence_item import (
    RespiratorySynchronizationSequenceItem,
)
from .rt_beam_limiting_device_opening_sequence_item import (
    RTBeamLimitingDeviceOpeningSequenceItem,
)
from .rt_image_frame_context_sequence_item import RTImageFrameContextSequenceItem
from .rt_image_frame_general_content_sequence_item import (
    RTImageFrameGeneralContentSequenceItem,
)
from .rt_image_frame_imaging_device_position_sequence_item import (
    RTImageFrameImagingDevicePositionSequenceItem,
)
from .rt_image_frame_radiation_acquisition_sequence_item import (
    RTImageFrameRadiationAcquisitionSequenceItem,
)


class PerFrameFunctionalGroupsSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._ReferencedImageSequence: List[ReferencedImageSequenceItem] = []
        self._DerivationImageSequence: List[DerivationImageSequenceItem] = []
        self._CardiacSynchronizationSequence: List[CardiacSynchronizationSequenceItem] = []
        self._ContrastBolusUsageSequence: List[ContrastBolusUsageSequenceItem] = []
        self._FrameContentSequence: List[FrameContentSequenceItem] = []
        self._PlanePositionSequence: List[PlanePositionSequenceItem] = []
        self._PlaneOrientationSequence: List[PlaneOrientationSequenceItem] = []
        self._RespiratorySynchronizationSequence: List[RespiratorySynchronizationSequenceItem] = []
        self._PixelMeasuresSequence: List[PixelMeasuresSequenceItem] = []
        self._FrameVOILUTSequence: List[FrameVOILUTSequenceItem] = []
        self._RealWorldValueMappingSequence: List[RealWorldValueMappingSequenceItem] = []
        self._RTImageFrameGeneralContentSequence: List[RTImageFrameGeneralContentSequenceItem] = []
        self._RTImageFrameContextSequence: List[RTImageFrameContextSequenceItem] = []
        self._RTImageFrameImagingDevicePositionSequence: List[RTImageFrameImagingDevicePositionSequenceItem] = []
        self._RTImageFrameRadiationAcquisitionSequence: List[RTImageFrameRadiationAcquisitionSequenceItem] = []
        self._RTBeamLimitingDeviceOpeningSequence: List[RTBeamLimitingDeviceOpeningSequenceItem] = []

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
    def CardiacSynchronizationSequence(self) -> Optional[List[CardiacSynchronizationSequenceItem]]:
        if "CardiacSynchronizationSequence" in self._dataset:
            if len(self._CardiacSynchronizationSequence) == len(self._dataset.CardiacSynchronizationSequence):
                return self._CardiacSynchronizationSequence
            else:
                return [CardiacSynchronizationSequenceItem(x) for x in self._dataset.CardiacSynchronizationSequence]
        return None

    @CardiacSynchronizationSequence.setter
    def CardiacSynchronizationSequence(self, value: Optional[List[CardiacSynchronizationSequenceItem]]):
        if value is None:
            self._CardiacSynchronizationSequence = []
            if "CardiacSynchronizationSequence" in self._dataset:
                del self._dataset.CardiacSynchronizationSequence
        elif not isinstance(value, list) or not all(isinstance(item, CardiacSynchronizationSequenceItem) for item in value):
            raise ValueError("CardiacSynchronizationSequence must be a list of CardiacSynchronizationSequenceItem objects")
        else:
            self._CardiacSynchronizationSequence = value
            if "CardiacSynchronizationSequence" not in self._dataset:
                self._dataset.CardiacSynchronizationSequence = pydicom.Sequence()
            self._dataset.CardiacSynchronizationSequence.clear()
            self._dataset.CardiacSynchronizationSequence.extend([item.to_dataset() for item in value])

    def add_CardiacSynchronization(self, item: CardiacSynchronizationSequenceItem):
        if not isinstance(item, CardiacSynchronizationSequenceItem):
            raise ValueError("Item must be an instance of CardiacSynchronizationSequenceItem")
        self._CardiacSynchronizationSequence.append(item)
        if "CardiacSynchronizationSequence" not in self._dataset:
            self._dataset.CardiacSynchronizationSequence = pydicom.Sequence()
        self._dataset.CardiacSynchronizationSequence.append(item.to_dataset())

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
    def RespiratorySynchronizationSequence(self) -> Optional[List[RespiratorySynchronizationSequenceItem]]:
        if "RespiratorySynchronizationSequence" in self._dataset:
            if len(self._RespiratorySynchronizationSequence) == len(self._dataset.RespiratorySynchronizationSequence):
                return self._RespiratorySynchronizationSequence
            else:
                return [RespiratorySynchronizationSequenceItem(x) for x in self._dataset.RespiratorySynchronizationSequence]
        return None

    @RespiratorySynchronizationSequence.setter
    def RespiratorySynchronizationSequence(self, value: Optional[List[RespiratorySynchronizationSequenceItem]]):
        if value is None:
            self._RespiratorySynchronizationSequence = []
            if "RespiratorySynchronizationSequence" in self._dataset:
                del self._dataset.RespiratorySynchronizationSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, RespiratorySynchronizationSequenceItem) for item in value
        ):
            raise ValueError(
                "RespiratorySynchronizationSequence must be a list of RespiratorySynchronizationSequenceItem objects"
            )
        else:
            self._RespiratorySynchronizationSequence = value
            if "RespiratorySynchronizationSequence" not in self._dataset:
                self._dataset.RespiratorySynchronizationSequence = pydicom.Sequence()
            self._dataset.RespiratorySynchronizationSequence.clear()
            self._dataset.RespiratorySynchronizationSequence.extend([item.to_dataset() for item in value])

    def add_RespiratorySynchronization(self, item: RespiratorySynchronizationSequenceItem):
        if not isinstance(item, RespiratorySynchronizationSequenceItem):
            raise ValueError("Item must be an instance of RespiratorySynchronizationSequenceItem")
        self._RespiratorySynchronizationSequence.append(item)
        if "RespiratorySynchronizationSequence" not in self._dataset:
            self._dataset.RespiratorySynchronizationSequence = pydicom.Sequence()
        self._dataset.RespiratorySynchronizationSequence.append(item.to_dataset())

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
    def RTImageFrameGeneralContentSequence(self) -> Optional[List[RTImageFrameGeneralContentSequenceItem]]:
        if "RTImageFrameGeneralContentSequence" in self._dataset:
            if len(self._RTImageFrameGeneralContentSequence) == len(self._dataset.RTImageFrameGeneralContentSequence):
                return self._RTImageFrameGeneralContentSequence
            else:
                return [RTImageFrameGeneralContentSequenceItem(x) for x in self._dataset.RTImageFrameGeneralContentSequence]
        return None

    @RTImageFrameGeneralContentSequence.setter
    def RTImageFrameGeneralContentSequence(self, value: Optional[List[RTImageFrameGeneralContentSequenceItem]]):
        if value is None:
            self._RTImageFrameGeneralContentSequence = []
            if "RTImageFrameGeneralContentSequence" in self._dataset:
                del self._dataset.RTImageFrameGeneralContentSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, RTImageFrameGeneralContentSequenceItem) for item in value
        ):
            raise ValueError(
                "RTImageFrameGeneralContentSequence must be a list of RTImageFrameGeneralContentSequenceItem objects"
            )
        else:
            self._RTImageFrameGeneralContentSequence = value
            if "RTImageFrameGeneralContentSequence" not in self._dataset:
                self._dataset.RTImageFrameGeneralContentSequence = pydicom.Sequence()
            self._dataset.RTImageFrameGeneralContentSequence.clear()
            self._dataset.RTImageFrameGeneralContentSequence.extend([item.to_dataset() for item in value])

    def add_RTImageFrameGeneralContent(self, item: RTImageFrameGeneralContentSequenceItem):
        if not isinstance(item, RTImageFrameGeneralContentSequenceItem):
            raise ValueError("Item must be an instance of RTImageFrameGeneralContentSequenceItem")
        self._RTImageFrameGeneralContentSequence.append(item)
        if "RTImageFrameGeneralContentSequence" not in self._dataset:
            self._dataset.RTImageFrameGeneralContentSequence = pydicom.Sequence()
        self._dataset.RTImageFrameGeneralContentSequence.append(item.to_dataset())

    @property
    def RTImageFrameContextSequence(self) -> Optional[List[RTImageFrameContextSequenceItem]]:
        if "RTImageFrameContextSequence" in self._dataset:
            if len(self._RTImageFrameContextSequence) == len(self._dataset.RTImageFrameContextSequence):
                return self._RTImageFrameContextSequence
            else:
                return [RTImageFrameContextSequenceItem(x) for x in self._dataset.RTImageFrameContextSequence]
        return None

    @RTImageFrameContextSequence.setter
    def RTImageFrameContextSequence(self, value: Optional[List[RTImageFrameContextSequenceItem]]):
        if value is None:
            self._RTImageFrameContextSequence = []
            if "RTImageFrameContextSequence" in self._dataset:
                del self._dataset.RTImageFrameContextSequence
        elif not isinstance(value, list) or not all(isinstance(item, RTImageFrameContextSequenceItem) for item in value):
            raise ValueError("RTImageFrameContextSequence must be a list of RTImageFrameContextSequenceItem objects")
        else:
            self._RTImageFrameContextSequence = value
            if "RTImageFrameContextSequence" not in self._dataset:
                self._dataset.RTImageFrameContextSequence = pydicom.Sequence()
            self._dataset.RTImageFrameContextSequence.clear()
            self._dataset.RTImageFrameContextSequence.extend([item.to_dataset() for item in value])

    def add_RTImageFrameContext(self, item: RTImageFrameContextSequenceItem):
        if not isinstance(item, RTImageFrameContextSequenceItem):
            raise ValueError("Item must be an instance of RTImageFrameContextSequenceItem")
        self._RTImageFrameContextSequence.append(item)
        if "RTImageFrameContextSequence" not in self._dataset:
            self._dataset.RTImageFrameContextSequence = pydicom.Sequence()
        self._dataset.RTImageFrameContextSequence.append(item.to_dataset())

    @property
    def RTImageFrameImagingDevicePositionSequence(self) -> Optional[List[RTImageFrameImagingDevicePositionSequenceItem]]:
        if "RTImageFrameImagingDevicePositionSequence" in self._dataset:
            if len(self._RTImageFrameImagingDevicePositionSequence) == len(
                self._dataset.RTImageFrameImagingDevicePositionSequence
            ):
                return self._RTImageFrameImagingDevicePositionSequence
            else:
                return [
                    RTImageFrameImagingDevicePositionSequenceItem(x)
                    for x in self._dataset.RTImageFrameImagingDevicePositionSequence
                ]
        return None

    @RTImageFrameImagingDevicePositionSequence.setter
    def RTImageFrameImagingDevicePositionSequence(self, value: Optional[List[RTImageFrameImagingDevicePositionSequenceItem]]):
        if value is None:
            self._RTImageFrameImagingDevicePositionSequence = []
            if "RTImageFrameImagingDevicePositionSequence" in self._dataset:
                del self._dataset.RTImageFrameImagingDevicePositionSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, RTImageFrameImagingDevicePositionSequenceItem) for item in value
        ):
            raise ValueError(
                "RTImageFrameImagingDevicePositionSequence must be a list of RTImageFrameImagingDevicePositionSequenceItem"
                " objects"
            )
        else:
            self._RTImageFrameImagingDevicePositionSequence = value
            if "RTImageFrameImagingDevicePositionSequence" not in self._dataset:
                self._dataset.RTImageFrameImagingDevicePositionSequence = pydicom.Sequence()
            self._dataset.RTImageFrameImagingDevicePositionSequence.clear()
            self._dataset.RTImageFrameImagingDevicePositionSequence.extend([item.to_dataset() for item in value])

    def add_RTImageFrameImagingDevicePosition(self, item: RTImageFrameImagingDevicePositionSequenceItem):
        if not isinstance(item, RTImageFrameImagingDevicePositionSequenceItem):
            raise ValueError("Item must be an instance of RTImageFrameImagingDevicePositionSequenceItem")
        self._RTImageFrameImagingDevicePositionSequence.append(item)
        if "RTImageFrameImagingDevicePositionSequence" not in self._dataset:
            self._dataset.RTImageFrameImagingDevicePositionSequence = pydicom.Sequence()
        self._dataset.RTImageFrameImagingDevicePositionSequence.append(item.to_dataset())

    @property
    def RTImageFrameRadiationAcquisitionSequence(self) -> Optional[List[RTImageFrameRadiationAcquisitionSequenceItem]]:
        if "RTImageFrameRadiationAcquisitionSequence" in self._dataset:
            if len(self._RTImageFrameRadiationAcquisitionSequence) == len(
                self._dataset.RTImageFrameRadiationAcquisitionSequence
            ):
                return self._RTImageFrameRadiationAcquisitionSequence
            else:
                return [
                    RTImageFrameRadiationAcquisitionSequenceItem(x)
                    for x in self._dataset.RTImageFrameRadiationAcquisitionSequence
                ]
        return None

    @RTImageFrameRadiationAcquisitionSequence.setter
    def RTImageFrameRadiationAcquisitionSequence(self, value: Optional[List[RTImageFrameRadiationAcquisitionSequenceItem]]):
        if value is None:
            self._RTImageFrameRadiationAcquisitionSequence = []
            if "RTImageFrameRadiationAcquisitionSequence" in self._dataset:
                del self._dataset.RTImageFrameRadiationAcquisitionSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, RTImageFrameRadiationAcquisitionSequenceItem) for item in value
        ):
            raise ValueError(
                "RTImageFrameRadiationAcquisitionSequence must be a list of RTImageFrameRadiationAcquisitionSequenceItem"
                " objects"
            )
        else:
            self._RTImageFrameRadiationAcquisitionSequence = value
            if "RTImageFrameRadiationAcquisitionSequence" not in self._dataset:
                self._dataset.RTImageFrameRadiationAcquisitionSequence = pydicom.Sequence()
            self._dataset.RTImageFrameRadiationAcquisitionSequence.clear()
            self._dataset.RTImageFrameRadiationAcquisitionSequence.extend([item.to_dataset() for item in value])

    def add_RTImageFrameRadiationAcquisition(self, item: RTImageFrameRadiationAcquisitionSequenceItem):
        if not isinstance(item, RTImageFrameRadiationAcquisitionSequenceItem):
            raise ValueError("Item must be an instance of RTImageFrameRadiationAcquisitionSequenceItem")
        self._RTImageFrameRadiationAcquisitionSequence.append(item)
        if "RTImageFrameRadiationAcquisitionSequence" not in self._dataset:
            self._dataset.RTImageFrameRadiationAcquisitionSequence = pydicom.Sequence()
        self._dataset.RTImageFrameRadiationAcquisitionSequence.append(item.to_dataset())

    @property
    def RTBeamLimitingDeviceOpeningSequence(self) -> Optional[List[RTBeamLimitingDeviceOpeningSequenceItem]]:
        if "RTBeamLimitingDeviceOpeningSequence" in self._dataset:
            if len(self._RTBeamLimitingDeviceOpeningSequence) == len(self._dataset.RTBeamLimitingDeviceOpeningSequence):
                return self._RTBeamLimitingDeviceOpeningSequence
            else:
                return [RTBeamLimitingDeviceOpeningSequenceItem(x) for x in self._dataset.RTBeamLimitingDeviceOpeningSequence]
        return None

    @RTBeamLimitingDeviceOpeningSequence.setter
    def RTBeamLimitingDeviceOpeningSequence(self, value: Optional[List[RTBeamLimitingDeviceOpeningSequenceItem]]):
        if value is None:
            self._RTBeamLimitingDeviceOpeningSequence = []
            if "RTBeamLimitingDeviceOpeningSequence" in self._dataset:
                del self._dataset.RTBeamLimitingDeviceOpeningSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, RTBeamLimitingDeviceOpeningSequenceItem) for item in value
        ):
            raise ValueError(
                "RTBeamLimitingDeviceOpeningSequence must be a list of RTBeamLimitingDeviceOpeningSequenceItem objects"
            )
        else:
            self._RTBeamLimitingDeviceOpeningSequence = value
            if "RTBeamLimitingDeviceOpeningSequence" not in self._dataset:
                self._dataset.RTBeamLimitingDeviceOpeningSequence = pydicom.Sequence()
            self._dataset.RTBeamLimitingDeviceOpeningSequence.clear()
            self._dataset.RTBeamLimitingDeviceOpeningSequence.extend([item.to_dataset() for item in value])

    def add_RTBeamLimitingDeviceOpening(self, item: RTBeamLimitingDeviceOpeningSequenceItem):
        if not isinstance(item, RTBeamLimitingDeviceOpeningSequenceItem):
            raise ValueError("Item must be an instance of RTBeamLimitingDeviceOpeningSequenceItem")
        self._RTBeamLimitingDeviceOpeningSequence.append(item)
        if "RTBeamLimitingDeviceOpeningSequence" not in self._dataset:
            self._dataset.RTBeamLimitingDeviceOpeningSequence = pydicom.Sequence()
        self._dataset.RTBeamLimitingDeviceOpeningSequence.append(item.to_dataset())
