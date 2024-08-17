from typing import Any, List, Optional

import pydicom


class IntravascularOCTFrameContentSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def OCTZOffsetCorrection(self) -> Optional[int]:
        if "OCTZOffsetCorrection" in self._dataset:
            return self._dataset.OCTZOffsetCorrection
        return None

    @OCTZOffsetCorrection.setter
    def OCTZOffsetCorrection(self, value: Optional[int]):
        if value is None:
            if "OCTZOffsetCorrection" in self._dataset:
                del self._dataset.OCTZOffsetCorrection
        else:
            self._dataset.OCTZOffsetCorrection = value

    @property
    def SeamLineIndex(self) -> Optional[int]:
        if "SeamLineIndex" in self._dataset:
            return self._dataset.SeamLineIndex
        return None

    @SeamLineIndex.setter
    def SeamLineIndex(self, value: Optional[int]):
        if value is None:
            if "SeamLineIndex" in self._dataset:
                del self._dataset.SeamLineIndex
        else:
            self._dataset.SeamLineIndex = value

    @property
    def NumberOfPaddedALines(self) -> Optional[int]:
        if "NumberOfPaddedALines" in self._dataset:
            return self._dataset.NumberOfPaddedALines
        return None

    @NumberOfPaddedALines.setter
    def NumberOfPaddedALines(self, value: Optional[int]):
        if value is None:
            if "NumberOfPaddedALines" in self._dataset:
                del self._dataset.NumberOfPaddedALines
        else:
            self._dataset.NumberOfPaddedALines = value
