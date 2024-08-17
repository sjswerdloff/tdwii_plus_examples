from typing import Any, List, Optional  # noqa

import pydicom


class PertinentDocumentsSequenceItem:
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
    def HL7InstanceIdentifier(self) -> Optional[str]:
        if "HL7InstanceIdentifier" in self._dataset:
            return self._dataset.HL7InstanceIdentifier
        return None

    @HL7InstanceIdentifier.setter
    def HL7InstanceIdentifier(self, value: Optional[str]):
        if value is None:
            if "HL7InstanceIdentifier" in self._dataset:
                del self._dataset.HL7InstanceIdentifier
        else:
            self._dataset.HL7InstanceIdentifier = value

    @property
    def RetrieveURI(self) -> Optional[str]:
        if "RetrieveURI" in self._dataset:
            return self._dataset.RetrieveURI
        return None

    @RetrieveURI.setter
    def RetrieveURI(self, value: Optional[str]):
        if value is None:
            if "RetrieveURI" in self._dataset:
                del self._dataset.RetrieveURI
        else:
            self._dataset.RetrieveURI = value
