from typing import Any, List, Optional

import pydicom


class RelatedAssertionSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ReferencedAssertionUID(self) -> Optional[str]:
        if "ReferencedAssertionUID" in self._dataset:
            return self._dataset.ReferencedAssertionUID
        return None

    @ReferencedAssertionUID.setter
    def ReferencedAssertionUID(self, value: Optional[str]):
        if value is None:
            if "ReferencedAssertionUID" in self._dataset:
                del self._dataset.ReferencedAssertionUID
        else:
            self._dataset.ReferencedAssertionUID = value
