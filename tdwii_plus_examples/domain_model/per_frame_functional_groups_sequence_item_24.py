from typing import Any, List, Optional

import pydicom

from .cardiac_synchronization_sequence_item import CardiacSynchronizationSequenceItem
from .contrast_bolus_usage_sequence_item import ContrastBolusUsageSequenceItem
from .derivation_image_sequence_item import DerivationImageSequenceItem
from .frame_anatomy_sequence_item import FrameAnatomySequenceItem
from .frame_content_sequence_item import FrameContentSequenceItem
from .mr_averages_sequence_item import MRAveragesSequenceItem
from .mr_diffusion_sequence_item import MRDiffusionSequenceItem
from .mr_echo_sequence_item import MREchoSequenceItem
from .mr_modifier_sequence_item import MRModifierSequenceItem
from .mr_receive_coil_sequence_item import MRReceiveCoilSequenceItem
from .mr_spatial_saturation_sequence_item import MRSpatialSaturationSequenceItem
from .mr_spectroscopy_fov_geometry_sequence_item import (
    MRSpectroscopyFOVGeometrySequenceItem,
)
from .mr_spectroscopy_frame_type_sequence_item import (
    MRSpectroscopyFrameTypeSequenceItem,
)
from .mr_timing_and_related_parameters_sequence_item import (
    MRTimingAndRelatedParametersSequenceItem,
)
from .mr_transmit_coil_sequence_item import MRTransmitCoilSequenceItem
from .mr_velocity_encoding_sequence_item import MRVelocityEncodingSequenceItem
from .pixel_measures_sequence_item import PixelMeasuresSequenceItem
from .plane_orientation_sequence_item import PlaneOrientationSequenceItem
from .plane_position_sequence_item import PlanePositionSequenceItem
from .referenced_image_sequence_item import ReferencedImageSequenceItem
from .respiratory_synchronization_sequence_item import (
    RespiratorySynchronizationSequenceItem,
)
from .temporal_position_sequence_item import TemporalPositionSequenceItem


class PerFrameFunctionalGroupsSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._ReferencedImageSequence: List[ReferencedImageSequenceItem] = []
        self._DerivationImageSequence: List[DerivationImageSequenceItem] = []
        self._MRReceiveCoilSequence: List[MRReceiveCoilSequenceItem] = []
        self._MRTransmitCoilSequence: List[MRTransmitCoilSequenceItem] = []
        self._MRSpectroscopyFOVGeometrySequence: List[MRSpectroscopyFOVGeometrySequenceItem] = []
        self._MRSpatialSaturationSequence: List[MRSpatialSaturationSequenceItem] = []
        self._MRTimingAndRelatedParametersSequence: List[MRTimingAndRelatedParametersSequenceItem] = []
        self._MREchoSequence: List[MREchoSequenceItem] = []
        self._MRModifierSequence: List[MRModifierSequenceItem] = []
        self._MRDiffusionSequence: List[MRDiffusionSequenceItem] = []
        self._CardiacSynchronizationSequence: List[CardiacSynchronizationSequenceItem] = []
        self._MRAveragesSequence: List[MRAveragesSequenceItem] = []
        self._MRVelocityEncodingSequence: List[MRVelocityEncodingSequenceItem] = []
        self._MRSpectroscopyFrameTypeSequence: List[MRSpectroscopyFrameTypeSequenceItem] = []
        self._ContrastBolusUsageSequence: List[ContrastBolusUsageSequenceItem] = []
        self._FrameAnatomySequence: List[FrameAnatomySequenceItem] = []
        self._FrameContentSequence: List[FrameContentSequenceItem] = []
        self._PlanePositionSequence: List[PlanePositionSequenceItem] = []
        self._PlaneOrientationSequence: List[PlaneOrientationSequenceItem] = []
        self._RespiratorySynchronizationSequence: List[RespiratorySynchronizationSequenceItem] = []
        self._TemporalPositionSequence: List[TemporalPositionSequenceItem] = []
        self._PixelMeasuresSequence: List[PixelMeasuresSequenceItem] = []

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
            raise ValueError(f"DerivationImageSequence must be a list of DerivationImageSequenceItem objects")
        else:
            self._DerivationImageSequence = value
            if "DerivationImageSequence" not in self._dataset:
                self._dataset.DerivationImageSequence = pydicom.Sequence()
            self._dataset.DerivationImageSequence.clear()
            self._dataset.DerivationImageSequence.extend([item.to_dataset() for item in value])

    def add_DerivationImage(self, item: DerivationImageSequenceItem):
        if not isinstance(item, DerivationImageSequenceItem):
            raise ValueError(f"Item must be an instance of DerivationImageSequenceItem")
        self._DerivationImageSequence.append(item)
        if "DerivationImageSequence" not in self._dataset:
            self._dataset.DerivationImageSequence = pydicom.Sequence()
        self._dataset.DerivationImageSequence.append(item.to_dataset())

    @property
    def MRReceiveCoilSequence(self) -> Optional[List[MRReceiveCoilSequenceItem]]:
        if "MRReceiveCoilSequence" in self._dataset:
            if len(self._MRReceiveCoilSequence) == len(self._dataset.MRReceiveCoilSequence):
                return self._MRReceiveCoilSequence
            else:
                return [MRReceiveCoilSequenceItem(x) for x in self._dataset.MRReceiveCoilSequence]
        return None

    @MRReceiveCoilSequence.setter
    def MRReceiveCoilSequence(self, value: Optional[List[MRReceiveCoilSequenceItem]]):
        if value is None:
            self._MRReceiveCoilSequence = []
            if "MRReceiveCoilSequence" in self._dataset:
                del self._dataset.MRReceiveCoilSequence
        elif not isinstance(value, list) or not all(isinstance(item, MRReceiveCoilSequenceItem) for item in value):
            raise ValueError(f"MRReceiveCoilSequence must be a list of MRReceiveCoilSequenceItem objects")
        else:
            self._MRReceiveCoilSequence = value
            if "MRReceiveCoilSequence" not in self._dataset:
                self._dataset.MRReceiveCoilSequence = pydicom.Sequence()
            self._dataset.MRReceiveCoilSequence.clear()
            self._dataset.MRReceiveCoilSequence.extend([item.to_dataset() for item in value])

    def add_MRReceiveCoil(self, item: MRReceiveCoilSequenceItem):
        if not isinstance(item, MRReceiveCoilSequenceItem):
            raise ValueError(f"Item must be an instance of MRReceiveCoilSequenceItem")
        self._MRReceiveCoilSequence.append(item)
        if "MRReceiveCoilSequence" not in self._dataset:
            self._dataset.MRReceiveCoilSequence = pydicom.Sequence()
        self._dataset.MRReceiveCoilSequence.append(item.to_dataset())

    @property
    def MRTransmitCoilSequence(self) -> Optional[List[MRTransmitCoilSequenceItem]]:
        if "MRTransmitCoilSequence" in self._dataset:
            if len(self._MRTransmitCoilSequence) == len(self._dataset.MRTransmitCoilSequence):
                return self._MRTransmitCoilSequence
            else:
                return [MRTransmitCoilSequenceItem(x) for x in self._dataset.MRTransmitCoilSequence]
        return None

    @MRTransmitCoilSequence.setter
    def MRTransmitCoilSequence(self, value: Optional[List[MRTransmitCoilSequenceItem]]):
        if value is None:
            self._MRTransmitCoilSequence = []
            if "MRTransmitCoilSequence" in self._dataset:
                del self._dataset.MRTransmitCoilSequence
        elif not isinstance(value, list) or not all(isinstance(item, MRTransmitCoilSequenceItem) for item in value):
            raise ValueError(f"MRTransmitCoilSequence must be a list of MRTransmitCoilSequenceItem objects")
        else:
            self._MRTransmitCoilSequence = value
            if "MRTransmitCoilSequence" not in self._dataset:
                self._dataset.MRTransmitCoilSequence = pydicom.Sequence()
            self._dataset.MRTransmitCoilSequence.clear()
            self._dataset.MRTransmitCoilSequence.extend([item.to_dataset() for item in value])

    def add_MRTransmitCoil(self, item: MRTransmitCoilSequenceItem):
        if not isinstance(item, MRTransmitCoilSequenceItem):
            raise ValueError(f"Item must be an instance of MRTransmitCoilSequenceItem")
        self._MRTransmitCoilSequence.append(item)
        if "MRTransmitCoilSequence" not in self._dataset:
            self._dataset.MRTransmitCoilSequence = pydicom.Sequence()
        self._dataset.MRTransmitCoilSequence.append(item.to_dataset())

    @property
    def MRSpectroscopyFOVGeometrySequence(self) -> Optional[List[MRSpectroscopyFOVGeometrySequenceItem]]:
        if "MRSpectroscopyFOVGeometrySequence" in self._dataset:
            if len(self._MRSpectroscopyFOVGeometrySequence) == len(self._dataset.MRSpectroscopyFOVGeometrySequence):
                return self._MRSpectroscopyFOVGeometrySequence
            else:
                return [MRSpectroscopyFOVGeometrySequenceItem(x) for x in self._dataset.MRSpectroscopyFOVGeometrySequence]
        return None

    @MRSpectroscopyFOVGeometrySequence.setter
    def MRSpectroscopyFOVGeometrySequence(self, value: Optional[List[MRSpectroscopyFOVGeometrySequenceItem]]):
        if value is None:
            self._MRSpectroscopyFOVGeometrySequence = []
            if "MRSpectroscopyFOVGeometrySequence" in self._dataset:
                del self._dataset.MRSpectroscopyFOVGeometrySequence
        elif not isinstance(value, list) or not all(isinstance(item, MRSpectroscopyFOVGeometrySequenceItem) for item in value):
            raise ValueError(
                f"MRSpectroscopyFOVGeometrySequence must be a list of MRSpectroscopyFOVGeometrySequenceItem objects"
            )
        else:
            self._MRSpectroscopyFOVGeometrySequence = value
            if "MRSpectroscopyFOVGeometrySequence" not in self._dataset:
                self._dataset.MRSpectroscopyFOVGeometrySequence = pydicom.Sequence()
            self._dataset.MRSpectroscopyFOVGeometrySequence.clear()
            self._dataset.MRSpectroscopyFOVGeometrySequence.extend([item.to_dataset() for item in value])

    def add_MRSpectroscopyFOVGeometry(self, item: MRSpectroscopyFOVGeometrySequenceItem):
        if not isinstance(item, MRSpectroscopyFOVGeometrySequenceItem):
            raise ValueError(f"Item must be an instance of MRSpectroscopyFOVGeometrySequenceItem")
        self._MRSpectroscopyFOVGeometrySequence.append(item)
        if "MRSpectroscopyFOVGeometrySequence" not in self._dataset:
            self._dataset.MRSpectroscopyFOVGeometrySequence = pydicom.Sequence()
        self._dataset.MRSpectroscopyFOVGeometrySequence.append(item.to_dataset())

    @property
    def MRSpatialSaturationSequence(self) -> Optional[List[MRSpatialSaturationSequenceItem]]:
        if "MRSpatialSaturationSequence" in self._dataset:
            if len(self._MRSpatialSaturationSequence) == len(self._dataset.MRSpatialSaturationSequence):
                return self._MRSpatialSaturationSequence
            else:
                return [MRSpatialSaturationSequenceItem(x) for x in self._dataset.MRSpatialSaturationSequence]
        return None

    @MRSpatialSaturationSequence.setter
    def MRSpatialSaturationSequence(self, value: Optional[List[MRSpatialSaturationSequenceItem]]):
        if value is None:
            self._MRSpatialSaturationSequence = []
            if "MRSpatialSaturationSequence" in self._dataset:
                del self._dataset.MRSpatialSaturationSequence
        elif not isinstance(value, list) or not all(isinstance(item, MRSpatialSaturationSequenceItem) for item in value):
            raise ValueError(f"MRSpatialSaturationSequence must be a list of MRSpatialSaturationSequenceItem objects")
        else:
            self._MRSpatialSaturationSequence = value
            if "MRSpatialSaturationSequence" not in self._dataset:
                self._dataset.MRSpatialSaturationSequence = pydicom.Sequence()
            self._dataset.MRSpatialSaturationSequence.clear()
            self._dataset.MRSpatialSaturationSequence.extend([item.to_dataset() for item in value])

    def add_MRSpatialSaturation(self, item: MRSpatialSaturationSequenceItem):
        if not isinstance(item, MRSpatialSaturationSequenceItem):
            raise ValueError(f"Item must be an instance of MRSpatialSaturationSequenceItem")
        self._MRSpatialSaturationSequence.append(item)
        if "MRSpatialSaturationSequence" not in self._dataset:
            self._dataset.MRSpatialSaturationSequence = pydicom.Sequence()
        self._dataset.MRSpatialSaturationSequence.append(item.to_dataset())

    @property
    def MRTimingAndRelatedParametersSequence(self) -> Optional[List[MRTimingAndRelatedParametersSequenceItem]]:
        if "MRTimingAndRelatedParametersSequence" in self._dataset:
            if len(self._MRTimingAndRelatedParametersSequence) == len(self._dataset.MRTimingAndRelatedParametersSequence):
                return self._MRTimingAndRelatedParametersSequence
            else:
                return [
                    MRTimingAndRelatedParametersSequenceItem(x) for x in self._dataset.MRTimingAndRelatedParametersSequence
                ]
        return None

    @MRTimingAndRelatedParametersSequence.setter
    def MRTimingAndRelatedParametersSequence(self, value: Optional[List[MRTimingAndRelatedParametersSequenceItem]]):
        if value is None:
            self._MRTimingAndRelatedParametersSequence = []
            if "MRTimingAndRelatedParametersSequence" in self._dataset:
                del self._dataset.MRTimingAndRelatedParametersSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, MRTimingAndRelatedParametersSequenceItem) for item in value
        ):
            raise ValueError(
                f"MRTimingAndRelatedParametersSequence must be a list of MRTimingAndRelatedParametersSequenceItem objects"
            )
        else:
            self._MRTimingAndRelatedParametersSequence = value
            if "MRTimingAndRelatedParametersSequence" not in self._dataset:
                self._dataset.MRTimingAndRelatedParametersSequence = pydicom.Sequence()
            self._dataset.MRTimingAndRelatedParametersSequence.clear()
            self._dataset.MRTimingAndRelatedParametersSequence.extend([item.to_dataset() for item in value])

    def add_MRTimingAndRelatedParameters(self, item: MRTimingAndRelatedParametersSequenceItem):
        if not isinstance(item, MRTimingAndRelatedParametersSequenceItem):
            raise ValueError(f"Item must be an instance of MRTimingAndRelatedParametersSequenceItem")
        self._MRTimingAndRelatedParametersSequence.append(item)
        if "MRTimingAndRelatedParametersSequence" not in self._dataset:
            self._dataset.MRTimingAndRelatedParametersSequence = pydicom.Sequence()
        self._dataset.MRTimingAndRelatedParametersSequence.append(item.to_dataset())

    @property
    def MREchoSequence(self) -> Optional[List[MREchoSequenceItem]]:
        if "MREchoSequence" in self._dataset:
            if len(self._MREchoSequence) == len(self._dataset.MREchoSequence):
                return self._MREchoSequence
            else:
                return [MREchoSequenceItem(x) for x in self._dataset.MREchoSequence]
        return None

    @MREchoSequence.setter
    def MREchoSequence(self, value: Optional[List[MREchoSequenceItem]]):
        if value is None:
            self._MREchoSequence = []
            if "MREchoSequence" in self._dataset:
                del self._dataset.MREchoSequence
        elif not isinstance(value, list) or not all(isinstance(item, MREchoSequenceItem) for item in value):
            raise ValueError(f"MREchoSequence must be a list of MREchoSequenceItem objects")
        else:
            self._MREchoSequence = value
            if "MREchoSequence" not in self._dataset:
                self._dataset.MREchoSequence = pydicom.Sequence()
            self._dataset.MREchoSequence.clear()
            self._dataset.MREchoSequence.extend([item.to_dataset() for item in value])

    def add_MREcho(self, item: MREchoSequenceItem):
        if not isinstance(item, MREchoSequenceItem):
            raise ValueError(f"Item must be an instance of MREchoSequenceItem")
        self._MREchoSequence.append(item)
        if "MREchoSequence" not in self._dataset:
            self._dataset.MREchoSequence = pydicom.Sequence()
        self._dataset.MREchoSequence.append(item.to_dataset())

    @property
    def MRModifierSequence(self) -> Optional[List[MRModifierSequenceItem]]:
        if "MRModifierSequence" in self._dataset:
            if len(self._MRModifierSequence) == len(self._dataset.MRModifierSequence):
                return self._MRModifierSequence
            else:
                return [MRModifierSequenceItem(x) for x in self._dataset.MRModifierSequence]
        return None

    @MRModifierSequence.setter
    def MRModifierSequence(self, value: Optional[List[MRModifierSequenceItem]]):
        if value is None:
            self._MRModifierSequence = []
            if "MRModifierSequence" in self._dataset:
                del self._dataset.MRModifierSequence
        elif not isinstance(value, list) or not all(isinstance(item, MRModifierSequenceItem) for item in value):
            raise ValueError(f"MRModifierSequence must be a list of MRModifierSequenceItem objects")
        else:
            self._MRModifierSequence = value
            if "MRModifierSequence" not in self._dataset:
                self._dataset.MRModifierSequence = pydicom.Sequence()
            self._dataset.MRModifierSequence.clear()
            self._dataset.MRModifierSequence.extend([item.to_dataset() for item in value])

    def add_MRModifier(self, item: MRModifierSequenceItem):
        if not isinstance(item, MRModifierSequenceItem):
            raise ValueError(f"Item must be an instance of MRModifierSequenceItem")
        self._MRModifierSequence.append(item)
        if "MRModifierSequence" not in self._dataset:
            self._dataset.MRModifierSequence = pydicom.Sequence()
        self._dataset.MRModifierSequence.append(item.to_dataset())

    @property
    def MRDiffusionSequence(self) -> Optional[List[MRDiffusionSequenceItem]]:
        if "MRDiffusionSequence" in self._dataset:
            if len(self._MRDiffusionSequence) == len(self._dataset.MRDiffusionSequence):
                return self._MRDiffusionSequence
            else:
                return [MRDiffusionSequenceItem(x) for x in self._dataset.MRDiffusionSequence]
        return None

    @MRDiffusionSequence.setter
    def MRDiffusionSequence(self, value: Optional[List[MRDiffusionSequenceItem]]):
        if value is None:
            self._MRDiffusionSequence = []
            if "MRDiffusionSequence" in self._dataset:
                del self._dataset.MRDiffusionSequence
        elif not isinstance(value, list) or not all(isinstance(item, MRDiffusionSequenceItem) for item in value):
            raise ValueError(f"MRDiffusionSequence must be a list of MRDiffusionSequenceItem objects")
        else:
            self._MRDiffusionSequence = value
            if "MRDiffusionSequence" not in self._dataset:
                self._dataset.MRDiffusionSequence = pydicom.Sequence()
            self._dataset.MRDiffusionSequence.clear()
            self._dataset.MRDiffusionSequence.extend([item.to_dataset() for item in value])

    def add_MRDiffusion(self, item: MRDiffusionSequenceItem):
        if not isinstance(item, MRDiffusionSequenceItem):
            raise ValueError(f"Item must be an instance of MRDiffusionSequenceItem")
        self._MRDiffusionSequence.append(item)
        if "MRDiffusionSequence" not in self._dataset:
            self._dataset.MRDiffusionSequence = pydicom.Sequence()
        self._dataset.MRDiffusionSequence.append(item.to_dataset())

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
            raise ValueError(f"CardiacSynchronizationSequence must be a list of CardiacSynchronizationSequenceItem objects")
        else:
            self._CardiacSynchronizationSequence = value
            if "CardiacSynchronizationSequence" not in self._dataset:
                self._dataset.CardiacSynchronizationSequence = pydicom.Sequence()
            self._dataset.CardiacSynchronizationSequence.clear()
            self._dataset.CardiacSynchronizationSequence.extend([item.to_dataset() for item in value])

    def add_CardiacSynchronization(self, item: CardiacSynchronizationSequenceItem):
        if not isinstance(item, CardiacSynchronizationSequenceItem):
            raise ValueError(f"Item must be an instance of CardiacSynchronizationSequenceItem")
        self._CardiacSynchronizationSequence.append(item)
        if "CardiacSynchronizationSequence" not in self._dataset:
            self._dataset.CardiacSynchronizationSequence = pydicom.Sequence()
        self._dataset.CardiacSynchronizationSequence.append(item.to_dataset())

    @property
    def MRAveragesSequence(self) -> Optional[List[MRAveragesSequenceItem]]:
        if "MRAveragesSequence" in self._dataset:
            if len(self._MRAveragesSequence) == len(self._dataset.MRAveragesSequence):
                return self._MRAveragesSequence
            else:
                return [MRAveragesSequenceItem(x) for x in self._dataset.MRAveragesSequence]
        return None

    @MRAveragesSequence.setter
    def MRAveragesSequence(self, value: Optional[List[MRAveragesSequenceItem]]):
        if value is None:
            self._MRAveragesSequence = []
            if "MRAveragesSequence" in self._dataset:
                del self._dataset.MRAveragesSequence
        elif not isinstance(value, list) or not all(isinstance(item, MRAveragesSequenceItem) for item in value):
            raise ValueError(f"MRAveragesSequence must be a list of MRAveragesSequenceItem objects")
        else:
            self._MRAveragesSequence = value
            if "MRAveragesSequence" not in self._dataset:
                self._dataset.MRAveragesSequence = pydicom.Sequence()
            self._dataset.MRAveragesSequence.clear()
            self._dataset.MRAveragesSequence.extend([item.to_dataset() for item in value])

    def add_MRAverages(self, item: MRAveragesSequenceItem):
        if not isinstance(item, MRAveragesSequenceItem):
            raise ValueError(f"Item must be an instance of MRAveragesSequenceItem")
        self._MRAveragesSequence.append(item)
        if "MRAveragesSequence" not in self._dataset:
            self._dataset.MRAveragesSequence = pydicom.Sequence()
        self._dataset.MRAveragesSequence.append(item.to_dataset())

    @property
    def MRVelocityEncodingSequence(self) -> Optional[List[MRVelocityEncodingSequenceItem]]:
        if "MRVelocityEncodingSequence" in self._dataset:
            if len(self._MRVelocityEncodingSequence) == len(self._dataset.MRVelocityEncodingSequence):
                return self._MRVelocityEncodingSequence
            else:
                return [MRVelocityEncodingSequenceItem(x) for x in self._dataset.MRVelocityEncodingSequence]
        return None

    @MRVelocityEncodingSequence.setter
    def MRVelocityEncodingSequence(self, value: Optional[List[MRVelocityEncodingSequenceItem]]):
        if value is None:
            self._MRVelocityEncodingSequence = []
            if "MRVelocityEncodingSequence" in self._dataset:
                del self._dataset.MRVelocityEncodingSequence
        elif not isinstance(value, list) or not all(isinstance(item, MRVelocityEncodingSequenceItem) for item in value):
            raise ValueError(f"MRVelocityEncodingSequence must be a list of MRVelocityEncodingSequenceItem objects")
        else:
            self._MRVelocityEncodingSequence = value
            if "MRVelocityEncodingSequence" not in self._dataset:
                self._dataset.MRVelocityEncodingSequence = pydicom.Sequence()
            self._dataset.MRVelocityEncodingSequence.clear()
            self._dataset.MRVelocityEncodingSequence.extend([item.to_dataset() for item in value])

    def add_MRVelocityEncoding(self, item: MRVelocityEncodingSequenceItem):
        if not isinstance(item, MRVelocityEncodingSequenceItem):
            raise ValueError(f"Item must be an instance of MRVelocityEncodingSequenceItem")
        self._MRVelocityEncodingSequence.append(item)
        if "MRVelocityEncodingSequence" not in self._dataset:
            self._dataset.MRVelocityEncodingSequence = pydicom.Sequence()
        self._dataset.MRVelocityEncodingSequence.append(item.to_dataset())

    @property
    def MRSpectroscopyFrameTypeSequence(self) -> Optional[List[MRSpectroscopyFrameTypeSequenceItem]]:
        if "MRSpectroscopyFrameTypeSequence" in self._dataset:
            if len(self._MRSpectroscopyFrameTypeSequence) == len(self._dataset.MRSpectroscopyFrameTypeSequence):
                return self._MRSpectroscopyFrameTypeSequence
            else:
                return [MRSpectroscopyFrameTypeSequenceItem(x) for x in self._dataset.MRSpectroscopyFrameTypeSequence]
        return None

    @MRSpectroscopyFrameTypeSequence.setter
    def MRSpectroscopyFrameTypeSequence(self, value: Optional[List[MRSpectroscopyFrameTypeSequenceItem]]):
        if value is None:
            self._MRSpectroscopyFrameTypeSequence = []
            if "MRSpectroscopyFrameTypeSequence" in self._dataset:
                del self._dataset.MRSpectroscopyFrameTypeSequence
        elif not isinstance(value, list) or not all(isinstance(item, MRSpectroscopyFrameTypeSequenceItem) for item in value):
            raise ValueError(f"MRSpectroscopyFrameTypeSequence must be a list of MRSpectroscopyFrameTypeSequenceItem objects")
        else:
            self._MRSpectroscopyFrameTypeSequence = value
            if "MRSpectroscopyFrameTypeSequence" not in self._dataset:
                self._dataset.MRSpectroscopyFrameTypeSequence = pydicom.Sequence()
            self._dataset.MRSpectroscopyFrameTypeSequence.clear()
            self._dataset.MRSpectroscopyFrameTypeSequence.extend([item.to_dataset() for item in value])

    def add_MRSpectroscopyFrameType(self, item: MRSpectroscopyFrameTypeSequenceItem):
        if not isinstance(item, MRSpectroscopyFrameTypeSequenceItem):
            raise ValueError(f"Item must be an instance of MRSpectroscopyFrameTypeSequenceItem")
        self._MRSpectroscopyFrameTypeSequence.append(item)
        if "MRSpectroscopyFrameTypeSequence" not in self._dataset:
            self._dataset.MRSpectroscopyFrameTypeSequence = pydicom.Sequence()
        self._dataset.MRSpectroscopyFrameTypeSequence.append(item.to_dataset())

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
            raise ValueError(f"ContrastBolusUsageSequence must be a list of ContrastBolusUsageSequenceItem objects")
        else:
            self._ContrastBolusUsageSequence = value
            if "ContrastBolusUsageSequence" not in self._dataset:
                self._dataset.ContrastBolusUsageSequence = pydicom.Sequence()
            self._dataset.ContrastBolusUsageSequence.clear()
            self._dataset.ContrastBolusUsageSequence.extend([item.to_dataset() for item in value])

    def add_ContrastBolusUsage(self, item: ContrastBolusUsageSequenceItem):
        if not isinstance(item, ContrastBolusUsageSequenceItem):
            raise ValueError(f"Item must be an instance of ContrastBolusUsageSequenceItem")
        self._ContrastBolusUsageSequence.append(item)
        if "ContrastBolusUsageSequence" not in self._dataset:
            self._dataset.ContrastBolusUsageSequence = pydicom.Sequence()
        self._dataset.ContrastBolusUsageSequence.append(item.to_dataset())

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
            raise ValueError(f"FrameAnatomySequence must be a list of FrameAnatomySequenceItem objects")
        else:
            self._FrameAnatomySequence = value
            if "FrameAnatomySequence" not in self._dataset:
                self._dataset.FrameAnatomySequence = pydicom.Sequence()
            self._dataset.FrameAnatomySequence.clear()
            self._dataset.FrameAnatomySequence.extend([item.to_dataset() for item in value])

    def add_FrameAnatomy(self, item: FrameAnatomySequenceItem):
        if not isinstance(item, FrameAnatomySequenceItem):
            raise ValueError(f"Item must be an instance of FrameAnatomySequenceItem")
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
            raise ValueError(f"FrameContentSequence must be a list of FrameContentSequenceItem objects")
        else:
            self._FrameContentSequence = value
            if "FrameContentSequence" not in self._dataset:
                self._dataset.FrameContentSequence = pydicom.Sequence()
            self._dataset.FrameContentSequence.clear()
            self._dataset.FrameContentSequence.extend([item.to_dataset() for item in value])

    def add_FrameContent(self, item: FrameContentSequenceItem):
        if not isinstance(item, FrameContentSequenceItem):
            raise ValueError(f"Item must be an instance of FrameContentSequenceItem")
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
            raise ValueError(f"PlanePositionSequence must be a list of PlanePositionSequenceItem objects")
        else:
            self._PlanePositionSequence = value
            if "PlanePositionSequence" not in self._dataset:
                self._dataset.PlanePositionSequence = pydicom.Sequence()
            self._dataset.PlanePositionSequence.clear()
            self._dataset.PlanePositionSequence.extend([item.to_dataset() for item in value])

    def add_PlanePosition(self, item: PlanePositionSequenceItem):
        if not isinstance(item, PlanePositionSequenceItem):
            raise ValueError(f"Item must be an instance of PlanePositionSequenceItem")
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
            raise ValueError(f"PlaneOrientationSequence must be a list of PlaneOrientationSequenceItem objects")
        else:
            self._PlaneOrientationSequence = value
            if "PlaneOrientationSequence" not in self._dataset:
                self._dataset.PlaneOrientationSequence = pydicom.Sequence()
            self._dataset.PlaneOrientationSequence.clear()
            self._dataset.PlaneOrientationSequence.extend([item.to_dataset() for item in value])

    def add_PlaneOrientation(self, item: PlaneOrientationSequenceItem):
        if not isinstance(item, PlaneOrientationSequenceItem):
            raise ValueError(f"Item must be an instance of PlaneOrientationSequenceItem")
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
                f"RespiratorySynchronizationSequence must be a list of RespiratorySynchronizationSequenceItem objects"
            )
        else:
            self._RespiratorySynchronizationSequence = value
            if "RespiratorySynchronizationSequence" not in self._dataset:
                self._dataset.RespiratorySynchronizationSequence = pydicom.Sequence()
            self._dataset.RespiratorySynchronizationSequence.clear()
            self._dataset.RespiratorySynchronizationSequence.extend([item.to_dataset() for item in value])

    def add_RespiratorySynchronization(self, item: RespiratorySynchronizationSequenceItem):
        if not isinstance(item, RespiratorySynchronizationSequenceItem):
            raise ValueError(f"Item must be an instance of RespiratorySynchronizationSequenceItem")
        self._RespiratorySynchronizationSequence.append(item)
        if "RespiratorySynchronizationSequence" not in self._dataset:
            self._dataset.RespiratorySynchronizationSequence = pydicom.Sequence()
        self._dataset.RespiratorySynchronizationSequence.append(item.to_dataset())

    @property
    def TemporalPositionSequence(self) -> Optional[List[TemporalPositionSequenceItem]]:
        if "TemporalPositionSequence" in self._dataset:
            if len(self._TemporalPositionSequence) == len(self._dataset.TemporalPositionSequence):
                return self._TemporalPositionSequence
            else:
                return [TemporalPositionSequenceItem(x) for x in self._dataset.TemporalPositionSequence]
        return None

    @TemporalPositionSequence.setter
    def TemporalPositionSequence(self, value: Optional[List[TemporalPositionSequenceItem]]):
        if value is None:
            self._TemporalPositionSequence = []
            if "TemporalPositionSequence" in self._dataset:
                del self._dataset.TemporalPositionSequence
        elif not isinstance(value, list) or not all(isinstance(item, TemporalPositionSequenceItem) for item in value):
            raise ValueError(f"TemporalPositionSequence must be a list of TemporalPositionSequenceItem objects")
        else:
            self._TemporalPositionSequence = value
            if "TemporalPositionSequence" not in self._dataset:
                self._dataset.TemporalPositionSequence = pydicom.Sequence()
            self._dataset.TemporalPositionSequence.clear()
            self._dataset.TemporalPositionSequence.extend([item.to_dataset() for item in value])

    def add_TemporalPosition(self, item: TemporalPositionSequenceItem):
        if not isinstance(item, TemporalPositionSequenceItem):
            raise ValueError(f"Item must be an instance of TemporalPositionSequenceItem")
        self._TemporalPositionSequence.append(item)
        if "TemporalPositionSequence" not in self._dataset:
            self._dataset.TemporalPositionSequence = pydicom.Sequence()
        self._dataset.TemporalPositionSequence.append(item.to_dataset())

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
            raise ValueError(f"PixelMeasuresSequence must be a list of PixelMeasuresSequenceItem objects")
        else:
            self._PixelMeasuresSequence = value
            if "PixelMeasuresSequence" not in self._dataset:
                self._dataset.PixelMeasuresSequence = pydicom.Sequence()
            self._dataset.PixelMeasuresSequence.clear()
            self._dataset.PixelMeasuresSequence.extend([item.to_dataset() for item in value])

    def add_PixelMeasures(self, item: PixelMeasuresSequenceItem):
        if not isinstance(item, PixelMeasuresSequenceItem):
            raise ValueError(f"Item must be an instance of PixelMeasuresSequenceItem")
        self._PixelMeasuresSequence.append(item)
        if "PixelMeasuresSequence" not in self._dataset:
            self._dataset.PixelMeasuresSequence = pydicom.Sequence()
        self._dataset.PixelMeasuresSequence.append(item.to_dataset())
