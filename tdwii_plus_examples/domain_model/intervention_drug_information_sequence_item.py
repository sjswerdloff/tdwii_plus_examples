from decimal import Decimal
from typing import Any, List, Optional  # noqa

import pydicom

from .code_sequence_item import CodeSequenceItem


class InterventionDrugInformationSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._InterventionDrugCodeSequence: List[CodeSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def InterventionDrugStopTime(self) -> Optional[str]:
        if "InterventionDrugStopTime" in self._dataset:
            return self._dataset.InterventionDrugStopTime
        return None

    @InterventionDrugStopTime.setter
    def InterventionDrugStopTime(self, value: Optional[str]):
        if value is None:
            if "InterventionDrugStopTime" in self._dataset:
                del self._dataset.InterventionDrugStopTime
        else:
            self._dataset.InterventionDrugStopTime = value

    @property
    def InterventionDrugDose(self) -> Optional[Decimal]:
        if "InterventionDrugDose" in self._dataset:
            return self._dataset.InterventionDrugDose
        return None

    @InterventionDrugDose.setter
    def InterventionDrugDose(self, value: Optional[Decimal]):
        if value is None:
            if "InterventionDrugDose" in self._dataset:
                del self._dataset.InterventionDrugDose
        else:
            self._dataset.InterventionDrugDose = value

    @property
    def InterventionDrugCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "InterventionDrugCodeSequence" in self._dataset:
            if len(self._InterventionDrugCodeSequence) == len(self._dataset.InterventionDrugCodeSequence):
                return self._InterventionDrugCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.InterventionDrugCodeSequence]
        return None

    @InterventionDrugCodeSequence.setter
    def InterventionDrugCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._InterventionDrugCodeSequence = []
            if "InterventionDrugCodeSequence" in self._dataset:
                del self._dataset.InterventionDrugCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("InterventionDrugCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._InterventionDrugCodeSequence = value
            if "InterventionDrugCodeSequence" not in self._dataset:
                self._dataset.InterventionDrugCodeSequence = pydicom.Sequence()
            self._dataset.InterventionDrugCodeSequence.clear()
            self._dataset.InterventionDrugCodeSequence.extend([item.to_dataset() for item in value])

    def add_InterventionDrugCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._InterventionDrugCodeSequence.append(item)
        if "InterventionDrugCodeSequence" not in self._dataset:
            self._dataset.InterventionDrugCodeSequence = pydicom.Sequence()
        self._dataset.InterventionDrugCodeSequence.append(item.to_dataset())

    @property
    def InterventionDrugName(self) -> Optional[str]:
        if "InterventionDrugName" in self._dataset:
            return self._dataset.InterventionDrugName
        return None

    @InterventionDrugName.setter
    def InterventionDrugName(self, value: Optional[str]):
        if value is None:
            if "InterventionDrugName" in self._dataset:
                del self._dataset.InterventionDrugName
        else:
            self._dataset.InterventionDrugName = value

    @property
    def InterventionDrugStartTime(self) -> Optional[str]:
        if "InterventionDrugStartTime" in self._dataset:
            return self._dataset.InterventionDrugStartTime
        return None

    @InterventionDrugStartTime.setter
    def InterventionDrugStartTime(self, value: Optional[str]):
        if value is None:
            if "InterventionDrugStartTime" in self._dataset:
                del self._dataset.InterventionDrugStartTime
        else:
            self._dataset.InterventionDrugStartTime = value
