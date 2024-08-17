from typing import Any, List, Optional

import pydicom


class LineStyleSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ShadowStyle(self) -> Optional[str]:
        if "ShadowStyle" in self._dataset:
            return self._dataset.ShadowStyle
        return None

    @ShadowStyle.setter
    def ShadowStyle(self, value: Optional[str]):
        if value is None:
            if "ShadowStyle" in self._dataset:
                del self._dataset.ShadowStyle
        else:
            self._dataset.ShadowStyle = value

    @property
    def ShadowOffsetX(self) -> Optional[float]:
        if "ShadowOffsetX" in self._dataset:
            return self._dataset.ShadowOffsetX
        return None

    @ShadowOffsetX.setter
    def ShadowOffsetX(self, value: Optional[float]):
        if value is None:
            if "ShadowOffsetX" in self._dataset:
                del self._dataset.ShadowOffsetX
        else:
            self._dataset.ShadowOffsetX = value

    @property
    def ShadowOffsetY(self) -> Optional[float]:
        if "ShadowOffsetY" in self._dataset:
            return self._dataset.ShadowOffsetY
        return None

    @ShadowOffsetY.setter
    def ShadowOffsetY(self, value: Optional[float]):
        if value is None:
            if "ShadowOffsetY" in self._dataset:
                del self._dataset.ShadowOffsetY
        else:
            self._dataset.ShadowOffsetY = value

    @property
    def ShadowColorCIELabValue(self) -> Optional[List[int]]:
        if "ShadowColorCIELabValue" in self._dataset:
            return self._dataset.ShadowColorCIELabValue
        return None

    @ShadowColorCIELabValue.setter
    def ShadowColorCIELabValue(self, value: Optional[List[int]]):
        if value is None:
            if "ShadowColorCIELabValue" in self._dataset:
                del self._dataset.ShadowColorCIELabValue
        else:
            self._dataset.ShadowColorCIELabValue = value

    @property
    def PatternOnColorCIELabValue(self) -> Optional[List[int]]:
        if "PatternOnColorCIELabValue" in self._dataset:
            return self._dataset.PatternOnColorCIELabValue
        return None

    @PatternOnColorCIELabValue.setter
    def PatternOnColorCIELabValue(self, value: Optional[List[int]]):
        if value is None:
            if "PatternOnColorCIELabValue" in self._dataset:
                del self._dataset.PatternOnColorCIELabValue
        else:
            self._dataset.PatternOnColorCIELabValue = value

    @property
    def PatternOffColorCIELabValue(self) -> Optional[List[int]]:
        if "PatternOffColorCIELabValue" in self._dataset:
            return self._dataset.PatternOffColorCIELabValue
        return None

    @PatternOffColorCIELabValue.setter
    def PatternOffColorCIELabValue(self, value: Optional[List[int]]):
        if value is None:
            if "PatternOffColorCIELabValue" in self._dataset:
                del self._dataset.PatternOffColorCIELabValue
        else:
            self._dataset.PatternOffColorCIELabValue = value

    @property
    def LineThickness(self) -> Optional[float]:
        if "LineThickness" in self._dataset:
            return self._dataset.LineThickness
        return None

    @LineThickness.setter
    def LineThickness(self, value: Optional[float]):
        if value is None:
            if "LineThickness" in self._dataset:
                del self._dataset.LineThickness
        else:
            self._dataset.LineThickness = value

    @property
    def LineDashingStyle(self) -> Optional[str]:
        if "LineDashingStyle" in self._dataset:
            return self._dataset.LineDashingStyle
        return None

    @LineDashingStyle.setter
    def LineDashingStyle(self, value: Optional[str]):
        if value is None:
            if "LineDashingStyle" in self._dataset:
                del self._dataset.LineDashingStyle
        else:
            self._dataset.LineDashingStyle = value

    @property
    def LinePattern(self) -> Optional[int]:
        if "LinePattern" in self._dataset:
            return self._dataset.LinePattern
        return None

    @LinePattern.setter
    def LinePattern(self, value: Optional[int]):
        if value is None:
            if "LinePattern" in self._dataset:
                del self._dataset.LinePattern
        else:
            self._dataset.LinePattern = value

    @property
    def ShadowOpacity(self) -> Optional[float]:
        if "ShadowOpacity" in self._dataset:
            return self._dataset.ShadowOpacity
        return None

    @ShadowOpacity.setter
    def ShadowOpacity(self, value: Optional[float]):
        if value is None:
            if "ShadowOpacity" in self._dataset:
                del self._dataset.ShadowOpacity
        else:
            self._dataset.ShadowOpacity = value

    @property
    def PatternOnOpacity(self) -> Optional[float]:
        if "PatternOnOpacity" in self._dataset:
            return self._dataset.PatternOnOpacity
        return None

    @PatternOnOpacity.setter
    def PatternOnOpacity(self, value: Optional[float]):
        if value is None:
            if "PatternOnOpacity" in self._dataset:
                del self._dataset.PatternOnOpacity
        else:
            self._dataset.PatternOnOpacity = value

    @property
    def PatternOffOpacity(self) -> Optional[float]:
        if "PatternOffOpacity" in self._dataset:
            return self._dataset.PatternOffOpacity
        return None

    @PatternOffOpacity.setter
    def PatternOffOpacity(self, value: Optional[float]):
        if value is None:
            if "PatternOffOpacity" in self._dataset:
                del self._dataset.PatternOffOpacity
        else:
            self._dataset.PatternOffOpacity = value
