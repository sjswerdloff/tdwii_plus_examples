from typing import Any, List, Optional  # noqa

import pydicom

from .code_sequence_item import CodeSequenceItem


class SourceImageSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._PurposeOfReferenceCodeSequence: List[CodeSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ReferencedSOPClassUID(self) -> Optional[str]:
        if "ReferencedSOPClassUID" in self._dataset:
            return self._dataset.ReferencedSOPClassUID
        return None

    @ReferencedSOPClassUID.setter
    def ReferencedSOPClassUID(self, value: Optional[str]):
        if value is None:
            if "ReferencedSOPClassUID" in self._dataset:
                del self._dataset.ReferencedSOPClassUID
        else:
            self._dataset.ReferencedSOPClassUID = value

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
    def ReferencedFrameNumber(self) -> Optional[List[int]]:
        if "ReferencedFrameNumber" in self._dataset:
            return self._dataset.ReferencedFrameNumber
        return None

    @ReferencedFrameNumber.setter
    def ReferencedFrameNumber(self, value: Optional[List[int]]):
        if value is None:
            if "ReferencedFrameNumber" in self._dataset:
                del self._dataset.ReferencedFrameNumber
        else:
            self._dataset.ReferencedFrameNumber = value

    @property
    def PatientOrientation(self) -> Optional[List[str]]:
        if "PatientOrientation" in self._dataset:
            return self._dataset.PatientOrientation
        return None

    @PatientOrientation.setter
    def PatientOrientation(self, value: Optional[List[str]]):
        if value is None:
            if "PatientOrientation" in self._dataset:
                del self._dataset.PatientOrientation
        else:
            self._dataset.PatientOrientation = value

    @property
    def SpatialLocationsPreserved(self) -> Optional[str]:
        if "SpatialLocationsPreserved" in self._dataset:
            return self._dataset.SpatialLocationsPreserved
        return None

    @SpatialLocationsPreserved.setter
    def SpatialLocationsPreserved(self, value: Optional[str]):
        if value is None:
            if "SpatialLocationsPreserved" in self._dataset:
                del self._dataset.SpatialLocationsPreserved
        else:
            self._dataset.SpatialLocationsPreserved = value

    @property
    def PurposeOfReferenceCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "PurposeOfReferenceCodeSequence" in self._dataset:
            if len(self._PurposeOfReferenceCodeSequence) == len(self._dataset.PurposeOfReferenceCodeSequence):
                return self._PurposeOfReferenceCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.PurposeOfReferenceCodeSequence]
        return None

    @PurposeOfReferenceCodeSequence.setter
    def PurposeOfReferenceCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._PurposeOfReferenceCodeSequence = []
            if "PurposeOfReferenceCodeSequence" in self._dataset:
                del self._dataset.PurposeOfReferenceCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("PurposeOfReferenceCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._PurposeOfReferenceCodeSequence = value
            if "PurposeOfReferenceCodeSequence" not in self._dataset:
                self._dataset.PurposeOfReferenceCodeSequence = pydicom.Sequence()
            self._dataset.PurposeOfReferenceCodeSequence.clear()
            self._dataset.PurposeOfReferenceCodeSequence.extend([item.to_dataset() for item in value])

    def add_PurposeOfReferenceCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._PurposeOfReferenceCodeSequence.append(item)
        if "PurposeOfReferenceCodeSequence" not in self._dataset:
            self._dataset.PurposeOfReferenceCodeSequence = pydicom.Sequence()
        self._dataset.PurposeOfReferenceCodeSequence.append(item.to_dataset())

    @property
    def ReferencedSegmentNumber(self) -> Optional[List[int]]:
        if "ReferencedSegmentNumber" in self._dataset:
            return self._dataset.ReferencedSegmentNumber
        return None

    @ReferencedSegmentNumber.setter
    def ReferencedSegmentNumber(self, value: Optional[List[int]]):
        if value is None:
            if "ReferencedSegmentNumber" in self._dataset:
                del self._dataset.ReferencedSegmentNumber
        else:
            self._dataset.ReferencedSegmentNumber = value
