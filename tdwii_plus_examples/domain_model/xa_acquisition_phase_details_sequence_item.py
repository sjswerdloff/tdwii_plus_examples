from typing import Any, List, Optional  # noqa

import pydicom


class XAAcquisitionPhaseDetailsSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def XAAcquisitionFrameRate(self) -> Optional[float]:
        if "XAAcquisitionFrameRate" in self._dataset:
            return self._dataset.XAAcquisitionFrameRate
        return None

    @XAAcquisitionFrameRate.setter
    def XAAcquisitionFrameRate(self, value: Optional[float]):
        if value is None:
            if "XAAcquisitionFrameRate" in self._dataset:
                del self._dataset.XAAcquisitionFrameRate
        else:
            self._dataset.XAAcquisitionFrameRate = value

    @property
    def XAAcquisitionDuration(self) -> Optional[float]:
        if "XAAcquisitionDuration" in self._dataset:
            return self._dataset.XAAcquisitionDuration
        return None

    @XAAcquisitionDuration.setter
    def XAAcquisitionDuration(self, value: Optional[float]):
        if value is None:
            if "XAAcquisitionDuration" in self._dataset:
                del self._dataset.XAAcquisitionDuration
        else:
            self._dataset.XAAcquisitionDuration = value
