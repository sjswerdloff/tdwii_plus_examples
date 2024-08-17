from typing import Any, List, Optional  # noqa

import pydicom


class ASLBolusCutoffTimingSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ASLBolusCutoffTechnique(self) -> Optional[str]:
        if "ASLBolusCutoffTechnique" in self._dataset:
            return self._dataset.ASLBolusCutoffTechnique
        return None

    @ASLBolusCutoffTechnique.setter
    def ASLBolusCutoffTechnique(self, value: Optional[str]):
        if value is None:
            if "ASLBolusCutoffTechnique" in self._dataset:
                del self._dataset.ASLBolusCutoffTechnique
        else:
            self._dataset.ASLBolusCutoffTechnique = value

    @property
    def ASLBolusCutoffDelayTime(self) -> Optional[int]:
        if "ASLBolusCutoffDelayTime" in self._dataset:
            return self._dataset.ASLBolusCutoffDelayTime
        return None

    @ASLBolusCutoffDelayTime.setter
    def ASLBolusCutoffDelayTime(self, value: Optional[int]):
        if value is None:
            if "ASLBolusCutoffDelayTime" in self._dataset:
                del self._dataset.ASLBolusCutoffDelayTime
        else:
            self._dataset.ASLBolusCutoffDelayTime = value
