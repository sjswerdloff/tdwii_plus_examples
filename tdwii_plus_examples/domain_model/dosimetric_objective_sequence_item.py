from typing import Any, List, Optional

import pydicom

from .code_sequence_item import CodeSequenceItem
from .dosimetric_objective_parameter_sequence_item import (
    DosimetricObjectiveParameterSequenceItem,
)
from .originating_sop_instance_reference_sequence_item import (
    OriginatingSOPInstanceReferenceSequenceItem,
)


class DosimetricObjectiveSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._OriginatingSOPInstanceReferenceSequence: List[OriginatingSOPInstanceReferenceSequenceItem] = []
        self._DosimetricObjectiveTypeCodeSequence: List[CodeSequenceItem] = []
        self._DosimetricObjectiveParameterSequence: List[DosimetricObjectiveParameterSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def OriginatingSOPInstanceReferenceSequence(self) -> Optional[List[OriginatingSOPInstanceReferenceSequenceItem]]:
        if "OriginatingSOPInstanceReferenceSequence" in self._dataset:
            if len(self._OriginatingSOPInstanceReferenceSequence) == len(
                self._dataset.OriginatingSOPInstanceReferenceSequence
            ):
                return self._OriginatingSOPInstanceReferenceSequence
            else:
                return [
                    OriginatingSOPInstanceReferenceSequenceItem(x)
                    for x in self._dataset.OriginatingSOPInstanceReferenceSequence
                ]
        return None

    @OriginatingSOPInstanceReferenceSequence.setter
    def OriginatingSOPInstanceReferenceSequence(self, value: Optional[List[OriginatingSOPInstanceReferenceSequenceItem]]):
        if value is None:
            self._OriginatingSOPInstanceReferenceSequence = []
            if "OriginatingSOPInstanceReferenceSequence" in self._dataset:
                del self._dataset.OriginatingSOPInstanceReferenceSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, OriginatingSOPInstanceReferenceSequenceItem) for item in value
        ):
            raise ValueError(
                f"OriginatingSOPInstanceReferenceSequence must be a list of OriginatingSOPInstanceReferenceSequenceItem objects"
            )
        else:
            self._OriginatingSOPInstanceReferenceSequence = value
            if "OriginatingSOPInstanceReferenceSequence" not in self._dataset:
                self._dataset.OriginatingSOPInstanceReferenceSequence = pydicom.Sequence()
            self._dataset.OriginatingSOPInstanceReferenceSequence.clear()
            self._dataset.OriginatingSOPInstanceReferenceSequence.extend([item.to_dataset() for item in value])

    def add_OriginatingSOPInstanceReference(self, item: OriginatingSOPInstanceReferenceSequenceItem):
        if not isinstance(item, OriginatingSOPInstanceReferenceSequenceItem):
            raise ValueError(f"Item must be an instance of OriginatingSOPInstanceReferenceSequenceItem")
        self._OriginatingSOPInstanceReferenceSequence.append(item)
        if "OriginatingSOPInstanceReferenceSequence" not in self._dataset:
            self._dataset.OriginatingSOPInstanceReferenceSequence = pydicom.Sequence()
        self._dataset.OriginatingSOPInstanceReferenceSequence.append(item.to_dataset())

    @property
    def ReferencedConceptualVolumeUID(self) -> Optional[str]:
        if "ReferencedConceptualVolumeUID" in self._dataset:
            return self._dataset.ReferencedConceptualVolumeUID
        return None

    @ReferencedConceptualVolumeUID.setter
    def ReferencedConceptualVolumeUID(self, value: Optional[str]):
        if value is None:
            if "ReferencedConceptualVolumeUID" in self._dataset:
                del self._dataset.ReferencedConceptualVolumeUID
        else:
            self._dataset.ReferencedConceptualVolumeUID = value

    @property
    def DosimetricObjectiveEvaluationScope(self) -> Optional[str]:
        if "DosimetricObjectiveEvaluationScope" in self._dataset:
            return self._dataset.DosimetricObjectiveEvaluationScope
        return None

    @DosimetricObjectiveEvaluationScope.setter
    def DosimetricObjectiveEvaluationScope(self, value: Optional[str]):
        if value is None:
            if "DosimetricObjectiveEvaluationScope" in self._dataset:
                del self._dataset.DosimetricObjectiveEvaluationScope
        else:
            self._dataset.DosimetricObjectiveEvaluationScope = value

    @property
    def DosimetricObjectiveTypeCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "DosimetricObjectiveTypeCodeSequence" in self._dataset:
            if len(self._DosimetricObjectiveTypeCodeSequence) == len(self._dataset.DosimetricObjectiveTypeCodeSequence):
                return self._DosimetricObjectiveTypeCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.DosimetricObjectiveTypeCodeSequence]
        return None

    @DosimetricObjectiveTypeCodeSequence.setter
    def DosimetricObjectiveTypeCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._DosimetricObjectiveTypeCodeSequence = []
            if "DosimetricObjectiveTypeCodeSequence" in self._dataset:
                del self._dataset.DosimetricObjectiveTypeCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError(f"DosimetricObjectiveTypeCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._DosimetricObjectiveTypeCodeSequence = value
            if "DosimetricObjectiveTypeCodeSequence" not in self._dataset:
                self._dataset.DosimetricObjectiveTypeCodeSequence = pydicom.Sequence()
            self._dataset.DosimetricObjectiveTypeCodeSequence.clear()
            self._dataset.DosimetricObjectiveTypeCodeSequence.extend([item.to_dataset() for item in value])

    def add_DosimetricObjectiveTypeCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError(f"Item must be an instance of CodeSequenceItem")
        self._DosimetricObjectiveTypeCodeSequence.append(item)
        if "DosimetricObjectiveTypeCodeSequence" not in self._dataset:
            self._dataset.DosimetricObjectiveTypeCodeSequence = pydicom.Sequence()
        self._dataset.DosimetricObjectiveTypeCodeSequence.append(item.to_dataset())

    @property
    def DosimetricObjectiveUID(self) -> Optional[str]:
        if "DosimetricObjectiveUID" in self._dataset:
            return self._dataset.DosimetricObjectiveUID
        return None

    @DosimetricObjectiveUID.setter
    def DosimetricObjectiveUID(self, value: Optional[str]):
        if value is None:
            if "DosimetricObjectiveUID" in self._dataset:
                del self._dataset.DosimetricObjectiveUID
        else:
            self._dataset.DosimetricObjectiveUID = value

    @property
    def DosimetricObjectiveParameterSequence(self) -> Optional[List[DosimetricObjectiveParameterSequenceItem]]:
        if "DosimetricObjectiveParameterSequence" in self._dataset:
            if len(self._DosimetricObjectiveParameterSequence) == len(self._dataset.DosimetricObjectiveParameterSequence):
                return self._DosimetricObjectiveParameterSequence
            else:
                return [
                    DosimetricObjectiveParameterSequenceItem(x) for x in self._dataset.DosimetricObjectiveParameterSequence
                ]
        return None

    @DosimetricObjectiveParameterSequence.setter
    def DosimetricObjectiveParameterSequence(self, value: Optional[List[DosimetricObjectiveParameterSequenceItem]]):
        if value is None:
            self._DosimetricObjectiveParameterSequence = []
            if "DosimetricObjectiveParameterSequence" in self._dataset:
                del self._dataset.DosimetricObjectiveParameterSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, DosimetricObjectiveParameterSequenceItem) for item in value
        ):
            raise ValueError(
                f"DosimetricObjectiveParameterSequence must be a list of DosimetricObjectiveParameterSequenceItem objects"
            )
        else:
            self._DosimetricObjectiveParameterSequence = value
            if "DosimetricObjectiveParameterSequence" not in self._dataset:
                self._dataset.DosimetricObjectiveParameterSequence = pydicom.Sequence()
            self._dataset.DosimetricObjectiveParameterSequence.clear()
            self._dataset.DosimetricObjectiveParameterSequence.extend([item.to_dataset() for item in value])

    def add_DosimetricObjectiveParameter(self, item: DosimetricObjectiveParameterSequenceItem):
        if not isinstance(item, DosimetricObjectiveParameterSequenceItem):
            raise ValueError(f"Item must be an instance of DosimetricObjectiveParameterSequenceItem")
        self._DosimetricObjectiveParameterSequence.append(item)
        if "DosimetricObjectiveParameterSequence" not in self._dataset:
            self._dataset.DosimetricObjectiveParameterSequence = pydicom.Sequence()
        self._dataset.DosimetricObjectiveParameterSequence.append(item.to_dataset())

    @property
    def AbsoluteDosimetricObjectiveFlag(self) -> Optional[str]:
        if "AbsoluteDosimetricObjectiveFlag" in self._dataset:
            return self._dataset.AbsoluteDosimetricObjectiveFlag
        return None

    @AbsoluteDosimetricObjectiveFlag.setter
    def AbsoluteDosimetricObjectiveFlag(self, value: Optional[str]):
        if value is None:
            if "AbsoluteDosimetricObjectiveFlag" in self._dataset:
                del self._dataset.AbsoluteDosimetricObjectiveFlag
        else:
            self._dataset.AbsoluteDosimetricObjectiveFlag = value

    @property
    def DosimetricObjectivePurpose(self) -> Optional[str]:
        if "DosimetricObjectivePurpose" in self._dataset:
            return self._dataset.DosimetricObjectivePurpose
        return None

    @DosimetricObjectivePurpose.setter
    def DosimetricObjectivePurpose(self, value: Optional[str]):
        if value is None:
            if "DosimetricObjectivePurpose" in self._dataset:
                del self._dataset.DosimetricObjectivePurpose
        else:
            self._dataset.DosimetricObjectivePurpose = value
