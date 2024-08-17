from typing import Any, List, Optional  # noqa

import pydicom


class TransducerResponseSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def CenterFrequency(self) -> Optional[float]:
        if "CenterFrequency" in self._dataset:
            return self._dataset.CenterFrequency
        return None

    @CenterFrequency.setter
    def CenterFrequency(self, value: Optional[float]):
        if value is None:
            if "CenterFrequency" in self._dataset:
                del self._dataset.CenterFrequency
        else:
            self._dataset.CenterFrequency = value

    @property
    def FractionalBandwidth(self) -> Optional[float]:
        if "FractionalBandwidth" in self._dataset:
            return self._dataset.FractionalBandwidth
        return None

    @FractionalBandwidth.setter
    def FractionalBandwidth(self, value: Optional[float]):
        if value is None:
            if "FractionalBandwidth" in self._dataset:
                del self._dataset.FractionalBandwidth
        else:
            self._dataset.FractionalBandwidth = value

    @property
    def LowerCutoffFrequency(self) -> Optional[float]:
        if "LowerCutoffFrequency" in self._dataset:
            return self._dataset.LowerCutoffFrequency
        return None

    @LowerCutoffFrequency.setter
    def LowerCutoffFrequency(self, value: Optional[float]):
        if value is None:
            if "LowerCutoffFrequency" in self._dataset:
                del self._dataset.LowerCutoffFrequency
        else:
            self._dataset.LowerCutoffFrequency = value

    @property
    def UpperCutoffFrequency(self) -> Optional[float]:
        if "UpperCutoffFrequency" in self._dataset:
            return self._dataset.UpperCutoffFrequency
        return None

    @UpperCutoffFrequency.setter
    def UpperCutoffFrequency(self, value: Optional[float]):
        if value is None:
            if "UpperCutoffFrequency" in self._dataset:
                del self._dataset.UpperCutoffFrequency
        else:
            self._dataset.UpperCutoffFrequency = value
