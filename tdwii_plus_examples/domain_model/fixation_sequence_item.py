from typing import Any, List, Optional  # noqa

import pydicom

from .code_sequence_item import CodeSequenceItem


class FixationSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._FixationMonitoringCodeSequence: List[CodeSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def FixationMonitoringCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "FixationMonitoringCodeSequence" in self._dataset:
            if len(self._FixationMonitoringCodeSequence) == len(self._dataset.FixationMonitoringCodeSequence):
                return self._FixationMonitoringCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.FixationMonitoringCodeSequence]
        return None

    @FixationMonitoringCodeSequence.setter
    def FixationMonitoringCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._FixationMonitoringCodeSequence = []
            if "FixationMonitoringCodeSequence" in self._dataset:
                del self._dataset.FixationMonitoringCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("FixationMonitoringCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._FixationMonitoringCodeSequence = value
            if "FixationMonitoringCodeSequence" not in self._dataset:
                self._dataset.FixationMonitoringCodeSequence = pydicom.Sequence()
            self._dataset.FixationMonitoringCodeSequence.clear()
            self._dataset.FixationMonitoringCodeSequence.extend([item.to_dataset() for item in value])

    def add_FixationMonitoringCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._FixationMonitoringCodeSequence.append(item)
        if "FixationMonitoringCodeSequence" not in self._dataset:
            self._dataset.FixationMonitoringCodeSequence = pydicom.Sequence()
        self._dataset.FixationMonitoringCodeSequence.append(item.to_dataset())

    @property
    def FixationCheckedQuantity(self) -> Optional[int]:
        if "FixationCheckedQuantity" in self._dataset:
            return self._dataset.FixationCheckedQuantity
        return None

    @FixationCheckedQuantity.setter
    def FixationCheckedQuantity(self, value: Optional[int]):
        if value is None:
            if "FixationCheckedQuantity" in self._dataset:
                del self._dataset.FixationCheckedQuantity
        else:
            self._dataset.FixationCheckedQuantity = value

    @property
    def PatientNotProperlyFixatedQuantity(self) -> Optional[int]:
        if "PatientNotProperlyFixatedQuantity" in self._dataset:
            return self._dataset.PatientNotProperlyFixatedQuantity
        return None

    @PatientNotProperlyFixatedQuantity.setter
    def PatientNotProperlyFixatedQuantity(self, value: Optional[int]):
        if value is None:
            if "PatientNotProperlyFixatedQuantity" in self._dataset:
                del self._dataset.PatientNotProperlyFixatedQuantity
        else:
            self._dataset.PatientNotProperlyFixatedQuantity = value

    @property
    def ExcessiveFixationLossesDataFlag(self) -> Optional[str]:
        if "ExcessiveFixationLossesDataFlag" in self._dataset:
            return self._dataset.ExcessiveFixationLossesDataFlag
        return None

    @ExcessiveFixationLossesDataFlag.setter
    def ExcessiveFixationLossesDataFlag(self, value: Optional[str]):
        if value is None:
            if "ExcessiveFixationLossesDataFlag" in self._dataset:
                del self._dataset.ExcessiveFixationLossesDataFlag
        else:
            self._dataset.ExcessiveFixationLossesDataFlag = value

    @property
    def ExcessiveFixationLosses(self) -> Optional[str]:
        if "ExcessiveFixationLosses" in self._dataset:
            return self._dataset.ExcessiveFixationLosses
        return None

    @ExcessiveFixationLosses.setter
    def ExcessiveFixationLosses(self, value: Optional[str]):
        if value is None:
            if "ExcessiveFixationLosses" in self._dataset:
                del self._dataset.ExcessiveFixationLosses
        else:
            self._dataset.ExcessiveFixationLosses = value
