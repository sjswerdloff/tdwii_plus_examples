from typing import Any, List, Optional  # noqa

import pydicom


class OmittedBeamTaskSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ReferencedBeamNumber(self) -> Optional[int]:
        if "ReferencedBeamNumber" in self._dataset:
            return self._dataset.ReferencedBeamNumber
        return None

    @ReferencedBeamNumber.setter
    def ReferencedBeamNumber(self, value: Optional[int]):
        if value is None:
            if "ReferencedBeamNumber" in self._dataset:
                del self._dataset.ReferencedBeamNumber
        else:
            self._dataset.ReferencedBeamNumber = value

    @property
    def ReasonForOmission(self) -> Optional[str]:
        if "ReasonForOmission" in self._dataset:
            return self._dataset.ReasonForOmission
        return None

    @ReasonForOmission.setter
    def ReasonForOmission(self, value: Optional[str]):
        if value is None:
            if "ReasonForOmission" in self._dataset:
                del self._dataset.ReasonForOmission
        else:
            self._dataset.ReasonForOmission = value

    @property
    def ReasonForOmissionDescription(self) -> Optional[str]:
        if "ReasonForOmissionDescription" in self._dataset:
            return self._dataset.ReasonForOmissionDescription
        return None

    @ReasonForOmissionDescription.setter
    def ReasonForOmissionDescription(self, value: Optional[str]):
        if value is None:
            if "ReasonForOmissionDescription" in self._dataset:
                del self._dataset.ReasonForOmissionDescription
        else:
            self._dataset.ReasonForOmissionDescription = value
