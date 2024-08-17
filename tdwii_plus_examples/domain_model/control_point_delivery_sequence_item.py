from decimal import Decimal
from typing import Any, List, Optional  # noqa

import pydicom

from .beam_limiting_device_position_sequence_item import (
    BeamLimitingDevicePositionSequenceItem,
)
from .corrected_parameter_sequence_item import CorrectedParameterSequenceItem
from .enhanced_rt_beam_limiting_opening_sequence_item import (
    EnhancedRTBeamLimitingOpeningSequenceItem,
)
from .override_sequence_item import OverrideSequenceItem
from .wedge_position_sequence_item import WedgePositionSequenceItem


class ControlPointDeliverySequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._OverrideSequence: List[OverrideSequenceItem] = []
        self._CorrectedParameterSequence: List[CorrectedParameterSequenceItem] = []
        self._EnhancedRTBeamLimitingOpeningSequence: List[EnhancedRTBeamLimitingOpeningSequenceItem] = []
        self._WedgePositionSequence: List[WedgePositionSequenceItem] = []
        self._BeamLimitingDevicePositionSequence: List[BeamLimitingDevicePositionSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def TreatmentControlPointDate(self) -> Optional[str]:
        if "TreatmentControlPointDate" in self._dataset:
            return self._dataset.TreatmentControlPointDate
        return None

    @TreatmentControlPointDate.setter
    def TreatmentControlPointDate(self, value: Optional[str]):
        if value is None:
            if "TreatmentControlPointDate" in self._dataset:
                del self._dataset.TreatmentControlPointDate
        else:
            self._dataset.TreatmentControlPointDate = value

    @property
    def TreatmentControlPointTime(self) -> Optional[str]:
        if "TreatmentControlPointTime" in self._dataset:
            return self._dataset.TreatmentControlPointTime
        return None

    @TreatmentControlPointTime.setter
    def TreatmentControlPointTime(self, value: Optional[str]):
        if value is None:
            if "TreatmentControlPointTime" in self._dataset:
                del self._dataset.TreatmentControlPointTime
        else:
            self._dataset.TreatmentControlPointTime = value

    @property
    def SpecifiedMeterset(self) -> Optional[Decimal]:
        if "SpecifiedMeterset" in self._dataset:
            return self._dataset.SpecifiedMeterset
        return None

    @SpecifiedMeterset.setter
    def SpecifiedMeterset(self, value: Optional[Decimal]):
        if value is None:
            if "SpecifiedMeterset" in self._dataset:
                del self._dataset.SpecifiedMeterset
        else:
            self._dataset.SpecifiedMeterset = value

    @property
    def DeliveredMeterset(self) -> Optional[Decimal]:
        if "DeliveredMeterset" in self._dataset:
            return self._dataset.DeliveredMeterset
        return None

    @DeliveredMeterset.setter
    def DeliveredMeterset(self, value: Optional[Decimal]):
        if value is None:
            if "DeliveredMeterset" in self._dataset:
                del self._dataset.DeliveredMeterset
        else:
            self._dataset.DeliveredMeterset = value

    @property
    def DoseRateDelivered(self) -> Optional[Decimal]:
        if "DoseRateDelivered" in self._dataset:
            return self._dataset.DoseRateDelivered
        return None

    @DoseRateDelivered.setter
    def DoseRateDelivered(self, value: Optional[Decimal]):
        if value is None:
            if "DoseRateDelivered" in self._dataset:
                del self._dataset.DoseRateDelivered
        else:
            self._dataset.DoseRateDelivered = value

    @property
    def OverrideSequence(self) -> Optional[List[OverrideSequenceItem]]:
        if "OverrideSequence" in self._dataset:
            if len(self._OverrideSequence) == len(self._dataset.OverrideSequence):
                return self._OverrideSequence
            else:
                return [OverrideSequenceItem(x) for x in self._dataset.OverrideSequence]
        return None

    @OverrideSequence.setter
    def OverrideSequence(self, value: Optional[List[OverrideSequenceItem]]):
        if value is None:
            self._OverrideSequence = []
            if "OverrideSequence" in self._dataset:
                del self._dataset.OverrideSequence
        elif not isinstance(value, list) or not all(isinstance(item, OverrideSequenceItem) for item in value):
            raise ValueError("OverrideSequence must be a list of OverrideSequenceItem objects")
        else:
            self._OverrideSequence = value
            if "OverrideSequence" not in self._dataset:
                self._dataset.OverrideSequence = pydicom.Sequence()
            self._dataset.OverrideSequence.clear()
            self._dataset.OverrideSequence.extend([item.to_dataset() for item in value])

    def add_Override(self, item: OverrideSequenceItem):
        if not isinstance(item, OverrideSequenceItem):
            raise ValueError("Item must be an instance of OverrideSequenceItem")
        self._OverrideSequence.append(item)
        if "OverrideSequence" not in self._dataset:
            self._dataset.OverrideSequence = pydicom.Sequence()
        self._dataset.OverrideSequence.append(item.to_dataset())

    @property
    def CorrectedParameterSequence(self) -> Optional[List[CorrectedParameterSequenceItem]]:
        if "CorrectedParameterSequence" in self._dataset:
            if len(self._CorrectedParameterSequence) == len(self._dataset.CorrectedParameterSequence):
                return self._CorrectedParameterSequence
            else:
                return [CorrectedParameterSequenceItem(x) for x in self._dataset.CorrectedParameterSequence]
        return None

    @CorrectedParameterSequence.setter
    def CorrectedParameterSequence(self, value: Optional[List[CorrectedParameterSequenceItem]]):
        if value is None:
            self._CorrectedParameterSequence = []
            if "CorrectedParameterSequence" in self._dataset:
                del self._dataset.CorrectedParameterSequence
        elif not isinstance(value, list) or not all(isinstance(item, CorrectedParameterSequenceItem) for item in value):
            raise ValueError("CorrectedParameterSequence must be a list of CorrectedParameterSequenceItem objects")
        else:
            self._CorrectedParameterSequence = value
            if "CorrectedParameterSequence" not in self._dataset:
                self._dataset.CorrectedParameterSequence = pydicom.Sequence()
            self._dataset.CorrectedParameterSequence.clear()
            self._dataset.CorrectedParameterSequence.extend([item.to_dataset() for item in value])

    def add_CorrectedParameter(self, item: CorrectedParameterSequenceItem):
        if not isinstance(item, CorrectedParameterSequenceItem):
            raise ValueError("Item must be an instance of CorrectedParameterSequenceItem")
        self._CorrectedParameterSequence.append(item)
        if "CorrectedParameterSequence" not in self._dataset:
            self._dataset.CorrectedParameterSequence = pydicom.Sequence()
        self._dataset.CorrectedParameterSequence.append(item.to_dataset())

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
                "EnhancedRTBeamLimitingOpeningSequence must be a list of EnhancedRTBeamLimitingOpeningSequenceItem objects"
            )
        else:
            self._EnhancedRTBeamLimitingOpeningSequence = value
            if "EnhancedRTBeamLimitingOpeningSequence" not in self._dataset:
                self._dataset.EnhancedRTBeamLimitingOpeningSequence = pydicom.Sequence()
            self._dataset.EnhancedRTBeamLimitingOpeningSequence.clear()
            self._dataset.EnhancedRTBeamLimitingOpeningSequence.extend([item.to_dataset() for item in value])

    def add_EnhancedRTBeamLimitingOpening(self, item: EnhancedRTBeamLimitingOpeningSequenceItem):
        if not isinstance(item, EnhancedRTBeamLimitingOpeningSequenceItem):
            raise ValueError("Item must be an instance of EnhancedRTBeamLimitingOpeningSequenceItem")
        self._EnhancedRTBeamLimitingOpeningSequence.append(item)
        if "EnhancedRTBeamLimitingOpeningSequence" not in self._dataset:
            self._dataset.EnhancedRTBeamLimitingOpeningSequence = pydicom.Sequence()
        self._dataset.EnhancedRTBeamLimitingOpeningSequence.append(item.to_dataset())

    @property
    def BeamStopperPosition(self) -> Optional[str]:
        if "BeamStopperPosition" in self._dataset:
            return self._dataset.BeamStopperPosition
        return None

    @BeamStopperPosition.setter
    def BeamStopperPosition(self, value: Optional[str]):
        if value is None:
            if "BeamStopperPosition" in self._dataset:
                del self._dataset.BeamStopperPosition
        else:
            self._dataset.BeamStopperPosition = value

    @property
    def NominalBeamEnergyUnit(self) -> Optional[str]:
        if "NominalBeamEnergyUnit" in self._dataset:
            return self._dataset.NominalBeamEnergyUnit
        return None

    @NominalBeamEnergyUnit.setter
    def NominalBeamEnergyUnit(self, value: Optional[str]):
        if value is None:
            if "NominalBeamEnergyUnit" in self._dataset:
                del self._dataset.NominalBeamEnergyUnit
        else:
            self._dataset.NominalBeamEnergyUnit = value

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
            raise ValueError("WedgePositionSequence must be a list of WedgePositionSequenceItem objects")
        else:
            self._WedgePositionSequence = value
            if "WedgePositionSequence" not in self._dataset:
                self._dataset.WedgePositionSequence = pydicom.Sequence()
            self._dataset.WedgePositionSequence.clear()
            self._dataset.WedgePositionSequence.extend([item.to_dataset() for item in value])

    def add_WedgePosition(self, item: WedgePositionSequenceItem):
        if not isinstance(item, WedgePositionSequenceItem):
            raise ValueError("Item must be an instance of WedgePositionSequenceItem")
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
                "BeamLimitingDevicePositionSequence must be a list of BeamLimitingDevicePositionSequenceItem objects"
            )
        else:
            self._BeamLimitingDevicePositionSequence = value
            if "BeamLimitingDevicePositionSequence" not in self._dataset:
                self._dataset.BeamLimitingDevicePositionSequence = pydicom.Sequence()
            self._dataset.BeamLimitingDevicePositionSequence.clear()
            self._dataset.BeamLimitingDevicePositionSequence.extend([item.to_dataset() for item in value])

    def add_BeamLimitingDevicePosition(self, item: BeamLimitingDevicePositionSequenceItem):
        if not isinstance(item, BeamLimitingDevicePositionSequenceItem):
            raise ValueError("Item must be an instance of BeamLimitingDevicePositionSequenceItem")
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
    def ReferencedControlPointIndex(self) -> Optional[int]:
        if "ReferencedControlPointIndex" in self._dataset:
            return self._dataset.ReferencedControlPointIndex
        return None

    @ReferencedControlPointIndex.setter
    def ReferencedControlPointIndex(self, value: Optional[int]):
        if value is None:
            if "ReferencedControlPointIndex" in self._dataset:
                del self._dataset.ReferencedControlPointIndex
        else:
            self._dataset.ReferencedControlPointIndex = value
