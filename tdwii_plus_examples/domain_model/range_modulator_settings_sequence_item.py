from typing import Any, List, Optional

import pydicom


class RangeModulatorSettingsSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def RangeModulatorGatingStartValue(self) -> Optional[float]:
        if "RangeModulatorGatingStartValue" in self._dataset:
            return self._dataset.RangeModulatorGatingStartValue
        return None

    @RangeModulatorGatingStartValue.setter
    def RangeModulatorGatingStartValue(self, value: Optional[float]):
        if value is None:
            if "RangeModulatorGatingStartValue" in self._dataset:
                del self._dataset.RangeModulatorGatingStartValue
        else:
            self._dataset.RangeModulatorGatingStartValue = value

    @property
    def RangeModulatorGatingStopValue(self) -> Optional[float]:
        if "RangeModulatorGatingStopValue" in self._dataset:
            return self._dataset.RangeModulatorGatingStopValue
        return None

    @RangeModulatorGatingStopValue.setter
    def RangeModulatorGatingStopValue(self, value: Optional[float]):
        if value is None:
            if "RangeModulatorGatingStopValue" in self._dataset:
                del self._dataset.RangeModulatorGatingStopValue
        else:
            self._dataset.RangeModulatorGatingStopValue = value

    @property
    def RangeModulatorGatingStartWaterEquivalentThickness(self) -> Optional[float]:
        if "RangeModulatorGatingStartWaterEquivalentThickness" in self._dataset:
            return self._dataset.RangeModulatorGatingStartWaterEquivalentThickness
        return None

    @RangeModulatorGatingStartWaterEquivalentThickness.setter
    def RangeModulatorGatingStartWaterEquivalentThickness(self, value: Optional[float]):
        if value is None:
            if "RangeModulatorGatingStartWaterEquivalentThickness" in self._dataset:
                del self._dataset.RangeModulatorGatingStartWaterEquivalentThickness
        else:
            self._dataset.RangeModulatorGatingStartWaterEquivalentThickness = value

    @property
    def RangeModulatorGatingStopWaterEquivalentThickness(self) -> Optional[float]:
        if "RangeModulatorGatingStopWaterEquivalentThickness" in self._dataset:
            return self._dataset.RangeModulatorGatingStopWaterEquivalentThickness
        return None

    @RangeModulatorGatingStopWaterEquivalentThickness.setter
    def RangeModulatorGatingStopWaterEquivalentThickness(self, value: Optional[float]):
        if value is None:
            if "RangeModulatorGatingStopWaterEquivalentThickness" in self._dataset:
                del self._dataset.RangeModulatorGatingStopWaterEquivalentThickness
        else:
            self._dataset.RangeModulatorGatingStopWaterEquivalentThickness = value

    @property
    def IsocenterToRangeModulatorDistance(self) -> Optional[float]:
        if "IsocenterToRangeModulatorDistance" in self._dataset:
            return self._dataset.IsocenterToRangeModulatorDistance
        return None

    @IsocenterToRangeModulatorDistance.setter
    def IsocenterToRangeModulatorDistance(self, value: Optional[float]):
        if value is None:
            if "IsocenterToRangeModulatorDistance" in self._dataset:
                del self._dataset.IsocenterToRangeModulatorDistance
        else:
            self._dataset.IsocenterToRangeModulatorDistance = value

    @property
    def ReferencedRangeModulatorNumber(self) -> Optional[int]:
        if "ReferencedRangeModulatorNumber" in self._dataset:
            return self._dataset.ReferencedRangeModulatorNumber
        return None

    @ReferencedRangeModulatorNumber.setter
    def ReferencedRangeModulatorNumber(self, value: Optional[int]):
        if value is None:
            if "ReferencedRangeModulatorNumber" in self._dataset:
                del self._dataset.ReferencedRangeModulatorNumber
        else:
            self._dataset.ReferencedRangeModulatorNumber = value
