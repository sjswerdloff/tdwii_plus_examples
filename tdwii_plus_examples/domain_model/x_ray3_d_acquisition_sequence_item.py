from decimal import Decimal
from typing import Any, List, Optional  # noqa

import pydicom

from .contrast_bolus_agent_sequence_item import ContrastBolusAgentSequenceItem
from .per_projection_acquisition_sequence_item import (
    PerProjectionAcquisitionSequenceItem,
)
from .source_image_sequence_item import SourceImageSequenceItem


class XRay3DAcquisitionSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._SourceImageSequence: List[SourceImageSequenceItem] = []
        self._ContrastBolusAgentSequence: List[ContrastBolusAgentSequenceItem] = []
        self._PerProjectionAcquisitionSequence: List[PerProjectionAcquisitionSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def SourceImageSequence(self) -> Optional[List[SourceImageSequenceItem]]:
        if "SourceImageSequence" in self._dataset:
            if len(self._SourceImageSequence) == len(self._dataset.SourceImageSequence):
                return self._SourceImageSequence
            else:
                return [SourceImageSequenceItem(x) for x in self._dataset.SourceImageSequence]
        return None

    @SourceImageSequence.setter
    def SourceImageSequence(self, value: Optional[List[SourceImageSequenceItem]]):
        if value is None:
            self._SourceImageSequence = []
            if "SourceImageSequence" in self._dataset:
                del self._dataset.SourceImageSequence
        elif not isinstance(value, list) or not all(isinstance(item, SourceImageSequenceItem) for item in value):
            raise ValueError("SourceImageSequence must be a list of SourceImageSequenceItem objects")
        else:
            self._SourceImageSequence = value
            if "SourceImageSequence" not in self._dataset:
                self._dataset.SourceImageSequence = pydicom.Sequence()
            self._dataset.SourceImageSequence.clear()
            self._dataset.SourceImageSequence.extend([item.to_dataset() for item in value])

    def add_SourceImage(self, item: SourceImageSequenceItem):
        if not isinstance(item, SourceImageSequenceItem):
            raise ValueError("Item must be an instance of SourceImageSequenceItem")
        self._SourceImageSequence.append(item)
        if "SourceImageSequence" not in self._dataset:
            self._dataset.SourceImageSequence = pydicom.Sequence()
        self._dataset.SourceImageSequence.append(item.to_dataset())

    @property
    def ContrastBolusAgent(self) -> Optional[str]:
        if "ContrastBolusAgent" in self._dataset:
            return self._dataset.ContrastBolusAgent
        return None

    @ContrastBolusAgent.setter
    def ContrastBolusAgent(self, value: Optional[str]):
        if value is None:
            if "ContrastBolusAgent" in self._dataset:
                del self._dataset.ContrastBolusAgent
        else:
            self._dataset.ContrastBolusAgent = value

    @property
    def ContrastBolusAgentSequence(self) -> Optional[List[ContrastBolusAgentSequenceItem]]:
        if "ContrastBolusAgentSequence" in self._dataset:
            if len(self._ContrastBolusAgentSequence) == len(self._dataset.ContrastBolusAgentSequence):
                return self._ContrastBolusAgentSequence
            else:
                return [ContrastBolusAgentSequenceItem(x) for x in self._dataset.ContrastBolusAgentSequence]
        return None

    @ContrastBolusAgentSequence.setter
    def ContrastBolusAgentSequence(self, value: Optional[List[ContrastBolusAgentSequenceItem]]):
        if value is None:
            self._ContrastBolusAgentSequence = []
            if "ContrastBolusAgentSequence" in self._dataset:
                del self._dataset.ContrastBolusAgentSequence
        elif not isinstance(value, list) or not all(isinstance(item, ContrastBolusAgentSequenceItem) for item in value):
            raise ValueError("ContrastBolusAgentSequence must be a list of ContrastBolusAgentSequenceItem objects")
        else:
            self._ContrastBolusAgentSequence = value
            if "ContrastBolusAgentSequence" not in self._dataset:
                self._dataset.ContrastBolusAgentSequence = pydicom.Sequence()
            self._dataset.ContrastBolusAgentSequence.clear()
            self._dataset.ContrastBolusAgentSequence.extend([item.to_dataset() for item in value])

    def add_ContrastBolusAgent(self, item: ContrastBolusAgentSequenceItem):
        if not isinstance(item, ContrastBolusAgentSequenceItem):
            raise ValueError("Item must be an instance of ContrastBolusAgentSequenceItem")
        self._ContrastBolusAgentSequence.append(item)
        if "ContrastBolusAgentSequence" not in self._dataset:
            self._dataset.ContrastBolusAgentSequence = pydicom.Sequence()
        self._dataset.ContrastBolusAgentSequence.append(item.to_dataset())

    @property
    def KVP(self) -> Optional[Decimal]:
        if "KVP" in self._dataset:
            return self._dataset.KVP
        return None

    @KVP.setter
    def KVP(self, value: Optional[Decimal]):
        if value is None:
            if "KVP" in self._dataset:
                del self._dataset.KVP
        else:
            self._dataset.KVP = value

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
    def DistanceSourceToDetector(self) -> Optional[Decimal]:
        if "DistanceSourceToDetector" in self._dataset:
            return self._dataset.DistanceSourceToDetector
        return None

    @DistanceSourceToDetector.setter
    def DistanceSourceToDetector(self, value: Optional[Decimal]):
        if value is None:
            if "DistanceSourceToDetector" in self._dataset:
                del self._dataset.DistanceSourceToDetector
        else:
            self._dataset.DistanceSourceToDetector = value

    @property
    def FieldOfViewShape(self) -> Optional[str]:
        if "FieldOfViewShape" in self._dataset:
            return self._dataset.FieldOfViewShape
        return None

    @FieldOfViewShape.setter
    def FieldOfViewShape(self, value: Optional[str]):
        if value is None:
            if "FieldOfViewShape" in self._dataset:
                del self._dataset.FieldOfViewShape
        else:
            self._dataset.FieldOfViewShape = value

    @property
    def FilterType(self) -> Optional[str]:
        if "FilterType" in self._dataset:
            return self._dataset.FilterType
        return None

    @FilterType.setter
    def FilterType(self, value: Optional[str]):
        if value is None:
            if "FilterType" in self._dataset:
                del self._dataset.FilterType
        else:
            self._dataset.FilterType = value

    @property
    def Grid(self) -> Optional[List[str]]:
        if "Grid" in self._dataset:
            return self._dataset.Grid
        return None

    @Grid.setter
    def Grid(self, value: Optional[List[str]]):
        if value is None:
            if "Grid" in self._dataset:
                del self._dataset.Grid
        else:
            self._dataset.Grid = value

    @property
    def FocalSpots(self) -> Optional[List[Decimal]]:
        if "FocalSpots" in self._dataset:
            return self._dataset.FocalSpots
        return None

    @FocalSpots.setter
    def FocalSpots(self, value: Optional[List[Decimal]]):
        if value is None:
            if "FocalSpots" in self._dataset:
                del self._dataset.FocalSpots
        else:
            self._dataset.FocalSpots = value

    @property
    def ExposureIndex(self) -> Optional[Decimal]:
        if "ExposureIndex" in self._dataset:
            return self._dataset.ExposureIndex
        return None

    @ExposureIndex.setter
    def ExposureIndex(self, value: Optional[Decimal]):
        if value is None:
            if "ExposureIndex" in self._dataset:
                del self._dataset.ExposureIndex
        else:
            self._dataset.ExposureIndex = value

    @property
    def TargetExposureIndex(self) -> Optional[Decimal]:
        if "TargetExposureIndex" in self._dataset:
            return self._dataset.TargetExposureIndex
        return None

    @TargetExposureIndex.setter
    def TargetExposureIndex(self, value: Optional[Decimal]):
        if value is None:
            if "TargetExposureIndex" in self._dataset:
                del self._dataset.TargetExposureIndex
        else:
            self._dataset.TargetExposureIndex = value

    @property
    def DeviationIndex(self) -> Optional[Decimal]:
        if "DeviationIndex" in self._dataset:
            return self._dataset.DeviationIndex
        return None

    @DeviationIndex.setter
    def DeviationIndex(self, value: Optional[Decimal]):
        if value is None:
            if "DeviationIndex" in self._dataset:
                del self._dataset.DeviationIndex
        else:
            self._dataset.DeviationIndex = value

    @property
    def Sensitivity(self) -> Optional[Decimal]:
        if "Sensitivity" in self._dataset:
            return self._dataset.Sensitivity
        return None

    @Sensitivity.setter
    def Sensitivity(self, value: Optional[Decimal]):
        if value is None:
            if "Sensitivity" in self._dataset:
                del self._dataset.Sensitivity
        else:
            self._dataset.Sensitivity = value

    @property
    def DetectorConditionsNominalFlag(self) -> Optional[str]:
        if "DetectorConditionsNominalFlag" in self._dataset:
            return self._dataset.DetectorConditionsNominalFlag
        return None

    @DetectorConditionsNominalFlag.setter
    def DetectorConditionsNominalFlag(self, value: Optional[str]):
        if value is None:
            if "DetectorConditionsNominalFlag" in self._dataset:
                del self._dataset.DetectorConditionsNominalFlag
        else:
            self._dataset.DetectorConditionsNominalFlag = value

    @property
    def DetectorTemperature(self) -> Optional[Decimal]:
        if "DetectorTemperature" in self._dataset:
            return self._dataset.DetectorTemperature
        return None

    @DetectorTemperature.setter
    def DetectorTemperature(self, value: Optional[Decimal]):
        if value is None:
            if "DetectorTemperature" in self._dataset:
                del self._dataset.DetectorTemperature
        else:
            self._dataset.DetectorTemperature = value

    @property
    def DetectorType(self) -> Optional[str]:
        if "DetectorType" in self._dataset:
            return self._dataset.DetectorType
        return None

    @DetectorType.setter
    def DetectorType(self, value: Optional[str]):
        if value is None:
            if "DetectorType" in self._dataset:
                del self._dataset.DetectorType
        else:
            self._dataset.DetectorType = value

    @property
    def DetectorConfiguration(self) -> Optional[str]:
        if "DetectorConfiguration" in self._dataset:
            return self._dataset.DetectorConfiguration
        return None

    @DetectorConfiguration.setter
    def DetectorConfiguration(self, value: Optional[str]):
        if value is None:
            if "DetectorConfiguration" in self._dataset:
                del self._dataset.DetectorConfiguration
        else:
            self._dataset.DetectorConfiguration = value

    @property
    def DetectorDescription(self) -> Optional[str]:
        if "DetectorDescription" in self._dataset:
            return self._dataset.DetectorDescription
        return None

    @DetectorDescription.setter
    def DetectorDescription(self, value: Optional[str]):
        if value is None:
            if "DetectorDescription" in self._dataset:
                del self._dataset.DetectorDescription
        else:
            self._dataset.DetectorDescription = value

    @property
    def DetectorMode(self) -> Optional[str]:
        if "DetectorMode" in self._dataset:
            return self._dataset.DetectorMode
        return None

    @DetectorMode.setter
    def DetectorMode(self, value: Optional[str]):
        if value is None:
            if "DetectorMode" in self._dataset:
                del self._dataset.DetectorMode
        else:
            self._dataset.DetectorMode = value

    @property
    def DetectorID(self) -> Optional[str]:
        if "DetectorID" in self._dataset:
            return self._dataset.DetectorID
        return None

    @DetectorID.setter
    def DetectorID(self, value: Optional[str]):
        if value is None:
            if "DetectorID" in self._dataset:
                del self._dataset.DetectorID
        else:
            self._dataset.DetectorID = value

    @property
    def DateOfLastDetectorCalibration(self) -> Optional[str]:
        if "DateOfLastDetectorCalibration" in self._dataset:
            return self._dataset.DateOfLastDetectorCalibration
        return None

    @DateOfLastDetectorCalibration.setter
    def DateOfLastDetectorCalibration(self, value: Optional[str]):
        if value is None:
            if "DateOfLastDetectorCalibration" in self._dataset:
                del self._dataset.DateOfLastDetectorCalibration
        else:
            self._dataset.DateOfLastDetectorCalibration = value

    @property
    def TimeOfLastDetectorCalibration(self) -> Optional[str]:
        if "TimeOfLastDetectorCalibration" in self._dataset:
            return self._dataset.TimeOfLastDetectorCalibration
        return None

    @TimeOfLastDetectorCalibration.setter
    def TimeOfLastDetectorCalibration(self, value: Optional[str]):
        if value is None:
            if "TimeOfLastDetectorCalibration" in self._dataset:
                del self._dataset.TimeOfLastDetectorCalibration
        else:
            self._dataset.TimeOfLastDetectorCalibration = value

    @property
    def ExposuresOnDetectorSinceLastCalibration(self) -> Optional[int]:
        if "ExposuresOnDetectorSinceLastCalibration" in self._dataset:
            return self._dataset.ExposuresOnDetectorSinceLastCalibration
        return None

    @ExposuresOnDetectorSinceLastCalibration.setter
    def ExposuresOnDetectorSinceLastCalibration(self, value: Optional[int]):
        if value is None:
            if "ExposuresOnDetectorSinceLastCalibration" in self._dataset:
                del self._dataset.ExposuresOnDetectorSinceLastCalibration
        else:
            self._dataset.ExposuresOnDetectorSinceLastCalibration = value

    @property
    def ExposuresOnDetectorSinceManufactured(self) -> Optional[int]:
        if "ExposuresOnDetectorSinceManufactured" in self._dataset:
            return self._dataset.ExposuresOnDetectorSinceManufactured
        return None

    @ExposuresOnDetectorSinceManufactured.setter
    def ExposuresOnDetectorSinceManufactured(self, value: Optional[int]):
        if value is None:
            if "ExposuresOnDetectorSinceManufactured" in self._dataset:
                del self._dataset.ExposuresOnDetectorSinceManufactured
        else:
            self._dataset.ExposuresOnDetectorSinceManufactured = value

    @property
    def DetectorTimeSinceLastExposure(self) -> Optional[Decimal]:
        if "DetectorTimeSinceLastExposure" in self._dataset:
            return self._dataset.DetectorTimeSinceLastExposure
        return None

    @DetectorTimeSinceLastExposure.setter
    def DetectorTimeSinceLastExposure(self, value: Optional[Decimal]):
        if value is None:
            if "DetectorTimeSinceLastExposure" in self._dataset:
                del self._dataset.DetectorTimeSinceLastExposure
        else:
            self._dataset.DetectorTimeSinceLastExposure = value

    @property
    def DetectorBinning(self) -> Optional[List[Decimal]]:
        if "DetectorBinning" in self._dataset:
            return self._dataset.DetectorBinning
        return None

    @DetectorBinning.setter
    def DetectorBinning(self, value: Optional[List[Decimal]]):
        if value is None:
            if "DetectorBinning" in self._dataset:
                del self._dataset.DetectorBinning
        else:
            self._dataset.DetectorBinning = value

    @property
    def DetectorElementPhysicalSize(self) -> Optional[List[Decimal]]:
        if "DetectorElementPhysicalSize" in self._dataset:
            return self._dataset.DetectorElementPhysicalSize
        return None

    @DetectorElementPhysicalSize.setter
    def DetectorElementPhysicalSize(self, value: Optional[List[Decimal]]):
        if value is None:
            if "DetectorElementPhysicalSize" in self._dataset:
                del self._dataset.DetectorElementPhysicalSize
        else:
            self._dataset.DetectorElementPhysicalSize = value

    @property
    def DetectorElementSpacing(self) -> Optional[List[Decimal]]:
        if "DetectorElementSpacing" in self._dataset:
            return self._dataset.DetectorElementSpacing
        return None

    @DetectorElementSpacing.setter
    def DetectorElementSpacing(self, value: Optional[List[Decimal]]):
        if value is None:
            if "DetectorElementSpacing" in self._dataset:
                del self._dataset.DetectorElementSpacing
        else:
            self._dataset.DetectorElementSpacing = value

    @property
    def DetectorActiveShape(self) -> Optional[str]:
        if "DetectorActiveShape" in self._dataset:
            return self._dataset.DetectorActiveShape
        return None

    @DetectorActiveShape.setter
    def DetectorActiveShape(self, value: Optional[str]):
        if value is None:
            if "DetectorActiveShape" in self._dataset:
                del self._dataset.DetectorActiveShape
        else:
            self._dataset.DetectorActiveShape = value

    @property
    def DetectorActiveDimensions(self) -> Optional[List[Decimal]]:
        if "DetectorActiveDimensions" in self._dataset:
            return self._dataset.DetectorActiveDimensions
        return None

    @DetectorActiveDimensions.setter
    def DetectorActiveDimensions(self, value: Optional[List[Decimal]]):
        if value is None:
            if "DetectorActiveDimensions" in self._dataset:
                del self._dataset.DetectorActiveDimensions
        else:
            self._dataset.DetectorActiveDimensions = value

    @property
    def DetectorActiveOrigin(self) -> Optional[List[Decimal]]:
        if "DetectorActiveOrigin" in self._dataset:
            return self._dataset.DetectorActiveOrigin
        return None

    @DetectorActiveOrigin.setter
    def DetectorActiveOrigin(self, value: Optional[List[Decimal]]):
        if value is None:
            if "DetectorActiveOrigin" in self._dataset:
                del self._dataset.DetectorActiveOrigin
        else:
            self._dataset.DetectorActiveOrigin = value

    @property
    def DetectorManufacturerName(self) -> Optional[str]:
        if "DetectorManufacturerName" in self._dataset:
            return self._dataset.DetectorManufacturerName
        return None

    @DetectorManufacturerName.setter
    def DetectorManufacturerName(self, value: Optional[str]):
        if value is None:
            if "DetectorManufacturerName" in self._dataset:
                del self._dataset.DetectorManufacturerName
        else:
            self._dataset.DetectorManufacturerName = value

    @property
    def DetectorManufacturerModelName(self) -> Optional[str]:
        if "DetectorManufacturerModelName" in self._dataset:
            return self._dataset.DetectorManufacturerModelName
        return None

    @DetectorManufacturerModelName.setter
    def DetectorManufacturerModelName(self, value: Optional[str]):
        if value is None:
            if "DetectorManufacturerModelName" in self._dataset:
                del self._dataset.DetectorManufacturerModelName
        else:
            self._dataset.DetectorManufacturerModelName = value

    @property
    def FieldOfViewOrigin(self) -> Optional[List[Decimal]]:
        if "FieldOfViewOrigin" in self._dataset:
            return self._dataset.FieldOfViewOrigin
        return None

    @FieldOfViewOrigin.setter
    def FieldOfViewOrigin(self, value: Optional[List[Decimal]]):
        if value is None:
            if "FieldOfViewOrigin" in self._dataset:
                del self._dataset.FieldOfViewOrigin
        else:
            self._dataset.FieldOfViewOrigin = value

    @property
    def FieldOfViewRotation(self) -> Optional[Decimal]:
        if "FieldOfViewRotation" in self._dataset:
            return self._dataset.FieldOfViewRotation
        return None

    @FieldOfViewRotation.setter
    def FieldOfViewRotation(self, value: Optional[Decimal]):
        if value is None:
            if "FieldOfViewRotation" in self._dataset:
                del self._dataset.FieldOfViewRotation
        else:
            self._dataset.FieldOfViewRotation = value

    @property
    def FieldOfViewHorizontalFlip(self) -> Optional[str]:
        if "FieldOfViewHorizontalFlip" in self._dataset:
            return self._dataset.FieldOfViewHorizontalFlip
        return None

    @FieldOfViewHorizontalFlip.setter
    def FieldOfViewHorizontalFlip(self, value: Optional[str]):
        if value is None:
            if "FieldOfViewHorizontalFlip" in self._dataset:
                del self._dataset.FieldOfViewHorizontalFlip
        else:
            self._dataset.FieldOfViewHorizontalFlip = value

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
    def FilterMaterial(self) -> Optional[List[str]]:
        if "FilterMaterial" in self._dataset:
            return self._dataset.FilterMaterial
        return None

    @FilterMaterial.setter
    def FilterMaterial(self, value: Optional[List[str]]):
        if value is None:
            if "FilterMaterial" in self._dataset:
                del self._dataset.FilterMaterial
        else:
            self._dataset.FilterMaterial = value

    @property
    def FilterThicknessMinimum(self) -> Optional[List[Decimal]]:
        if "FilterThicknessMinimum" in self._dataset:
            return self._dataset.FilterThicknessMinimum
        return None

    @FilterThicknessMinimum.setter
    def FilterThicknessMinimum(self, value: Optional[List[Decimal]]):
        if value is None:
            if "FilterThicknessMinimum" in self._dataset:
                del self._dataset.FilterThicknessMinimum
        else:
            self._dataset.FilterThicknessMinimum = value

    @property
    def FilterThicknessMaximum(self) -> Optional[List[Decimal]]:
        if "FilterThicknessMaximum" in self._dataset:
            return self._dataset.FilterThicknessMaximum
        return None

    @FilterThicknessMaximum.setter
    def FilterThicknessMaximum(self, value: Optional[List[Decimal]]):
        if value is None:
            if "FilterThicknessMaximum" in self._dataset:
                del self._dataset.FilterThicknessMaximum
        else:
            self._dataset.FilterThicknessMaximum = value

    @property
    def FilterBeamPathLengthMinimum(self) -> Optional[List[float]]:
        if "FilterBeamPathLengthMinimum" in self._dataset:
            return self._dataset.FilterBeamPathLengthMinimum
        return None

    @FilterBeamPathLengthMinimum.setter
    def FilterBeamPathLengthMinimum(self, value: Optional[List[float]]):
        if value is None:
            if "FilterBeamPathLengthMinimum" in self._dataset:
                del self._dataset.FilterBeamPathLengthMinimum
        else:
            self._dataset.FilterBeamPathLengthMinimum = value

    @property
    def FilterBeamPathLengthMaximum(self) -> Optional[List[float]]:
        if "FilterBeamPathLengthMaximum" in self._dataset:
            return self._dataset.FilterBeamPathLengthMaximum
        return None

    @FilterBeamPathLengthMaximum.setter
    def FilterBeamPathLengthMaximum(self, value: Optional[List[float]]):
        if value is None:
            if "FilterBeamPathLengthMaximum" in self._dataset:
                del self._dataset.FilterBeamPathLengthMaximum
        else:
            self._dataset.FilterBeamPathLengthMaximum = value

    @property
    def ExposureTimeInms(self) -> Optional[float]:
        if "ExposureTimeInms" in self._dataset:
            return self._dataset.ExposureTimeInms
        return None

    @ExposureTimeInms.setter
    def ExposureTimeInms(self, value: Optional[float]):
        if value is None:
            if "ExposureTimeInms" in self._dataset:
                del self._dataset.ExposureTimeInms
        else:
            self._dataset.ExposureTimeInms = value

    @property
    def XRayTubeCurrentInmA(self) -> Optional[float]:
        if "XRayTubeCurrentInmA" in self._dataset:
            return self._dataset.XRayTubeCurrentInmA
        return None

    @XRayTubeCurrentInmA.setter
    def XRayTubeCurrentInmA(self, value: Optional[float]):
        if value is None:
            if "XRayTubeCurrentInmA" in self._dataset:
                del self._dataset.XRayTubeCurrentInmA
        else:
            self._dataset.XRayTubeCurrentInmA = value

    @property
    def ExposureInmAs(self) -> Optional[float]:
        if "ExposureInmAs" in self._dataset:
            return self._dataset.ExposureInmAs
        return None

    @ExposureInmAs.setter
    def ExposureInmAs(self, value: Optional[float]):
        if value is None:
            if "ExposureInmAs" in self._dataset:
                del self._dataset.ExposureInmAs
        else:
            self._dataset.ExposureInmAs = value

    @property
    def DistanceSourceToIsocenter(self) -> Optional[float]:
        if "DistanceSourceToIsocenter" in self._dataset:
            return self._dataset.DistanceSourceToIsocenter
        return None

    @DistanceSourceToIsocenter.setter
    def DistanceSourceToIsocenter(self, value: Optional[float]):
        if value is None:
            if "DistanceSourceToIsocenter" in self._dataset:
                del self._dataset.DistanceSourceToIsocenter
        else:
            self._dataset.DistanceSourceToIsocenter = value

    @property
    def XRayReceptorType(self) -> Optional[str]:
        if "XRayReceptorType" in self._dataset:
            return self._dataset.XRayReceptorType
        return None

    @XRayReceptorType.setter
    def XRayReceptorType(self, value: Optional[str]):
        if value is None:
            if "XRayReceptorType" in self._dataset:
                del self._dataset.XRayReceptorType
        else:
            self._dataset.XRayReceptorType = value

    @property
    def PhysicalDetectorSize(self) -> Optional[List[float]]:
        if "PhysicalDetectorSize" in self._dataset:
            return self._dataset.PhysicalDetectorSize
        return None

    @PhysicalDetectorSize.setter
    def PhysicalDetectorSize(self, value: Optional[List[float]]):
        if value is None:
            if "PhysicalDetectorSize" in self._dataset:
                del self._dataset.PhysicalDetectorSize
        else:
            self._dataset.PhysicalDetectorSize = value

    @property
    def PositionOfIsocenterProjection(self) -> Optional[List[float]]:
        if "PositionOfIsocenterProjection" in self._dataset:
            return self._dataset.PositionOfIsocenterProjection
        return None

    @PositionOfIsocenterProjection.setter
    def PositionOfIsocenterProjection(self, value: Optional[List[float]]):
        if value is None:
            if "PositionOfIsocenterProjection" in self._dataset:
                del self._dataset.PositionOfIsocenterProjection
        else:
            self._dataset.PositionOfIsocenterProjection = value

    @property
    def FieldOfViewDimensionsInFloat(self) -> Optional[List[float]]:
        if "FieldOfViewDimensionsInFloat" in self._dataset:
            return self._dataset.FieldOfViewDimensionsInFloat
        return None

    @FieldOfViewDimensionsInFloat.setter
    def FieldOfViewDimensionsInFloat(self, value: Optional[List[float]]):
        if value is None:
            if "FieldOfViewDimensionsInFloat" in self._dataset:
                del self._dataset.FieldOfViewDimensionsInFloat
        else:
            self._dataset.FieldOfViewDimensionsInFloat = value

    @property
    def TableXPositionToIsocenter(self) -> Optional[float]:
        if "TableXPositionToIsocenter" in self._dataset:
            return self._dataset.TableXPositionToIsocenter
        return None

    @TableXPositionToIsocenter.setter
    def TableXPositionToIsocenter(self, value: Optional[float]):
        if value is None:
            if "TableXPositionToIsocenter" in self._dataset:
                del self._dataset.TableXPositionToIsocenter
        else:
            self._dataset.TableXPositionToIsocenter = value

    @property
    def TableYPositionToIsocenter(self) -> Optional[float]:
        if "TableYPositionToIsocenter" in self._dataset:
            return self._dataset.TableYPositionToIsocenter
        return None

    @TableYPositionToIsocenter.setter
    def TableYPositionToIsocenter(self, value: Optional[float]):
        if value is None:
            if "TableYPositionToIsocenter" in self._dataset:
                del self._dataset.TableYPositionToIsocenter
        else:
            self._dataset.TableYPositionToIsocenter = value

    @property
    def TableZPositionToIsocenter(self) -> Optional[float]:
        if "TableZPositionToIsocenter" in self._dataset:
            return self._dataset.TableZPositionToIsocenter
        return None

    @TableZPositionToIsocenter.setter
    def TableZPositionToIsocenter(self, value: Optional[float]):
        if value is None:
            if "TableZPositionToIsocenter" in self._dataset:
                del self._dataset.TableZPositionToIsocenter
        else:
            self._dataset.TableZPositionToIsocenter = value

    @property
    def TableHorizontalRotationAngle(self) -> Optional[float]:
        if "TableHorizontalRotationAngle" in self._dataset:
            return self._dataset.TableHorizontalRotationAngle
        return None

    @TableHorizontalRotationAngle.setter
    def TableHorizontalRotationAngle(self, value: Optional[float]):
        if value is None:
            if "TableHorizontalRotationAngle" in self._dataset:
                del self._dataset.TableHorizontalRotationAngle
        else:
            self._dataset.TableHorizontalRotationAngle = value

    @property
    def TableHeadTiltAngle(self) -> Optional[float]:
        if "TableHeadTiltAngle" in self._dataset:
            return self._dataset.TableHeadTiltAngle
        return None

    @TableHeadTiltAngle.setter
    def TableHeadTiltAngle(self, value: Optional[float]):
        if value is None:
            if "TableHeadTiltAngle" in self._dataset:
                del self._dataset.TableHeadTiltAngle
        else:
            self._dataset.TableHeadTiltAngle = value

    @property
    def TableCradleTiltAngle(self) -> Optional[float]:
        if "TableCradleTiltAngle" in self._dataset:
            return self._dataset.TableCradleTiltAngle
        return None

    @TableCradleTiltAngle.setter
    def TableCradleTiltAngle(self, value: Optional[float]):
        if value is None:
            if "TableCradleTiltAngle" in self._dataset:
                del self._dataset.TableCradleTiltAngle
        else:
            self._dataset.TableCradleTiltAngle = value

    @property
    def PrimaryPositionerScanArc(self) -> Optional[float]:
        if "PrimaryPositionerScanArc" in self._dataset:
            return self._dataset.PrimaryPositionerScanArc
        return None

    @PrimaryPositionerScanArc.setter
    def PrimaryPositionerScanArc(self, value: Optional[float]):
        if value is None:
            if "PrimaryPositionerScanArc" in self._dataset:
                del self._dataset.PrimaryPositionerScanArc
        else:
            self._dataset.PrimaryPositionerScanArc = value

    @property
    def SecondaryPositionerScanArc(self) -> Optional[float]:
        if "SecondaryPositionerScanArc" in self._dataset:
            return self._dataset.SecondaryPositionerScanArc
        return None

    @SecondaryPositionerScanArc.setter
    def SecondaryPositionerScanArc(self, value: Optional[float]):
        if value is None:
            if "SecondaryPositionerScanArc" in self._dataset:
                del self._dataset.SecondaryPositionerScanArc
        else:
            self._dataset.SecondaryPositionerScanArc = value

    @property
    def PrimaryPositionerScanStartAngle(self) -> Optional[float]:
        if "PrimaryPositionerScanStartAngle" in self._dataset:
            return self._dataset.PrimaryPositionerScanStartAngle
        return None

    @PrimaryPositionerScanStartAngle.setter
    def PrimaryPositionerScanStartAngle(self, value: Optional[float]):
        if value is None:
            if "PrimaryPositionerScanStartAngle" in self._dataset:
                del self._dataset.PrimaryPositionerScanStartAngle
        else:
            self._dataset.PrimaryPositionerScanStartAngle = value

    @property
    def SecondaryPositionerScanStartAngle(self) -> Optional[float]:
        if "SecondaryPositionerScanStartAngle" in self._dataset:
            return self._dataset.SecondaryPositionerScanStartAngle
        return None

    @SecondaryPositionerScanStartAngle.setter
    def SecondaryPositionerScanStartAngle(self, value: Optional[float]):
        if value is None:
            if "SecondaryPositionerScanStartAngle" in self._dataset:
                del self._dataset.SecondaryPositionerScanStartAngle
        else:
            self._dataset.SecondaryPositionerScanStartAngle = value

    @property
    def PrimaryPositionerIncrement(self) -> Optional[float]:
        if "PrimaryPositionerIncrement" in self._dataset:
            return self._dataset.PrimaryPositionerIncrement
        return None

    @PrimaryPositionerIncrement.setter
    def PrimaryPositionerIncrement(self, value: Optional[float]):
        if value is None:
            if "PrimaryPositionerIncrement" in self._dataset:
                del self._dataset.PrimaryPositionerIncrement
        else:
            self._dataset.PrimaryPositionerIncrement = value

    @property
    def SecondaryPositionerIncrement(self) -> Optional[float]:
        if "SecondaryPositionerIncrement" in self._dataset:
            return self._dataset.SecondaryPositionerIncrement
        return None

    @SecondaryPositionerIncrement.setter
    def SecondaryPositionerIncrement(self, value: Optional[float]):
        if value is None:
            if "SecondaryPositionerIncrement" in self._dataset:
                del self._dataset.SecondaryPositionerIncrement
        else:
            self._dataset.SecondaryPositionerIncrement = value

    @property
    def StartAcquisitionDateTime(self) -> Optional[str]:
        if "StartAcquisitionDateTime" in self._dataset:
            return self._dataset.StartAcquisitionDateTime
        return None

    @StartAcquisitionDateTime.setter
    def StartAcquisitionDateTime(self, value: Optional[str]):
        if value is None:
            if "StartAcquisitionDateTime" in self._dataset:
                del self._dataset.StartAcquisitionDateTime
        else:
            self._dataset.StartAcquisitionDateTime = value

    @property
    def EndAcquisitionDateTime(self) -> Optional[str]:
        if "EndAcquisitionDateTime" in self._dataset:
            return self._dataset.EndAcquisitionDateTime
        return None

    @EndAcquisitionDateTime.setter
    def EndAcquisitionDateTime(self, value: Optional[str]):
        if value is None:
            if "EndAcquisitionDateTime" in self._dataset:
                del self._dataset.EndAcquisitionDateTime
        else:
            self._dataset.EndAcquisitionDateTime = value

    @property
    def PrimaryPositionerIncrementSign(self) -> Optional[int]:
        if "PrimaryPositionerIncrementSign" in self._dataset:
            return self._dataset.PrimaryPositionerIncrementSign
        return None

    @PrimaryPositionerIncrementSign.setter
    def PrimaryPositionerIncrementSign(self, value: Optional[int]):
        if value is None:
            if "PrimaryPositionerIncrementSign" in self._dataset:
                del self._dataset.PrimaryPositionerIncrementSign
        else:
            self._dataset.PrimaryPositionerIncrementSign = value

    @property
    def SecondaryPositionerIncrementSign(self) -> Optional[int]:
        if "SecondaryPositionerIncrementSign" in self._dataset:
            return self._dataset.SecondaryPositionerIncrementSign
        return None

    @SecondaryPositionerIncrementSign.setter
    def SecondaryPositionerIncrementSign(self, value: Optional[int]):
        if value is None:
            if "SecondaryPositionerIncrementSign" in self._dataset:
                del self._dataset.SecondaryPositionerIncrementSign
        else:
            self._dataset.SecondaryPositionerIncrementSign = value

    @property
    def PerProjectionAcquisitionSequence(self) -> Optional[List[PerProjectionAcquisitionSequenceItem]]:
        if "PerProjectionAcquisitionSequence" in self._dataset:
            if len(self._PerProjectionAcquisitionSequence) == len(self._dataset.PerProjectionAcquisitionSequence):
                return self._PerProjectionAcquisitionSequence
            else:
                return [PerProjectionAcquisitionSequenceItem(x) for x in self._dataset.PerProjectionAcquisitionSequence]
        return None

    @PerProjectionAcquisitionSequence.setter
    def PerProjectionAcquisitionSequence(self, value: Optional[List[PerProjectionAcquisitionSequenceItem]]):
        if value is None:
            self._PerProjectionAcquisitionSequence = []
            if "PerProjectionAcquisitionSequence" in self._dataset:
                del self._dataset.PerProjectionAcquisitionSequence
        elif not isinstance(value, list) or not all(isinstance(item, PerProjectionAcquisitionSequenceItem) for item in value):
            raise ValueError("PerProjectionAcquisitionSequence must be a list of PerProjectionAcquisitionSequenceItem objects")
        else:
            self._PerProjectionAcquisitionSequence = value
            if "PerProjectionAcquisitionSequence" not in self._dataset:
                self._dataset.PerProjectionAcquisitionSequence = pydicom.Sequence()
            self._dataset.PerProjectionAcquisitionSequence.clear()
            self._dataset.PerProjectionAcquisitionSequence.extend([item.to_dataset() for item in value])

    def add_PerProjectionAcquisition(self, item: PerProjectionAcquisitionSequenceItem):
        if not isinstance(item, PerProjectionAcquisitionSequenceItem):
            raise ValueError("Item must be an instance of PerProjectionAcquisitionSequenceItem")
        self._PerProjectionAcquisitionSequence.append(item)
        if "PerProjectionAcquisitionSequence" not in self._dataset:
            self._dataset.PerProjectionAcquisitionSequence = pydicom.Sequence()
        self._dataset.PerProjectionAcquisitionSequence.append(item.to_dataset())
