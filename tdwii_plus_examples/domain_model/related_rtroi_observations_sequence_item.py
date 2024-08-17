from typing import Any, List, Optional  # noqa

import pydicom


class RelatedRTROIObservationsSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ObservationNumber(self) -> Optional[int]:
        if "ObservationNumber" in self._dataset:
            return self._dataset.ObservationNumber
        return None

    @ObservationNumber.setter
    def ObservationNumber(self, value: Optional[int]):
        if value is None:
            if "ObservationNumber" in self._dataset:
                del self._dataset.ObservationNumber
        else:
            self._dataset.ObservationNumber = value
