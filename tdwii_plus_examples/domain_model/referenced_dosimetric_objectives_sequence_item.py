from typing import Any, List, Optional  # noqa

import pydicom


class ReferencedDosimetricObjectivesSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ReferencedDosimetricObjectiveUID(self) -> Optional[str]:
        if "ReferencedDosimetricObjectiveUID" in self._dataset:
            return self._dataset.ReferencedDosimetricObjectiveUID
        return None

    @ReferencedDosimetricObjectiveUID.setter
    def ReferencedDosimetricObjectiveUID(self, value: Optional[str]):
        if value is None:
            if "ReferencedDosimetricObjectiveUID" in self._dataset:
                del self._dataset.ReferencedDosimetricObjectiveUID
        else:
            self._dataset.ReferencedDosimetricObjectiveUID = value

    @property
    def DosimetricObjectiveWeight(self) -> Optional[float]:
        if "DosimetricObjectiveWeight" in self._dataset:
            return self._dataset.DosimetricObjectiveWeight
        return None

    @DosimetricObjectiveWeight.setter
    def DosimetricObjectiveWeight(self, value: Optional[float]):
        if value is None:
            if "DosimetricObjectiveWeight" in self._dataset:
                del self._dataset.DosimetricObjectiveWeight
        else:
            self._dataset.DosimetricObjectiveWeight = value
