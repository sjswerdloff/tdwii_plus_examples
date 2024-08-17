from decimal import Decimal
from typing import Any, List, Optional

import pydicom

from .code_sequence_item import CodeSequenceItem


class AcquisitionStartLocationSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._ReferenceBasisCodeSequence: List[CodeSequenceItem] = []
        self._ReferenceGeometryCodeSequence: List[CodeSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ReferenceLocationLabel(self) -> Optional[str]:
        if "ReferenceLocationLabel" in self._dataset:
            return self._dataset.ReferenceLocationLabel
        return None

    @ReferenceLocationLabel.setter
    def ReferenceLocationLabel(self, value: Optional[str]):
        if value is None:
            if "ReferenceLocationLabel" in self._dataset:
                del self._dataset.ReferenceLocationLabel
        else:
            self._dataset.ReferenceLocationLabel = value

    @property
    def ReferenceLocationDescription(self) -> Optional[str]:
        if "ReferenceLocationDescription" in self._dataset:
            return self._dataset.ReferenceLocationDescription
        return None

    @ReferenceLocationDescription.setter
    def ReferenceLocationDescription(self, value: Optional[str]):
        if value is None:
            if "ReferenceLocationDescription" in self._dataset:
                del self._dataset.ReferenceLocationDescription
        else:
            self._dataset.ReferenceLocationDescription = value

    @property
    def ReferenceBasisCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "ReferenceBasisCodeSequence" in self._dataset:
            if len(self._ReferenceBasisCodeSequence) == len(self._dataset.ReferenceBasisCodeSequence):
                return self._ReferenceBasisCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.ReferenceBasisCodeSequence]
        return None

    @ReferenceBasisCodeSequence.setter
    def ReferenceBasisCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._ReferenceBasisCodeSequence = []
            if "ReferenceBasisCodeSequence" in self._dataset:
                del self._dataset.ReferenceBasisCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError(f"ReferenceBasisCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._ReferenceBasisCodeSequence = value
            if "ReferenceBasisCodeSequence" not in self._dataset:
                self._dataset.ReferenceBasisCodeSequence = pydicom.Sequence()
            self._dataset.ReferenceBasisCodeSequence.clear()
            self._dataset.ReferenceBasisCodeSequence.extend([item.to_dataset() for item in value])

    def add_ReferenceBasisCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError(f"Item must be an instance of CodeSequenceItem")
        self._ReferenceBasisCodeSequence.append(item)
        if "ReferenceBasisCodeSequence" not in self._dataset:
            self._dataset.ReferenceBasisCodeSequence = pydicom.Sequence()
        self._dataset.ReferenceBasisCodeSequence.append(item.to_dataset())

    @property
    def ReferenceGeometryCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "ReferenceGeometryCodeSequence" in self._dataset:
            if len(self._ReferenceGeometryCodeSequence) == len(self._dataset.ReferenceGeometryCodeSequence):
                return self._ReferenceGeometryCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.ReferenceGeometryCodeSequence]
        return None

    @ReferenceGeometryCodeSequence.setter
    def ReferenceGeometryCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._ReferenceGeometryCodeSequence = []
            if "ReferenceGeometryCodeSequence" in self._dataset:
                del self._dataset.ReferenceGeometryCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError(f"ReferenceGeometryCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._ReferenceGeometryCodeSequence = value
            if "ReferenceGeometryCodeSequence" not in self._dataset:
                self._dataset.ReferenceGeometryCodeSequence = pydicom.Sequence()
            self._dataset.ReferenceGeometryCodeSequence.clear()
            self._dataset.ReferenceGeometryCodeSequence.extend([item.to_dataset() for item in value])

    def add_ReferenceGeometryCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError(f"Item must be an instance of CodeSequenceItem")
        self._ReferenceGeometryCodeSequence.append(item)
        if "ReferenceGeometryCodeSequence" not in self._dataset:
            self._dataset.ReferenceGeometryCodeSequence = pydicom.Sequence()
        self._dataset.ReferenceGeometryCodeSequence.append(item.to_dataset())

    @property
    def OffsetDistance(self) -> Optional[Decimal]:
        if "OffsetDistance" in self._dataset:
            return self._dataset.OffsetDistance
        return None

    @OffsetDistance.setter
    def OffsetDistance(self, value: Optional[Decimal]):
        if value is None:
            if "OffsetDistance" in self._dataset:
                del self._dataset.OffsetDistance
        else:
            self._dataset.OffsetDistance = value

    @property
    def OffsetDirection(self) -> Optional[str]:
        if "OffsetDirection" in self._dataset:
            return self._dataset.OffsetDirection
        return None

    @OffsetDirection.setter
    def OffsetDirection(self, value: Optional[str]):
        if value is None:
            if "OffsetDirection" in self._dataset:
                del self._dataset.OffsetDirection
        else:
            self._dataset.OffsetDirection = value
