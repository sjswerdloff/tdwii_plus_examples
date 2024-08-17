from typing import Any, List, Optional  # noqa

import pydicom


class MRSpatialSaturationSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def SlabThickness(self) -> Optional[float]:
        if "SlabThickness" in self._dataset:
            return self._dataset.SlabThickness
        return None

    @SlabThickness.setter
    def SlabThickness(self, value: Optional[float]):
        if value is None:
            if "SlabThickness" in self._dataset:
                del self._dataset.SlabThickness
        else:
            self._dataset.SlabThickness = value

    @property
    def SlabOrientation(self) -> Optional[List[float]]:
        if "SlabOrientation" in self._dataset:
            return self._dataset.SlabOrientation
        return None

    @SlabOrientation.setter
    def SlabOrientation(self, value: Optional[List[float]]):
        if value is None:
            if "SlabOrientation" in self._dataset:
                del self._dataset.SlabOrientation
        else:
            self._dataset.SlabOrientation = value

    @property
    def MidSlabPosition(self) -> Optional[List[float]]:
        if "MidSlabPosition" in self._dataset:
            return self._dataset.MidSlabPosition
        return None

    @MidSlabPosition.setter
    def MidSlabPosition(self, value: Optional[List[float]]):
        if value is None:
            if "MidSlabPosition" in self._dataset:
                del self._dataset.MidSlabPosition
        else:
            self._dataset.MidSlabPosition = value
