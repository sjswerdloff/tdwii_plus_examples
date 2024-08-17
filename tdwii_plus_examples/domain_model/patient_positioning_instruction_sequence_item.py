from typing import Any, List, Optional  # noqa

import pydicom


class PatientPositioningInstructionSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def InstructionIndex(self) -> Optional[int]:
        if "InstructionIndex" in self._dataset:
            return self._dataset.InstructionIndex
        return None

    @InstructionIndex.setter
    def InstructionIndex(self, value: Optional[int]):
        if value is None:
            if "InstructionIndex" in self._dataset:
                del self._dataset.InstructionIndex
        else:
            self._dataset.InstructionIndex = value

    @property
    def InstructionText(self) -> Optional[str]:
        if "InstructionText" in self._dataset:
            return self._dataset.InstructionText
        return None

    @InstructionText.setter
    def InstructionText(self, value: Optional[str]):
        if value is None:
            if "InstructionText" in self._dataset:
                del self._dataset.InstructionText
        else:
            self._dataset.InstructionText = value

    @property
    def InstructionDescription(self) -> Optional[str]:
        if "InstructionDescription" in self._dataset:
            return self._dataset.InstructionDescription
        return None

    @InstructionDescription.setter
    def InstructionDescription(self, value: Optional[str]):
        if value is None:
            if "InstructionDescription" in self._dataset:
                del self._dataset.InstructionDescription
        else:
            self._dataset.InstructionDescription = value

    @property
    def InstructionPerformedFlag(self) -> Optional[str]:
        if "InstructionPerformedFlag" in self._dataset:
            return self._dataset.InstructionPerformedFlag
        return None

    @InstructionPerformedFlag.setter
    def InstructionPerformedFlag(self, value: Optional[str]):
        if value is None:
            if "InstructionPerformedFlag" in self._dataset:
                del self._dataset.InstructionPerformedFlag
        else:
            self._dataset.InstructionPerformedFlag = value

    @property
    def InstructionPerformedDateTime(self) -> Optional[str]:
        if "InstructionPerformedDateTime" in self._dataset:
            return self._dataset.InstructionPerformedDateTime
        return None

    @InstructionPerformedDateTime.setter
    def InstructionPerformedDateTime(self, value: Optional[str]):
        if value is None:
            if "InstructionPerformedDateTime" in self._dataset:
                del self._dataset.InstructionPerformedDateTime
        else:
            self._dataset.InstructionPerformedDateTime = value
