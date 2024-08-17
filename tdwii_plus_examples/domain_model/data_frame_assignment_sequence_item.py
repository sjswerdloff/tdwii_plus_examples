from decimal import Decimal
from typing import Any, List, Optional  # noqa

import pydicom

from .voilut_sequence_item import VOILUTSequenceItem


class DataFrameAssignmentSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._VOILUTSequence: List[VOILUTSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def DataType(self) -> Optional[str]:
        if "DataType" in self._dataset:
            return self._dataset.DataType
        return None

    @DataType.setter
    def DataType(self, value: Optional[str]):
        if value is None:
            if "DataType" in self._dataset:
                del self._dataset.DataType
        else:
            self._dataset.DataType = value

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

    @property
    def DataPathAssignment(self) -> Optional[str]:
        if "DataPathAssignment" in self._dataset:
            return self._dataset.DataPathAssignment
        return None

    @DataPathAssignment.setter
    def DataPathAssignment(self, value: Optional[str]):
        if value is None:
            if "DataPathAssignment" in self._dataset:
                del self._dataset.DataPathAssignment
        else:
            self._dataset.DataPathAssignment = value

    @property
    def BitsMappedToColorLookupTable(self) -> Optional[int]:
        if "BitsMappedToColorLookupTable" in self._dataset:
            return self._dataset.BitsMappedToColorLookupTable
        return None

    @BitsMappedToColorLookupTable.setter
    def BitsMappedToColorLookupTable(self, value: Optional[int]):
        if value is None:
            if "BitsMappedToColorLookupTable" in self._dataset:
                del self._dataset.BitsMappedToColorLookupTable
        else:
            self._dataset.BitsMappedToColorLookupTable = value

    @property
    def VOILUTSequence(self) -> Optional[List[VOILUTSequenceItem]]:
        if "VOILUTSequence" in self._dataset:
            if len(self._VOILUTSequence) == len(self._dataset.VOILUTSequence):
                return self._VOILUTSequence
            else:
                return [VOILUTSequenceItem(x) for x in self._dataset.VOILUTSequence]
        return None

    @VOILUTSequence.setter
    def VOILUTSequence(self, value: Optional[List[VOILUTSequenceItem]]):
        if value is None:
            self._VOILUTSequence = []
            if "VOILUTSequence" in self._dataset:
                del self._dataset.VOILUTSequence
        elif not isinstance(value, list) or not all(isinstance(item, VOILUTSequenceItem) for item in value):
            raise ValueError("VOILUTSequence must be a list of VOILUTSequenceItem objects")
        else:
            self._VOILUTSequence = value
            if "VOILUTSequence" not in self._dataset:
                self._dataset.VOILUTSequence = pydicom.Sequence()
            self._dataset.VOILUTSequence.clear()
            self._dataset.VOILUTSequence.extend([item.to_dataset() for item in value])

    def add_VOILUT(self, item: VOILUTSequenceItem):
        if not isinstance(item, VOILUTSequenceItem):
            raise ValueError("Item must be an instance of VOILUTSequenceItem")
        self._VOILUTSequence.append(item)
        if "VOILUTSequence" not in self._dataset:
            self._dataset.VOILUTSequence = pydicom.Sequence()
        self._dataset.VOILUTSequence.append(item.to_dataset())
