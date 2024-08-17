from typing import Any, List, Optional

import pydicom


class IrradiationEventIdentificationSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def IrradiationEventUID(self) -> Optional[List[str]]:
        if "IrradiationEventUID" in self._dataset:
            return self._dataset.IrradiationEventUID
        return None

    @IrradiationEventUID.setter
    def IrradiationEventUID(self, value: Optional[List[str]]):
        if value is None:
            if "IrradiationEventUID" in self._dataset:
                del self._dataset.IrradiationEventUID
        else:
            self._dataset.IrradiationEventUID = value
