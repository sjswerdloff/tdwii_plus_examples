from decimal import Decimal
from typing import Any, List, Optional

import pydicom

from .dose_calibration_conditions_sequence_item import (
    DoseCalibrationConditionsSequenceItem,
)
from .radiation_device_configuration_and_commissioning_key_sequence_item import (
    RadiationDeviceConfigurationAndCommissioningKeySequenceItem,
)


class ReferencedBeamSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._RadiationDeviceConfigurationAndCommissioningKeySequence: List[
            RadiationDeviceConfigurationAndCommissioningKeySequenceItem
        ] = []
        self._DoseCalibrationConditionsSequence: List[DoseCalibrationConditionsSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ReferencedDoseReferenceUID(self) -> Optional[str]:
        if "ReferencedDoseReferenceUID" in self._dataset:
            return self._dataset.ReferencedDoseReferenceUID
        return None

    @ReferencedDoseReferenceUID.setter
    def ReferencedDoseReferenceUID(self, value: Optional[str]):
        if value is None:
            if "ReferencedDoseReferenceUID" in self._dataset:
                del self._dataset.ReferencedDoseReferenceUID
        else:
            self._dataset.ReferencedDoseReferenceUID = value

    @property
    def BeamDose(self) -> Optional[Decimal]:
        if "BeamDose" in self._dataset:
            return self._dataset.BeamDose
        return None

    @BeamDose.setter
    def BeamDose(self, value: Optional[Decimal]):
        if value is None:
            if "BeamDose" in self._dataset:
                del self._dataset.BeamDose
        else:
            self._dataset.BeamDose = value

    @property
    def BeamMeterset(self) -> Optional[Decimal]:
        if "BeamMeterset" in self._dataset:
            return self._dataset.BeamMeterset
        return None

    @BeamMeterset.setter
    def BeamMeterset(self, value: Optional[Decimal]):
        if value is None:
            if "BeamMeterset" in self._dataset:
                del self._dataset.BeamMeterset
        else:
            self._dataset.BeamMeterset = value

    @property
    def BeamDoseType(self) -> Optional[str]:
        if "BeamDoseType" in self._dataset:
            return self._dataset.BeamDoseType
        return None

    @BeamDoseType.setter
    def BeamDoseType(self, value: Optional[str]):
        if value is None:
            if "BeamDoseType" in self._dataset:
                del self._dataset.BeamDoseType
        else:
            self._dataset.BeamDoseType = value

    @property
    def AlternateBeamDose(self) -> Optional[Decimal]:
        if "AlternateBeamDose" in self._dataset:
            return self._dataset.AlternateBeamDose
        return None

    @AlternateBeamDose.setter
    def AlternateBeamDose(self, value: Optional[Decimal]):
        if value is None:
            if "AlternateBeamDose" in self._dataset:
                del self._dataset.AlternateBeamDose
        else:
            self._dataset.AlternateBeamDose = value

    @property
    def AlternateBeamDoseType(self) -> Optional[str]:
        if "AlternateBeamDoseType" in self._dataset:
            return self._dataset.AlternateBeamDoseType
        return None

    @AlternateBeamDoseType.setter
    def AlternateBeamDoseType(self, value: Optional[str]):
        if value is None:
            if "AlternateBeamDoseType" in self._dataset:
                del self._dataset.AlternateBeamDoseType
        else:
            self._dataset.AlternateBeamDoseType = value

    @property
    def BeamDeliveryDurationLimit(self) -> Optional[float]:
        if "BeamDeliveryDurationLimit" in self._dataset:
            return self._dataset.BeamDeliveryDurationLimit
        return None

    @BeamDeliveryDurationLimit.setter
    def BeamDeliveryDurationLimit(self, value: Optional[float]):
        if value is None:
            if "BeamDeliveryDurationLimit" in self._dataset:
                del self._dataset.BeamDeliveryDurationLimit
        else:
            self._dataset.BeamDeliveryDurationLimit = value

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
                f"RadiationDeviceConfigurationAndCommissioningKeySequence must be a list of RadiationDeviceConfigurationAndCommissioningKeySequenceItem objects"
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
            raise ValueError(f"Item must be an instance of RadiationDeviceConfigurationAndCommissioningKeySequenceItem")
        self._RadiationDeviceConfigurationAndCommissioningKeySequence.append(item)
        if "RadiationDeviceConfigurationAndCommissioningKeySequence" not in self._dataset:
            self._dataset.RadiationDeviceConfigurationAndCommissioningKeySequence = pydicom.Sequence()
        self._dataset.RadiationDeviceConfigurationAndCommissioningKeySequence.append(item.to_dataset())

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
                f"DoseCalibrationConditionsSequence must be a list of DoseCalibrationConditionsSequenceItem objects"
            )
        else:
            self._DoseCalibrationConditionsSequence = value
            if "DoseCalibrationConditionsSequence" not in self._dataset:
                self._dataset.DoseCalibrationConditionsSequence = pydicom.Sequence()
            self._dataset.DoseCalibrationConditionsSequence.clear()
            self._dataset.DoseCalibrationConditionsSequence.extend([item.to_dataset() for item in value])

    def add_DoseCalibrationConditions(self, item: DoseCalibrationConditionsSequenceItem):
        if not isinstance(item, DoseCalibrationConditionsSequenceItem):
            raise ValueError(f"Item must be an instance of DoseCalibrationConditionsSequenceItem")
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
