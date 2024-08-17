from typing import Any, List, Optional  # noqa

import pydicom

from .contour_image_sequence_item import ContourImageSequenceItem


class RTReferencedSeriesSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._ContourImageSequence: List[ContourImageSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def SeriesInstanceUID(self) -> Optional[str]:
        if "SeriesInstanceUID" in self._dataset:
            return self._dataset.SeriesInstanceUID
        return None

    @SeriesInstanceUID.setter
    def SeriesInstanceUID(self, value: Optional[str]):
        if value is None:
            if "SeriesInstanceUID" in self._dataset:
                del self._dataset.SeriesInstanceUID
        else:
            self._dataset.SeriesInstanceUID = value

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
