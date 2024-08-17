from decimal import Decimal
from typing import Any, List, Optional  # noqa

import pydicom


class PETReconstructionSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ReconstructionDiameter(self) -> Optional[Decimal]:
        if "ReconstructionDiameter" in self._dataset:
            return self._dataset.ReconstructionDiameter
        return None

    @ReconstructionDiameter.setter
    def ReconstructionDiameter(self, value: Optional[Decimal]):
        if value is None:
            if "ReconstructionDiameter" in self._dataset:
                del self._dataset.ReconstructionDiameter
        else:
            self._dataset.ReconstructionDiameter = value

    @property
    def ReconstructionAlgorithm(self) -> Optional[str]:
        if "ReconstructionAlgorithm" in self._dataset:
            return self._dataset.ReconstructionAlgorithm
        return None

    @ReconstructionAlgorithm.setter
    def ReconstructionAlgorithm(self, value: Optional[str]):
        if value is None:
            if "ReconstructionAlgorithm" in self._dataset:
                del self._dataset.ReconstructionAlgorithm
        else:
            self._dataset.ReconstructionAlgorithm = value

    @property
    def ReconstructionFieldOfView(self) -> Optional[List[float]]:
        if "ReconstructionFieldOfView" in self._dataset:
            return self._dataset.ReconstructionFieldOfView
        return None

    @ReconstructionFieldOfView.setter
    def ReconstructionFieldOfView(self, value: Optional[List[float]]):
        if value is None:
            if "ReconstructionFieldOfView" in self._dataset:
                del self._dataset.ReconstructionFieldOfView
        else:
            self._dataset.ReconstructionFieldOfView = value

    @property
    def NumberOfIterations(self) -> Optional[int]:
        if "NumberOfIterations" in self._dataset:
            return self._dataset.NumberOfIterations
        return None

    @NumberOfIterations.setter
    def NumberOfIterations(self, value: Optional[int]):
        if value is None:
            if "NumberOfIterations" in self._dataset:
                del self._dataset.NumberOfIterations
        else:
            self._dataset.NumberOfIterations = value

    @property
    def NumberOfSubsets(self) -> Optional[int]:
        if "NumberOfSubsets" in self._dataset:
            return self._dataset.NumberOfSubsets
        return None

    @NumberOfSubsets.setter
    def NumberOfSubsets(self, value: Optional[int]):
        if value is None:
            if "NumberOfSubsets" in self._dataset:
                del self._dataset.NumberOfSubsets
        else:
            self._dataset.NumberOfSubsets = value

    @property
    def ReconstructionType(self) -> Optional[str]:
        if "ReconstructionType" in self._dataset:
            return self._dataset.ReconstructionType
        return None

    @ReconstructionType.setter
    def ReconstructionType(self, value: Optional[str]):
        if value is None:
            if "ReconstructionType" in self._dataset:
                del self._dataset.ReconstructionType
        else:
            self._dataset.ReconstructionType = value

    @property
    def IterativeReconstructionMethod(self) -> Optional[str]:
        if "IterativeReconstructionMethod" in self._dataset:
            return self._dataset.IterativeReconstructionMethod
        return None

    @IterativeReconstructionMethod.setter
    def IterativeReconstructionMethod(self, value: Optional[str]):
        if value is None:
            if "IterativeReconstructionMethod" in self._dataset:
                del self._dataset.IterativeReconstructionMethod
        else:
            self._dataset.IterativeReconstructionMethod = value
