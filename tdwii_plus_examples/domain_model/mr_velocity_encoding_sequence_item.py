from typing import Any, List, Optional  # noqa

import pydicom


class MRVelocityEncodingSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def VelocityEncodingDirection(self) -> Optional[List[float]]:
        if "VelocityEncodingDirection" in self._dataset:
            return self._dataset.VelocityEncodingDirection
        return None

    @VelocityEncodingDirection.setter
    def VelocityEncodingDirection(self, value: Optional[List[float]]):
        if value is None:
            if "VelocityEncodingDirection" in self._dataset:
                del self._dataset.VelocityEncodingDirection
        else:
            self._dataset.VelocityEncodingDirection = value

    @property
    def VelocityEncodingMinimumValue(self) -> Optional[float]:
        if "VelocityEncodingMinimumValue" in self._dataset:
            return self._dataset.VelocityEncodingMinimumValue
        return None

    @VelocityEncodingMinimumValue.setter
    def VelocityEncodingMinimumValue(self, value: Optional[float]):
        if value is None:
            if "VelocityEncodingMinimumValue" in self._dataset:
                del self._dataset.VelocityEncodingMinimumValue
        else:
            self._dataset.VelocityEncodingMinimumValue = value

    @property
    def VelocityEncodingMaximumValue(self) -> Optional[float]:
        if "VelocityEncodingMaximumValue" in self._dataset:
            return self._dataset.VelocityEncodingMaximumValue
        return None

    @VelocityEncodingMaximumValue.setter
    def VelocityEncodingMaximumValue(self, value: Optional[float]):
        if value is None:
            if "VelocityEncodingMaximumValue" in self._dataset:
                del self._dataset.VelocityEncodingMaximumValue
        else:
            self._dataset.VelocityEncodingMaximumValue = value
