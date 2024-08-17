from typing import Any, List, Optional  # noqa

import pydicom

from .rt_beam_delimiter_geometry_sequence_item import (
    RTBeamDelimiterGeometrySequenceItem,
)


class RTBeamLimitingDeviceOpeningSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._RTBeamDelimiterGeometrySequence: List[RTBeamDelimiterGeometrySequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ReferencedDeviceIndex(self) -> Optional[int]:
        if "ReferencedDeviceIndex" in self._dataset:
            return self._dataset.ReferencedDeviceIndex
        return None

    @ReferencedDeviceIndex.setter
    def ReferencedDeviceIndex(self, value: Optional[int]):
        if value is None:
            if "ReferencedDeviceIndex" in self._dataset:
                del self._dataset.ReferencedDeviceIndex
        else:
            self._dataset.ReferencedDeviceIndex = value

    @property
    def ParallelRTBeamDelimiterPositions(self) -> Optional[List[float]]:
        if "ParallelRTBeamDelimiterPositions" in self._dataset:
            return self._dataset.ParallelRTBeamDelimiterPositions
        return None

    @ParallelRTBeamDelimiterPositions.setter
    def ParallelRTBeamDelimiterPositions(self, value: Optional[List[float]]):
        if value is None:
            if "ParallelRTBeamDelimiterPositions" in self._dataset:
                del self._dataset.ParallelRTBeamDelimiterPositions
        else:
            self._dataset.ParallelRTBeamDelimiterPositions = value

    @property
    def RTBeamLimitingDeviceOffset(self) -> Optional[List[float]]:
        if "RTBeamLimitingDeviceOffset" in self._dataset:
            return self._dataset.RTBeamLimitingDeviceOffset
        return None

    @RTBeamLimitingDeviceOffset.setter
    def RTBeamLimitingDeviceOffset(self, value: Optional[List[float]]):
        if value is None:
            if "RTBeamLimitingDeviceOffset" in self._dataset:
                del self._dataset.RTBeamLimitingDeviceOffset
        else:
            self._dataset.RTBeamLimitingDeviceOffset = value

    @property
    def RTBeamDelimiterGeometrySequence(self) -> Optional[List[RTBeamDelimiterGeometrySequenceItem]]:
        if "RTBeamDelimiterGeometrySequence" in self._dataset:
            if len(self._RTBeamDelimiterGeometrySequence) == len(self._dataset.RTBeamDelimiterGeometrySequence):
                return self._RTBeamDelimiterGeometrySequence
            else:
                return [RTBeamDelimiterGeometrySequenceItem(x) for x in self._dataset.RTBeamDelimiterGeometrySequence]
        return None

    @RTBeamDelimiterGeometrySequence.setter
    def RTBeamDelimiterGeometrySequence(self, value: Optional[List[RTBeamDelimiterGeometrySequenceItem]]):
        if value is None:
            self._RTBeamDelimiterGeometrySequence = []
            if "RTBeamDelimiterGeometrySequence" in self._dataset:
                del self._dataset.RTBeamDelimiterGeometrySequence
        elif not isinstance(value, list) or not all(isinstance(item, RTBeamDelimiterGeometrySequenceItem) for item in value):
            raise ValueError("RTBeamDelimiterGeometrySequence must be a list of RTBeamDelimiterGeometrySequenceItem objects")
        else:
            self._RTBeamDelimiterGeometrySequence = value
            if "RTBeamDelimiterGeometrySequence" not in self._dataset:
                self._dataset.RTBeamDelimiterGeometrySequence = pydicom.Sequence()
            self._dataset.RTBeamDelimiterGeometrySequence.clear()
            self._dataset.RTBeamDelimiterGeometrySequence.extend([item.to_dataset() for item in value])

    def add_RTBeamDelimiterGeometry(self, item: RTBeamDelimiterGeometrySequenceItem):
        if not isinstance(item, RTBeamDelimiterGeometrySequenceItem):
            raise ValueError("Item must be an instance of RTBeamDelimiterGeometrySequenceItem")
        self._RTBeamDelimiterGeometrySequence.append(item)
        if "RTBeamDelimiterGeometrySequence" not in self._dataset:
            self._dataset.RTBeamDelimiterGeometrySequence = pydicom.Sequence()
        self._dataset.RTBeamDelimiterGeometrySequence.append(item.to_dataset())
