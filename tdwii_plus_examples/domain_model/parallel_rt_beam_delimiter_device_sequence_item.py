from typing import Any, List, Optional  # noqa

import pydicom

from .code_sequence_item import CodeSequenceItem


class ParallelRTBeamDelimiterDeviceSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._ParallelRTBeamDelimiterDeviceOrientationLabelCodeSequence: List[CodeSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ParallelRTBeamDelimiterOpeningExtents(self) -> Optional[List[float]]:
        if "ParallelRTBeamDelimiterOpeningExtents" in self._dataset:
            return self._dataset.ParallelRTBeamDelimiterOpeningExtents
        return None

    @ParallelRTBeamDelimiterOpeningExtents.setter
    def ParallelRTBeamDelimiterOpeningExtents(self, value: Optional[List[float]]):
        if value is None:
            if "ParallelRTBeamDelimiterOpeningExtents" in self._dataset:
                del self._dataset.ParallelRTBeamDelimiterOpeningExtents
        else:
            self._dataset.ParallelRTBeamDelimiterOpeningExtents = value

    @property
    def ParallelRTBeamDelimiterDeviceOrientationLabelCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "ParallelRTBeamDelimiterDeviceOrientationLabelCodeSequence" in self._dataset:
            if len(self._ParallelRTBeamDelimiterDeviceOrientationLabelCodeSequence) == len(
                self._dataset.ParallelRTBeamDelimiterDeviceOrientationLabelCodeSequence
            ):
                return self._ParallelRTBeamDelimiterDeviceOrientationLabelCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.ParallelRTBeamDelimiterDeviceOrientationLabelCodeSequence]
        return None

    @ParallelRTBeamDelimiterDeviceOrientationLabelCodeSequence.setter
    def ParallelRTBeamDelimiterDeviceOrientationLabelCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._ParallelRTBeamDelimiterDeviceOrientationLabelCodeSequence = []
            if "ParallelRTBeamDelimiterDeviceOrientationLabelCodeSequence" in self._dataset:
                del self._dataset.ParallelRTBeamDelimiterDeviceOrientationLabelCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError(
                "ParallelRTBeamDelimiterDeviceOrientationLabelCodeSequence must be a list of CodeSequenceItem objects"
            )
        else:
            self._ParallelRTBeamDelimiterDeviceOrientationLabelCodeSequence = value
            if "ParallelRTBeamDelimiterDeviceOrientationLabelCodeSequence" not in self._dataset:
                self._dataset.ParallelRTBeamDelimiterDeviceOrientationLabelCodeSequence = pydicom.Sequence()
            self._dataset.ParallelRTBeamDelimiterDeviceOrientationLabelCodeSequence.clear()
            self._dataset.ParallelRTBeamDelimiterDeviceOrientationLabelCodeSequence.extend(
                [item.to_dataset() for item in value]
            )

    def add_ParallelRTBeamDelimiterDeviceOrientationLabelCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._ParallelRTBeamDelimiterDeviceOrientationLabelCodeSequence.append(item)
        if "ParallelRTBeamDelimiterDeviceOrientationLabelCodeSequence" not in self._dataset:
            self._dataset.ParallelRTBeamDelimiterDeviceOrientationLabelCodeSequence = pydicom.Sequence()
        self._dataset.ParallelRTBeamDelimiterDeviceOrientationLabelCodeSequence.append(item.to_dataset())

    @property
    def NumberOfParallelRTBeamDelimiters(self) -> Optional[int]:
        if "NumberOfParallelRTBeamDelimiters" in self._dataset:
            return self._dataset.NumberOfParallelRTBeamDelimiters
        return None

    @NumberOfParallelRTBeamDelimiters.setter
    def NumberOfParallelRTBeamDelimiters(self, value: Optional[int]):
        if value is None:
            if "NumberOfParallelRTBeamDelimiters" in self._dataset:
                del self._dataset.NumberOfParallelRTBeamDelimiters
        else:
            self._dataset.NumberOfParallelRTBeamDelimiters = value

    @property
    def ParallelRTBeamDelimiterBoundaries(self) -> Optional[List[float]]:
        if "ParallelRTBeamDelimiterBoundaries" in self._dataset:
            return self._dataset.ParallelRTBeamDelimiterBoundaries
        return None

    @ParallelRTBeamDelimiterBoundaries.setter
    def ParallelRTBeamDelimiterBoundaries(self, value: Optional[List[float]]):
        if value is None:
            if "ParallelRTBeamDelimiterBoundaries" in self._dataset:
                del self._dataset.ParallelRTBeamDelimiterBoundaries
        else:
            self._dataset.ParallelRTBeamDelimiterBoundaries = value

    @property
    def ParallelRTBeamDelimiterOpeningMode(self) -> Optional[str]:
        if "ParallelRTBeamDelimiterOpeningMode" in self._dataset:
            return self._dataset.ParallelRTBeamDelimiterOpeningMode
        return None

    @ParallelRTBeamDelimiterOpeningMode.setter
    def ParallelRTBeamDelimiterOpeningMode(self, value: Optional[str]):
        if value is None:
            if "ParallelRTBeamDelimiterOpeningMode" in self._dataset:
                del self._dataset.ParallelRTBeamDelimiterOpeningMode
        else:
            self._dataset.ParallelRTBeamDelimiterOpeningMode = value

    @property
    def ParallelRTBeamDelimiterLeafMountingSide(self) -> Optional[List[str]]:
        if "ParallelRTBeamDelimiterLeafMountingSide" in self._dataset:
            return self._dataset.ParallelRTBeamDelimiterLeafMountingSide
        return None

    @ParallelRTBeamDelimiterLeafMountingSide.setter
    def ParallelRTBeamDelimiterLeafMountingSide(self, value: Optional[List[str]]):
        if value is None:
            if "ParallelRTBeamDelimiterLeafMountingSide" in self._dataset:
                del self._dataset.ParallelRTBeamDelimiterLeafMountingSide
        else:
            self._dataset.ParallelRTBeamDelimiterLeafMountingSide = value
