from typing import Any, List, Optional  # noqa

import pydicom


class PhaseInformationSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ActualFrameDuration(self) -> Optional[int]:
        if "ActualFrameDuration" in self._dataset:
            return self._dataset.ActualFrameDuration
        return None

    @ActualFrameDuration.setter
    def ActualFrameDuration(self, value: Optional[int]):
        if value is None:
            if "ActualFrameDuration" in self._dataset:
                del self._dataset.ActualFrameDuration
        else:
            self._dataset.ActualFrameDuration = value

    @property
    def NumberOfFramesInPhase(self) -> Optional[int]:
        if "NumberOfFramesInPhase" in self._dataset:
            return self._dataset.NumberOfFramesInPhase
        return None

    @NumberOfFramesInPhase.setter
    def NumberOfFramesInPhase(self, value: Optional[int]):
        if value is None:
            if "NumberOfFramesInPhase" in self._dataset:
                del self._dataset.NumberOfFramesInPhase
        else:
            self._dataset.NumberOfFramesInPhase = value

    @property
    def PhaseDelay(self) -> Optional[int]:
        if "PhaseDelay" in self._dataset:
            return self._dataset.PhaseDelay
        return None

    @PhaseDelay.setter
    def PhaseDelay(self, value: Optional[int]):
        if value is None:
            if "PhaseDelay" in self._dataset:
                del self._dataset.PhaseDelay
        else:
            self._dataset.PhaseDelay = value

    @property
    def PauseBetweenFrames(self) -> Optional[int]:
        if "PauseBetweenFrames" in self._dataset:
            return self._dataset.PauseBetweenFrames
        return None

    @PauseBetweenFrames.setter
    def PauseBetweenFrames(self, value: Optional[int]):
        if value is None:
            if "PauseBetweenFrames" in self._dataset:
                del self._dataset.PauseBetweenFrames
        else:
            self._dataset.PauseBetweenFrames = value

    @property
    def PhaseDescription(self) -> Optional[str]:
        if "PhaseDescription" in self._dataset:
            return self._dataset.PhaseDescription
        return None

    @PhaseDescription.setter
    def PhaseDescription(self, value: Optional[str]):
        if value is None:
            if "PhaseDescription" in self._dataset:
                del self._dataset.PhaseDescription
        else:
            self._dataset.PhaseDescription = value

    @property
    def TriggerVector(self) -> Optional[List[int]]:
        if "TriggerVector" in self._dataset:
            return self._dataset.TriggerVector
        return None

    @TriggerVector.setter
    def TriggerVector(self, value: Optional[List[int]]):
        if value is None:
            if "TriggerVector" in self._dataset:
                del self._dataset.TriggerVector
        else:
            self._dataset.TriggerVector = value

    @property
    def NumberOfTriggersInPhase(self) -> Optional[int]:
        if "NumberOfTriggersInPhase" in self._dataset:
            return self._dataset.NumberOfTriggersInPhase
        return None

    @NumberOfTriggersInPhase.setter
    def NumberOfTriggersInPhase(self, value: Optional[int]):
        if value is None:
            if "NumberOfTriggersInPhase" in self._dataset:
                del self._dataset.NumberOfTriggersInPhase
        else:
            self._dataset.NumberOfTriggersInPhase = value
