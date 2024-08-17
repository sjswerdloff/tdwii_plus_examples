from typing import Any, List, Optional

import pydicom


class PETTableDynamicsSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def TableSpeed(self) -> Optional[float]:
        if "TableSpeed" in self._dataset:
            return self._dataset.TableSpeed
        return None

    @TableSpeed.setter
    def TableSpeed(self, value: Optional[float]):
        if value is None:
            if "TableSpeed" in self._dataset:
                del self._dataset.TableSpeed
        else:
            self._dataset.TableSpeed = value
