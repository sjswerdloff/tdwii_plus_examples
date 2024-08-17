from typing import Any, List, Optional

import pydicom

from .beam_area_limit_sequence_item import BeamAreaLimitSequenceItem
from .delivery_rate_unit_sequence_item import DeliveryRateUnitSequenceItem
from .rt_beam_limiting_device_opening_sequence_item import (
    RTBeamLimitingDeviceOpeningSequenceItem,
)
from .wedge_position_sequence_item import WedgePositionSequenceItem


class CArmPhotonElectronControlPointSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._WedgePositionSequence: List[WedgePositionSequenceItem] = []
        self._DeliveryRateUnitSequence: List[DeliveryRateUnitSequenceItem] = []
        self._RTBeamLimitingDeviceOpeningSequence: List[RTBeamLimitingDeviceOpeningSequenceItem] = []
        self._BeamAreaLimitSequence: List[BeamAreaLimitSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

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
    def SourceToPatientSurfaceDistance(self) -> Optional[float]:
        if "SourceToPatientSurfaceDistance" in self._dataset:
            return self._dataset.SourceToPatientSurfaceDistance
        return None

    @SourceToPatientSurfaceDistance.setter
    def SourceToPatientSurfaceDistance(self, value: Optional[float]):
        if value is None:
            if "SourceToPatientSurfaceDistance" in self._dataset:
                del self._dataset.SourceToPatientSurfaceDistance
        else:
            self._dataset.SourceToPatientSurfaceDistance = value

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
            raise ValueError(f"DeliveryRateUnitSequence must be a list of DeliveryRateUnitSequenceItem objects")
        else:
            self._DeliveryRateUnitSequence = value
            if "DeliveryRateUnitSequence" not in self._dataset:
                self._dataset.DeliveryRateUnitSequence = pydicom.Sequence()
            self._dataset.DeliveryRateUnitSequence.clear()
            self._dataset.DeliveryRateUnitSequence.extend([item.to_dataset() for item in value])

    def add_DeliveryRateUnit(self, item: DeliveryRateUnitSequenceItem):
        if not isinstance(item, DeliveryRateUnitSequenceItem):
            raise ValueError(f"Item must be an instance of DeliveryRateUnitSequenceItem")
        self._DeliveryRateUnitSequence.append(item)
        if "DeliveryRateUnitSequence" not in self._dataset:
            self._dataset.DeliveryRateUnitSequence = pydicom.Sequence()
        self._dataset.DeliveryRateUnitSequence.append(item.to_dataset())

    @property
    def NumberOfWedgePositions(self) -> Optional[int]:
        if "NumberOfWedgePositions" in self._dataset:
            return self._dataset.NumberOfWedgePositions
        return None

    @NumberOfWedgePositions.setter
    def NumberOfWedgePositions(self, value: Optional[int]):
        if value is None:
            if "NumberOfWedgePositions" in self._dataset:
                del self._dataset.NumberOfWedgePositions
        else:
            self._dataset.NumberOfWedgePositions = value

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
                f"RTBeamLimitingDeviceOpeningSequence must be a list of RTBeamLimitingDeviceOpeningSequenceItem objects"
            )
        else:
            self._RTBeamLimitingDeviceOpeningSequence = value
            if "RTBeamLimitingDeviceOpeningSequence" not in self._dataset:
                self._dataset.RTBeamLimitingDeviceOpeningSequence = pydicom.Sequence()
            self._dataset.RTBeamLimitingDeviceOpeningSequence.clear()
            self._dataset.RTBeamLimitingDeviceOpeningSequence.extend([item.to_dataset() for item in value])

    def add_RTBeamLimitingDeviceOpening(self, item: RTBeamLimitingDeviceOpeningSequenceItem):
        if not isinstance(item, RTBeamLimitingDeviceOpeningSequenceItem):
            raise ValueError(f"Item must be an instance of RTBeamLimitingDeviceOpeningSequenceItem")
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
    def RTBeamLimitingDeviceAngle(self) -> Optional[float]:
        if "RTBeamLimitingDeviceAngle" in self._dataset:
            return self._dataset.RTBeamLimitingDeviceAngle
        return None

    @RTBeamLimitingDeviceAngle.setter
    def RTBeamLimitingDeviceAngle(self, value: Optional[float]):
        if value is None:
            if "RTBeamLimitingDeviceAngle" in self._dataset:
                del self._dataset.RTBeamLimitingDeviceAngle
        else:
            self._dataset.RTBeamLimitingDeviceAngle = value

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
            raise ValueError(f"BeamAreaLimitSequence must be a list of BeamAreaLimitSequenceItem objects")
        else:
            self._BeamAreaLimitSequence = value
            if "BeamAreaLimitSequence" not in self._dataset:
                self._dataset.BeamAreaLimitSequence = pydicom.Sequence()
            self._dataset.BeamAreaLimitSequence.clear()
            self._dataset.BeamAreaLimitSequence.extend([item.to_dataset() for item in value])

    def add_BeamAreaLimit(self, item: BeamAreaLimitSequenceItem):
        if not isinstance(item, BeamAreaLimitSequenceItem):
            raise ValueError(f"Item must be an instance of BeamAreaLimitSequenceItem")
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
