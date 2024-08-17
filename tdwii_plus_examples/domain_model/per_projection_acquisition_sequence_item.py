from decimal import Decimal
from typing import Any, List, Optional  # noqa

import pydicom


class PerProjectionAcquisitionSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def KVP(self) -> Optional[Decimal]:
        if "KVP" in self._dataset:
            return self._dataset.KVP
        return None

    @KVP.setter
    def KVP(self, value: Optional[Decimal]):
        if value is None:
            if "KVP" in self._dataset:
                del self._dataset.KVP
        else:
            self._dataset.KVP = value

    @property
    def PositionerPrimaryAngle(self) -> Optional[Decimal]:
        if "PositionerPrimaryAngle" in self._dataset:
            return self._dataset.PositionerPrimaryAngle
        return None

    @PositionerPrimaryAngle.setter
    def PositionerPrimaryAngle(self, value: Optional[Decimal]):
        if value is None:
            if "PositionerPrimaryAngle" in self._dataset:
                del self._dataset.PositionerPrimaryAngle
        else:
            self._dataset.PositionerPrimaryAngle = value

    @property
    def PositionerSecondaryAngle(self) -> Optional[Decimal]:
        if "PositionerSecondaryAngle" in self._dataset:
            return self._dataset.PositionerSecondaryAngle
        return None

    @PositionerSecondaryAngle.setter
    def PositionerSecondaryAngle(self, value: Optional[Decimal]):
        if value is None:
            if "PositionerSecondaryAngle" in self._dataset:
                del self._dataset.PositionerSecondaryAngle
        else:
            self._dataset.PositionerSecondaryAngle = value

    @property
    def CollimatorShape(self) -> Optional[List[str]]:
        if "CollimatorShape" in self._dataset:
            return self._dataset.CollimatorShape
        return None

    @CollimatorShape.setter
    def CollimatorShape(self, value: Optional[List[str]]):
        if value is None:
            if "CollimatorShape" in self._dataset:
                del self._dataset.CollimatorShape
        else:
            self._dataset.CollimatorShape = value

    @property
    def CollimatorLeftVerticalEdge(self) -> Optional[int]:
        if "CollimatorLeftVerticalEdge" in self._dataset:
            return self._dataset.CollimatorLeftVerticalEdge
        return None

    @CollimatorLeftVerticalEdge.setter
    def CollimatorLeftVerticalEdge(self, value: Optional[int]):
        if value is None:
            if "CollimatorLeftVerticalEdge" in self._dataset:
                del self._dataset.CollimatorLeftVerticalEdge
        else:
            self._dataset.CollimatorLeftVerticalEdge = value

    @property
    def CollimatorRightVerticalEdge(self) -> Optional[int]:
        if "CollimatorRightVerticalEdge" in self._dataset:
            return self._dataset.CollimatorRightVerticalEdge
        return None

    @CollimatorRightVerticalEdge.setter
    def CollimatorRightVerticalEdge(self, value: Optional[int]):
        if value is None:
            if "CollimatorRightVerticalEdge" in self._dataset:
                del self._dataset.CollimatorRightVerticalEdge
        else:
            self._dataset.CollimatorRightVerticalEdge = value

    @property
    def CollimatorUpperHorizontalEdge(self) -> Optional[int]:
        if "CollimatorUpperHorizontalEdge" in self._dataset:
            return self._dataset.CollimatorUpperHorizontalEdge
        return None

    @CollimatorUpperHorizontalEdge.setter
    def CollimatorUpperHorizontalEdge(self, value: Optional[int]):
        if value is None:
            if "CollimatorUpperHorizontalEdge" in self._dataset:
                del self._dataset.CollimatorUpperHorizontalEdge
        else:
            self._dataset.CollimatorUpperHorizontalEdge = value

    @property
    def CollimatorLowerHorizontalEdge(self) -> Optional[int]:
        if "CollimatorLowerHorizontalEdge" in self._dataset:
            return self._dataset.CollimatorLowerHorizontalEdge
        return None

    @CollimatorLowerHorizontalEdge.setter
    def CollimatorLowerHorizontalEdge(self, value: Optional[int]):
        if value is None:
            if "CollimatorLowerHorizontalEdge" in self._dataset:
                del self._dataset.CollimatorLowerHorizontalEdge
        else:
            self._dataset.CollimatorLowerHorizontalEdge = value

    @property
    def CenterOfCircularCollimator(self) -> Optional[List[int]]:
        if "CenterOfCircularCollimator" in self._dataset:
            return self._dataset.CenterOfCircularCollimator
        return None

    @CenterOfCircularCollimator.setter
    def CenterOfCircularCollimator(self, value: Optional[List[int]]):
        if value is None:
            if "CenterOfCircularCollimator" in self._dataset:
                del self._dataset.CenterOfCircularCollimator
        else:
            self._dataset.CenterOfCircularCollimator = value

    @property
    def RadiusOfCircularCollimator(self) -> Optional[int]:
        if "RadiusOfCircularCollimator" in self._dataset:
            return self._dataset.RadiusOfCircularCollimator
        return None

    @RadiusOfCircularCollimator.setter
    def RadiusOfCircularCollimator(self, value: Optional[int]):
        if value is None:
            if "RadiusOfCircularCollimator" in self._dataset:
                del self._dataset.RadiusOfCircularCollimator
        else:
            self._dataset.RadiusOfCircularCollimator = value

    @property
    def VerticesOfThePolygonalCollimator(self) -> Optional[List[int]]:
        if "VerticesOfThePolygonalCollimator" in self._dataset:
            return self._dataset.VerticesOfThePolygonalCollimator
        return None

    @VerticesOfThePolygonalCollimator.setter
    def VerticesOfThePolygonalCollimator(self, value: Optional[List[int]]):
        if value is None:
            if "VerticesOfThePolygonalCollimator" in self._dataset:
                del self._dataset.VerticesOfThePolygonalCollimator
        else:
            self._dataset.VerticesOfThePolygonalCollimator = value

    @property
    def FrameAcquisitionDuration(self) -> Optional[float]:
        if "FrameAcquisitionDuration" in self._dataset:
            return self._dataset.FrameAcquisitionDuration
        return None

    @FrameAcquisitionDuration.setter
    def FrameAcquisitionDuration(self, value: Optional[float]):
        if value is None:
            if "FrameAcquisitionDuration" in self._dataset:
                del self._dataset.FrameAcquisitionDuration
        else:
            self._dataset.FrameAcquisitionDuration = value

    @property
    def XRayTubeCurrentInmA(self) -> Optional[float]:
        if "XRayTubeCurrentInmA" in self._dataset:
            return self._dataset.XRayTubeCurrentInmA
        return None

    @XRayTubeCurrentInmA.setter
    def XRayTubeCurrentInmA(self, value: Optional[float]):
        if value is None:
            if "XRayTubeCurrentInmA" in self._dataset:
                del self._dataset.XRayTubeCurrentInmA
        else:
            self._dataset.XRayTubeCurrentInmA = value

    @property
    def PositionerIsocenterPrimaryAngle(self) -> Optional[float]:
        if "PositionerIsocenterPrimaryAngle" in self._dataset:
            return self._dataset.PositionerIsocenterPrimaryAngle
        return None

    @PositionerIsocenterPrimaryAngle.setter
    def PositionerIsocenterPrimaryAngle(self, value: Optional[float]):
        if value is None:
            if "PositionerIsocenterPrimaryAngle" in self._dataset:
                del self._dataset.PositionerIsocenterPrimaryAngle
        else:
            self._dataset.PositionerIsocenterPrimaryAngle = value

    @property
    def PositionerIsocenterSecondaryAngle(self) -> Optional[float]:
        if "PositionerIsocenterSecondaryAngle" in self._dataset:
            return self._dataset.PositionerIsocenterSecondaryAngle
        return None

    @PositionerIsocenterSecondaryAngle.setter
    def PositionerIsocenterSecondaryAngle(self, value: Optional[float]):
        if value is None:
            if "PositionerIsocenterSecondaryAngle" in self._dataset:
                del self._dataset.PositionerIsocenterSecondaryAngle
        else:
            self._dataset.PositionerIsocenterSecondaryAngle = value

    @property
    def PositionerIsocenterDetectorRotationAngle(self) -> Optional[float]:
        if "PositionerIsocenterDetectorRotationAngle" in self._dataset:
            return self._dataset.PositionerIsocenterDetectorRotationAngle
        return None

    @PositionerIsocenterDetectorRotationAngle.setter
    def PositionerIsocenterDetectorRotationAngle(self, value: Optional[float]):
        if value is None:
            if "PositionerIsocenterDetectorRotationAngle" in self._dataset:
                del self._dataset.PositionerIsocenterDetectorRotationAngle
        else:
            self._dataset.PositionerIsocenterDetectorRotationAngle = value
