from decimal import Decimal
from typing import Any, List, Optional  # noqa

import pydicom


class FrameDetectorParametersSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def DetectorActiveTime(self) -> Optional[Decimal]:
        if "DetectorActiveTime" in self._dataset:
            return self._dataset.DetectorActiveTime
        return None

    @DetectorActiveTime.setter
    def DetectorActiveTime(self, value: Optional[Decimal]):
        if value is None:
            if "DetectorActiveTime" in self._dataset:
                del self._dataset.DetectorActiveTime
        else:
            self._dataset.DetectorActiveTime = value

    @property
    def DetectorActivationOffsetFromExposure(self) -> Optional[Decimal]:
        if "DetectorActivationOffsetFromExposure" in self._dataset:
            return self._dataset.DetectorActivationOffsetFromExposure
        return None

    @DetectorActivationOffsetFromExposure.setter
    def DetectorActivationOffsetFromExposure(self, value: Optional[Decimal]):
        if value is None:
            if "DetectorActivationOffsetFromExposure" in self._dataset:
                del self._dataset.DetectorActivationOffsetFromExposure
        else:
            self._dataset.DetectorActivationOffsetFromExposure = value
