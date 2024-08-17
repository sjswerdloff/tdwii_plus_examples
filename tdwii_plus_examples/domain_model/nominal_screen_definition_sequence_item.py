from typing import Any, List, Optional  # noqa

import pydicom


class NominalScreenDefinitionSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def NumberOfVerticalPixels(self) -> Optional[int]:
        if "NumberOfVerticalPixels" in self._dataset:
            return self._dataset.NumberOfVerticalPixels
        return None

    @NumberOfVerticalPixels.setter
    def NumberOfVerticalPixels(self, value: Optional[int]):
        if value is None:
            if "NumberOfVerticalPixels" in self._dataset:
                del self._dataset.NumberOfVerticalPixels
        else:
            self._dataset.NumberOfVerticalPixels = value

    @property
    def NumberOfHorizontalPixels(self) -> Optional[int]:
        if "NumberOfHorizontalPixels" in self._dataset:
            return self._dataset.NumberOfHorizontalPixels
        return None

    @NumberOfHorizontalPixels.setter
    def NumberOfHorizontalPixels(self, value: Optional[int]):
        if value is None:
            if "NumberOfHorizontalPixels" in self._dataset:
                del self._dataset.NumberOfHorizontalPixels
        else:
            self._dataset.NumberOfHorizontalPixels = value

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

    @property
    def ScreenMinimumGrayscaleBitDepth(self) -> Optional[int]:
        if "ScreenMinimumGrayscaleBitDepth" in self._dataset:
            return self._dataset.ScreenMinimumGrayscaleBitDepth
        return None

    @ScreenMinimumGrayscaleBitDepth.setter
    def ScreenMinimumGrayscaleBitDepth(self, value: Optional[int]):
        if value is None:
            if "ScreenMinimumGrayscaleBitDepth" in self._dataset:
                del self._dataset.ScreenMinimumGrayscaleBitDepth
        else:
            self._dataset.ScreenMinimumGrayscaleBitDepth = value

    @property
    def ScreenMinimumColorBitDepth(self) -> Optional[int]:
        if "ScreenMinimumColorBitDepth" in self._dataset:
            return self._dataset.ScreenMinimumColorBitDepth
        return None

    @ScreenMinimumColorBitDepth.setter
    def ScreenMinimumColorBitDepth(self, value: Optional[int]):
        if value is None:
            if "ScreenMinimumColorBitDepth" in self._dataset:
                del self._dataset.ScreenMinimumColorBitDepth
        else:
            self._dataset.ScreenMinimumColorBitDepth = value

    @property
    def ApplicationMaximumRepaintTime(self) -> Optional[int]:
        if "ApplicationMaximumRepaintTime" in self._dataset:
            return self._dataset.ApplicationMaximumRepaintTime
        return None

    @ApplicationMaximumRepaintTime.setter
    def ApplicationMaximumRepaintTime(self, value: Optional[int]):
        if value is None:
            if "ApplicationMaximumRepaintTime" in self._dataset:
                del self._dataset.ApplicationMaximumRepaintTime
        else:
            self._dataset.ApplicationMaximumRepaintTime = value
