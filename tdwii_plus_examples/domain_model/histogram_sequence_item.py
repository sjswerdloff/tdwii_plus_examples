from typing import Any, List, Optional

import pydicom


class HistogramSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def HistogramNumberOfBins(self) -> Optional[int]:
        if "HistogramNumberOfBins" in self._dataset:
            return self._dataset.HistogramNumberOfBins
        return None

    @HistogramNumberOfBins.setter
    def HistogramNumberOfBins(self, value: Optional[int]):
        if value is None:
            if "HistogramNumberOfBins" in self._dataset:
                del self._dataset.HistogramNumberOfBins
        else:
            self._dataset.HistogramNumberOfBins = value

    @property
    def HistogramFirstBinValue(self) -> Optional[int]:
        if "HistogramFirstBinValue" in self._dataset:
            return self._dataset.HistogramFirstBinValue
        return None

    @HistogramFirstBinValue.setter
    def HistogramFirstBinValue(self, value: Optional[int]):
        if value is None:
            if "HistogramFirstBinValue" in self._dataset:
                del self._dataset.HistogramFirstBinValue
        else:
            self._dataset.HistogramFirstBinValue = value

    @property
    def HistogramLastBinValue(self) -> Optional[int]:
        if "HistogramLastBinValue" in self._dataset:
            return self._dataset.HistogramLastBinValue
        return None

    @HistogramLastBinValue.setter
    def HistogramLastBinValue(self, value: Optional[int]):
        if value is None:
            if "HistogramLastBinValue" in self._dataset:
                del self._dataset.HistogramLastBinValue
        else:
            self._dataset.HistogramLastBinValue = value

    @property
    def HistogramBinWidth(self) -> Optional[int]:
        if "HistogramBinWidth" in self._dataset:
            return self._dataset.HistogramBinWidth
        return None

    @HistogramBinWidth.setter
    def HistogramBinWidth(self, value: Optional[int]):
        if value is None:
            if "HistogramBinWidth" in self._dataset:
                del self._dataset.HistogramBinWidth
        else:
            self._dataset.HistogramBinWidth = value

    @property
    def HistogramExplanation(self) -> Optional[str]:
        if "HistogramExplanation" in self._dataset:
            return self._dataset.HistogramExplanation
        return None

    @HistogramExplanation.setter
    def HistogramExplanation(self, value: Optional[str]):
        if value is None:
            if "HistogramExplanation" in self._dataset:
                del self._dataset.HistogramExplanation
        else:
            self._dataset.HistogramExplanation = value

    @property
    def HistogramData(self) -> Optional[List[int]]:
        if "HistogramData" in self._dataset:
            return self._dataset.HistogramData
        return None

    @HistogramData.setter
    def HistogramData(self, value: Optional[List[int]]):
        if value is None:
            if "HistogramData" in self._dataset:
                del self._dataset.HistogramData
        else:
            self._dataset.HistogramData = value
