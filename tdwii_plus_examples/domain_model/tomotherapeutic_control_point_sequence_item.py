from typing import Any, List, Optional  # noqa

import pydicom

from .beam_area_limit_sequence_item import BeamAreaLimitSequenceItem
from .delivery_rate_unit_sequence_item import DeliveryRateUnitSequenceItem
from .rt_beam_limiting_device_opening_sequence_item import (
    RTBeamLimitingDeviceOpeningSequenceItem,
)


class TomotherapeuticControlPointSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._DeliveryRateUnitSequence: List[DeliveryRateUnitSequenceItem] = []
        self._RTBeamLimitingDeviceOpeningSequence: List[RTBeamLimitingDeviceOpeningSequenceItem] = []
        self._BeamAreaLimitSequence: List[BeamAreaLimitSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def RTControlPointIndex(self) -> Optional[int]:
        if "RTControlPointIndex" in self._dataset:
            return self._dataset.RTControlPointIndex
        return None

    @RTControlPointIndex.setter
    def RTControlPointIndex(self, value: Optional[int]):
        if value is None:
            if "RTControlPointIndex" in self._dataset:
                del self._dataset.RTControlPointIndex
        else:
            self._dataset.RTControlPointIndex = value

    @property
    def ReferencedRadiationGenerationModeIndex(self) -> Optional[int]:
        if "ReferencedRadiationGenerationModeIndex" in self._dataset:
            return self._dataset.ReferencedRadiationGenerationModeIndex
        return None

    @ReferencedRadiationGenerationModeIndex.setter
    def ReferencedRadiationGenerationModeIndex(self, value: Optional[int]):
        if value is None:
            if "ReferencedRadiationGenerationModeIndex" in self._dataset:
                del self._dataset.ReferencedRadiationGenerationModeIndex
        else:
            self._dataset.ReferencedRadiationGenerationModeIndex = value

    @property
    def ReferencedTreatmentPositionIndex(self) -> Optional[int]:
        if "ReferencedTreatmentPositionIndex" in self._dataset:
            return self._dataset.ReferencedTreatmentPositionIndex
        return None

    @ReferencedTreatmentPositionIndex.setter
    def ReferencedTreatmentPositionIndex(self, value: Optional[int]):
        if value is None:
            if "ReferencedTreatmentPositionIndex" in self._dataset:
                del self._dataset.ReferencedTreatmentPositionIndex
        else:
            self._dataset.ReferencedTreatmentPositionIndex = value

    @property
    def CumulativeMeterset(self) -> Optional[float]:
        if "CumulativeMeterset" in self._dataset:
            return self._dataset.CumulativeMeterset
        return None

    @CumulativeMeterset.setter
    def CumulativeMeterset(self, value: Optional[float]):
        if value is None:
            if "CumulativeMeterset" in self._dataset:
                del self._dataset.CumulativeMeterset
        else:
            self._dataset.CumulativeMeterset = value

    @property
    def DeliveryRate(self) -> Optional[float]:
        if "DeliveryRate" in self._dataset:
            return self._dataset.DeliveryRate
        return None

    @DeliveryRate.setter
    def DeliveryRate(self, value: Optional[float]):
        if value is None:
            if "DeliveryRate" in self._dataset:
                del self._dataset.DeliveryRate
        else:
            self._dataset.DeliveryRate = value

    @property
    def DeliveryRateUnitSequence(self) -> Optional[List[DeliveryRateUnitSequenceItem]]:
        if "DeliveryRateUnitSequence" in self._dataset:
            if len(self._DeliveryRateUnitSequence) == len(self._dataset.DeliveryRateUnitSequence):
                return self._DeliveryRateUnitSequence
            else:
                return [DeliveryRateUnitSequenceItem(x) for x in self._dataset.DeliveryRateUnitSequence]
        return None

    @DeliveryRateUnitSequence.setter
    def DeliveryRateUnitSequence(self, value: Optional[List[DeliveryRateUnitSequenceItem]]):
        if value is None:
            self._DeliveryRateUnitSequence = []
            if "DeliveryRateUnitSequence" in self._dataset:
                del self._dataset.DeliveryRateUnitSequence
        elif not isinstance(value, list) or not all(isinstance(item, DeliveryRateUnitSequenceItem) for item in value):
            raise ValueError("DeliveryRateUnitSequence must be a list of DeliveryRateUnitSequenceItem objects")
        else:
            self._DeliveryRateUnitSequence = value
            if "DeliveryRateUnitSequence" not in self._dataset:
                self._dataset.DeliveryRateUnitSequence = pydicom.Sequence()
            self._dataset.DeliveryRateUnitSequence.clear()
            self._dataset.DeliveryRateUnitSequence.extend([item.to_dataset() for item in value])

    def add_DeliveryRateUnit(self, item: DeliveryRateUnitSequenceItem):
        if not isinstance(item, DeliveryRateUnitSequenceItem):
            raise ValueError("Item must be an instance of DeliveryRateUnitSequenceItem")
        self._DeliveryRateUnitSequence.append(item)
        if "DeliveryRateUnitSequence" not in self._dataset:
            self._dataset.DeliveryRateUnitSequence = pydicom.Sequence()
        self._dataset.DeliveryRateUnitSequence.append(item.to_dataset())

    @property
    def RTBeamLimitingDeviceOpeningSequence(self) -> Optional[List[RTBeamLimitingDeviceOpeningSequenceItem]]:
        if "RTBeamLimitingDeviceOpeningSequence" in self._dataset:
            if len(self._RTBeamLimitingDeviceOpeningSequence) == len(self._dataset.RTBeamLimitingDeviceOpeningSequence):
                return self._RTBeamLimitingDeviceOpeningSequence
            else:
                return [RTBeamLimitingDeviceOpeningSequenceItem(x) for x in self._dataset.RTBeamLimitingDeviceOpeningSequence]
        return None

    @RTBeamLimitingDeviceOpeningSequence.setter
    def RTBeamLimitingDeviceOpeningSequence(self, value: Optional[List[RTBeamLimitingDeviceOpeningSequenceItem]]):
        if value is None:
            self._RTBeamLimitingDeviceOpeningSequence = []
            if "RTBeamLimitingDeviceOpeningSequence" in self._dataset:
                del self._dataset.RTBeamLimitingDeviceOpeningSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, RTBeamLimitingDeviceOpeningSequenceItem) for item in value
        ):
            raise ValueError(
                "RTBeamLimitingDeviceOpeningSequence must be a list of RTBeamLimitingDeviceOpeningSequenceItem objects"
            )
        else:
            self._RTBeamLimitingDeviceOpeningSequence = value
            if "RTBeamLimitingDeviceOpeningSequence" not in self._dataset:
                self._dataset.RTBeamLimitingDeviceOpeningSequence = pydicom.Sequence()
            self._dataset.RTBeamLimitingDeviceOpeningSequence.clear()
            self._dataset.RTBeamLimitingDeviceOpeningSequence.extend([item.to_dataset() for item in value])

    def add_RTBeamLimitingDeviceOpening(self, item: RTBeamLimitingDeviceOpeningSequenceItem):
        if not isinstance(item, RTBeamLimitingDeviceOpeningSequenceItem):
            raise ValueError("Item must be an instance of RTBeamLimitingDeviceOpeningSequenceItem")
        self._RTBeamLimitingDeviceOpeningSequence.append(item)
        if "RTBeamLimitingDeviceOpeningSequence" not in self._dataset:
            self._dataset.RTBeamLimitingDeviceOpeningSequence = pydicom.Sequence()
        self._dataset.RTBeamLimitingDeviceOpeningSequence.append(item.to_dataset())

    @property
    def NumberOfRTBeamLimitingDeviceOpenings(self) -> Optional[int]:
        if "NumberOfRTBeamLimitingDeviceOpenings" in self._dataset:
            return self._dataset.NumberOfRTBeamLimitingDeviceOpenings
        return None

    @NumberOfRTBeamLimitingDeviceOpenings.setter
    def NumberOfRTBeamLimitingDeviceOpenings(self, value: Optional[int]):
        if value is None:
            if "NumberOfRTBeamLimitingDeviceOpenings" in self._dataset:
                del self._dataset.NumberOfRTBeamLimitingDeviceOpenings
        else:
            self._dataset.NumberOfRTBeamLimitingDeviceOpenings = value

    @property
    def SourceRollAngle(self) -> Optional[float]:
        if "SourceRollAngle" in self._dataset:
            return self._dataset.SourceRollAngle
        return None

    @SourceRollAngle.setter
    def SourceRollAngle(self, value: Optional[float]):
        if value is None:
            if "SourceRollAngle" in self._dataset:
                del self._dataset.SourceRollAngle
        else:
            self._dataset.SourceRollAngle = value

    @property
    def BeamAreaLimitSequence(self) -> Optional[List[BeamAreaLimitSequenceItem]]:
        if "BeamAreaLimitSequence" in self._dataset:
            if len(self._BeamAreaLimitSequence) == len(self._dataset.BeamAreaLimitSequence):
                return self._BeamAreaLimitSequence
            else:
                return [BeamAreaLimitSequenceItem(x) for x in self._dataset.BeamAreaLimitSequence]
        return None

    @BeamAreaLimitSequence.setter
    def BeamAreaLimitSequence(self, value: Optional[List[BeamAreaLimitSequenceItem]]):
        if value is None:
            self._BeamAreaLimitSequence = []
            if "BeamAreaLimitSequence" in self._dataset:
                del self._dataset.BeamAreaLimitSequence
        elif not isinstance(value, list) or not all(isinstance(item, BeamAreaLimitSequenceItem) for item in value):
            raise ValueError("BeamAreaLimitSequence must be a list of BeamAreaLimitSequenceItem objects")
        else:
            self._BeamAreaLimitSequence = value
            if "BeamAreaLimitSequence" not in self._dataset:
                self._dataset.BeamAreaLimitSequence = pydicom.Sequence()
            self._dataset.BeamAreaLimitSequence.clear()
            self._dataset.BeamAreaLimitSequence.extend([item.to_dataset() for item in value])

    def add_BeamAreaLimit(self, item: BeamAreaLimitSequenceItem):
        if not isinstance(item, BeamAreaLimitSequenceItem):
            raise ValueError("Item must be an instance of BeamAreaLimitSequenceItem")
        self._BeamAreaLimitSequence.append(item)
        if "BeamAreaLimitSequence" not in self._dataset:
            self._dataset.BeamAreaLimitSequence = pydicom.Sequence()
        self._dataset.BeamAreaLimitSequence.append(item.to_dataset())

    @property
    def RecordedRTControlPointDateTime(self) -> Optional[str]:
        if "RecordedRTControlPointDateTime" in self._dataset:
            return self._dataset.RecordedRTControlPointDateTime
        return None

    @RecordedRTControlPointDateTime.setter
    def RecordedRTControlPointDateTime(self, value: Optional[str]):
        if value is None:
            if "RecordedRTControlPointDateTime" in self._dataset:
                del self._dataset.RecordedRTControlPointDateTime
        else:
            self._dataset.RecordedRTControlPointDateTime = value

    @property
    def ReferencedRadiationRTControlPointIndex(self) -> Optional[int]:
        if "ReferencedRadiationRTControlPointIndex" in self._dataset:
            return self._dataset.ReferencedRadiationRTControlPointIndex
        return None

    @ReferencedRadiationRTControlPointIndex.setter
    def ReferencedRadiationRTControlPointIndex(self, value: Optional[int]):
        if value is None:
            if "ReferencedRadiationRTControlPointIndex" in self._dataset:
                del self._dataset.ReferencedRadiationRTControlPointIndex
        else:
            self._dataset.ReferencedRadiationRTControlPointIndex = value

    @property
    def TomotherapeuticLeafOpenDurations(self) -> Optional[List[float]]:
        if "TomotherapeuticLeafOpenDurations" in self._dataset:
            return self._dataset.TomotherapeuticLeafOpenDurations
        return None

    @TomotherapeuticLeafOpenDurations.setter
    def TomotherapeuticLeafOpenDurations(self, value: Optional[List[float]]):
        if value is None:
            if "TomotherapeuticLeafOpenDurations" in self._dataset:
                del self._dataset.TomotherapeuticLeafOpenDurations
        else:
            self._dataset.TomotherapeuticLeafOpenDurations = value

    @property
    def TomotherapeuticLeafInitialClosedDurations(self) -> Optional[List[float]]:
        if "TomotherapeuticLeafInitialClosedDurations" in self._dataset:
            return self._dataset.TomotherapeuticLeafInitialClosedDurations
        return None

    @TomotherapeuticLeafInitialClosedDurations.setter
    def TomotherapeuticLeafInitialClosedDurations(self, value: Optional[List[float]]):
        if value is None:
            if "TomotherapeuticLeafInitialClosedDurations" in self._dataset:
                del self._dataset.TomotherapeuticLeafInitialClosedDurations
        else:
            self._dataset.TomotherapeuticLeafInitialClosedDurations = value
