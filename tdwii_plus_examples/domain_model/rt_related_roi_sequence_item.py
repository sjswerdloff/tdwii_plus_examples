from typing import Any, List, Optional  # noqa

import pydicom


class RTRelatedROISequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def RTROIRelationship(self) -> Optional[str]:
        if "RTROIRelationship" in self._dataset:
            return self._dataset.RTROIRelationship
        return None

    @RTROIRelationship.setter
    def RTROIRelationship(self, value: Optional[str]):
        if value is None:
            if "RTROIRelationship" in self._dataset:
                del self._dataset.RTROIRelationship
        else:
            self._dataset.RTROIRelationship = value

    @property
    def ReferencedROINumber(self) -> Optional[int]:
        if "ReferencedROINumber" in self._dataset:
            return self._dataset.ReferencedROINumber
        return None

    @ReferencedROINumber.setter
    def ReferencedROINumber(self, value: Optional[int]):
        if value is None:
            if "ReferencedROINumber" in self._dataset:
                del self._dataset.ReferencedROINumber
        else:
            self._dataset.ReferencedROINumber = value
