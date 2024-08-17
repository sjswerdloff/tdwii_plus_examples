from typing import Any, List, Optional

import pydicom

from .cardiac_synchronization_sequence_item import CardiacSynchronizationSequenceItem
from .derivation_image_sequence_item import DerivationImageSequenceItem
from .frame_anatomy_sequence_item import FrameAnatomySequenceItem
from .frame_content_sequence_item import FrameContentSequenceItem
from .frame_voilut_sequence_item import FrameVOILUTSequenceItem
from .patient_physiological_state_sequence_item import (
    PatientPhysiologicalStateSequenceItem,
)
from .pet_detector_motion_details_sequence_item import (
    PETDetectorMotionDetailsSequenceItem,
)
from .pet_frame_acquisition_sequence_item import PETFrameAcquisitionSequenceItem
from .pet_frame_correction_factors_sequence_item import (
    PETFrameCorrectionFactorsSequenceItem,
)
from .pet_frame_type_sequence_item import PETFrameTypeSequenceItem
from .pet_position_sequence_item import PETPositionSequenceItem
from .pet_reconstruction_sequence_item import PETReconstructionSequenceItem
from .pet_table_dynamics_sequence_item import PETTableDynamicsSequenceItem
from .pixel_measures_sequence_item import PixelMeasuresSequenceItem
from .pixel_value_transformation_sequence_item import (
    PixelValueTransformationSequenceItem,
)
from .plane_orientation_sequence_item import PlaneOrientationSequenceItem
from .plane_position_sequence_item import PlanePositionSequenceItem
from .radiopharmaceutical_usage_sequence_item import (
    RadiopharmaceuticalUsageSequenceItem,
)
from .real_world_value_mapping_sequence_item import RealWorldValueMappingSequenceItem
from .referenced_image_sequence_item import ReferencedImageSequenceItem
from .respiratory_synchronization_sequence_item import (
    RespiratorySynchronizationSequenceItem,
)


class PerFrameFunctionalGroupsSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._ReferencedImageSequence: List[ReferencedImageSequenceItem] = []
        self._DerivationImageSequence: List[DerivationImageSequenceItem] = []
        self._CardiacSynchronizationSequence: List[CardiacSynchronizationSequenceItem] = []
        self._PETFrameAcquisitionSequence: List[PETFrameAcquisitionSequenceItem] = []
        self._PETDetectorMotionDetailsSequence: List[PETDetectorMotionDetailsSequenceItem] = []
        self._PETTableDynamicsSequence: List[PETTableDynamicsSequenceItem] = []
        self._PETPositionSequence: List[PETPositionSequenceItem] = []
        self._PETFrameCorrectionFactorsSequence: List[PETFrameCorrectionFactorsSequenceItem] = []
        self._RadiopharmaceuticalUsageSequence: List[RadiopharmaceuticalUsageSequenceItem] = []
        self._PETReconstructionSequence: List[PETReconstructionSequenceItem] = []
        self._PETFrameTypeSequence: List[PETFrameTypeSequenceItem] = []
        self._PatientPhysiologicalStateSequence: List[PatientPhysiologicalStateSequenceItem] = []
        self._FrameAnatomySequence: List[FrameAnatomySequenceItem] = []
        self._FrameContentSequence: List[FrameContentSequenceItem] = []
        self._PlanePositionSequence: List[PlanePositionSequenceItem] = []
        self._PlaneOrientationSequence: List[PlaneOrientationSequenceItem] = []
        self._RespiratorySynchronizationSequence: List[RespiratorySynchronizationSequenceItem] = []
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
    def PETFrameAcquisitionSequence(self) -> Optional[List[PETFrameAcquisitionSequenceItem]]:
        if "PETFrameAcquisitionSequence" in self._dataset:
            if len(self._PETFrameAcquisitionSequence) == len(self._dataset.PETFrameAcquisitionSequence):
                return self._PETFrameAcquisitionSequence
            else:
                return [PETFrameAcquisitionSequenceItem(x) for x in self._dataset.PETFrameAcquisitionSequence]
        return None

    @PETFrameAcquisitionSequence.setter
    def PETFrameAcquisitionSequence(self, value: Optional[List[PETFrameAcquisitionSequenceItem]]):
        if value is None:
            self._PETFrameAcquisitionSequence = []
            if "PETFrameAcquisitionSequence" in self._dataset:
                del self._dataset.PETFrameAcquisitionSequence
        elif not isinstance(value, list) or not all(isinstance(item, PETFrameAcquisitionSequenceItem) for item in value):
            raise ValueError(f"PETFrameAcquisitionSequence must be a list of PETFrameAcquisitionSequenceItem objects")
        else:
            self._PETFrameAcquisitionSequence = value
            if "PETFrameAcquisitionSequence" not in self._dataset:
                self._dataset.PETFrameAcquisitionSequence = pydicom.Sequence()
            self._dataset.PETFrameAcquisitionSequence.clear()
            self._dataset.PETFrameAcquisitionSequence.extend([item.to_dataset() for item in value])

    def add_PETFrameAcquisition(self, item: PETFrameAcquisitionSequenceItem):
        if not isinstance(item, PETFrameAcquisitionSequenceItem):
            raise ValueError(f"Item must be an instance of PETFrameAcquisitionSequenceItem")
        self._PETFrameAcquisitionSequence.append(item)
        if "PETFrameAcquisitionSequence" not in self._dataset:
            self._dataset.PETFrameAcquisitionSequence = pydicom.Sequence()
        self._dataset.PETFrameAcquisitionSequence.append(item.to_dataset())

    @property
    def PETDetectorMotionDetailsSequence(self) -> Optional[List[PETDetectorMotionDetailsSequenceItem]]:
        if "PETDetectorMotionDetailsSequence" in self._dataset:
            if len(self._PETDetectorMotionDetailsSequence) == len(self._dataset.PETDetectorMotionDetailsSequence):
                return self._PETDetectorMotionDetailsSequence
            else:
                return [PETDetectorMotionDetailsSequenceItem(x) for x in self._dataset.PETDetectorMotionDetailsSequence]
        return None

    @PETDetectorMotionDetailsSequence.setter
    def PETDetectorMotionDetailsSequence(self, value: Optional[List[PETDetectorMotionDetailsSequenceItem]]):
        if value is None:
            self._PETDetectorMotionDetailsSequence = []
            if "PETDetectorMotionDetailsSequence" in self._dataset:
                del self._dataset.PETDetectorMotionDetailsSequence
        elif not isinstance(value, list) or not all(isinstance(item, PETDetectorMotionDetailsSequenceItem) for item in value):
            raise ValueError(
                f"PETDetectorMotionDetailsSequence must be a list of PETDetectorMotionDetailsSequenceItem objects"
            )
        else:
            self._PETDetectorMotionDetailsSequence = value
            if "PETDetectorMotionDetailsSequence" not in self._dataset:
                self._dataset.PETDetectorMotionDetailsSequence = pydicom.Sequence()
            self._dataset.PETDetectorMotionDetailsSequence.clear()
            self._dataset.PETDetectorMotionDetailsSequence.extend([item.to_dataset() for item in value])

    def add_PETDetectorMotionDetails(self, item: PETDetectorMotionDetailsSequenceItem):
        if not isinstance(item, PETDetectorMotionDetailsSequenceItem):
            raise ValueError(f"Item must be an instance of PETDetectorMotionDetailsSequenceItem")
        self._PETDetectorMotionDetailsSequence.append(item)
        if "PETDetectorMotionDetailsSequence" not in self._dataset:
            self._dataset.PETDetectorMotionDetailsSequence = pydicom.Sequence()
        self._dataset.PETDetectorMotionDetailsSequence.append(item.to_dataset())

    @property
    def PETTableDynamicsSequence(self) -> Optional[List[PETTableDynamicsSequenceItem]]:
        if "PETTableDynamicsSequence" in self._dataset:
            if len(self._PETTableDynamicsSequence) == len(self._dataset.PETTableDynamicsSequence):
                return self._PETTableDynamicsSequence
            else:
                return [PETTableDynamicsSequenceItem(x) for x in self._dataset.PETTableDynamicsSequence]
        return None

    @PETTableDynamicsSequence.setter
    def PETTableDynamicsSequence(self, value: Optional[List[PETTableDynamicsSequenceItem]]):
        if value is None:
            self._PETTableDynamicsSequence = []
            if "PETTableDynamicsSequence" in self._dataset:
                del self._dataset.PETTableDynamicsSequence
        elif not isinstance(value, list) or not all(isinstance(item, PETTableDynamicsSequenceItem) for item in value):
            raise ValueError(f"PETTableDynamicsSequence must be a list of PETTableDynamicsSequenceItem objects")
        else:
            self._PETTableDynamicsSequence = value
            if "PETTableDynamicsSequence" not in self._dataset:
                self._dataset.PETTableDynamicsSequence = pydicom.Sequence()
            self._dataset.PETTableDynamicsSequence.clear()
            self._dataset.PETTableDynamicsSequence.extend([item.to_dataset() for item in value])

    def add_PETTableDynamics(self, item: PETTableDynamicsSequenceItem):
        if not isinstance(item, PETTableDynamicsSequenceItem):
            raise ValueError(f"Item must be an instance of PETTableDynamicsSequenceItem")
        self._PETTableDynamicsSequence.append(item)
        if "PETTableDynamicsSequence" not in self._dataset:
            self._dataset.PETTableDynamicsSequence = pydicom.Sequence()
        self._dataset.PETTableDynamicsSequence.append(item.to_dataset())

    @property
    def PETPositionSequence(self) -> Optional[List[PETPositionSequenceItem]]:
        if "PETPositionSequence" in self._dataset:
            if len(self._PETPositionSequence) == len(self._dataset.PETPositionSequence):
                return self._PETPositionSequence
            else:
                return [PETPositionSequenceItem(x) for x in self._dataset.PETPositionSequence]
        return None

    @PETPositionSequence.setter
    def PETPositionSequence(self, value: Optional[List[PETPositionSequenceItem]]):
        if value is None:
            self._PETPositionSequence = []
            if "PETPositionSequence" in self._dataset:
                del self._dataset.PETPositionSequence
        elif not isinstance(value, list) or not all(isinstance(item, PETPositionSequenceItem) for item in value):
            raise ValueError(f"PETPositionSequence must be a list of PETPositionSequenceItem objects")
        else:
            self._PETPositionSequence = value
            if "PETPositionSequence" not in self._dataset:
                self._dataset.PETPositionSequence = pydicom.Sequence()
            self._dataset.PETPositionSequence.clear()
            self._dataset.PETPositionSequence.extend([item.to_dataset() for item in value])

    def add_PETPosition(self, item: PETPositionSequenceItem):
        if not isinstance(item, PETPositionSequenceItem):
            raise ValueError(f"Item must be an instance of PETPositionSequenceItem")
        self._PETPositionSequence.append(item)
        if "PETPositionSequence" not in self._dataset:
            self._dataset.PETPositionSequence = pydicom.Sequence()
        self._dataset.PETPositionSequence.append(item.to_dataset())

    @property
    def PETFrameCorrectionFactorsSequence(self) -> Optional[List[PETFrameCorrectionFactorsSequenceItem]]:
        if "PETFrameCorrectionFactorsSequence" in self._dataset:
            if len(self._PETFrameCorrectionFactorsSequence) == len(self._dataset.PETFrameCorrectionFactorsSequence):
                return self._PETFrameCorrectionFactorsSequence
            else:
                return [PETFrameCorrectionFactorsSequenceItem(x) for x in self._dataset.PETFrameCorrectionFactorsSequence]
        return None

    @PETFrameCorrectionFactorsSequence.setter
    def PETFrameCorrectionFactorsSequence(self, value: Optional[List[PETFrameCorrectionFactorsSequenceItem]]):
        if value is None:
            self._PETFrameCorrectionFactorsSequence = []
            if "PETFrameCorrectionFactorsSequence" in self._dataset:
                del self._dataset.PETFrameCorrectionFactorsSequence
        elif not isinstance(value, list) or not all(isinstance(item, PETFrameCorrectionFactorsSequenceItem) for item in value):
            raise ValueError(
                f"PETFrameCorrectionFactorsSequence must be a list of PETFrameCorrectionFactorsSequenceItem objects"
            )
        else:
            self._PETFrameCorrectionFactorsSequence = value
            if "PETFrameCorrectionFactorsSequence" not in self._dataset:
                self._dataset.PETFrameCorrectionFactorsSequence = pydicom.Sequence()
            self._dataset.PETFrameCorrectionFactorsSequence.clear()
            self._dataset.PETFrameCorrectionFactorsSequence.extend([item.to_dataset() for item in value])

    def add_PETFrameCorrectionFactors(self, item: PETFrameCorrectionFactorsSequenceItem):
        if not isinstance(item, PETFrameCorrectionFactorsSequenceItem):
            raise ValueError(f"Item must be an instance of PETFrameCorrectionFactorsSequenceItem")
        self._PETFrameCorrectionFactorsSequence.append(item)
        if "PETFrameCorrectionFactorsSequence" not in self._dataset:
            self._dataset.PETFrameCorrectionFactorsSequence = pydicom.Sequence()
        self._dataset.PETFrameCorrectionFactorsSequence.append(item.to_dataset())

    @property
    def RadiopharmaceuticalUsageSequence(self) -> Optional[List[RadiopharmaceuticalUsageSequenceItem]]:
        if "RadiopharmaceuticalUsageSequence" in self._dataset:
            if len(self._RadiopharmaceuticalUsageSequence) == len(self._dataset.RadiopharmaceuticalUsageSequence):
                return self._RadiopharmaceuticalUsageSequence
            else:
                return [RadiopharmaceuticalUsageSequenceItem(x) for x in self._dataset.RadiopharmaceuticalUsageSequence]
        return None

    @RadiopharmaceuticalUsageSequence.setter
    def RadiopharmaceuticalUsageSequence(self, value: Optional[List[RadiopharmaceuticalUsageSequenceItem]]):
        if value is None:
            self._RadiopharmaceuticalUsageSequence = []
            if "RadiopharmaceuticalUsageSequence" in self._dataset:
                del self._dataset.RadiopharmaceuticalUsageSequence
        elif not isinstance(value, list) or not all(isinstance(item, RadiopharmaceuticalUsageSequenceItem) for item in value):
            raise ValueError(
                f"RadiopharmaceuticalUsageSequence must be a list of RadiopharmaceuticalUsageSequenceItem objects"
            )
        else:
            self._RadiopharmaceuticalUsageSequence = value
            if "RadiopharmaceuticalUsageSequence" not in self._dataset:
                self._dataset.RadiopharmaceuticalUsageSequence = pydicom.Sequence()
            self._dataset.RadiopharmaceuticalUsageSequence.clear()
            self._dataset.RadiopharmaceuticalUsageSequence.extend([item.to_dataset() for item in value])

    def add_RadiopharmaceuticalUsage(self, item: RadiopharmaceuticalUsageSequenceItem):
        if not isinstance(item, RadiopharmaceuticalUsageSequenceItem):
            raise ValueError(f"Item must be an instance of RadiopharmaceuticalUsageSequenceItem")
        self._RadiopharmaceuticalUsageSequence.append(item)
        if "RadiopharmaceuticalUsageSequence" not in self._dataset:
            self._dataset.RadiopharmaceuticalUsageSequence = pydicom.Sequence()
        self._dataset.RadiopharmaceuticalUsageSequence.append(item.to_dataset())

    @property
    def PETReconstructionSequence(self) -> Optional[List[PETReconstructionSequenceItem]]:
        if "PETReconstructionSequence" in self._dataset:
            if len(self._PETReconstructionSequence) == len(self._dataset.PETReconstructionSequence):
                return self._PETReconstructionSequence
            else:
                return [PETReconstructionSequenceItem(x) for x in self._dataset.PETReconstructionSequence]
        return None

    @PETReconstructionSequence.setter
    def PETReconstructionSequence(self, value: Optional[List[PETReconstructionSequenceItem]]):
        if value is None:
            self._PETReconstructionSequence = []
            if "PETReconstructionSequence" in self._dataset:
                del self._dataset.PETReconstructionSequence
        elif not isinstance(value, list) or not all(isinstance(item, PETReconstructionSequenceItem) for item in value):
            raise ValueError(f"PETReconstructionSequence must be a list of PETReconstructionSequenceItem objects")
        else:
            self._PETReconstructionSequence = value
            if "PETReconstructionSequence" not in self._dataset:
                self._dataset.PETReconstructionSequence = pydicom.Sequence()
            self._dataset.PETReconstructionSequence.clear()
            self._dataset.PETReconstructionSequence.extend([item.to_dataset() for item in value])

    def add_PETReconstruction(self, item: PETReconstructionSequenceItem):
        if not isinstance(item, PETReconstructionSequenceItem):
            raise ValueError(f"Item must be an instance of PETReconstructionSequenceItem")
        self._PETReconstructionSequence.append(item)
        if "PETReconstructionSequence" not in self._dataset:
            self._dataset.PETReconstructionSequence = pydicom.Sequence()
        self._dataset.PETReconstructionSequence.append(item.to_dataset())

    @property
    def PETFrameTypeSequence(self) -> Optional[List[PETFrameTypeSequenceItem]]:
        if "PETFrameTypeSequence" in self._dataset:
            if len(self._PETFrameTypeSequence) == len(self._dataset.PETFrameTypeSequence):
                return self._PETFrameTypeSequence
            else:
                return [PETFrameTypeSequenceItem(x) for x in self._dataset.PETFrameTypeSequence]
        return None

    @PETFrameTypeSequence.setter
    def PETFrameTypeSequence(self, value: Optional[List[PETFrameTypeSequenceItem]]):
        if value is None:
            self._PETFrameTypeSequence = []
            if "PETFrameTypeSequence" in self._dataset:
                del self._dataset.PETFrameTypeSequence
        elif not isinstance(value, list) or not all(isinstance(item, PETFrameTypeSequenceItem) for item in value):
            raise ValueError(f"PETFrameTypeSequence must be a list of PETFrameTypeSequenceItem objects")
        else:
            self._PETFrameTypeSequence = value
            if "PETFrameTypeSequence" not in self._dataset:
                self._dataset.PETFrameTypeSequence = pydicom.Sequence()
            self._dataset.PETFrameTypeSequence.clear()
            self._dataset.PETFrameTypeSequence.extend([item.to_dataset() for item in value])

    def add_PETFrameType(self, item: PETFrameTypeSequenceItem):
        if not isinstance(item, PETFrameTypeSequenceItem):
            raise ValueError(f"Item must be an instance of PETFrameTypeSequenceItem")
        self._PETFrameTypeSequence.append(item)
        if "PETFrameTypeSequence" not in self._dataset:
            self._dataset.PETFrameTypeSequence = pydicom.Sequence()
        self._dataset.PETFrameTypeSequence.append(item.to_dataset())

    @property
    def PatientPhysiologicalStateSequence(self) -> Optional[List[PatientPhysiologicalStateSequenceItem]]:
        if "PatientPhysiologicalStateSequence" in self._dataset:
            if len(self._PatientPhysiologicalStateSequence) == len(self._dataset.PatientPhysiologicalStateSequence):
                return self._PatientPhysiologicalStateSequence
            else:
                return [PatientPhysiologicalStateSequenceItem(x) for x in self._dataset.PatientPhysiologicalStateSequence]
        return None

    @PatientPhysiologicalStateSequence.setter
    def PatientPhysiologicalStateSequence(self, value: Optional[List[PatientPhysiologicalStateSequenceItem]]):
        if value is None:
            self._PatientPhysiologicalStateSequence = []
            if "PatientPhysiologicalStateSequence" in self._dataset:
                del self._dataset.PatientPhysiologicalStateSequence
        elif not isinstance(value, list) or not all(isinstance(item, PatientPhysiologicalStateSequenceItem) for item in value):
            raise ValueError(
                f"PatientPhysiologicalStateSequence must be a list of PatientPhysiologicalStateSequenceItem objects"
            )
        else:
            self._PatientPhysiologicalStateSequence = value
            if "PatientPhysiologicalStateSequence" not in self._dataset:
                self._dataset.PatientPhysiologicalStateSequence = pydicom.Sequence()
            self._dataset.PatientPhysiologicalStateSequence.clear()
            self._dataset.PatientPhysiologicalStateSequence.extend([item.to_dataset() for item in value])

    def add_PatientPhysiologicalState(self, item: PatientPhysiologicalStateSequenceItem):
        if not isinstance(item, PatientPhysiologicalStateSequenceItem):
            raise ValueError(f"Item must be an instance of PatientPhysiologicalStateSequenceItem")
        self._PatientPhysiologicalStateSequence.append(item)
        if "PatientPhysiologicalStateSequence" not in self._dataset:
            self._dataset.PatientPhysiologicalStateSequence = pydicom.Sequence()
        self._dataset.PatientPhysiologicalStateSequence.append(item.to_dataset())

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
