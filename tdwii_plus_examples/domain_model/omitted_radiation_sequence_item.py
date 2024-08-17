from typing import Any, List, Optional  # noqa

import pydicom

from .asserter_identification_sequence_item import AsserterIdentificationSequenceItem
from .code_sequence_item import CodeSequenceItem
from .referenced_rt_radiation_sequence_item import ReferencedRTRadiationSequenceItem


class OmittedRadiationSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._AsserterIdentificationSequence: List[AsserterIdentificationSequenceItem] = []
        self._ReferencedRTRadiationSequence: List[ReferencedRTRadiationSequenceItem] = []
        self._ReasonForOmissionCodeSequence: List[CodeSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def AsserterIdentificationSequence(self) -> Optional[List[AsserterIdentificationSequenceItem]]:
        if "AsserterIdentificationSequence" in self._dataset:
            if len(self._AsserterIdentificationSequence) == len(self._dataset.AsserterIdentificationSequence):
                return self._AsserterIdentificationSequence
            else:
                return [AsserterIdentificationSequenceItem(x) for x in self._dataset.AsserterIdentificationSequence]
        return None

    @AsserterIdentificationSequence.setter
    def AsserterIdentificationSequence(self, value: Optional[List[AsserterIdentificationSequenceItem]]):
        if value is None:
            self._AsserterIdentificationSequence = []
            if "AsserterIdentificationSequence" in self._dataset:
                del self._dataset.AsserterIdentificationSequence
        elif not isinstance(value, list) or not all(isinstance(item, AsserterIdentificationSequenceItem) for item in value):
            raise ValueError("AsserterIdentificationSequence must be a list of AsserterIdentificationSequenceItem objects")
        else:
            self._AsserterIdentificationSequence = value
            if "AsserterIdentificationSequence" not in self._dataset:
                self._dataset.AsserterIdentificationSequence = pydicom.Sequence()
            self._dataset.AsserterIdentificationSequence.clear()
            self._dataset.AsserterIdentificationSequence.extend([item.to_dataset() for item in value])

    def add_AsserterIdentification(self, item: AsserterIdentificationSequenceItem):
        if not isinstance(item, AsserterIdentificationSequenceItem):
            raise ValueError("Item must be an instance of AsserterIdentificationSequenceItem")
        self._AsserterIdentificationSequence.append(item)
        if "AsserterIdentificationSequence" not in self._dataset:
            self._dataset.AsserterIdentificationSequence = pydicom.Sequence()
        self._dataset.AsserterIdentificationSequence.append(item.to_dataset())

    @property
    def ReferencedRTRadiationSequence(self) -> Optional[List[ReferencedRTRadiationSequenceItem]]:
        if "ReferencedRTRadiationSequence" in self._dataset:
            if len(self._ReferencedRTRadiationSequence) == len(self._dataset.ReferencedRTRadiationSequence):
                return self._ReferencedRTRadiationSequence
            else:
                return [ReferencedRTRadiationSequenceItem(x) for x in self._dataset.ReferencedRTRadiationSequence]
        return None

    @ReferencedRTRadiationSequence.setter
    def ReferencedRTRadiationSequence(self, value: Optional[List[ReferencedRTRadiationSequenceItem]]):
        if value is None:
            self._ReferencedRTRadiationSequence = []
            if "ReferencedRTRadiationSequence" in self._dataset:
                del self._dataset.ReferencedRTRadiationSequence
        elif not isinstance(value, list) or not all(isinstance(item, ReferencedRTRadiationSequenceItem) for item in value):
            raise ValueError("ReferencedRTRadiationSequence must be a list of ReferencedRTRadiationSequenceItem objects")
        else:
            self._ReferencedRTRadiationSequence = value
            if "ReferencedRTRadiationSequence" not in self._dataset:
                self._dataset.ReferencedRTRadiationSequence = pydicom.Sequence()
            self._dataset.ReferencedRTRadiationSequence.clear()
            self._dataset.ReferencedRTRadiationSequence.extend([item.to_dataset() for item in value])

    def add_ReferencedRTRadiation(self, item: ReferencedRTRadiationSequenceItem):
        if not isinstance(item, ReferencedRTRadiationSequenceItem):
            raise ValueError("Item must be an instance of ReferencedRTRadiationSequenceItem")
        self._ReferencedRTRadiationSequence.append(item)
        if "ReferencedRTRadiationSequence" not in self._dataset:
            self._dataset.ReferencedRTRadiationSequence = pydicom.Sequence()
        self._dataset.ReferencedRTRadiationSequence.append(item.to_dataset())

    @property
    def ReasonForOmissionCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "ReasonForOmissionCodeSequence" in self._dataset:
            if len(self._ReasonForOmissionCodeSequence) == len(self._dataset.ReasonForOmissionCodeSequence):
                return self._ReasonForOmissionCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.ReasonForOmissionCodeSequence]
        return None

    @ReasonForOmissionCodeSequence.setter
    def ReasonForOmissionCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._ReasonForOmissionCodeSequence = []
            if "ReasonForOmissionCodeSequence" in self._dataset:
                del self._dataset.ReasonForOmissionCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("ReasonForOmissionCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._ReasonForOmissionCodeSequence = value
            if "ReasonForOmissionCodeSequence" not in self._dataset:
                self._dataset.ReasonForOmissionCodeSequence = pydicom.Sequence()
            self._dataset.ReasonForOmissionCodeSequence.clear()
            self._dataset.ReasonForOmissionCodeSequence.extend([item.to_dataset() for item in value])

    def add_ReasonForOmissionCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._ReasonForOmissionCodeSequence.append(item)
        if "ReasonForOmissionCodeSequence" not in self._dataset:
            self._dataset.ReasonForOmissionCodeSequence = pydicom.Sequence()
        self._dataset.ReasonForOmissionCodeSequence.append(item.to_dataset())

    @property
    def ReasonForOmissionDescription(self) -> Optional[str]:
        if "ReasonForOmissionDescription" in self._dataset:
            return self._dataset.ReasonForOmissionDescription
        return None

    @ReasonForOmissionDescription.setter
    def ReasonForOmissionDescription(self, value: Optional[str]):
        if value is None:
            if "ReasonForOmissionDescription" in self._dataset:
                del self._dataset.ReasonForOmissionDescription
        else:
            self._dataset.ReasonForOmissionDescription = value
