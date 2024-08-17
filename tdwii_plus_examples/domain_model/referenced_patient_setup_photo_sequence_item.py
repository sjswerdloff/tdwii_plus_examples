from typing import Any, List, Optional

import pydicom


class ReferencedPatientSetupPhotoSequenceItem:
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
    def PatientSetupPhotoDescription(self) -> Optional[str]:
        if "PatientSetupPhotoDescription" in self._dataset:
            return self._dataset.PatientSetupPhotoDescription
        return None

    @PatientSetupPhotoDescription.setter
    def PatientSetupPhotoDescription(self, value: Optional[str]):
        if value is None:
            if "PatientSetupPhotoDescription" in self._dataset:
                del self._dataset.PatientSetupPhotoDescription
        else:
            self._dataset.PatientSetupPhotoDescription = value

    @property
    def ReferencedPatientSetupProcedureIndex(self) -> Optional[int]:
        if "ReferencedPatientSetupProcedureIndex" in self._dataset:
            return self._dataset.ReferencedPatientSetupProcedureIndex
        return None

    @ReferencedPatientSetupProcedureIndex.setter
    def ReferencedPatientSetupProcedureIndex(self, value: Optional[int]):
        if value is None:
            if "ReferencedPatientSetupProcedureIndex" in self._dataset:
                del self._dataset.ReferencedPatientSetupProcedureIndex
        else:
            self._dataset.ReferencedPatientSetupProcedureIndex = value
