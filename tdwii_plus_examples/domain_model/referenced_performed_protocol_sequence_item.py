from typing import Any, List, Optional  # noqa

import pydicom


class ReferencedPerformedProtocolSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

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
    def SourceAcquisitionProtocolElementNumber(self) -> Optional[List[int]]:
        if "SourceAcquisitionProtocolElementNumber" in self._dataset:
            return self._dataset.SourceAcquisitionProtocolElementNumber
        return None

    @SourceAcquisitionProtocolElementNumber.setter
    def SourceAcquisitionProtocolElementNumber(self, value: Optional[List[int]]):
        if value is None:
            if "SourceAcquisitionProtocolElementNumber" in self._dataset:
                del self._dataset.SourceAcquisitionProtocolElementNumber
        else:
            self._dataset.SourceAcquisitionProtocolElementNumber = value

    @property
    def SourceReconstructionProtocolElementNumber(self) -> Optional[List[int]]:
        if "SourceReconstructionProtocolElementNumber" in self._dataset:
            return self._dataset.SourceReconstructionProtocolElementNumber
        return None

    @SourceReconstructionProtocolElementNumber.setter
    def SourceReconstructionProtocolElementNumber(self, value: Optional[List[int]]):
        if value is None:
            if "SourceReconstructionProtocolElementNumber" in self._dataset:
                del self._dataset.SourceReconstructionProtocolElementNumber
        else:
            self._dataset.SourceReconstructionProtocolElementNumber = value
