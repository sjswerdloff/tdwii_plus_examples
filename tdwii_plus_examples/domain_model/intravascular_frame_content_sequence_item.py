from typing import Any, List, Optional  # noqa

import pydicom


class IntravascularFrameContentSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def IntravascularLongitudinalDistance(self) -> Optional[float]:
        if "IntravascularLongitudinalDistance" in self._dataset:
            return self._dataset.IntravascularLongitudinalDistance
        return None

    @IntravascularLongitudinalDistance.setter
    def IntravascularLongitudinalDistance(self, value: Optional[float]):
        if value is None:
            if "IntravascularLongitudinalDistance" in self._dataset:
                del self._dataset.IntravascularLongitudinalDistance
        else:
            self._dataset.IntravascularLongitudinalDistance = value

    @property
    def SeamLineLocation(self) -> Optional[float]:
        if "SeamLineLocation" in self._dataset:
            return self._dataset.SeamLineLocation
        return None

    @SeamLineLocation.setter
    def SeamLineLocation(self, value: Optional[float]):
        if value is None:
            if "SeamLineLocation" in self._dataset:
                del self._dataset.SeamLineLocation
        else:
            self._dataset.SeamLineLocation = value
