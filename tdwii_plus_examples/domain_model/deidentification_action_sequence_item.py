from typing import Any, List, Optional

import pydicom


class DeidentificationActionSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def IdentifyingPrivateElements(self) -> Optional[List[int]]:
        if "IdentifyingPrivateElements" in self._dataset:
            return self._dataset.IdentifyingPrivateElements
        return None

    @IdentifyingPrivateElements.setter
    def IdentifyingPrivateElements(self, value: Optional[List[int]]):
        if value is None:
            if "IdentifyingPrivateElements" in self._dataset:
                del self._dataset.IdentifyingPrivateElements
        else:
            self._dataset.IdentifyingPrivateElements = value

    @property
    def DeidentificationAction(self) -> Optional[str]:
        if "DeidentificationAction" in self._dataset:
            return self._dataset.DeidentificationAction
        return None

    @DeidentificationAction.setter
    def DeidentificationAction(self, value: Optional[str]):
        if value is None:
            if "DeidentificationAction" in self._dataset:
                del self._dataset.DeidentificationAction
        else:
            self._dataset.DeidentificationAction = value
