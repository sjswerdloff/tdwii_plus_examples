from typing import Any, List, Optional

import pydicom


class FrameDisplaySequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def StartTrim(self) -> Optional[int]:
        if "StartTrim" in self._dataset:
            return self._dataset.StartTrim
        return None

    @StartTrim.setter
    def StartTrim(self, value: Optional[int]):
        if value is None:
            if "StartTrim" in self._dataset:
                del self._dataset.StartTrim
        else:
            self._dataset.StartTrim = value

    @property
    def StopTrim(self) -> Optional[int]:
        if "StopTrim" in self._dataset:
            return self._dataset.StopTrim
        return None

    @StopTrim.setter
    def StopTrim(self, value: Optional[int]):
        if value is None:
            if "StopTrim" in self._dataset:
                del self._dataset.StopTrim
        else:
            self._dataset.StopTrim = value

    @property
    def RecommendedDisplayFrameRateInFloat(self) -> Optional[float]:
        if "RecommendedDisplayFrameRateInFloat" in self._dataset:
            return self._dataset.RecommendedDisplayFrameRateInFloat
        return None

    @RecommendedDisplayFrameRateInFloat.setter
    def RecommendedDisplayFrameRateInFloat(self, value: Optional[float]):
        if value is None:
            if "RecommendedDisplayFrameRateInFloat" in self._dataset:
                del self._dataset.RecommendedDisplayFrameRateInFloat
        else:
            self._dataset.RecommendedDisplayFrameRateInFloat = value

    @property
    def SkipFrameRangeFlag(self) -> Optional[str]:
        if "SkipFrameRangeFlag" in self._dataset:
            return self._dataset.SkipFrameRangeFlag
        return None

    @SkipFrameRangeFlag.setter
    def SkipFrameRangeFlag(self, value: Optional[str]):
        if value is None:
            if "SkipFrameRangeFlag" in self._dataset:
                del self._dataset.SkipFrameRangeFlag
        else:
            self._dataset.SkipFrameRangeFlag = value

    @property
    def RecommendedViewingMode(self) -> Optional[str]:
        if "RecommendedViewingMode" in self._dataset:
            return self._dataset.RecommendedViewingMode
        return None

    @RecommendedViewingMode.setter
    def RecommendedViewingMode(self, value: Optional[str]):
        if value is None:
            if "RecommendedViewingMode" in self._dataset:
                del self._dataset.RecommendedViewingMode
        else:
            self._dataset.RecommendedViewingMode = value

    @property
    def DisplayFilterPercentage(self) -> Optional[float]:
        if "DisplayFilterPercentage" in self._dataset:
            return self._dataset.DisplayFilterPercentage
        return None

    @DisplayFilterPercentage.setter
    def DisplayFilterPercentage(self, value: Optional[float]):
        if value is None:
            if "DisplayFilterPercentage" in self._dataset:
                del self._dataset.DisplayFilterPercentage
        else:
            self._dataset.DisplayFilterPercentage = value

    @property
    def MaskVisibilityPercentage(self) -> Optional[float]:
        if "MaskVisibilityPercentage" in self._dataset:
            return self._dataset.MaskVisibilityPercentage
        return None

    @MaskVisibilityPercentage.setter
    def MaskVisibilityPercentage(self, value: Optional[float]):
        if value is None:
            if "MaskVisibilityPercentage" in self._dataset:
                del self._dataset.MaskVisibilityPercentage
        else:
            self._dataset.MaskVisibilityPercentage = value
