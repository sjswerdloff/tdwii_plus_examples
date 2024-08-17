from typing import Any, List, Optional

import pydicom


class XRay3DReconstructionSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ApplicationName(self) -> Optional[str]:
        if "ApplicationName" in self._dataset:
            return self._dataset.ApplicationName
        return None

    @ApplicationName.setter
    def ApplicationName(self, value: Optional[str]):
        if value is None:
            if "ApplicationName" in self._dataset:
                del self._dataset.ApplicationName
        else:
            self._dataset.ApplicationName = value

    @property
    def ApplicationVersion(self) -> Optional[str]:
        if "ApplicationVersion" in self._dataset:
            return self._dataset.ApplicationVersion
        return None

    @ApplicationVersion.setter
    def ApplicationVersion(self, value: Optional[str]):
        if value is None:
            if "ApplicationVersion" in self._dataset:
                del self._dataset.ApplicationVersion
        else:
            self._dataset.ApplicationVersion = value

    @property
    def ApplicationManufacturer(self) -> Optional[str]:
        if "ApplicationManufacturer" in self._dataset:
            return self._dataset.ApplicationManufacturer
        return None

    @ApplicationManufacturer.setter
    def ApplicationManufacturer(self, value: Optional[str]):
        if value is None:
            if "ApplicationManufacturer" in self._dataset:
                del self._dataset.ApplicationManufacturer
        else:
            self._dataset.ApplicationManufacturer = value

    @property
    def AlgorithmType(self) -> Optional[str]:
        if "AlgorithmType" in self._dataset:
            return self._dataset.AlgorithmType
        return None

    @AlgorithmType.setter
    def AlgorithmType(self, value: Optional[str]):
        if value is None:
            if "AlgorithmType" in self._dataset:
                del self._dataset.AlgorithmType
        else:
            self._dataset.AlgorithmType = value

    @property
    def AlgorithmDescription(self) -> Optional[str]:
        if "AlgorithmDescription" in self._dataset:
            return self._dataset.AlgorithmDescription
        return None

    @AlgorithmDescription.setter
    def AlgorithmDescription(self, value: Optional[str]):
        if value is None:
            if "AlgorithmDescription" in self._dataset:
                del self._dataset.AlgorithmDescription
        else:
            self._dataset.AlgorithmDescription = value

    @property
    def ReconstructionDescription(self) -> Optional[str]:
        if "ReconstructionDescription" in self._dataset:
            return self._dataset.ReconstructionDescription
        return None

    @ReconstructionDescription.setter
    def ReconstructionDescription(self, value: Optional[str]):
        if value is None:
            if "ReconstructionDescription" in self._dataset:
                del self._dataset.ReconstructionDescription
        else:
            self._dataset.ReconstructionDescription = value

    @property
    def AcquisitionIndex(self) -> Optional[List[int]]:
        if "AcquisitionIndex" in self._dataset:
            return self._dataset.AcquisitionIndex
        return None

    @AcquisitionIndex.setter
    def AcquisitionIndex(self, value: Optional[List[int]]):
        if value is None:
            if "AcquisitionIndex" in self._dataset:
                del self._dataset.AcquisitionIndex
        else:
            self._dataset.AcquisitionIndex = value
