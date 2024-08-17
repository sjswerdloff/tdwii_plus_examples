from typing import Any, List, Optional  # noqa

import pydicom


class AnimationCurveSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def NumberOfVolumetricCurvePoints(self) -> Optional[int]:
        if "NumberOfVolumetricCurvePoints" in self._dataset:
            return self._dataset.NumberOfVolumetricCurvePoints
        return None

    @NumberOfVolumetricCurvePoints.setter
    def NumberOfVolumetricCurvePoints(self, value: Optional[int]):
        if value is None:
            if "NumberOfVolumetricCurvePoints" in self._dataset:
                del self._dataset.NumberOfVolumetricCurvePoints
        else:
            self._dataset.NumberOfVolumetricCurvePoints = value

    @property
    def VolumetricCurvePoints(self) -> Optional[bytes]:
        if "VolumetricCurvePoints" in self._dataset:
            return self._dataset.VolumetricCurvePoints
        return None

    @VolumetricCurvePoints.setter
    def VolumetricCurvePoints(self, value: Optional[bytes]):
        if value is None:
            if "VolumetricCurvePoints" in self._dataset:
                del self._dataset.VolumetricCurvePoints
        else:
            self._dataset.VolumetricCurvePoints = value

    @property
    def VolumetricCurveUpDirections(self) -> Optional[bytes]:
        if "VolumetricCurveUpDirections" in self._dataset:
            return self._dataset.VolumetricCurveUpDirections
        return None

    @VolumetricCurveUpDirections.setter
    def VolumetricCurveUpDirections(self, value: Optional[bytes]):
        if value is None:
            if "VolumetricCurveUpDirections" in self._dataset:
                del self._dataset.VolumetricCurveUpDirections
        else:
            self._dataset.VolumetricCurveUpDirections = value
