from decimal import Decimal
from typing import Any, List, Optional  # noqa

import pydicom


class ContrastAdministrationProfileSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ContrastBolusVolume(self) -> Optional[Decimal]:
        if "ContrastBolusVolume" in self._dataset:
            return self._dataset.ContrastBolusVolume
        return None

    @ContrastBolusVolume.setter
    def ContrastBolusVolume(self, value: Optional[Decimal]):
        if value is None:
            if "ContrastBolusVolume" in self._dataset:
                del self._dataset.ContrastBolusVolume
        else:
            self._dataset.ContrastBolusVolume = value

    @property
    def ContrastBolusStartTime(self) -> Optional[str]:
        if "ContrastBolusStartTime" in self._dataset:
            return self._dataset.ContrastBolusStartTime
        return None

    @ContrastBolusStartTime.setter
    def ContrastBolusStartTime(self, value: Optional[str]):
        if value is None:
            if "ContrastBolusStartTime" in self._dataset:
                del self._dataset.ContrastBolusStartTime
        else:
            self._dataset.ContrastBolusStartTime = value

    @property
    def ContrastBolusStopTime(self) -> Optional[str]:
        if "ContrastBolusStopTime" in self._dataset:
            return self._dataset.ContrastBolusStopTime
        return None

    @ContrastBolusStopTime.setter
    def ContrastBolusStopTime(self, value: Optional[str]):
        if value is None:
            if "ContrastBolusStopTime" in self._dataset:
                del self._dataset.ContrastBolusStopTime
        else:
            self._dataset.ContrastBolusStopTime = value

    @property
    def ContrastFlowRate(self) -> Optional[List[Decimal]]:
        if "ContrastFlowRate" in self._dataset:
            return self._dataset.ContrastFlowRate
        return None

    @ContrastFlowRate.setter
    def ContrastFlowRate(self, value: Optional[List[Decimal]]):
        if value is None:
            if "ContrastFlowRate" in self._dataset:
                del self._dataset.ContrastFlowRate
        else:
            self._dataset.ContrastFlowRate = value

    @property
    def ContrastFlowDuration(self) -> Optional[List[Decimal]]:
        if "ContrastFlowDuration" in self._dataset:
            return self._dataset.ContrastFlowDuration
        return None

    @ContrastFlowDuration.setter
    def ContrastFlowDuration(self, value: Optional[List[Decimal]]):
        if value is None:
            if "ContrastFlowDuration" in self._dataset:
                del self._dataset.ContrastFlowDuration
        else:
            self._dataset.ContrastFlowDuration = value
