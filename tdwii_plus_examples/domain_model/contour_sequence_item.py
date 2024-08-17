from decimal import Decimal
from typing import Any, List, Optional  # noqa

import pydicom

from .contour_image_sequence_item import ContourImageSequenceItem


class ContourSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._ContourImageSequence: List[ContourImageSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ContourImageSequence(self) -> Optional[List[ContourImageSequenceItem]]:
        if "ContourImageSequence" in self._dataset:
            if len(self._ContourImageSequence) == len(self._dataset.ContourImageSequence):
                return self._ContourImageSequence
            else:
                return [ContourImageSequenceItem(x) for x in self._dataset.ContourImageSequence]
        return None

    @ContourImageSequence.setter
    def ContourImageSequence(self, value: Optional[List[ContourImageSequenceItem]]):
        if value is None:
            self._ContourImageSequence = []
            if "ContourImageSequence" in self._dataset:
                del self._dataset.ContourImageSequence
        elif not isinstance(value, list) or not all(isinstance(item, ContourImageSequenceItem) for item in value):
            raise ValueError("ContourImageSequence must be a list of ContourImageSequenceItem objects")
        else:
            self._ContourImageSequence = value
            if "ContourImageSequence" not in self._dataset:
                self._dataset.ContourImageSequence = pydicom.Sequence()
            self._dataset.ContourImageSequence.clear()
            self._dataset.ContourImageSequence.extend([item.to_dataset() for item in value])

    def add_ContourImage(self, item: ContourImageSequenceItem):
        if not isinstance(item, ContourImageSequenceItem):
            raise ValueError("Item must be an instance of ContourImageSequenceItem")
        self._ContourImageSequence.append(item)
        if "ContourImageSequence" not in self._dataset:
            self._dataset.ContourImageSequence = pydicom.Sequence()
        self._dataset.ContourImageSequence.append(item.to_dataset())

    @property
    def ContourGeometricType(self) -> Optional[str]:
        if "ContourGeometricType" in self._dataset:
            return self._dataset.ContourGeometricType
        return None

    @ContourGeometricType.setter
    def ContourGeometricType(self, value: Optional[str]):
        if value is None:
            if "ContourGeometricType" in self._dataset:
                del self._dataset.ContourGeometricType
        else:
            self._dataset.ContourGeometricType = value

    @property
    def NumberOfContourPoints(self) -> Optional[int]:
        if "NumberOfContourPoints" in self._dataset:
            return self._dataset.NumberOfContourPoints
        return None

    @NumberOfContourPoints.setter
    def NumberOfContourPoints(self, value: Optional[int]):
        if value is None:
            if "NumberOfContourPoints" in self._dataset:
                del self._dataset.NumberOfContourPoints
        else:
            self._dataset.NumberOfContourPoints = value

    @property
    def ContourNumber(self) -> Optional[int]:
        if "ContourNumber" in self._dataset:
            return self._dataset.ContourNumber
        return None

    @ContourNumber.setter
    def ContourNumber(self, value: Optional[int]):
        if value is None:
            if "ContourNumber" in self._dataset:
                del self._dataset.ContourNumber
        else:
            self._dataset.ContourNumber = value

    @property
    def ContourData(self) -> Optional[List[Decimal]]:
        if "ContourData" in self._dataset:
            return self._dataset.ContourData
        return None

    @ContourData.setter
    def ContourData(self, value: Optional[List[Decimal]]):
        if value is None:
            if "ContourData" in self._dataset:
                del self._dataset.ContourData
        else:
            self._dataset.ContourData = value
