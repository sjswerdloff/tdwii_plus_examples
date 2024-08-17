from typing import Any, List, Optional

import pydicom

from .calibration_sequence_item import CalibrationSequenceItem
from .cardiac_synchronization_sequence_item import CardiacSynchronizationSequenceItem
from .collimator_shape_sequence_item import CollimatorShapeSequenceItem
from .contrast_bolus_usage_sequence_item import ContrastBolusUsageSequenceItem
from .derivation_image_sequence_item import DerivationImageSequenceItem
from .exposure_control_sensing_regions_sequence_item import (
    ExposureControlSensingRegionsSequenceItem,
)
from .field_of_view_sequence_item import FieldOfViewSequenceItem
from .frame_acquisition_sequence_item import FrameAcquisitionSequenceItem
from .frame_anatomy_sequence_item import FrameAnatomySequenceItem
from .frame_content_sequence_item import FrameContentSequenceItem
from .frame_detector_parameters_sequence_item import FrameDetectorParametersSequenceItem
from .frame_display_shutter_sequence_item import FrameDisplayShutterSequenceItem
from .frame_pixel_data_properties_sequence_item import (
    FramePixelDataPropertiesSequenceItem,
)
from .frame_pixel_shift_sequence_item import FramePixelShiftSequenceItem
from .frame_voilut_sequence_item import FrameVOILUTSequenceItem
from .irradiation_event_identification_sequence_item import (
    IrradiationEventIdentificationSequenceItem,
)
from .isocenter_reference_system_sequence_item import (
    IsocenterReferenceSystemSequenceItem,
)
from .object_thickness_sequence_item import ObjectThicknessSequenceItem
from .patient_orientation_in_frame_sequence_item import (
    PatientOrientationInFrameSequenceItem,
)
from .pixel_intensity_relationship_lut_sequence_item import (
    PixelIntensityRelationshipLUTSequenceItem,
)
from .positioner_position_sequence_item import PositionerPositionSequenceItem
from .projection_pixel_calibration_sequence_item import (
    ProjectionPixelCalibrationSequenceItem,
)
from .referenced_image_sequence_item import ReferencedImageSequenceItem
from .respiratory_synchronization_sequence_item import (
    RespiratorySynchronizationSequenceItem,
)
from .table_position_sequence_item import TablePositionSequenceItem
from .x_ray_geometry_sequence_item import XRayGeometrySequenceItem
from .xaxrf_frame_characteristics_sequence_item import (
    XAXRFFrameCharacteristicsSequenceItem,
)


class SharedFunctionalGroupsSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._ReferencedImageSequence: List[ReferencedImageSequenceItem] = []
        self._DerivationImageSequence: List[DerivationImageSequenceItem] = []
        self._CardiacSynchronizationSequence: List[CardiacSynchronizationSequenceItem] = []
        self._ContrastBolusUsageSequence: List[ContrastBolusUsageSequenceItem] = []
        self._ProjectionPixelCalibrationSequence: List[ProjectionPixelCalibrationSequenceItem] = []
        self._PositionerPositionSequence: List[PositionerPositionSequenceItem] = []
        self._TablePositionSequence: List[TablePositionSequenceItem] = []
        self._CollimatorShapeSequence: List[CollimatorShapeSequenceItem] = []
        self._XAXRFFrameCharacteristicsSequence: List[XAXRFFrameCharacteristicsSequenceItem] = []
        self._FrameAcquisitionSequence: List[FrameAcquisitionSequenceItem] = []
        self._FieldOfViewSequence: List[FieldOfViewSequenceItem] = []
        self._ExposureControlSensingRegionsSequence: List[ExposureControlSensingRegionsSequenceItem] = []
        self._FrameDetectorParametersSequence: List[FrameDetectorParametersSequenceItem] = []
        self._CalibrationSequence: List[CalibrationSequenceItem] = []
        self._ObjectThicknessSequence: List[ObjectThicknessSequenceItem] = []
        self._IsocenterReferenceSystemSequence: List[IsocenterReferenceSystemSequenceItem] = []
        self._FrameDisplayShutterSequence: List[FrameDisplayShutterSequenceItem] = []
        self._XRayGeometrySequence: List[XRayGeometrySequenceItem] = []
        self._IrradiationEventIdentificationSequence: List[IrradiationEventIdentificationSequenceItem] = []
        self._FrameAnatomySequence: List[FrameAnatomySequenceItem] = []
        self._FrameContentSequence: List[FrameContentSequenceItem] = []
        self._RespiratorySynchronizationSequence: List[RespiratorySynchronizationSequenceItem] = []
        self._PatientOrientationInFrameSequence: List[PatientOrientationInFrameSequenceItem] = []
        self._FrameVOILUTSequence: List[FrameVOILUTSequenceItem] = []
        self._FramePixelShiftSequence: List[FramePixelShiftSequenceItem] = []
        self._PixelIntensityRelationshipLUTSequence: List[PixelIntensityRelationshipLUTSequenceItem] = []
        self._FramePixelDataPropertiesSequence: List[FramePixelDataPropertiesSequenceItem] = []

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
    def ProjectionPixelCalibrationSequence(self) -> Optional[List[ProjectionPixelCalibrationSequenceItem]]:
        if "ProjectionPixelCalibrationSequence" in self._dataset:
            if len(self._ProjectionPixelCalibrationSequence) == len(self._dataset.ProjectionPixelCalibrationSequence):
                return self._ProjectionPixelCalibrationSequence
            else:
                return [ProjectionPixelCalibrationSequenceItem(x) for x in self._dataset.ProjectionPixelCalibrationSequence]
        return None

    @ProjectionPixelCalibrationSequence.setter
    def ProjectionPixelCalibrationSequence(self, value: Optional[List[ProjectionPixelCalibrationSequenceItem]]):
        if value is None:
            self._ProjectionPixelCalibrationSequence = []
            if "ProjectionPixelCalibrationSequence" in self._dataset:
                del self._dataset.ProjectionPixelCalibrationSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, ProjectionPixelCalibrationSequenceItem) for item in value
        ):
            raise ValueError(
                f"ProjectionPixelCalibrationSequence must be a list of ProjectionPixelCalibrationSequenceItem objects"
            )
        else:
            self._ProjectionPixelCalibrationSequence = value
            if "ProjectionPixelCalibrationSequence" not in self._dataset:
                self._dataset.ProjectionPixelCalibrationSequence = pydicom.Sequence()
            self._dataset.ProjectionPixelCalibrationSequence.clear()
            self._dataset.ProjectionPixelCalibrationSequence.extend([item.to_dataset() for item in value])

    def add_ProjectionPixelCalibration(self, item: ProjectionPixelCalibrationSequenceItem):
        if not isinstance(item, ProjectionPixelCalibrationSequenceItem):
            raise ValueError(f"Item must be an instance of ProjectionPixelCalibrationSequenceItem")
        self._ProjectionPixelCalibrationSequence.append(item)
        if "ProjectionPixelCalibrationSequence" not in self._dataset:
            self._dataset.ProjectionPixelCalibrationSequence = pydicom.Sequence()
        self._dataset.ProjectionPixelCalibrationSequence.append(item.to_dataset())

    @property
    def PositionerPositionSequence(self) -> Optional[List[PositionerPositionSequenceItem]]:
        if "PositionerPositionSequence" in self._dataset:
            if len(self._PositionerPositionSequence) == len(self._dataset.PositionerPositionSequence):
                return self._PositionerPositionSequence
            else:
                return [PositionerPositionSequenceItem(x) for x in self._dataset.PositionerPositionSequence]
        return None

    @PositionerPositionSequence.setter
    def PositionerPositionSequence(self, value: Optional[List[PositionerPositionSequenceItem]]):
        if value is None:
            self._PositionerPositionSequence = []
            if "PositionerPositionSequence" in self._dataset:
                del self._dataset.PositionerPositionSequence
        elif not isinstance(value, list) or not all(isinstance(item, PositionerPositionSequenceItem) for item in value):
            raise ValueError(f"PositionerPositionSequence must be a list of PositionerPositionSequenceItem objects")
        else:
            self._PositionerPositionSequence = value
            if "PositionerPositionSequence" not in self._dataset:
                self._dataset.PositionerPositionSequence = pydicom.Sequence()
            self._dataset.PositionerPositionSequence.clear()
            self._dataset.PositionerPositionSequence.extend([item.to_dataset() for item in value])

    def add_PositionerPosition(self, item: PositionerPositionSequenceItem):
        if not isinstance(item, PositionerPositionSequenceItem):
            raise ValueError(f"Item must be an instance of PositionerPositionSequenceItem")
        self._PositionerPositionSequence.append(item)
        if "PositionerPositionSequence" not in self._dataset:
            self._dataset.PositionerPositionSequence = pydicom.Sequence()
        self._dataset.PositionerPositionSequence.append(item.to_dataset())

    @property
    def TablePositionSequence(self) -> Optional[List[TablePositionSequenceItem]]:
        if "TablePositionSequence" in self._dataset:
            if len(self._TablePositionSequence) == len(self._dataset.TablePositionSequence):
                return self._TablePositionSequence
            else:
                return [TablePositionSequenceItem(x) for x in self._dataset.TablePositionSequence]
        return None

    @TablePositionSequence.setter
    def TablePositionSequence(self, value: Optional[List[TablePositionSequenceItem]]):
        if value is None:
            self._TablePositionSequence = []
            if "TablePositionSequence" in self._dataset:
                del self._dataset.TablePositionSequence
        elif not isinstance(value, list) or not all(isinstance(item, TablePositionSequenceItem) for item in value):
            raise ValueError(f"TablePositionSequence must be a list of TablePositionSequenceItem objects")
        else:
            self._TablePositionSequence = value
            if "TablePositionSequence" not in self._dataset:
                self._dataset.TablePositionSequence = pydicom.Sequence()
            self._dataset.TablePositionSequence.clear()
            self._dataset.TablePositionSequence.extend([item.to_dataset() for item in value])

    def add_TablePosition(self, item: TablePositionSequenceItem):
        if not isinstance(item, TablePositionSequenceItem):
            raise ValueError(f"Item must be an instance of TablePositionSequenceItem")
        self._TablePositionSequence.append(item)
        if "TablePositionSequence" not in self._dataset:
            self._dataset.TablePositionSequence = pydicom.Sequence()
        self._dataset.TablePositionSequence.append(item.to_dataset())

    @property
    def CollimatorShapeSequence(self) -> Optional[List[CollimatorShapeSequenceItem]]:
        if "CollimatorShapeSequence" in self._dataset:
            if len(self._CollimatorShapeSequence) == len(self._dataset.CollimatorShapeSequence):
                return self._CollimatorShapeSequence
            else:
                return [CollimatorShapeSequenceItem(x) for x in self._dataset.CollimatorShapeSequence]
        return None

    @CollimatorShapeSequence.setter
    def CollimatorShapeSequence(self, value: Optional[List[CollimatorShapeSequenceItem]]):
        if value is None:
            self._CollimatorShapeSequence = []
            if "CollimatorShapeSequence" in self._dataset:
                del self._dataset.CollimatorShapeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CollimatorShapeSequenceItem) for item in value):
            raise ValueError(f"CollimatorShapeSequence must be a list of CollimatorShapeSequenceItem objects")
        else:
            self._CollimatorShapeSequence = value
            if "CollimatorShapeSequence" not in self._dataset:
                self._dataset.CollimatorShapeSequence = pydicom.Sequence()
            self._dataset.CollimatorShapeSequence.clear()
            self._dataset.CollimatorShapeSequence.extend([item.to_dataset() for item in value])

    def add_CollimatorShape(self, item: CollimatorShapeSequenceItem):
        if not isinstance(item, CollimatorShapeSequenceItem):
            raise ValueError(f"Item must be an instance of CollimatorShapeSequenceItem")
        self._CollimatorShapeSequence.append(item)
        if "CollimatorShapeSequence" not in self._dataset:
            self._dataset.CollimatorShapeSequence = pydicom.Sequence()
        self._dataset.CollimatorShapeSequence.append(item.to_dataset())

    @property
    def XAXRFFrameCharacteristicsSequence(self) -> Optional[List[XAXRFFrameCharacteristicsSequenceItem]]:
        if "XAXRFFrameCharacteristicsSequence" in self._dataset:
            if len(self._XAXRFFrameCharacteristicsSequence) == len(self._dataset.XAXRFFrameCharacteristicsSequence):
                return self._XAXRFFrameCharacteristicsSequence
            else:
                return [XAXRFFrameCharacteristicsSequenceItem(x) for x in self._dataset.XAXRFFrameCharacteristicsSequence]
        return None

    @XAXRFFrameCharacteristicsSequence.setter
    def XAXRFFrameCharacteristicsSequence(self, value: Optional[List[XAXRFFrameCharacteristicsSequenceItem]]):
        if value is None:
            self._XAXRFFrameCharacteristicsSequence = []
            if "XAXRFFrameCharacteristicsSequence" in self._dataset:
                del self._dataset.XAXRFFrameCharacteristicsSequence
        elif not isinstance(value, list) or not all(isinstance(item, XAXRFFrameCharacteristicsSequenceItem) for item in value):
            raise ValueError(
                f"XAXRFFrameCharacteristicsSequence must be a list of XAXRFFrameCharacteristicsSequenceItem objects"
            )
        else:
            self._XAXRFFrameCharacteristicsSequence = value
            if "XAXRFFrameCharacteristicsSequence" not in self._dataset:
                self._dataset.XAXRFFrameCharacteristicsSequence = pydicom.Sequence()
            self._dataset.XAXRFFrameCharacteristicsSequence.clear()
            self._dataset.XAXRFFrameCharacteristicsSequence.extend([item.to_dataset() for item in value])

    def add_XAXRFFrameCharacteristics(self, item: XAXRFFrameCharacteristicsSequenceItem):
        if not isinstance(item, XAXRFFrameCharacteristicsSequenceItem):
            raise ValueError(f"Item must be an instance of XAXRFFrameCharacteristicsSequenceItem")
        self._XAXRFFrameCharacteristicsSequence.append(item)
        if "XAXRFFrameCharacteristicsSequence" not in self._dataset:
            self._dataset.XAXRFFrameCharacteristicsSequence = pydicom.Sequence()
        self._dataset.XAXRFFrameCharacteristicsSequence.append(item.to_dataset())

    @property
    def FrameAcquisitionSequence(self) -> Optional[List[FrameAcquisitionSequenceItem]]:
        if "FrameAcquisitionSequence" in self._dataset:
            if len(self._FrameAcquisitionSequence) == len(self._dataset.FrameAcquisitionSequence):
                return self._FrameAcquisitionSequence
            else:
                return [FrameAcquisitionSequenceItem(x) for x in self._dataset.FrameAcquisitionSequence]
        return None

    @FrameAcquisitionSequence.setter
    def FrameAcquisitionSequence(self, value: Optional[List[FrameAcquisitionSequenceItem]]):
        if value is None:
            self._FrameAcquisitionSequence = []
            if "FrameAcquisitionSequence" in self._dataset:
                del self._dataset.FrameAcquisitionSequence
        elif not isinstance(value, list) or not all(isinstance(item, FrameAcquisitionSequenceItem) for item in value):
            raise ValueError(f"FrameAcquisitionSequence must be a list of FrameAcquisitionSequenceItem objects")
        else:
            self._FrameAcquisitionSequence = value
            if "FrameAcquisitionSequence" not in self._dataset:
                self._dataset.FrameAcquisitionSequence = pydicom.Sequence()
            self._dataset.FrameAcquisitionSequence.clear()
            self._dataset.FrameAcquisitionSequence.extend([item.to_dataset() for item in value])

    def add_FrameAcquisition(self, item: FrameAcquisitionSequenceItem):
        if not isinstance(item, FrameAcquisitionSequenceItem):
            raise ValueError(f"Item must be an instance of FrameAcquisitionSequenceItem")
        self._FrameAcquisitionSequence.append(item)
        if "FrameAcquisitionSequence" not in self._dataset:
            self._dataset.FrameAcquisitionSequence = pydicom.Sequence()
        self._dataset.FrameAcquisitionSequence.append(item.to_dataset())

    @property
    def FieldOfViewSequence(self) -> Optional[List[FieldOfViewSequenceItem]]:
        if "FieldOfViewSequence" in self._dataset:
            if len(self._FieldOfViewSequence) == len(self._dataset.FieldOfViewSequence):
                return self._FieldOfViewSequence
            else:
                return [FieldOfViewSequenceItem(x) for x in self._dataset.FieldOfViewSequence]
        return None

    @FieldOfViewSequence.setter
    def FieldOfViewSequence(self, value: Optional[List[FieldOfViewSequenceItem]]):
        if value is None:
            self._FieldOfViewSequence = []
            if "FieldOfViewSequence" in self._dataset:
                del self._dataset.FieldOfViewSequence
        elif not isinstance(value, list) or not all(isinstance(item, FieldOfViewSequenceItem) for item in value):
            raise ValueError(f"FieldOfViewSequence must be a list of FieldOfViewSequenceItem objects")
        else:
            self._FieldOfViewSequence = value
            if "FieldOfViewSequence" not in self._dataset:
                self._dataset.FieldOfViewSequence = pydicom.Sequence()
            self._dataset.FieldOfViewSequence.clear()
            self._dataset.FieldOfViewSequence.extend([item.to_dataset() for item in value])

    def add_FieldOfView(self, item: FieldOfViewSequenceItem):
        if not isinstance(item, FieldOfViewSequenceItem):
            raise ValueError(f"Item must be an instance of FieldOfViewSequenceItem")
        self._FieldOfViewSequence.append(item)
        if "FieldOfViewSequence" not in self._dataset:
            self._dataset.FieldOfViewSequence = pydicom.Sequence()
        self._dataset.FieldOfViewSequence.append(item.to_dataset())

    @property
    def ExposureControlSensingRegionsSequence(self) -> Optional[List[ExposureControlSensingRegionsSequenceItem]]:
        if "ExposureControlSensingRegionsSequence" in self._dataset:
            if len(self._ExposureControlSensingRegionsSequence) == len(self._dataset.ExposureControlSensingRegionsSequence):
                return self._ExposureControlSensingRegionsSequence
            else:
                return [
                    ExposureControlSensingRegionsSequenceItem(x) for x in self._dataset.ExposureControlSensingRegionsSequence
                ]
        return None

    @ExposureControlSensingRegionsSequence.setter
    def ExposureControlSensingRegionsSequence(self, value: Optional[List[ExposureControlSensingRegionsSequenceItem]]):
        if value is None:
            self._ExposureControlSensingRegionsSequence = []
            if "ExposureControlSensingRegionsSequence" in self._dataset:
                del self._dataset.ExposureControlSensingRegionsSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, ExposureControlSensingRegionsSequenceItem) for item in value
        ):
            raise ValueError(
                f"ExposureControlSensingRegionsSequence must be a list of ExposureControlSensingRegionsSequenceItem objects"
            )
        else:
            self._ExposureControlSensingRegionsSequence = value
            if "ExposureControlSensingRegionsSequence" not in self._dataset:
                self._dataset.ExposureControlSensingRegionsSequence = pydicom.Sequence()
            self._dataset.ExposureControlSensingRegionsSequence.clear()
            self._dataset.ExposureControlSensingRegionsSequence.extend([item.to_dataset() for item in value])

    def add_ExposureControlSensingRegions(self, item: ExposureControlSensingRegionsSequenceItem):
        if not isinstance(item, ExposureControlSensingRegionsSequenceItem):
            raise ValueError(f"Item must be an instance of ExposureControlSensingRegionsSequenceItem")
        self._ExposureControlSensingRegionsSequence.append(item)
        if "ExposureControlSensingRegionsSequence" not in self._dataset:
            self._dataset.ExposureControlSensingRegionsSequence = pydicom.Sequence()
        self._dataset.ExposureControlSensingRegionsSequence.append(item.to_dataset())

    @property
    def FrameDetectorParametersSequence(self) -> Optional[List[FrameDetectorParametersSequenceItem]]:
        if "FrameDetectorParametersSequence" in self._dataset:
            if len(self._FrameDetectorParametersSequence) == len(self._dataset.FrameDetectorParametersSequence):
                return self._FrameDetectorParametersSequence
            else:
                return [FrameDetectorParametersSequenceItem(x) for x in self._dataset.FrameDetectorParametersSequence]
        return None

    @FrameDetectorParametersSequence.setter
    def FrameDetectorParametersSequence(self, value: Optional[List[FrameDetectorParametersSequenceItem]]):
        if value is None:
            self._FrameDetectorParametersSequence = []
            if "FrameDetectorParametersSequence" in self._dataset:
                del self._dataset.FrameDetectorParametersSequence
        elif not isinstance(value, list) or not all(isinstance(item, FrameDetectorParametersSequenceItem) for item in value):
            raise ValueError(f"FrameDetectorParametersSequence must be a list of FrameDetectorParametersSequenceItem objects")
        else:
            self._FrameDetectorParametersSequence = value
            if "FrameDetectorParametersSequence" not in self._dataset:
                self._dataset.FrameDetectorParametersSequence = pydicom.Sequence()
            self._dataset.FrameDetectorParametersSequence.clear()
            self._dataset.FrameDetectorParametersSequence.extend([item.to_dataset() for item in value])

    def add_FrameDetectorParameters(self, item: FrameDetectorParametersSequenceItem):
        if not isinstance(item, FrameDetectorParametersSequenceItem):
            raise ValueError(f"Item must be an instance of FrameDetectorParametersSequenceItem")
        self._FrameDetectorParametersSequence.append(item)
        if "FrameDetectorParametersSequence" not in self._dataset:
            self._dataset.FrameDetectorParametersSequence = pydicom.Sequence()
        self._dataset.FrameDetectorParametersSequence.append(item.to_dataset())

    @property
    def CalibrationSequence(self) -> Optional[List[CalibrationSequenceItem]]:
        if "CalibrationSequence" in self._dataset:
            if len(self._CalibrationSequence) == len(self._dataset.CalibrationSequence):
                return self._CalibrationSequence
            else:
                return [CalibrationSequenceItem(x) for x in self._dataset.CalibrationSequence]
        return None

    @CalibrationSequence.setter
    def CalibrationSequence(self, value: Optional[List[CalibrationSequenceItem]]):
        if value is None:
            self._CalibrationSequence = []
            if "CalibrationSequence" in self._dataset:
                del self._dataset.CalibrationSequence
        elif not isinstance(value, list) or not all(isinstance(item, CalibrationSequenceItem) for item in value):
            raise ValueError(f"CalibrationSequence must be a list of CalibrationSequenceItem objects")
        else:
            self._CalibrationSequence = value
            if "CalibrationSequence" not in self._dataset:
                self._dataset.CalibrationSequence = pydicom.Sequence()
            self._dataset.CalibrationSequence.clear()
            self._dataset.CalibrationSequence.extend([item.to_dataset() for item in value])

    def add_Calibration(self, item: CalibrationSequenceItem):
        if not isinstance(item, CalibrationSequenceItem):
            raise ValueError(f"Item must be an instance of CalibrationSequenceItem")
        self._CalibrationSequence.append(item)
        if "CalibrationSequence" not in self._dataset:
            self._dataset.CalibrationSequence = pydicom.Sequence()
        self._dataset.CalibrationSequence.append(item.to_dataset())

    @property
    def ObjectThicknessSequence(self) -> Optional[List[ObjectThicknessSequenceItem]]:
        if "ObjectThicknessSequence" in self._dataset:
            if len(self._ObjectThicknessSequence) == len(self._dataset.ObjectThicknessSequence):
                return self._ObjectThicknessSequence
            else:
                return [ObjectThicknessSequenceItem(x) for x in self._dataset.ObjectThicknessSequence]
        return None

    @ObjectThicknessSequence.setter
    def ObjectThicknessSequence(self, value: Optional[List[ObjectThicknessSequenceItem]]):
        if value is None:
            self._ObjectThicknessSequence = []
            if "ObjectThicknessSequence" in self._dataset:
                del self._dataset.ObjectThicknessSequence
        elif not isinstance(value, list) or not all(isinstance(item, ObjectThicknessSequenceItem) for item in value):
            raise ValueError(f"ObjectThicknessSequence must be a list of ObjectThicknessSequenceItem objects")
        else:
            self._ObjectThicknessSequence = value
            if "ObjectThicknessSequence" not in self._dataset:
                self._dataset.ObjectThicknessSequence = pydicom.Sequence()
            self._dataset.ObjectThicknessSequence.clear()
            self._dataset.ObjectThicknessSequence.extend([item.to_dataset() for item in value])

    def add_ObjectThickness(self, item: ObjectThicknessSequenceItem):
        if not isinstance(item, ObjectThicknessSequenceItem):
            raise ValueError(f"Item must be an instance of ObjectThicknessSequenceItem")
        self._ObjectThicknessSequence.append(item)
        if "ObjectThicknessSequence" not in self._dataset:
            self._dataset.ObjectThicknessSequence = pydicom.Sequence()
        self._dataset.ObjectThicknessSequence.append(item.to_dataset())

    @property
    def IsocenterReferenceSystemSequence(self) -> Optional[List[IsocenterReferenceSystemSequenceItem]]:
        if "IsocenterReferenceSystemSequence" in self._dataset:
            if len(self._IsocenterReferenceSystemSequence) == len(self._dataset.IsocenterReferenceSystemSequence):
                return self._IsocenterReferenceSystemSequence
            else:
                return [IsocenterReferenceSystemSequenceItem(x) for x in self._dataset.IsocenterReferenceSystemSequence]
        return None

    @IsocenterReferenceSystemSequence.setter
    def IsocenterReferenceSystemSequence(self, value: Optional[List[IsocenterReferenceSystemSequenceItem]]):
        if value is None:
            self._IsocenterReferenceSystemSequence = []
            if "IsocenterReferenceSystemSequence" in self._dataset:
                del self._dataset.IsocenterReferenceSystemSequence
        elif not isinstance(value, list) or not all(isinstance(item, IsocenterReferenceSystemSequenceItem) for item in value):
            raise ValueError(
                f"IsocenterReferenceSystemSequence must be a list of IsocenterReferenceSystemSequenceItem objects"
            )
        else:
            self._IsocenterReferenceSystemSequence = value
            if "IsocenterReferenceSystemSequence" not in self._dataset:
                self._dataset.IsocenterReferenceSystemSequence = pydicom.Sequence()
            self._dataset.IsocenterReferenceSystemSequence.clear()
            self._dataset.IsocenterReferenceSystemSequence.extend([item.to_dataset() for item in value])

    def add_IsocenterReferenceSystem(self, item: IsocenterReferenceSystemSequenceItem):
        if not isinstance(item, IsocenterReferenceSystemSequenceItem):
            raise ValueError(f"Item must be an instance of IsocenterReferenceSystemSequenceItem")
        self._IsocenterReferenceSystemSequence.append(item)
        if "IsocenterReferenceSystemSequence" not in self._dataset:
            self._dataset.IsocenterReferenceSystemSequence = pydicom.Sequence()
        self._dataset.IsocenterReferenceSystemSequence.append(item.to_dataset())

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
            raise ValueError(f"FrameDisplayShutterSequence must be a list of FrameDisplayShutterSequenceItem objects")
        else:
            self._FrameDisplayShutterSequence = value
            if "FrameDisplayShutterSequence" not in self._dataset:
                self._dataset.FrameDisplayShutterSequence = pydicom.Sequence()
            self._dataset.FrameDisplayShutterSequence.clear()
            self._dataset.FrameDisplayShutterSequence.extend([item.to_dataset() for item in value])

    def add_FrameDisplayShutter(self, item: FrameDisplayShutterSequenceItem):
        if not isinstance(item, FrameDisplayShutterSequenceItem):
            raise ValueError(f"Item must be an instance of FrameDisplayShutterSequenceItem")
        self._FrameDisplayShutterSequence.append(item)
        if "FrameDisplayShutterSequence" not in self._dataset:
            self._dataset.FrameDisplayShutterSequence = pydicom.Sequence()
        self._dataset.FrameDisplayShutterSequence.append(item.to_dataset())

    @property
    def XRayGeometrySequence(self) -> Optional[List[XRayGeometrySequenceItem]]:
        if "XRayGeometrySequence" in self._dataset:
            if len(self._XRayGeometrySequence) == len(self._dataset.XRayGeometrySequence):
                return self._XRayGeometrySequence
            else:
                return [XRayGeometrySequenceItem(x) for x in self._dataset.XRayGeometrySequence]
        return None

    @XRayGeometrySequence.setter
    def XRayGeometrySequence(self, value: Optional[List[XRayGeometrySequenceItem]]):
        if value is None:
            self._XRayGeometrySequence = []
            if "XRayGeometrySequence" in self._dataset:
                del self._dataset.XRayGeometrySequence
        elif not isinstance(value, list) or not all(isinstance(item, XRayGeometrySequenceItem) for item in value):
            raise ValueError(f"XRayGeometrySequence must be a list of XRayGeometrySequenceItem objects")
        else:
            self._XRayGeometrySequence = value
            if "XRayGeometrySequence" not in self._dataset:
                self._dataset.XRayGeometrySequence = pydicom.Sequence()
            self._dataset.XRayGeometrySequence.clear()
            self._dataset.XRayGeometrySequence.extend([item.to_dataset() for item in value])

    def add_XRayGeometry(self, item: XRayGeometrySequenceItem):
        if not isinstance(item, XRayGeometrySequenceItem):
            raise ValueError(f"Item must be an instance of XRayGeometrySequenceItem")
        self._XRayGeometrySequence.append(item)
        if "XRayGeometrySequence" not in self._dataset:
            self._dataset.XRayGeometrySequence = pydicom.Sequence()
        self._dataset.XRayGeometrySequence.append(item.to_dataset())

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
                f"PatientOrientationInFrameSequence must be a list of PatientOrientationInFrameSequenceItem objects"
            )
        else:
            self._PatientOrientationInFrameSequence = value
            if "PatientOrientationInFrameSequence" not in self._dataset:
                self._dataset.PatientOrientationInFrameSequence = pydicom.Sequence()
            self._dataset.PatientOrientationInFrameSequence.clear()
            self._dataset.PatientOrientationInFrameSequence.extend([item.to_dataset() for item in value])

    def add_PatientOrientationInFrame(self, item: PatientOrientationInFrameSequenceItem):
        if not isinstance(item, PatientOrientationInFrameSequenceItem):
            raise ValueError(f"Item must be an instance of PatientOrientationInFrameSequenceItem")
        self._PatientOrientationInFrameSequence.append(item)
        if "PatientOrientationInFrameSequence" not in self._dataset:
            self._dataset.PatientOrientationInFrameSequence = pydicom.Sequence()
        self._dataset.PatientOrientationInFrameSequence.append(item.to_dataset())

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
    def FramePixelShiftSequence(self) -> Optional[List[FramePixelShiftSequenceItem]]:
        if "FramePixelShiftSequence" in self._dataset:
            if len(self._FramePixelShiftSequence) == len(self._dataset.FramePixelShiftSequence):
                return self._FramePixelShiftSequence
            else:
                return [FramePixelShiftSequenceItem(x) for x in self._dataset.FramePixelShiftSequence]
        return None

    @FramePixelShiftSequence.setter
    def FramePixelShiftSequence(self, value: Optional[List[FramePixelShiftSequenceItem]]):
        if value is None:
            self._FramePixelShiftSequence = []
            if "FramePixelShiftSequence" in self._dataset:
                del self._dataset.FramePixelShiftSequence
        elif not isinstance(value, list) or not all(isinstance(item, FramePixelShiftSequenceItem) for item in value):
            raise ValueError(f"FramePixelShiftSequence must be a list of FramePixelShiftSequenceItem objects")
        else:
            self._FramePixelShiftSequence = value
            if "FramePixelShiftSequence" not in self._dataset:
                self._dataset.FramePixelShiftSequence = pydicom.Sequence()
            self._dataset.FramePixelShiftSequence.clear()
            self._dataset.FramePixelShiftSequence.extend([item.to_dataset() for item in value])

    def add_FramePixelShift(self, item: FramePixelShiftSequenceItem):
        if not isinstance(item, FramePixelShiftSequenceItem):
            raise ValueError(f"Item must be an instance of FramePixelShiftSequenceItem")
        self._FramePixelShiftSequence.append(item)
        if "FramePixelShiftSequence" not in self._dataset:
            self._dataset.FramePixelShiftSequence = pydicom.Sequence()
        self._dataset.FramePixelShiftSequence.append(item.to_dataset())

    @property
    def PixelIntensityRelationshipLUTSequence(self) -> Optional[List[PixelIntensityRelationshipLUTSequenceItem]]:
        if "PixelIntensityRelationshipLUTSequence" in self._dataset:
            if len(self._PixelIntensityRelationshipLUTSequence) == len(self._dataset.PixelIntensityRelationshipLUTSequence):
                return self._PixelIntensityRelationshipLUTSequence
            else:
                return [
                    PixelIntensityRelationshipLUTSequenceItem(x) for x in self._dataset.PixelIntensityRelationshipLUTSequence
                ]
        return None

    @PixelIntensityRelationshipLUTSequence.setter
    def PixelIntensityRelationshipLUTSequence(self, value: Optional[List[PixelIntensityRelationshipLUTSequenceItem]]):
        if value is None:
            self._PixelIntensityRelationshipLUTSequence = []
            if "PixelIntensityRelationshipLUTSequence" in self._dataset:
                del self._dataset.PixelIntensityRelationshipLUTSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, PixelIntensityRelationshipLUTSequenceItem) for item in value
        ):
            raise ValueError(
                f"PixelIntensityRelationshipLUTSequence must be a list of PixelIntensityRelationshipLUTSequenceItem objects"
            )
        else:
            self._PixelIntensityRelationshipLUTSequence = value
            if "PixelIntensityRelationshipLUTSequence" not in self._dataset:
                self._dataset.PixelIntensityRelationshipLUTSequence = pydicom.Sequence()
            self._dataset.PixelIntensityRelationshipLUTSequence.clear()
            self._dataset.PixelIntensityRelationshipLUTSequence.extend([item.to_dataset() for item in value])

    def add_PixelIntensityRelationshipLUT(self, item: PixelIntensityRelationshipLUTSequenceItem):
        if not isinstance(item, PixelIntensityRelationshipLUTSequenceItem):
            raise ValueError(f"Item must be an instance of PixelIntensityRelationshipLUTSequenceItem")
        self._PixelIntensityRelationshipLUTSequence.append(item)
        if "PixelIntensityRelationshipLUTSequence" not in self._dataset:
            self._dataset.PixelIntensityRelationshipLUTSequence = pydicom.Sequence()
        self._dataset.PixelIntensityRelationshipLUTSequence.append(item.to_dataset())

    @property
    def FramePixelDataPropertiesSequence(self) -> Optional[List[FramePixelDataPropertiesSequenceItem]]:
        if "FramePixelDataPropertiesSequence" in self._dataset:
            if len(self._FramePixelDataPropertiesSequence) == len(self._dataset.FramePixelDataPropertiesSequence):
                return self._FramePixelDataPropertiesSequence
            else:
                return [FramePixelDataPropertiesSequenceItem(x) for x in self._dataset.FramePixelDataPropertiesSequence]
        return None

    @FramePixelDataPropertiesSequence.setter
    def FramePixelDataPropertiesSequence(self, value: Optional[List[FramePixelDataPropertiesSequenceItem]]):
        if value is None:
            self._FramePixelDataPropertiesSequence = []
            if "FramePixelDataPropertiesSequence" in self._dataset:
                del self._dataset.FramePixelDataPropertiesSequence
        elif not isinstance(value, list) or not all(isinstance(item, FramePixelDataPropertiesSequenceItem) for item in value):
            raise ValueError(
                f"FramePixelDataPropertiesSequence must be a list of FramePixelDataPropertiesSequenceItem objects"
            )
        else:
            self._FramePixelDataPropertiesSequence = value
            if "FramePixelDataPropertiesSequence" not in self._dataset:
                self._dataset.FramePixelDataPropertiesSequence = pydicom.Sequence()
            self._dataset.FramePixelDataPropertiesSequence.clear()
            self._dataset.FramePixelDataPropertiesSequence.extend([item.to_dataset() for item in value])

    def add_FramePixelDataProperties(self, item: FramePixelDataPropertiesSequenceItem):
        if not isinstance(item, FramePixelDataPropertiesSequenceItem):
            raise ValueError(f"Item must be an instance of FramePixelDataPropertiesSequenceItem")
        self._FramePixelDataPropertiesSequence.append(item)
        if "FramePixelDataPropertiesSequence" not in self._dataset:
            self._dataset.FramePixelDataPropertiesSequence = pydicom.Sequence()
        self._dataset.FramePixelDataPropertiesSequence.append(item.to_dataset())
