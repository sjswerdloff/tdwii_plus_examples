from typing import Any, List, Optional  # noqa

import pydicom


class DepthDoseParametersSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def DistalDepthFraction(self) -> Optional[float]:
        if "DistalDepthFraction" in self._dataset:
            return self._dataset.DistalDepthFraction
        return None

    @DistalDepthFraction.setter
    def DistalDepthFraction(self, value: Optional[float]):
        if value is None:
            if "DistalDepthFraction" in self._dataset:
                del self._dataset.DistalDepthFraction
        else:
            self._dataset.DistalDepthFraction = value

    @property
    def DistalDepth(self) -> Optional[float]:
        if "DistalDepth" in self._dataset:
            return self._dataset.DistalDepth
        return None

    @DistalDepth.setter
    def DistalDepth(self, value: Optional[float]):
        if value is None:
            if "DistalDepth" in self._dataset:
                del self._dataset.DistalDepth
        else:
            self._dataset.DistalDepth = value

    @property
    def NominalRangeModulationFractions(self) -> Optional[List[float]]:
        if "NominalRangeModulationFractions" in self._dataset:
            return self._dataset.NominalRangeModulationFractions
        return None

    @NominalRangeModulationFractions.setter
    def NominalRangeModulationFractions(self, value: Optional[List[float]]):
        if value is None:
            if "NominalRangeModulationFractions" in self._dataset:
                del self._dataset.NominalRangeModulationFractions
        else:
            self._dataset.NominalRangeModulationFractions = value

    @property
    def NominalRangeModulatedRegionDepths(self) -> Optional[List[float]]:
        if "NominalRangeModulatedRegionDepths" in self._dataset:
            return self._dataset.NominalRangeModulatedRegionDepths
        return None

    @NominalRangeModulatedRegionDepths.setter
    def NominalRangeModulatedRegionDepths(self, value: Optional[List[float]]):
        if value is None:
            if "NominalRangeModulatedRegionDepths" in self._dataset:
                del self._dataset.NominalRangeModulatedRegionDepths
        else:
            self._dataset.NominalRangeModulatedRegionDepths = value

    @property
    def ReferenceDoseDefinition(self) -> Optional[str]:
        if "ReferenceDoseDefinition" in self._dataset:
            return self._dataset.ReferenceDoseDefinition
        return None

    @ReferenceDoseDefinition.setter
    def ReferenceDoseDefinition(self, value: Optional[str]):
        if value is None:
            if "ReferenceDoseDefinition" in self._dataset:
                del self._dataset.ReferenceDoseDefinition
        else:
            self._dataset.ReferenceDoseDefinition = value
