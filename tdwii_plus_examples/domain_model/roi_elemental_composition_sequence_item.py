from typing import Any, List, Optional  # noqa

import pydicom


class ROIElementalCompositionSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ROIElementalCompositionAtomicNumber(self) -> Optional[int]:
        if "ROIElementalCompositionAtomicNumber" in self._dataset:
            return self._dataset.ROIElementalCompositionAtomicNumber
        return None

    @ROIElementalCompositionAtomicNumber.setter
    def ROIElementalCompositionAtomicNumber(self, value: Optional[int]):
        if value is None:
            if "ROIElementalCompositionAtomicNumber" in self._dataset:
                del self._dataset.ROIElementalCompositionAtomicNumber
        else:
            self._dataset.ROIElementalCompositionAtomicNumber = value

    @property
    def ROIElementalCompositionAtomicMassFraction(self) -> Optional[float]:
        if "ROIElementalCompositionAtomicMassFraction" in self._dataset:
            return self._dataset.ROIElementalCompositionAtomicMassFraction
        return None

    @ROIElementalCompositionAtomicMassFraction.setter
    def ROIElementalCompositionAtomicMassFraction(self, value: Optional[float]):
        if value is None:
            if "ROIElementalCompositionAtomicMassFraction" in self._dataset:
                del self._dataset.ROIElementalCompositionAtomicMassFraction
        else:
            self._dataset.ROIElementalCompositionAtomicMassFraction = value
