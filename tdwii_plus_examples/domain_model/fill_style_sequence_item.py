from typing import Any, List, Optional  # noqa

import pydicom


class FillStyleSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

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
    def FillPattern(self) -> Optional[bytes]:
        if "FillPattern" in self._dataset:
            return self._dataset.FillPattern
        return None

    @FillPattern.setter
    def FillPattern(self, value: Optional[bytes]):
        if value is None:
            if "FillPattern" in self._dataset:
                del self._dataset.FillPattern
        else:
            self._dataset.FillPattern = value

    @property
    def FillMode(self) -> Optional[str]:
        if "FillMode" in self._dataset:
            return self._dataset.FillMode
        return None

    @FillMode.setter
    def FillMode(self, value: Optional[str]):
        if value is None:
            if "FillMode" in self._dataset:
                del self._dataset.FillMode
        else:
            self._dataset.FillMode = value

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
