from typing import Any, List, Optional  # noqa

import pydicom


class RelevantOPTAttributesSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def DepthSpatialResolution(self) -> Optional[float]:
        if "DepthSpatialResolution" in self._dataset:
            return self._dataset.DepthSpatialResolution
        return None

    @DepthSpatialResolution.setter
    def DepthSpatialResolution(self, value: Optional[float]):
        if value is None:
            if "DepthSpatialResolution" in self._dataset:
                del self._dataset.DepthSpatialResolution
        else:
            self._dataset.DepthSpatialResolution = value

    @property
    def MaximumDepthDistortion(self) -> Optional[float]:
        if "MaximumDepthDistortion" in self._dataset:
            return self._dataset.MaximumDepthDistortion
        return None

    @MaximumDepthDistortion.setter
    def MaximumDepthDistortion(self, value: Optional[float]):
        if value is None:
            if "MaximumDepthDistortion" in self._dataset:
                del self._dataset.MaximumDepthDistortion
        else:
            self._dataset.MaximumDepthDistortion = value
