from typing import Any, List, Optional

import pydicom


class GraphicLayerSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def GraphicLayer(self) -> Optional[str]:
        if "GraphicLayer" in self._dataset:
            return self._dataset.GraphicLayer
        return None

    @GraphicLayer.setter
    def GraphicLayer(self, value: Optional[str]):
        if value is None:
            if "GraphicLayer" in self._dataset:
                del self._dataset.GraphicLayer
        else:
            self._dataset.GraphicLayer = value

    @property
    def GraphicLayerOrder(self) -> Optional[int]:
        if "GraphicLayerOrder" in self._dataset:
            return self._dataset.GraphicLayerOrder
        return None

    @GraphicLayerOrder.setter
    def GraphicLayerOrder(self, value: Optional[int]):
        if value is None:
            if "GraphicLayerOrder" in self._dataset:
                del self._dataset.GraphicLayerOrder
        else:
            self._dataset.GraphicLayerOrder = value

    @property
    def GraphicLayerRecommendedDisplayGrayscaleValue(self) -> Optional[int]:
        if "GraphicLayerRecommendedDisplayGrayscaleValue" in self._dataset:
            return self._dataset.GraphicLayerRecommendedDisplayGrayscaleValue
        return None

    @GraphicLayerRecommendedDisplayGrayscaleValue.setter
    def GraphicLayerRecommendedDisplayGrayscaleValue(self, value: Optional[int]):
        if value is None:
            if "GraphicLayerRecommendedDisplayGrayscaleValue" in self._dataset:
                del self._dataset.GraphicLayerRecommendedDisplayGrayscaleValue
        else:
            self._dataset.GraphicLayerRecommendedDisplayGrayscaleValue = value

    @property
    def GraphicLayerDescription(self) -> Optional[str]:
        if "GraphicLayerDescription" in self._dataset:
            return self._dataset.GraphicLayerDescription
        return None

    @GraphicLayerDescription.setter
    def GraphicLayerDescription(self, value: Optional[str]):
        if value is None:
            if "GraphicLayerDescription" in self._dataset:
                del self._dataset.GraphicLayerDescription
        else:
            self._dataset.GraphicLayerDescription = value

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
