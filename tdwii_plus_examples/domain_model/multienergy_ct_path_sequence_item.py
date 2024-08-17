from typing import Any, List, Optional  # noqa

import pydicom


class MultienergyCTPathSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ReferencedXRayDetectorIndex(self) -> Optional[List[int]]:
        if "ReferencedXRayDetectorIndex" in self._dataset:
            return self._dataset.ReferencedXRayDetectorIndex
        return None

    @ReferencedXRayDetectorIndex.setter
    def ReferencedXRayDetectorIndex(self, value: Optional[List[int]]):
        if value is None:
            if "ReferencedXRayDetectorIndex" in self._dataset:
                del self._dataset.ReferencedXRayDetectorIndex
        else:
            self._dataset.ReferencedXRayDetectorIndex = value

    @property
    def ReferencedXRaySourceIndex(self) -> Optional[List[int]]:
        if "ReferencedXRaySourceIndex" in self._dataset:
            return self._dataset.ReferencedXRaySourceIndex
        return None

    @ReferencedXRaySourceIndex.setter
    def ReferencedXRaySourceIndex(self, value: Optional[List[int]]):
        if value is None:
            if "ReferencedXRaySourceIndex" in self._dataset:
                del self._dataset.ReferencedXRaySourceIndex
        else:
            self._dataset.ReferencedXRaySourceIndex = value

    @property
    def MultienergyCTPathIndex(self) -> Optional[int]:
        if "MultienergyCTPathIndex" in self._dataset:
            return self._dataset.MultienergyCTPathIndex
        return None

    @MultienergyCTPathIndex.setter
    def MultienergyCTPathIndex(self, value: Optional[int]):
        if value is None:
            if "MultienergyCTPathIndex" in self._dataset:
                del self._dataset.MultienergyCTPathIndex
        else:
            self._dataset.MultienergyCTPathIndex = value
