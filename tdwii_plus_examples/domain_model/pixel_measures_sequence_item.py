from decimal import Decimal
from typing import Any, List, Optional

import pydicom


class PixelMeasuresSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def SliceThickness(self) -> Optional[Decimal]:
        if "SliceThickness" in self._dataset:
            return self._dataset.SliceThickness
        return None

    @SliceThickness.setter
    def SliceThickness(self, value: Optional[Decimal]):
        if value is None:
            if "SliceThickness" in self._dataset:
                del self._dataset.SliceThickness
        else:
            self._dataset.SliceThickness = value

    @property
    def SpacingBetweenSlices(self) -> Optional[Decimal]:
        if "SpacingBetweenSlices" in self._dataset:
            return self._dataset.SpacingBetweenSlices
        return None

    @SpacingBetweenSlices.setter
    def SpacingBetweenSlices(self, value: Optional[Decimal]):
        if value is None:
            if "SpacingBetweenSlices" in self._dataset:
                del self._dataset.SpacingBetweenSlices
        else:
            self._dataset.SpacingBetweenSlices = value

    @property
    def PixelSpacing(self) -> Optional[List[Decimal]]:
        if "PixelSpacing" in self._dataset:
            return self._dataset.PixelSpacing
        return None

    @PixelSpacing.setter
    def PixelSpacing(self, value: Optional[List[Decimal]]):
        if value is None:
            if "PixelSpacing" in self._dataset:
                del self._dataset.PixelSpacing
        else:
            self._dataset.PixelSpacing = value
