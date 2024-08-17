from typing import Any, List, Optional

import pydicom


class FrameContentSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def FrameAcquisitionDateTime(self) -> Optional[str]:
        if "FrameAcquisitionDateTime" in self._dataset:
            return self._dataset.FrameAcquisitionDateTime
        return None

    @FrameAcquisitionDateTime.setter
    def FrameAcquisitionDateTime(self, value: Optional[str]):
        if value is None:
            if "FrameAcquisitionDateTime" in self._dataset:
                del self._dataset.FrameAcquisitionDateTime
        else:
            self._dataset.FrameAcquisitionDateTime = value

    @property
    def FrameReferenceDateTime(self) -> Optional[str]:
        if "FrameReferenceDateTime" in self._dataset:
            return self._dataset.FrameReferenceDateTime
        return None

    @FrameReferenceDateTime.setter
    def FrameReferenceDateTime(self, value: Optional[str]):
        if value is None:
            if "FrameReferenceDateTime" in self._dataset:
                del self._dataset.FrameReferenceDateTime
        else:
            self._dataset.FrameReferenceDateTime = value

    @property
    def RespiratoryCyclePosition(self) -> Optional[str]:
        if "RespiratoryCyclePosition" in self._dataset:
            return self._dataset.RespiratoryCyclePosition
        return None

    @RespiratoryCyclePosition.setter
    def RespiratoryCyclePosition(self, value: Optional[str]):
        if value is None:
            if "RespiratoryCyclePosition" in self._dataset:
                del self._dataset.RespiratoryCyclePosition
        else:
            self._dataset.RespiratoryCyclePosition = value

    @property
    def FrameAcquisitionDuration(self) -> Optional[float]:
        if "FrameAcquisitionDuration" in self._dataset:
            return self._dataset.FrameAcquisitionDuration
        return None

    @FrameAcquisitionDuration.setter
    def FrameAcquisitionDuration(self, value: Optional[float]):
        if value is None:
            if "FrameAcquisitionDuration" in self._dataset:
                del self._dataset.FrameAcquisitionDuration
        else:
            self._dataset.FrameAcquisitionDuration = value

    @property
    def CardiacCyclePosition(self) -> Optional[str]:
        if "CardiacCyclePosition" in self._dataset:
            return self._dataset.CardiacCyclePosition
        return None

    @CardiacCyclePosition.setter
    def CardiacCyclePosition(self, value: Optional[str]):
        if value is None:
            if "CardiacCyclePosition" in self._dataset:
                del self._dataset.CardiacCyclePosition
        else:
            self._dataset.CardiacCyclePosition = value

    @property
    def StackID(self) -> Optional[str]:
        if "StackID" in self._dataset:
            return self._dataset.StackID
        return None

    @StackID.setter
    def StackID(self, value: Optional[str]):
        if value is None:
            if "StackID" in self._dataset:
                del self._dataset.StackID
        else:
            self._dataset.StackID = value

    @property
    def InStackPositionNumber(self) -> Optional[int]:
        if "InStackPositionNumber" in self._dataset:
            return self._dataset.InStackPositionNumber
        return None

    @InStackPositionNumber.setter
    def InStackPositionNumber(self, value: Optional[int]):
        if value is None:
            if "InStackPositionNumber" in self._dataset:
                del self._dataset.InStackPositionNumber
        else:
            self._dataset.InStackPositionNumber = value

    @property
    def TemporalPositionIndex(self) -> Optional[int]:
        if "TemporalPositionIndex" in self._dataset:
            return self._dataset.TemporalPositionIndex
        return None

    @TemporalPositionIndex.setter
    def TemporalPositionIndex(self, value: Optional[int]):
        if value is None:
            if "TemporalPositionIndex" in self._dataset:
                del self._dataset.TemporalPositionIndex
        else:
            self._dataset.TemporalPositionIndex = value

    @property
    def FrameAcquisitionNumber(self) -> Optional[int]:
        if "FrameAcquisitionNumber" in self._dataset:
            return self._dataset.FrameAcquisitionNumber
        return None

    @FrameAcquisitionNumber.setter
    def FrameAcquisitionNumber(self, value: Optional[int]):
        if value is None:
            if "FrameAcquisitionNumber" in self._dataset:
                del self._dataset.FrameAcquisitionNumber
        else:
            self._dataset.FrameAcquisitionNumber = value

    @property
    def DimensionIndexValues(self) -> Optional[List[int]]:
        if "DimensionIndexValues" in self._dataset:
            return self._dataset.DimensionIndexValues
        return None

    @DimensionIndexValues.setter
    def DimensionIndexValues(self, value: Optional[List[int]]):
        if value is None:
            if "DimensionIndexValues" in self._dataset:
                del self._dataset.DimensionIndexValues
        else:
            self._dataset.DimensionIndexValues = value

    @property
    def FrameComments(self) -> Optional[str]:
        if "FrameComments" in self._dataset:
            return self._dataset.FrameComments
        return None

    @FrameComments.setter
    def FrameComments(self, value: Optional[str]):
        if value is None:
            if "FrameComments" in self._dataset:
                del self._dataset.FrameComments
        else:
            self._dataset.FrameComments = value

    @property
    def FrameLabel(self) -> Optional[str]:
        if "FrameLabel" in self._dataset:
            return self._dataset.FrameLabel
        return None

    @FrameLabel.setter
    def FrameLabel(self, value: Optional[str]):
        if value is None:
            if "FrameLabel" in self._dataset:
                del self._dataset.FrameLabel
        else:
            self._dataset.FrameLabel = value
