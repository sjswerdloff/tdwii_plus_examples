from decimal import Decimal
from typing import Any, List, Optional  # noqa

import pydicom

from .operating_mode_sequence_item import OperatingModeSequenceItem
from .specific_absorption_rate_sequence_item import SpecificAbsorptionRateSequenceItem


class MRTimingAndRelatedParametersSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._OperatingModeSequence: List[OperatingModeSequenceItem] = []
        self._SpecificAbsorptionRateSequence: List[SpecificAbsorptionRateSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def RepetitionTime(self) -> Optional[Decimal]:
        if "RepetitionTime" in self._dataset:
            return self._dataset.RepetitionTime
        return None

    @RepetitionTime.setter
    def RepetitionTime(self, value: Optional[Decimal]):
        if value is None:
            if "RepetitionTime" in self._dataset:
                del self._dataset.RepetitionTime
        else:
            self._dataset.RepetitionTime = value

    @property
    def EchoTrainLength(self) -> Optional[int]:
        if "EchoTrainLength" in self._dataset:
            return self._dataset.EchoTrainLength
        return None

    @EchoTrainLength.setter
    def EchoTrainLength(self, value: Optional[int]):
        if value is None:
            if "EchoTrainLength" in self._dataset:
                del self._dataset.EchoTrainLength
        else:
            self._dataset.EchoTrainLength = value

    @property
    def FlipAngle(self) -> Optional[Decimal]:
        if "FlipAngle" in self._dataset:
            return self._dataset.FlipAngle
        return None

    @FlipAngle.setter
    def FlipAngle(self, value: Optional[Decimal]):
        if value is None:
            if "FlipAngle" in self._dataset:
                del self._dataset.FlipAngle
        else:
            self._dataset.FlipAngle = value

    @property
    def OperatingModeSequence(self) -> Optional[List[OperatingModeSequenceItem]]:
        if "OperatingModeSequence" in self._dataset:
            if len(self._OperatingModeSequence) == len(self._dataset.OperatingModeSequence):
                return self._OperatingModeSequence
            else:
                return [OperatingModeSequenceItem(x) for x in self._dataset.OperatingModeSequence]
        return None

    @OperatingModeSequence.setter
    def OperatingModeSequence(self, value: Optional[List[OperatingModeSequenceItem]]):
        if value is None:
            self._OperatingModeSequence = []
            if "OperatingModeSequence" in self._dataset:
                del self._dataset.OperatingModeSequence
        elif not isinstance(value, list) or not all(isinstance(item, OperatingModeSequenceItem) for item in value):
            raise ValueError("OperatingModeSequence must be a list of OperatingModeSequenceItem objects")
        else:
            self._OperatingModeSequence = value
            if "OperatingModeSequence" not in self._dataset:
                self._dataset.OperatingModeSequence = pydicom.Sequence()
            self._dataset.OperatingModeSequence.clear()
            self._dataset.OperatingModeSequence.extend([item.to_dataset() for item in value])

    def add_OperatingMode(self, item: OperatingModeSequenceItem):
        if not isinstance(item, OperatingModeSequenceItem):
            raise ValueError("Item must be an instance of OperatingModeSequenceItem")
        self._OperatingModeSequence.append(item)
        if "OperatingModeSequence" not in self._dataset:
            self._dataset.OperatingModeSequence = pydicom.Sequence()
        self._dataset.OperatingModeSequence.append(item.to_dataset())

    @property
    def GradientOutputType(self) -> Optional[str]:
        if "GradientOutputType" in self._dataset:
            return self._dataset.GradientOutputType
        return None

    @GradientOutputType.setter
    def GradientOutputType(self, value: Optional[str]):
        if value is None:
            if "GradientOutputType" in self._dataset:
                del self._dataset.GradientOutputType
        else:
            self._dataset.GradientOutputType = value

    @property
    def GradientOutput(self) -> Optional[float]:
        if "GradientOutput" in self._dataset:
            return self._dataset.GradientOutput
        return None

    @GradientOutput.setter
    def GradientOutput(self, value: Optional[float]):
        if value is None:
            if "GradientOutput" in self._dataset:
                del self._dataset.GradientOutput
        else:
            self._dataset.GradientOutput = value

    @property
    def SpecificAbsorptionRateSequence(self) -> Optional[List[SpecificAbsorptionRateSequenceItem]]:
        if "SpecificAbsorptionRateSequence" in self._dataset:
            if len(self._SpecificAbsorptionRateSequence) == len(self._dataset.SpecificAbsorptionRateSequence):
                return self._SpecificAbsorptionRateSequence
            else:
                return [SpecificAbsorptionRateSequenceItem(x) for x in self._dataset.SpecificAbsorptionRateSequence]
        return None

    @SpecificAbsorptionRateSequence.setter
    def SpecificAbsorptionRateSequence(self, value: Optional[List[SpecificAbsorptionRateSequenceItem]]):
        if value is None:
            self._SpecificAbsorptionRateSequence = []
            if "SpecificAbsorptionRateSequence" in self._dataset:
                del self._dataset.SpecificAbsorptionRateSequence
        elif not isinstance(value, list) or not all(isinstance(item, SpecificAbsorptionRateSequenceItem) for item in value):
            raise ValueError("SpecificAbsorptionRateSequence must be a list of SpecificAbsorptionRateSequenceItem objects")
        else:
            self._SpecificAbsorptionRateSequence = value
            if "SpecificAbsorptionRateSequence" not in self._dataset:
                self._dataset.SpecificAbsorptionRateSequence = pydicom.Sequence()
            self._dataset.SpecificAbsorptionRateSequence.clear()
            self._dataset.SpecificAbsorptionRateSequence.extend([item.to_dataset() for item in value])

    def add_SpecificAbsorptionRate(self, item: SpecificAbsorptionRateSequenceItem):
        if not isinstance(item, SpecificAbsorptionRateSequenceItem):
            raise ValueError("Item must be an instance of SpecificAbsorptionRateSequenceItem")
        self._SpecificAbsorptionRateSequence.append(item)
        if "SpecificAbsorptionRateSequence" not in self._dataset:
            self._dataset.SpecificAbsorptionRateSequence = pydicom.Sequence()
        self._dataset.SpecificAbsorptionRateSequence.append(item.to_dataset())

    @property
    def RFEchoTrainLength(self) -> Optional[int]:
        if "RFEchoTrainLength" in self._dataset:
            return self._dataset.RFEchoTrainLength
        return None

    @RFEchoTrainLength.setter
    def RFEchoTrainLength(self, value: Optional[int]):
        if value is None:
            if "RFEchoTrainLength" in self._dataset:
                del self._dataset.RFEchoTrainLength
        else:
            self._dataset.RFEchoTrainLength = value

    @property
    def GradientEchoTrainLength(self) -> Optional[int]:
        if "GradientEchoTrainLength" in self._dataset:
            return self._dataset.GradientEchoTrainLength
        return None

    @GradientEchoTrainLength.setter
    def GradientEchoTrainLength(self, value: Optional[int]):
        if value is None:
            if "GradientEchoTrainLength" in self._dataset:
                del self._dataset.GradientEchoTrainLength
        else:
            self._dataset.GradientEchoTrainLength = value
