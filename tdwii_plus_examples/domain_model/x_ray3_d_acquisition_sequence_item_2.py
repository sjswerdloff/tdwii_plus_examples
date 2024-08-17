from decimal import Decimal
from typing import Any, List, Optional

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
            raise ValueError(f"SourceImageSequence must be a list of SourceImageSequenceItem objects")
        else:
            self._SourceImageSequence = value
            if "SourceImageSequence" not in self._dataset:
                self._dataset.SourceImageSequence = pydicom.Sequence()
            self._dataset.SourceImageSequence.clear()
            self._dataset.SourceImageSequence.extend([item.to_dataset() for item in value])

    def add_SourceImage(self, item: SourceImageSequenceItem):
        if not isinstance(item, SourceImageSequenceItem):
            raise ValueError(f"Item must be an instance of SourceImageSequenceItem")
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
            raise ValueError(f"ContrastBolusAgentSequence must be a list of ContrastBolusAgentSequenceItem objects")
        else:
            self._ContrastBolusAgentSequence = value
            if "ContrastBolusAgentSequence" not in self._dataset:
                self._dataset.ContrastBolusAgentSequence = pydicom.Sequence()
            self._dataset.ContrastBolusAgentSequence.clear()
            self._dataset.ContrastBolusAgentSequence.extend([item.to_dataset() for item in value])

    def add_ContrastBolusAgent(self, item: ContrastBolusAgentSequenceItem):
        if not isinstance(item, ContrastBolusAgentSequenceItem):
            raise ValueError(f"Item must be an instance of ContrastBolusAgentSequenceItem")
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
    def DistanceSourceToPatient(self) -> Optional[Decimal]:
        if "DistanceSourceToPatient" in self._dataset:
            return self._dataset.DistanceSourceToPatient
        return None

    @DistanceSourceToPatient.setter
    def DistanceSourceToPatient(self, value: Optional[Decimal]):
        if value is None:
            if "DistanceSourceToPatient" in self._dataset:
                del self._dataset.DistanceSourceToPatient
        else:
            self._dataset.DistanceSourceToPatient = value

    @property
    def EstimatedRadiographicMagnificationFactor(self) -> Optional[Decimal]:
        if "EstimatedRadiographicMagnificationFactor" in self._dataset:
            return self._dataset.EstimatedRadiographicMagnificationFactor
        return None

    @EstimatedRadiographicMagnificationFactor.setter
    def EstimatedRadiographicMagnificationFactor(self, value: Optional[Decimal]):
        if value is None:
            if "EstimatedRadiographicMagnificationFactor" in self._dataset:
                del self._dataset.EstimatedRadiographicMagnificationFactor
        else:
            self._dataset.EstimatedRadiographicMagnificationFactor = value

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
    def AnodeTargetMaterial(self) -> Optional[str]:
        if "AnodeTargetMaterial" in self._dataset:
            return self._dataset.AnodeTargetMaterial
        return None

    @AnodeTargetMaterial.setter
    def AnodeTargetMaterial(self, value: Optional[str]):
        if value is None:
            if "AnodeTargetMaterial" in self._dataset:
                del self._dataset.AnodeTargetMaterial
        else:
            self._dataset.AnodeTargetMaterial = value

    @property
    def BodyPartThickness(self) -> Optional[Decimal]:
        if "BodyPartThickness" in self._dataset:
            return self._dataset.BodyPartThickness
        return None

    @BodyPartThickness.setter
    def BodyPartThickness(self, value: Optional[Decimal]):
        if value is None:
            if "BodyPartThickness" in self._dataset:
                del self._dataset.BodyPartThickness
        else:
            self._dataset.BodyPartThickness = value

    @property
    def CompressionForce(self) -> Optional[Decimal]:
        if "CompressionForce" in self._dataset:
            return self._dataset.CompressionForce
        return None

    @CompressionForce.setter
    def CompressionForce(self, value: Optional[Decimal]):
        if value is None:
            if "CompressionForce" in self._dataset:
                del self._dataset.CompressionForce
        else:
            self._dataset.CompressionForce = value

    @property
    def CompressionPressure(self) -> Optional[Decimal]:
        if "CompressionPressure" in self._dataset:
            return self._dataset.CompressionPressure
        return None

    @CompressionPressure.setter
    def CompressionPressure(self, value: Optional[Decimal]):
        if value is None:
            if "CompressionPressure" in self._dataset:
                del self._dataset.CompressionPressure
        else:
            self._dataset.CompressionPressure = value

    @property
    def PaddleDescription(self) -> Optional[str]:
        if "PaddleDescription" in self._dataset:
            return self._dataset.PaddleDescription
        return None

    @PaddleDescription.setter
    def PaddleDescription(self, value: Optional[str]):
        if value is None:
            if "PaddleDescription" in self._dataset:
                del self._dataset.PaddleDescription
        else:
            self._dataset.PaddleDescription = value

    @property
    def CompressionContactArea(self) -> Optional[Decimal]:
        if "CompressionContactArea" in self._dataset:
            return self._dataset.CompressionContactArea
        return None

    @CompressionContactArea.setter
    def CompressionContactArea(self, value: Optional[Decimal]):
        if value is None:
            if "CompressionContactArea" in self._dataset:
                del self._dataset.CompressionContactArea
        else:
            self._dataset.CompressionContactArea = value

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
    def ExposureControlMode(self) -> Optional[str]:
        if "ExposureControlMode" in self._dataset:
            return self._dataset.ExposureControlMode
        return None

    @ExposureControlMode.setter
    def ExposureControlMode(self, value: Optional[str]):
        if value is None:
            if "ExposureControlMode" in self._dataset:
                del self._dataset.ExposureControlMode
        else:
            self._dataset.ExposureControlMode = value

    @property
    def ExposureControlModeDescription(self) -> Optional[str]:
        if "ExposureControlModeDescription" in self._dataset:
            return self._dataset.ExposureControlModeDescription
        return None

    @ExposureControlModeDescription.setter
    def ExposureControlModeDescription(self, value: Optional[str]):
        if value is None:
            if "ExposureControlModeDescription" in self._dataset:
                del self._dataset.ExposureControlModeDescription
        else:
            self._dataset.ExposureControlModeDescription = value

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
            raise ValueError(
                f"PerProjectionAcquisitionSequence must be a list of PerProjectionAcquisitionSequenceItem objects"
            )
        else:
            self._PerProjectionAcquisitionSequence = value
            if "PerProjectionAcquisitionSequence" not in self._dataset:
                self._dataset.PerProjectionAcquisitionSequence = pydicom.Sequence()
            self._dataset.PerProjectionAcquisitionSequence.clear()
            self._dataset.PerProjectionAcquisitionSequence.extend([item.to_dataset() for item in value])

    def add_PerProjectionAcquisition(self, item: PerProjectionAcquisitionSequenceItem):
        if not isinstance(item, PerProjectionAcquisitionSequenceItem):
            raise ValueError(f"Item must be an instance of PerProjectionAcquisitionSequenceItem")
        self._PerProjectionAcquisitionSequence.append(item)
        if "PerProjectionAcquisitionSequence" not in self._dataset:
            self._dataset.PerProjectionAcquisitionSequence = pydicom.Sequence()
        self._dataset.PerProjectionAcquisitionSequence.append(item.to_dataset())

    @property
    def HalfValueLayer(self) -> Optional[Decimal]:
        if "HalfValueLayer" in self._dataset:
            return self._dataset.HalfValueLayer
        return None

    @HalfValueLayer.setter
    def HalfValueLayer(self, value: Optional[Decimal]):
        if value is None:
            if "HalfValueLayer" in self._dataset:
                del self._dataset.HalfValueLayer
        else:
            self._dataset.HalfValueLayer = value

    @property
    def OrganDose(self) -> Optional[Decimal]:
        if "OrganDose" in self._dataset:
            return self._dataset.OrganDose
        return None

    @OrganDose.setter
    def OrganDose(self, value: Optional[Decimal]):
        if value is None:
            if "OrganDose" in self._dataset:
                del self._dataset.OrganDose
        else:
            self._dataset.OrganDose = value

    @property
    def EntranceDoseInmGy(self) -> Optional[Decimal]:
        if "EntranceDoseInmGy" in self._dataset:
            return self._dataset.EntranceDoseInmGy
        return None

    @EntranceDoseInmGy.setter
    def EntranceDoseInmGy(self, value: Optional[Decimal]):
        if value is None:
            if "EntranceDoseInmGy" in self._dataset:
                del self._dataset.EntranceDoseInmGy
        else:
            self._dataset.EntranceDoseInmGy = value

    @property
    def EntranceDoseDerivation(self) -> Optional[str]:
        if "EntranceDoseDerivation" in self._dataset:
            return self._dataset.EntranceDoseDerivation
        return None

    @EntranceDoseDerivation.setter
    def EntranceDoseDerivation(self, value: Optional[str]):
        if value is None:
            if "EntranceDoseDerivation" in self._dataset:
                del self._dataset.EntranceDoseDerivation
        else:
            self._dataset.EntranceDoseDerivation = value
