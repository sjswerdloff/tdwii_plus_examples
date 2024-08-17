from typing import Any, List, Optional

import pydicom


class OmittedChannelSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ReferencedChannelNumber(self) -> Optional[int]:
        if "ReferencedChannelNumber" in self._dataset:
            return self._dataset.ReferencedChannelNumber
        return None

    @ReferencedChannelNumber.setter
    def ReferencedChannelNumber(self, value: Optional[int]):
        if value is None:
            if "ReferencedChannelNumber" in self._dataset:
                del self._dataset.ReferencedChannelNumber
        else:
            self._dataset.ReferencedChannelNumber = value

    @property
    def ReasonForChannelOmission(self) -> Optional[str]:
        if "ReasonForChannelOmission" in self._dataset:
            return self._dataset.ReasonForChannelOmission
        return None

    @ReasonForChannelOmission.setter
    def ReasonForChannelOmission(self, value: Optional[str]):
        if value is None:
            if "ReasonForChannelOmission" in self._dataset:
                del self._dataset.ReasonForChannelOmission
        else:
            self._dataset.ReasonForChannelOmission = value

    @property
    def ReasonForChannelOmissionDescription(self) -> Optional[str]:
        if "ReasonForChannelOmissionDescription" in self._dataset:
            return self._dataset.ReasonForChannelOmissionDescription
        return None

    @ReasonForChannelOmissionDescription.setter
    def ReasonForChannelOmissionDescription(self, value: Optional[str]):
        if value is None:
            if "ReasonForChannelOmissionDescription" in self._dataset:
                del self._dataset.ReasonForChannelOmissionDescription
        else:
            self._dataset.ReasonForChannelOmissionDescription = value
