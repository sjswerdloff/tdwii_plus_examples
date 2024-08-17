from decimal import Decimal
from typing import Any, List, Optional

import pydicom

from .delivery_verification_image_sequence_item import (
    DeliveryVerificationImageSequenceItem,
)
from .device_motion_control_sequence_item import DeviceMotionControlSequenceItem


class BeamTaskSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._DeliveryVerificationImageSequence: List[DeliveryVerificationImageSequenceItem] = []
        self._DeviceMotionControlSequence: List[DeviceMotionControlSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ContinuationStartMeterset(self) -> Optional[float]:
        if "ContinuationStartMeterset" in self._dataset:
            return self._dataset.ContinuationStartMeterset
        return None

    @ContinuationStartMeterset.setter
    def ContinuationStartMeterset(self, value: Optional[float]):
        if value is None:
            if "ContinuationStartMeterset" in self._dataset:
                del self._dataset.ContinuationStartMeterset
        else:
            self._dataset.ContinuationStartMeterset = value

    @property
    def ContinuationEndMeterset(self) -> Optional[float]:
        if "ContinuationEndMeterset" in self._dataset:
            return self._dataset.ContinuationEndMeterset
        return None

    @ContinuationEndMeterset.setter
    def ContinuationEndMeterset(self, value: Optional[float]):
        if value is None:
            if "ContinuationEndMeterset" in self._dataset:
                del self._dataset.ContinuationEndMeterset
        else:
            self._dataset.ContinuationEndMeterset = value

    @property
    def BeamTaskType(self) -> Optional[str]:
        if "BeamTaskType" in self._dataset:
            return self._dataset.BeamTaskType
        return None

    @BeamTaskType.setter
    def BeamTaskType(self, value: Optional[str]):
        if value is None:
            if "BeamTaskType" in self._dataset:
                del self._dataset.BeamTaskType
        else:
            self._dataset.BeamTaskType = value

    @property
    def AutosequenceFlag(self) -> Optional[str]:
        if "AutosequenceFlag" in self._dataset:
            return self._dataset.AutosequenceFlag
        return None

    @AutosequenceFlag.setter
    def AutosequenceFlag(self, value: Optional[str]):
        if value is None:
            if "AutosequenceFlag" in self._dataset:
                del self._dataset.AutosequenceFlag
        else:
            self._dataset.AutosequenceFlag = value

    @property
    def TableTopVerticalAdjustedPosition(self) -> Optional[float]:
        if "TableTopVerticalAdjustedPosition" in self._dataset:
            return self._dataset.TableTopVerticalAdjustedPosition
        return None

    @TableTopVerticalAdjustedPosition.setter
    def TableTopVerticalAdjustedPosition(self, value: Optional[float]):
        if value is None:
            if "TableTopVerticalAdjustedPosition" in self._dataset:
                del self._dataset.TableTopVerticalAdjustedPosition
        else:
            self._dataset.TableTopVerticalAdjustedPosition = value

    @property
    def TableTopLongitudinalAdjustedPosition(self) -> Optional[float]:
        if "TableTopLongitudinalAdjustedPosition" in self._dataset:
            return self._dataset.TableTopLongitudinalAdjustedPosition
        return None

    @TableTopLongitudinalAdjustedPosition.setter
    def TableTopLongitudinalAdjustedPosition(self, value: Optional[float]):
        if value is None:
            if "TableTopLongitudinalAdjustedPosition" in self._dataset:
                del self._dataset.TableTopLongitudinalAdjustedPosition
        else:
            self._dataset.TableTopLongitudinalAdjustedPosition = value

    @property
    def TableTopLateralAdjustedPosition(self) -> Optional[float]:
        if "TableTopLateralAdjustedPosition" in self._dataset:
            return self._dataset.TableTopLateralAdjustedPosition
        return None

    @TableTopLateralAdjustedPosition.setter
    def TableTopLateralAdjustedPosition(self, value: Optional[float]):
        if value is None:
            if "TableTopLateralAdjustedPosition" in self._dataset:
                del self._dataset.TableTopLateralAdjustedPosition
        else:
            self._dataset.TableTopLateralAdjustedPosition = value

    @property
    def PatientSupportAdjustedAngle(self) -> Optional[float]:
        if "PatientSupportAdjustedAngle" in self._dataset:
            return self._dataset.PatientSupportAdjustedAngle
        return None

    @PatientSupportAdjustedAngle.setter
    def PatientSupportAdjustedAngle(self, value: Optional[float]):
        if value is None:
            if "PatientSupportAdjustedAngle" in self._dataset:
                del self._dataset.PatientSupportAdjustedAngle
        else:
            self._dataset.PatientSupportAdjustedAngle = value

    @property
    def TableTopEccentricAdjustedAngle(self) -> Optional[float]:
        if "TableTopEccentricAdjustedAngle" in self._dataset:
            return self._dataset.TableTopEccentricAdjustedAngle
        return None

    @TableTopEccentricAdjustedAngle.setter
    def TableTopEccentricAdjustedAngle(self, value: Optional[float]):
        if value is None:
            if "TableTopEccentricAdjustedAngle" in self._dataset:
                del self._dataset.TableTopEccentricAdjustedAngle
        else:
            self._dataset.TableTopEccentricAdjustedAngle = value

    @property
    def TableTopPitchAdjustedAngle(self) -> Optional[float]:
        if "TableTopPitchAdjustedAngle" in self._dataset:
            return self._dataset.TableTopPitchAdjustedAngle
        return None

    @TableTopPitchAdjustedAngle.setter
    def TableTopPitchAdjustedAngle(self, value: Optional[float]):
        if value is None:
            if "TableTopPitchAdjustedAngle" in self._dataset:
                del self._dataset.TableTopPitchAdjustedAngle
        else:
            self._dataset.TableTopPitchAdjustedAngle = value

    @property
    def TableTopRollAdjustedAngle(self) -> Optional[float]:
        if "TableTopRollAdjustedAngle" in self._dataset:
            return self._dataset.TableTopRollAdjustedAngle
        return None

    @TableTopRollAdjustedAngle.setter
    def TableTopRollAdjustedAngle(self, value: Optional[float]):
        if value is None:
            if "TableTopRollAdjustedAngle" in self._dataset:
                del self._dataset.TableTopRollAdjustedAngle
        else:
            self._dataset.TableTopRollAdjustedAngle = value

    @property
    def DeliveryVerificationImageSequence(self) -> Optional[List[DeliveryVerificationImageSequenceItem]]:
        if "DeliveryVerificationImageSequence" in self._dataset:
            if len(self._DeliveryVerificationImageSequence) == len(self._dataset.DeliveryVerificationImageSequence):
                return self._DeliveryVerificationImageSequence
            else:
                return [DeliveryVerificationImageSequenceItem(x) for x in self._dataset.DeliveryVerificationImageSequence]
        return None

    @DeliveryVerificationImageSequence.setter
    def DeliveryVerificationImageSequence(self, value: Optional[List[DeliveryVerificationImageSequenceItem]]):
        if value is None:
            self._DeliveryVerificationImageSequence = []
            if "DeliveryVerificationImageSequence" in self._dataset:
                del self._dataset.DeliveryVerificationImageSequence
        elif not isinstance(value, list) or not all(isinstance(item, DeliveryVerificationImageSequenceItem) for item in value):
            raise ValueError(
                f"DeliveryVerificationImageSequence must be a list of DeliveryVerificationImageSequenceItem objects"
            )
        else:
            self._DeliveryVerificationImageSequence = value
            if "DeliveryVerificationImageSequence" not in self._dataset:
                self._dataset.DeliveryVerificationImageSequence = pydicom.Sequence()
            self._dataset.DeliveryVerificationImageSequence.clear()
            self._dataset.DeliveryVerificationImageSequence.extend([item.to_dataset() for item in value])

    def add_DeliveryVerificationImage(self, item: DeliveryVerificationImageSequenceItem):
        if not isinstance(item, DeliveryVerificationImageSequenceItem):
            raise ValueError(f"Item must be an instance of DeliveryVerificationImageSequenceItem")
        self._DeliveryVerificationImageSequence.append(item)
        if "DeliveryVerificationImageSequence" not in self._dataset:
            self._dataset.DeliveryVerificationImageSequence = pydicom.Sequence()
        self._dataset.DeliveryVerificationImageSequence.append(item.to_dataset())

    @property
    def BeamOrderIndex(self) -> Optional[int]:
        if "BeamOrderIndex" in self._dataset:
            return self._dataset.BeamOrderIndex
        return None

    @BeamOrderIndex.setter
    def BeamOrderIndex(self, value: Optional[int]):
        if value is None:
            if "BeamOrderIndex" in self._dataset:
                del self._dataset.BeamOrderIndex
        else:
            self._dataset.BeamOrderIndex = value

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
    def PrimaryDosimeterUnit(self) -> Optional[str]:
        if "PrimaryDosimeterUnit" in self._dataset:
            return self._dataset.PrimaryDosimeterUnit
        return None

    @PrimaryDosimeterUnit.setter
    def PrimaryDosimeterUnit(self, value: Optional[str]):
        if value is None:
            if "PrimaryDosimeterUnit" in self._dataset:
                del self._dataset.PrimaryDosimeterUnit
        else:
            self._dataset.PrimaryDosimeterUnit = value

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
    def TableTopVerticalSetupDisplacement(self) -> Optional[Decimal]:
        if "TableTopVerticalSetupDisplacement" in self._dataset:
            return self._dataset.TableTopVerticalSetupDisplacement
        return None

    @TableTopVerticalSetupDisplacement.setter
    def TableTopVerticalSetupDisplacement(self, value: Optional[Decimal]):
        if value is None:
            if "TableTopVerticalSetupDisplacement" in self._dataset:
                del self._dataset.TableTopVerticalSetupDisplacement
        else:
            self._dataset.TableTopVerticalSetupDisplacement = value

    @property
    def TableTopLongitudinalSetupDisplacement(self) -> Optional[Decimal]:
        if "TableTopLongitudinalSetupDisplacement" in self._dataset:
            return self._dataset.TableTopLongitudinalSetupDisplacement
        return None

    @TableTopLongitudinalSetupDisplacement.setter
    def TableTopLongitudinalSetupDisplacement(self, value: Optional[Decimal]):
        if value is None:
            if "TableTopLongitudinalSetupDisplacement" in self._dataset:
                del self._dataset.TableTopLongitudinalSetupDisplacement
        else:
            self._dataset.TableTopLongitudinalSetupDisplacement = value

    @property
    def TableTopLateralSetupDisplacement(self) -> Optional[Decimal]:
        if "TableTopLateralSetupDisplacement" in self._dataset:
            return self._dataset.TableTopLateralSetupDisplacement
        return None

    @TableTopLateralSetupDisplacement.setter
    def TableTopLateralSetupDisplacement(self, value: Optional[Decimal]):
        if value is None:
            if "TableTopLateralSetupDisplacement" in self._dataset:
                del self._dataset.TableTopLateralSetupDisplacement
        else:
            self._dataset.TableTopLateralSetupDisplacement = value

    @property
    def DeviceMotionControlSequence(self) -> Optional[List[DeviceMotionControlSequenceItem]]:
        if "DeviceMotionControlSequence" in self._dataset:
            if len(self._DeviceMotionControlSequence) == len(self._dataset.DeviceMotionControlSequence):
                return self._DeviceMotionControlSequence
            else:
                return [DeviceMotionControlSequenceItem(x) for x in self._dataset.DeviceMotionControlSequence]
        return None

    @DeviceMotionControlSequence.setter
    def DeviceMotionControlSequence(self, value: Optional[List[DeviceMotionControlSequenceItem]]):
        if value is None:
            self._DeviceMotionControlSequence = []
            if "DeviceMotionControlSequence" in self._dataset:
                del self._dataset.DeviceMotionControlSequence
        elif not isinstance(value, list) or not all(isinstance(item, DeviceMotionControlSequenceItem) for item in value):
            raise ValueError(f"DeviceMotionControlSequence must be a list of DeviceMotionControlSequenceItem objects")
        else:
            self._DeviceMotionControlSequence = value
            if "DeviceMotionControlSequence" not in self._dataset:
                self._dataset.DeviceMotionControlSequence = pydicom.Sequence()
            self._dataset.DeviceMotionControlSequence.clear()
            self._dataset.DeviceMotionControlSequence.extend([item.to_dataset() for item in value])

    def add_DeviceMotionControl(self, item: DeviceMotionControlSequenceItem):
        if not isinstance(item, DeviceMotionControlSequenceItem):
            raise ValueError(f"Item must be an instance of DeviceMotionControlSequenceItem")
        self._DeviceMotionControlSequence.append(item)
        if "DeviceMotionControlSequence" not in self._dataset:
            self._dataset.DeviceMotionControlSequence = pydicom.Sequence()
        self._dataset.DeviceMotionControlSequence.append(item.to_dataset())

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
    def ReferencedFractionGroupNumber(self) -> Optional[int]:
        if "ReferencedFractionGroupNumber" in self._dataset:
            return self._dataset.ReferencedFractionGroupNumber
        return None

    @ReferencedFractionGroupNumber.setter
    def ReferencedFractionGroupNumber(self, value: Optional[int]):
        if value is None:
            if "ReferencedFractionGroupNumber" in self._dataset:
                del self._dataset.ReferencedFractionGroupNumber
        else:
            self._dataset.ReferencedFractionGroupNumber = value
