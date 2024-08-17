from typing import Any, List, Optional

import pydicom


class CameraPositionGroupSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def RenderProjection(self) -> Optional[str]:
        if "RenderProjection" in self._dataset:
            return self._dataset.RenderProjection
        return None

    @RenderProjection.setter
    def RenderProjection(self, value: Optional[str]):
        if value is None:
            if "RenderProjection" in self._dataset:
                del self._dataset.RenderProjection
        else:
            self._dataset.RenderProjection = value

    @property
    def ViewpointPosition(self) -> Optional[List[float]]:
        if "ViewpointPosition" in self._dataset:
            return self._dataset.ViewpointPosition
        return None

    @ViewpointPosition.setter
    def ViewpointPosition(self, value: Optional[List[float]]):
        if value is None:
            if "ViewpointPosition" in self._dataset:
                del self._dataset.ViewpointPosition
        else:
            self._dataset.ViewpointPosition = value

    @property
    def ViewpointLookAtPoint(self) -> Optional[List[float]]:
        if "ViewpointLookAtPoint" in self._dataset:
            return self._dataset.ViewpointLookAtPoint
        return None

    @ViewpointLookAtPoint.setter
    def ViewpointLookAtPoint(self, value: Optional[List[float]]):
        if value is None:
            if "ViewpointLookAtPoint" in self._dataset:
                del self._dataset.ViewpointLookAtPoint
        else:
            self._dataset.ViewpointLookAtPoint = value

    @property
    def ViewpointUpDirection(self) -> Optional[List[float]]:
        if "ViewpointUpDirection" in self._dataset:
            return self._dataset.ViewpointUpDirection
        return None

    @ViewpointUpDirection.setter
    def ViewpointUpDirection(self, value: Optional[List[float]]):
        if value is None:
            if "ViewpointUpDirection" in self._dataset:
                del self._dataset.ViewpointUpDirection
        else:
            self._dataset.ViewpointUpDirection = value

    @property
    def RenderFieldOfView(self) -> Optional[List[float]]:
        if "RenderFieldOfView" in self._dataset:
            return self._dataset.RenderFieldOfView
        return None

    @RenderFieldOfView.setter
    def RenderFieldOfView(self, value: Optional[List[float]]):
        if value is None:
            if "RenderFieldOfView" in self._dataset:
                del self._dataset.RenderFieldOfView
        else:
            self._dataset.RenderFieldOfView = value
