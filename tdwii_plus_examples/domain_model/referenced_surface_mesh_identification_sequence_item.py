from typing import Any, List, Optional

import pydicom

from .code_sequence_item import CodeSequenceItem


class ReferencedSurfaceMeshIdentificationSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._SegmentedPropertyTypeCodeSequence: List[CodeSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ReferencedSOPInstanceUID(self) -> Optional[str]:
        if "ReferencedSOPInstanceUID" in self._dataset:
            return self._dataset.ReferencedSOPInstanceUID
        return None

    @ReferencedSOPInstanceUID.setter
    def ReferencedSOPInstanceUID(self, value: Optional[str]):
        if value is None:
            if "ReferencedSOPInstanceUID" in self._dataset:
                del self._dataset.ReferencedSOPInstanceUID
        else:
            self._dataset.ReferencedSOPInstanceUID = value

    @property
    def SurfaceMeshZPixelOffset(self) -> Optional[int]:
        if "SurfaceMeshZPixelOffset" in self._dataset:
            return self._dataset.SurfaceMeshZPixelOffset
        return None

    @SurfaceMeshZPixelOffset.setter
    def SurfaceMeshZPixelOffset(self, value: Optional[int]):
        if value is None:
            if "SurfaceMeshZPixelOffset" in self._dataset:
                del self._dataset.SurfaceMeshZPixelOffset
        else:
            self._dataset.SurfaceMeshZPixelOffset = value

    @property
    def SegmentedPropertyTypeCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "SegmentedPropertyTypeCodeSequence" in self._dataset:
            if len(self._SegmentedPropertyTypeCodeSequence) == len(self._dataset.SegmentedPropertyTypeCodeSequence):
                return self._SegmentedPropertyTypeCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.SegmentedPropertyTypeCodeSequence]
        return None

    @SegmentedPropertyTypeCodeSequence.setter
    def SegmentedPropertyTypeCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._SegmentedPropertyTypeCodeSequence = []
            if "SegmentedPropertyTypeCodeSequence" in self._dataset:
                del self._dataset.SegmentedPropertyTypeCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError(f"SegmentedPropertyTypeCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._SegmentedPropertyTypeCodeSequence = value
            if "SegmentedPropertyTypeCodeSequence" not in self._dataset:
                self._dataset.SegmentedPropertyTypeCodeSequence = pydicom.Sequence()
            self._dataset.SegmentedPropertyTypeCodeSequence.clear()
            self._dataset.SegmentedPropertyTypeCodeSequence.extend([item.to_dataset() for item in value])

    def add_SegmentedPropertyTypeCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError(f"Item must be an instance of CodeSequenceItem")
        self._SegmentedPropertyTypeCodeSequence.append(item)
        if "SegmentedPropertyTypeCodeSequence" not in self._dataset:
            self._dataset.SegmentedPropertyTypeCodeSequence = pydicom.Sequence()
        self._dataset.SegmentedPropertyTypeCodeSequence.append(item.to_dataset())

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
