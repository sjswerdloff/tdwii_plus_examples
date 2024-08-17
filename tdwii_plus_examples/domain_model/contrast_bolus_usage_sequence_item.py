from typing import Any, List, Optional  # noqa

import pydicom


class ContrastBolusUsageSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ContrastBolusAgentNumber(self) -> Optional[int]:
        if "ContrastBolusAgentNumber" in self._dataset:
            return self._dataset.ContrastBolusAgentNumber
        return None

    @ContrastBolusAgentNumber.setter
    def ContrastBolusAgentNumber(self, value: Optional[int]):
        if value is None:
            if "ContrastBolusAgentNumber" in self._dataset:
                del self._dataset.ContrastBolusAgentNumber
        else:
            self._dataset.ContrastBolusAgentNumber = value

    @property
    def ContrastBolusAgentAdministered(self) -> Optional[str]:
        if "ContrastBolusAgentAdministered" in self._dataset:
            return self._dataset.ContrastBolusAgentAdministered
        return None

    @ContrastBolusAgentAdministered.setter
    def ContrastBolusAgentAdministered(self, value: Optional[str]):
        if value is None:
            if "ContrastBolusAgentAdministered" in self._dataset:
                del self._dataset.ContrastBolusAgentAdministered
        else:
            self._dataset.ContrastBolusAgentAdministered = value

    @property
    def ContrastBolusAgentDetected(self) -> Optional[str]:
        if "ContrastBolusAgentDetected" in self._dataset:
            return self._dataset.ContrastBolusAgentDetected
        return None

    @ContrastBolusAgentDetected.setter
    def ContrastBolusAgentDetected(self, value: Optional[str]):
        if value is None:
            if "ContrastBolusAgentDetected" in self._dataset:
                del self._dataset.ContrastBolusAgentDetected
        else:
            self._dataset.ContrastBolusAgentDetected = value

    @property
    def ContrastBolusAgentPhase(self) -> Optional[str]:
        if "ContrastBolusAgentPhase" in self._dataset:
            return self._dataset.ContrastBolusAgentPhase
        return None

    @ContrastBolusAgentPhase.setter
    def ContrastBolusAgentPhase(self, value: Optional[str]):
        if value is None:
            if "ContrastBolusAgentPhase" in self._dataset:
                del self._dataset.ContrastBolusAgentPhase
        else:
            self._dataset.ContrastBolusAgentPhase = value
