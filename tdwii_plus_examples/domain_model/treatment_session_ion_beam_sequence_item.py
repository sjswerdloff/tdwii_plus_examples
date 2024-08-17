from decimal import Decimal
from typing import Any, List, Optional  # noqa

import pydicom

from .applicator_sequence_item import ApplicatorSequenceItem
from .beam_limiting_device_leaf_pairs_sequence_item import (
    BeamLimitingDeviceLeafPairsSequenceItem,
)
from .code_sequence_item import CodeSequenceItem
from .delivered_depth_dose_parameters_sequence_item import (
    DeliveredDepthDoseParametersSequenceItem,
)
from .enhanced_rt_beam_limiting_device_sequence_item import (
    EnhancedRTBeamLimitingDeviceSequenceItem,
)
from .general_accessory_sequence_item import GeneralAccessorySequenceItem
from .interlock_sequence_item import InterlockSequenceItem
from .ion_control_point_delivery_sequence_item import (
    IonControlPointDeliverySequenceItem,
)
from .recorded_block_sequence_item import RecordedBlockSequenceItem
from .recorded_compensator_sequence_item import RecordedCompensatorSequenceItem
from .recorded_lateral_spreading_device_sequence_item import (
    RecordedLateralSpreadingDeviceSequenceItem,
)
from .recorded_range_modulator_sequence_item import RecordedRangeModulatorSequenceItem
from .recorded_range_shifter_sequence_item import RecordedRangeShifterSequenceItem
from .recorded_snout_sequence_item import RecordedSnoutSequenceItem
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


class TreatmentSessionIonBeamSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._IonControlPointDeliverySequence: List[IonControlPointDeliverySequenceItem] = []
        self._ReferencedMeasuredDoseReferenceSequence: List[ReferencedMeasuredDoseReferenceSequenceItem] = []
        self._ReferencedCalculatedDoseReferenceSequence: List[ReferencedCalculatedDoseReferenceSequenceItem] = []
        self._BeamLimitingDeviceLeafPairsSequence: List[BeamLimitingDeviceLeafPairsSequenceItem] = []
        self._EnhancedRTBeamLimitingDeviceSequence: List[EnhancedRTBeamLimitingDeviceSequenceItem] = []
        self._RecordedWedgeSequence: List[RecordedWedgeSequenceItem] = []
        self._RecordedCompensatorSequence: List[RecordedCompensatorSequenceItem] = []
        self._RecordedBlockSequence: List[RecordedBlockSequenceItem] = []
        self._RecordedSnoutSequence: List[RecordedSnoutSequenceItem] = []
        self._RecordedRangeShifterSequence: List[RecordedRangeShifterSequenceItem] = []
        self._RecordedLateralSpreadingDeviceSequence: List[RecordedLateralSpreadingDeviceSequenceItem] = []
        self._RecordedRangeModulatorSequence: List[RecordedRangeModulatorSequenceItem] = []
        self._ApplicatorSequence: List[ApplicatorSequenceItem] = []
        self._GeneralAccessorySequence: List[GeneralAccessorySequenceItem] = []
        self._DeliveredDepthDoseParametersSequence: List[DeliveredDepthDoseParametersSequenceItem] = []
        self._RTTreatmentTerminationReasonCodeSequence: List[CodeSequenceItem] = []
        self._MachineSpecificTreatmentTerminationCodeSequence: List[CodeSequenceItem] = []
        self._InterlockSequence: List[InterlockSequenceItem] = []
        self._ReferencedVerificationImageSequence: List[ReferencedVerificationImageSequenceItem] = []
        self._ReferencedBolusSequence: List[ReferencedBolusSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

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
    def IonControlPointDeliverySequence(self) -> Optional[List[IonControlPointDeliverySequenceItem]]:
        if "IonControlPointDeliverySequence" in self._dataset:
            if len(self._IonControlPointDeliverySequence) == len(self._dataset.IonControlPointDeliverySequence):
                return self._IonControlPointDeliverySequence
            else:
                return [IonControlPointDeliverySequenceItem(x) for x in self._dataset.IonControlPointDeliverySequence]
        return None

    @IonControlPointDeliverySequence.setter
    def IonControlPointDeliverySequence(self, value: Optional[List[IonControlPointDeliverySequenceItem]]):
        if value is None:
            self._IonControlPointDeliverySequence = []
            if "IonControlPointDeliverySequence" in self._dataset:
                del self._dataset.IonControlPointDeliverySequence
        elif not isinstance(value, list) or not all(isinstance(item, IonControlPointDeliverySequenceItem) for item in value):
            raise ValueError("IonControlPointDeliverySequence must be a list of IonControlPointDeliverySequenceItem objects")
        else:
            self._IonControlPointDeliverySequence = value
            if "IonControlPointDeliverySequence" not in self._dataset:
                self._dataset.IonControlPointDeliverySequence = pydicom.Sequence()
            self._dataset.IonControlPointDeliverySequence.clear()
            self._dataset.IonControlPointDeliverySequence.extend([item.to_dataset() for item in value])

    def add_IonControlPointDelivery(self, item: IonControlPointDeliverySequenceItem):
        if not isinstance(item, IonControlPointDeliverySequenceItem):
            raise ValueError("Item must be an instance of IonControlPointDeliverySequenceItem")
        self._IonControlPointDeliverySequence.append(item)
        if "IonControlPointDeliverySequence" not in self._dataset:
            self._dataset.IonControlPointDeliverySequence = pydicom.Sequence()
        self._dataset.IonControlPointDeliverySequence.append(item.to_dataset())

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
    def RecordedSnoutSequence(self) -> Optional[List[RecordedSnoutSequenceItem]]:
        if "RecordedSnoutSequence" in self._dataset:
            if len(self._RecordedSnoutSequence) == len(self._dataset.RecordedSnoutSequence):
                return self._RecordedSnoutSequence
            else:
                return [RecordedSnoutSequenceItem(x) for x in self._dataset.RecordedSnoutSequence]
        return None

    @RecordedSnoutSequence.setter
    def RecordedSnoutSequence(self, value: Optional[List[RecordedSnoutSequenceItem]]):
        if value is None:
            self._RecordedSnoutSequence = []
            if "RecordedSnoutSequence" in self._dataset:
                del self._dataset.RecordedSnoutSequence
        elif not isinstance(value, list) or not all(isinstance(item, RecordedSnoutSequenceItem) for item in value):
            raise ValueError("RecordedSnoutSequence must be a list of RecordedSnoutSequenceItem objects")
        else:
            self._RecordedSnoutSequence = value
            if "RecordedSnoutSequence" not in self._dataset:
                self._dataset.RecordedSnoutSequence = pydicom.Sequence()
            self._dataset.RecordedSnoutSequence.clear()
            self._dataset.RecordedSnoutSequence.extend([item.to_dataset() for item in value])

    def add_RecordedSnout(self, item: RecordedSnoutSequenceItem):
        if not isinstance(item, RecordedSnoutSequenceItem):
            raise ValueError("Item must be an instance of RecordedSnoutSequenceItem")
        self._RecordedSnoutSequence.append(item)
        if "RecordedSnoutSequence" not in self._dataset:
            self._dataset.RecordedSnoutSequence = pydicom.Sequence()
        self._dataset.RecordedSnoutSequence.append(item.to_dataset())

    @property
    def RecordedRangeShifterSequence(self) -> Optional[List[RecordedRangeShifterSequenceItem]]:
        if "RecordedRangeShifterSequence" in self._dataset:
            if len(self._RecordedRangeShifterSequence) == len(self._dataset.RecordedRangeShifterSequence):
                return self._RecordedRangeShifterSequence
            else:
                return [RecordedRangeShifterSequenceItem(x) for x in self._dataset.RecordedRangeShifterSequence]
        return None

    @RecordedRangeShifterSequence.setter
    def RecordedRangeShifterSequence(self, value: Optional[List[RecordedRangeShifterSequenceItem]]):
        if value is None:
            self._RecordedRangeShifterSequence = []
            if "RecordedRangeShifterSequence" in self._dataset:
                del self._dataset.RecordedRangeShifterSequence
        elif not isinstance(value, list) or not all(isinstance(item, RecordedRangeShifterSequenceItem) for item in value):
            raise ValueError("RecordedRangeShifterSequence must be a list of RecordedRangeShifterSequenceItem objects")
        else:
            self._RecordedRangeShifterSequence = value
            if "RecordedRangeShifterSequence" not in self._dataset:
                self._dataset.RecordedRangeShifterSequence = pydicom.Sequence()
            self._dataset.RecordedRangeShifterSequence.clear()
            self._dataset.RecordedRangeShifterSequence.extend([item.to_dataset() for item in value])

    def add_RecordedRangeShifter(self, item: RecordedRangeShifterSequenceItem):
        if not isinstance(item, RecordedRangeShifterSequenceItem):
            raise ValueError("Item must be an instance of RecordedRangeShifterSequenceItem")
        self._RecordedRangeShifterSequence.append(item)
        if "RecordedRangeShifterSequence" not in self._dataset:
            self._dataset.RecordedRangeShifterSequence = pydicom.Sequence()
        self._dataset.RecordedRangeShifterSequence.append(item.to_dataset())

    @property
    def RecordedLateralSpreadingDeviceSequence(self) -> Optional[List[RecordedLateralSpreadingDeviceSequenceItem]]:
        if "RecordedLateralSpreadingDeviceSequence" in self._dataset:
            if len(self._RecordedLateralSpreadingDeviceSequence) == len(self._dataset.RecordedLateralSpreadingDeviceSequence):
                return self._RecordedLateralSpreadingDeviceSequence
            else:
                return [
                    RecordedLateralSpreadingDeviceSequenceItem(x) for x in self._dataset.RecordedLateralSpreadingDeviceSequence
                ]
        return None

    @RecordedLateralSpreadingDeviceSequence.setter
    def RecordedLateralSpreadingDeviceSequence(self, value: Optional[List[RecordedLateralSpreadingDeviceSequenceItem]]):
        if value is None:
            self._RecordedLateralSpreadingDeviceSequence = []
            if "RecordedLateralSpreadingDeviceSequence" in self._dataset:
                del self._dataset.RecordedLateralSpreadingDeviceSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, RecordedLateralSpreadingDeviceSequenceItem) for item in value
        ):
            raise ValueError(
                "RecordedLateralSpreadingDeviceSequence must be a list of RecordedLateralSpreadingDeviceSequenceItem objects"
            )
        else:
            self._RecordedLateralSpreadingDeviceSequence = value
            if "RecordedLateralSpreadingDeviceSequence" not in self._dataset:
                self._dataset.RecordedLateralSpreadingDeviceSequence = pydicom.Sequence()
            self._dataset.RecordedLateralSpreadingDeviceSequence.clear()
            self._dataset.RecordedLateralSpreadingDeviceSequence.extend([item.to_dataset() for item in value])

    def add_RecordedLateralSpreadingDevice(self, item: RecordedLateralSpreadingDeviceSequenceItem):
        if not isinstance(item, RecordedLateralSpreadingDeviceSequenceItem):
            raise ValueError("Item must be an instance of RecordedLateralSpreadingDeviceSequenceItem")
        self._RecordedLateralSpreadingDeviceSequence.append(item)
        if "RecordedLateralSpreadingDeviceSequence" not in self._dataset:
            self._dataset.RecordedLateralSpreadingDeviceSequence = pydicom.Sequence()
        self._dataset.RecordedLateralSpreadingDeviceSequence.append(item.to_dataset())

    @property
    def RecordedRangeModulatorSequence(self) -> Optional[List[RecordedRangeModulatorSequenceItem]]:
        if "RecordedRangeModulatorSequence" in self._dataset:
            if len(self._RecordedRangeModulatorSequence) == len(self._dataset.RecordedRangeModulatorSequence):
                return self._RecordedRangeModulatorSequence
            else:
                return [RecordedRangeModulatorSequenceItem(x) for x in self._dataset.RecordedRangeModulatorSequence]
        return None

    @RecordedRangeModulatorSequence.setter
    def RecordedRangeModulatorSequence(self, value: Optional[List[RecordedRangeModulatorSequenceItem]]):
        if value is None:
            self._RecordedRangeModulatorSequence = []
            if "RecordedRangeModulatorSequence" in self._dataset:
                del self._dataset.RecordedRangeModulatorSequence
        elif not isinstance(value, list) or not all(isinstance(item, RecordedRangeModulatorSequenceItem) for item in value):
            raise ValueError("RecordedRangeModulatorSequence must be a list of RecordedRangeModulatorSequenceItem objects")
        else:
            self._RecordedRangeModulatorSequence = value
            if "RecordedRangeModulatorSequence" not in self._dataset:
                self._dataset.RecordedRangeModulatorSequence = pydicom.Sequence()
            self._dataset.RecordedRangeModulatorSequence.clear()
            self._dataset.RecordedRangeModulatorSequence.extend([item.to_dataset() for item in value])

    def add_RecordedRangeModulator(self, item: RecordedRangeModulatorSequenceItem):
        if not isinstance(item, RecordedRangeModulatorSequenceItem):
            raise ValueError("Item must be an instance of RecordedRangeModulatorSequenceItem")
        self._RecordedRangeModulatorSequence.append(item)
        if "RecordedRangeModulatorSequence" not in self._dataset:
            self._dataset.RecordedRangeModulatorSequence = pydicom.Sequence()
        self._dataset.RecordedRangeModulatorSequence.append(item.to_dataset())

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
    def FixationEye(self) -> Optional[str]:
        if "FixationEye" in self._dataset:
            return self._dataset.FixationEye
        return None

    @FixationEye.setter
    def FixationEye(self, value: Optional[str]):
        if value is None:
            if "FixationEye" in self._dataset:
                del self._dataset.FixationEye
        else:
            self._dataset.FixationEye = value

    @property
    def RadiationMassNumber(self) -> Optional[int]:
        if "RadiationMassNumber" in self._dataset:
            return self._dataset.RadiationMassNumber
        return None

    @RadiationMassNumber.setter
    def RadiationMassNumber(self, value: Optional[int]):
        if value is None:
            if "RadiationMassNumber" in self._dataset:
                del self._dataset.RadiationMassNumber
        else:
            self._dataset.RadiationMassNumber = value

    @property
    def RadiationAtomicNumber(self) -> Optional[int]:
        if "RadiationAtomicNumber" in self._dataset:
            return self._dataset.RadiationAtomicNumber
        return None

    @RadiationAtomicNumber.setter
    def RadiationAtomicNumber(self, value: Optional[int]):
        if value is None:
            if "RadiationAtomicNumber" in self._dataset:
                del self._dataset.RadiationAtomicNumber
        else:
            self._dataset.RadiationAtomicNumber = value

    @property
    def RadiationChargeState(self) -> Optional[int]:
        if "RadiationChargeState" in self._dataset:
            return self._dataset.RadiationChargeState
        return None

    @RadiationChargeState.setter
    def RadiationChargeState(self, value: Optional[int]):
        if value is None:
            if "RadiationChargeState" in self._dataset:
                del self._dataset.RadiationChargeState
        else:
            self._dataset.RadiationChargeState = value

    @property
    def ScanMode(self) -> Optional[str]:
        if "ScanMode" in self._dataset:
            return self._dataset.ScanMode
        return None

    @ScanMode.setter
    def ScanMode(self, value: Optional[str]):
        if value is None:
            if "ScanMode" in self._dataset:
                del self._dataset.ScanMode
        else:
            self._dataset.ScanMode = value

    @property
    def ModulatedScanModeType(self) -> Optional[str]:
        if "ModulatedScanModeType" in self._dataset:
            return self._dataset.ModulatedScanModeType
        return None

    @ModulatedScanModeType.setter
    def ModulatedScanModeType(self, value: Optional[str]):
        if value is None:
            if "ModulatedScanModeType" in self._dataset:
                del self._dataset.ModulatedScanModeType
        else:
            self._dataset.ModulatedScanModeType = value

    @property
    def NumberOfRangeShifters(self) -> Optional[int]:
        if "NumberOfRangeShifters" in self._dataset:
            return self._dataset.NumberOfRangeShifters
        return None

    @NumberOfRangeShifters.setter
    def NumberOfRangeShifters(self, value: Optional[int]):
        if value is None:
            if "NumberOfRangeShifters" in self._dataset:
                del self._dataset.NumberOfRangeShifters
        else:
            self._dataset.NumberOfRangeShifters = value

    @property
    def NumberOfLateralSpreadingDevices(self) -> Optional[int]:
        if "NumberOfLateralSpreadingDevices" in self._dataset:
            return self._dataset.NumberOfLateralSpreadingDevices
        return None

    @NumberOfLateralSpreadingDevices.setter
    def NumberOfLateralSpreadingDevices(self, value: Optional[int]):
        if value is None:
            if "NumberOfLateralSpreadingDevices" in self._dataset:
                del self._dataset.NumberOfLateralSpreadingDevices
        else:
            self._dataset.NumberOfLateralSpreadingDevices = value

    @property
    def NumberOfRangeModulators(self) -> Optional[int]:
        if "NumberOfRangeModulators" in self._dataset:
            return self._dataset.NumberOfRangeModulators
        return None

    @NumberOfRangeModulators.setter
    def NumberOfRangeModulators(self, value: Optional[int]):
        if value is None:
            if "NumberOfRangeModulators" in self._dataset:
                del self._dataset.NumberOfRangeModulators
        else:
            self._dataset.NumberOfRangeModulators = value

    @property
    def PatientSupportType(self) -> Optional[str]:
        if "PatientSupportType" in self._dataset:
            return self._dataset.PatientSupportType
        return None

    @PatientSupportType.setter
    def PatientSupportType(self, value: Optional[str]):
        if value is None:
            if "PatientSupportType" in self._dataset:
                del self._dataset.PatientSupportType
        else:
            self._dataset.PatientSupportType = value

    @property
    def PatientSupportID(self) -> Optional[str]:
        if "PatientSupportID" in self._dataset:
            return self._dataset.PatientSupportID
        return None

    @PatientSupportID.setter
    def PatientSupportID(self, value: Optional[str]):
        if value is None:
            if "PatientSupportID" in self._dataset:
                del self._dataset.PatientSupportID
        else:
            self._dataset.PatientSupportID = value

    @property
    def PatientSupportAccessoryCode(self) -> Optional[str]:
        if "PatientSupportAccessoryCode" in self._dataset:
            return self._dataset.PatientSupportAccessoryCode
        return None

    @PatientSupportAccessoryCode.setter
    def PatientSupportAccessoryCode(self, value: Optional[str]):
        if value is None:
            if "PatientSupportAccessoryCode" in self._dataset:
                del self._dataset.PatientSupportAccessoryCode
        else:
            self._dataset.PatientSupportAccessoryCode = value

    @property
    def FixationLightAzimuthalAngle(self) -> Optional[float]:
        if "FixationLightAzimuthalAngle" in self._dataset:
            return self._dataset.FixationLightAzimuthalAngle
        return None

    @FixationLightAzimuthalAngle.setter
    def FixationLightAzimuthalAngle(self, value: Optional[float]):
        if value is None:
            if "FixationLightAzimuthalAngle" in self._dataset:
                del self._dataset.FixationLightAzimuthalAngle
        else:
            self._dataset.FixationLightAzimuthalAngle = value

    @property
    def FixationLightPolarAngle(self) -> Optional[float]:
        if "FixationLightPolarAngle" in self._dataset:
            return self._dataset.FixationLightPolarAngle
        return None

    @FixationLightPolarAngle.setter
    def FixationLightPolarAngle(self, value: Optional[float]):
        if value is None:
            if "FixationLightPolarAngle" in self._dataset:
                del self._dataset.FixationLightPolarAngle
        else:
            self._dataset.FixationLightPolarAngle = value

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
    def DeliveredDepthDoseParametersSequence(self) -> Optional[List[DeliveredDepthDoseParametersSequenceItem]]:
        if "DeliveredDepthDoseParametersSequence" in self._dataset:
            if len(self._DeliveredDepthDoseParametersSequence) == len(self._dataset.DeliveredDepthDoseParametersSequence):
                return self._DeliveredDepthDoseParametersSequence
            else:
                return [
                    DeliveredDepthDoseParametersSequenceItem(x) for x in self._dataset.DeliveredDepthDoseParametersSequence
                ]
        return None

    @DeliveredDepthDoseParametersSequence.setter
    def DeliveredDepthDoseParametersSequence(self, value: Optional[List[DeliveredDepthDoseParametersSequenceItem]]):
        if value is None:
            self._DeliveredDepthDoseParametersSequence = []
            if "DeliveredDepthDoseParametersSequence" in self._dataset:
                del self._dataset.DeliveredDepthDoseParametersSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, DeliveredDepthDoseParametersSequenceItem) for item in value
        ):
            raise ValueError(
                "DeliveredDepthDoseParametersSequence must be a list of DeliveredDepthDoseParametersSequenceItem objects"
            )
        else:
            self._DeliveredDepthDoseParametersSequence = value
            if "DeliveredDepthDoseParametersSequence" not in self._dataset:
                self._dataset.DeliveredDepthDoseParametersSequence = pydicom.Sequence()
            self._dataset.DeliveredDepthDoseParametersSequence.clear()
            self._dataset.DeliveredDepthDoseParametersSequence.extend([item.to_dataset() for item in value])

    def add_DeliveredDepthDoseParameters(self, item: DeliveredDepthDoseParametersSequenceItem):
        if not isinstance(item, DeliveredDepthDoseParametersSequenceItem):
            raise ValueError("Item must be an instance of DeliveredDepthDoseParametersSequenceItem")
        self._DeliveredDepthDoseParametersSequence.append(item)
        if "DeliveredDepthDoseParametersSequence" not in self._dataset:
            self._dataset.DeliveredDepthDoseParametersSequence = pydicom.Sequence()
        self._dataset.DeliveredDepthDoseParametersSequence.append(item.to_dataset())

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
    def ReferencedToleranceTableNumber(self) -> Optional[int]:
        if "ReferencedToleranceTableNumber" in self._dataset:
            return self._dataset.ReferencedToleranceTableNumber
        return None

    @ReferencedToleranceTableNumber.setter
    def ReferencedToleranceTableNumber(self, value: Optional[int]):
        if value is None:
            if "ReferencedToleranceTableNumber" in self._dataset:
                del self._dataset.ReferencedToleranceTableNumber
        else:
            self._dataset.ReferencedToleranceTableNumber = value

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
