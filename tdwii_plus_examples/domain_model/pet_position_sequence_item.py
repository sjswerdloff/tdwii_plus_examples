from typing import Any, List, Optional  # noqa

import pydicom


class PETPositionSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def DataCollectionCenterPatient(self) -> Optional[List[float]]:
        if "DataCollectionCenterPatient" in self._dataset:
            return self._dataset.DataCollectionCenterPatient
        return None

    @DataCollectionCenterPatient.setter
    def DataCollectionCenterPatient(self, value: Optional[List[float]]):
        if value is None:
            if "DataCollectionCenterPatient" in self._dataset:
                del self._dataset.DataCollectionCenterPatient
        else:
            self._dataset.DataCollectionCenterPatient = value

    @property
    def ReconstructionTargetCenterPatient(self) -> Optional[List[float]]:
        if "ReconstructionTargetCenterPatient" in self._dataset:
            return self._dataset.ReconstructionTargetCenterPatient
        return None

    @ReconstructionTargetCenterPatient.setter
    def ReconstructionTargetCenterPatient(self, value: Optional[List[float]]):
        if value is None:
            if "ReconstructionTargetCenterPatient" in self._dataset:
                del self._dataset.ReconstructionTargetCenterPatient
        else:
            self._dataset.ReconstructionTargetCenterPatient = value

    @property
    def TablePosition(self) -> Optional[float]:
        if "TablePosition" in self._dataset:
            return self._dataset.TablePosition
        return None

    @TablePosition.setter
    def TablePosition(self, value: Optional[float]):
        if value is None:
            if "TablePosition" in self._dataset:
                del self._dataset.TablePosition
        else:
            self._dataset.TablePosition = value
