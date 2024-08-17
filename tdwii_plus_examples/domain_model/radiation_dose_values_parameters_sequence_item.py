from typing import Any, List, Optional

import pydicom

from .dose_values_sequence_item import DoseValuesSequenceItem


class RadiationDoseValuesParametersSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._DoseValuesSequence: List[DoseValuesSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ReferencedRadiationDoseIdentificationIndex(self) -> Optional[int]:
        if "ReferencedRadiationDoseIdentificationIndex" in self._dataset:
            return self._dataset.ReferencedRadiationDoseIdentificationIndex
        return None

    @ReferencedRadiationDoseIdentificationIndex.setter
    def ReferencedRadiationDoseIdentificationIndex(self, value: Optional[int]):
        if value is None:
            if "ReferencedRadiationDoseIdentificationIndex" in self._dataset:
                del self._dataset.ReferencedRadiationDoseIdentificationIndex
        else:
            self._dataset.ReferencedRadiationDoseIdentificationIndex = value

    @property
    def PrimaryDoseValueIndicator(self) -> Optional[str]:
        if "PrimaryDoseValueIndicator" in self._dataset:
            return self._dataset.PrimaryDoseValueIndicator
        return None

    @PrimaryDoseValueIndicator.setter
    def PrimaryDoseValueIndicator(self, value: Optional[str]):
        if value is None:
            if "PrimaryDoseValueIndicator" in self._dataset:
                del self._dataset.PrimaryDoseValueIndicator
        else:
            self._dataset.PrimaryDoseValueIndicator = value

    @property
    def DoseValuesSequence(self) -> Optional[List[DoseValuesSequenceItem]]:
        if "DoseValuesSequence" in self._dataset:
            if len(self._DoseValuesSequence) == len(self._dataset.DoseValuesSequence):
                return self._DoseValuesSequence
            else:
                return [DoseValuesSequenceItem(x) for x in self._dataset.DoseValuesSequence]
        return None

    @DoseValuesSequence.setter
    def DoseValuesSequence(self, value: Optional[List[DoseValuesSequenceItem]]):
        if value is None:
            self._DoseValuesSequence = []
            if "DoseValuesSequence" in self._dataset:
                del self._dataset.DoseValuesSequence
        elif not isinstance(value, list) or not all(isinstance(item, DoseValuesSequenceItem) for item in value):
            raise ValueError(f"DoseValuesSequence must be a list of DoseValuesSequenceItem objects")
        else:
            self._DoseValuesSequence = value
            if "DoseValuesSequence" not in self._dataset:
                self._dataset.DoseValuesSequence = pydicom.Sequence()
            self._dataset.DoseValuesSequence.clear()
            self._dataset.DoseValuesSequence.extend([item.to_dataset() for item in value])

    def add_DoseValues(self, item: DoseValuesSequenceItem):
        if not isinstance(item, DoseValuesSequenceItem):
            raise ValueError(f"Item must be an instance of DoseValuesSequenceItem")
        self._DoseValuesSequence.append(item)
        if "DoseValuesSequence" not in self._dataset:
            self._dataset.DoseValuesSequence = pydicom.Sequence()
        self._dataset.DoseValuesSequence.append(item.to_dataset())
