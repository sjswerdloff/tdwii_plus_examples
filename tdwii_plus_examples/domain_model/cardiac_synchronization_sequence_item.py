from typing import Any, List, Optional

import pydicom


class CardiacSynchronizationSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def LowRRValue(self) -> Optional[int]:
        if "LowRRValue" in self._dataset:
            return self._dataset.LowRRValue
        return None

    @LowRRValue.setter
    def LowRRValue(self, value: Optional[int]):
        if value is None:
            if "LowRRValue" in self._dataset:
                del self._dataset.LowRRValue
        else:
            self._dataset.LowRRValue = value

    @property
    def HighRRValue(self) -> Optional[int]:
        if "HighRRValue" in self._dataset:
            return self._dataset.HighRRValue
        return None

    @HighRRValue.setter
    def HighRRValue(self, value: Optional[int]):
        if value is None:
            if "HighRRValue" in self._dataset:
                del self._dataset.HighRRValue
        else:
            self._dataset.HighRRValue = value

    @property
    def IntervalsAcquired(self) -> Optional[int]:
        if "IntervalsAcquired" in self._dataset:
            return self._dataset.IntervalsAcquired
        return None

    @IntervalsAcquired.setter
    def IntervalsAcquired(self, value: Optional[int]):
        if value is None:
            if "IntervalsAcquired" in self._dataset:
                del self._dataset.IntervalsAcquired
        else:
            self._dataset.IntervalsAcquired = value

    @property
    def IntervalsRejected(self) -> Optional[int]:
        if "IntervalsRejected" in self._dataset:
            return self._dataset.IntervalsRejected
        return None

    @IntervalsRejected.setter
    def IntervalsRejected(self, value: Optional[int]):
        if value is None:
            if "IntervalsRejected" in self._dataset:
                del self._dataset.IntervalsRejected
        else:
            self._dataset.IntervalsRejected = value

    @property
    def HeartRate(self) -> Optional[int]:
        if "HeartRate" in self._dataset:
            return self._dataset.HeartRate
        return None

    @HeartRate.setter
    def HeartRate(self, value: Optional[int]):
        if value is None:
            if "HeartRate" in self._dataset:
                del self._dataset.HeartRate
        else:
            self._dataset.HeartRate = value

    @property
    def NominalCardiacTriggerDelayTime(self) -> Optional[float]:
        if "NominalCardiacTriggerDelayTime" in self._dataset:
            return self._dataset.NominalCardiacTriggerDelayTime
        return None

    @NominalCardiacTriggerDelayTime.setter
    def NominalCardiacTriggerDelayTime(self, value: Optional[float]):
        if value is None:
            if "NominalCardiacTriggerDelayTime" in self._dataset:
                del self._dataset.NominalCardiacTriggerDelayTime
        else:
            self._dataset.NominalCardiacTriggerDelayTime = value

    @property
    def NominalCardiacTriggerTimePriorToRPeak(self) -> Optional[float]:
        if "NominalCardiacTriggerTimePriorToRPeak" in self._dataset:
            return self._dataset.NominalCardiacTriggerTimePriorToRPeak
        return None

    @NominalCardiacTriggerTimePriorToRPeak.setter
    def NominalCardiacTriggerTimePriorToRPeak(self, value: Optional[float]):
        if value is None:
            if "NominalCardiacTriggerTimePriorToRPeak" in self._dataset:
                del self._dataset.NominalCardiacTriggerTimePriorToRPeak
        else:
            self._dataset.NominalCardiacTriggerTimePriorToRPeak = value

    @property
    def ActualCardiacTriggerTimePriorToRPeak(self) -> Optional[float]:
        if "ActualCardiacTriggerTimePriorToRPeak" in self._dataset:
            return self._dataset.ActualCardiacTriggerTimePriorToRPeak
        return None

    @ActualCardiacTriggerTimePriorToRPeak.setter
    def ActualCardiacTriggerTimePriorToRPeak(self, value: Optional[float]):
        if value is None:
            if "ActualCardiacTriggerTimePriorToRPeak" in self._dataset:
                del self._dataset.ActualCardiacTriggerTimePriorToRPeak
        else:
            self._dataset.ActualCardiacTriggerTimePriorToRPeak = value

    @property
    def NominalPercentageOfCardiacPhase(self) -> Optional[float]:
        if "NominalPercentageOfCardiacPhase" in self._dataset:
            return self._dataset.NominalPercentageOfCardiacPhase
        return None

    @NominalPercentageOfCardiacPhase.setter
    def NominalPercentageOfCardiacPhase(self, value: Optional[float]):
        if value is None:
            if "NominalPercentageOfCardiacPhase" in self._dataset:
                del self._dataset.NominalPercentageOfCardiacPhase
        else:
            self._dataset.NominalPercentageOfCardiacPhase = value

    @property
    def RRIntervalTimeNominal(self) -> Optional[float]:
        if "RRIntervalTimeNominal" in self._dataset:
            return self._dataset.RRIntervalTimeNominal
        return None

    @RRIntervalTimeNominal.setter
    def RRIntervalTimeNominal(self, value: Optional[float]):
        if value is None:
            if "RRIntervalTimeNominal" in self._dataset:
                del self._dataset.RRIntervalTimeNominal
        else:
            self._dataset.RRIntervalTimeNominal = value

    @property
    def ActualCardiacTriggerDelayTime(self) -> Optional[float]:
        if "ActualCardiacTriggerDelayTime" in self._dataset:
            return self._dataset.ActualCardiacTriggerDelayTime
        return None

    @ActualCardiacTriggerDelayTime.setter
    def ActualCardiacTriggerDelayTime(self, value: Optional[float]):
        if value is None:
            if "ActualCardiacTriggerDelayTime" in self._dataset:
                del self._dataset.ActualCardiacTriggerDelayTime
        else:
            self._dataset.ActualCardiacTriggerDelayTime = value
