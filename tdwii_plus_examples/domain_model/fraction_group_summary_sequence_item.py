from typing import Any, List, Optional  # noqa

import pydicom

from .fraction_status_summary_sequence_item import FractionStatusSummarySequenceItem


class FractionGroupSummarySequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._FractionStatusSummarySequence: List[FractionStatusSummarySequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def NumberOfFractionsDelivered(self) -> Optional[int]:
        if "NumberOfFractionsDelivered" in self._dataset:
            return self._dataset.NumberOfFractionsDelivered
        return None

    @NumberOfFractionsDelivered.setter
    def NumberOfFractionsDelivered(self, value: Optional[int]):
        if value is None:
            if "NumberOfFractionsDelivered" in self._dataset:
                del self._dataset.NumberOfFractionsDelivered
        else:
            self._dataset.NumberOfFractionsDelivered = value

    @property
    def FractionGroupType(self) -> Optional[str]:
        if "FractionGroupType" in self._dataset:
            return self._dataset.FractionGroupType
        return None

    @FractionGroupType.setter
    def FractionGroupType(self, value: Optional[str]):
        if value is None:
            if "FractionGroupType" in self._dataset:
                del self._dataset.FractionGroupType
        else:
            self._dataset.FractionGroupType = value

    @property
    def FractionStatusSummarySequence(self) -> Optional[List[FractionStatusSummarySequenceItem]]:
        if "FractionStatusSummarySequence" in self._dataset:
            if len(self._FractionStatusSummarySequence) == len(self._dataset.FractionStatusSummarySequence):
                return self._FractionStatusSummarySequence
            else:
                return [FractionStatusSummarySequenceItem(x) for x in self._dataset.FractionStatusSummarySequence]
        return None

    @FractionStatusSummarySequence.setter
    def FractionStatusSummarySequence(self, value: Optional[List[FractionStatusSummarySequenceItem]]):
        if value is None:
            self._FractionStatusSummarySequence = []
            if "FractionStatusSummarySequence" in self._dataset:
                del self._dataset.FractionStatusSummarySequence
        elif not isinstance(value, list) or not all(isinstance(item, FractionStatusSummarySequenceItem) for item in value):
            raise ValueError("FractionStatusSummarySequence must be a list of FractionStatusSummarySequenceItem objects")
        else:
            self._FractionStatusSummarySequence = value
            if "FractionStatusSummarySequence" not in self._dataset:
                self._dataset.FractionStatusSummarySequence = pydicom.Sequence()
            self._dataset.FractionStatusSummarySequence.clear()
            self._dataset.FractionStatusSummarySequence.extend([item.to_dataset() for item in value])

    def add_FractionStatusSummary(self, item: FractionStatusSummarySequenceItem):
        if not isinstance(item, FractionStatusSummarySequenceItem):
            raise ValueError("Item must be an instance of FractionStatusSummarySequenceItem")
        self._FractionStatusSummarySequence.append(item)
        if "FractionStatusSummarySequence" not in self._dataset:
            self._dataset.FractionStatusSummarySequence = pydicom.Sequence()
        self._dataset.FractionStatusSummarySequence.append(item.to_dataset())

    @property
    def NumberOfFractionsPlanned(self) -> Optional[int]:
        if "NumberOfFractionsPlanned" in self._dataset:
            return self._dataset.NumberOfFractionsPlanned
        return None

    @NumberOfFractionsPlanned.setter
    def NumberOfFractionsPlanned(self, value: Optional[int]):
        if value is None:
            if "NumberOfFractionsPlanned" in self._dataset:
                del self._dataset.NumberOfFractionsPlanned
        else:
            self._dataset.NumberOfFractionsPlanned = value

    @property
    def ReferencedFractionGroupNumber(self) -> Optional[int]:
        if "ReferencedFractionGroupNumber" in self._dataset:
            return self._dataset.ReferencedFractionGroupNumber
        return None

    @ReferencedFractionGroupNumber.setter
    def ReferencedFractionGroupNumber(self, value: Optional[int]):
        if value is None:
            if "ReferencedFractionGroupNumber" in self._dataset:
                del self._dataset.ReferencedFractionGroupNumber
        else:
            self._dataset.ReferencedFractionGroupNumber = value
