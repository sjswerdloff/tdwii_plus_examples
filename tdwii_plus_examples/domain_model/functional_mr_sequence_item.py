from typing import Any, List, Optional  # noqa

import pydicom


class FunctionalMRSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def FunctionalSyncPulse(self) -> Optional[str]:
        if "FunctionalSyncPulse" in self._dataset:
            return self._dataset.FunctionalSyncPulse
        return None

    @FunctionalSyncPulse.setter
    def FunctionalSyncPulse(self, value: Optional[str]):
        if value is None:
            if "FunctionalSyncPulse" in self._dataset:
                del self._dataset.FunctionalSyncPulse
        else:
            self._dataset.FunctionalSyncPulse = value

    @property
    def SettlingPhaseFrame(self) -> Optional[str]:
        if "SettlingPhaseFrame" in self._dataset:
            return self._dataset.SettlingPhaseFrame
        return None

    @SettlingPhaseFrame.setter
    def SettlingPhaseFrame(self, value: Optional[str]):
        if value is None:
            if "SettlingPhaseFrame" in self._dataset:
                del self._dataset.SettlingPhaseFrame
        else:
            self._dataset.SettlingPhaseFrame = value
