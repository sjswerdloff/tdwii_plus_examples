from typing import Any, List, Optional

import pydicom

from .cardiac_synchronization_sequence_item import CardiacSynchronizationSequenceItem
from .contrast_bolus_usage_sequence_item import ContrastBolusUsageSequenceItem
from .ct_acquisition_details_sequence_item import CTAcquisitionDetailsSequenceItem
from .ct_acquisition_type_sequence_item import CTAcquisitionTypeSequenceItem
from .ct_additional_x_ray_source_sequence_item import CTAdditionalXRaySourceSequenceItem
from .ct_exposure_sequence_item import CTExposureSequenceItem
from .ct_geometry_sequence_item import CTGeometrySequenceItem
from .ct_image_frame_type_sequence_item import CTImageFrameTypeSequenceItem
from .ct_position_sequence_item import CTPositionSequenceItem
from .ct_reconstruction_sequence_item import CTReconstructionSequenceItem
from .ct_table_dynamics_sequence_item import CTTableDynamicsSequenceItem
from .ctx_ray_details_sequence_item import CTXRayDetailsSequenceItem
from .derivation_image_sequence_item import DerivationImageSequenceItem
from .frame_anatomy_sequence_item import FrameAnatomySequenceItem
from .frame_content_sequence_item import FrameContentSequenceItem
from .frame_voilut_sequence_item import FrameVOILUTSequenceItem
from .irradiation_event_identification_sequence_item import (
    IrradiationEventIdentificationSequenceItem,
)
from .multienergy_ct_characteristics_sequence_item import (
    MultienergyCTCharacteristicsSequenceItem,
)
from .multienergy_ct_processing_sequence_item import MultienergyCTProcessingSequenceItem
from .pixel_measures_sequence_item import PixelMeasuresSequenceItem
from .pixel_value_transformation_sequence_item import (
    PixelValueTransformationSequenceItem,
)
from .plane_orientation_sequence_item import PlaneOrientationSequenceItem
from .plane_position_sequence_item import PlanePositionSequenceItem
from .real_world_value_mapping_sequence_item import RealWorldValueMappingSequenceItem
from .referenced_image_sequence_item import ReferencedImageSequenceItem
from .respiratory_synchronization_sequence_item import (
    RespiratorySynchronizationSequenceItem,
)
from .temporal_position_sequence_item import TemporalPositionSequenceItem


class SharedFunctionalGroupsSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._ReferencedImageSequence: List[ReferencedImageSequenceItem] = []
        self._DerivationImageSequence: List[DerivationImageSequenceItem] = []
        self._CardiacSynchronizationSequence: List[CardiacSynchronizationSequenceItem] = []
        self._CTAcquisitionTypeSequence: List[CTAcquisitionTypeSequenceItem] = []
        self._CTAcquisitionDetailsSequence: List[CTAcquisitionDetailsSequenceItem] = []
        self._CTTableDynamicsSequence: List[CTTableDynamicsSequenceItem] = []
        self._CTGeometrySequence: List[CTGeometrySequenceItem] = []
        self._CTReconstructionSequence: List[CTReconstructionSequenceItem] = []
        self._CTExposureSequence: List[CTExposureSequenceItem] = []
        self._CTXRayDetailsSequence: List[CTXRayDetailsSequenceItem] = []
        self._CTPositionSequence: List[CTPositionSequenceItem] = []
        self._CTImageFrameTypeSequence: List[CTImageFrameTypeSequenceItem] = []
        self._ContrastBolusUsageSequence: List[ContrastBolusUsageSequenceItem] = []
        self._CTAdditionalXRaySourceSequence: List[CTAdditionalXRaySourceSequenceItem] = []
        self._MultienergyCTProcessingSequence: List[MultienergyCTProcessingSequenceItem] = []
        self._MultienergyCTCharacteristicsSequence: List[MultienergyCTCharacteristicsSequenceItem] = []
        self._IrradiationEventIdentificationSequence: List[IrradiationEventIdentificationSequenceItem] = []
        self._FrameAnatomySequence: List[FrameAnatomySequenceItem] = []
        self._FrameContentSequence: List[FrameContentSequenceItem] = []
        self._PlanePositionSequence: List[PlanePositionSequenceItem] = []
        self._PlaneOrientationSequence: List[PlaneOrientationSequenceItem] = []
        self._RespiratorySynchronizationSequence: List[RespiratorySynchronizationSequenceItem] = []
        self._TemporalPositionSequence: List[TemporalPositionSequenceItem] = []
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
    def CTAcquisitionTypeSequence(self) -> Optional[List[CTAcquisitionTypeSequenceItem]]:
        if "CTAcquisitionTypeSequence" in self._dataset:
            if len(self._CTAcquisitionTypeSequence) == len(self._dataset.CTAcquisitionTypeSequence):
                return self._CTAcquisitionTypeSequence
            else:
                return [CTAcquisitionTypeSequenceItem(x) for x in self._dataset.CTAcquisitionTypeSequence]
        return None

    @CTAcquisitionTypeSequence.setter
    def CTAcquisitionTypeSequence(self, value: Optional[List[CTAcquisitionTypeSequenceItem]]):
        if value is None:
            self._CTAcquisitionTypeSequence = []
            if "CTAcquisitionTypeSequence" in self._dataset:
                del self._dataset.CTAcquisitionTypeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CTAcquisitionTypeSequenceItem) for item in value):
            raise ValueError(f"CTAcquisitionTypeSequence must be a list of CTAcquisitionTypeSequenceItem objects")
        else:
            self._CTAcquisitionTypeSequence = value
            if "CTAcquisitionTypeSequence" not in self._dataset:
                self._dataset.CTAcquisitionTypeSequence = pydicom.Sequence()
            self._dataset.CTAcquisitionTypeSequence.clear()
            self._dataset.CTAcquisitionTypeSequence.extend([item.to_dataset() for item in value])

    def add_CTAcquisitionType(self, item: CTAcquisitionTypeSequenceItem):
        if not isinstance(item, CTAcquisitionTypeSequenceItem):
            raise ValueError(f"Item must be an instance of CTAcquisitionTypeSequenceItem")
        self._CTAcquisitionTypeSequence.append(item)
        if "CTAcquisitionTypeSequence" not in self._dataset:
            self._dataset.CTAcquisitionTypeSequence = pydicom.Sequence()
        self._dataset.CTAcquisitionTypeSequence.append(item.to_dataset())

    @property
    def CTAcquisitionDetailsSequence(self) -> Optional[List[CTAcquisitionDetailsSequenceItem]]:
        if "CTAcquisitionDetailsSequence" in self._dataset:
            if len(self._CTAcquisitionDetailsSequence) == len(self._dataset.CTAcquisitionDetailsSequence):
                return self._CTAcquisitionDetailsSequence
            else:
                return [CTAcquisitionDetailsSequenceItem(x) for x in self._dataset.CTAcquisitionDetailsSequence]
        return None

    @CTAcquisitionDetailsSequence.setter
    def CTAcquisitionDetailsSequence(self, value: Optional[List[CTAcquisitionDetailsSequenceItem]]):
        if value is None:
            self._CTAcquisitionDetailsSequence = []
            if "CTAcquisitionDetailsSequence" in self._dataset:
                del self._dataset.CTAcquisitionDetailsSequence
        elif not isinstance(value, list) or not all(isinstance(item, CTAcquisitionDetailsSequenceItem) for item in value):
            raise ValueError(f"CTAcquisitionDetailsSequence must be a list of CTAcquisitionDetailsSequenceItem objects")
        else:
            self._CTAcquisitionDetailsSequence = value
            if "CTAcquisitionDetailsSequence" not in self._dataset:
                self._dataset.CTAcquisitionDetailsSequence = pydicom.Sequence()
            self._dataset.CTAcquisitionDetailsSequence.clear()
            self._dataset.CTAcquisitionDetailsSequence.extend([item.to_dataset() for item in value])

    def add_CTAcquisitionDetails(self, item: CTAcquisitionDetailsSequenceItem):
        if not isinstance(item, CTAcquisitionDetailsSequenceItem):
            raise ValueError(f"Item must be an instance of CTAcquisitionDetailsSequenceItem")
        self._CTAcquisitionDetailsSequence.append(item)
        if "CTAcquisitionDetailsSequence" not in self._dataset:
            self._dataset.CTAcquisitionDetailsSequence = pydicom.Sequence()
        self._dataset.CTAcquisitionDetailsSequence.append(item.to_dataset())

    @property
    def CTTableDynamicsSequence(self) -> Optional[List[CTTableDynamicsSequenceItem]]:
        if "CTTableDynamicsSequence" in self._dataset:
            if len(self._CTTableDynamicsSequence) == len(self._dataset.CTTableDynamicsSequence):
                return self._CTTableDynamicsSequence
            else:
                return [CTTableDynamicsSequenceItem(x) for x in self._dataset.CTTableDynamicsSequence]
        return None

    @CTTableDynamicsSequence.setter
    def CTTableDynamicsSequence(self, value: Optional[List[CTTableDynamicsSequenceItem]]):
        if value is None:
            self._CTTableDynamicsSequence = []
            if "CTTableDynamicsSequence" in self._dataset:
                del self._dataset.CTTableDynamicsSequence
        elif not isinstance(value, list) or not all(isinstance(item, CTTableDynamicsSequenceItem) for item in value):
            raise ValueError(f"CTTableDynamicsSequence must be a list of CTTableDynamicsSequenceItem objects")
        else:
            self._CTTableDynamicsSequence = value
            if "CTTableDynamicsSequence" not in self._dataset:
                self._dataset.CTTableDynamicsSequence = pydicom.Sequence()
            self._dataset.CTTableDynamicsSequence.clear()
            self._dataset.CTTableDynamicsSequence.extend([item.to_dataset() for item in value])

    def add_CTTableDynamics(self, item: CTTableDynamicsSequenceItem):
        if not isinstance(item, CTTableDynamicsSequenceItem):
            raise ValueError(f"Item must be an instance of CTTableDynamicsSequenceItem")
        self._CTTableDynamicsSequence.append(item)
        if "CTTableDynamicsSequence" not in self._dataset:
            self._dataset.CTTableDynamicsSequence = pydicom.Sequence()
        self._dataset.CTTableDynamicsSequence.append(item.to_dataset())

    @property
    def CTGeometrySequence(self) -> Optional[List[CTGeometrySequenceItem]]:
        if "CTGeometrySequence" in self._dataset:
            if len(self._CTGeometrySequence) == len(self._dataset.CTGeometrySequence):
                return self._CTGeometrySequence
            else:
                return [CTGeometrySequenceItem(x) for x in self._dataset.CTGeometrySequence]
        return None

    @CTGeometrySequence.setter
    def CTGeometrySequence(self, value: Optional[List[CTGeometrySequenceItem]]):
        if value is None:
            self._CTGeometrySequence = []
            if "CTGeometrySequence" in self._dataset:
                del self._dataset.CTGeometrySequence
        elif not isinstance(value, list) or not all(isinstance(item, CTGeometrySequenceItem) for item in value):
            raise ValueError(f"CTGeometrySequence must be a list of CTGeometrySequenceItem objects")
        else:
            self._CTGeometrySequence = value
            if "CTGeometrySequence" not in self._dataset:
                self._dataset.CTGeometrySequence = pydicom.Sequence()
            self._dataset.CTGeometrySequence.clear()
            self._dataset.CTGeometrySequence.extend([item.to_dataset() for item in value])

    def add_CTGeometry(self, item: CTGeometrySequenceItem):
        if not isinstance(item, CTGeometrySequenceItem):
            raise ValueError(f"Item must be an instance of CTGeometrySequenceItem")
        self._CTGeometrySequence.append(item)
        if "CTGeometrySequence" not in self._dataset:
            self._dataset.CTGeometrySequence = pydicom.Sequence()
        self._dataset.CTGeometrySequence.append(item.to_dataset())

    @property
    def CTReconstructionSequence(self) -> Optional[List[CTReconstructionSequenceItem]]:
        if "CTReconstructionSequence" in self._dataset:
            if len(self._CTReconstructionSequence) == len(self._dataset.CTReconstructionSequence):
                return self._CTReconstructionSequence
            else:
                return [CTReconstructionSequenceItem(x) for x in self._dataset.CTReconstructionSequence]
        return None

    @CTReconstructionSequence.setter
    def CTReconstructionSequence(self, value: Optional[List[CTReconstructionSequenceItem]]):
        if value is None:
            self._CTReconstructionSequence = []
            if "CTReconstructionSequence" in self._dataset:
                del self._dataset.CTReconstructionSequence
        elif not isinstance(value, list) or not all(isinstance(item, CTReconstructionSequenceItem) for item in value):
            raise ValueError(f"CTReconstructionSequence must be a list of CTReconstructionSequenceItem objects")
        else:
            self._CTReconstructionSequence = value
            if "CTReconstructionSequence" not in self._dataset:
                self._dataset.CTReconstructionSequence = pydicom.Sequence()
            self._dataset.CTReconstructionSequence.clear()
            self._dataset.CTReconstructionSequence.extend([item.to_dataset() for item in value])

    def add_CTReconstruction(self, item: CTReconstructionSequenceItem):
        if not isinstance(item, CTReconstructionSequenceItem):
            raise ValueError(f"Item must be an instance of CTReconstructionSequenceItem")
        self._CTReconstructionSequence.append(item)
        if "CTReconstructionSequence" not in self._dataset:
            self._dataset.CTReconstructionSequence = pydicom.Sequence()
        self._dataset.CTReconstructionSequence.append(item.to_dataset())

    @property
    def CTExposureSequence(self) -> Optional[List[CTExposureSequenceItem]]:
        if "CTExposureSequence" in self._dataset:
            if len(self._CTExposureSequence) == len(self._dataset.CTExposureSequence):
                return self._CTExposureSequence
            else:
                return [CTExposureSequenceItem(x) for x in self._dataset.CTExposureSequence]
        return None

    @CTExposureSequence.setter
    def CTExposureSequence(self, value: Optional[List[CTExposureSequenceItem]]):
        if value is None:
            self._CTExposureSequence = []
            if "CTExposureSequence" in self._dataset:
                del self._dataset.CTExposureSequence
        elif not isinstance(value, list) or not all(isinstance(item, CTExposureSequenceItem) for item in value):
            raise ValueError(f"CTExposureSequence must be a list of CTExposureSequenceItem objects")
        else:
            self._CTExposureSequence = value
            if "CTExposureSequence" not in self._dataset:
                self._dataset.CTExposureSequence = pydicom.Sequence()
            self._dataset.CTExposureSequence.clear()
            self._dataset.CTExposureSequence.extend([item.to_dataset() for item in value])

    def add_CTExposure(self, item: CTExposureSequenceItem):
        if not isinstance(item, CTExposureSequenceItem):
            raise ValueError(f"Item must be an instance of CTExposureSequenceItem")
        self._CTExposureSequence.append(item)
        if "CTExposureSequence" not in self._dataset:
            self._dataset.CTExposureSequence = pydicom.Sequence()
        self._dataset.CTExposureSequence.append(item.to_dataset())

    @property
    def CTXRayDetailsSequence(self) -> Optional[List[CTXRayDetailsSequenceItem]]:
        if "CTXRayDetailsSequence" in self._dataset:
            if len(self._CTXRayDetailsSequence) == len(self._dataset.CTXRayDetailsSequence):
                return self._CTXRayDetailsSequence
            else:
                return [CTXRayDetailsSequenceItem(x) for x in self._dataset.CTXRayDetailsSequence]
        return None

    @CTXRayDetailsSequence.setter
    def CTXRayDetailsSequence(self, value: Optional[List[CTXRayDetailsSequenceItem]]):
        if value is None:
            self._CTXRayDetailsSequence = []
            if "CTXRayDetailsSequence" in self._dataset:
                del self._dataset.CTXRayDetailsSequence
        elif not isinstance(value, list) or not all(isinstance(item, CTXRayDetailsSequenceItem) for item in value):
            raise ValueError(f"CTXRayDetailsSequence must be a list of CTXRayDetailsSequenceItem objects")
        else:
            self._CTXRayDetailsSequence = value
            if "CTXRayDetailsSequence" not in self._dataset:
                self._dataset.CTXRayDetailsSequence = pydicom.Sequence()
            self._dataset.CTXRayDetailsSequence.clear()
            self._dataset.CTXRayDetailsSequence.extend([item.to_dataset() for item in value])

    def add_CTXRayDetails(self, item: CTXRayDetailsSequenceItem):
        if not isinstance(item, CTXRayDetailsSequenceItem):
            raise ValueError(f"Item must be an instance of CTXRayDetailsSequenceItem")
        self._CTXRayDetailsSequence.append(item)
        if "CTXRayDetailsSequence" not in self._dataset:
            self._dataset.CTXRayDetailsSequence = pydicom.Sequence()
        self._dataset.CTXRayDetailsSequence.append(item.to_dataset())

    @property
    def CTPositionSequence(self) -> Optional[List[CTPositionSequenceItem]]:
        if "CTPositionSequence" in self._dataset:
            if len(self._CTPositionSequence) == len(self._dataset.CTPositionSequence):
                return self._CTPositionSequence
            else:
                return [CTPositionSequenceItem(x) for x in self._dataset.CTPositionSequence]
        return None

    @CTPositionSequence.setter
    def CTPositionSequence(self, value: Optional[List[CTPositionSequenceItem]]):
        if value is None:
            self._CTPositionSequence = []
            if "CTPositionSequence" in self._dataset:
                del self._dataset.CTPositionSequence
        elif not isinstance(value, list) or not all(isinstance(item, CTPositionSequenceItem) for item in value):
            raise ValueError(f"CTPositionSequence must be a list of CTPositionSequenceItem objects")
        else:
            self._CTPositionSequence = value
            if "CTPositionSequence" not in self._dataset:
                self._dataset.CTPositionSequence = pydicom.Sequence()
            self._dataset.CTPositionSequence.clear()
            self._dataset.CTPositionSequence.extend([item.to_dataset() for item in value])

    def add_CTPosition(self, item: CTPositionSequenceItem):
        if not isinstance(item, CTPositionSequenceItem):
            raise ValueError(f"Item must be an instance of CTPositionSequenceItem")
        self._CTPositionSequence.append(item)
        if "CTPositionSequence" not in self._dataset:
            self._dataset.CTPositionSequence = pydicom.Sequence()
        self._dataset.CTPositionSequence.append(item.to_dataset())

    @property
    def CTImageFrameTypeSequence(self) -> Optional[List[CTImageFrameTypeSequenceItem]]:
        if "CTImageFrameTypeSequence" in self._dataset:
            if len(self._CTImageFrameTypeSequence) == len(self._dataset.CTImageFrameTypeSequence):
                return self._CTImageFrameTypeSequence
            else:
                return [CTImageFrameTypeSequenceItem(x) for x in self._dataset.CTImageFrameTypeSequence]
        return None

    @CTImageFrameTypeSequence.setter
    def CTImageFrameTypeSequence(self, value: Optional[List[CTImageFrameTypeSequenceItem]]):
        if value is None:
            self._CTImageFrameTypeSequence = []
            if "CTImageFrameTypeSequence" in self._dataset:
                del self._dataset.CTImageFrameTypeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CTImageFrameTypeSequenceItem) for item in value):
            raise ValueError(f"CTImageFrameTypeSequence must be a list of CTImageFrameTypeSequenceItem objects")
        else:
            self._CTImageFrameTypeSequence = value
            if "CTImageFrameTypeSequence" not in self._dataset:
                self._dataset.CTImageFrameTypeSequence = pydicom.Sequence()
            self._dataset.CTImageFrameTypeSequence.clear()
            self._dataset.CTImageFrameTypeSequence.extend([item.to_dataset() for item in value])

    def add_CTImageFrameType(self, item: CTImageFrameTypeSequenceItem):
        if not isinstance(item, CTImageFrameTypeSequenceItem):
            raise ValueError(f"Item must be an instance of CTImageFrameTypeSequenceItem")
        self._CTImageFrameTypeSequence.append(item)
        if "CTImageFrameTypeSequence" not in self._dataset:
            self._dataset.CTImageFrameTypeSequence = pydicom.Sequence()
        self._dataset.CTImageFrameTypeSequence.append(item.to_dataset())

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
    def CTAdditionalXRaySourceSequence(self) -> Optional[List[CTAdditionalXRaySourceSequenceItem]]:
        if "CTAdditionalXRaySourceSequence" in self._dataset:
            if len(self._CTAdditionalXRaySourceSequence) == len(self._dataset.CTAdditionalXRaySourceSequence):
                return self._CTAdditionalXRaySourceSequence
            else:
                return [CTAdditionalXRaySourceSequenceItem(x) for x in self._dataset.CTAdditionalXRaySourceSequence]
        return None

    @CTAdditionalXRaySourceSequence.setter
    def CTAdditionalXRaySourceSequence(self, value: Optional[List[CTAdditionalXRaySourceSequenceItem]]):
        if value is None:
            self._CTAdditionalXRaySourceSequence = []
            if "CTAdditionalXRaySourceSequence" in self._dataset:
                del self._dataset.CTAdditionalXRaySourceSequence
        elif not isinstance(value, list) or not all(isinstance(item, CTAdditionalXRaySourceSequenceItem) for item in value):
            raise ValueError(f"CTAdditionalXRaySourceSequence must be a list of CTAdditionalXRaySourceSequenceItem objects")
        else:
            self._CTAdditionalXRaySourceSequence = value
            if "CTAdditionalXRaySourceSequence" not in self._dataset:
                self._dataset.CTAdditionalXRaySourceSequence = pydicom.Sequence()
            self._dataset.CTAdditionalXRaySourceSequence.clear()
            self._dataset.CTAdditionalXRaySourceSequence.extend([item.to_dataset() for item in value])

    def add_CTAdditionalXRaySource(self, item: CTAdditionalXRaySourceSequenceItem):
        if not isinstance(item, CTAdditionalXRaySourceSequenceItem):
            raise ValueError(f"Item must be an instance of CTAdditionalXRaySourceSequenceItem")
        self._CTAdditionalXRaySourceSequence.append(item)
        if "CTAdditionalXRaySourceSequence" not in self._dataset:
            self._dataset.CTAdditionalXRaySourceSequence = pydicom.Sequence()
        self._dataset.CTAdditionalXRaySourceSequence.append(item.to_dataset())

    @property
    def MultienergyCTProcessingSequence(self) -> Optional[List[MultienergyCTProcessingSequenceItem]]:
        if "MultienergyCTProcessingSequence" in self._dataset:
            if len(self._MultienergyCTProcessingSequence) == len(self._dataset.MultienergyCTProcessingSequence):
                return self._MultienergyCTProcessingSequence
            else:
                return [MultienergyCTProcessingSequenceItem(x) for x in self._dataset.MultienergyCTProcessingSequence]
        return None

    @MultienergyCTProcessingSequence.setter
    def MultienergyCTProcessingSequence(self, value: Optional[List[MultienergyCTProcessingSequenceItem]]):
        if value is None:
            self._MultienergyCTProcessingSequence = []
            if "MultienergyCTProcessingSequence" in self._dataset:
                del self._dataset.MultienergyCTProcessingSequence
        elif not isinstance(value, list) or not all(isinstance(item, MultienergyCTProcessingSequenceItem) for item in value):
            raise ValueError(f"MultienergyCTProcessingSequence must be a list of MultienergyCTProcessingSequenceItem objects")
        else:
            self._MultienergyCTProcessingSequence = value
            if "MultienergyCTProcessingSequence" not in self._dataset:
                self._dataset.MultienergyCTProcessingSequence = pydicom.Sequence()
            self._dataset.MultienergyCTProcessingSequence.clear()
            self._dataset.MultienergyCTProcessingSequence.extend([item.to_dataset() for item in value])

    def add_MultienergyCTProcessing(self, item: MultienergyCTProcessingSequenceItem):
        if not isinstance(item, MultienergyCTProcessingSequenceItem):
            raise ValueError(f"Item must be an instance of MultienergyCTProcessingSequenceItem")
        self._MultienergyCTProcessingSequence.append(item)
        if "MultienergyCTProcessingSequence" not in self._dataset:
            self._dataset.MultienergyCTProcessingSequence = pydicom.Sequence()
        self._dataset.MultienergyCTProcessingSequence.append(item.to_dataset())

    @property
    def MultienergyCTCharacteristicsSequence(self) -> Optional[List[MultienergyCTCharacteristicsSequenceItem]]:
        if "MultienergyCTCharacteristicsSequence" in self._dataset:
            if len(self._MultienergyCTCharacteristicsSequence) == len(self._dataset.MultienergyCTCharacteristicsSequence):
                return self._MultienergyCTCharacteristicsSequence
            else:
                return [
                    MultienergyCTCharacteristicsSequenceItem(x) for x in self._dataset.MultienergyCTCharacteristicsSequence
                ]
        return None

    @MultienergyCTCharacteristicsSequence.setter
    def MultienergyCTCharacteristicsSequence(self, value: Optional[List[MultienergyCTCharacteristicsSequenceItem]]):
        if value is None:
            self._MultienergyCTCharacteristicsSequence = []
            if "MultienergyCTCharacteristicsSequence" in self._dataset:
                del self._dataset.MultienergyCTCharacteristicsSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, MultienergyCTCharacteristicsSequenceItem) for item in value
        ):
            raise ValueError(
                f"MultienergyCTCharacteristicsSequence must be a list of MultienergyCTCharacteristicsSequenceItem objects"
            )
        else:
            self._MultienergyCTCharacteristicsSequence = value
            if "MultienergyCTCharacteristicsSequence" not in self._dataset:
                self._dataset.MultienergyCTCharacteristicsSequence = pydicom.Sequence()
            self._dataset.MultienergyCTCharacteristicsSequence.clear()
            self._dataset.MultienergyCTCharacteristicsSequence.extend([item.to_dataset() for item in value])

    def add_MultienergyCTCharacteristics(self, item: MultienergyCTCharacteristicsSequenceItem):
        if not isinstance(item, MultienergyCTCharacteristicsSequenceItem):
            raise ValueError(f"Item must be an instance of MultienergyCTCharacteristicsSequenceItem")
        self._MultienergyCTCharacteristicsSequence.append(item)
        if "MultienergyCTCharacteristicsSequence" not in self._dataset:
            self._dataset.MultienergyCTCharacteristicsSequence = pydicom.Sequence()
        self._dataset.MultienergyCTCharacteristicsSequence.append(item.to_dataset())

    @property
    def IrradiationEventIdentificationSequence(self) -> Optional[List[IrradiationEventIdentificationSequenceItem]]:
        if "IrradiationEventIdentificationSequence" in self._dataset:
            if len(self._IrradiationEventIdentificationSequence) == len(self._dataset.IrradiationEventIdentificationSequence):
                return self._IrradiationEventIdentificationSequence
            else:
                return [
                    IrradiationEventIdentificationSequenceItem(x) for x in self._dataset.IrradiationEventIdentificationSequence
                ]
        return None

    @IrradiationEventIdentificationSequence.setter
    def IrradiationEventIdentificationSequence(self, value: Optional[List[IrradiationEventIdentificationSequenceItem]]):
        if value is None:
            self._IrradiationEventIdentificationSequence = []
            if "IrradiationEventIdentificationSequence" in self._dataset:
                del self._dataset.IrradiationEventIdentificationSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, IrradiationEventIdentificationSequenceItem) for item in value
        ):
            raise ValueError(
                f"IrradiationEventIdentificationSequence must be a list of IrradiationEventIdentificationSequenceItem objects"
            )
        else:
            self._IrradiationEventIdentificationSequence = value
            if "IrradiationEventIdentificationSequence" not in self._dataset:
                self._dataset.IrradiationEventIdentificationSequence = pydicom.Sequence()
            self._dataset.IrradiationEventIdentificationSequence.clear()
            self._dataset.IrradiationEventIdentificationSequence.extend([item.to_dataset() for item in value])

    def add_IrradiationEventIdentification(self, item: IrradiationEventIdentificationSequenceItem):
        if not isinstance(item, IrradiationEventIdentificationSequenceItem):
            raise ValueError(f"Item must be an instance of IrradiationEventIdentificationSequenceItem")
        self._IrradiationEventIdentificationSequence.append(item)
        if "IrradiationEventIdentificationSequence" not in self._dataset:
            self._dataset.IrradiationEventIdentificationSequence = pydicom.Sequence()
        self._dataset.IrradiationEventIdentificationSequence.append(item.to_dataset())

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
            raise ValueError(f"FrameVOILUTSequence must be a list of FrameVOILUTSequenceItem objects")
        else:
            self._FrameVOILUTSequence = value
            if "FrameVOILUTSequence" not in self._dataset:
                self._dataset.FrameVOILUTSequence = pydicom.Sequence()
            self._dataset.FrameVOILUTSequence.clear()
            self._dataset.FrameVOILUTSequence.extend([item.to_dataset() for item in value])

    def add_FrameVOILUT(self, item: FrameVOILUTSequenceItem):
        if not isinstance(item, FrameVOILUTSequenceItem):
            raise ValueError(f"Item must be an instance of FrameVOILUTSequenceItem")
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
            raise ValueError(
                f"PixelValueTransformationSequence must be a list of PixelValueTransformationSequenceItem objects"
            )
        else:
            self._PixelValueTransformationSequence = value
            if "PixelValueTransformationSequence" not in self._dataset:
                self._dataset.PixelValueTransformationSequence = pydicom.Sequence()
            self._dataset.PixelValueTransformationSequence.clear()
            self._dataset.PixelValueTransformationSequence.extend([item.to_dataset() for item in value])

    def add_PixelValueTransformation(self, item: PixelValueTransformationSequenceItem):
        if not isinstance(item, PixelValueTransformationSequenceItem):
            raise ValueError(f"Item must be an instance of PixelValueTransformationSequenceItem")
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
            raise ValueError(f"RealWorldValueMappingSequence must be a list of RealWorldValueMappingSequenceItem objects")
        else:
            self._RealWorldValueMappingSequence = value
            if "RealWorldValueMappingSequence" not in self._dataset:
                self._dataset.RealWorldValueMappingSequence = pydicom.Sequence()
            self._dataset.RealWorldValueMappingSequence.clear()
            self._dataset.RealWorldValueMappingSequence.extend([item.to_dataset() for item in value])

    def add_RealWorldValueMapping(self, item: RealWorldValueMappingSequenceItem):
        if not isinstance(item, RealWorldValueMappingSequenceItem):
            raise ValueError(f"Item must be an instance of RealWorldValueMappingSequenceItem")
        self._RealWorldValueMappingSequence.append(item)
        if "RealWorldValueMappingSequence" not in self._dataset:
            self._dataset.RealWorldValueMappingSequence = pydicom.Sequence()
        self._dataset.RealWorldValueMappingSequence.append(item.to_dataset())
