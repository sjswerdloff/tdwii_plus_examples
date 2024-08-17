from typing import Any, List, Optional  # noqa

import pydicom


class DVHReferencedROISequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def DVHROIContributionType(self) -> Optional[str]:
        if "DVHROIContributionType" in self._dataset:
            return self._dataset.DVHROIContributionType
        return None

    @DVHROIContributionType.setter
    def DVHROIContributionType(self, value: Optional[str]):
        if value is None:
            if "DVHROIContributionType" in self._dataset:
                del self._dataset.DVHROIContributionType
        else:
            self._dataset.DVHROIContributionType = value

    @property
    def ReferencedROINumber(self) -> Optional[int]:
        if "ReferencedROINumber" in self._dataset:
            return self._dataset.ReferencedROINumber
        return None

    @ReferencedROINumber.setter
    def ReferencedROINumber(self, value: Optional[int]):
        if value is None:
            if "ReferencedROINumber" in self._dataset:
                del self._dataset.ReferencedROINumber
        else:
            self._dataset.ReferencedROINumber = value
