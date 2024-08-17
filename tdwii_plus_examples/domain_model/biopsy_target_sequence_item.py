from typing import Any, List, Optional  # noqa

import pydicom


class BiopsyTargetSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def TargetUID(self) -> Optional[str]:
        if "TargetUID" in self._dataset:
            return self._dataset.TargetUID
        return None

    @TargetUID.setter
    def TargetUID(self, value: Optional[str]):
        if value is None:
            if "TargetUID" in self._dataset:
                del self._dataset.TargetUID
        else:
            self._dataset.TargetUID = value

    @property
    def LocalizingCursorPosition(self) -> Optional[List[float]]:
        if "LocalizingCursorPosition" in self._dataset:
            return self._dataset.LocalizingCursorPosition
        return None

    @LocalizingCursorPosition.setter
    def LocalizingCursorPosition(self, value: Optional[List[float]]):
        if value is None:
            if "LocalizingCursorPosition" in self._dataset:
                del self._dataset.LocalizingCursorPosition
        else:
            self._dataset.LocalizingCursorPosition = value

    @property
    def CalculatedTargetPosition(self) -> Optional[List[float]]:
        if "CalculatedTargetPosition" in self._dataset:
            return self._dataset.CalculatedTargetPosition
        return None

    @CalculatedTargetPosition.setter
    def CalculatedTargetPosition(self, value: Optional[List[float]]):
        if value is None:
            if "CalculatedTargetPosition" in self._dataset:
                del self._dataset.CalculatedTargetPosition
        else:
            self._dataset.CalculatedTargetPosition = value

    @property
    def TargetLabel(self) -> Optional[str]:
        if "TargetLabel" in self._dataset:
            return self._dataset.TargetLabel
        return None

    @TargetLabel.setter
    def TargetLabel(self, value: Optional[str]):
        if value is None:
            if "TargetLabel" in self._dataset:
                del self._dataset.TargetLabel
        else:
            self._dataset.TargetLabel = value

    @property
    def DisplayedZValue(self) -> Optional[float]:
        if "DisplayedZValue" in self._dataset:
            return self._dataset.DisplayedZValue
        return None

    @DisplayedZValue.setter
    def DisplayedZValue(self, value: Optional[float]):
        if value is None:
            if "DisplayedZValue" in self._dataset:
                del self._dataset.DisplayedZValue
        else:
            self._dataset.DisplayedZValue = value
