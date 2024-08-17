from typing import Any, List, Optional

import pydicom


class StructuredDisplayTextBoxSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def UnformattedTextValue(self) -> Optional[str]:
        if "UnformattedTextValue" in self._dataset:
            return self._dataset.UnformattedTextValue
        return None

    @UnformattedTextValue.setter
    def UnformattedTextValue(self, value: Optional[str]):
        if value is None:
            if "UnformattedTextValue" in self._dataset:
                del self._dataset.UnformattedTextValue
        else:
            self._dataset.UnformattedTextValue = value

    @property
    def BoundingBoxTextHorizontalJustification(self) -> Optional[str]:
        if "BoundingBoxTextHorizontalJustification" in self._dataset:
            return self._dataset.BoundingBoxTextHorizontalJustification
        return None

    @BoundingBoxTextHorizontalJustification.setter
    def BoundingBoxTextHorizontalJustification(self, value: Optional[str]):
        if value is None:
            if "BoundingBoxTextHorizontalJustification" in self._dataset:
                del self._dataset.BoundingBoxTextHorizontalJustification
        else:
            self._dataset.BoundingBoxTextHorizontalJustification = value

    @property
    def GraphicLayerRecommendedDisplayCIELabValue(self) -> Optional[List[int]]:
        if "GraphicLayerRecommendedDisplayCIELabValue" in self._dataset:
            return self._dataset.GraphicLayerRecommendedDisplayCIELabValue
        return None

    @GraphicLayerRecommendedDisplayCIELabValue.setter
    def GraphicLayerRecommendedDisplayCIELabValue(self, value: Optional[List[int]]):
        if value is None:
            if "GraphicLayerRecommendedDisplayCIELabValue" in self._dataset:
                del self._dataset.GraphicLayerRecommendedDisplayCIELabValue
        else:
            self._dataset.GraphicLayerRecommendedDisplayCIELabValue = value

    @property
    def DisplayEnvironmentSpatialPosition(self) -> Optional[List[float]]:
        if "DisplayEnvironmentSpatialPosition" in self._dataset:
            return self._dataset.DisplayEnvironmentSpatialPosition
        return None

    @DisplayEnvironmentSpatialPosition.setter
    def DisplayEnvironmentSpatialPosition(self, value: Optional[List[float]]):
        if value is None:
            if "DisplayEnvironmentSpatialPosition" in self._dataset:
                del self._dataset.DisplayEnvironmentSpatialPosition
        else:
            self._dataset.DisplayEnvironmentSpatialPosition = value
