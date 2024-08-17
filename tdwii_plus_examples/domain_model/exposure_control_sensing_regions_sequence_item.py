from typing import Any, List, Optional

import pydicom


class ExposureControlSensingRegionsSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ExposureControlSensingRegionShape(self) -> Optional[str]:
        if "ExposureControlSensingRegionShape" in self._dataset:
            return self._dataset.ExposureControlSensingRegionShape
        return None

    @ExposureControlSensingRegionShape.setter
    def ExposureControlSensingRegionShape(self, value: Optional[str]):
        if value is None:
            if "ExposureControlSensingRegionShape" in self._dataset:
                del self._dataset.ExposureControlSensingRegionShape
        else:
            self._dataset.ExposureControlSensingRegionShape = value

    @property
    def ExposureControlSensingRegionLeftVerticalEdge(self) -> Optional[int]:
        if "ExposureControlSensingRegionLeftVerticalEdge" in self._dataset:
            return self._dataset.ExposureControlSensingRegionLeftVerticalEdge
        return None

    @ExposureControlSensingRegionLeftVerticalEdge.setter
    def ExposureControlSensingRegionLeftVerticalEdge(self, value: Optional[int]):
        if value is None:
            if "ExposureControlSensingRegionLeftVerticalEdge" in self._dataset:
                del self._dataset.ExposureControlSensingRegionLeftVerticalEdge
        else:
            self._dataset.ExposureControlSensingRegionLeftVerticalEdge = value

    @property
    def ExposureControlSensingRegionRightVerticalEdge(self) -> Optional[int]:
        if "ExposureControlSensingRegionRightVerticalEdge" in self._dataset:
            return self._dataset.ExposureControlSensingRegionRightVerticalEdge
        return None

    @ExposureControlSensingRegionRightVerticalEdge.setter
    def ExposureControlSensingRegionRightVerticalEdge(self, value: Optional[int]):
        if value is None:
            if "ExposureControlSensingRegionRightVerticalEdge" in self._dataset:
                del self._dataset.ExposureControlSensingRegionRightVerticalEdge
        else:
            self._dataset.ExposureControlSensingRegionRightVerticalEdge = value

    @property
    def ExposureControlSensingRegionUpperHorizontalEdge(self) -> Optional[int]:
        if "ExposureControlSensingRegionUpperHorizontalEdge" in self._dataset:
            return self._dataset.ExposureControlSensingRegionUpperHorizontalEdge
        return None

    @ExposureControlSensingRegionUpperHorizontalEdge.setter
    def ExposureControlSensingRegionUpperHorizontalEdge(self, value: Optional[int]):
        if value is None:
            if "ExposureControlSensingRegionUpperHorizontalEdge" in self._dataset:
                del self._dataset.ExposureControlSensingRegionUpperHorizontalEdge
        else:
            self._dataset.ExposureControlSensingRegionUpperHorizontalEdge = value

    @property
    def ExposureControlSensingRegionLowerHorizontalEdge(self) -> Optional[int]:
        if "ExposureControlSensingRegionLowerHorizontalEdge" in self._dataset:
            return self._dataset.ExposureControlSensingRegionLowerHorizontalEdge
        return None

    @ExposureControlSensingRegionLowerHorizontalEdge.setter
    def ExposureControlSensingRegionLowerHorizontalEdge(self, value: Optional[int]):
        if value is None:
            if "ExposureControlSensingRegionLowerHorizontalEdge" in self._dataset:
                del self._dataset.ExposureControlSensingRegionLowerHorizontalEdge
        else:
            self._dataset.ExposureControlSensingRegionLowerHorizontalEdge = value

    @property
    def CenterOfCircularExposureControlSensingRegion(self) -> Optional[List[int]]:
        if "CenterOfCircularExposureControlSensingRegion" in self._dataset:
            return self._dataset.CenterOfCircularExposureControlSensingRegion
        return None

    @CenterOfCircularExposureControlSensingRegion.setter
    def CenterOfCircularExposureControlSensingRegion(self, value: Optional[List[int]]):
        if value is None:
            if "CenterOfCircularExposureControlSensingRegion" in self._dataset:
                del self._dataset.CenterOfCircularExposureControlSensingRegion
        else:
            self._dataset.CenterOfCircularExposureControlSensingRegion = value

    @property
    def RadiusOfCircularExposureControlSensingRegion(self) -> Optional[int]:
        if "RadiusOfCircularExposureControlSensingRegion" in self._dataset:
            return self._dataset.RadiusOfCircularExposureControlSensingRegion
        return None

    @RadiusOfCircularExposureControlSensingRegion.setter
    def RadiusOfCircularExposureControlSensingRegion(self, value: Optional[int]):
        if value is None:
            if "RadiusOfCircularExposureControlSensingRegion" in self._dataset:
                del self._dataset.RadiusOfCircularExposureControlSensingRegion
        else:
            self._dataset.RadiusOfCircularExposureControlSensingRegion = value

    @property
    def VerticesOfThePolygonalExposureControlSensingRegion(self) -> Optional[List[int]]:
        if "VerticesOfThePolygonalExposureControlSensingRegion" in self._dataset:
            return self._dataset.VerticesOfThePolygonalExposureControlSensingRegion
        return None

    @VerticesOfThePolygonalExposureControlSensingRegion.setter
    def VerticesOfThePolygonalExposureControlSensingRegion(self, value: Optional[List[int]]):
        if value is None:
            if "VerticesOfThePolygonalExposureControlSensingRegion" in self._dataset:
                del self._dataset.VerticesOfThePolygonalExposureControlSensingRegion
        else:
            self._dataset.VerticesOfThePolygonalExposureControlSensingRegion = value
