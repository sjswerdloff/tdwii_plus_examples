from typing import Any, List, Optional  # noqa

import pydicom

from .contrast_bolus_usage_sequence_item import ContrastBolusUsageSequenceItem
from .derivation_image_sequence_item import DerivationImageSequenceItem
from .frame_content_sequence_item import FrameContentSequenceItem
from .frame_display_shutter_sequence_item import FrameDisplayShutterSequenceItem
from .frame_voilut_sequence_item import FrameVOILUTSequenceItem
from .image_data_type_sequence_item import ImageDataTypeSequenceItem
from .patient_orientation_in_frame_sequence_item import (
    PatientOrientationInFrameSequenceItem,
)
from .photoacoustic_excitation_characteristics_sequence_item import (
    PhotoacousticExcitationCharacteristicsSequenceItem,
)
from .photoacoustic_image_frame_type_sequence_item import (
    PhotoacousticImageFrameTypeSequenceItem,
)
from .pixel_measures_sequence_item import PixelMeasuresSequenceItem
from .plane_orientation_sequence_item import PlaneOrientationSequenceItem
from .plane_orientation_volume_sequence_item import PlaneOrientationVolumeSequenceItem
from .plane_position_sequence_item import PlanePositionSequenceItem
from .plane_position_volume_sequence_item import PlanePositionVolumeSequenceItem
from .real_world_value_mapping_sequence_item import RealWorldValueMappingSequenceItem
from .reconstruction_algorithm_sequence_item import ReconstructionAlgorithmSequenceItem
from .referenced_image_sequence_item import ReferencedImageSequenceItem
from .temporal_position_sequence_item import TemporalPositionSequenceItem


class PerFrameFunctionalGroupsSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._ReferencedImageSequence: List[ReferencedImageSequenceItem] = []
        self._DerivationImageSequence: List[DerivationImageSequenceItem] = []
        self._ContrastBolusUsageSequence: List[ContrastBolusUsageSequenceItem] = []
        self._FrameDisplayShutterSequence: List[FrameDisplayShutterSequenceItem] = []
        self._ImageDataTypeSequence: List[ImageDataTypeSequenceItem] = []
        self._PhotoacousticExcitationCharacteristicsSequence: List[PhotoacousticExcitationCharacteristicsSequenceItem] = []
        self._PhotoacousticImageFrameTypeSequence: List[PhotoacousticImageFrameTypeSequenceItem] = []
        self._ReconstructionAlgorithmSequence: List[ReconstructionAlgorithmSequenceItem] = []
        self._FrameContentSequence: List[FrameContentSequenceItem] = []
        self._PlanePositionSequence: List[PlanePositionSequenceItem] = []
        self._PlaneOrientationSequence: List[PlaneOrientationSequenceItem] = []
        self._PlanePositionVolumeSequence: List[PlanePositionVolumeSequenceItem] = []
        self._PlaneOrientationVolumeSequence: List[PlaneOrientationVolumeSequenceItem] = []
        self._TemporalPositionSequence: List[TemporalPositionSequenceItem] = []
        self._PatientOrientationInFrameSequence: List[PatientOrientationInFrameSequenceItem] = []
        self._PixelMeasuresSequence: List[PixelMeasuresSequenceItem] = []
        self._FrameVOILUTSequence: List[FrameVOILUTSequenceItem] = []
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
    def FrameDisplayShutterSequence(self) -> Optional[List[FrameDisplayShutterSequenceItem]]:
        if "FrameDisplayShutterSequence" in self._dataset:
            if len(self._FrameDisplayShutterSequence) == len(self._dataset.FrameDisplayShutterSequence):
                return self._FrameDisplayShutterSequence
            else:
                return [FrameDisplayShutterSequenceItem(x) for x in self._dataset.FrameDisplayShutterSequence]
        return None

    @FrameDisplayShutterSequence.setter
    def FrameDisplayShutterSequence(self, value: Optional[List[FrameDisplayShutterSequenceItem]]):
        if value is None:
            self._FrameDisplayShutterSequence = []
            if "FrameDisplayShutterSequence" in self._dataset:
                del self._dataset.FrameDisplayShutterSequence
        elif not isinstance(value, list) or not all(isinstance(item, FrameDisplayShutterSequenceItem) for item in value):
            raise ValueError("FrameDisplayShutterSequence must be a list of FrameDisplayShutterSequenceItem objects")
        else:
            self._FrameDisplayShutterSequence = value
            if "FrameDisplayShutterSequence" not in self._dataset:
                self._dataset.FrameDisplayShutterSequence = pydicom.Sequence()
            self._dataset.FrameDisplayShutterSequence.clear()
            self._dataset.FrameDisplayShutterSequence.extend([item.to_dataset() for item in value])

    def add_FrameDisplayShutter(self, item: FrameDisplayShutterSequenceItem):
        if not isinstance(item, FrameDisplayShutterSequenceItem):
            raise ValueError("Item must be an instance of FrameDisplayShutterSequenceItem")
        self._FrameDisplayShutterSequence.append(item)
        if "FrameDisplayShutterSequence" not in self._dataset:
            self._dataset.FrameDisplayShutterSequence = pydicom.Sequence()
        self._dataset.FrameDisplayShutterSequence.append(item.to_dataset())

    @property
    def ImageDataTypeSequence(self) -> Optional[List[ImageDataTypeSequenceItem]]:
        if "ImageDataTypeSequence" in self._dataset:
            if len(self._ImageDataTypeSequence) == len(self._dataset.ImageDataTypeSequence):
                return self._ImageDataTypeSequence
            else:
                return [ImageDataTypeSequenceItem(x) for x in self._dataset.ImageDataTypeSequence]
        return None

    @ImageDataTypeSequence.setter
    def ImageDataTypeSequence(self, value: Optional[List[ImageDataTypeSequenceItem]]):
        if value is None:
            self._ImageDataTypeSequence = []
            if "ImageDataTypeSequence" in self._dataset:
                del self._dataset.ImageDataTypeSequence
        elif not isinstance(value, list) or not all(isinstance(item, ImageDataTypeSequenceItem) for item in value):
            raise ValueError("ImageDataTypeSequence must be a list of ImageDataTypeSequenceItem objects")
        else:
            self._ImageDataTypeSequence = value
            if "ImageDataTypeSequence" not in self._dataset:
                self._dataset.ImageDataTypeSequence = pydicom.Sequence()
            self._dataset.ImageDataTypeSequence.clear()
            self._dataset.ImageDataTypeSequence.extend([item.to_dataset() for item in value])

    def add_ImageDataType(self, item: ImageDataTypeSequenceItem):
        if not isinstance(item, ImageDataTypeSequenceItem):
            raise ValueError("Item must be an instance of ImageDataTypeSequenceItem")
        self._ImageDataTypeSequence.append(item)
        if "ImageDataTypeSequence" not in self._dataset:
            self._dataset.ImageDataTypeSequence = pydicom.Sequence()
        self._dataset.ImageDataTypeSequence.append(item.to_dataset())

    @property
    def PhotoacousticExcitationCharacteristicsSequence(
        self,
    ) -> Optional[List[PhotoacousticExcitationCharacteristicsSequenceItem]]:
        if "PhotoacousticExcitationCharacteristicsSequence" in self._dataset:
            if len(self._PhotoacousticExcitationCharacteristicsSequence) == len(
                self._dataset.PhotoacousticExcitationCharacteristicsSequence
            ):
                return self._PhotoacousticExcitationCharacteristicsSequence
            else:
                return [
                    PhotoacousticExcitationCharacteristicsSequenceItem(x)
                    for x in self._dataset.PhotoacousticExcitationCharacteristicsSequence
                ]
        return None

    @PhotoacousticExcitationCharacteristicsSequence.setter
    def PhotoacousticExcitationCharacteristicsSequence(
        self, value: Optional[List[PhotoacousticExcitationCharacteristicsSequenceItem]]
    ):
        if value is None:
            self._PhotoacousticExcitationCharacteristicsSequence = []
            if "PhotoacousticExcitationCharacteristicsSequence" in self._dataset:
                del self._dataset.PhotoacousticExcitationCharacteristicsSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, PhotoacousticExcitationCharacteristicsSequenceItem) for item in value
        ):
            raise ValueError(
                "PhotoacousticExcitationCharacteristicsSequence must be a list of"
                " PhotoacousticExcitationCharacteristicsSequenceItem objects"
            )
        else:
            self._PhotoacousticExcitationCharacteristicsSequence = value
            if "PhotoacousticExcitationCharacteristicsSequence" not in self._dataset:
                self._dataset.PhotoacousticExcitationCharacteristicsSequence = pydicom.Sequence()
            self._dataset.PhotoacousticExcitationCharacteristicsSequence.clear()
            self._dataset.PhotoacousticExcitationCharacteristicsSequence.extend([item.to_dataset() for item in value])

    def add_PhotoacousticExcitationCharacteristics(self, item: PhotoacousticExcitationCharacteristicsSequenceItem):
        if not isinstance(item, PhotoacousticExcitationCharacteristicsSequenceItem):
            raise ValueError("Item must be an instance of PhotoacousticExcitationCharacteristicsSequenceItem")
        self._PhotoacousticExcitationCharacteristicsSequence.append(item)
        if "PhotoacousticExcitationCharacteristicsSequence" not in self._dataset:
            self._dataset.PhotoacousticExcitationCharacteristicsSequence = pydicom.Sequence()
        self._dataset.PhotoacousticExcitationCharacteristicsSequence.append(item.to_dataset())

    @property
    def PhotoacousticImageFrameTypeSequence(self) -> Optional[List[PhotoacousticImageFrameTypeSequenceItem]]:
        if "PhotoacousticImageFrameTypeSequence" in self._dataset:
            if len(self._PhotoacousticImageFrameTypeSequence) == len(self._dataset.PhotoacousticImageFrameTypeSequence):
                return self._PhotoacousticImageFrameTypeSequence
            else:
                return [PhotoacousticImageFrameTypeSequenceItem(x) for x in self._dataset.PhotoacousticImageFrameTypeSequence]
        return None

    @PhotoacousticImageFrameTypeSequence.setter
    def PhotoacousticImageFrameTypeSequence(self, value: Optional[List[PhotoacousticImageFrameTypeSequenceItem]]):
        if value is None:
            self._PhotoacousticImageFrameTypeSequence = []
            if "PhotoacousticImageFrameTypeSequence" in self._dataset:
                del self._dataset.PhotoacousticImageFrameTypeSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, PhotoacousticImageFrameTypeSequenceItem) for item in value
        ):
            raise ValueError(
                "PhotoacousticImageFrameTypeSequence must be a list of PhotoacousticImageFrameTypeSequenceItem objects"
            )
        else:
            self._PhotoacousticImageFrameTypeSequence = value
            if "PhotoacousticImageFrameTypeSequence" not in self._dataset:
                self._dataset.PhotoacousticImageFrameTypeSequence = pydicom.Sequence()
            self._dataset.PhotoacousticImageFrameTypeSequence.clear()
            self._dataset.PhotoacousticImageFrameTypeSequence.extend([item.to_dataset() for item in value])

    def add_PhotoacousticImageFrameType(self, item: PhotoacousticImageFrameTypeSequenceItem):
        if not isinstance(item, PhotoacousticImageFrameTypeSequenceItem):
            raise ValueError("Item must be an instance of PhotoacousticImageFrameTypeSequenceItem")
        self._PhotoacousticImageFrameTypeSequence.append(item)
        if "PhotoacousticImageFrameTypeSequence" not in self._dataset:
            self._dataset.PhotoacousticImageFrameTypeSequence = pydicom.Sequence()
        self._dataset.PhotoacousticImageFrameTypeSequence.append(item.to_dataset())

    @property
    def ReconstructionAlgorithmSequence(self) -> Optional[List[ReconstructionAlgorithmSequenceItem]]:
        if "ReconstructionAlgorithmSequence" in self._dataset:
            if len(self._ReconstructionAlgorithmSequence) == len(self._dataset.ReconstructionAlgorithmSequence):
                return self._ReconstructionAlgorithmSequence
            else:
                return [ReconstructionAlgorithmSequenceItem(x) for x in self._dataset.ReconstructionAlgorithmSequence]
        return None

    @ReconstructionAlgorithmSequence.setter
    def ReconstructionAlgorithmSequence(self, value: Optional[List[ReconstructionAlgorithmSequenceItem]]):
        if value is None:
            self._ReconstructionAlgorithmSequence = []
            if "ReconstructionAlgorithmSequence" in self._dataset:
                del self._dataset.ReconstructionAlgorithmSequence
        elif not isinstance(value, list) or not all(isinstance(item, ReconstructionAlgorithmSequenceItem) for item in value):
            raise ValueError("ReconstructionAlgorithmSequence must be a list of ReconstructionAlgorithmSequenceItem objects")
        else:
            self._ReconstructionAlgorithmSequence = value
            if "ReconstructionAlgorithmSequence" not in self._dataset:
                self._dataset.ReconstructionAlgorithmSequence = pydicom.Sequence()
            self._dataset.ReconstructionAlgorithmSequence.clear()
            self._dataset.ReconstructionAlgorithmSequence.extend([item.to_dataset() for item in value])

    def add_ReconstructionAlgorithm(self, item: ReconstructionAlgorithmSequenceItem):
        if not isinstance(item, ReconstructionAlgorithmSequenceItem):
            raise ValueError("Item must be an instance of ReconstructionAlgorithmSequenceItem")
        self._ReconstructionAlgorithmSequence.append(item)
        if "ReconstructionAlgorithmSequence" not in self._dataset:
            self._dataset.ReconstructionAlgorithmSequence = pydicom.Sequence()
        self._dataset.ReconstructionAlgorithmSequence.append(item.to_dataset())

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
    def PlanePositionVolumeSequence(self) -> Optional[List[PlanePositionVolumeSequenceItem]]:
        if "PlanePositionVolumeSequence" in self._dataset:
            if len(self._PlanePositionVolumeSequence) == len(self._dataset.PlanePositionVolumeSequence):
                return self._PlanePositionVolumeSequence
            else:
                return [PlanePositionVolumeSequenceItem(x) for x in self._dataset.PlanePositionVolumeSequence]
        return None

    @PlanePositionVolumeSequence.setter
    def PlanePositionVolumeSequence(self, value: Optional[List[PlanePositionVolumeSequenceItem]]):
        if value is None:
            self._PlanePositionVolumeSequence = []
            if "PlanePositionVolumeSequence" in self._dataset:
                del self._dataset.PlanePositionVolumeSequence
        elif not isinstance(value, list) or not all(isinstance(item, PlanePositionVolumeSequenceItem) for item in value):
            raise ValueError("PlanePositionVolumeSequence must be a list of PlanePositionVolumeSequenceItem objects")
        else:
            self._PlanePositionVolumeSequence = value
            if "PlanePositionVolumeSequence" not in self._dataset:
                self._dataset.PlanePositionVolumeSequence = pydicom.Sequence()
            self._dataset.PlanePositionVolumeSequence.clear()
            self._dataset.PlanePositionVolumeSequence.extend([item.to_dataset() for item in value])

    def add_PlanePositionVolume(self, item: PlanePositionVolumeSequenceItem):
        if not isinstance(item, PlanePositionVolumeSequenceItem):
            raise ValueError("Item must be an instance of PlanePositionVolumeSequenceItem")
        self._PlanePositionVolumeSequence.append(item)
        if "PlanePositionVolumeSequence" not in self._dataset:
            self._dataset.PlanePositionVolumeSequence = pydicom.Sequence()
        self._dataset.PlanePositionVolumeSequence.append(item.to_dataset())

    @property
    def PlaneOrientationVolumeSequence(self) -> Optional[List[PlaneOrientationVolumeSequenceItem]]:
        if "PlaneOrientationVolumeSequence" in self._dataset:
            if len(self._PlaneOrientationVolumeSequence) == len(self._dataset.PlaneOrientationVolumeSequence):
                return self._PlaneOrientationVolumeSequence
            else:
                return [PlaneOrientationVolumeSequenceItem(x) for x in self._dataset.PlaneOrientationVolumeSequence]
        return None

    @PlaneOrientationVolumeSequence.setter
    def PlaneOrientationVolumeSequence(self, value: Optional[List[PlaneOrientationVolumeSequenceItem]]):
        if value is None:
            self._PlaneOrientationVolumeSequence = []
            if "PlaneOrientationVolumeSequence" in self._dataset:
                del self._dataset.PlaneOrientationVolumeSequence
        elif not isinstance(value, list) or not all(isinstance(item, PlaneOrientationVolumeSequenceItem) for item in value):
            raise ValueError("PlaneOrientationVolumeSequence must be a list of PlaneOrientationVolumeSequenceItem objects")
        else:
            self._PlaneOrientationVolumeSequence = value
            if "PlaneOrientationVolumeSequence" not in self._dataset:
                self._dataset.PlaneOrientationVolumeSequence = pydicom.Sequence()
            self._dataset.PlaneOrientationVolumeSequence.clear()
            self._dataset.PlaneOrientationVolumeSequence.extend([item.to_dataset() for item in value])

    def add_PlaneOrientationVolume(self, item: PlaneOrientationVolumeSequenceItem):
        if not isinstance(item, PlaneOrientationVolumeSequenceItem):
            raise ValueError("Item must be an instance of PlaneOrientationVolumeSequenceItem")
        self._PlaneOrientationVolumeSequence.append(item)
        if "PlaneOrientationVolumeSequence" not in self._dataset:
            self._dataset.PlaneOrientationVolumeSequence = pydicom.Sequence()
        self._dataset.PlaneOrientationVolumeSequence.append(item.to_dataset())

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
            raise ValueError("TemporalPositionSequence must be a list of TemporalPositionSequenceItem objects")
        else:
            self._TemporalPositionSequence = value
            if "TemporalPositionSequence" not in self._dataset:
                self._dataset.TemporalPositionSequence = pydicom.Sequence()
            self._dataset.TemporalPositionSequence.clear()
            self._dataset.TemporalPositionSequence.extend([item.to_dataset() for item in value])

    def add_TemporalPosition(self, item: TemporalPositionSequenceItem):
        if not isinstance(item, TemporalPositionSequenceItem):
            raise ValueError("Item must be an instance of TemporalPositionSequenceItem")
        self._TemporalPositionSequence.append(item)
        if "TemporalPositionSequence" not in self._dataset:
            self._dataset.TemporalPositionSequence = pydicom.Sequence()
        self._dataset.TemporalPositionSequence.append(item.to_dataset())

    @property
    def PatientOrientationInFrameSequence(self) -> Optional[List[PatientOrientationInFrameSequenceItem]]:
        if "PatientOrientationInFrameSequence" in self._dataset:
            if len(self._PatientOrientationInFrameSequence) == len(self._dataset.PatientOrientationInFrameSequence):
                return self._PatientOrientationInFrameSequence
            else:
                return [PatientOrientationInFrameSequenceItem(x) for x in self._dataset.PatientOrientationInFrameSequence]
        return None

    @PatientOrientationInFrameSequence.setter
    def PatientOrientationInFrameSequence(self, value: Optional[List[PatientOrientationInFrameSequenceItem]]):
        if value is None:
            self._PatientOrientationInFrameSequence = []
            if "PatientOrientationInFrameSequence" in self._dataset:
                del self._dataset.PatientOrientationInFrameSequence
        elif not isinstance(value, list) or not all(isinstance(item, PatientOrientationInFrameSequenceItem) for item in value):
            raise ValueError(
                "PatientOrientationInFrameSequence must be a list of PatientOrientationInFrameSequenceItem objects"
            )
        else:
            self._PatientOrientationInFrameSequence = value
            if "PatientOrientationInFrameSequence" not in self._dataset:
                self._dataset.PatientOrientationInFrameSequence = pydicom.Sequence()
            self._dataset.PatientOrientationInFrameSequence.clear()
            self._dataset.PatientOrientationInFrameSequence.extend([item.to_dataset() for item in value])

    def add_PatientOrientationInFrame(self, item: PatientOrientationInFrameSequenceItem):
        if not isinstance(item, PatientOrientationInFrameSequenceItem):
            raise ValueError("Item must be an instance of PatientOrientationInFrameSequenceItem")
        self._PatientOrientationInFrameSequence.append(item)
        if "PatientOrientationInFrameSequence" not in self._dataset:
            self._dataset.PatientOrientationInFrameSequence = pydicom.Sequence()
        self._dataset.PatientOrientationInFrameSequence.append(item.to_dataset())

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
