from typing import Any, List, Optional  # noqa

import pydicom

from .code_sequence_item import CodeSequenceItem
from .rt_physician_intent_input_instance_sequence_item import (
    RTPhysicianIntentInputInstanceSequenceItem,
)
from .rt_physician_intent_predecessor_sequence_item import (
    RTPhysicianIntentPredecessorSequenceItem,
)


class RTPhysicianIntentSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._RTPhysicianIntentPredecessorSequence: List[RTPhysicianIntentPredecessorSequenceItem] = []
        self._RTProtocolCodeSequence: List[CodeSequenceItem] = []
        self._RTDiagnosisCodeSequence: List[CodeSequenceItem] = []
        self._RTPhysicianIntentInputInstanceSequence: List[RTPhysicianIntentInputInstanceSequenceItem] = []
        self._TreatmentSiteCodeSequence: List[CodeSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def RTPhysicianIntentPredecessorSequence(self) -> Optional[List[RTPhysicianIntentPredecessorSequenceItem]]:
        if "RTPhysicianIntentPredecessorSequence" in self._dataset:
            if len(self._RTPhysicianIntentPredecessorSequence) == len(self._dataset.RTPhysicianIntentPredecessorSequence):
                return self._RTPhysicianIntentPredecessorSequence
            else:
                return [
                    RTPhysicianIntentPredecessorSequenceItem(x) for x in self._dataset.RTPhysicianIntentPredecessorSequence
                ]
        return None

    @RTPhysicianIntentPredecessorSequence.setter
    def RTPhysicianIntentPredecessorSequence(self, value: Optional[List[RTPhysicianIntentPredecessorSequenceItem]]):
        if value is None:
            self._RTPhysicianIntentPredecessorSequence = []
            if "RTPhysicianIntentPredecessorSequence" in self._dataset:
                del self._dataset.RTPhysicianIntentPredecessorSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, RTPhysicianIntentPredecessorSequenceItem) for item in value
        ):
            raise ValueError(
                "RTPhysicianIntentPredecessorSequence must be a list of RTPhysicianIntentPredecessorSequenceItem objects"
            )
        else:
            self._RTPhysicianIntentPredecessorSequence = value
            if "RTPhysicianIntentPredecessorSequence" not in self._dataset:
                self._dataset.RTPhysicianIntentPredecessorSequence = pydicom.Sequence()
            self._dataset.RTPhysicianIntentPredecessorSequence.clear()
            self._dataset.RTPhysicianIntentPredecessorSequence.extend([item.to_dataset() for item in value])

    def add_RTPhysicianIntentPredecessor(self, item: RTPhysicianIntentPredecessorSequenceItem):
        if not isinstance(item, RTPhysicianIntentPredecessorSequenceItem):
            raise ValueError("Item must be an instance of RTPhysicianIntentPredecessorSequenceItem")
        self._RTPhysicianIntentPredecessorSequence.append(item)
        if "RTPhysicianIntentPredecessorSequence" not in self._dataset:
            self._dataset.RTPhysicianIntentPredecessorSequence = pydicom.Sequence()
        self._dataset.RTPhysicianIntentPredecessorSequence.append(item.to_dataset())

    @property
    def RTTreatmentApproachLabel(self) -> Optional[str]:
        if "RTTreatmentApproachLabel" in self._dataset:
            return self._dataset.RTTreatmentApproachLabel
        return None

    @RTTreatmentApproachLabel.setter
    def RTTreatmentApproachLabel(self, value: Optional[str]):
        if value is None:
            if "RTTreatmentApproachLabel" in self._dataset:
                del self._dataset.RTTreatmentApproachLabel
        else:
            self._dataset.RTTreatmentApproachLabel = value

    @property
    def RTPhysicianIntentIndex(self) -> Optional[int]:
        if "RTPhysicianIntentIndex" in self._dataset:
            return self._dataset.RTPhysicianIntentIndex
        return None

    @RTPhysicianIntentIndex.setter
    def RTPhysicianIntentIndex(self, value: Optional[int]):
        if value is None:
            if "RTPhysicianIntentIndex" in self._dataset:
                del self._dataset.RTPhysicianIntentIndex
        else:
            self._dataset.RTPhysicianIntentIndex = value

    @property
    def RTTreatmentIntentType(self) -> Optional[str]:
        if "RTTreatmentIntentType" in self._dataset:
            return self._dataset.RTTreatmentIntentType
        return None

    @RTTreatmentIntentType.setter
    def RTTreatmentIntentType(self, value: Optional[str]):
        if value is None:
            if "RTTreatmentIntentType" in self._dataset:
                del self._dataset.RTTreatmentIntentType
        else:
            self._dataset.RTTreatmentIntentType = value

    @property
    def RTPhysicianIntentNarrative(self) -> Optional[str]:
        if "RTPhysicianIntentNarrative" in self._dataset:
            return self._dataset.RTPhysicianIntentNarrative
        return None

    @RTPhysicianIntentNarrative.setter
    def RTPhysicianIntentNarrative(self, value: Optional[str]):
        if value is None:
            if "RTPhysicianIntentNarrative" in self._dataset:
                del self._dataset.RTPhysicianIntentNarrative
        else:
            self._dataset.RTPhysicianIntentNarrative = value

    @property
    def RTProtocolCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "RTProtocolCodeSequence" in self._dataset:
            if len(self._RTProtocolCodeSequence) == len(self._dataset.RTProtocolCodeSequence):
                return self._RTProtocolCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.RTProtocolCodeSequence]
        return None

    @RTProtocolCodeSequence.setter
    def RTProtocolCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._RTProtocolCodeSequence = []
            if "RTProtocolCodeSequence" in self._dataset:
                del self._dataset.RTProtocolCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("RTProtocolCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._RTProtocolCodeSequence = value
            if "RTProtocolCodeSequence" not in self._dataset:
                self._dataset.RTProtocolCodeSequence = pydicom.Sequence()
            self._dataset.RTProtocolCodeSequence.clear()
            self._dataset.RTProtocolCodeSequence.extend([item.to_dataset() for item in value])

    def add_RTProtocolCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._RTProtocolCodeSequence.append(item)
        if "RTProtocolCodeSequence" not in self._dataset:
            self._dataset.RTProtocolCodeSequence = pydicom.Sequence()
        self._dataset.RTProtocolCodeSequence.append(item.to_dataset())

    @property
    def RTDiagnosisCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "RTDiagnosisCodeSequence" in self._dataset:
            if len(self._RTDiagnosisCodeSequence) == len(self._dataset.RTDiagnosisCodeSequence):
                return self._RTDiagnosisCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.RTDiagnosisCodeSequence]
        return None

    @RTDiagnosisCodeSequence.setter
    def RTDiagnosisCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._RTDiagnosisCodeSequence = []
            if "RTDiagnosisCodeSequence" in self._dataset:
                del self._dataset.RTDiagnosisCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("RTDiagnosisCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._RTDiagnosisCodeSequence = value
            if "RTDiagnosisCodeSequence" not in self._dataset:
                self._dataset.RTDiagnosisCodeSequence = pydicom.Sequence()
            self._dataset.RTDiagnosisCodeSequence.clear()
            self._dataset.RTDiagnosisCodeSequence.extend([item.to_dataset() for item in value])

    def add_RTDiagnosisCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._RTDiagnosisCodeSequence.append(item)
        if "RTDiagnosisCodeSequence" not in self._dataset:
            self._dataset.RTDiagnosisCodeSequence = pydicom.Sequence()
        self._dataset.RTDiagnosisCodeSequence.append(item.to_dataset())

    @property
    def RTPhysicianIntentInputInstanceSequence(self) -> Optional[List[RTPhysicianIntentInputInstanceSequenceItem]]:
        if "RTPhysicianIntentInputInstanceSequence" in self._dataset:
            if len(self._RTPhysicianIntentInputInstanceSequence) == len(self._dataset.RTPhysicianIntentInputInstanceSequence):
                return self._RTPhysicianIntentInputInstanceSequence
            else:
                return [
                    RTPhysicianIntentInputInstanceSequenceItem(x) for x in self._dataset.RTPhysicianIntentInputInstanceSequence
                ]
        return None

    @RTPhysicianIntentInputInstanceSequence.setter
    def RTPhysicianIntentInputInstanceSequence(self, value: Optional[List[RTPhysicianIntentInputInstanceSequenceItem]]):
        if value is None:
            self._RTPhysicianIntentInputInstanceSequence = []
            if "RTPhysicianIntentInputInstanceSequence" in self._dataset:
                del self._dataset.RTPhysicianIntentInputInstanceSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, RTPhysicianIntentInputInstanceSequenceItem) for item in value
        ):
            raise ValueError(
                "RTPhysicianIntentInputInstanceSequence must be a list of RTPhysicianIntentInputInstanceSequenceItem objects"
            )
        else:
            self._RTPhysicianIntentInputInstanceSequence = value
            if "RTPhysicianIntentInputInstanceSequence" not in self._dataset:
                self._dataset.RTPhysicianIntentInputInstanceSequence = pydicom.Sequence()
            self._dataset.RTPhysicianIntentInputInstanceSequence.clear()
            self._dataset.RTPhysicianIntentInputInstanceSequence.extend([item.to_dataset() for item in value])

    def add_RTPhysicianIntentInputInstance(self, item: RTPhysicianIntentInputInstanceSequenceItem):
        if not isinstance(item, RTPhysicianIntentInputInstanceSequenceItem):
            raise ValueError("Item must be an instance of RTPhysicianIntentInputInstanceSequenceItem")
        self._RTPhysicianIntentInputInstanceSequence.append(item)
        if "RTPhysicianIntentInputInstanceSequence" not in self._dataset:
            self._dataset.RTPhysicianIntentInputInstanceSequence = pydicom.Sequence()
        self._dataset.RTPhysicianIntentInputInstanceSequence.append(item.to_dataset())

    @property
    def TreatmentSite(self) -> Optional[str]:
        if "TreatmentSite" in self._dataset:
            return self._dataset.TreatmentSite
        return None

    @TreatmentSite.setter
    def TreatmentSite(self, value: Optional[str]):
        if value is None:
            if "TreatmentSite" in self._dataset:
                del self._dataset.TreatmentSite
        else:
            self._dataset.TreatmentSite = value

    @property
    def TreatmentSiteCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "TreatmentSiteCodeSequence" in self._dataset:
            if len(self._TreatmentSiteCodeSequence) == len(self._dataset.TreatmentSiteCodeSequence):
                return self._TreatmentSiteCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.TreatmentSiteCodeSequence]
        return None

    @TreatmentSiteCodeSequence.setter
    def TreatmentSiteCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._TreatmentSiteCodeSequence = []
            if "TreatmentSiteCodeSequence" in self._dataset:
                del self._dataset.TreatmentSiteCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("TreatmentSiteCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._TreatmentSiteCodeSequence = value
            if "TreatmentSiteCodeSequence" not in self._dataset:
                self._dataset.TreatmentSiteCodeSequence = pydicom.Sequence()
            self._dataset.TreatmentSiteCodeSequence.clear()
            self._dataset.TreatmentSiteCodeSequence.extend([item.to_dataset() for item in value])

    def add_TreatmentSiteCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._TreatmentSiteCodeSequence.append(item)
        if "TreatmentSiteCodeSequence" not in self._dataset:
            self._dataset.TreatmentSiteCodeSequence = pydicom.Sequence()
        self._dataset.TreatmentSiteCodeSequence.append(item.to_dataset())
