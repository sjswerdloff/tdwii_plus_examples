from decimal import Decimal
from typing import Any, List, Optional

import pydicom

from .beam_limiting_device_position_sequence_item import (
    BeamLimitingDevicePositionSequenceItem,
)
from .enhanced_rt_beam_limiting_opening_sequence_item import (
    EnhancedRTBeamLimitingOpeningSequenceItem,
)
from .referenced_dose_reference_sequence_item import ReferencedDoseReferenceSequenceItem
from .referenced_dose_sequence_item import ReferencedDoseSequenceItem
from .wedge_position_sequence_item import WedgePositionSequenceItem


class ControlPointSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._EnhancedRTBeamLimitingOpeningSequence: List[EnhancedRTBeamLimitingOpeningSequenceItem] = []
        self._WedgePositionSequence: List[WedgePositionSequenceItem] = []
        self._BeamLimitingDevicePositionSequence: List[BeamLimitingDevicePositionSequenceItem] = []
        self._ReferencedDoseReferenceSequence: List[ReferencedDoseReferenceSequenceItem] = []
        self._ReferencedDoseSequence: List[ReferencedDoseSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def EnhancedRTBeamLimitingOpeningSequence(self) -> Optional[List[EnhancedRTBeamLimitingOpeningSequenceItem]]:
        if "EnhancedRTBeamLimitingOpeningSequence" in self._dataset:
            if len(self._EnhancedRTBeamLimitingOpeningSequence) == len(self._dataset.EnhancedRTBeamLimitingOpeningSequence):
                return self._EnhancedRTBeamLimitingOpeningSequence
            else:
                return [
                    EnhancedRTBeamLimitingOpeningSequenceItem(x) for x in self._dataset.EnhancedRTBeamLimitingOpeningSequence
                ]
        return None

    @EnhancedRTBeamLimitingOpeningSequence.setter
    def EnhancedRTBeamLimitingOpeningSequence(self, value: Optional[List[EnhancedRTBeamLimitingOpeningSequenceItem]]):
        if value is None:
            self._EnhancedRTBeamLimitingOpeningSequence = []
            if "EnhancedRTBeamLimitingOpeningSequence" in self._dataset:
                del self._dataset.EnhancedRTBeamLimitingOpeningSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, EnhancedRTBeamLimitingOpeningSequenceItem) for item in value
        ):
            raise ValueError(
                f"EnhancedRTBeamLimitingOpeningSequence must be a list of EnhancedRTBeamLimitingOpeningSequenceItem objects"
            )
        else:
            self._EnhancedRTBeamLimitingOpeningSequence = value
            if "EnhancedRTBeamLimitingOpeningSequence" not in self._dataset:
                self._dataset.EnhancedRTBeamLimitingOpeningSequence = pydicom.Sequence()
            self._dataset.EnhancedRTBeamLimitingOpeningSequence.clear()
            self._dataset.EnhancedRTBeamLimitingOpeningSequence.extend([item.to_dataset() for item in value])

    def add_EnhancedRTBeamLimitingOpening(self, item: EnhancedRTBeamLimitingOpeningSequenceItem):
        if not isinstance(item, EnhancedRTBeamLimitingOpeningSequenceItem):
            raise ValueError(f"Item must be an instance of EnhancedRTBeamLimitingOpeningSequenceItem")
        self._EnhancedRTBeamLimitingOpeningSequence.append(item)
        if "EnhancedRTBeamLimitingOpeningSequence" not in self._dataset:
            self._dataset.EnhancedRTBeamLimitingOpeningSequence = pydicom.Sequence()
        self._dataset.EnhancedRTBeamLimitingOpeningSequence.append(item.to_dataset())

    @property
    def ControlPointIndex(self) -> Optional[int]:
        if "ControlPointIndex" in self._dataset:
            return self._dataset.ControlPointIndex
        return None

    @ControlPointIndex.setter
    def ControlPointIndex(self, value: Optional[int]):
        if value is None:
            if "ControlPointIndex" in self._dataset:
                del self._dataset.ControlPointIndex
        else:
            self._dataset.ControlPointIndex = value

    @property
    def NominalBeamEnergy(self) -> Optional[Decimal]:
        if "NominalBeamEnergy" in self._dataset:
            return self._dataset.NominalBeamEnergy
        return None

    @NominalBeamEnergy.setter
    def NominalBeamEnergy(self, value: Optional[Decimal]):
        if value is None:
            if "NominalBeamEnergy" in self._dataset:
                del self._dataset.NominalBeamEnergy
        else:
            self._dataset.NominalBeamEnergy = value

    @property
    def DoseRateSet(self) -> Optional[Decimal]:
        if "DoseRateSet" in self._dataset:
            return self._dataset.DoseRateSet
        return None

    @DoseRateSet.setter
    def DoseRateSet(self, value: Optional[Decimal]):
        if value is None:
            if "DoseRateSet" in self._dataset:
                del self._dataset.DoseRateSet
        else:
            self._dataset.DoseRateSet = value

    @property
    def WedgePositionSequence(self) -> Optional[List[WedgePositionSequenceItem]]:
        if "WedgePositionSequence" in self._dataset:
            if len(self._WedgePositionSequence) == len(self._dataset.WedgePositionSequence):
                return self._WedgePositionSequence
            else:
                return [WedgePositionSequenceItem(x) for x in self._dataset.WedgePositionSequence]
        return None

    @WedgePositionSequence.setter
    def WedgePositionSequence(self, value: Optional[List[WedgePositionSequenceItem]]):
        if value is None:
            self._WedgePositionSequence = []
            if "WedgePositionSequence" in self._dataset:
                del self._dataset.WedgePositionSequence
        elif not isinstance(value, list) or not all(isinstance(item, WedgePositionSequenceItem) for item in value):
            raise ValueError(f"WedgePositionSequence must be a list of WedgePositionSequenceItem objects")
        else:
            self._WedgePositionSequence = value
            if "WedgePositionSequence" not in self._dataset:
                self._dataset.WedgePositionSequence = pydicom.Sequence()
            self._dataset.WedgePositionSequence.clear()
            self._dataset.WedgePositionSequence.extend([item.to_dataset() for item in value])

    def add_WedgePosition(self, item: WedgePositionSequenceItem):
        if not isinstance(item, WedgePositionSequenceItem):
            raise ValueError(f"Item must be an instance of WedgePositionSequenceItem")
        self._WedgePositionSequence.append(item)
        if "WedgePositionSequence" not in self._dataset:
            self._dataset.WedgePositionSequence = pydicom.Sequence()
        self._dataset.WedgePositionSequence.append(item.to_dataset())

    @property
    def BeamLimitingDevicePositionSequence(self) -> Optional[List[BeamLimitingDevicePositionSequenceItem]]:
        if "BeamLimitingDevicePositionSequence" in self._dataset:
            if len(self._BeamLimitingDevicePositionSequence) == len(self._dataset.BeamLimitingDevicePositionSequence):
                return self._BeamLimitingDevicePositionSequence
            else:
                return [BeamLimitingDevicePositionSequenceItem(x) for x in self._dataset.BeamLimitingDevicePositionSequence]
        return None

    @BeamLimitingDevicePositionSequence.setter
    def BeamLimitingDevicePositionSequence(self, value: Optional[List[BeamLimitingDevicePositionSequenceItem]]):
        if value is None:
            self._BeamLimitingDevicePositionSequence = []
            if "BeamLimitingDevicePositionSequence" in self._dataset:
                del self._dataset.BeamLimitingDevicePositionSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, BeamLimitingDevicePositionSequenceItem) for item in value
        ):
            raise ValueError(
                f"BeamLimitingDevicePositionSequence must be a list of BeamLimitingDevicePositionSequenceItem objects"
            )
        else:
            self._BeamLimitingDevicePositionSequence = value
            if "BeamLimitingDevicePositionSequence" not in self._dataset:
                self._dataset.BeamLimitingDevicePositionSequence = pydicom.Sequence()
            self._dataset.BeamLimitingDevicePositionSequence.clear()
            self._dataset.BeamLimitingDevicePositionSequence.extend([item.to_dataset() for item in value])

    def add_BeamLimitingDevicePosition(self, item: BeamLimitingDevicePositionSequenceItem):
        if not isinstance(item, BeamLimitingDevicePositionSequenceItem):
            raise ValueError(f"Item must be an instance of BeamLimitingDevicePositionSequenceItem")
        self._BeamLimitingDevicePositionSequence.append(item)
        if "BeamLimitingDevicePositionSequence" not in self._dataset:
            self._dataset.BeamLimitingDevicePositionSequence = pydicom.Sequence()
        self._dataset.BeamLimitingDevicePositionSequence.append(item.to_dataset())

    @property
    def GantryAngle(self) -> Optional[Decimal]:
        if "GantryAngle" in self._dataset:
            return self._dataset.GantryAngle
        return None

    @GantryAngle.setter
    def GantryAngle(self, value: Optional[Decimal]):
        if value is None:
            if "GantryAngle" in self._dataset:
                del self._dataset.GantryAngle
        else:
            self._dataset.GantryAngle = value

    @property
    def GantryRotationDirection(self) -> Optional[str]:
        if "GantryRotationDirection" in self._dataset:
            return self._dataset.GantryRotationDirection
        return None

    @GantryRotationDirection.setter
    def GantryRotationDirection(self, value: Optional[str]):
        if value is None:
            if "GantryRotationDirection" in self._dataset:
                del self._dataset.GantryRotationDirection
        else:
            self._dataset.GantryRotationDirection = value

    @property
    def BeamLimitingDeviceAngle(self) -> Optional[Decimal]:
        if "BeamLimitingDeviceAngle" in self._dataset:
            return self._dataset.BeamLimitingDeviceAngle
        return None

    @BeamLimitingDeviceAngle.setter
    def BeamLimitingDeviceAngle(self, value: Optional[Decimal]):
        if value is None:
            if "BeamLimitingDeviceAngle" in self._dataset:
                del self._dataset.BeamLimitingDeviceAngle
        else:
            self._dataset.BeamLimitingDeviceAngle = value

    @property
    def BeamLimitingDeviceRotationDirection(self) -> Optional[str]:
        if "BeamLimitingDeviceRotationDirection" in self._dataset:
            return self._dataset.BeamLimitingDeviceRotationDirection
        return None

    @BeamLimitingDeviceRotationDirection.setter
    def BeamLimitingDeviceRotationDirection(self, value: Optional[str]):
        if value is None:
            if "BeamLimitingDeviceRotationDirection" in self._dataset:
                del self._dataset.BeamLimitingDeviceRotationDirection
        else:
            self._dataset.BeamLimitingDeviceRotationDirection = value

    @property
    def PatientSupportAngle(self) -> Optional[Decimal]:
        if "PatientSupportAngle" in self._dataset:
            return self._dataset.PatientSupportAngle
        return None

    @PatientSupportAngle.setter
    def PatientSupportAngle(self, value: Optional[Decimal]):
        if value is None:
            if "PatientSupportAngle" in self._dataset:
                del self._dataset.PatientSupportAngle
        else:
            self._dataset.PatientSupportAngle = value

    @property
    def PatientSupportRotationDirection(self) -> Optional[str]:
        if "PatientSupportRotationDirection" in self._dataset:
            return self._dataset.PatientSupportRotationDirection
        return None

    @PatientSupportRotationDirection.setter
    def PatientSupportRotationDirection(self, value: Optional[str]):
        if value is None:
            if "PatientSupportRotationDirection" in self._dataset:
                del self._dataset.PatientSupportRotationDirection
        else:
            self._dataset.PatientSupportRotationDirection = value

    @property
    def TableTopEccentricAxisDistance(self) -> Optional[Decimal]:
        if "TableTopEccentricAxisDistance" in self._dataset:
            return self._dataset.TableTopEccentricAxisDistance
        return None

    @TableTopEccentricAxisDistance.setter
    def TableTopEccentricAxisDistance(self, value: Optional[Decimal]):
        if value is None:
            if "TableTopEccentricAxisDistance" in self._dataset:
                del self._dataset.TableTopEccentricAxisDistance
        else:
            self._dataset.TableTopEccentricAxisDistance = value

    @property
    def TableTopEccentricAngle(self) -> Optional[Decimal]:
        if "TableTopEccentricAngle" in self._dataset:
            return self._dataset.TableTopEccentricAngle
        return None

    @TableTopEccentricAngle.setter
    def TableTopEccentricAngle(self, value: Optional[Decimal]):
        if value is None:
            if "TableTopEccentricAngle" in self._dataset:
                del self._dataset.TableTopEccentricAngle
        else:
            self._dataset.TableTopEccentricAngle = value

    @property
    def TableTopEccentricRotationDirection(self) -> Optional[str]:
        if "TableTopEccentricRotationDirection" in self._dataset:
            return self._dataset.TableTopEccentricRotationDirection
        return None

    @TableTopEccentricRotationDirection.setter
    def TableTopEccentricRotationDirection(self, value: Optional[str]):
        if value is None:
            if "TableTopEccentricRotationDirection" in self._dataset:
                del self._dataset.TableTopEccentricRotationDirection
        else:
            self._dataset.TableTopEccentricRotationDirection = value

    @property
    def TableTopVerticalPosition(self) -> Optional[Decimal]:
        if "TableTopVerticalPosition" in self._dataset:
            return self._dataset.TableTopVerticalPosition
        return None

    @TableTopVerticalPosition.setter
    def TableTopVerticalPosition(self, value: Optional[Decimal]):
        if value is None:
            if "TableTopVerticalPosition" in self._dataset:
                del self._dataset.TableTopVerticalPosition
        else:
            self._dataset.TableTopVerticalPosition = value

    @property
    def TableTopLongitudinalPosition(self) -> Optional[Decimal]:
        if "TableTopLongitudinalPosition" in self._dataset:
            return self._dataset.TableTopLongitudinalPosition
        return None

    @TableTopLongitudinalPosition.setter
    def TableTopLongitudinalPosition(self, value: Optional[Decimal]):
        if value is None:
            if "TableTopLongitudinalPosition" in self._dataset:
                del self._dataset.TableTopLongitudinalPosition
        else:
            self._dataset.TableTopLongitudinalPosition = value

    @property
    def TableTopLateralPosition(self) -> Optional[Decimal]:
        if "TableTopLateralPosition" in self._dataset:
            return self._dataset.TableTopLateralPosition
        return None

    @TableTopLateralPosition.setter
    def TableTopLateralPosition(self, value: Optional[Decimal]):
        if value is None:
            if "TableTopLateralPosition" in self._dataset:
                del self._dataset.TableTopLateralPosition
        else:
            self._dataset.TableTopLateralPosition = value

    @property
    def IsocenterPosition(self) -> Optional[List[Decimal]]:
        if "IsocenterPosition" in self._dataset:
            return self._dataset.IsocenterPosition
        return None

    @IsocenterPosition.setter
    def IsocenterPosition(self, value: Optional[List[Decimal]]):
        if value is None:
            if "IsocenterPosition" in self._dataset:
                del self._dataset.IsocenterPosition
        else:
            self._dataset.IsocenterPosition = value

    @property
    def SurfaceEntryPoint(self) -> Optional[List[Decimal]]:
        if "SurfaceEntryPoint" in self._dataset:
            return self._dataset.SurfaceEntryPoint
        return None

    @SurfaceEntryPoint.setter
    def SurfaceEntryPoint(self, value: Optional[List[Decimal]]):
        if value is None:
            if "SurfaceEntryPoint" in self._dataset:
                del self._dataset.SurfaceEntryPoint
        else:
            self._dataset.SurfaceEntryPoint = value

    @property
    def SourceToSurfaceDistance(self) -> Optional[Decimal]:
        if "SourceToSurfaceDistance" in self._dataset:
            return self._dataset.SourceToSurfaceDistance
        return None

    @SourceToSurfaceDistance.setter
    def SourceToSurfaceDistance(self, value: Optional[Decimal]):
        if value is None:
            if "SourceToSurfaceDistance" in self._dataset:
                del self._dataset.SourceToSurfaceDistance
        else:
            self._dataset.SourceToSurfaceDistance = value

    @property
    def SourceToExternalContourDistance(self) -> Optional[float]:
        if "SourceToExternalContourDistance" in self._dataset:
            return self._dataset.SourceToExternalContourDistance
        return None

    @SourceToExternalContourDistance.setter
    def SourceToExternalContourDistance(self, value: Optional[float]):
        if value is None:
            if "SourceToExternalContourDistance" in self._dataset:
                del self._dataset.SourceToExternalContourDistance
        else:
            self._dataset.SourceToExternalContourDistance = value

    @property
    def ExternalContourEntryPoint(self) -> Optional[List[float]]:
        if "ExternalContourEntryPoint" in self._dataset:
            return self._dataset.ExternalContourEntryPoint
        return None

    @ExternalContourEntryPoint.setter
    def ExternalContourEntryPoint(self, value: Optional[List[float]]):
        if value is None:
            if "ExternalContourEntryPoint" in self._dataset:
                del self._dataset.ExternalContourEntryPoint
        else:
            self._dataset.ExternalContourEntryPoint = value

    @property
    def CumulativeMetersetWeight(self) -> Optional[Decimal]:
        if "CumulativeMetersetWeight" in self._dataset:
            return self._dataset.CumulativeMetersetWeight
        return None

    @CumulativeMetersetWeight.setter
    def CumulativeMetersetWeight(self, value: Optional[Decimal]):
        if value is None:
            if "CumulativeMetersetWeight" in self._dataset:
                del self._dataset.CumulativeMetersetWeight
        else:
            self._dataset.CumulativeMetersetWeight = value

    @property
    def TableTopPitchAngle(self) -> Optional[float]:
        if "TableTopPitchAngle" in self._dataset:
            return self._dataset.TableTopPitchAngle
        return None

    @TableTopPitchAngle.setter
    def TableTopPitchAngle(self, value: Optional[float]):
        if value is None:
            if "TableTopPitchAngle" in self._dataset:
                del self._dataset.TableTopPitchAngle
        else:
            self._dataset.TableTopPitchAngle = value

    @property
    def TableTopPitchRotationDirection(self) -> Optional[str]:
        if "TableTopPitchRotationDirection" in self._dataset:
            return self._dataset.TableTopPitchRotationDirection
        return None

    @TableTopPitchRotationDirection.setter
    def TableTopPitchRotationDirection(self, value: Optional[str]):
        if value is None:
            if "TableTopPitchRotationDirection" in self._dataset:
                del self._dataset.TableTopPitchRotationDirection
        else:
            self._dataset.TableTopPitchRotationDirection = value

    @property
    def TableTopRollAngle(self) -> Optional[float]:
        if "TableTopRollAngle" in self._dataset:
            return self._dataset.TableTopRollAngle
        return None

    @TableTopRollAngle.setter
    def TableTopRollAngle(self, value: Optional[float]):
        if value is None:
            if "TableTopRollAngle" in self._dataset:
                del self._dataset.TableTopRollAngle
        else:
            self._dataset.TableTopRollAngle = value

    @property
    def TableTopRollRotationDirection(self) -> Optional[str]:
        if "TableTopRollRotationDirection" in self._dataset:
            return self._dataset.TableTopRollRotationDirection
        return None

    @TableTopRollRotationDirection.setter
    def TableTopRollRotationDirection(self, value: Optional[str]):
        if value is None:
            if "TableTopRollRotationDirection" in self._dataset:
                del self._dataset.TableTopRollRotationDirection
        else:
            self._dataset.TableTopRollRotationDirection = value

    @property
    def GantryPitchAngle(self) -> Optional[float]:
        if "GantryPitchAngle" in self._dataset:
            return self._dataset.GantryPitchAngle
        return None

    @GantryPitchAngle.setter
    def GantryPitchAngle(self, value: Optional[float]):
        if value is None:
            if "GantryPitchAngle" in self._dataset:
                del self._dataset.GantryPitchAngle
        else:
            self._dataset.GantryPitchAngle = value

    @property
    def GantryPitchRotationDirection(self) -> Optional[str]:
        if "GantryPitchRotationDirection" in self._dataset:
            return self._dataset.GantryPitchRotationDirection
        return None

    @GantryPitchRotationDirection.setter
    def GantryPitchRotationDirection(self, value: Optional[str]):
        if value is None:
            if "GantryPitchRotationDirection" in self._dataset:
                del self._dataset.GantryPitchRotationDirection
        else:
            self._dataset.GantryPitchRotationDirection = value

    @property
    def ReferencedDoseReferenceSequence(self) -> Optional[List[ReferencedDoseReferenceSequenceItem]]:
        if "ReferencedDoseReferenceSequence" in self._dataset:
            if len(self._ReferencedDoseReferenceSequence) == len(self._dataset.ReferencedDoseReferenceSequence):
                return self._ReferencedDoseReferenceSequence
            else:
                return [ReferencedDoseReferenceSequenceItem(x) for x in self._dataset.ReferencedDoseReferenceSequence]
        return None

    @ReferencedDoseReferenceSequence.setter
    def ReferencedDoseReferenceSequence(self, value: Optional[List[ReferencedDoseReferenceSequenceItem]]):
        if value is None:
            self._ReferencedDoseReferenceSequence = []
            if "ReferencedDoseReferenceSequence" in self._dataset:
                del self._dataset.ReferencedDoseReferenceSequence
        elif not isinstance(value, list) or not all(isinstance(item, ReferencedDoseReferenceSequenceItem) for item in value):
            raise ValueError(f"ReferencedDoseReferenceSequence must be a list of ReferencedDoseReferenceSequenceItem objects")
        else:
            self._ReferencedDoseReferenceSequence = value
            if "ReferencedDoseReferenceSequence" not in self._dataset:
                self._dataset.ReferencedDoseReferenceSequence = pydicom.Sequence()
            self._dataset.ReferencedDoseReferenceSequence.clear()
            self._dataset.ReferencedDoseReferenceSequence.extend([item.to_dataset() for item in value])

    def add_ReferencedDoseReference(self, item: ReferencedDoseReferenceSequenceItem):
        if not isinstance(item, ReferencedDoseReferenceSequenceItem):
            raise ValueError(f"Item must be an instance of ReferencedDoseReferenceSequenceItem")
        self._ReferencedDoseReferenceSequence.append(item)
        if "ReferencedDoseReferenceSequence" not in self._dataset:
            self._dataset.ReferencedDoseReferenceSequence = pydicom.Sequence()
        self._dataset.ReferencedDoseReferenceSequence.append(item.to_dataset())

    @property
    def ReferencedDoseSequence(self) -> Optional[List[ReferencedDoseSequenceItem]]:
        if "ReferencedDoseSequence" in self._dataset:
            if len(self._ReferencedDoseSequence) == len(self._dataset.ReferencedDoseSequence):
                return self._ReferencedDoseSequence
            else:
                return [ReferencedDoseSequenceItem(x) for x in self._dataset.ReferencedDoseSequence]
        return None

    @ReferencedDoseSequence.setter
    def ReferencedDoseSequence(self, value: Optional[List[ReferencedDoseSequenceItem]]):
        if value is None:
            self._ReferencedDoseSequence = []
            if "ReferencedDoseSequence" in self._dataset:
                del self._dataset.ReferencedDoseSequence
        elif not isinstance(value, list) or not all(isinstance(item, ReferencedDoseSequenceItem) for item in value):
            raise ValueError(f"ReferencedDoseSequence must be a list of ReferencedDoseSequenceItem objects")
        else:
            self._ReferencedDoseSequence = value
            if "ReferencedDoseSequence" not in self._dataset:
                self._dataset.ReferencedDoseSequence = pydicom.Sequence()
            self._dataset.ReferencedDoseSequence.clear()
            self._dataset.ReferencedDoseSequence.extend([item.to_dataset() for item in value])

    def add_ReferencedDose(self, item: ReferencedDoseSequenceItem):
        if not isinstance(item, ReferencedDoseSequenceItem):
            raise ValueError(f"Item must be an instance of ReferencedDoseSequenceItem")
        self._ReferencedDoseSequence.append(item)
        if "ReferencedDoseSequence" not in self._dataset:
            self._dataset.ReferencedDoseSequence = pydicom.Sequence()
        self._dataset.ReferencedDoseSequence.append(item.to_dataset())
