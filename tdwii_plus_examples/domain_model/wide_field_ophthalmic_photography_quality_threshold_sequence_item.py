from typing import Any, List, Optional

import pydicom


class WideFieldOphthalmicPhotographyQualityThresholdSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def WideFieldOphthalmicPhotographyThresholdQualityRating(self) -> Optional[float]:
        if "WideFieldOphthalmicPhotographyThresholdQualityRating" in self._dataset:
            return self._dataset.WideFieldOphthalmicPhotographyThresholdQualityRating
        return None

    @WideFieldOphthalmicPhotographyThresholdQualityRating.setter
    def WideFieldOphthalmicPhotographyThresholdQualityRating(self, value: Optional[float]):
        if value is None:
            if "WideFieldOphthalmicPhotographyThresholdQualityRating" in self._dataset:
                del self._dataset.WideFieldOphthalmicPhotographyThresholdQualityRating
        else:
            self._dataset.WideFieldOphthalmicPhotographyThresholdQualityRating = value
