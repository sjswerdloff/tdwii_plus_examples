from typing import Any, List, Optional

import pydicom


class CalculationCommentSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def CalculationCommentType(self) -> Optional[str]:
        if "CalculationCommentType" in self._dataset:
            return self._dataset.CalculationCommentType
        return None

    @CalculationCommentType.setter
    def CalculationCommentType(self, value: Optional[str]):
        if value is None:
            if "CalculationCommentType" in self._dataset:
                del self._dataset.CalculationCommentType
        else:
            self._dataset.CalculationCommentType = value

    @property
    def CalculationComment(self) -> Optional[str]:
        if "CalculationComment" in self._dataset:
            return self._dataset.CalculationComment
        return None

    @CalculationComment.setter
    def CalculationComment(self, value: Optional[str]):
        if value is None:
            if "CalculationComment" in self._dataset:
                del self._dataset.CalculationComment
        else:
            self._dataset.CalculationComment = value
