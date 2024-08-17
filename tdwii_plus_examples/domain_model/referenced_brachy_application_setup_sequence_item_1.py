from typing import Any, List, Optional

import pydicom


class ReferencedBrachyApplicationSetupSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ReferencedBrachyApplicationSetupNumber(self) -> Optional[int]:
        if "ReferencedBrachyApplicationSetupNumber" in self._dataset:
            return self._dataset.ReferencedBrachyApplicationSetupNumber
        return None

    @ReferencedBrachyApplicationSetupNumber.setter
    def ReferencedBrachyApplicationSetupNumber(self, value: Optional[int]):
        if value is None:
            if "ReferencedBrachyApplicationSetupNumber" in self._dataset:
                del self._dataset.ReferencedBrachyApplicationSetupNumber
        else:
            self._dataset.ReferencedBrachyApplicationSetupNumber = value
