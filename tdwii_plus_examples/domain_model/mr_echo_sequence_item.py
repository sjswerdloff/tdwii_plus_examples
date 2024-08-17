from typing import Any, List, Optional  # noqa

import pydicom


class MREchoSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def EffectiveEchoTime(self) -> Optional[float]:
        if "EffectiveEchoTime" in self._dataset:
            return self._dataset.EffectiveEchoTime
        return None

    @EffectiveEchoTime.setter
    def EffectiveEchoTime(self, value: Optional[float]):
        if value is None:
            if "EffectiveEchoTime" in self._dataset:
                del self._dataset.EffectiveEchoTime
        else:
            self._dataset.EffectiveEchoTime = value
