from typing import Any, List, Optional  # noqa

import pydicom


class TextStyleSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def FontName(self) -> Optional[str]:
        if "FontName" in self._dataset:
            return self._dataset.FontName
        return None

    @FontName.setter
    def FontName(self, value: Optional[str]):
        if value is None:
            if "FontName" in self._dataset:
                del self._dataset.FontName
        else:
            self._dataset.FontName = value

    @property
    def FontNameType(self) -> Optional[str]:
        if "FontNameType" in self._dataset:
            return self._dataset.FontNameType
        return None

    @FontNameType.setter
    def FontNameType(self, value: Optional[str]):
        if value is None:
            if "FontNameType" in self._dataset:
                del self._dataset.FontNameType
        else:
            self._dataset.FontNameType = value

    @property
    def CSSFontName(self) -> Optional[str]:
        if "CSSFontName" in self._dataset:
            return self._dataset.CSSFontName
        return None

    @CSSFontName.setter
    def CSSFontName(self, value: Optional[str]):
        if value is None:
            if "CSSFontName" in self._dataset:
                del self._dataset.CSSFontName
        else:
            self._dataset.CSSFontName = value

    @property
    def TextColorCIELabValue(self) -> Optional[List[int]]:
        if "TextColorCIELabValue" in self._dataset:
            return self._dataset.TextColorCIELabValue
        return None

    @TextColorCIELabValue.setter
    def TextColorCIELabValue(self, value: Optional[List[int]]):
        if value is None:
            if "TextColorCIELabValue" in self._dataset:
                del self._dataset.TextColorCIELabValue
        else:
            self._dataset.TextColorCIELabValue = value

    @property
    def HorizontalAlignment(self) -> Optional[str]:
        if "HorizontalAlignment" in self._dataset:
            return self._dataset.HorizontalAlignment
        return None

    @HorizontalAlignment.setter
    def HorizontalAlignment(self, value: Optional[str]):
        if value is None:
            if "HorizontalAlignment" in self._dataset:
                del self._dataset.HorizontalAlignment
        else:
            self._dataset.HorizontalAlignment = value

    @property
    def VerticalAlignment(self) -> Optional[str]:
        if "VerticalAlignment" in self._dataset:
            return self._dataset.VerticalAlignment
        return None

    @VerticalAlignment.setter
    def VerticalAlignment(self, value: Optional[str]):
        if value is None:
            if "VerticalAlignment" in self._dataset:
                del self._dataset.VerticalAlignment
        else:
            self._dataset.VerticalAlignment = value

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
    def Underlined(self) -> Optional[str]:
        if "Underlined" in self._dataset:
            return self._dataset.Underlined
        return None

    @Underlined.setter
    def Underlined(self, value: Optional[str]):
        if value is None:
            if "Underlined" in self._dataset:
                del self._dataset.Underlined
        else:
            self._dataset.Underlined = value

    @property
    def Bold(self) -> Optional[str]:
        if "Bold" in self._dataset:
            return self._dataset.Bold
        return None

    @Bold.setter
    def Bold(self, value: Optional[str]):
        if value is None:
            if "Bold" in self._dataset:
                del self._dataset.Bold
        else:
            self._dataset.Bold = value

    @property
    def Italic(self) -> Optional[str]:
        if "Italic" in self._dataset:
            return self._dataset.Italic
        return None

    @Italic.setter
    def Italic(self, value: Optional[str]):
        if value is None:
            if "Italic" in self._dataset:
                del self._dataset.Italic
        else:
            self._dataset.Italic = value

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
