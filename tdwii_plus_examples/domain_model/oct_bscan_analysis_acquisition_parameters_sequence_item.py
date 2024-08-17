from typing import Any, List, Optional

import pydicom

from .code_sequence_item import CodeSequenceItem


class OCTBscanAnalysisAcquisitionParametersSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._ScanPatternTypeCodeSequence: List[CodeSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ScanPatternTypeCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "ScanPatternTypeCodeSequence" in self._dataset:
            if len(self._ScanPatternTypeCodeSequence) == len(self._dataset.ScanPatternTypeCodeSequence):
                return self._ScanPatternTypeCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.ScanPatternTypeCodeSequence]
        return None

    @ScanPatternTypeCodeSequence.setter
    def ScanPatternTypeCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._ScanPatternTypeCodeSequence = []
            if "ScanPatternTypeCodeSequence" in self._dataset:
                del self._dataset.ScanPatternTypeCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError(f"ScanPatternTypeCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._ScanPatternTypeCodeSequence = value
            if "ScanPatternTypeCodeSequence" not in self._dataset:
                self._dataset.ScanPatternTypeCodeSequence = pydicom.Sequence()
            self._dataset.ScanPatternTypeCodeSequence.clear()
            self._dataset.ScanPatternTypeCodeSequence.extend([item.to_dataset() for item in value])

    def add_ScanPatternTypeCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError(f"Item must be an instance of CodeSequenceItem")
        self._ScanPatternTypeCodeSequence.append(item)
        if "ScanPatternTypeCodeSequence" not in self._dataset:
            self._dataset.ScanPatternTypeCodeSequence = pydicom.Sequence()
        self._dataset.ScanPatternTypeCodeSequence.append(item.to_dataset())

    @property
    def NumberOfBscansPerFrame(self) -> Optional[int]:
        if "NumberOfBscansPerFrame" in self._dataset:
            return self._dataset.NumberOfBscansPerFrame
        return None

    @NumberOfBscansPerFrame.setter
    def NumberOfBscansPerFrame(self, value: Optional[int]):
        if value is None:
            if "NumberOfBscansPerFrame" in self._dataset:
                del self._dataset.NumberOfBscansPerFrame
        else:
            self._dataset.NumberOfBscansPerFrame = value

    @property
    def BscanSlabThickness(self) -> Optional[float]:
        if "BscanSlabThickness" in self._dataset:
            return self._dataset.BscanSlabThickness
        return None

    @BscanSlabThickness.setter
    def BscanSlabThickness(self, value: Optional[float]):
        if value is None:
            if "BscanSlabThickness" in self._dataset:
                del self._dataset.BscanSlabThickness
        else:
            self._dataset.BscanSlabThickness = value

    @property
    def DistanceBetweenBscanSlabs(self) -> Optional[float]:
        if "DistanceBetweenBscanSlabs" in self._dataset:
            return self._dataset.DistanceBetweenBscanSlabs
        return None

    @DistanceBetweenBscanSlabs.setter
    def DistanceBetweenBscanSlabs(self, value: Optional[float]):
        if value is None:
            if "DistanceBetweenBscanSlabs" in self._dataset:
                del self._dataset.DistanceBetweenBscanSlabs
        else:
            self._dataset.DistanceBetweenBscanSlabs = value

    @property
    def BscanCycleTime(self) -> Optional[float]:
        if "BscanCycleTime" in self._dataset:
            return self._dataset.BscanCycleTime
        return None

    @BscanCycleTime.setter
    def BscanCycleTime(self, value: Optional[float]):
        if value is None:
            if "BscanCycleTime" in self._dataset:
                del self._dataset.BscanCycleTime
        else:
            self._dataset.BscanCycleTime = value

    @property
    def BscanCycleTimeVector(self) -> Optional[List[float]]:
        if "BscanCycleTimeVector" in self._dataset:
            return self._dataset.BscanCycleTimeVector
        return None

    @BscanCycleTimeVector.setter
    def BscanCycleTimeVector(self, value: Optional[List[float]]):
        if value is None:
            if "BscanCycleTimeVector" in self._dataset:
                del self._dataset.BscanCycleTimeVector
        else:
            self._dataset.BscanCycleTimeVector = value

    @property
    def AscanRate(self) -> Optional[float]:
        if "AscanRate" in self._dataset:
            return self._dataset.AscanRate
        return None

    @AscanRate.setter
    def AscanRate(self, value: Optional[float]):
        if value is None:
            if "AscanRate" in self._dataset:
                del self._dataset.AscanRate
        else:
            self._dataset.AscanRate = value

    @property
    def BscanRate(self) -> Optional[float]:
        if "BscanRate" in self._dataset:
            return self._dataset.BscanRate
        return None

    @BscanRate.setter
    def BscanRate(self, value: Optional[float]):
        if value is None:
            if "BscanRate" in self._dataset:
                del self._dataset.BscanRate
        else:
            self._dataset.BscanRate = value
