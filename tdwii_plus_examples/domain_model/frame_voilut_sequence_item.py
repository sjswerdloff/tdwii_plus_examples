from decimal import Decimal
from typing import Any, List, Optional

import pydicom


class FrameVOILUTSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def WindowCenter(self) -> Optional[List[Decimal]]:
        if "WindowCenter" in self._dataset:
            return self._dataset.WindowCenter
        return None

    @WindowCenter.setter
    def WindowCenter(self, value: Optional[List[Decimal]]):
        if value is None:
            if "WindowCenter" in self._dataset:
                del self._dataset.WindowCenter
        else:
            self._dataset.WindowCenter = value

    @property
    def WindowWidth(self) -> Optional[List[Decimal]]:
        if "WindowWidth" in self._dataset:
            return self._dataset.WindowWidth
        return None

    @WindowWidth.setter
    def WindowWidth(self, value: Optional[List[Decimal]]):
        if value is None:
            if "WindowWidth" in self._dataset:
                del self._dataset.WindowWidth
        else:
            self._dataset.WindowWidth = value

    @property
    def WindowCenterWidthExplanation(self) -> Optional[List[str]]:
        if "WindowCenterWidthExplanation" in self._dataset:
            return self._dataset.WindowCenterWidthExplanation
        return None

    @WindowCenterWidthExplanation.setter
    def WindowCenterWidthExplanation(self, value: Optional[List[str]]):
        if value is None:
            if "WindowCenterWidthExplanation" in self._dataset:
                del self._dataset.WindowCenterWidthExplanation
        else:
            self._dataset.WindowCenterWidthExplanation = value

    @property
    def VOILUTFunction(self) -> Optional[str]:
        if "VOILUTFunction" in self._dataset:
            return self._dataset.VOILUTFunction
        return None

    @VOILUTFunction.setter
    def VOILUTFunction(self, value: Optional[str]):
        if value is None:
            if "VOILUTFunction" in self._dataset:
                del self._dataset.VOILUTFunction
        else:
            self._dataset.VOILUTFunction = value
