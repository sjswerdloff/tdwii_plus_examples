from decimal import Decimal
from typing import Any, List, Optional

import pydicom

from .brachy_control_point_delivered_sequence_item import (
    BrachyControlPointDeliveredSequenceItem,
)
from .pulse_specific_brachy_control_point_delivered_sequence_item import (
    PulseSpecificBrachyControlPointDeliveredSequenceItem,
)
from .recorded_channel_shield_sequence_item import RecordedChannelShieldSequenceItem
from .recorded_source_applicator_sequence_item import (
    RecordedSourceApplicatorSequenceItem,
)
from .referenced_calculated_dose_reference_sequence_item import (
    ReferencedCalculatedDoseReferenceSequenceItem,
)
from .referenced_measured_dose_reference_sequence_item import (
    ReferencedMeasuredDoseReferenceSequenceItem,
)


class RecordedChannelSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._ReferencedMeasuredDoseReferenceSequence: List[ReferencedMeasuredDoseReferenceSequenceItem] = []
        self._ReferencedCalculatedDoseReferenceSequence: List[ReferencedCalculatedDoseReferenceSequenceItem] = []
        self._RecordedSourceApplicatorSequence: List[RecordedSourceApplicatorSequenceItem] = []
        self._RecordedChannelShieldSequence: List[RecordedChannelShieldSequenceItem] = []
        self._BrachyControlPointDeliveredSequence: List[BrachyControlPointDeliveredSequenceItem] = []
        self._PulseSpecificBrachyControlPointDeliveredSequence: List[PulseSpecificBrachyControlPointDeliveredSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ReferencedChannelNumber(self) -> Optional[int]:
        if "ReferencedChannelNumber" in self._dataset:
            return self._dataset.ReferencedChannelNumber
        return None

    @ReferencedChannelNumber.setter
    def ReferencedChannelNumber(self, value: Optional[int]):
        if value is None:
            if "ReferencedChannelNumber" in self._dataset:
                del self._dataset.ReferencedChannelNumber
        else:
            self._dataset.ReferencedChannelNumber = value

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
                f"ReferencedMeasuredDoseReferenceSequence must be a list of ReferencedMeasuredDoseReferenceSequenceItem objects"
            )
        else:
            self._ReferencedMeasuredDoseReferenceSequence = value
            if "ReferencedMeasuredDoseReferenceSequence" not in self._dataset:
                self._dataset.ReferencedMeasuredDoseReferenceSequence = pydicom.Sequence()
            self._dataset.ReferencedMeasuredDoseReferenceSequence.clear()
            self._dataset.ReferencedMeasuredDoseReferenceSequence.extend([item.to_dataset() for item in value])

    def add_ReferencedMeasuredDoseReference(self, item: ReferencedMeasuredDoseReferenceSequenceItem):
        if not isinstance(item, ReferencedMeasuredDoseReferenceSequenceItem):
            raise ValueError(f"Item must be an instance of ReferencedMeasuredDoseReferenceSequenceItem")
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
                f"ReferencedCalculatedDoseReferenceSequence must be a list of ReferencedCalculatedDoseReferenceSequenceItem objects"
            )
        else:
            self._ReferencedCalculatedDoseReferenceSequence = value
            if "ReferencedCalculatedDoseReferenceSequence" not in self._dataset:
                self._dataset.ReferencedCalculatedDoseReferenceSequence = pydicom.Sequence()
            self._dataset.ReferencedCalculatedDoseReferenceSequence.clear()
            self._dataset.ReferencedCalculatedDoseReferenceSequence.extend([item.to_dataset() for item in value])

    def add_ReferencedCalculatedDoseReference(self, item: ReferencedCalculatedDoseReferenceSequenceItem):
        if not isinstance(item, ReferencedCalculatedDoseReferenceSequenceItem):
            raise ValueError(f"Item must be an instance of ReferencedCalculatedDoseReferenceSequenceItem")
        self._ReferencedCalculatedDoseReferenceSequence.append(item)
        if "ReferencedCalculatedDoseReferenceSequence" not in self._dataset:
            self._dataset.ReferencedCalculatedDoseReferenceSequence = pydicom.Sequence()
        self._dataset.ReferencedCalculatedDoseReferenceSequence.append(item.to_dataset())

    @property
    def SpecifiedChannelTotalTime(self) -> Optional[Decimal]:
        if "SpecifiedChannelTotalTime" in self._dataset:
            return self._dataset.SpecifiedChannelTotalTime
        return None

    @SpecifiedChannelTotalTime.setter
    def SpecifiedChannelTotalTime(self, value: Optional[Decimal]):
        if value is None:
            if "SpecifiedChannelTotalTime" in self._dataset:
                del self._dataset.SpecifiedChannelTotalTime
        else:
            self._dataset.SpecifiedChannelTotalTime = value

    @property
    def DeliveredChannelTotalTime(self) -> Optional[Decimal]:
        if "DeliveredChannelTotalTime" in self._dataset:
            return self._dataset.DeliveredChannelTotalTime
        return None

    @DeliveredChannelTotalTime.setter
    def DeliveredChannelTotalTime(self, value: Optional[Decimal]):
        if value is None:
            if "DeliveredChannelTotalTime" in self._dataset:
                del self._dataset.DeliveredChannelTotalTime
        else:
            self._dataset.DeliveredChannelTotalTime = value

    @property
    def SpecifiedNumberOfPulses(self) -> Optional[int]:
        if "SpecifiedNumberOfPulses" in self._dataset:
            return self._dataset.SpecifiedNumberOfPulses
        return None

    @SpecifiedNumberOfPulses.setter
    def SpecifiedNumberOfPulses(self, value: Optional[int]):
        if value is None:
            if "SpecifiedNumberOfPulses" in self._dataset:
                del self._dataset.SpecifiedNumberOfPulses
        else:
            self._dataset.SpecifiedNumberOfPulses = value

    @property
    def DeliveredNumberOfPulses(self) -> Optional[int]:
        if "DeliveredNumberOfPulses" in self._dataset:
            return self._dataset.DeliveredNumberOfPulses
        return None

    @DeliveredNumberOfPulses.setter
    def DeliveredNumberOfPulses(self, value: Optional[int]):
        if value is None:
            if "DeliveredNumberOfPulses" in self._dataset:
                del self._dataset.DeliveredNumberOfPulses
        else:
            self._dataset.DeliveredNumberOfPulses = value

    @property
    def SpecifiedPulseRepetitionInterval(self) -> Optional[Decimal]:
        if "SpecifiedPulseRepetitionInterval" in self._dataset:
            return self._dataset.SpecifiedPulseRepetitionInterval
        return None

    @SpecifiedPulseRepetitionInterval.setter
    def SpecifiedPulseRepetitionInterval(self, value: Optional[Decimal]):
        if value is None:
            if "SpecifiedPulseRepetitionInterval" in self._dataset:
                del self._dataset.SpecifiedPulseRepetitionInterval
        else:
            self._dataset.SpecifiedPulseRepetitionInterval = value

    @property
    def DeliveredPulseRepetitionInterval(self) -> Optional[Decimal]:
        if "DeliveredPulseRepetitionInterval" in self._dataset:
            return self._dataset.DeliveredPulseRepetitionInterval
        return None

    @DeliveredPulseRepetitionInterval.setter
    def DeliveredPulseRepetitionInterval(self, value: Optional[Decimal]):
        if value is None:
            if "DeliveredPulseRepetitionInterval" in self._dataset:
                del self._dataset.DeliveredPulseRepetitionInterval
        else:
            self._dataset.DeliveredPulseRepetitionInterval = value

    @property
    def RecordedSourceApplicatorSequence(self) -> Optional[List[RecordedSourceApplicatorSequenceItem]]:
        if "RecordedSourceApplicatorSequence" in self._dataset:
            if len(self._RecordedSourceApplicatorSequence) == len(self._dataset.RecordedSourceApplicatorSequence):
                return self._RecordedSourceApplicatorSequence
            else:
                return [RecordedSourceApplicatorSequenceItem(x) for x in self._dataset.RecordedSourceApplicatorSequence]
        return None

    @RecordedSourceApplicatorSequence.setter
    def RecordedSourceApplicatorSequence(self, value: Optional[List[RecordedSourceApplicatorSequenceItem]]):
        if value is None:
            self._RecordedSourceApplicatorSequence = []
            if "RecordedSourceApplicatorSequence" in self._dataset:
                del self._dataset.RecordedSourceApplicatorSequence
        elif not isinstance(value, list) or not all(isinstance(item, RecordedSourceApplicatorSequenceItem) for item in value):
            raise ValueError(
                f"RecordedSourceApplicatorSequence must be a list of RecordedSourceApplicatorSequenceItem objects"
            )
        else:
            self._RecordedSourceApplicatorSequence = value
            if "RecordedSourceApplicatorSequence" not in self._dataset:
                self._dataset.RecordedSourceApplicatorSequence = pydicom.Sequence()
            self._dataset.RecordedSourceApplicatorSequence.clear()
            self._dataset.RecordedSourceApplicatorSequence.extend([item.to_dataset() for item in value])

    def add_RecordedSourceApplicator(self, item: RecordedSourceApplicatorSequenceItem):
        if not isinstance(item, RecordedSourceApplicatorSequenceItem):
            raise ValueError(f"Item must be an instance of RecordedSourceApplicatorSequenceItem")
        self._RecordedSourceApplicatorSequence.append(item)
        if "RecordedSourceApplicatorSequence" not in self._dataset:
            self._dataset.RecordedSourceApplicatorSequence = pydicom.Sequence()
        self._dataset.RecordedSourceApplicatorSequence.append(item.to_dataset())

    @property
    def RecordedChannelShieldSequence(self) -> Optional[List[RecordedChannelShieldSequenceItem]]:
        if "RecordedChannelShieldSequence" in self._dataset:
            if len(self._RecordedChannelShieldSequence) == len(self._dataset.RecordedChannelShieldSequence):
                return self._RecordedChannelShieldSequence
            else:
                return [RecordedChannelShieldSequenceItem(x) for x in self._dataset.RecordedChannelShieldSequence]
        return None

    @RecordedChannelShieldSequence.setter
    def RecordedChannelShieldSequence(self, value: Optional[List[RecordedChannelShieldSequenceItem]]):
        if value is None:
            self._RecordedChannelShieldSequence = []
            if "RecordedChannelShieldSequence" in self._dataset:
                del self._dataset.RecordedChannelShieldSequence
        elif not isinstance(value, list) or not all(isinstance(item, RecordedChannelShieldSequenceItem) for item in value):
            raise ValueError(f"RecordedChannelShieldSequence must be a list of RecordedChannelShieldSequenceItem objects")
        else:
            self._RecordedChannelShieldSequence = value
            if "RecordedChannelShieldSequence" not in self._dataset:
                self._dataset.RecordedChannelShieldSequence = pydicom.Sequence()
            self._dataset.RecordedChannelShieldSequence.clear()
            self._dataset.RecordedChannelShieldSequence.extend([item.to_dataset() for item in value])

    def add_RecordedChannelShield(self, item: RecordedChannelShieldSequenceItem):
        if not isinstance(item, RecordedChannelShieldSequenceItem):
            raise ValueError(f"Item must be an instance of RecordedChannelShieldSequenceItem")
        self._RecordedChannelShieldSequence.append(item)
        if "RecordedChannelShieldSequence" not in self._dataset:
            self._dataset.RecordedChannelShieldSequence = pydicom.Sequence()
        self._dataset.RecordedChannelShieldSequence.append(item.to_dataset())

    @property
    def BrachyControlPointDeliveredSequence(self) -> Optional[List[BrachyControlPointDeliveredSequenceItem]]:
        if "BrachyControlPointDeliveredSequence" in self._dataset:
            if len(self._BrachyControlPointDeliveredSequence) == len(self._dataset.BrachyControlPointDeliveredSequence):
                return self._BrachyControlPointDeliveredSequence
            else:
                return [BrachyControlPointDeliveredSequenceItem(x) for x in self._dataset.BrachyControlPointDeliveredSequence]
        return None

    @BrachyControlPointDeliveredSequence.setter
    def BrachyControlPointDeliveredSequence(self, value: Optional[List[BrachyControlPointDeliveredSequenceItem]]):
        if value is None:
            self._BrachyControlPointDeliveredSequence = []
            if "BrachyControlPointDeliveredSequence" in self._dataset:
                del self._dataset.BrachyControlPointDeliveredSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, BrachyControlPointDeliveredSequenceItem) for item in value
        ):
            raise ValueError(
                f"BrachyControlPointDeliveredSequence must be a list of BrachyControlPointDeliveredSequenceItem objects"
            )
        else:
            self._BrachyControlPointDeliveredSequence = value
            if "BrachyControlPointDeliveredSequence" not in self._dataset:
                self._dataset.BrachyControlPointDeliveredSequence = pydicom.Sequence()
            self._dataset.BrachyControlPointDeliveredSequence.clear()
            self._dataset.BrachyControlPointDeliveredSequence.extend([item.to_dataset() for item in value])

    def add_BrachyControlPointDelivered(self, item: BrachyControlPointDeliveredSequenceItem):
        if not isinstance(item, BrachyControlPointDeliveredSequenceItem):
            raise ValueError(f"Item must be an instance of BrachyControlPointDeliveredSequenceItem")
        self._BrachyControlPointDeliveredSequence.append(item)
        if "BrachyControlPointDeliveredSequence" not in self._dataset:
            self._dataset.BrachyControlPointDeliveredSequence = pydicom.Sequence()
        self._dataset.BrachyControlPointDeliveredSequence.append(item.to_dataset())

    @property
    def SafePositionExitDate(self) -> Optional[str]:
        if "SafePositionExitDate" in self._dataset:
            return self._dataset.SafePositionExitDate
        return None

    @SafePositionExitDate.setter
    def SafePositionExitDate(self, value: Optional[str]):
        if value is None:
            if "SafePositionExitDate" in self._dataset:
                del self._dataset.SafePositionExitDate
        else:
            self._dataset.SafePositionExitDate = value

    @property
    def SafePositionExitTime(self) -> Optional[str]:
        if "SafePositionExitTime" in self._dataset:
            return self._dataset.SafePositionExitTime
        return None

    @SafePositionExitTime.setter
    def SafePositionExitTime(self, value: Optional[str]):
        if value is None:
            if "SafePositionExitTime" in self._dataset:
                del self._dataset.SafePositionExitTime
        else:
            self._dataset.SafePositionExitTime = value

    @property
    def SafePositionReturnDate(self) -> Optional[str]:
        if "SafePositionReturnDate" in self._dataset:
            return self._dataset.SafePositionReturnDate
        return None

    @SafePositionReturnDate.setter
    def SafePositionReturnDate(self, value: Optional[str]):
        if value is None:
            if "SafePositionReturnDate" in self._dataset:
                del self._dataset.SafePositionReturnDate
        else:
            self._dataset.SafePositionReturnDate = value

    @property
    def SafePositionReturnTime(self) -> Optional[str]:
        if "SafePositionReturnTime" in self._dataset:
            return self._dataset.SafePositionReturnTime
        return None

    @SafePositionReturnTime.setter
    def SafePositionReturnTime(self, value: Optional[str]):
        if value is None:
            if "SafePositionReturnTime" in self._dataset:
                del self._dataset.SafePositionReturnTime
        else:
            self._dataset.SafePositionReturnTime = value

    @property
    def PulseSpecificBrachyControlPointDeliveredSequence(
        self,
    ) -> Optional[List[PulseSpecificBrachyControlPointDeliveredSequenceItem]]:
        if "PulseSpecificBrachyControlPointDeliveredSequence" in self._dataset:
            if len(self._PulseSpecificBrachyControlPointDeliveredSequence) == len(
                self._dataset.PulseSpecificBrachyControlPointDeliveredSequence
            ):
                return self._PulseSpecificBrachyControlPointDeliveredSequence
            else:
                return [
                    PulseSpecificBrachyControlPointDeliveredSequenceItem(x)
                    for x in self._dataset.PulseSpecificBrachyControlPointDeliveredSequence
                ]
        return None

    @PulseSpecificBrachyControlPointDeliveredSequence.setter
    def PulseSpecificBrachyControlPointDeliveredSequence(
        self, value: Optional[List[PulseSpecificBrachyControlPointDeliveredSequenceItem]]
    ):
        if value is None:
            self._PulseSpecificBrachyControlPointDeliveredSequence = []
            if "PulseSpecificBrachyControlPointDeliveredSequence" in self._dataset:
                del self._dataset.PulseSpecificBrachyControlPointDeliveredSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, PulseSpecificBrachyControlPointDeliveredSequenceItem) for item in value
        ):
            raise ValueError(
                f"PulseSpecificBrachyControlPointDeliveredSequence must be a list of PulseSpecificBrachyControlPointDeliveredSequenceItem objects"
            )
        else:
            self._PulseSpecificBrachyControlPointDeliveredSequence = value
            if "PulseSpecificBrachyControlPointDeliveredSequence" not in self._dataset:
                self._dataset.PulseSpecificBrachyControlPointDeliveredSequence = pydicom.Sequence()
            self._dataset.PulseSpecificBrachyControlPointDeliveredSequence.clear()
            self._dataset.PulseSpecificBrachyControlPointDeliveredSequence.extend([item.to_dataset() for item in value])

    def add_PulseSpecificBrachyControlPointDelivered(self, item: PulseSpecificBrachyControlPointDeliveredSequenceItem):
        if not isinstance(item, PulseSpecificBrachyControlPointDeliveredSequenceItem):
            raise ValueError(f"Item must be an instance of PulseSpecificBrachyControlPointDeliveredSequenceItem")
        self._PulseSpecificBrachyControlPointDeliveredSequence.append(item)
        if "PulseSpecificBrachyControlPointDeliveredSequence" not in self._dataset:
            self._dataset.PulseSpecificBrachyControlPointDeliveredSequence = pydicom.Sequence()
        self._dataset.PulseSpecificBrachyControlPointDeliveredSequence.append(item.to_dataset())

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
    def ChannelEffectiveLength(self) -> Optional[Decimal]:
        if "ChannelEffectiveLength" in self._dataset:
            return self._dataset.ChannelEffectiveLength
        return None

    @ChannelEffectiveLength.setter
    def ChannelEffectiveLength(self, value: Optional[Decimal]):
        if value is None:
            if "ChannelEffectiveLength" in self._dataset:
                del self._dataset.ChannelEffectiveLength
        else:
            self._dataset.ChannelEffectiveLength = value

    @property
    def ChannelInnerLength(self) -> Optional[Decimal]:
        if "ChannelInnerLength" in self._dataset:
            return self._dataset.ChannelInnerLength
        return None

    @ChannelInnerLength.setter
    def ChannelInnerLength(self, value: Optional[Decimal]):
        if value is None:
            if "ChannelInnerLength" in self._dataset:
                del self._dataset.ChannelInnerLength
        else:
            self._dataset.ChannelInnerLength = value

    @property
    def AfterloaderChannelID(self) -> Optional[str]:
        if "AfterloaderChannelID" in self._dataset:
            return self._dataset.AfterloaderChannelID
        return None

    @AfterloaderChannelID.setter
    def AfterloaderChannelID(self, value: Optional[str]):
        if value is None:
            if "AfterloaderChannelID" in self._dataset:
                del self._dataset.AfterloaderChannelID
        else:
            self._dataset.AfterloaderChannelID = value

    @property
    def ChannelNumber(self) -> Optional[int]:
        if "ChannelNumber" in self._dataset:
            return self._dataset.ChannelNumber
        return None

    @ChannelNumber.setter
    def ChannelNumber(self, value: Optional[int]):
        if value is None:
            if "ChannelNumber" in self._dataset:
                del self._dataset.ChannelNumber
        else:
            self._dataset.ChannelNumber = value

    @property
    def ChannelLength(self) -> Optional[Decimal]:
        if "ChannelLength" in self._dataset:
            return self._dataset.ChannelLength
        return None

    @ChannelLength.setter
    def ChannelLength(self, value: Optional[Decimal]):
        if value is None:
            if "ChannelLength" in self._dataset:
                del self._dataset.ChannelLength
        else:
            self._dataset.ChannelLength = value

    @property
    def SourceMovementType(self) -> Optional[str]:
        if "SourceMovementType" in self._dataset:
            return self._dataset.SourceMovementType
        return None

    @SourceMovementType.setter
    def SourceMovementType(self, value: Optional[str]):
        if value is None:
            if "SourceMovementType" in self._dataset:
                del self._dataset.SourceMovementType
        else:
            self._dataset.SourceMovementType = value

    @property
    def TransferTubeNumber(self) -> Optional[int]:
        if "TransferTubeNumber" in self._dataset:
            return self._dataset.TransferTubeNumber
        return None

    @TransferTubeNumber.setter
    def TransferTubeNumber(self, value: Optional[int]):
        if value is None:
            if "TransferTubeNumber" in self._dataset:
                del self._dataset.TransferTubeNumber
        else:
            self._dataset.TransferTubeNumber = value

    @property
    def TransferTubeLength(self) -> Optional[Decimal]:
        if "TransferTubeLength" in self._dataset:
            return self._dataset.TransferTubeLength
        return None

    @TransferTubeLength.setter
    def TransferTubeLength(self, value: Optional[Decimal]):
        if value is None:
            if "TransferTubeLength" in self._dataset:
                del self._dataset.TransferTubeLength
        else:
            self._dataset.TransferTubeLength = value

    @property
    def ReferencedSourceNumber(self) -> Optional[int]:
        if "ReferencedSourceNumber" in self._dataset:
            return self._dataset.ReferencedSourceNumber
        return None

    @ReferencedSourceNumber.setter
    def ReferencedSourceNumber(self, value: Optional[int]):
        if value is None:
            if "ReferencedSourceNumber" in self._dataset:
                del self._dataset.ReferencedSourceNumber
        else:
            self._dataset.ReferencedSourceNumber = value
