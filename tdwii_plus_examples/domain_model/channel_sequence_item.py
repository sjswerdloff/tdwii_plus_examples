from decimal import Decimal
from typing import Any, List, Optional

import pydicom

from .brachy_control_point_sequence_item import BrachyControlPointSequenceItem
from .channel_shield_sequence_item import ChannelShieldSequenceItem


class ChannelSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._ChannelShieldSequence: List[ChannelShieldSequenceItem] = []
        self._BrachyControlPointSequence: List[BrachyControlPointSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ReferencedROINumber(self) -> Optional[int]:
        if "ReferencedROINumber" in self._dataset:
            return self._dataset.ReferencedROINumber
        return None

    @ReferencedROINumber.setter
    def ReferencedROINumber(self, value: Optional[int]):
        if value is None:
            if "ReferencedROINumber" in self._dataset:
                del self._dataset.ReferencedROINumber
        else:
            self._dataset.ReferencedROINumber = value

    @property
    def MaterialID(self) -> Optional[str]:
        if "MaterialID" in self._dataset:
            return self._dataset.MaterialID
        return None

    @MaterialID.setter
    def MaterialID(self, value: Optional[str]):
        if value is None:
            if "MaterialID" in self._dataset:
                del self._dataset.MaterialID
        else:
            self._dataset.MaterialID = value

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
    def SourceApplicatorTipLength(self) -> Optional[Decimal]:
        if "SourceApplicatorTipLength" in self._dataset:
            return self._dataset.SourceApplicatorTipLength
        return None

    @SourceApplicatorTipLength.setter
    def SourceApplicatorTipLength(self, value: Optional[Decimal]):
        if value is None:
            if "SourceApplicatorTipLength" in self._dataset:
                del self._dataset.SourceApplicatorTipLength
        else:
            self._dataset.SourceApplicatorTipLength = value

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
    def ChannelTotalTime(self) -> Optional[Decimal]:
        if "ChannelTotalTime" in self._dataset:
            return self._dataset.ChannelTotalTime
        return None

    @ChannelTotalTime.setter
    def ChannelTotalTime(self, value: Optional[Decimal]):
        if value is None:
            if "ChannelTotalTime" in self._dataset:
                del self._dataset.ChannelTotalTime
        else:
            self._dataset.ChannelTotalTime = value

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
    def NumberOfPulses(self) -> Optional[int]:
        if "NumberOfPulses" in self._dataset:
            return self._dataset.NumberOfPulses
        return None

    @NumberOfPulses.setter
    def NumberOfPulses(self, value: Optional[int]):
        if value is None:
            if "NumberOfPulses" in self._dataset:
                del self._dataset.NumberOfPulses
        else:
            self._dataset.NumberOfPulses = value

    @property
    def PulseRepetitionInterval(self) -> Optional[Decimal]:
        if "PulseRepetitionInterval" in self._dataset:
            return self._dataset.PulseRepetitionInterval
        return None

    @PulseRepetitionInterval.setter
    def PulseRepetitionInterval(self, value: Optional[Decimal]):
        if value is None:
            if "PulseRepetitionInterval" in self._dataset:
                del self._dataset.PulseRepetitionInterval
        else:
            self._dataset.PulseRepetitionInterval = value

    @property
    def SourceApplicatorNumber(self) -> Optional[int]:
        if "SourceApplicatorNumber" in self._dataset:
            return self._dataset.SourceApplicatorNumber
        return None

    @SourceApplicatorNumber.setter
    def SourceApplicatorNumber(self, value: Optional[int]):
        if value is None:
            if "SourceApplicatorNumber" in self._dataset:
                del self._dataset.SourceApplicatorNumber
        else:
            self._dataset.SourceApplicatorNumber = value

    @property
    def SourceApplicatorID(self) -> Optional[str]:
        if "SourceApplicatorID" in self._dataset:
            return self._dataset.SourceApplicatorID
        return None

    @SourceApplicatorID.setter
    def SourceApplicatorID(self, value: Optional[str]):
        if value is None:
            if "SourceApplicatorID" in self._dataset:
                del self._dataset.SourceApplicatorID
        else:
            self._dataset.SourceApplicatorID = value

    @property
    def SourceApplicatorType(self) -> Optional[str]:
        if "SourceApplicatorType" in self._dataset:
            return self._dataset.SourceApplicatorType
        return None

    @SourceApplicatorType.setter
    def SourceApplicatorType(self, value: Optional[str]):
        if value is None:
            if "SourceApplicatorType" in self._dataset:
                del self._dataset.SourceApplicatorType
        else:
            self._dataset.SourceApplicatorType = value

    @property
    def SourceApplicatorName(self) -> Optional[str]:
        if "SourceApplicatorName" in self._dataset:
            return self._dataset.SourceApplicatorName
        return None

    @SourceApplicatorName.setter
    def SourceApplicatorName(self, value: Optional[str]):
        if value is None:
            if "SourceApplicatorName" in self._dataset:
                del self._dataset.SourceApplicatorName
        else:
            self._dataset.SourceApplicatorName = value

    @property
    def SourceApplicatorLength(self) -> Optional[Decimal]:
        if "SourceApplicatorLength" in self._dataset:
            return self._dataset.SourceApplicatorLength
        return None

    @SourceApplicatorLength.setter
    def SourceApplicatorLength(self, value: Optional[Decimal]):
        if value is None:
            if "SourceApplicatorLength" in self._dataset:
                del self._dataset.SourceApplicatorLength
        else:
            self._dataset.SourceApplicatorLength = value

    @property
    def SourceApplicatorManufacturer(self) -> Optional[str]:
        if "SourceApplicatorManufacturer" in self._dataset:
            return self._dataset.SourceApplicatorManufacturer
        return None

    @SourceApplicatorManufacturer.setter
    def SourceApplicatorManufacturer(self, value: Optional[str]):
        if value is None:
            if "SourceApplicatorManufacturer" in self._dataset:
                del self._dataset.SourceApplicatorManufacturer
        else:
            self._dataset.SourceApplicatorManufacturer = value

    @property
    def SourceApplicatorWallNominalThickness(self) -> Optional[Decimal]:
        if "SourceApplicatorWallNominalThickness" in self._dataset:
            return self._dataset.SourceApplicatorWallNominalThickness
        return None

    @SourceApplicatorWallNominalThickness.setter
    def SourceApplicatorWallNominalThickness(self, value: Optional[Decimal]):
        if value is None:
            if "SourceApplicatorWallNominalThickness" in self._dataset:
                del self._dataset.SourceApplicatorWallNominalThickness
        else:
            self._dataset.SourceApplicatorWallNominalThickness = value

    @property
    def SourceApplicatorWallNominalTransmission(self) -> Optional[Decimal]:
        if "SourceApplicatorWallNominalTransmission" in self._dataset:
            return self._dataset.SourceApplicatorWallNominalTransmission
        return None

    @SourceApplicatorWallNominalTransmission.setter
    def SourceApplicatorWallNominalTransmission(self, value: Optional[Decimal]):
        if value is None:
            if "SourceApplicatorWallNominalTransmission" in self._dataset:
                del self._dataset.SourceApplicatorWallNominalTransmission
        else:
            self._dataset.SourceApplicatorWallNominalTransmission = value

    @property
    def SourceApplicatorStepSize(self) -> Optional[Decimal]:
        if "SourceApplicatorStepSize" in self._dataset:
            return self._dataset.SourceApplicatorStepSize
        return None

    @SourceApplicatorStepSize.setter
    def SourceApplicatorStepSize(self, value: Optional[Decimal]):
        if value is None:
            if "SourceApplicatorStepSize" in self._dataset:
                del self._dataset.SourceApplicatorStepSize
        else:
            self._dataset.SourceApplicatorStepSize = value

    @property
    def ApplicatorShapeReferencedROINumber(self) -> Optional[int]:
        if "ApplicatorShapeReferencedROINumber" in self._dataset:
            return self._dataset.ApplicatorShapeReferencedROINumber
        return None

    @ApplicatorShapeReferencedROINumber.setter
    def ApplicatorShapeReferencedROINumber(self, value: Optional[int]):
        if value is None:
            if "ApplicatorShapeReferencedROINumber" in self._dataset:
                del self._dataset.ApplicatorShapeReferencedROINumber
        else:
            self._dataset.ApplicatorShapeReferencedROINumber = value

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
    def ChannelShieldSequence(self) -> Optional[List[ChannelShieldSequenceItem]]:
        if "ChannelShieldSequence" in self._dataset:
            if len(self._ChannelShieldSequence) == len(self._dataset.ChannelShieldSequence):
                return self._ChannelShieldSequence
            else:
                return [ChannelShieldSequenceItem(x) for x in self._dataset.ChannelShieldSequence]
        return None

    @ChannelShieldSequence.setter
    def ChannelShieldSequence(self, value: Optional[List[ChannelShieldSequenceItem]]):
        if value is None:
            self._ChannelShieldSequence = []
            if "ChannelShieldSequence" in self._dataset:
                del self._dataset.ChannelShieldSequence
        elif not isinstance(value, list) or not all(isinstance(item, ChannelShieldSequenceItem) for item in value):
            raise ValueError(f"ChannelShieldSequence must be a list of ChannelShieldSequenceItem objects")
        else:
            self._ChannelShieldSequence = value
            if "ChannelShieldSequence" not in self._dataset:
                self._dataset.ChannelShieldSequence = pydicom.Sequence()
            self._dataset.ChannelShieldSequence.clear()
            self._dataset.ChannelShieldSequence.extend([item.to_dataset() for item in value])

    def add_ChannelShield(self, item: ChannelShieldSequenceItem):
        if not isinstance(item, ChannelShieldSequenceItem):
            raise ValueError(f"Item must be an instance of ChannelShieldSequenceItem")
        self._ChannelShieldSequence.append(item)
        if "ChannelShieldSequence" not in self._dataset:
            self._dataset.ChannelShieldSequence = pydicom.Sequence()
        self._dataset.ChannelShieldSequence.append(item.to_dataset())

    @property
    def FinalCumulativeTimeWeight(self) -> Optional[Decimal]:
        if "FinalCumulativeTimeWeight" in self._dataset:
            return self._dataset.FinalCumulativeTimeWeight
        return None

    @FinalCumulativeTimeWeight.setter
    def FinalCumulativeTimeWeight(self, value: Optional[Decimal]):
        if value is None:
            if "FinalCumulativeTimeWeight" in self._dataset:
                del self._dataset.FinalCumulativeTimeWeight
        else:
            self._dataset.FinalCumulativeTimeWeight = value

    @property
    def BrachyControlPointSequence(self) -> Optional[List[BrachyControlPointSequenceItem]]:
        if "BrachyControlPointSequence" in self._dataset:
            if len(self._BrachyControlPointSequence) == len(self._dataset.BrachyControlPointSequence):
                return self._BrachyControlPointSequence
            else:
                return [BrachyControlPointSequenceItem(x) for x in self._dataset.BrachyControlPointSequence]
        return None

    @BrachyControlPointSequence.setter
    def BrachyControlPointSequence(self, value: Optional[List[BrachyControlPointSequenceItem]]):
        if value is None:
            self._BrachyControlPointSequence = []
            if "BrachyControlPointSequence" in self._dataset:
                del self._dataset.BrachyControlPointSequence
        elif not isinstance(value, list) or not all(isinstance(item, BrachyControlPointSequenceItem) for item in value):
            raise ValueError(f"BrachyControlPointSequence must be a list of BrachyControlPointSequenceItem objects")
        else:
            self._BrachyControlPointSequence = value
            if "BrachyControlPointSequence" not in self._dataset:
                self._dataset.BrachyControlPointSequence = pydicom.Sequence()
            self._dataset.BrachyControlPointSequence.clear()
            self._dataset.BrachyControlPointSequence.extend([item.to_dataset() for item in value])

    def add_BrachyControlPoint(self, item: BrachyControlPointSequenceItem):
        if not isinstance(item, BrachyControlPointSequenceItem):
            raise ValueError(f"Item must be an instance of BrachyControlPointSequenceItem")
        self._BrachyControlPointSequence.append(item)
        if "BrachyControlPointSequence" not in self._dataset:
            self._dataset.BrachyControlPointSequence = pydicom.Sequence()
        self._dataset.BrachyControlPointSequence.append(item.to_dataset())

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
