from decimal import Decimal
from typing import Any, List, Optional  # noqa

import pydicom


class ReferencedVerificationImageSequenceItem:
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
    def StartMeterset(self) -> Optional[Decimal]:
        if "StartMeterset" in self._dataset:
            return self._dataset.StartMeterset
        return None

    @StartMeterset.setter
    def StartMeterset(self, value: Optional[Decimal]):
        if value is None:
            if "StartMeterset" in self._dataset:
                del self._dataset.StartMeterset
        else:
            self._dataset.StartMeterset = value

    @property
    def EndMeterset(self) -> Optional[Decimal]:
        if "EndMeterset" in self._dataset:
            return self._dataset.EndMeterset
        return None

    @EndMeterset.setter
    def EndMeterset(self, value: Optional[Decimal]):
        if value is None:
            if "EndMeterset" in self._dataset:
                del self._dataset.EndMeterset
        else:
            self._dataset.EndMeterset = value
