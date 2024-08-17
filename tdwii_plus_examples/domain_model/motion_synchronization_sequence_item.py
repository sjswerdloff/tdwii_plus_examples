from typing import Any, List, Optional  # noqa

import pydicom


class MotionSynchronizationSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def RespiratoryMotionCompensationTechnique(self) -> Optional[str]:
        if "RespiratoryMotionCompensationTechnique" in self._dataset:
            return self._dataset.RespiratoryMotionCompensationTechnique
        return None

    @RespiratoryMotionCompensationTechnique.setter
    def RespiratoryMotionCompensationTechnique(self, value: Optional[str]):
        if value is None:
            if "RespiratoryMotionCompensationTechnique" in self._dataset:
                del self._dataset.RespiratoryMotionCompensationTechnique
        else:
            self._dataset.RespiratoryMotionCompensationTechnique = value

    @property
    def RespiratorySignalSource(self) -> Optional[str]:
        if "RespiratorySignalSource" in self._dataset:
            return self._dataset.RespiratorySignalSource
        return None

    @RespiratorySignalSource.setter
    def RespiratorySignalSource(self, value: Optional[str]):
        if value is None:
            if "RespiratorySignalSource" in self._dataset:
                del self._dataset.RespiratorySignalSource
        else:
            self._dataset.RespiratorySignalSource = value

    @property
    def RespiratoryMotionCompensationTechniqueDescription(self) -> Optional[str]:
        if "RespiratoryMotionCompensationTechniqueDescription" in self._dataset:
            return self._dataset.RespiratoryMotionCompensationTechniqueDescription
        return None

    @RespiratoryMotionCompensationTechniqueDescription.setter
    def RespiratoryMotionCompensationTechniqueDescription(self, value: Optional[str]):
        if value is None:
            if "RespiratoryMotionCompensationTechniqueDescription" in self._dataset:
                del self._dataset.RespiratoryMotionCompensationTechniqueDescription
        else:
            self._dataset.RespiratoryMotionCompensationTechniqueDescription = value

    @property
    def RespiratorySignalSourceID(self) -> Optional[str]:
        if "RespiratorySignalSourceID" in self._dataset:
            return self._dataset.RespiratorySignalSourceID
        return None

    @RespiratorySignalSourceID.setter
    def RespiratorySignalSourceID(self, value: Optional[str]):
        if value is None:
            if "RespiratorySignalSourceID" in self._dataset:
                del self._dataset.RespiratorySignalSourceID
        else:
            self._dataset.RespiratorySignalSourceID = value
