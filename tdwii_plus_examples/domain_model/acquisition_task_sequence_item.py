from typing import Any, List, Optional  # noqa

import pydicom

from .acquisition_subtask_sequence_item import AcquisitionSubtaskSequenceItem
from .acquisition_task_applicability_sequence_item import (
    AcquisitionTaskApplicabilitySequenceItem,
)
from .code_sequence_item import CodeSequenceItem
from .rt_acquisition_patient_position_sequence_item import (
    RTAcquisitionPatientPositionSequenceItem,
)


class AcquisitionTaskSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._RTAcquisitionPatientPositionSequence: List[RTAcquisitionPatientPositionSequenceItem] = []
        self._AcquisitionTaskWorkitemCodeSequence: List[CodeSequenceItem] = []
        self._AcquisitionSubtaskSequence: List[AcquisitionSubtaskSequenceItem] = []
        self._AcquisitionTaskApplicabilitySequence: List[AcquisitionTaskApplicabilitySequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def RTAcquisitionPatientPositionSequence(self) -> Optional[List[RTAcquisitionPatientPositionSequenceItem]]:
        if "RTAcquisitionPatientPositionSequence" in self._dataset:
            if len(self._RTAcquisitionPatientPositionSequence) == len(self._dataset.RTAcquisitionPatientPositionSequence):
                return self._RTAcquisitionPatientPositionSequence
            else:
                return [
                    RTAcquisitionPatientPositionSequenceItem(x) for x in self._dataset.RTAcquisitionPatientPositionSequence
                ]
        return None

    @RTAcquisitionPatientPositionSequence.setter
    def RTAcquisitionPatientPositionSequence(self, value: Optional[List[RTAcquisitionPatientPositionSequenceItem]]):
        if value is None:
            self._RTAcquisitionPatientPositionSequence = []
            if "RTAcquisitionPatientPositionSequence" in self._dataset:
                del self._dataset.RTAcquisitionPatientPositionSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, RTAcquisitionPatientPositionSequenceItem) for item in value
        ):
            raise ValueError(
                "RTAcquisitionPatientPositionSequence must be a list of RTAcquisitionPatientPositionSequenceItem objects"
            )
        else:
            self._RTAcquisitionPatientPositionSequence = value
            if "RTAcquisitionPatientPositionSequence" not in self._dataset:
                self._dataset.RTAcquisitionPatientPositionSequence = pydicom.Sequence()
            self._dataset.RTAcquisitionPatientPositionSequence.clear()
            self._dataset.RTAcquisitionPatientPositionSequence.extend([item.to_dataset() for item in value])

    def add_RTAcquisitionPatientPosition(self, item: RTAcquisitionPatientPositionSequenceItem):
        if not isinstance(item, RTAcquisitionPatientPositionSequenceItem):
            raise ValueError("Item must be an instance of RTAcquisitionPatientPositionSequenceItem")
        self._RTAcquisitionPatientPositionSequence.append(item)
        if "RTAcquisitionPatientPositionSequence" not in self._dataset:
            self._dataset.RTAcquisitionPatientPositionSequence = pydicom.Sequence()
        self._dataset.RTAcquisitionPatientPositionSequence.append(item.to_dataset())

    @property
    def AcquisitionTaskWorkitemCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "AcquisitionTaskWorkitemCodeSequence" in self._dataset:
            if len(self._AcquisitionTaskWorkitemCodeSequence) == len(self._dataset.AcquisitionTaskWorkitemCodeSequence):
                return self._AcquisitionTaskWorkitemCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.AcquisitionTaskWorkitemCodeSequence]
        return None

    @AcquisitionTaskWorkitemCodeSequence.setter
    def AcquisitionTaskWorkitemCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._AcquisitionTaskWorkitemCodeSequence = []
            if "AcquisitionTaskWorkitemCodeSequence" in self._dataset:
                del self._dataset.AcquisitionTaskWorkitemCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("AcquisitionTaskWorkitemCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._AcquisitionTaskWorkitemCodeSequence = value
            if "AcquisitionTaskWorkitemCodeSequence" not in self._dataset:
                self._dataset.AcquisitionTaskWorkitemCodeSequence = pydicom.Sequence()
            self._dataset.AcquisitionTaskWorkitemCodeSequence.clear()
            self._dataset.AcquisitionTaskWorkitemCodeSequence.extend([item.to_dataset() for item in value])

    def add_AcquisitionTaskWorkitemCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._AcquisitionTaskWorkitemCodeSequence.append(item)
        if "AcquisitionTaskWorkitemCodeSequence" not in self._dataset:
            self._dataset.AcquisitionTaskWorkitemCodeSequence = pydicom.Sequence()
        self._dataset.AcquisitionTaskWorkitemCodeSequence.append(item.to_dataset())

    @property
    def AcquisitionSubtaskSequence(self) -> Optional[List[AcquisitionSubtaskSequenceItem]]:
        if "AcquisitionSubtaskSequence" in self._dataset:
            if len(self._AcquisitionSubtaskSequence) == len(self._dataset.AcquisitionSubtaskSequence):
                return self._AcquisitionSubtaskSequence
            else:
                return [AcquisitionSubtaskSequenceItem(x) for x in self._dataset.AcquisitionSubtaskSequence]
        return None

    @AcquisitionSubtaskSequence.setter
    def AcquisitionSubtaskSequence(self, value: Optional[List[AcquisitionSubtaskSequenceItem]]):
        if value is None:
            self._AcquisitionSubtaskSequence = []
            if "AcquisitionSubtaskSequence" in self._dataset:
                del self._dataset.AcquisitionSubtaskSequence
        elif not isinstance(value, list) or not all(isinstance(item, AcquisitionSubtaskSequenceItem) for item in value):
            raise ValueError("AcquisitionSubtaskSequence must be a list of AcquisitionSubtaskSequenceItem objects")
        else:
            self._AcquisitionSubtaskSequence = value
            if "AcquisitionSubtaskSequence" not in self._dataset:
                self._dataset.AcquisitionSubtaskSequence = pydicom.Sequence()
            self._dataset.AcquisitionSubtaskSequence.clear()
            self._dataset.AcquisitionSubtaskSequence.extend([item.to_dataset() for item in value])

    def add_AcquisitionSubtask(self, item: AcquisitionSubtaskSequenceItem):
        if not isinstance(item, AcquisitionSubtaskSequenceItem):
            raise ValueError("Item must be an instance of AcquisitionSubtaskSequenceItem")
        self._AcquisitionSubtaskSequence.append(item)
        if "AcquisitionSubtaskSequence" not in self._dataset:
            self._dataset.AcquisitionSubtaskSequence = pydicom.Sequence()
        self._dataset.AcquisitionSubtaskSequence.append(item.to_dataset())

    @property
    def AcquisitionTaskIndex(self) -> Optional[int]:
        if "AcquisitionTaskIndex" in self._dataset:
            return self._dataset.AcquisitionTaskIndex
        return None

    @AcquisitionTaskIndex.setter
    def AcquisitionTaskIndex(self, value: Optional[int]):
        if value is None:
            if "AcquisitionTaskIndex" in self._dataset:
                del self._dataset.AcquisitionTaskIndex
        else:
            self._dataset.AcquisitionTaskIndex = value

    @property
    def AcquisitionTaskApplicabilitySequence(self) -> Optional[List[AcquisitionTaskApplicabilitySequenceItem]]:
        if "AcquisitionTaskApplicabilitySequence" in self._dataset:
            if len(self._AcquisitionTaskApplicabilitySequence) == len(self._dataset.AcquisitionTaskApplicabilitySequence):
                return self._AcquisitionTaskApplicabilitySequence
            else:
                return [
                    AcquisitionTaskApplicabilitySequenceItem(x) for x in self._dataset.AcquisitionTaskApplicabilitySequence
                ]
        return None

    @AcquisitionTaskApplicabilitySequence.setter
    def AcquisitionTaskApplicabilitySequence(self, value: Optional[List[AcquisitionTaskApplicabilitySequenceItem]]):
        if value is None:
            self._AcquisitionTaskApplicabilitySequence = []
            if "AcquisitionTaskApplicabilitySequence" in self._dataset:
                del self._dataset.AcquisitionTaskApplicabilitySequence
        elif not isinstance(value, list) or not all(
            isinstance(item, AcquisitionTaskApplicabilitySequenceItem) for item in value
        ):
            raise ValueError(
                "AcquisitionTaskApplicabilitySequence must be a list of AcquisitionTaskApplicabilitySequenceItem objects"
            )
        else:
            self._AcquisitionTaskApplicabilitySequence = value
            if "AcquisitionTaskApplicabilitySequence" not in self._dataset:
                self._dataset.AcquisitionTaskApplicabilitySequence = pydicom.Sequence()
            self._dataset.AcquisitionTaskApplicabilitySequence.clear()
            self._dataset.AcquisitionTaskApplicabilitySequence.extend([item.to_dataset() for item in value])

    def add_AcquisitionTaskApplicability(self, item: AcquisitionTaskApplicabilitySequenceItem):
        if not isinstance(item, AcquisitionTaskApplicabilitySequenceItem):
            raise ValueError("Item must be an instance of AcquisitionTaskApplicabilitySequenceItem")
        self._AcquisitionTaskApplicabilitySequence.append(item)
        if "AcquisitionTaskApplicabilitySequence" not in self._dataset:
            self._dataset.AcquisitionTaskApplicabilitySequence = pydicom.Sequence()
        self._dataset.AcquisitionTaskApplicabilitySequence.append(item.to_dataset())
