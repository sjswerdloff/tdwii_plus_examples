from decimal import Decimal
from typing import Any, List, Optional  # noqa

import pydicom

from .beam_limiting_device_tolerance_sequence_item import (
    BeamLimitingDeviceToleranceSequenceItem,
)


class IonToleranceTableSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._BeamLimitingDeviceToleranceSequence: List[BeamLimitingDeviceToleranceSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ToleranceTableNumber(self) -> Optional[int]:
        if "ToleranceTableNumber" in self._dataset:
            return self._dataset.ToleranceTableNumber
        return None

    @ToleranceTableNumber.setter
    def ToleranceTableNumber(self, value: Optional[int]):
        if value is None:
            if "ToleranceTableNumber" in self._dataset:
                del self._dataset.ToleranceTableNumber
        else:
            self._dataset.ToleranceTableNumber = value

    @property
    def ToleranceTableLabel(self) -> Optional[str]:
        if "ToleranceTableLabel" in self._dataset:
            return self._dataset.ToleranceTableLabel
        return None

    @ToleranceTableLabel.setter
    def ToleranceTableLabel(self, value: Optional[str]):
        if value is None:
            if "ToleranceTableLabel" in self._dataset:
                del self._dataset.ToleranceTableLabel
        else:
            self._dataset.ToleranceTableLabel = value

    @property
    def GantryAngleTolerance(self) -> Optional[Decimal]:
        if "GantryAngleTolerance" in self._dataset:
            return self._dataset.GantryAngleTolerance
        return None

    @GantryAngleTolerance.setter
    def GantryAngleTolerance(self, value: Optional[Decimal]):
        if value is None:
            if "GantryAngleTolerance" in self._dataset:
                del self._dataset.GantryAngleTolerance
        else:
            self._dataset.GantryAngleTolerance = value

    @property
    def BeamLimitingDeviceAngleTolerance(self) -> Optional[Decimal]:
        if "BeamLimitingDeviceAngleTolerance" in self._dataset:
            return self._dataset.BeamLimitingDeviceAngleTolerance
        return None

    @BeamLimitingDeviceAngleTolerance.setter
    def BeamLimitingDeviceAngleTolerance(self, value: Optional[Decimal]):
        if value is None:
            if "BeamLimitingDeviceAngleTolerance" in self._dataset:
                del self._dataset.BeamLimitingDeviceAngleTolerance
        else:
            self._dataset.BeamLimitingDeviceAngleTolerance = value

    @property
    def BeamLimitingDeviceToleranceSequence(self) -> Optional[List[BeamLimitingDeviceToleranceSequenceItem]]:
        if "BeamLimitingDeviceToleranceSequence" in self._dataset:
            if len(self._BeamLimitingDeviceToleranceSequence) == len(self._dataset.BeamLimitingDeviceToleranceSequence):
                return self._BeamLimitingDeviceToleranceSequence
            else:
                return [BeamLimitingDeviceToleranceSequenceItem(x) for x in self._dataset.BeamLimitingDeviceToleranceSequence]
        return None

    @BeamLimitingDeviceToleranceSequence.setter
    def BeamLimitingDeviceToleranceSequence(self, value: Optional[List[BeamLimitingDeviceToleranceSequenceItem]]):
        if value is None:
            self._BeamLimitingDeviceToleranceSequence = []
            if "BeamLimitingDeviceToleranceSequence" in self._dataset:
                del self._dataset.BeamLimitingDeviceToleranceSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, BeamLimitingDeviceToleranceSequenceItem) for item in value
        ):
            raise ValueError(
                "BeamLimitingDeviceToleranceSequence must be a list of BeamLimitingDeviceToleranceSequenceItem objects"
            )
        else:
            self._BeamLimitingDeviceToleranceSequence = value
            if "BeamLimitingDeviceToleranceSequence" not in self._dataset:
                self._dataset.BeamLimitingDeviceToleranceSequence = pydicom.Sequence()
            self._dataset.BeamLimitingDeviceToleranceSequence.clear()
            self._dataset.BeamLimitingDeviceToleranceSequence.extend([item.to_dataset() for item in value])

    def add_BeamLimitingDeviceTolerance(self, item: BeamLimitingDeviceToleranceSequenceItem):
        if not isinstance(item, BeamLimitingDeviceToleranceSequenceItem):
            raise ValueError("Item must be an instance of BeamLimitingDeviceToleranceSequenceItem")
        self._BeamLimitingDeviceToleranceSequence.append(item)
        if "BeamLimitingDeviceToleranceSequence" not in self._dataset:
            self._dataset.BeamLimitingDeviceToleranceSequence = pydicom.Sequence()
        self._dataset.BeamLimitingDeviceToleranceSequence.append(item.to_dataset())

    @property
    def SnoutPositionTolerance(self) -> Optional[float]:
        if "SnoutPositionTolerance" in self._dataset:
            return self._dataset.SnoutPositionTolerance
        return None

    @SnoutPositionTolerance.setter
    def SnoutPositionTolerance(self, value: Optional[float]):
        if value is None:
            if "SnoutPositionTolerance" in self._dataset:
                del self._dataset.SnoutPositionTolerance
        else:
            self._dataset.SnoutPositionTolerance = value

    @property
    def PatientSupportAngleTolerance(self) -> Optional[Decimal]:
        if "PatientSupportAngleTolerance" in self._dataset:
            return self._dataset.PatientSupportAngleTolerance
        return None

    @PatientSupportAngleTolerance.setter
    def PatientSupportAngleTolerance(self, value: Optional[Decimal]):
        if value is None:
            if "PatientSupportAngleTolerance" in self._dataset:
                del self._dataset.PatientSupportAngleTolerance
        else:
            self._dataset.PatientSupportAngleTolerance = value

    @property
    def TableTopPitchAngleTolerance(self) -> Optional[float]:
        if "TableTopPitchAngleTolerance" in self._dataset:
            return self._dataset.TableTopPitchAngleTolerance
        return None

    @TableTopPitchAngleTolerance.setter
    def TableTopPitchAngleTolerance(self, value: Optional[float]):
        if value is None:
            if "TableTopPitchAngleTolerance" in self._dataset:
                del self._dataset.TableTopPitchAngleTolerance
        else:
            self._dataset.TableTopPitchAngleTolerance = value

    @property
    def TableTopRollAngleTolerance(self) -> Optional[float]:
        if "TableTopRollAngleTolerance" in self._dataset:
            return self._dataset.TableTopRollAngleTolerance
        return None

    @TableTopRollAngleTolerance.setter
    def TableTopRollAngleTolerance(self, value: Optional[float]):
        if value is None:
            if "TableTopRollAngleTolerance" in self._dataset:
                del self._dataset.TableTopRollAngleTolerance
        else:
            self._dataset.TableTopRollAngleTolerance = value

    @property
    def TableTopVerticalPositionTolerance(self) -> Optional[Decimal]:
        if "TableTopVerticalPositionTolerance" in self._dataset:
            return self._dataset.TableTopVerticalPositionTolerance
        return None

    @TableTopVerticalPositionTolerance.setter
    def TableTopVerticalPositionTolerance(self, value: Optional[Decimal]):
        if value is None:
            if "TableTopVerticalPositionTolerance" in self._dataset:
                del self._dataset.TableTopVerticalPositionTolerance
        else:
            self._dataset.TableTopVerticalPositionTolerance = value

    @property
    def TableTopLongitudinalPositionTolerance(self) -> Optional[Decimal]:
        if "TableTopLongitudinalPositionTolerance" in self._dataset:
            return self._dataset.TableTopLongitudinalPositionTolerance
        return None

    @TableTopLongitudinalPositionTolerance.setter
    def TableTopLongitudinalPositionTolerance(self, value: Optional[Decimal]):
        if value is None:
            if "TableTopLongitudinalPositionTolerance" in self._dataset:
                del self._dataset.TableTopLongitudinalPositionTolerance
        else:
            self._dataset.TableTopLongitudinalPositionTolerance = value

    @property
    def TableTopLateralPositionTolerance(self) -> Optional[Decimal]:
        if "TableTopLateralPositionTolerance" in self._dataset:
            return self._dataset.TableTopLateralPositionTolerance
        return None

    @TableTopLateralPositionTolerance.setter
    def TableTopLateralPositionTolerance(self, value: Optional[Decimal]):
        if value is None:
            if "TableTopLateralPositionTolerance" in self._dataset:
                del self._dataset.TableTopLateralPositionTolerance
        else:
            self._dataset.TableTopLateralPositionTolerance = value

    @property
    def HeadFixationAngleTolerance(self) -> Optional[Decimal]:
        if "HeadFixationAngleTolerance" in self._dataset:
            return self._dataset.HeadFixationAngleTolerance
        return None

    @HeadFixationAngleTolerance.setter
    def HeadFixationAngleTolerance(self, value: Optional[Decimal]):
        if value is None:
            if "HeadFixationAngleTolerance" in self._dataset:
                del self._dataset.HeadFixationAngleTolerance
        else:
            self._dataset.HeadFixationAngleTolerance = value

    @property
    def ChairHeadFramePositionTolerance(self) -> Optional[Decimal]:
        if "ChairHeadFramePositionTolerance" in self._dataset:
            return self._dataset.ChairHeadFramePositionTolerance
        return None

    @ChairHeadFramePositionTolerance.setter
    def ChairHeadFramePositionTolerance(self, value: Optional[Decimal]):
        if value is None:
            if "ChairHeadFramePositionTolerance" in self._dataset:
                del self._dataset.ChairHeadFramePositionTolerance
        else:
            self._dataset.ChairHeadFramePositionTolerance = value

    @property
    def FixationLightAzimuthalAngleTolerance(self) -> Optional[Decimal]:
        if "FixationLightAzimuthalAngleTolerance" in self._dataset:
            return self._dataset.FixationLightAzimuthalAngleTolerance
        return None

    @FixationLightAzimuthalAngleTolerance.setter
    def FixationLightAzimuthalAngleTolerance(self, value: Optional[Decimal]):
        if value is None:
            if "FixationLightAzimuthalAngleTolerance" in self._dataset:
                del self._dataset.FixationLightAzimuthalAngleTolerance
        else:
            self._dataset.FixationLightAzimuthalAngleTolerance = value

    @property
    def FixationLightPolarAngleTolerance(self) -> Optional[Decimal]:
        if "FixationLightPolarAngleTolerance" in self._dataset:
            return self._dataset.FixationLightPolarAngleTolerance
        return None

    @FixationLightPolarAngleTolerance.setter
    def FixationLightPolarAngleTolerance(self, value: Optional[Decimal]):
        if value is None:
            if "FixationLightPolarAngleTolerance" in self._dataset:
                del self._dataset.FixationLightPolarAngleTolerance
        else:
            self._dataset.FixationLightPolarAngleTolerance = value
