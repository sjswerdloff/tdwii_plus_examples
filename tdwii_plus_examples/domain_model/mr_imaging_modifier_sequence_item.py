from decimal import Decimal
from typing import Any, List, Optional  # noqa

import pydicom


class MRImagingModifierSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def PixelBandwidth(self) -> Optional[Decimal]:
        if "PixelBandwidth" in self._dataset:
            return self._dataset.PixelBandwidth
        return None

    @PixelBandwidth.setter
    def PixelBandwidth(self, value: Optional[Decimal]):
        if value is None:
            if "PixelBandwidth" in self._dataset:
                del self._dataset.PixelBandwidth
        else:
            self._dataset.PixelBandwidth = value

    @property
    def TagAngleFirstAxis(self) -> Optional[float]:
        if "TagAngleFirstAxis" in self._dataset:
            return self._dataset.TagAngleFirstAxis
        return None

    @TagAngleFirstAxis.setter
    def TagAngleFirstAxis(self, value: Optional[float]):
        if value is None:
            if "TagAngleFirstAxis" in self._dataset:
                del self._dataset.TagAngleFirstAxis
        else:
            self._dataset.TagAngleFirstAxis = value

    @property
    def MagnetizationTransfer(self) -> Optional[str]:
        if "MagnetizationTransfer" in self._dataset:
            return self._dataset.MagnetizationTransfer
        return None

    @MagnetizationTransfer.setter
    def MagnetizationTransfer(self, value: Optional[str]):
        if value is None:
            if "MagnetizationTransfer" in self._dataset:
                del self._dataset.MagnetizationTransfer
        else:
            self._dataset.MagnetizationTransfer = value

    @property
    def BloodSignalNulling(self) -> Optional[str]:
        if "BloodSignalNulling" in self._dataset:
            return self._dataset.BloodSignalNulling
        return None

    @BloodSignalNulling.setter
    def BloodSignalNulling(self, value: Optional[str]):
        if value is None:
            if "BloodSignalNulling" in self._dataset:
                del self._dataset.BloodSignalNulling
        else:
            self._dataset.BloodSignalNulling = value

    @property
    def Tagging(self) -> Optional[str]:
        if "Tagging" in self._dataset:
            return self._dataset.Tagging
        return None

    @Tagging.setter
    def Tagging(self, value: Optional[str]):
        if value is None:
            if "Tagging" in self._dataset:
                del self._dataset.Tagging
        else:
            self._dataset.Tagging = value

    @property
    def TagSpacingFirstDimension(self) -> Optional[float]:
        if "TagSpacingFirstDimension" in self._dataset:
            return self._dataset.TagSpacingFirstDimension
        return None

    @TagSpacingFirstDimension.setter
    def TagSpacingFirstDimension(self, value: Optional[float]):
        if value is None:
            if "TagSpacingFirstDimension" in self._dataset:
                del self._dataset.TagSpacingFirstDimension
        else:
            self._dataset.TagSpacingFirstDimension = value

    @property
    def TagThickness(self) -> Optional[float]:
        if "TagThickness" in self._dataset:
            return self._dataset.TagThickness
        return None

    @TagThickness.setter
    def TagThickness(self, value: Optional[float]):
        if value is None:
            if "TagThickness" in self._dataset:
                del self._dataset.TagThickness
        else:
            self._dataset.TagThickness = value

    @property
    def TransmitterFrequency(self) -> Optional[List[float]]:
        if "TransmitterFrequency" in self._dataset:
            return self._dataset.TransmitterFrequency
        return None

    @TransmitterFrequency.setter
    def TransmitterFrequency(self, value: Optional[List[float]]):
        if value is None:
            if "TransmitterFrequency" in self._dataset:
                del self._dataset.TransmitterFrequency
        else:
            self._dataset.TransmitterFrequency = value

    @property
    def TaggingDelay(self) -> Optional[float]:
        if "TaggingDelay" in self._dataset:
            return self._dataset.TaggingDelay
        return None

    @TaggingDelay.setter
    def TaggingDelay(self, value: Optional[float]):
        if value is None:
            if "TaggingDelay" in self._dataset:
                del self._dataset.TaggingDelay
        else:
            self._dataset.TaggingDelay = value

    @property
    def TagSpacingSecondDimension(self) -> Optional[float]:
        if "TagSpacingSecondDimension" in self._dataset:
            return self._dataset.TagSpacingSecondDimension
        return None

    @TagSpacingSecondDimension.setter
    def TagSpacingSecondDimension(self, value: Optional[float]):
        if value is None:
            if "TagSpacingSecondDimension" in self._dataset:
                del self._dataset.TagSpacingSecondDimension
        else:
            self._dataset.TagSpacingSecondDimension = value

    @property
    def TagAngleSecondAxis(self) -> Optional[int]:
        if "TagAngleSecondAxis" in self._dataset:
            return self._dataset.TagAngleSecondAxis
        return None

    @TagAngleSecondAxis.setter
    def TagAngleSecondAxis(self, value: Optional[int]):
        if value is None:
            if "TagAngleSecondAxis" in self._dataset:
                del self._dataset.TagAngleSecondAxis
        else:
            self._dataset.TagAngleSecondAxis = value
