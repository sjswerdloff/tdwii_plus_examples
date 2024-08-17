from typing import Any, List, Optional

import pydicom


class ApplicatorGeometrySequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ApplicatorApertureShape(self) -> Optional[str]:
        if "ApplicatorApertureShape" in self._dataset:
            return self._dataset.ApplicatorApertureShape
        return None

    @ApplicatorApertureShape.setter
    def ApplicatorApertureShape(self, value: Optional[str]):
        if value is None:
            if "ApplicatorApertureShape" in self._dataset:
                del self._dataset.ApplicatorApertureShape
        else:
            self._dataset.ApplicatorApertureShape = value

    @property
    def ApplicatorOpening(self) -> Optional[float]:
        if "ApplicatorOpening" in self._dataset:
            return self._dataset.ApplicatorOpening
        return None

    @ApplicatorOpening.setter
    def ApplicatorOpening(self, value: Optional[float]):
        if value is None:
            if "ApplicatorOpening" in self._dataset:
                del self._dataset.ApplicatorOpening
        else:
            self._dataset.ApplicatorOpening = value

    @property
    def ApplicatorOpeningX(self) -> Optional[float]:
        if "ApplicatorOpeningX" in self._dataset:
            return self._dataset.ApplicatorOpeningX
        return None

    @ApplicatorOpeningX.setter
    def ApplicatorOpeningX(self, value: Optional[float]):
        if value is None:
            if "ApplicatorOpeningX" in self._dataset:
                del self._dataset.ApplicatorOpeningX
        else:
            self._dataset.ApplicatorOpeningX = value

    @property
    def ApplicatorOpeningY(self) -> Optional[float]:
        if "ApplicatorOpeningY" in self._dataset:
            return self._dataset.ApplicatorOpeningY
        return None

    @ApplicatorOpeningY.setter
    def ApplicatorOpeningY(self, value: Optional[float]):
        if value is None:
            if "ApplicatorOpeningY" in self._dataset:
                del self._dataset.ApplicatorOpeningY
        else:
            self._dataset.ApplicatorOpeningY = value
