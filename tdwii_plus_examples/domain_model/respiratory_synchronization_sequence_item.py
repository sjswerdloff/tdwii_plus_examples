from typing import Any, List, Optional  # noqa

import pydicom


class RespiratorySynchronizationSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def NominalPercentageOfRespiratoryPhase(self) -> Optional[float]:
        if "NominalPercentageOfRespiratoryPhase" in self._dataset:
            return self._dataset.NominalPercentageOfRespiratoryPhase
        return None

    @NominalPercentageOfRespiratoryPhase.setter
    def NominalPercentageOfRespiratoryPhase(self, value: Optional[float]):
        if value is None:
            if "NominalPercentageOfRespiratoryPhase" in self._dataset:
                del self._dataset.NominalPercentageOfRespiratoryPhase
        else:
            self._dataset.NominalPercentageOfRespiratoryPhase = value

    @property
    def StartingRespiratoryAmplitude(self) -> Optional[float]:
        if "StartingRespiratoryAmplitude" in self._dataset:
            return self._dataset.StartingRespiratoryAmplitude
        return None

    @StartingRespiratoryAmplitude.setter
    def StartingRespiratoryAmplitude(self, value: Optional[float]):
        if value is None:
            if "StartingRespiratoryAmplitude" in self._dataset:
                del self._dataset.StartingRespiratoryAmplitude
        else:
            self._dataset.StartingRespiratoryAmplitude = value

    @property
    def StartingRespiratoryPhase(self) -> Optional[str]:
        if "StartingRespiratoryPhase" in self._dataset:
            return self._dataset.StartingRespiratoryPhase
        return None

    @StartingRespiratoryPhase.setter
    def StartingRespiratoryPhase(self, value: Optional[str]):
        if value is None:
            if "StartingRespiratoryPhase" in self._dataset:
                del self._dataset.StartingRespiratoryPhase
        else:
            self._dataset.StartingRespiratoryPhase = value

    @property
    def EndingRespiratoryAmplitude(self) -> Optional[float]:
        if "EndingRespiratoryAmplitude" in self._dataset:
            return self._dataset.EndingRespiratoryAmplitude
        return None

    @EndingRespiratoryAmplitude.setter
    def EndingRespiratoryAmplitude(self, value: Optional[float]):
        if value is None:
            if "EndingRespiratoryAmplitude" in self._dataset:
                del self._dataset.EndingRespiratoryAmplitude
        else:
            self._dataset.EndingRespiratoryAmplitude = value

    @property
    def EndingRespiratoryPhase(self) -> Optional[str]:
        if "EndingRespiratoryPhase" in self._dataset:
            return self._dataset.EndingRespiratoryPhase
        return None

    @EndingRespiratoryPhase.setter
    def EndingRespiratoryPhase(self, value: Optional[str]):
        if value is None:
            if "EndingRespiratoryPhase" in self._dataset:
                del self._dataset.EndingRespiratoryPhase
        else:
            self._dataset.EndingRespiratoryPhase = value

    @property
    def RespiratoryIntervalTime(self) -> Optional[float]:
        if "RespiratoryIntervalTime" in self._dataset:
            return self._dataset.RespiratoryIntervalTime
        return None

    @RespiratoryIntervalTime.setter
    def RespiratoryIntervalTime(self, value: Optional[float]):
        if value is None:
            if "RespiratoryIntervalTime" in self._dataset:
                del self._dataset.RespiratoryIntervalTime
        else:
            self._dataset.RespiratoryIntervalTime = value

    @property
    def NominalRespiratoryTriggerDelayTime(self) -> Optional[float]:
        if "NominalRespiratoryTriggerDelayTime" in self._dataset:
            return self._dataset.NominalRespiratoryTriggerDelayTime
        return None

    @NominalRespiratoryTriggerDelayTime.setter
    def NominalRespiratoryTriggerDelayTime(self, value: Optional[float]):
        if value is None:
            if "NominalRespiratoryTriggerDelayTime" in self._dataset:
                del self._dataset.NominalRespiratoryTriggerDelayTime
        else:
            self._dataset.NominalRespiratoryTriggerDelayTime = value

    @property
    def ActualRespiratoryTriggerDelayTime(self) -> Optional[float]:
        if "ActualRespiratoryTriggerDelayTime" in self._dataset:
            return self._dataset.ActualRespiratoryTriggerDelayTime
        return None

    @ActualRespiratoryTriggerDelayTime.setter
    def ActualRespiratoryTriggerDelayTime(self, value: Optional[float]):
        if value is None:
            if "ActualRespiratoryTriggerDelayTime" in self._dataset:
                del self._dataset.ActualRespiratoryTriggerDelayTime
        else:
            self._dataset.ActualRespiratoryTriggerDelayTime = value
