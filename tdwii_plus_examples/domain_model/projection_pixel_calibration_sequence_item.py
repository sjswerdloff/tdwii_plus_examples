from decimal import Decimal
from typing import Any, List, Optional  # noqa

import pydicom


class ProjectionPixelCalibrationSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def TableHeight(self) -> Optional[Decimal]:
        if "TableHeight" in self._dataset:
            return self._dataset.TableHeight
        return None

    @TableHeight.setter
    def TableHeight(self, value: Optional[Decimal]):
        if value is None:
            if "TableHeight" in self._dataset:
                del self._dataset.TableHeight
        else:
            self._dataset.TableHeight = value

    @property
    def DistanceObjectToTableTop(self) -> Optional[float]:
        if "DistanceObjectToTableTop" in self._dataset:
            return self._dataset.DistanceObjectToTableTop
        return None

    @DistanceObjectToTableTop.setter
    def DistanceObjectToTableTop(self, value: Optional[float]):
        if value is None:
            if "DistanceObjectToTableTop" in self._dataset:
                del self._dataset.DistanceObjectToTableTop
        else:
            self._dataset.DistanceObjectToTableTop = value

    @property
    def ObjectPixelSpacingInCenterOfBeam(self) -> Optional[List[float]]:
        if "ObjectPixelSpacingInCenterOfBeam" in self._dataset:
            return self._dataset.ObjectPixelSpacingInCenterOfBeam
        return None

    @ObjectPixelSpacingInCenterOfBeam.setter
    def ObjectPixelSpacingInCenterOfBeam(self, value: Optional[List[float]]):
        if value is None:
            if "ObjectPixelSpacingInCenterOfBeam" in self._dataset:
                del self._dataset.ObjectPixelSpacingInCenterOfBeam
        else:
            self._dataset.ObjectPixelSpacingInCenterOfBeam = value

    @property
    def BeamAngle(self) -> Optional[float]:
        if "BeamAngle" in self._dataset:
            return self._dataset.BeamAngle
        return None

    @BeamAngle.setter
    def BeamAngle(self, value: Optional[float]):
        if value is None:
            if "BeamAngle" in self._dataset:
                del self._dataset.BeamAngle
        else:
            self._dataset.BeamAngle = value
