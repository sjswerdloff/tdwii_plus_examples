from typing import Any, List, Optional  # noqa

import pydicom

from .parameters_specification_sequence_item import ParametersSpecificationSequenceItem
from .scan_start_position_sequence_item import ScanStartPositionSequenceItem
from .scan_stop_position_sequence_item import ScanStopPositionSequenceItem


class CTImagingAcquisitionParameterSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._ParametersSpecificationSequence: List[ParametersSpecificationSequenceItem] = []
        self._ScanStartPositionSequence: List[ScanStartPositionSequenceItem] = []
        self._ScanStopPositionSequence: List[ScanStopPositionSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ParametersSpecificationSequence(self) -> Optional[List[ParametersSpecificationSequenceItem]]:
        if "ParametersSpecificationSequence" in self._dataset:
            if len(self._ParametersSpecificationSequence) == len(self._dataset.ParametersSpecificationSequence):
                return self._ParametersSpecificationSequence
            else:
                return [ParametersSpecificationSequenceItem(x) for x in self._dataset.ParametersSpecificationSequence]
        return None

    @ParametersSpecificationSequence.setter
    def ParametersSpecificationSequence(self, value: Optional[List[ParametersSpecificationSequenceItem]]):
        if value is None:
            self._ParametersSpecificationSequence = []
            if "ParametersSpecificationSequence" in self._dataset:
                del self._dataset.ParametersSpecificationSequence
        elif not isinstance(value, list) or not all(isinstance(item, ParametersSpecificationSequenceItem) for item in value):
            raise ValueError("ParametersSpecificationSequence must be a list of ParametersSpecificationSequenceItem objects")
        else:
            self._ParametersSpecificationSequence = value
            if "ParametersSpecificationSequence" not in self._dataset:
                self._dataset.ParametersSpecificationSequence = pydicom.Sequence()
            self._dataset.ParametersSpecificationSequence.clear()
            self._dataset.ParametersSpecificationSequence.extend([item.to_dataset() for item in value])

    def add_ParametersSpecification(self, item: ParametersSpecificationSequenceItem):
        if not isinstance(item, ParametersSpecificationSequenceItem):
            raise ValueError("Item must be an instance of ParametersSpecificationSequenceItem")
        self._ParametersSpecificationSequence.append(item)
        if "ParametersSpecificationSequence" not in self._dataset:
            self._dataset.ParametersSpecificationSequence = pydicom.Sequence()
        self._dataset.ParametersSpecificationSequence.append(item.to_dataset())

    @property
    def ScanStartPositionSequence(self) -> Optional[List[ScanStartPositionSequenceItem]]:
        if "ScanStartPositionSequence" in self._dataset:
            if len(self._ScanStartPositionSequence) == len(self._dataset.ScanStartPositionSequence):
                return self._ScanStartPositionSequence
            else:
                return [ScanStartPositionSequenceItem(x) for x in self._dataset.ScanStartPositionSequence]
        return None

    @ScanStartPositionSequence.setter
    def ScanStartPositionSequence(self, value: Optional[List[ScanStartPositionSequenceItem]]):
        if value is None:
            self._ScanStartPositionSequence = []
            if "ScanStartPositionSequence" in self._dataset:
                del self._dataset.ScanStartPositionSequence
        elif not isinstance(value, list) or not all(isinstance(item, ScanStartPositionSequenceItem) for item in value):
            raise ValueError("ScanStartPositionSequence must be a list of ScanStartPositionSequenceItem objects")
        else:
            self._ScanStartPositionSequence = value
            if "ScanStartPositionSequence" not in self._dataset:
                self._dataset.ScanStartPositionSequence = pydicom.Sequence()
            self._dataset.ScanStartPositionSequence.clear()
            self._dataset.ScanStartPositionSequence.extend([item.to_dataset() for item in value])

    def add_ScanStartPosition(self, item: ScanStartPositionSequenceItem):
        if not isinstance(item, ScanStartPositionSequenceItem):
            raise ValueError("Item must be an instance of ScanStartPositionSequenceItem")
        self._ScanStartPositionSequence.append(item)
        if "ScanStartPositionSequence" not in self._dataset:
            self._dataset.ScanStartPositionSequence = pydicom.Sequence()
        self._dataset.ScanStartPositionSequence.append(item.to_dataset())

    @property
    def ScanStopPositionSequence(self) -> Optional[List[ScanStopPositionSequenceItem]]:
        if "ScanStopPositionSequence" in self._dataset:
            if len(self._ScanStopPositionSequence) == len(self._dataset.ScanStopPositionSequence):
                return self._ScanStopPositionSequence
            else:
                return [ScanStopPositionSequenceItem(x) for x in self._dataset.ScanStopPositionSequence]
        return None

    @ScanStopPositionSequence.setter
    def ScanStopPositionSequence(self, value: Optional[List[ScanStopPositionSequenceItem]]):
        if value is None:
            self._ScanStopPositionSequence = []
            if "ScanStopPositionSequence" in self._dataset:
                del self._dataset.ScanStopPositionSequence
        elif not isinstance(value, list) or not all(isinstance(item, ScanStopPositionSequenceItem) for item in value):
            raise ValueError("ScanStopPositionSequence must be a list of ScanStopPositionSequenceItem objects")
        else:
            self._ScanStopPositionSequence = value
            if "ScanStopPositionSequence" not in self._dataset:
                self._dataset.ScanStopPositionSequence = pydicom.Sequence()
            self._dataset.ScanStopPositionSequence.clear()
            self._dataset.ScanStopPositionSequence.extend([item.to_dataset() for item in value])

    def add_ScanStopPosition(self, item: ScanStopPositionSequenceItem):
        if not isinstance(item, ScanStopPositionSequenceItem):
            raise ValueError("Item must be an instance of ScanStopPositionSequenceItem")
        self._ScanStopPositionSequence.append(item)
        if "ScanStopPositionSequence" not in self._dataset:
            self._dataset.ScanStopPositionSequence = pydicom.Sequence()
        self._dataset.ScanStopPositionSequence.append(item.to_dataset())

    @property
    def ScanArcType(self) -> Optional[str]:
        if "ScanArcType" in self._dataset:
            return self._dataset.ScanArcType
        return None

    @ScanArcType.setter
    def ScanArcType(self, value: Optional[str]):
        if value is None:
            if "ScanArcType" in self._dataset:
                del self._dataset.ScanArcType
        else:
            self._dataset.ScanArcType = value

    @property
    def DetectorPositioningType(self) -> Optional[str]:
        if "DetectorPositioningType" in self._dataset:
            return self._dataset.DetectorPositioningType
        return None

    @DetectorPositioningType.setter
    def DetectorPositioningType(self, value: Optional[str]):
        if value is None:
            if "DetectorPositioningType" in self._dataset:
                del self._dataset.DetectorPositioningType
        else:
            self._dataset.DetectorPositioningType = value
