from typing import Any, List, Optional

import pydicom

from .predicted_toric_error_sequence_item import PredictedToricErrorSequenceItem
from .toric_iol_power_sequence_item import ToricIOLPowerSequenceItem


class IOLPowerSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._ToricIOLPowerSequence: List[ToricIOLPowerSequenceItem] = []
        self._PredictedToricErrorSequence: List[PredictedToricErrorSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ToricIOLPowerSequence(self) -> Optional[List[ToricIOLPowerSequenceItem]]:
        if "ToricIOLPowerSequence" in self._dataset:
            if len(self._ToricIOLPowerSequence) == len(self._dataset.ToricIOLPowerSequence):
                return self._ToricIOLPowerSequence
            else:
                return [ToricIOLPowerSequenceItem(x) for x in self._dataset.ToricIOLPowerSequence]
        return None

    @ToricIOLPowerSequence.setter
    def ToricIOLPowerSequence(self, value: Optional[List[ToricIOLPowerSequenceItem]]):
        if value is None:
            self._ToricIOLPowerSequence = []
            if "ToricIOLPowerSequence" in self._dataset:
                del self._dataset.ToricIOLPowerSequence
        elif not isinstance(value, list) or not all(isinstance(item, ToricIOLPowerSequenceItem) for item in value):
            raise ValueError(f"ToricIOLPowerSequence must be a list of ToricIOLPowerSequenceItem objects")
        else:
            self._ToricIOLPowerSequence = value
            if "ToricIOLPowerSequence" not in self._dataset:
                self._dataset.ToricIOLPowerSequence = pydicom.Sequence()
            self._dataset.ToricIOLPowerSequence.clear()
            self._dataset.ToricIOLPowerSequence.extend([item.to_dataset() for item in value])

    def add_ToricIOLPower(self, item: ToricIOLPowerSequenceItem):
        if not isinstance(item, ToricIOLPowerSequenceItem):
            raise ValueError(f"Item must be an instance of ToricIOLPowerSequenceItem")
        self._ToricIOLPowerSequence.append(item)
        if "ToricIOLPowerSequence" not in self._dataset:
            self._dataset.ToricIOLPowerSequence = pydicom.Sequence()
        self._dataset.ToricIOLPowerSequence.append(item.to_dataset())

    @property
    def PredictedToricErrorSequence(self) -> Optional[List[PredictedToricErrorSequenceItem]]:
        if "PredictedToricErrorSequence" in self._dataset:
            if len(self._PredictedToricErrorSequence) == len(self._dataset.PredictedToricErrorSequence):
                return self._PredictedToricErrorSequence
            else:
                return [PredictedToricErrorSequenceItem(x) for x in self._dataset.PredictedToricErrorSequence]
        return None

    @PredictedToricErrorSequence.setter
    def PredictedToricErrorSequence(self, value: Optional[List[PredictedToricErrorSequenceItem]]):
        if value is None:
            self._PredictedToricErrorSequence = []
            if "PredictedToricErrorSequence" in self._dataset:
                del self._dataset.PredictedToricErrorSequence
        elif not isinstance(value, list) or not all(isinstance(item, PredictedToricErrorSequenceItem) for item in value):
            raise ValueError(f"PredictedToricErrorSequence must be a list of PredictedToricErrorSequenceItem objects")
        else:
            self._PredictedToricErrorSequence = value
            if "PredictedToricErrorSequence" not in self._dataset:
                self._dataset.PredictedToricErrorSequence = pydicom.Sequence()
            self._dataset.PredictedToricErrorSequence.clear()
            self._dataset.PredictedToricErrorSequence.extend([item.to_dataset() for item in value])

    def add_PredictedToricError(self, item: PredictedToricErrorSequenceItem):
        if not isinstance(item, PredictedToricErrorSequenceItem):
            raise ValueError(f"Item must be an instance of PredictedToricErrorSequenceItem")
        self._PredictedToricErrorSequence.append(item)
        if "PredictedToricErrorSequence" not in self._dataset:
            self._dataset.PredictedToricErrorSequence = pydicom.Sequence()
        self._dataset.PredictedToricErrorSequence.append(item.to_dataset())

    @property
    def PreSelectedForImplantation(self) -> Optional[str]:
        if "PreSelectedForImplantation" in self._dataset:
            return self._dataset.PreSelectedForImplantation
        return None

    @PreSelectedForImplantation.setter
    def PreSelectedForImplantation(self, value: Optional[str]):
        if value is None:
            if "PreSelectedForImplantation" in self._dataset:
                del self._dataset.PreSelectedForImplantation
        else:
            self._dataset.PreSelectedForImplantation = value

    @property
    def IOLPower(self) -> Optional[float]:
        if "IOLPower" in self._dataset:
            return self._dataset.IOLPower
        return None

    @IOLPower.setter
    def IOLPower(self, value: Optional[float]):
        if value is None:
            if "IOLPower" in self._dataset:
                del self._dataset.IOLPower
        else:
            self._dataset.IOLPower = value

    @property
    def PredictedRefractiveError(self) -> Optional[float]:
        if "PredictedRefractiveError" in self._dataset:
            return self._dataset.PredictedRefractiveError
        return None

    @PredictedRefractiveError.setter
    def PredictedRefractiveError(self, value: Optional[float]):
        if value is None:
            if "PredictedRefractiveError" in self._dataset:
                del self._dataset.PredictedRefractiveError
        else:
            self._dataset.PredictedRefractiveError = value

    @property
    def ImplantPartNumber(self) -> Optional[str]:
        if "ImplantPartNumber" in self._dataset:
            return self._dataset.ImplantPartNumber
        return None

    @ImplantPartNumber.setter
    def ImplantPartNumber(self, value: Optional[str]):
        if value is None:
            if "ImplantPartNumber" in self._dataset:
                del self._dataset.ImplantPartNumber
        else:
            self._dataset.ImplantPartNumber = value
