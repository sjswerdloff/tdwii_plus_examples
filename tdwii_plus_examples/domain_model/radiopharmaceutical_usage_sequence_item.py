from typing import Any, List, Optional

import pydicom


class RadiopharmaceuticalUsageSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def RadiopharmaceuticalAgentNumber(self) -> Optional[int]:
        if "RadiopharmaceuticalAgentNumber" in self._dataset:
            return self._dataset.RadiopharmaceuticalAgentNumber
        return None

    @RadiopharmaceuticalAgentNumber.setter
    def RadiopharmaceuticalAgentNumber(self, value: Optional[int]):
        if value is None:
            if "RadiopharmaceuticalAgentNumber" in self._dataset:
                del self._dataset.RadiopharmaceuticalAgentNumber
        else:
            self._dataset.RadiopharmaceuticalAgentNumber = value
