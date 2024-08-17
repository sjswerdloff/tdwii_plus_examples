from typing import Any, List, Optional  # noqa

import pydicom

from .code_sequence_item import CodeSequenceItem
from .structured_constraint_observation_sequence_item import (
    StructuredConstraintObservationSequenceItem,
)


class AssessmentObservationsSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._StructuredConstraintObservationSequence: List[StructuredConstraintObservationSequenceItem] = []
        self._ObservationBasisCodeSequence: List[CodeSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ObservationSignificance(self) -> Optional[str]:
        if "ObservationSignificance" in self._dataset:
            return self._dataset.ObservationSignificance
        return None

    @ObservationSignificance.setter
    def ObservationSignificance(self, value: Optional[str]):
        if value is None:
            if "ObservationSignificance" in self._dataset:
                del self._dataset.ObservationSignificance
        else:
            self._dataset.ObservationSignificance = value

    @property
    def ObservationDescription(self) -> Optional[str]:
        if "ObservationDescription" in self._dataset:
            return self._dataset.ObservationDescription
        return None

    @ObservationDescription.setter
    def ObservationDescription(self, value: Optional[str]):
        if value is None:
            if "ObservationDescription" in self._dataset:
                del self._dataset.ObservationDescription
        else:
            self._dataset.ObservationDescription = value

    @property
    def StructuredConstraintObservationSequence(self) -> Optional[List[StructuredConstraintObservationSequenceItem]]:
        if "StructuredConstraintObservationSequence" in self._dataset:
            if len(self._StructuredConstraintObservationSequence) == len(
                self._dataset.StructuredConstraintObservationSequence
            ):
                return self._StructuredConstraintObservationSequence
            else:
                return [
                    StructuredConstraintObservationSequenceItem(x)
                    for x in self._dataset.StructuredConstraintObservationSequence
                ]
        return None

    @StructuredConstraintObservationSequence.setter
    def StructuredConstraintObservationSequence(self, value: Optional[List[StructuredConstraintObservationSequenceItem]]):
        if value is None:
            self._StructuredConstraintObservationSequence = []
            if "StructuredConstraintObservationSequence" in self._dataset:
                del self._dataset.StructuredConstraintObservationSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, StructuredConstraintObservationSequenceItem) for item in value
        ):
            raise ValueError(
                "StructuredConstraintObservationSequence must be a list of StructuredConstraintObservationSequenceItem objects"
            )
        else:
            self._StructuredConstraintObservationSequence = value
            if "StructuredConstraintObservationSequence" not in self._dataset:
                self._dataset.StructuredConstraintObservationSequence = pydicom.Sequence()
            self._dataset.StructuredConstraintObservationSequence.clear()
            self._dataset.StructuredConstraintObservationSequence.extend([item.to_dataset() for item in value])

    def add_StructuredConstraintObservation(self, item: StructuredConstraintObservationSequenceItem):
        if not isinstance(item, StructuredConstraintObservationSequenceItem):
            raise ValueError("Item must be an instance of StructuredConstraintObservationSequenceItem")
        self._StructuredConstraintObservationSequence.append(item)
        if "StructuredConstraintObservationSequence" not in self._dataset:
            self._dataset.StructuredConstraintObservationSequence = pydicom.Sequence()
        self._dataset.StructuredConstraintObservationSequence.append(item.to_dataset())

    @property
    def ObservationBasisCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "ObservationBasisCodeSequence" in self._dataset:
            if len(self._ObservationBasisCodeSequence) == len(self._dataset.ObservationBasisCodeSequence):
                return self._ObservationBasisCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.ObservationBasisCodeSequence]
        return None

    @ObservationBasisCodeSequence.setter
    def ObservationBasisCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._ObservationBasisCodeSequence = []
            if "ObservationBasisCodeSequence" in self._dataset:
                del self._dataset.ObservationBasisCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("ObservationBasisCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._ObservationBasisCodeSequence = value
            if "ObservationBasisCodeSequence" not in self._dataset:
                self._dataset.ObservationBasisCodeSequence = pydicom.Sequence()
            self._dataset.ObservationBasisCodeSequence.clear()
            self._dataset.ObservationBasisCodeSequence.extend([item.to_dataset() for item in value])

    def add_ObservationBasisCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._ObservationBasisCodeSequence.append(item)
        if "ObservationBasisCodeSequence" not in self._dataset:
            self._dataset.ObservationBasisCodeSequence = pydicom.Sequence()
        self._dataset.ObservationBasisCodeSequence.append(item.to_dataset())
