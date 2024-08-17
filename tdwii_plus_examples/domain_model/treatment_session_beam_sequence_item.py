from decimal import Decimal
from typing import Any, List, Optional  # noqa

import pydicom

from .applicator_sequence_item import ApplicatorSequenceItem
from .beam_limiting_device_leaf_pairs_sequence_item import (
    BeamLimitingDeviceLeafPairsSequenceItem,
)
from .code_sequence_item import CodeSequenceItem
from .control_point_delivery_sequence_item import ControlPointDeliverySequenceItem
from .definition_source_sequence_item import DefinitionSourceSequenceItem
from .dose_calibration_conditions_sequence_item import (
    DoseCalibrationConditionsSequenceItem,
)
from .enhanced_rt_beam_limiting_device_sequence_item import (
    EnhancedRTBeamLimitingDeviceSequenceItem,
)
from .gating_beam_hold_transition_sequence_item import (
    GatingBeamHoldTransitionSequenceItem,
)
from .general_accessory_sequence_item import GeneralAccessorySequenceItem
from .interlock_sequence_item import InterlockSequenceItem
from .primary_fluence_mode_sequence_item import PrimaryFluenceModeSequenceItem
from .radiation_device_configuration_and_commissioning_key_sequence_item import (
    RadiationDeviceConfigurationAndCommissioningKeySequenceItem,
)
from .recorded_block_sequence_item import RecordedBlockSequenceItem
from .recorded_compensator_sequence_item import RecordedCompensatorSequenceItem
from .recorded_wedge_sequence_item import RecordedWedgeSequenceItem
from .referenced_bolus_sequence_item import ReferencedBolusSequenceItem
from .referenced_calculated_dose_reference_sequence_item import (
    ReferencedCalculatedDoseReferenceSequenceItem,
)
from .referenced_measured_dose_reference_sequence_item import (
    ReferencedMeasuredDoseReferenceSequenceItem,
)
from .referenced_verification_image_sequence_item import (
    ReferencedVerificationImageSequenceItem,
)


class TreatmentSessionBeamSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._DefinitionSourceSequence: List[DefinitionSourceSequenceItem] = []
        self._PrimaryFluenceModeSequence: List[PrimaryFluenceModeSequenceItem] = []
        self._ControlPointDeliverySequence: List[ControlPointDeliverySequenceItem] = []
        self._ReferencedMeasuredDoseReferenceSequence: List[ReferencedMeasuredDoseReferenceSequenceItem] = []
        self._ReferencedCalculatedDoseReferenceSequence: List[ReferencedCalculatedDoseReferenceSequenceItem] = []
        self._BeamLimitingDeviceLeafPairsSequence: List[BeamLimitingDeviceLeafPairsSequenceItem] = []
        self._EnhancedRTBeamLimitingDeviceSequence: List[EnhancedRTBeamLimitingDeviceSequenceItem] = []
        self._RecordedWedgeSequence: List[RecordedWedgeSequenceItem] = []
        self._RecordedCompensatorSequence: List[RecordedCompensatorSequenceItem] = []
        self._RecordedBlockSequence: List[RecordedBlockSequenceItem] = []
        self._ApplicatorSequence: List[ApplicatorSequenceItem] = []
        self._GeneralAccessorySequence: List[GeneralAccessorySequenceItem] = []
        self._RadiationDeviceConfigurationAndCommissioningKeySequence: List[
            RadiationDeviceConfigurationAndCommissioningKeySequenceItem
        ] = []
        self._RTTreatmentTerminationReasonCodeSequence: List[CodeSequenceItem] = []
        self._MachineSpecificTreatmentTerminationCodeSequence: List[CodeSequenceItem] = []
        self._InterlockSequence: List[InterlockSequenceItem] = []
        self._ReferencedVerificationImageSequence: List[ReferencedVerificationImageSequenceItem] = []
        self._ReferencedBolusSequence: List[ReferencedBolusSequenceItem] = []
        self._DoseCalibrationConditionsSequence: List[DoseCalibrationConditionsSequenceItem] = []
        self._GatingBeamHoldTransitionSequence: List[GatingBeamHoldTransitionSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def DefinitionSourceSequence(self) -> Optional[List[DefinitionSourceSequenceItem]]:
        if "DefinitionSourceSequence" in self._dataset:
            if len(self._DefinitionSourceSequence) == len(self._dataset.DefinitionSourceSequence):
                return self._DefinitionSourceSequence
            else:
                return [DefinitionSourceSequenceItem(x) for x in self._dataset.DefinitionSourceSequence]
        return None

    @DefinitionSourceSequence.setter
    def DefinitionSourceSequence(self, value: Optional[List[DefinitionSourceSequenceItem]]):
        if value is None:
            self._DefinitionSourceSequence = []
            if "DefinitionSourceSequence" in self._dataset:
                del self._dataset.DefinitionSourceSequence
        elif not isinstance(value, list) or not all(isinstance(item, DefinitionSourceSequenceItem) for item in value):
            raise ValueError("DefinitionSourceSequence must be a list of DefinitionSourceSequenceItem objects")
        else:
            self._DefinitionSourceSequence = value
            if "DefinitionSourceSequence" not in self._dataset:
                self._dataset.DefinitionSourceSequence = pydicom.Sequence()
            self._dataset.DefinitionSourceSequence.clear()
            self._dataset.DefinitionSourceSequence.extend([item.to_dataset() for item in value])

    def add_DefinitionSource(self, item: DefinitionSourceSequenceItem):
        if not isinstance(item, DefinitionSourceSequenceItem):
            raise ValueError("Item must be an instance of DefinitionSourceSequenceItem")
        self._DefinitionSourceSequence.append(item)
        if "DefinitionSourceSequence" not in self._dataset:
            self._dataset.DefinitionSourceSequence = pydicom.Sequence()
        self._dataset.DefinitionSourceSequence.append(item.to_dataset())

    @property
    def PrimaryFluenceModeSequence(self) -> Optional[List[PrimaryFluenceModeSequenceItem]]:
        if "PrimaryFluenceModeSequence" in self._dataset:
            if len(self._PrimaryFluenceModeSequence) == len(self._dataset.PrimaryFluenceModeSequence):
                return self._PrimaryFluenceModeSequence
            else:
                return [PrimaryFluenceModeSequenceItem(x) for x in self._dataset.PrimaryFluenceModeSequence]
        return None

    @PrimaryFluenceModeSequence.setter
    def PrimaryFluenceModeSequence(self, value: Optional[List[PrimaryFluenceModeSequenceItem]]):
        if value is None:
            self._PrimaryFluenceModeSequence = []
            if "PrimaryFluenceModeSequence" in self._dataset:
                del self._dataset.PrimaryFluenceModeSequence
        elif not isinstance(value, list) or not all(isinstance(item, PrimaryFluenceModeSequenceItem) for item in value):
            raise ValueError("PrimaryFluenceModeSequence must be a list of PrimaryFluenceModeSequenceItem objects")
        else:
            self._PrimaryFluenceModeSequence = value
            if "PrimaryFluenceModeSequence" not in self._dataset:
                self._dataset.PrimaryFluenceModeSequence = pydicom.Sequence()
            self._dataset.PrimaryFluenceModeSequence.clear()
            self._dataset.PrimaryFluenceModeSequence.extend([item.to_dataset() for item in value])

    def add_PrimaryFluenceMode(self, item: PrimaryFluenceModeSequenceItem):
        if not isinstance(item, PrimaryFluenceModeSequenceItem):
            raise ValueError("Item must be an instance of PrimaryFluenceModeSequenceItem")
        self._PrimaryFluenceModeSequence.append(item)
        if "PrimaryFluenceModeSequence" not in self._dataset:
            self._dataset.PrimaryFluenceModeSequence = pydicom.Sequence()
        self._dataset.PrimaryFluenceModeSequence.append(item.to_dataset())

    @property
    def CurrentFractionNumber(self) -> Optional[int]:
        if "CurrentFractionNumber" in self._dataset:
            return self._dataset.CurrentFractionNumber
        return None

    @CurrentFractionNumber.setter
    def CurrentFractionNumber(self, value: Optional[int]):
        if value is None:
            if "CurrentFractionNumber" in self._dataset:
                del self._dataset.CurrentFractionNumber
        else:
            self._dataset.CurrentFractionNumber = value

    @property
    def TreatmentTerminationStatus(self) -> Optional[str]:
        if "TreatmentTerminationStatus" in self._dataset:
            return self._dataset.TreatmentTerminationStatus
        return None

    @TreatmentTerminationStatus.setter
    def TreatmentTerminationStatus(self, value: Optional[str]):
        if value is None:
            if "TreatmentTerminationStatus" in self._dataset:
                del self._dataset.TreatmentTerminationStatus
        else:
            self._dataset.TreatmentTerminationStatus = value

    @property
    def TreatmentVerificationStatus(self) -> Optional[str]:
        if "TreatmentVerificationStatus" in self._dataset:
            return self._dataset.TreatmentVerificationStatus
        return None

    @TreatmentVerificationStatus.setter
    def TreatmentVerificationStatus(self, value: Optional[str]):
        if value is None:
            if "TreatmentVerificationStatus" in self._dataset:
                del self._dataset.TreatmentVerificationStatus
        else:
            self._dataset.TreatmentVerificationStatus = value

    @property
    def SpecifiedPrimaryMeterset(self) -> Optional[Decimal]:
        if "SpecifiedPrimaryMeterset" in self._dataset:
            return self._dataset.SpecifiedPrimaryMeterset
        return None

    @SpecifiedPrimaryMeterset.setter
    def SpecifiedPrimaryMeterset(self, value: Optional[Decimal]):
        if value is None:
            if "SpecifiedPrimaryMeterset" in self._dataset:
                del self._dataset.SpecifiedPrimaryMeterset
        else:
            self._dataset.SpecifiedPrimaryMeterset = value

    @property
    def SpecifiedSecondaryMeterset(self) -> Optional[Decimal]:
        if "SpecifiedSecondaryMeterset" in self._dataset:
            return self._dataset.SpecifiedSecondaryMeterset
        return None

    @SpecifiedSecondaryMeterset.setter
    def SpecifiedSecondaryMeterset(self, value: Optional[Decimal]):
        if value is None:
            if "SpecifiedSecondaryMeterset" in self._dataset:
                del self._dataset.SpecifiedSecondaryMeterset
        else:
            self._dataset.SpecifiedSecondaryMeterset = value

    @property
    def DeliveredPrimaryMeterset(self) -> Optional[Decimal]:
        if "DeliveredPrimaryMeterset" in self._dataset:
            return self._dataset.DeliveredPrimaryMeterset
        return None

    @DeliveredPrimaryMeterset.setter
    def DeliveredPrimaryMeterset(self, value: Optional[Decimal]):
        if value is None:
            if "DeliveredPrimaryMeterset" in self._dataset:
                del self._dataset.DeliveredPrimaryMeterset
        else:
            self._dataset.DeliveredPrimaryMeterset = value

    @property
    def DeliveredSecondaryMeterset(self) -> Optional[Decimal]:
        if "DeliveredSecondaryMeterset" in self._dataset:
            return self._dataset.DeliveredSecondaryMeterset
        return None

    @DeliveredSecondaryMeterset.setter
    def DeliveredSecondaryMeterset(self, value: Optional[Decimal]):
        if value is None:
            if "DeliveredSecondaryMeterset" in self._dataset:
                del self._dataset.DeliveredSecondaryMeterset
        else:
            self._dataset.DeliveredSecondaryMeterset = value

    @property
    def SpecifiedTreatmentTime(self) -> Optional[Decimal]:
        if "SpecifiedTreatmentTime" in self._dataset:
            return self._dataset.SpecifiedTreatmentTime
        return None

    @SpecifiedTreatmentTime.setter
    def SpecifiedTreatmentTime(self, value: Optional[Decimal]):
        if value is None:
            if "SpecifiedTreatmentTime" in self._dataset:
                del self._dataset.SpecifiedTreatmentTime
        else:
            self._dataset.SpecifiedTreatmentTime = value

    @property
    def DeliveredTreatmentTime(self) -> Optional[Decimal]:
        if "DeliveredTreatmentTime" in self._dataset:
            return self._dataset.DeliveredTreatmentTime
        return None

    @DeliveredTreatmentTime.setter
    def DeliveredTreatmentTime(self, value: Optional[Decimal]):
        if value is None:
            if "DeliveredTreatmentTime" in self._dataset:
                del self._dataset.DeliveredTreatmentTime
        else:
            self._dataset.DeliveredTreatmentTime = value

    @property
    def ControlPointDeliverySequence(self) -> Optional[List[ControlPointDeliverySequenceItem]]:
        if "ControlPointDeliverySequence" in self._dataset:
            if len(self._ControlPointDeliverySequence) == len(self._dataset.ControlPointDeliverySequence):
                return self._ControlPointDeliverySequence
            else:
                return [ControlPointDeliverySequenceItem(x) for x in self._dataset.ControlPointDeliverySequence]
        return None

    @ControlPointDeliverySequence.setter
    def ControlPointDeliverySequence(self, value: Optional[List[ControlPointDeliverySequenceItem]]):
        if value is None:
            self._ControlPointDeliverySequence = []
            if "ControlPointDeliverySequence" in self._dataset:
                del self._dataset.ControlPointDeliverySequence
        elif not isinstance(value, list) or not all(isinstance(item, ControlPointDeliverySequenceItem) for item in value):
            raise ValueError("ControlPointDeliverySequence must be a list of ControlPointDeliverySequenceItem objects")
        else:
            self._ControlPointDeliverySequence = value
            if "ControlPointDeliverySequence" not in self._dataset:
                self._dataset.ControlPointDeliverySequence = pydicom.Sequence()
            self._dataset.ControlPointDeliverySequence.clear()
            self._dataset.ControlPointDeliverySequence.extend([item.to_dataset() for item in value])

    def add_ControlPointDelivery(self, item: ControlPointDeliverySequenceItem):
        if not isinstance(item, ControlPointDeliverySequenceItem):
            raise ValueError("Item must be an instance of ControlPointDeliverySequenceItem")
        self._ControlPointDeliverySequence.append(item)
        if "ControlPointDeliverySequence" not in self._dataset:
            self._dataset.ControlPointDeliverySequence = pydicom.Sequence()
        self._dataset.ControlPointDeliverySequence.append(item.to_dataset())

    @property
    def ReferencedMeasuredDoseReferenceSequence(self) -> Optional[List[ReferencedMeasuredDoseReferenceSequenceItem]]:
        if "ReferencedMeasuredDoseReferenceSequence" in self._dataset:
            if len(self._ReferencedMeasuredDoseReferenceSequence) == len(
                self._dataset.ReferencedMeasuredDoseReferenceSequence
            ):
                return self._ReferencedMeasuredDoseReferenceSequence
            else:
                return [
                    ReferencedMeasuredDoseReferenceSequenceItem(x)
                    for x in self._dataset.ReferencedMeasuredDoseReferenceSequence
                ]
        return None

    @ReferencedMeasuredDoseReferenceSequence.setter
    def ReferencedMeasuredDoseReferenceSequence(self, value: Optional[List[ReferencedMeasuredDoseReferenceSequenceItem]]):
        if value is None:
            self._ReferencedMeasuredDoseReferenceSequence = []
            if "ReferencedMeasuredDoseReferenceSequence" in self._dataset:
                del self._dataset.ReferencedMeasuredDoseReferenceSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, ReferencedMeasuredDoseReferenceSequenceItem) for item in value
        ):
            raise ValueError(
                "ReferencedMeasuredDoseReferenceSequence must be a list of ReferencedMeasuredDoseReferenceSequenceItem objects"
            )
        else:
            self._ReferencedMeasuredDoseReferenceSequence = value
            if "ReferencedMeasuredDoseReferenceSequence" not in self._dataset:
                self._dataset.ReferencedMeasuredDoseReferenceSequence = pydicom.Sequence()
            self._dataset.ReferencedMeasuredDoseReferenceSequence.clear()
            self._dataset.ReferencedMeasuredDoseReferenceSequence.extend([item.to_dataset() for item in value])

    def add_ReferencedMeasuredDoseReference(self, item: ReferencedMeasuredDoseReferenceSequenceItem):
        if not isinstance(item, ReferencedMeasuredDoseReferenceSequenceItem):
            raise ValueError("Item must be an instance of ReferencedMeasuredDoseReferenceSequenceItem")
        self._ReferencedMeasuredDoseReferenceSequence.append(item)
        if "ReferencedMeasuredDoseReferenceSequence" not in self._dataset:
            self._dataset.ReferencedMeasuredDoseReferenceSequence = pydicom.Sequence()
        self._dataset.ReferencedMeasuredDoseReferenceSequence.append(item.to_dataset())

    @property
    def ReferencedCalculatedDoseReferenceSequence(self) -> Optional[List[ReferencedCalculatedDoseReferenceSequenceItem]]:
        if "ReferencedCalculatedDoseReferenceSequence" in self._dataset:
            if len(self._ReferencedCalculatedDoseReferenceSequence) == len(
                self._dataset.ReferencedCalculatedDoseReferenceSequence
            ):
                return self._ReferencedCalculatedDoseReferenceSequence
            else:
                return [
                    ReferencedCalculatedDoseReferenceSequenceItem(x)
                    for x in self._dataset.ReferencedCalculatedDoseReferenceSequence
                ]
        return None

    @ReferencedCalculatedDoseReferenceSequence.setter
    def ReferencedCalculatedDoseReferenceSequence(self, value: Optional[List[ReferencedCalculatedDoseReferenceSequenceItem]]):
        if value is None:
            self._ReferencedCalculatedDoseReferenceSequence = []
            if "ReferencedCalculatedDoseReferenceSequence" in self._dataset:
                del self._dataset.ReferencedCalculatedDoseReferenceSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, ReferencedCalculatedDoseReferenceSequenceItem) for item in value
        ):
            raise ValueError(
                "ReferencedCalculatedDoseReferenceSequence must be a list of ReferencedCalculatedDoseReferenceSequenceItem"
                " objects"
            )
        else:
            self._ReferencedCalculatedDoseReferenceSequence = value
            if "ReferencedCalculatedDoseReferenceSequence" not in self._dataset:
                self._dataset.ReferencedCalculatedDoseReferenceSequence = pydicom.Sequence()
            self._dataset.ReferencedCalculatedDoseReferenceSequence.clear()
            self._dataset.ReferencedCalculatedDoseReferenceSequence.extend([item.to_dataset() for item in value])

    def add_ReferencedCalculatedDoseReference(self, item: ReferencedCalculatedDoseReferenceSequenceItem):
        if not isinstance(item, ReferencedCalculatedDoseReferenceSequenceItem):
            raise ValueError("Item must be an instance of ReferencedCalculatedDoseReferenceSequenceItem")
        self._ReferencedCalculatedDoseReferenceSequence.append(item)
        if "ReferencedCalculatedDoseReferenceSequence" not in self._dataset:
            self._dataset.ReferencedCalculatedDoseReferenceSequence = pydicom.Sequence()
        self._dataset.ReferencedCalculatedDoseReferenceSequence.append(item.to_dataset())

    @property
    def BeamLimitingDeviceLeafPairsSequence(self) -> Optional[List[BeamLimitingDeviceLeafPairsSequenceItem]]:
        if "BeamLimitingDeviceLeafPairsSequence" in self._dataset:
            if len(self._BeamLimitingDeviceLeafPairsSequence) == len(self._dataset.BeamLimitingDeviceLeafPairsSequence):
                return self._BeamLimitingDeviceLeafPairsSequence
            else:
                return [BeamLimitingDeviceLeafPairsSequenceItem(x) for x in self._dataset.BeamLimitingDeviceLeafPairsSequence]
        return None

    @BeamLimitingDeviceLeafPairsSequence.setter
    def BeamLimitingDeviceLeafPairsSequence(self, value: Optional[List[BeamLimitingDeviceLeafPairsSequenceItem]]):
        if value is None:
            self._BeamLimitingDeviceLeafPairsSequence = []
            if "BeamLimitingDeviceLeafPairsSequence" in self._dataset:
                del self._dataset.BeamLimitingDeviceLeafPairsSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, BeamLimitingDeviceLeafPairsSequenceItem) for item in value
        ):
            raise ValueError(
                "BeamLimitingDeviceLeafPairsSequence must be a list of BeamLimitingDeviceLeafPairsSequenceItem objects"
            )
        else:
            self._BeamLimitingDeviceLeafPairsSequence = value
            if "BeamLimitingDeviceLeafPairsSequence" not in self._dataset:
                self._dataset.BeamLimitingDeviceLeafPairsSequence = pydicom.Sequence()
            self._dataset.BeamLimitingDeviceLeafPairsSequence.clear()
            self._dataset.BeamLimitingDeviceLeafPairsSequence.extend([item.to_dataset() for item in value])

    def add_BeamLimitingDeviceLeafPairs(self, item: BeamLimitingDeviceLeafPairsSequenceItem):
        if not isinstance(item, BeamLimitingDeviceLeafPairsSequenceItem):
            raise ValueError("Item must be an instance of BeamLimitingDeviceLeafPairsSequenceItem")
        self._BeamLimitingDeviceLeafPairsSequence.append(item)
        if "BeamLimitingDeviceLeafPairsSequence" not in self._dataset:
            self._dataset.BeamLimitingDeviceLeafPairsSequence = pydicom.Sequence()
        self._dataset.BeamLimitingDeviceLeafPairsSequence.append(item.to_dataset())

    @property
    def EnhancedRTBeamLimitingDeviceSequence(self) -> Optional[List[EnhancedRTBeamLimitingDeviceSequenceItem]]:
        if "EnhancedRTBeamLimitingDeviceSequence" in self._dataset:
            if len(self._EnhancedRTBeamLimitingDeviceSequence) == len(self._dataset.EnhancedRTBeamLimitingDeviceSequence):
                return self._EnhancedRTBeamLimitingDeviceSequence
            else:
                return [
                    EnhancedRTBeamLimitingDeviceSequenceItem(x) for x in self._dataset.EnhancedRTBeamLimitingDeviceSequence
                ]
        return None

    @EnhancedRTBeamLimitingDeviceSequence.setter
    def EnhancedRTBeamLimitingDeviceSequence(self, value: Optional[List[EnhancedRTBeamLimitingDeviceSequenceItem]]):
        if value is None:
            self._EnhancedRTBeamLimitingDeviceSequence = []
            if "EnhancedRTBeamLimitingDeviceSequence" in self._dataset:
                del self._dataset.EnhancedRTBeamLimitingDeviceSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, EnhancedRTBeamLimitingDeviceSequenceItem) for item in value
        ):
            raise ValueError(
                "EnhancedRTBeamLimitingDeviceSequence must be a list of EnhancedRTBeamLimitingDeviceSequenceItem objects"
            )
        else:
            self._EnhancedRTBeamLimitingDeviceSequence = value
            if "EnhancedRTBeamLimitingDeviceSequence" not in self._dataset:
                self._dataset.EnhancedRTBeamLimitingDeviceSequence = pydicom.Sequence()
            self._dataset.EnhancedRTBeamLimitingDeviceSequence.clear()
            self._dataset.EnhancedRTBeamLimitingDeviceSequence.extend([item.to_dataset() for item in value])

    def add_EnhancedRTBeamLimitingDevice(self, item: EnhancedRTBeamLimitingDeviceSequenceItem):
        if not isinstance(item, EnhancedRTBeamLimitingDeviceSequenceItem):
            raise ValueError("Item must be an instance of EnhancedRTBeamLimitingDeviceSequenceItem")
        self._EnhancedRTBeamLimitingDeviceSequence.append(item)
        if "EnhancedRTBeamLimitingDeviceSequence" not in self._dataset:
            self._dataset.EnhancedRTBeamLimitingDeviceSequence = pydicom.Sequence()
        self._dataset.EnhancedRTBeamLimitingDeviceSequence.append(item.to_dataset())

    @property
    def EnhancedRTBeamLimitingDeviceDefinitionFlag(self) -> Optional[str]:
        if "EnhancedRTBeamLimitingDeviceDefinitionFlag" in self._dataset:
            return self._dataset.EnhancedRTBeamLimitingDeviceDefinitionFlag
        return None

    @EnhancedRTBeamLimitingDeviceDefinitionFlag.setter
    def EnhancedRTBeamLimitingDeviceDefinitionFlag(self, value: Optional[str]):
        if value is None:
            if "EnhancedRTBeamLimitingDeviceDefinitionFlag" in self._dataset:
                del self._dataset.EnhancedRTBeamLimitingDeviceDefinitionFlag
        else:
            self._dataset.EnhancedRTBeamLimitingDeviceDefinitionFlag = value

    @property
    def RecordedWedgeSequence(self) -> Optional[List[RecordedWedgeSequenceItem]]:
        if "RecordedWedgeSequence" in self._dataset:
            if len(self._RecordedWedgeSequence) == len(self._dataset.RecordedWedgeSequence):
                return self._RecordedWedgeSequence
            else:
                return [RecordedWedgeSequenceItem(x) for x in self._dataset.RecordedWedgeSequence]
        return None

    @RecordedWedgeSequence.setter
    def RecordedWedgeSequence(self, value: Optional[List[RecordedWedgeSequenceItem]]):
        if value is None:
            self._RecordedWedgeSequence = []
            if "RecordedWedgeSequence" in self._dataset:
                del self._dataset.RecordedWedgeSequence
        elif not isinstance(value, list) or not all(isinstance(item, RecordedWedgeSequenceItem) for item in value):
            raise ValueError("RecordedWedgeSequence must be a list of RecordedWedgeSequenceItem objects")
        else:
            self._RecordedWedgeSequence = value
            if "RecordedWedgeSequence" not in self._dataset:
                self._dataset.RecordedWedgeSequence = pydicom.Sequence()
            self._dataset.RecordedWedgeSequence.clear()
            self._dataset.RecordedWedgeSequence.extend([item.to_dataset() for item in value])

    def add_RecordedWedge(self, item: RecordedWedgeSequenceItem):
        if not isinstance(item, RecordedWedgeSequenceItem):
            raise ValueError("Item must be an instance of RecordedWedgeSequenceItem")
        self._RecordedWedgeSequence.append(item)
        if "RecordedWedgeSequence" not in self._dataset:
            self._dataset.RecordedWedgeSequence = pydicom.Sequence()
        self._dataset.RecordedWedgeSequence.append(item.to_dataset())

    @property
    def RecordedCompensatorSequence(self) -> Optional[List[RecordedCompensatorSequenceItem]]:
        if "RecordedCompensatorSequence" in self._dataset:
            if len(self._RecordedCompensatorSequence) == len(self._dataset.RecordedCompensatorSequence):
                return self._RecordedCompensatorSequence
            else:
                return [RecordedCompensatorSequenceItem(x) for x in self._dataset.RecordedCompensatorSequence]
        return None

    @RecordedCompensatorSequence.setter
    def RecordedCompensatorSequence(self, value: Optional[List[RecordedCompensatorSequenceItem]]):
        if value is None:
            self._RecordedCompensatorSequence = []
            if "RecordedCompensatorSequence" in self._dataset:
                del self._dataset.RecordedCompensatorSequence
        elif not isinstance(value, list) or not all(isinstance(item, RecordedCompensatorSequenceItem) for item in value):
            raise ValueError("RecordedCompensatorSequence must be a list of RecordedCompensatorSequenceItem objects")
        else:
            self._RecordedCompensatorSequence = value
            if "RecordedCompensatorSequence" not in self._dataset:
                self._dataset.RecordedCompensatorSequence = pydicom.Sequence()
            self._dataset.RecordedCompensatorSequence.clear()
            self._dataset.RecordedCompensatorSequence.extend([item.to_dataset() for item in value])

    def add_RecordedCompensator(self, item: RecordedCompensatorSequenceItem):
        if not isinstance(item, RecordedCompensatorSequenceItem):
            raise ValueError("Item must be an instance of RecordedCompensatorSequenceItem")
        self._RecordedCompensatorSequence.append(item)
        if "RecordedCompensatorSequence" not in self._dataset:
            self._dataset.RecordedCompensatorSequence = pydicom.Sequence()
        self._dataset.RecordedCompensatorSequence.append(item.to_dataset())

    @property
    def RecordedBlockSequence(self) -> Optional[List[RecordedBlockSequenceItem]]:
        if "RecordedBlockSequence" in self._dataset:
            if len(self._RecordedBlockSequence) == len(self._dataset.RecordedBlockSequence):
                return self._RecordedBlockSequence
            else:
                return [RecordedBlockSequenceItem(x) for x in self._dataset.RecordedBlockSequence]
        return None

    @RecordedBlockSequence.setter
    def RecordedBlockSequence(self, value: Optional[List[RecordedBlockSequenceItem]]):
        if value is None:
            self._RecordedBlockSequence = []
            if "RecordedBlockSequence" in self._dataset:
                del self._dataset.RecordedBlockSequence
        elif not isinstance(value, list) or not all(isinstance(item, RecordedBlockSequenceItem) for item in value):
            raise ValueError("RecordedBlockSequence must be a list of RecordedBlockSequenceItem objects")
        else:
            self._RecordedBlockSequence = value
            if "RecordedBlockSequence" not in self._dataset:
                self._dataset.RecordedBlockSequence = pydicom.Sequence()
            self._dataset.RecordedBlockSequence.clear()
            self._dataset.RecordedBlockSequence.extend([item.to_dataset() for item in value])

    def add_RecordedBlock(self, item: RecordedBlockSequenceItem):
        if not isinstance(item, RecordedBlockSequenceItem):
            raise ValueError("Item must be an instance of RecordedBlockSequenceItem")
        self._RecordedBlockSequence.append(item)
        if "RecordedBlockSequence" not in self._dataset:
            self._dataset.RecordedBlockSequence = pydicom.Sequence()
        self._dataset.RecordedBlockSequence.append(item.to_dataset())

    @property
    def SourceAxisDistance(self) -> Optional[Decimal]:
        if "SourceAxisDistance" in self._dataset:
            return self._dataset.SourceAxisDistance
        return None

    @SourceAxisDistance.setter
    def SourceAxisDistance(self, value: Optional[Decimal]):
        if value is None:
            if "SourceAxisDistance" in self._dataset:
                del self._dataset.SourceAxisDistance
        else:
            self._dataset.SourceAxisDistance = value

    @property
    def BeamName(self) -> Optional[str]:
        if "BeamName" in self._dataset:
            return self._dataset.BeamName
        return None

    @BeamName.setter
    def BeamName(self, value: Optional[str]):
        if value is None:
            if "BeamName" in self._dataset:
                del self._dataset.BeamName
        else:
            self._dataset.BeamName = value

    @property
    def BeamDescription(self) -> Optional[str]:
        if "BeamDescription" in self._dataset:
            return self._dataset.BeamDescription
        return None

    @BeamDescription.setter
    def BeamDescription(self, value: Optional[str]):
        if value is None:
            if "BeamDescription" in self._dataset:
                del self._dataset.BeamDescription
        else:
            self._dataset.BeamDescription = value

    @property
    def BeamType(self) -> Optional[str]:
        if "BeamType" in self._dataset:
            return self._dataset.BeamType
        return None

    @BeamType.setter
    def BeamType(self, value: Optional[str]):
        if value is None:
            if "BeamType" in self._dataset:
                del self._dataset.BeamType
        else:
            self._dataset.BeamType = value

    @property
    def RadiationType(self) -> Optional[str]:
        if "RadiationType" in self._dataset:
            return self._dataset.RadiationType
        return None

    @RadiationType.setter
    def RadiationType(self, value: Optional[str]):
        if value is None:
            if "RadiationType" in self._dataset:
                del self._dataset.RadiationType
        else:
            self._dataset.RadiationType = value

    @property
    def HighDoseTechniqueType(self) -> Optional[str]:
        if "HighDoseTechniqueType" in self._dataset:
            return self._dataset.HighDoseTechniqueType
        return None

    @HighDoseTechniqueType.setter
    def HighDoseTechniqueType(self, value: Optional[str]):
        if value is None:
            if "HighDoseTechniqueType" in self._dataset:
                del self._dataset.HighDoseTechniqueType
        else:
            self._dataset.HighDoseTechniqueType = value

    @property
    def TreatmentDeliveryType(self) -> Optional[str]:
        if "TreatmentDeliveryType" in self._dataset:
            return self._dataset.TreatmentDeliveryType
        return None

    @TreatmentDeliveryType.setter
    def TreatmentDeliveryType(self, value: Optional[str]):
        if value is None:
            if "TreatmentDeliveryType" in self._dataset:
                del self._dataset.TreatmentDeliveryType
        else:
            self._dataset.TreatmentDeliveryType = value

    @property
    def NumberOfWedges(self) -> Optional[int]:
        if "NumberOfWedges" in self._dataset:
            return self._dataset.NumberOfWedges
        return None

    @NumberOfWedges.setter
    def NumberOfWedges(self, value: Optional[int]):
        if value is None:
            if "NumberOfWedges" in self._dataset:
                del self._dataset.NumberOfWedges
        else:
            self._dataset.NumberOfWedges = value

    @property
    def NumberOfCompensators(self) -> Optional[int]:
        if "NumberOfCompensators" in self._dataset:
            return self._dataset.NumberOfCompensators
        return None

    @NumberOfCompensators.setter
    def NumberOfCompensators(self, value: Optional[int]):
        if value is None:
            if "NumberOfCompensators" in self._dataset:
                del self._dataset.NumberOfCompensators
        else:
            self._dataset.NumberOfCompensators = value

    @property
    def NumberOfBoli(self) -> Optional[int]:
        if "NumberOfBoli" in self._dataset:
            return self._dataset.NumberOfBoli
        return None

    @NumberOfBoli.setter
    def NumberOfBoli(self, value: Optional[int]):
        if value is None:
            if "NumberOfBoli" in self._dataset:
                del self._dataset.NumberOfBoli
        else:
            self._dataset.NumberOfBoli = value

    @property
    def NumberOfBlocks(self) -> Optional[int]:
        if "NumberOfBlocks" in self._dataset:
            return self._dataset.NumberOfBlocks
        return None

    @NumberOfBlocks.setter
    def NumberOfBlocks(self, value: Optional[int]):
        if value is None:
            if "NumberOfBlocks" in self._dataset:
                del self._dataset.NumberOfBlocks
        else:
            self._dataset.NumberOfBlocks = value

    @property
    def ApplicatorSequence(self) -> Optional[List[ApplicatorSequenceItem]]:
        if "ApplicatorSequence" in self._dataset:
            if len(self._ApplicatorSequence) == len(self._dataset.ApplicatorSequence):
                return self._ApplicatorSequence
            else:
                return [ApplicatorSequenceItem(x) for x in self._dataset.ApplicatorSequence]
        return None

    @ApplicatorSequence.setter
    def ApplicatorSequence(self, value: Optional[List[ApplicatorSequenceItem]]):
        if value is None:
            self._ApplicatorSequence = []
            if "ApplicatorSequence" in self._dataset:
                del self._dataset.ApplicatorSequence
        elif not isinstance(value, list) or not all(isinstance(item, ApplicatorSequenceItem) for item in value):
            raise ValueError("ApplicatorSequence must be a list of ApplicatorSequenceItem objects")
        else:
            self._ApplicatorSequence = value
            if "ApplicatorSequence" not in self._dataset:
                self._dataset.ApplicatorSequence = pydicom.Sequence()
            self._dataset.ApplicatorSequence.clear()
            self._dataset.ApplicatorSequence.extend([item.to_dataset() for item in value])

    def add_Applicator(self, item: ApplicatorSequenceItem):
        if not isinstance(item, ApplicatorSequenceItem):
            raise ValueError("Item must be an instance of ApplicatorSequenceItem")
        self._ApplicatorSequence.append(item)
        if "ApplicatorSequence" not in self._dataset:
            self._dataset.ApplicatorSequence = pydicom.Sequence()
        self._dataset.ApplicatorSequence.append(item.to_dataset())

    @property
    def NumberOfControlPoints(self) -> Optional[int]:
        if "NumberOfControlPoints" in self._dataset:
            return self._dataset.NumberOfControlPoints
        return None

    @NumberOfControlPoints.setter
    def NumberOfControlPoints(self, value: Optional[int]):
        if value is None:
            if "NumberOfControlPoints" in self._dataset:
                del self._dataset.NumberOfControlPoints
        else:
            self._dataset.NumberOfControlPoints = value

    @property
    def GeneralAccessorySequence(self) -> Optional[List[GeneralAccessorySequenceItem]]:
        if "GeneralAccessorySequence" in self._dataset:
            if len(self._GeneralAccessorySequence) == len(self._dataset.GeneralAccessorySequence):
                return self._GeneralAccessorySequence
            else:
                return [GeneralAccessorySequenceItem(x) for x in self._dataset.GeneralAccessorySequence]
        return None

    @GeneralAccessorySequence.setter
    def GeneralAccessorySequence(self, value: Optional[List[GeneralAccessorySequenceItem]]):
        if value is None:
            self._GeneralAccessorySequence = []
            if "GeneralAccessorySequence" in self._dataset:
                del self._dataset.GeneralAccessorySequence
        elif not isinstance(value, list) or not all(isinstance(item, GeneralAccessorySequenceItem) for item in value):
            raise ValueError("GeneralAccessorySequence must be a list of GeneralAccessorySequenceItem objects")
        else:
            self._GeneralAccessorySequence = value
            if "GeneralAccessorySequence" not in self._dataset:
                self._dataset.GeneralAccessorySequence = pydicom.Sequence()
            self._dataset.GeneralAccessorySequence.clear()
            self._dataset.GeneralAccessorySequence.extend([item.to_dataset() for item in value])

    def add_GeneralAccessory(self, item: GeneralAccessorySequenceItem):
        if not isinstance(item, GeneralAccessorySequenceItem):
            raise ValueError("Item must be an instance of GeneralAccessorySequenceItem")
        self._GeneralAccessorySequence.append(item)
        if "GeneralAccessorySequence" not in self._dataset:
            self._dataset.GeneralAccessorySequence = pydicom.Sequence()
        self._dataset.GeneralAccessorySequence.append(item.to_dataset())

    @property
    def RadiationDeviceConfigurationAndCommissioningKeySequence(
        self,
    ) -> Optional[List[RadiationDeviceConfigurationAndCommissioningKeySequenceItem]]:
        if "RadiationDeviceConfigurationAndCommissioningKeySequence" in self._dataset:
            if len(self._RadiationDeviceConfigurationAndCommissioningKeySequence) == len(
                self._dataset.RadiationDeviceConfigurationAndCommissioningKeySequence
            ):
                return self._RadiationDeviceConfigurationAndCommissioningKeySequence
            else:
                return [
                    RadiationDeviceConfigurationAndCommissioningKeySequenceItem(x)
                    for x in self._dataset.RadiationDeviceConfigurationAndCommissioningKeySequence
                ]
        return None

    @RadiationDeviceConfigurationAndCommissioningKeySequence.setter
    def RadiationDeviceConfigurationAndCommissioningKeySequence(
        self, value: Optional[List[RadiationDeviceConfigurationAndCommissioningKeySequenceItem]]
    ):
        if value is None:
            self._RadiationDeviceConfigurationAndCommissioningKeySequence = []
            if "RadiationDeviceConfigurationAndCommissioningKeySequence" in self._dataset:
                del self._dataset.RadiationDeviceConfigurationAndCommissioningKeySequence
        elif not isinstance(value, list) or not all(
            isinstance(item, RadiationDeviceConfigurationAndCommissioningKeySequenceItem) for item in value
        ):
            raise ValueError(
                "RadiationDeviceConfigurationAndCommissioningKeySequence must be a list of"
                " RadiationDeviceConfigurationAndCommissioningKeySequenceItem objects"
            )
        else:
            self._RadiationDeviceConfigurationAndCommissioningKeySequence = value
            if "RadiationDeviceConfigurationAndCommissioningKeySequence" not in self._dataset:
                self._dataset.RadiationDeviceConfigurationAndCommissioningKeySequence = pydicom.Sequence()
            self._dataset.RadiationDeviceConfigurationAndCommissioningKeySequence.clear()
            self._dataset.RadiationDeviceConfigurationAndCommissioningKeySequence.extend([item.to_dataset() for item in value])

    def add_RadiationDeviceConfigurationAndCommissioningKey(
        self, item: RadiationDeviceConfigurationAndCommissioningKeySequenceItem
    ):
        if not isinstance(item, RadiationDeviceConfigurationAndCommissioningKeySequenceItem):
            raise ValueError("Item must be an instance of RadiationDeviceConfigurationAndCommissioningKeySequenceItem")
        self._RadiationDeviceConfigurationAndCommissioningKeySequence.append(item)
        if "RadiationDeviceConfigurationAndCommissioningKeySequence" not in self._dataset:
            self._dataset.RadiationDeviceConfigurationAndCommissioningKeySequence = pydicom.Sequence()
        self._dataset.RadiationDeviceConfigurationAndCommissioningKeySequence.append(item.to_dataset())

    @property
    def RTTreatmentTerminationReasonCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "RTTreatmentTerminationReasonCodeSequence" in self._dataset:
            if len(self._RTTreatmentTerminationReasonCodeSequence) == len(
                self._dataset.RTTreatmentTerminationReasonCodeSequence
            ):
                return self._RTTreatmentTerminationReasonCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.RTTreatmentTerminationReasonCodeSequence]
        return None

    @RTTreatmentTerminationReasonCodeSequence.setter
    def RTTreatmentTerminationReasonCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._RTTreatmentTerminationReasonCodeSequence = []
            if "RTTreatmentTerminationReasonCodeSequence" in self._dataset:
                del self._dataset.RTTreatmentTerminationReasonCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("RTTreatmentTerminationReasonCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._RTTreatmentTerminationReasonCodeSequence = value
            if "RTTreatmentTerminationReasonCodeSequence" not in self._dataset:
                self._dataset.RTTreatmentTerminationReasonCodeSequence = pydicom.Sequence()
            self._dataset.RTTreatmentTerminationReasonCodeSequence.clear()
            self._dataset.RTTreatmentTerminationReasonCodeSequence.extend([item.to_dataset() for item in value])

    def add_RTTreatmentTerminationReasonCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._RTTreatmentTerminationReasonCodeSequence.append(item)
        if "RTTreatmentTerminationReasonCodeSequence" not in self._dataset:
            self._dataset.RTTreatmentTerminationReasonCodeSequence = pydicom.Sequence()
        self._dataset.RTTreatmentTerminationReasonCodeSequence.append(item.to_dataset())

    @property
    def MachineSpecificTreatmentTerminationCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "MachineSpecificTreatmentTerminationCodeSequence" in self._dataset:
            if len(self._MachineSpecificTreatmentTerminationCodeSequence) == len(
                self._dataset.MachineSpecificTreatmentTerminationCodeSequence
            ):
                return self._MachineSpecificTreatmentTerminationCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.MachineSpecificTreatmentTerminationCodeSequence]
        return None

    @MachineSpecificTreatmentTerminationCodeSequence.setter
    def MachineSpecificTreatmentTerminationCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._MachineSpecificTreatmentTerminationCodeSequence = []
            if "MachineSpecificTreatmentTerminationCodeSequence" in self._dataset:
                del self._dataset.MachineSpecificTreatmentTerminationCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("MachineSpecificTreatmentTerminationCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._MachineSpecificTreatmentTerminationCodeSequence = value
            if "MachineSpecificTreatmentTerminationCodeSequence" not in self._dataset:
                self._dataset.MachineSpecificTreatmentTerminationCodeSequence = pydicom.Sequence()
            self._dataset.MachineSpecificTreatmentTerminationCodeSequence.clear()
            self._dataset.MachineSpecificTreatmentTerminationCodeSequence.extend([item.to_dataset() for item in value])

    def add_MachineSpecificTreatmentTerminationCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._MachineSpecificTreatmentTerminationCodeSequence.append(item)
        if "MachineSpecificTreatmentTerminationCodeSequence" not in self._dataset:
            self._dataset.MachineSpecificTreatmentTerminationCodeSequence = pydicom.Sequence()
        self._dataset.MachineSpecificTreatmentTerminationCodeSequence.append(item.to_dataset())

    @property
    def TreatmentTerminationDescription(self) -> Optional[str]:
        if "TreatmentTerminationDescription" in self._dataset:
            return self._dataset.TreatmentTerminationDescription
        return None

    @TreatmentTerminationDescription.setter
    def TreatmentTerminationDescription(self, value: Optional[str]):
        if value is None:
            if "TreatmentTerminationDescription" in self._dataset:
                del self._dataset.TreatmentTerminationDescription
        else:
            self._dataset.TreatmentTerminationDescription = value

    @property
    def InterlockSequence(self) -> Optional[List[InterlockSequenceItem]]:
        if "InterlockSequence" in self._dataset:
            if len(self._InterlockSequence) == len(self._dataset.InterlockSequence):
                return self._InterlockSequence
            else:
                return [InterlockSequenceItem(x) for x in self._dataset.InterlockSequence]
        return None

    @InterlockSequence.setter
    def InterlockSequence(self, value: Optional[List[InterlockSequenceItem]]):
        if value is None:
            self._InterlockSequence = []
            if "InterlockSequence" in self._dataset:
                del self._dataset.InterlockSequence
        elif not isinstance(value, list) or not all(isinstance(item, InterlockSequenceItem) for item in value):
            raise ValueError("InterlockSequence must be a list of InterlockSequenceItem objects")
        else:
            self._InterlockSequence = value
            if "InterlockSequence" not in self._dataset:
                self._dataset.InterlockSequence = pydicom.Sequence()
            self._dataset.InterlockSequence.clear()
            self._dataset.InterlockSequence.extend([item.to_dataset() for item in value])

    def add_Interlock(self, item: InterlockSequenceItem):
        if not isinstance(item, InterlockSequenceItem):
            raise ValueError("Item must be an instance of InterlockSequenceItem")
        self._InterlockSequence.append(item)
        if "InterlockSequence" not in self._dataset:
            self._dataset.InterlockSequence = pydicom.Sequence()
        self._dataset.InterlockSequence.append(item.to_dataset())

    @property
    def ReferencedBeamNumber(self) -> Optional[int]:
        if "ReferencedBeamNumber" in self._dataset:
            return self._dataset.ReferencedBeamNumber
        return None

    @ReferencedBeamNumber.setter
    def ReferencedBeamNumber(self, value: Optional[int]):
        if value is None:
            if "ReferencedBeamNumber" in self._dataset:
                del self._dataset.ReferencedBeamNumber
        else:
            self._dataset.ReferencedBeamNumber = value

    @property
    def ReferencedVerificationImageSequence(self) -> Optional[List[ReferencedVerificationImageSequenceItem]]:
        if "ReferencedVerificationImageSequence" in self._dataset:
            if len(self._ReferencedVerificationImageSequence) == len(self._dataset.ReferencedVerificationImageSequence):
                return self._ReferencedVerificationImageSequence
            else:
                return [ReferencedVerificationImageSequenceItem(x) for x in self._dataset.ReferencedVerificationImageSequence]
        return None

    @ReferencedVerificationImageSequence.setter
    def ReferencedVerificationImageSequence(self, value: Optional[List[ReferencedVerificationImageSequenceItem]]):
        if value is None:
            self._ReferencedVerificationImageSequence = []
            if "ReferencedVerificationImageSequence" in self._dataset:
                del self._dataset.ReferencedVerificationImageSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, ReferencedVerificationImageSequenceItem) for item in value
        ):
            raise ValueError(
                "ReferencedVerificationImageSequence must be a list of ReferencedVerificationImageSequenceItem objects"
            )
        else:
            self._ReferencedVerificationImageSequence = value
            if "ReferencedVerificationImageSequence" not in self._dataset:
                self._dataset.ReferencedVerificationImageSequence = pydicom.Sequence()
            self._dataset.ReferencedVerificationImageSequence.clear()
            self._dataset.ReferencedVerificationImageSequence.extend([item.to_dataset() for item in value])

    def add_ReferencedVerificationImage(self, item: ReferencedVerificationImageSequenceItem):
        if not isinstance(item, ReferencedVerificationImageSequenceItem):
            raise ValueError("Item must be an instance of ReferencedVerificationImageSequenceItem")
        self._ReferencedVerificationImageSequence.append(item)
        if "ReferencedVerificationImageSequence" not in self._dataset:
            self._dataset.ReferencedVerificationImageSequence = pydicom.Sequence()
        self._dataset.ReferencedVerificationImageSequence.append(item.to_dataset())

    @property
    def ReferencedPatientSetupNumber(self) -> Optional[int]:
        if "ReferencedPatientSetupNumber" in self._dataset:
            return self._dataset.ReferencedPatientSetupNumber
        return None

    @ReferencedPatientSetupNumber.setter
    def ReferencedPatientSetupNumber(self, value: Optional[int]):
        if value is None:
            if "ReferencedPatientSetupNumber" in self._dataset:
                del self._dataset.ReferencedPatientSetupNumber
        else:
            self._dataset.ReferencedPatientSetupNumber = value

    @property
    def ReferencedBolusSequence(self) -> Optional[List[ReferencedBolusSequenceItem]]:
        if "ReferencedBolusSequence" in self._dataset:
            if len(self._ReferencedBolusSequence) == len(self._dataset.ReferencedBolusSequence):
                return self._ReferencedBolusSequence
            else:
                return [ReferencedBolusSequenceItem(x) for x in self._dataset.ReferencedBolusSequence]
        return None

    @ReferencedBolusSequence.setter
    def ReferencedBolusSequence(self, value: Optional[List[ReferencedBolusSequenceItem]]):
        if value is None:
            self._ReferencedBolusSequence = []
            if "ReferencedBolusSequence" in self._dataset:
                del self._dataset.ReferencedBolusSequence
        elif not isinstance(value, list) or not all(isinstance(item, ReferencedBolusSequenceItem) for item in value):
            raise ValueError("ReferencedBolusSequence must be a list of ReferencedBolusSequenceItem objects")
        else:
            self._ReferencedBolusSequence = value
            if "ReferencedBolusSequence" not in self._dataset:
                self._dataset.ReferencedBolusSequence = pydicom.Sequence()
            self._dataset.ReferencedBolusSequence.clear()
            self._dataset.ReferencedBolusSequence.extend([item.to_dataset() for item in value])

    def add_ReferencedBolus(self, item: ReferencedBolusSequenceItem):
        if not isinstance(item, ReferencedBolusSequenceItem):
            raise ValueError("Item must be an instance of ReferencedBolusSequenceItem")
        self._ReferencedBolusSequence.append(item)
        if "ReferencedBolusSequence" not in self._dataset:
            self._dataset.ReferencedBolusSequence = pydicom.Sequence()
        self._dataset.ReferencedBolusSequence.append(item.to_dataset())

    @property
    def DoseCalibrationConditionsSequence(self) -> Optional[List[DoseCalibrationConditionsSequenceItem]]:
        if "DoseCalibrationConditionsSequence" in self._dataset:
            if len(self._DoseCalibrationConditionsSequence) == len(self._dataset.DoseCalibrationConditionsSequence):
                return self._DoseCalibrationConditionsSequence
            else:
                return [DoseCalibrationConditionsSequenceItem(x) for x in self._dataset.DoseCalibrationConditionsSequence]
        return None

    @DoseCalibrationConditionsSequence.setter
    def DoseCalibrationConditionsSequence(self, value: Optional[List[DoseCalibrationConditionsSequenceItem]]):
        if value is None:
            self._DoseCalibrationConditionsSequence = []
            if "DoseCalibrationConditionsSequence" in self._dataset:
                del self._dataset.DoseCalibrationConditionsSequence
        elif not isinstance(value, list) or not all(isinstance(item, DoseCalibrationConditionsSequenceItem) for item in value):
            raise ValueError(
                "DoseCalibrationConditionsSequence must be a list of DoseCalibrationConditionsSequenceItem objects"
            )
        else:
            self._DoseCalibrationConditionsSequence = value
            if "DoseCalibrationConditionsSequence" not in self._dataset:
                self._dataset.DoseCalibrationConditionsSequence = pydicom.Sequence()
            self._dataset.DoseCalibrationConditionsSequence.clear()
            self._dataset.DoseCalibrationConditionsSequence.extend([item.to_dataset() for item in value])

    def add_DoseCalibrationConditions(self, item: DoseCalibrationConditionsSequenceItem):
        if not isinstance(item, DoseCalibrationConditionsSequenceItem):
            raise ValueError("Item must be an instance of DoseCalibrationConditionsSequenceItem")
        self._DoseCalibrationConditionsSequence.append(item)
        if "DoseCalibrationConditionsSequence" not in self._dataset:
            self._dataset.DoseCalibrationConditionsSequence = pydicom.Sequence()
        self._dataset.DoseCalibrationConditionsSequence.append(item.to_dataset())

    @property
    def DoseCalibrationConditionsVerifiedFlag(self) -> Optional[str]:
        if "DoseCalibrationConditionsVerifiedFlag" in self._dataset:
            return self._dataset.DoseCalibrationConditionsVerifiedFlag
        return None

    @DoseCalibrationConditionsVerifiedFlag.setter
    def DoseCalibrationConditionsVerifiedFlag(self, value: Optional[str]):
        if value is None:
            if "DoseCalibrationConditionsVerifiedFlag" in self._dataset:
                del self._dataset.DoseCalibrationConditionsVerifiedFlag
        else:
            self._dataset.DoseCalibrationConditionsVerifiedFlag = value

    @property
    def GatingBeamHoldTransitionSequence(self) -> Optional[List[GatingBeamHoldTransitionSequenceItem]]:
        if "GatingBeamHoldTransitionSequence" in self._dataset:
            if len(self._GatingBeamHoldTransitionSequence) == len(self._dataset.GatingBeamHoldTransitionSequence):
                return self._GatingBeamHoldTransitionSequence
            else:
                return [GatingBeamHoldTransitionSequenceItem(x) for x in self._dataset.GatingBeamHoldTransitionSequence]
        return None

    @GatingBeamHoldTransitionSequence.setter
    def GatingBeamHoldTransitionSequence(self, value: Optional[List[GatingBeamHoldTransitionSequenceItem]]):
        if value is None:
            self._GatingBeamHoldTransitionSequence = []
            if "GatingBeamHoldTransitionSequence" in self._dataset:
                del self._dataset.GatingBeamHoldTransitionSequence
        elif not isinstance(value, list) or not all(isinstance(item, GatingBeamHoldTransitionSequenceItem) for item in value):
            raise ValueError("GatingBeamHoldTransitionSequence must be a list of GatingBeamHoldTransitionSequenceItem objects")
        else:
            self._GatingBeamHoldTransitionSequence = value
            if "GatingBeamHoldTransitionSequence" not in self._dataset:
                self._dataset.GatingBeamHoldTransitionSequence = pydicom.Sequence()
            self._dataset.GatingBeamHoldTransitionSequence.clear()
            self._dataset.GatingBeamHoldTransitionSequence.extend([item.to_dataset() for item in value])

    def add_GatingBeamHoldTransition(self, item: GatingBeamHoldTransitionSequenceItem):
        if not isinstance(item, GatingBeamHoldTransitionSequenceItem):
            raise ValueError("Item must be an instance of GatingBeamHoldTransitionSequenceItem")
        self._GatingBeamHoldTransitionSequence.append(item)
        if "GatingBeamHoldTransitionSequence" not in self._dataset:
            self._dataset.GatingBeamHoldTransitionSequence = pydicom.Sequence()
        self._dataset.GatingBeamHoldTransitionSequence.append(item.to_dataset())

    @property
    def EntityLongLabel(self) -> Optional[str]:
        if "EntityLongLabel" in self._dataset:
            return self._dataset.EntityLongLabel
        return None

    @EntityLongLabel.setter
    def EntityLongLabel(self, value: Optional[str]):
        if value is None:
            if "EntityLongLabel" in self._dataset:
                del self._dataset.EntityLongLabel
        else:
            self._dataset.EntityLongLabel = value
