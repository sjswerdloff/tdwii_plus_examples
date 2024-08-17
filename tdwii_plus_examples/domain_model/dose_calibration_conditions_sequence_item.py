from decimal import Decimal
from typing import Any, List, Optional  # noqa

import pydicom


class DoseCalibrationConditionsSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def CalibrationDateTime(self) -> Optional[str]:
        if "CalibrationDateTime" in self._dataset:
            return self._dataset.CalibrationDateTime
        return None

    @CalibrationDateTime.setter
    def CalibrationDateTime(self, value: Optional[str]):
        if value is None:
            if "CalibrationDateTime" in self._dataset:
                del self._dataset.CalibrationDateTime
        else:
            self._dataset.CalibrationDateTime = value

    @property
    def SourceToSurfaceDistance(self) -> Optional[Decimal]:
        if "SourceToSurfaceDistance" in self._dataset:
            return self._dataset.SourceToSurfaceDistance
        return None

    @SourceToSurfaceDistance.setter
    def SourceToSurfaceDistance(self, value: Optional[Decimal]):
        if value is None:
            if "SourceToSurfaceDistance" in self._dataset:
                del self._dataset.SourceToSurfaceDistance
        else:
            self._dataset.SourceToSurfaceDistance = value

    @property
    def AbsorbedDoseToMetersetRatio(self) -> Optional[float]:
        if "AbsorbedDoseToMetersetRatio" in self._dataset:
            return self._dataset.AbsorbedDoseToMetersetRatio
        return None

    @AbsorbedDoseToMetersetRatio.setter
    def AbsorbedDoseToMetersetRatio(self, value: Optional[float]):
        if value is None:
            if "AbsorbedDoseToMetersetRatio" in self._dataset:
                del self._dataset.AbsorbedDoseToMetersetRatio
        else:
            self._dataset.AbsorbedDoseToMetersetRatio = value

    @property
    def DelineatedRadiationFieldSize(self) -> Optional[List[float]]:
        if "DelineatedRadiationFieldSize" in self._dataset:
            return self._dataset.DelineatedRadiationFieldSize
        return None

    @DelineatedRadiationFieldSize.setter
    def DelineatedRadiationFieldSize(self, value: Optional[List[float]]):
        if value is None:
            if "DelineatedRadiationFieldSize" in self._dataset:
                del self._dataset.DelineatedRadiationFieldSize
        else:
            self._dataset.DelineatedRadiationFieldSize = value

    @property
    def CalibrationReferencePointDepth(self) -> Optional[float]:
        if "CalibrationReferencePointDepth" in self._dataset:
            return self._dataset.CalibrationReferencePointDepth
        return None

    @CalibrationReferencePointDepth.setter
    def CalibrationReferencePointDepth(self, value: Optional[float]):
        if value is None:
            if "CalibrationReferencePointDepth" in self._dataset:
                del self._dataset.CalibrationReferencePointDepth
        else:
            self._dataset.CalibrationReferencePointDepth = value
