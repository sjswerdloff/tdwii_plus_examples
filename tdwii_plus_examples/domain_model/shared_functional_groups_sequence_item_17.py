from decimal import Decimal
from typing import Any, List, Optional  # noqa

import pydicom

from .calibration_sequence_item import CalibrationSequenceItem
from .collimator_shape_sequence_item import CollimatorShapeSequenceItem
from .contrast_bolus_usage_sequence_item import ContrastBolusUsageSequenceItem
from .derivation_image_sequence_item import DerivationImageSequenceItem
from .detector_position_sequence_item import DetectorPositionSequenceItem
from .field_of_view_sequence_item import FieldOfViewSequenceItem
from .frame_acquisition_sequence_item import FrameAcquisitionSequenceItem
from .frame_anatomy_sequence_item import FrameAnatomySequenceItem
from .frame_content_sequence_item import FrameContentSequenceItem
from .frame_detector_parameters_sequence_item import FrameDetectorParametersSequenceItem
from .frame_display_shutter_sequence_item import FrameDisplayShutterSequenceItem
from .frame_pixel_data_properties_sequence_item import (
    FramePixelDataPropertiesSequenceItem,
)
from .frame_voilut_sequence_item import FrameVOILUTSequenceItem
from .irradiation_event_identification_sequence_item import (
    IrradiationEventIdentificationSequenceItem,
)
from .isocenter_reference_system_sequence_item import (
    IsocenterReferenceSystemSequenceItem,
)
from .pixel_value_transformation_sequence_item import (
    PixelValueTransformationSequenceItem,
)
from .positioner_position_sequence_item import PositionerPositionSequenceItem
from .referenced_image_sequence_item import ReferencedImageSequenceItem
from .x_ray_acquisition_dose_sequence_item import XRayAcquisitionDoseSequenceItem
from .x_ray_filter_sequence_item import XRayFilterSequenceItem
from .x_ray_geometry_sequence_item import XRayGeometrySequenceItem
from .x_ray_grid_sequence_item import XRayGridSequenceItem
from .xaxrf_frame_characteristics_sequence_item import (
    XAXRFFrameCharacteristicsSequenceItem,
)


class SharedFunctionalGroupsSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._ReferencedImageSequence: List[ReferencedImageSequenceItem] = []
        self._DerivationImageSequence: List[DerivationImageSequenceItem] = []
        self._ContrastBolusUsageSequence: List[ContrastBolusUsageSequenceItem] = []
        self._PositionerPositionSequence: List[PositionerPositionSequenceItem] = []
        self._CollimatorShapeSequence: List[CollimatorShapeSequenceItem] = []
        self._XAXRFFrameCharacteristicsSequence: List[XAXRFFrameCharacteristicsSequenceItem] = []
        self._FrameAcquisitionSequence: List[FrameAcquisitionSequenceItem] = []
        self._FieldOfViewSequence: List[FieldOfViewSequenceItem] = []
        self._FrameDetectorParametersSequence: List[FrameDetectorParametersSequenceItem] = []
        self._CalibrationSequence: List[CalibrationSequenceItem] = []
        self._IsocenterReferenceSystemSequence: List[IsocenterReferenceSystemSequenceItem] = []
        self._FrameDisplayShutterSequence: List[FrameDisplayShutterSequenceItem] = []
        self._XRayGeometrySequence: List[XRayGeometrySequenceItem] = []
        self._IrradiationEventIdentificationSequence: List[IrradiationEventIdentificationSequenceItem] = []
        self._DetectorPositionSequence: List[DetectorPositionSequenceItem] = []
        self._XRayAcquisitionDoseSequence: List[XRayAcquisitionDoseSequenceItem] = []
        self._XRayGridSequence: List[XRayGridSequenceItem] = []
        self._XRayFilterSequence: List[XRayFilterSequenceItem] = []
        self._FrameAnatomySequence: List[FrameAnatomySequenceItem] = []
        self._FrameContentSequence: List[FrameContentSequenceItem] = []
        self._FrameVOILUTSequence: List[FrameVOILUTSequenceItem] = []
        self._PixelValueTransformationSequence: List[PixelValueTransformationSequenceItem] = []
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
    def GridID(self) -> Optional[str]:
        if "GridID" in self._dataset:
            return self._dataset.GridID
        return None

    @GridID.setter
    def GridID(self, value: Optional[str]):
        if value is None:
            if "GridID" in self._dataset:
                del self._dataset.GridID
        else:
            self._dataset.GridID = value

    @property
    def GridAbsorbingMaterial(self) -> Optional[str]:
        if "GridAbsorbingMaterial" in self._dataset:
            return self._dataset.GridAbsorbingMaterial
        return None

    @GridAbsorbingMaterial.setter
    def GridAbsorbingMaterial(self, value: Optional[str]):
        if value is None:
            if "GridAbsorbingMaterial" in self._dataset:
                del self._dataset.GridAbsorbingMaterial
        else:
            self._dataset.GridAbsorbingMaterial = value

    @property
    def GridSpacingMaterial(self) -> Optional[str]:
        if "GridSpacingMaterial" in self._dataset:
            return self._dataset.GridSpacingMaterial
        return None

    @GridSpacingMaterial.setter
    def GridSpacingMaterial(self, value: Optional[str]):
        if value is None:
            if "GridSpacingMaterial" in self._dataset:
                del self._dataset.GridSpacingMaterial
        else:
            self._dataset.GridSpacingMaterial = value

    @property
    def GridThickness(self) -> Optional[Decimal]:
        if "GridThickness" in self._dataset:
            return self._dataset.GridThickness
        return None

    @GridThickness.setter
    def GridThickness(self, value: Optional[Decimal]):
        if value is None:
            if "GridThickness" in self._dataset:
                del self._dataset.GridThickness
        else:
            self._dataset.GridThickness = value

    @property
    def GridPitch(self) -> Optional[Decimal]:
        if "GridPitch" in self._dataset:
            return self._dataset.GridPitch
        return None

    @GridPitch.setter
    def GridPitch(self, value: Optional[Decimal]):
        if value is None:
            if "GridPitch" in self._dataset:
                del self._dataset.GridPitch
        else:
            self._dataset.GridPitch = value

    @property
    def GridAspectRatio(self) -> Optional[List[int]]:
        if "GridAspectRatio" in self._dataset:
            return self._dataset.GridAspectRatio
        return None

    @GridAspectRatio.setter
    def GridAspectRatio(self, value: Optional[List[int]]):
        if value is None:
            if "GridAspectRatio" in self._dataset:
                del self._dataset.GridAspectRatio
        else:
            self._dataset.GridAspectRatio = value

    @property
    def GridPeriod(self) -> Optional[Decimal]:
        if "GridPeriod" in self._dataset:
            return self._dataset.GridPeriod
        return None

    @GridPeriod.setter
    def GridPeriod(self, value: Optional[Decimal]):
        if value is None:
            if "GridPeriod" in self._dataset:
                del self._dataset.GridPeriod
        else:
            self._dataset.GridPeriod = value

    @property
    def GridFocalDistance(self) -> Optional[Decimal]:
        if "GridFocalDistance" in self._dataset:
            return self._dataset.GridFocalDistance
        return None

    @GridFocalDistance.setter
    def GridFocalDistance(self, value: Optional[Decimal]):
        if value is None:
            if "GridFocalDistance" in self._dataset:
                del self._dataset.GridFocalDistance
        else:
            self._dataset.GridFocalDistance = value

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
            raise ValueError("PositionerPositionSequence must be a list of PositionerPositionSequenceItem objects")
        else:
            self._PositionerPositionSequence = value
            if "PositionerPositionSequence" not in self._dataset:
                self._dataset.PositionerPositionSequence = pydicom.Sequence()
            self._dataset.PositionerPositionSequence.clear()
            self._dataset.PositionerPositionSequence.extend([item.to_dataset() for item in value])

    def add_PositionerPosition(self, item: PositionerPositionSequenceItem):
        if not isinstance(item, PositionerPositionSequenceItem):
            raise ValueError("Item must be an instance of PositionerPositionSequenceItem")
        self._PositionerPositionSequence.append(item)
        if "PositionerPositionSequence" not in self._dataset:
            self._dataset.PositionerPositionSequence = pydicom.Sequence()
        self._dataset.PositionerPositionSequence.append(item.to_dataset())

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
            raise ValueError("CollimatorShapeSequence must be a list of CollimatorShapeSequenceItem objects")
        else:
            self._CollimatorShapeSequence = value
            if "CollimatorShapeSequence" not in self._dataset:
                self._dataset.CollimatorShapeSequence = pydicom.Sequence()
            self._dataset.CollimatorShapeSequence.clear()
            self._dataset.CollimatorShapeSequence.extend([item.to_dataset() for item in value])

    def add_CollimatorShape(self, item: CollimatorShapeSequenceItem):
        if not isinstance(item, CollimatorShapeSequenceItem):
            raise ValueError("Item must be an instance of CollimatorShapeSequenceItem")
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
                "XAXRFFrameCharacteristicsSequence must be a list of XAXRFFrameCharacteristicsSequenceItem objects"
            )
        else:
            self._XAXRFFrameCharacteristicsSequence = value
            if "XAXRFFrameCharacteristicsSequence" not in self._dataset:
                self._dataset.XAXRFFrameCharacteristicsSequence = pydicom.Sequence()
            self._dataset.XAXRFFrameCharacteristicsSequence.clear()
            self._dataset.XAXRFFrameCharacteristicsSequence.extend([item.to_dataset() for item in value])

    def add_XAXRFFrameCharacteristics(self, item: XAXRFFrameCharacteristicsSequenceItem):
        if not isinstance(item, XAXRFFrameCharacteristicsSequenceItem):
            raise ValueError("Item must be an instance of XAXRFFrameCharacteristicsSequenceItem")
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
            raise ValueError("FrameAcquisitionSequence must be a list of FrameAcquisitionSequenceItem objects")
        else:
            self._FrameAcquisitionSequence = value
            if "FrameAcquisitionSequence" not in self._dataset:
                self._dataset.FrameAcquisitionSequence = pydicom.Sequence()
            self._dataset.FrameAcquisitionSequence.clear()
            self._dataset.FrameAcquisitionSequence.extend([item.to_dataset() for item in value])

    def add_FrameAcquisition(self, item: FrameAcquisitionSequenceItem):
        if not isinstance(item, FrameAcquisitionSequenceItem):
            raise ValueError("Item must be an instance of FrameAcquisitionSequenceItem")
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
            raise ValueError("FieldOfViewSequence must be a list of FieldOfViewSequenceItem objects")
        else:
            self._FieldOfViewSequence = value
            if "FieldOfViewSequence" not in self._dataset:
                self._dataset.FieldOfViewSequence = pydicom.Sequence()
            self._dataset.FieldOfViewSequence.clear()
            self._dataset.FieldOfViewSequence.extend([item.to_dataset() for item in value])

    def add_FieldOfView(self, item: FieldOfViewSequenceItem):
        if not isinstance(item, FieldOfViewSequenceItem):
            raise ValueError("Item must be an instance of FieldOfViewSequenceItem")
        self._FieldOfViewSequence.append(item)
        if "FieldOfViewSequence" not in self._dataset:
            self._dataset.FieldOfViewSequence = pydicom.Sequence()
        self._dataset.FieldOfViewSequence.append(item.to_dataset())

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
            raise ValueError("FrameDetectorParametersSequence must be a list of FrameDetectorParametersSequenceItem objects")
        else:
            self._FrameDetectorParametersSequence = value
            if "FrameDetectorParametersSequence" not in self._dataset:
                self._dataset.FrameDetectorParametersSequence = pydicom.Sequence()
            self._dataset.FrameDetectorParametersSequence.clear()
            self._dataset.FrameDetectorParametersSequence.extend([item.to_dataset() for item in value])

    def add_FrameDetectorParameters(self, item: FrameDetectorParametersSequenceItem):
        if not isinstance(item, FrameDetectorParametersSequenceItem):
            raise ValueError("Item must be an instance of FrameDetectorParametersSequenceItem")
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
            raise ValueError("CalibrationSequence must be a list of CalibrationSequenceItem objects")
        else:
            self._CalibrationSequence = value
            if "CalibrationSequence" not in self._dataset:
                self._dataset.CalibrationSequence = pydicom.Sequence()
            self._dataset.CalibrationSequence.clear()
            self._dataset.CalibrationSequence.extend([item.to_dataset() for item in value])

    def add_Calibration(self, item: CalibrationSequenceItem):
        if not isinstance(item, CalibrationSequenceItem):
            raise ValueError("Item must be an instance of CalibrationSequenceItem")
        self._CalibrationSequence.append(item)
        if "CalibrationSequence" not in self._dataset:
            self._dataset.CalibrationSequence = pydicom.Sequence()
        self._dataset.CalibrationSequence.append(item.to_dataset())

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
            raise ValueError("IsocenterReferenceSystemSequence must be a list of IsocenterReferenceSystemSequenceItem objects")
        else:
            self._IsocenterReferenceSystemSequence = value
            if "IsocenterReferenceSystemSequence" not in self._dataset:
                self._dataset.IsocenterReferenceSystemSequence = pydicom.Sequence()
            self._dataset.IsocenterReferenceSystemSequence.clear()
            self._dataset.IsocenterReferenceSystemSequence.extend([item.to_dataset() for item in value])

    def add_IsocenterReferenceSystem(self, item: IsocenterReferenceSystemSequenceItem):
        if not isinstance(item, IsocenterReferenceSystemSequenceItem):
            raise ValueError("Item must be an instance of IsocenterReferenceSystemSequenceItem")
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
            raise ValueError("XRayGeometrySequence must be a list of XRayGeometrySequenceItem objects")
        else:
            self._XRayGeometrySequence = value
            if "XRayGeometrySequence" not in self._dataset:
                self._dataset.XRayGeometrySequence = pydicom.Sequence()
            self._dataset.XRayGeometrySequence.clear()
            self._dataset.XRayGeometrySequence.extend([item.to_dataset() for item in value])

    def add_XRayGeometry(self, item: XRayGeometrySequenceItem):
        if not isinstance(item, XRayGeometrySequenceItem):
            raise ValueError("Item must be an instance of XRayGeometrySequenceItem")
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
                "IrradiationEventIdentificationSequence must be a list of IrradiationEventIdentificationSequenceItem objects"
            )
        else:
            self._IrradiationEventIdentificationSequence = value
            if "IrradiationEventIdentificationSequence" not in self._dataset:
                self._dataset.IrradiationEventIdentificationSequence = pydicom.Sequence()
            self._dataset.IrradiationEventIdentificationSequence.clear()
            self._dataset.IrradiationEventIdentificationSequence.extend([item.to_dataset() for item in value])

    def add_IrradiationEventIdentification(self, item: IrradiationEventIdentificationSequenceItem):
        if not isinstance(item, IrradiationEventIdentificationSequenceItem):
            raise ValueError("Item must be an instance of IrradiationEventIdentificationSequenceItem")
        self._IrradiationEventIdentificationSequence.append(item)
        if "IrradiationEventIdentificationSequence" not in self._dataset:
            self._dataset.IrradiationEventIdentificationSequence = pydicom.Sequence()
        self._dataset.IrradiationEventIdentificationSequence.append(item.to_dataset())

    @property
    def DetectorPositionSequence(self) -> Optional[List[DetectorPositionSequenceItem]]:
        if "DetectorPositionSequence" in self._dataset:
            if len(self._DetectorPositionSequence) == len(self._dataset.DetectorPositionSequence):
                return self._DetectorPositionSequence
            else:
                return [DetectorPositionSequenceItem(x) for x in self._dataset.DetectorPositionSequence]
        return None

    @DetectorPositionSequence.setter
    def DetectorPositionSequence(self, value: Optional[List[DetectorPositionSequenceItem]]):
        if value is None:
            self._DetectorPositionSequence = []
            if "DetectorPositionSequence" in self._dataset:
                del self._dataset.DetectorPositionSequence
        elif not isinstance(value, list) or not all(isinstance(item, DetectorPositionSequenceItem) for item in value):
            raise ValueError("DetectorPositionSequence must be a list of DetectorPositionSequenceItem objects")
        else:
            self._DetectorPositionSequence = value
            if "DetectorPositionSequence" not in self._dataset:
                self._dataset.DetectorPositionSequence = pydicom.Sequence()
            self._dataset.DetectorPositionSequence.clear()
            self._dataset.DetectorPositionSequence.extend([item.to_dataset() for item in value])

    def add_DetectorPosition(self, item: DetectorPositionSequenceItem):
        if not isinstance(item, DetectorPositionSequenceItem):
            raise ValueError("Item must be an instance of DetectorPositionSequenceItem")
        self._DetectorPositionSequence.append(item)
        if "DetectorPositionSequence" not in self._dataset:
            self._dataset.DetectorPositionSequence = pydicom.Sequence()
        self._dataset.DetectorPositionSequence.append(item.to_dataset())

    @property
    def XRayAcquisitionDoseSequence(self) -> Optional[List[XRayAcquisitionDoseSequenceItem]]:
        if "XRayAcquisitionDoseSequence" in self._dataset:
            if len(self._XRayAcquisitionDoseSequence) == len(self._dataset.XRayAcquisitionDoseSequence):
                return self._XRayAcquisitionDoseSequence
            else:
                return [XRayAcquisitionDoseSequenceItem(x) for x in self._dataset.XRayAcquisitionDoseSequence]
        return None

    @XRayAcquisitionDoseSequence.setter
    def XRayAcquisitionDoseSequence(self, value: Optional[List[XRayAcquisitionDoseSequenceItem]]):
        if value is None:
            self._XRayAcquisitionDoseSequence = []
            if "XRayAcquisitionDoseSequence" in self._dataset:
                del self._dataset.XRayAcquisitionDoseSequence
        elif not isinstance(value, list) or not all(isinstance(item, XRayAcquisitionDoseSequenceItem) for item in value):
            raise ValueError("XRayAcquisitionDoseSequence must be a list of XRayAcquisitionDoseSequenceItem objects")
        else:
            self._XRayAcquisitionDoseSequence = value
            if "XRayAcquisitionDoseSequence" not in self._dataset:
                self._dataset.XRayAcquisitionDoseSequence = pydicom.Sequence()
            self._dataset.XRayAcquisitionDoseSequence.clear()
            self._dataset.XRayAcquisitionDoseSequence.extend([item.to_dataset() for item in value])

    def add_XRayAcquisitionDose(self, item: XRayAcquisitionDoseSequenceItem):
        if not isinstance(item, XRayAcquisitionDoseSequenceItem):
            raise ValueError("Item must be an instance of XRayAcquisitionDoseSequenceItem")
        self._XRayAcquisitionDoseSequence.append(item)
        if "XRayAcquisitionDoseSequence" not in self._dataset:
            self._dataset.XRayAcquisitionDoseSequence = pydicom.Sequence()
        self._dataset.XRayAcquisitionDoseSequence.append(item.to_dataset())

    @property
    def XRayGridSequence(self) -> Optional[List[XRayGridSequenceItem]]:
        if "XRayGridSequence" in self._dataset:
            if len(self._XRayGridSequence) == len(self._dataset.XRayGridSequence):
                return self._XRayGridSequence
            else:
                return [XRayGridSequenceItem(x) for x in self._dataset.XRayGridSequence]
        return None

    @XRayGridSequence.setter
    def XRayGridSequence(self, value: Optional[List[XRayGridSequenceItem]]):
        if value is None:
            self._XRayGridSequence = []
            if "XRayGridSequence" in self._dataset:
                del self._dataset.XRayGridSequence
        elif not isinstance(value, list) or not all(isinstance(item, XRayGridSequenceItem) for item in value):
            raise ValueError("XRayGridSequence must be a list of XRayGridSequenceItem objects")
        else:
            self._XRayGridSequence = value
            if "XRayGridSequence" not in self._dataset:
                self._dataset.XRayGridSequence = pydicom.Sequence()
            self._dataset.XRayGridSequence.clear()
            self._dataset.XRayGridSequence.extend([item.to_dataset() for item in value])

    def add_XRayGrid(self, item: XRayGridSequenceItem):
        if not isinstance(item, XRayGridSequenceItem):
            raise ValueError("Item must be an instance of XRayGridSequenceItem")
        self._XRayGridSequence.append(item)
        if "XRayGridSequence" not in self._dataset:
            self._dataset.XRayGridSequence = pydicom.Sequence()
        self._dataset.XRayGridSequence.append(item.to_dataset())

    @property
    def XRayFilterSequence(self) -> Optional[List[XRayFilterSequenceItem]]:
        if "XRayFilterSequence" in self._dataset:
            if len(self._XRayFilterSequence) == len(self._dataset.XRayFilterSequence):
                return self._XRayFilterSequence
            else:
                return [XRayFilterSequenceItem(x) for x in self._dataset.XRayFilterSequence]
        return None

    @XRayFilterSequence.setter
    def XRayFilterSequence(self, value: Optional[List[XRayFilterSequenceItem]]):
        if value is None:
            self._XRayFilterSequence = []
            if "XRayFilterSequence" in self._dataset:
                del self._dataset.XRayFilterSequence
        elif not isinstance(value, list) or not all(isinstance(item, XRayFilterSequenceItem) for item in value):
            raise ValueError("XRayFilterSequence must be a list of XRayFilterSequenceItem objects")
        else:
            self._XRayFilterSequence = value
            if "XRayFilterSequence" not in self._dataset:
                self._dataset.XRayFilterSequence = pydicom.Sequence()
            self._dataset.XRayFilterSequence.clear()
            self._dataset.XRayFilterSequence.extend([item.to_dataset() for item in value])

    def add_XRayFilter(self, item: XRayFilterSequenceItem):
        if not isinstance(item, XRayFilterSequenceItem):
            raise ValueError("Item must be an instance of XRayFilterSequenceItem")
        self._XRayFilterSequence.append(item)
        if "XRayFilterSequence" not in self._dataset:
            self._dataset.XRayFilterSequence = pydicom.Sequence()
        self._dataset.XRayFilterSequence.append(item.to_dataset())

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
            raise ValueError("FramePixelDataPropertiesSequence must be a list of FramePixelDataPropertiesSequenceItem objects")
        else:
            self._FramePixelDataPropertiesSequence = value
            if "FramePixelDataPropertiesSequence" not in self._dataset:
                self._dataset.FramePixelDataPropertiesSequence = pydicom.Sequence()
            self._dataset.FramePixelDataPropertiesSequence.clear()
            self._dataset.FramePixelDataPropertiesSequence.extend([item.to_dataset() for item in value])

    def add_FramePixelDataProperties(self, item: FramePixelDataPropertiesSequenceItem):
        if not isinstance(item, FramePixelDataPropertiesSequenceItem):
            raise ValueError("Item must be an instance of FramePixelDataPropertiesSequenceItem")
        self._FramePixelDataPropertiesSequence.append(item)
        if "FramePixelDataPropertiesSequence" not in self._dataset:
            self._dataset.FramePixelDataPropertiesSequence = pydicom.Sequence()
        self._dataset.FramePixelDataPropertiesSequence.append(item.to_dataset())
