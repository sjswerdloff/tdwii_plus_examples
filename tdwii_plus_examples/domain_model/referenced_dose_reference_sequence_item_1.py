from typing import Any, List, Optional  # noqa

import pydicom

from .beam_dose_verification_control_point_sequence_item import (
    BeamDoseVerificationControlPointSequenceItem,
)


class ReferencedDoseReferenceSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._BeamDoseVerificationControlPointSequence: List[BeamDoseVerificationControlPointSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def BeamDoseVerificationControlPointSequence(self) -> Optional[List[BeamDoseVerificationControlPointSequenceItem]]:
        if "BeamDoseVerificationControlPointSequence" in self._dataset:
            if len(self._BeamDoseVerificationControlPointSequence) == len(
                self._dataset.BeamDoseVerificationControlPointSequence
            ):
                return self._BeamDoseVerificationControlPointSequence
            else:
                return [
                    BeamDoseVerificationControlPointSequenceItem(x)
                    for x in self._dataset.BeamDoseVerificationControlPointSequence
                ]
        return None

    @BeamDoseVerificationControlPointSequence.setter
    def BeamDoseVerificationControlPointSequence(self, value: Optional[List[BeamDoseVerificationControlPointSequenceItem]]):
        if value is None:
            self._BeamDoseVerificationControlPointSequence = []
            if "BeamDoseVerificationControlPointSequence" in self._dataset:
                del self._dataset.BeamDoseVerificationControlPointSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, BeamDoseVerificationControlPointSequenceItem) for item in value
        ):
            raise ValueError(
                "BeamDoseVerificationControlPointSequence must be a list of BeamDoseVerificationControlPointSequenceItem"
                " objects"
            )
        else:
            self._BeamDoseVerificationControlPointSequence = value
            if "BeamDoseVerificationControlPointSequence" not in self._dataset:
                self._dataset.BeamDoseVerificationControlPointSequence = pydicom.Sequence()
            self._dataset.BeamDoseVerificationControlPointSequence.clear()
            self._dataset.BeamDoseVerificationControlPointSequence.extend([item.to_dataset() for item in value])

    def add_BeamDoseVerificationControlPoint(self, item: BeamDoseVerificationControlPointSequenceItem):
        if not isinstance(item, BeamDoseVerificationControlPointSequenceItem):
            raise ValueError("Item must be an instance of BeamDoseVerificationControlPointSequenceItem")
        self._BeamDoseVerificationControlPointSequence.append(item)
        if "BeamDoseVerificationControlPointSequence" not in self._dataset:
            self._dataset.BeamDoseVerificationControlPointSequence = pydicom.Sequence()
        self._dataset.BeamDoseVerificationControlPointSequence.append(item.to_dataset())

    @property
    def DepthValueAveragingFlag(self) -> Optional[str]:
        if "DepthValueAveragingFlag" in self._dataset:
            return self._dataset.DepthValueAveragingFlag
        return None

    @DepthValueAveragingFlag.setter
    def DepthValueAveragingFlag(self, value: Optional[str]):
        if value is None:
            if "DepthValueAveragingFlag" in self._dataset:
                del self._dataset.DepthValueAveragingFlag
        else:
            self._dataset.DepthValueAveragingFlag = value

    @property
    def ReferencedDoseReferenceNumber(self) -> Optional[int]:
        if "ReferencedDoseReferenceNumber" in self._dataset:
            return self._dataset.ReferencedDoseReferenceNumber
        return None

    @ReferencedDoseReferenceNumber.setter
    def ReferencedDoseReferenceNumber(self, value: Optional[int]):
        if value is None:
            if "ReferencedDoseReferenceNumber" in self._dataset:
                del self._dataset.ReferencedDoseReferenceNumber
        else:
            self._dataset.ReferencedDoseReferenceNumber = value
