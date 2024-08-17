from typing import Any, List, Optional  # noqa

import pydicom

from .segment_surface_generation_algorithm_identification_sequence_item import (
    SegmentSurfaceGenerationAlgorithmIdentificationSequenceItem,
)
from .segment_surface_source_instance_sequence_item import (
    SegmentSurfaceSourceInstanceSequenceItem,
)


class ReferencedSurfaceSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._SegmentSurfaceGenerationAlgorithmIdentificationSequence: List[
            SegmentSurfaceGenerationAlgorithmIdentificationSequenceItem
        ] = []
        self._SegmentSurfaceSourceInstanceSequence: List[SegmentSurfaceSourceInstanceSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ReferencedSurfaceNumber(self) -> Optional[int]:
        if "ReferencedSurfaceNumber" in self._dataset:
            return self._dataset.ReferencedSurfaceNumber
        return None

    @ReferencedSurfaceNumber.setter
    def ReferencedSurfaceNumber(self, value: Optional[int]):
        if value is None:
            if "ReferencedSurfaceNumber" in self._dataset:
                del self._dataset.ReferencedSurfaceNumber
        else:
            self._dataset.ReferencedSurfaceNumber = value

    @property
    def SegmentSurfaceGenerationAlgorithmIdentificationSequence(
        self,
    ) -> Optional[List[SegmentSurfaceGenerationAlgorithmIdentificationSequenceItem]]:
        if "SegmentSurfaceGenerationAlgorithmIdentificationSequence" in self._dataset:
            if len(self._SegmentSurfaceGenerationAlgorithmIdentificationSequence) == len(
                self._dataset.SegmentSurfaceGenerationAlgorithmIdentificationSequence
            ):
                return self._SegmentSurfaceGenerationAlgorithmIdentificationSequence
            else:
                return [
                    SegmentSurfaceGenerationAlgorithmIdentificationSequenceItem(x)
                    for x in self._dataset.SegmentSurfaceGenerationAlgorithmIdentificationSequence
                ]
        return None

    @SegmentSurfaceGenerationAlgorithmIdentificationSequence.setter
    def SegmentSurfaceGenerationAlgorithmIdentificationSequence(
        self, value: Optional[List[SegmentSurfaceGenerationAlgorithmIdentificationSequenceItem]]
    ):
        if value is None:
            self._SegmentSurfaceGenerationAlgorithmIdentificationSequence = []
            if "SegmentSurfaceGenerationAlgorithmIdentificationSequence" in self._dataset:
                del self._dataset.SegmentSurfaceGenerationAlgorithmIdentificationSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, SegmentSurfaceGenerationAlgorithmIdentificationSequenceItem) for item in value
        ):
            raise ValueError(
                "SegmentSurfaceGenerationAlgorithmIdentificationSequence must be a list of"
                " SegmentSurfaceGenerationAlgorithmIdentificationSequenceItem objects"
            )
        else:
            self._SegmentSurfaceGenerationAlgorithmIdentificationSequence = value
            if "SegmentSurfaceGenerationAlgorithmIdentificationSequence" not in self._dataset:
                self._dataset.SegmentSurfaceGenerationAlgorithmIdentificationSequence = pydicom.Sequence()
            self._dataset.SegmentSurfaceGenerationAlgorithmIdentificationSequence.clear()
            self._dataset.SegmentSurfaceGenerationAlgorithmIdentificationSequence.extend([item.to_dataset() for item in value])

    def add_SegmentSurfaceGenerationAlgorithmIdentification(
        self, item: SegmentSurfaceGenerationAlgorithmIdentificationSequenceItem
    ):
        if not isinstance(item, SegmentSurfaceGenerationAlgorithmIdentificationSequenceItem):
            raise ValueError("Item must be an instance of SegmentSurfaceGenerationAlgorithmIdentificationSequenceItem")
        self._SegmentSurfaceGenerationAlgorithmIdentificationSequence.append(item)
        if "SegmentSurfaceGenerationAlgorithmIdentificationSequence" not in self._dataset:
            self._dataset.SegmentSurfaceGenerationAlgorithmIdentificationSequence = pydicom.Sequence()
        self._dataset.SegmentSurfaceGenerationAlgorithmIdentificationSequence.append(item.to_dataset())

    @property
    def SegmentSurfaceSourceInstanceSequence(self) -> Optional[List[SegmentSurfaceSourceInstanceSequenceItem]]:
        if "SegmentSurfaceSourceInstanceSequence" in self._dataset:
            if len(self._SegmentSurfaceSourceInstanceSequence) == len(self._dataset.SegmentSurfaceSourceInstanceSequence):
                return self._SegmentSurfaceSourceInstanceSequence
            else:
                return [
                    SegmentSurfaceSourceInstanceSequenceItem(x) for x in self._dataset.SegmentSurfaceSourceInstanceSequence
                ]
        return None

    @SegmentSurfaceSourceInstanceSequence.setter
    def SegmentSurfaceSourceInstanceSequence(self, value: Optional[List[SegmentSurfaceSourceInstanceSequenceItem]]):
        if value is None:
            self._SegmentSurfaceSourceInstanceSequence = []
            if "SegmentSurfaceSourceInstanceSequence" in self._dataset:
                del self._dataset.SegmentSurfaceSourceInstanceSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, SegmentSurfaceSourceInstanceSequenceItem) for item in value
        ):
            raise ValueError(
                "SegmentSurfaceSourceInstanceSequence must be a list of SegmentSurfaceSourceInstanceSequenceItem objects"
            )
        else:
            self._SegmentSurfaceSourceInstanceSequence = value
            if "SegmentSurfaceSourceInstanceSequence" not in self._dataset:
                self._dataset.SegmentSurfaceSourceInstanceSequence = pydicom.Sequence()
            self._dataset.SegmentSurfaceSourceInstanceSequence.clear()
            self._dataset.SegmentSurfaceSourceInstanceSequence.extend([item.to_dataset() for item in value])

    def add_SegmentSurfaceSourceInstance(self, item: SegmentSurfaceSourceInstanceSequenceItem):
        if not isinstance(item, SegmentSurfaceSourceInstanceSequenceItem):
            raise ValueError("Item must be an instance of SegmentSurfaceSourceInstanceSequenceItem")
        self._SegmentSurfaceSourceInstanceSequence.append(item)
        if "SegmentSurfaceSourceInstanceSequence" not in self._dataset:
            self._dataset.SegmentSurfaceSourceInstanceSequence = pydicom.Sequence()
        self._dataset.SegmentSurfaceSourceInstanceSequence.append(item.to_dataset())
