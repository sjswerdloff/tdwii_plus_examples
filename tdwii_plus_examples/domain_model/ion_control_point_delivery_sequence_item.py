from decimal import Decimal
from typing import Any, List, Optional

import pydicom

from .beam_limiting_device_position_sequence_item import (
    BeamLimitingDevicePositionSequenceItem,
)
from .corrected_parameter_sequence_item import CorrectedParameterSequenceItem
from .enhanced_rt_beam_limiting_opening_sequence_item import (
    EnhancedRTBeamLimitingOpeningSequenceItem,
)
from .ion_wedge_position_sequence_item import IonWedgePositionSequenceItem
from .lateral_spreading_device_settings_sequence_item import (
    LateralSpreadingDeviceSettingsSequenceItem,
)
from .override_sequence_item import OverrideSequenceItem
from .range_modulator_settings_sequence_item import RangeModulatorSettingsSequenceItem
from .range_shifter_settings_sequence_item import RangeShifterSettingsSequenceItem


class IonControlPointDeliverySequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._OverrideSequence: List[OverrideSequenceItem] = []
        self._CorrectedParameterSequence: List[CorrectedParameterSequenceItem] = []
        self._EnhancedRTBeamLimitingOpeningSequence: List[EnhancedRTBeamLimitingOpeningSequenceItem] = []
        self._BeamLimitingDevicePositionSequence: List[BeamLimitingDevicePositionSequenceItem] = []
        self._RangeShifterSettingsSequence: List[RangeShifterSettingsSequenceItem] = []
        self._LateralSpreadingDeviceSettingsSequence: List[LateralSpreadingDeviceSettingsSequenceItem] = []
        self._RangeModulatorSettingsSequence: List[RangeModulatorSettingsSequenceItem] = []
        self._IonWedgePositionSequence: List[IonWedgePositionSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

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
    def MetersetRateSet(self) -> Optional[float]:
        if "MetersetRateSet" in self._dataset:
            return self._dataset.MetersetRateSet
        return None

    @MetersetRateSet.setter
    def MetersetRateSet(self, value: Optional[float]):
        if value is None:
            if "MetersetRateSet" in self._dataset:
                del self._dataset.MetersetRateSet
        else:
            self._dataset.MetersetRateSet = value

    @property
    def MetersetRateDelivered(self) -> Optional[float]:
        if "MetersetRateDelivered" in self._dataset:
            return self._dataset.MetersetRateDelivered
        return None

    @MetersetRateDelivered.setter
    def MetersetRateDelivered(self, value: Optional[float]):
        if value is None:
            if "MetersetRateDelivered" in self._dataset:
                del self._dataset.MetersetRateDelivered
        else:
            self._dataset.MetersetRateDelivered = value

    @property
    def ScanSpotMetersetsDelivered(self) -> Optional[List[float]]:
        if "ScanSpotMetersetsDelivered" in self._dataset:
            return self._dataset.ScanSpotMetersetsDelivered
        return None

    @ScanSpotMetersetsDelivered.setter
    def ScanSpotMetersetsDelivered(self, value: Optional[List[float]]):
        if value is None:
            if "ScanSpotMetersetsDelivered" in self._dataset:
                del self._dataset.ScanSpotMetersetsDelivered
        else:
            self._dataset.ScanSpotMetersetsDelivered = value

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
            raise ValueError(f"OverrideSequence must be a list of OverrideSequenceItem objects")
        else:
            self._OverrideSequence = value
            if "OverrideSequence" not in self._dataset:
                self._dataset.OverrideSequence = pydicom.Sequence()
            self._dataset.OverrideSequence.clear()
            self._dataset.OverrideSequence.extend([item.to_dataset() for item in value])

    def add_Override(self, item: OverrideSequenceItem):
        if not isinstance(item, OverrideSequenceItem):
            raise ValueError(f"Item must be an instance of OverrideSequenceItem")
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
            raise ValueError(f"CorrectedParameterSequence must be a list of CorrectedParameterSequenceItem objects")
        else:
            self._CorrectedParameterSequence = value
            if "CorrectedParameterSequence" not in self._dataset:
                self._dataset.CorrectedParameterSequence = pydicom.Sequence()
            self._dataset.CorrectedParameterSequence.clear()
            self._dataset.CorrectedParameterSequence.extend([item.to_dataset() for item in value])

    def add_CorrectedParameter(self, item: CorrectedParameterSequenceItem):
        if not isinstance(item, CorrectedParameterSequenceItem):
            raise ValueError(f"Item must be an instance of CorrectedParameterSequenceItem")
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
    def HeadFixationAngle(self) -> Optional[float]:
        if "HeadFixationAngle" in self._dataset:
            return self._dataset.HeadFixationAngle
        return None

    @HeadFixationAngle.setter
    def HeadFixationAngle(self, value: Optional[float]):
        if value is None:
            if "HeadFixationAngle" in self._dataset:
                del self._dataset.HeadFixationAngle
        else:
            self._dataset.HeadFixationAngle = value

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
    def ChairHeadFramePosition(self) -> Optional[Decimal]:
        if "ChairHeadFramePosition" in self._dataset:
            return self._dataset.ChairHeadFramePosition
        return None

    @ChairHeadFramePosition.setter
    def ChairHeadFramePosition(self, value: Optional[Decimal]):
        if value is None:
            if "ChairHeadFramePosition" in self._dataset:
                del self._dataset.ChairHeadFramePosition
        else:
            self._dataset.ChairHeadFramePosition = value

    @property
    def SnoutPosition(self) -> Optional[float]:
        if "SnoutPosition" in self._dataset:
            return self._dataset.SnoutPosition
        return None

    @SnoutPosition.setter
    def SnoutPosition(self, value: Optional[float]):
        if value is None:
            if "SnoutPosition" in self._dataset:
                del self._dataset.SnoutPosition
        else:
            self._dataset.SnoutPosition = value

    @property
    def RangeShifterSettingsSequence(self) -> Optional[List[RangeShifterSettingsSequenceItem]]:
        if "RangeShifterSettingsSequence" in self._dataset:
            if len(self._RangeShifterSettingsSequence) == len(self._dataset.RangeShifterSettingsSequence):
                return self._RangeShifterSettingsSequence
            else:
                return [RangeShifterSettingsSequenceItem(x) for x in self._dataset.RangeShifterSettingsSequence]
        return None

    @RangeShifterSettingsSequence.setter
    def RangeShifterSettingsSequence(self, value: Optional[List[RangeShifterSettingsSequenceItem]]):
        if value is None:
            self._RangeShifterSettingsSequence = []
            if "RangeShifterSettingsSequence" in self._dataset:
                del self._dataset.RangeShifterSettingsSequence
        elif not isinstance(value, list) or not all(isinstance(item, RangeShifterSettingsSequenceItem) for item in value):
            raise ValueError(f"RangeShifterSettingsSequence must be a list of RangeShifterSettingsSequenceItem objects")
        else:
            self._RangeShifterSettingsSequence = value
            if "RangeShifterSettingsSequence" not in self._dataset:
                self._dataset.RangeShifterSettingsSequence = pydicom.Sequence()
            self._dataset.RangeShifterSettingsSequence.clear()
            self._dataset.RangeShifterSettingsSequence.extend([item.to_dataset() for item in value])

    def add_RangeShifterSettings(self, item: RangeShifterSettingsSequenceItem):
        if not isinstance(item, RangeShifterSettingsSequenceItem):
            raise ValueError(f"Item must be an instance of RangeShifterSettingsSequenceItem")
        self._RangeShifterSettingsSequence.append(item)
        if "RangeShifterSettingsSequence" not in self._dataset:
            self._dataset.RangeShifterSettingsSequence = pydicom.Sequence()
        self._dataset.RangeShifterSettingsSequence.append(item.to_dataset())

    @property
    def LateralSpreadingDeviceSettingsSequence(self) -> Optional[List[LateralSpreadingDeviceSettingsSequenceItem]]:
        if "LateralSpreadingDeviceSettingsSequence" in self._dataset:
            if len(self._LateralSpreadingDeviceSettingsSequence) == len(self._dataset.LateralSpreadingDeviceSettingsSequence):
                return self._LateralSpreadingDeviceSettingsSequence
            else:
                return [
                    LateralSpreadingDeviceSettingsSequenceItem(x) for x in self._dataset.LateralSpreadingDeviceSettingsSequence
                ]
        return None

    @LateralSpreadingDeviceSettingsSequence.setter
    def LateralSpreadingDeviceSettingsSequence(self, value: Optional[List[LateralSpreadingDeviceSettingsSequenceItem]]):
        if value is None:
            self._LateralSpreadingDeviceSettingsSequence = []
            if "LateralSpreadingDeviceSettingsSequence" in self._dataset:
                del self._dataset.LateralSpreadingDeviceSettingsSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, LateralSpreadingDeviceSettingsSequenceItem) for item in value
        ):
            raise ValueError(
                f"LateralSpreadingDeviceSettingsSequence must be a list of LateralSpreadingDeviceSettingsSequenceItem objects"
            )
        else:
            self._LateralSpreadingDeviceSettingsSequence = value
            if "LateralSpreadingDeviceSettingsSequence" not in self._dataset:
                self._dataset.LateralSpreadingDeviceSettingsSequence = pydicom.Sequence()
            self._dataset.LateralSpreadingDeviceSettingsSequence.clear()
            self._dataset.LateralSpreadingDeviceSettingsSequence.extend([item.to_dataset() for item in value])

    def add_LateralSpreadingDeviceSettings(self, item: LateralSpreadingDeviceSettingsSequenceItem):
        if not isinstance(item, LateralSpreadingDeviceSettingsSequenceItem):
            raise ValueError(f"Item must be an instance of LateralSpreadingDeviceSettingsSequenceItem")
        self._LateralSpreadingDeviceSettingsSequence.append(item)
        if "LateralSpreadingDeviceSettingsSequence" not in self._dataset:
            self._dataset.LateralSpreadingDeviceSettingsSequence = pydicom.Sequence()
        self._dataset.LateralSpreadingDeviceSettingsSequence.append(item.to_dataset())

    @property
    def RangeModulatorSettingsSequence(self) -> Optional[List[RangeModulatorSettingsSequenceItem]]:
        if "RangeModulatorSettingsSequence" in self._dataset:
            if len(self._RangeModulatorSettingsSequence) == len(self._dataset.RangeModulatorSettingsSequence):
                return self._RangeModulatorSettingsSequence
            else:
                return [RangeModulatorSettingsSequenceItem(x) for x in self._dataset.RangeModulatorSettingsSequence]
        return None

    @RangeModulatorSettingsSequence.setter
    def RangeModulatorSettingsSequence(self, value: Optional[List[RangeModulatorSettingsSequenceItem]]):
        if value is None:
            self._RangeModulatorSettingsSequence = []
            if "RangeModulatorSettingsSequence" in self._dataset:
                del self._dataset.RangeModulatorSettingsSequence
        elif not isinstance(value, list) or not all(isinstance(item, RangeModulatorSettingsSequenceItem) for item in value):
            raise ValueError(f"RangeModulatorSettingsSequence must be a list of RangeModulatorSettingsSequenceItem objects")
        else:
            self._RangeModulatorSettingsSequence = value
            if "RangeModulatorSettingsSequence" not in self._dataset:
                self._dataset.RangeModulatorSettingsSequence = pydicom.Sequence()
            self._dataset.RangeModulatorSettingsSequence.clear()
            self._dataset.RangeModulatorSettingsSequence.extend([item.to_dataset() for item in value])

    def add_RangeModulatorSettings(self, item: RangeModulatorSettingsSequenceItem):
        if not isinstance(item, RangeModulatorSettingsSequenceItem):
            raise ValueError(f"Item must be an instance of RangeModulatorSettingsSequenceItem")
        self._RangeModulatorSettingsSequence.append(item)
        if "RangeModulatorSettingsSequence" not in self._dataset:
            self._dataset.RangeModulatorSettingsSequence = pydicom.Sequence()
        self._dataset.RangeModulatorSettingsSequence.append(item.to_dataset())

    @property
    def ScanSpotTimeOffset(self) -> Optional[List[float]]:
        if "ScanSpotTimeOffset" in self._dataset:
            return self._dataset.ScanSpotTimeOffset
        return None

    @ScanSpotTimeOffset.setter
    def ScanSpotTimeOffset(self, value: Optional[List[float]]):
        if value is None:
            if "ScanSpotTimeOffset" in self._dataset:
                del self._dataset.ScanSpotTimeOffset
        else:
            self._dataset.ScanSpotTimeOffset = value

    @property
    def ScanSpotTuneID(self) -> Optional[str]:
        if "ScanSpotTuneID" in self._dataset:
            return self._dataset.ScanSpotTuneID
        return None

    @ScanSpotTuneID.setter
    def ScanSpotTuneID(self, value: Optional[str]):
        if value is None:
            if "ScanSpotTuneID" in self._dataset:
                del self._dataset.ScanSpotTuneID
        else:
            self._dataset.ScanSpotTuneID = value

    @property
    def ScanSpotPrescribedIndices(self) -> Optional[List[int]]:
        if "ScanSpotPrescribedIndices" in self._dataset:
            return self._dataset.ScanSpotPrescribedIndices
        return None

    @ScanSpotPrescribedIndices.setter
    def ScanSpotPrescribedIndices(self, value: Optional[List[int]]):
        if value is None:
            if "ScanSpotPrescribedIndices" in self._dataset:
                del self._dataset.ScanSpotPrescribedIndices
        else:
            self._dataset.ScanSpotPrescribedIndices = value

    @property
    def NumberOfScanSpotPositions(self) -> Optional[int]:
        if "NumberOfScanSpotPositions" in self._dataset:
            return self._dataset.NumberOfScanSpotPositions
        return None

    @NumberOfScanSpotPositions.setter
    def NumberOfScanSpotPositions(self, value: Optional[int]):
        if value is None:
            if "NumberOfScanSpotPositions" in self._dataset:
                del self._dataset.NumberOfScanSpotPositions
        else:
            self._dataset.NumberOfScanSpotPositions = value

    @property
    def ScanSpotReordered(self) -> Optional[str]:
        if "ScanSpotReordered" in self._dataset:
            return self._dataset.ScanSpotReordered
        return None

    @ScanSpotReordered.setter
    def ScanSpotReordered(self, value: Optional[str]):
        if value is None:
            if "ScanSpotReordered" in self._dataset:
                del self._dataset.ScanSpotReordered
        else:
            self._dataset.ScanSpotReordered = value

    @property
    def ScanSpotPositionMap(self) -> Optional[List[float]]:
        if "ScanSpotPositionMap" in self._dataset:
            return self._dataset.ScanSpotPositionMap
        return None

    @ScanSpotPositionMap.setter
    def ScanSpotPositionMap(self, value: Optional[List[float]]):
        if value is None:
            if "ScanSpotPositionMap" in self._dataset:
                del self._dataset.ScanSpotPositionMap
        else:
            self._dataset.ScanSpotPositionMap = value

    @property
    def ScanSpotSizesDelivered(self) -> Optional[List[float]]:
        if "ScanSpotSizesDelivered" in self._dataset:
            return self._dataset.ScanSpotSizesDelivered
        return None

    @ScanSpotSizesDelivered.setter
    def ScanSpotSizesDelivered(self, value: Optional[List[float]]):
        if value is None:
            if "ScanSpotSizesDelivered" in self._dataset:
                del self._dataset.ScanSpotSizesDelivered
        else:
            self._dataset.ScanSpotSizesDelivered = value

    @property
    def NumberOfPaintings(self) -> Optional[int]:
        if "NumberOfPaintings" in self._dataset:
            return self._dataset.NumberOfPaintings
        return None

    @NumberOfPaintings.setter
    def NumberOfPaintings(self, value: Optional[int]):
        if value is None:
            if "NumberOfPaintings" in self._dataset:
                del self._dataset.NumberOfPaintings
        else:
            self._dataset.NumberOfPaintings = value

    @property
    def IonWedgePositionSequence(self) -> Optional[List[IonWedgePositionSequenceItem]]:
        if "IonWedgePositionSequence" in self._dataset:
            if len(self._IonWedgePositionSequence) == len(self._dataset.IonWedgePositionSequence):
                return self._IonWedgePositionSequence
            else:
                return [IonWedgePositionSequenceItem(x) for x in self._dataset.IonWedgePositionSequence]
        return None

    @IonWedgePositionSequence.setter
    def IonWedgePositionSequence(self, value: Optional[List[IonWedgePositionSequenceItem]]):
        if value is None:
            self._IonWedgePositionSequence = []
            if "IonWedgePositionSequence" in self._dataset:
                del self._dataset.IonWedgePositionSequence
        elif not isinstance(value, list) or not all(isinstance(item, IonWedgePositionSequenceItem) for item in value):
            raise ValueError(f"IonWedgePositionSequence must be a list of IonWedgePositionSequenceItem objects")
        else:
            self._IonWedgePositionSequence = value
            if "IonWedgePositionSequence" not in self._dataset:
                self._dataset.IonWedgePositionSequence = pydicom.Sequence()
            self._dataset.IonWedgePositionSequence.clear()
            self._dataset.IonWedgePositionSequence.extend([item.to_dataset() for item in value])

    def add_IonWedgePosition(self, item: IonWedgePositionSequenceItem):
        if not isinstance(item, IonWedgePositionSequenceItem):
            raise ValueError(f"Item must be an instance of IonWedgePositionSequenceItem")
        self._IonWedgePositionSequence.append(item)
        if "IonWedgePositionSequence" not in self._dataset:
            self._dataset.IonWedgePositionSequence = pydicom.Sequence()
        self._dataset.IonWedgePositionSequence.append(item.to_dataset())

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
