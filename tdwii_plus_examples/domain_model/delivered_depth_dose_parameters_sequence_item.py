from typing import Any, List, Optional  # noqa

import pydicom


class DeliveredDepthDoseParametersSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def DeliveredDistalDepthFraction(self) -> Optional[float]:
        if "DeliveredDistalDepthFraction" in self._dataset:
            return self._dataset.DeliveredDistalDepthFraction
        return None

    @DeliveredDistalDepthFraction.setter
    def DeliveredDistalDepthFraction(self, value: Optional[float]):
        if value is None:
            if "DeliveredDistalDepthFraction" in self._dataset:
                del self._dataset.DeliveredDistalDepthFraction
        else:
            self._dataset.DeliveredDistalDepthFraction = value

    @property
    def DeliveredDistalDepth(self) -> Optional[float]:
        if "DeliveredDistalDepth" in self._dataset:
            return self._dataset.DeliveredDistalDepth
        return None

    @DeliveredDistalDepth.setter
    def DeliveredDistalDepth(self, value: Optional[float]):
        if value is None:
            if "DeliveredDistalDepth" in self._dataset:
                del self._dataset.DeliveredDistalDepth
        else:
            self._dataset.DeliveredDistalDepth = value

    @property
    def DeliveredNominalRangeModulationFractions(self) -> Optional[List[float]]:
        if "DeliveredNominalRangeModulationFractions" in self._dataset:
            return self._dataset.DeliveredNominalRangeModulationFractions
        return None

    @DeliveredNominalRangeModulationFractions.setter
    def DeliveredNominalRangeModulationFractions(self, value: Optional[List[float]]):
        if value is None:
            if "DeliveredNominalRangeModulationFractions" in self._dataset:
                del self._dataset.DeliveredNominalRangeModulationFractions
        else:
            self._dataset.DeliveredNominalRangeModulationFractions = value

    @property
    def DeliveredNominalRangeModulatedRegionDepths(self) -> Optional[List[float]]:
        if "DeliveredNominalRangeModulatedRegionDepths" in self._dataset:
            return self._dataset.DeliveredNominalRangeModulatedRegionDepths
        return None

    @DeliveredNominalRangeModulatedRegionDepths.setter
    def DeliveredNominalRangeModulatedRegionDepths(self, value: Optional[List[float]]):
        if value is None:
            if "DeliveredNominalRangeModulatedRegionDepths" in self._dataset:
                del self._dataset.DeliveredNominalRangeModulatedRegionDepths
        else:
            self._dataset.DeliveredNominalRangeModulatedRegionDepths = value

    @property
    def DeliveredReferenceDoseDefinition(self) -> Optional[str]:
        if "DeliveredReferenceDoseDefinition" in self._dataset:
            return self._dataset.DeliveredReferenceDoseDefinition
        return None

    @DeliveredReferenceDoseDefinition.setter
    def DeliveredReferenceDoseDefinition(self, value: Optional[str]):
        if value is None:
            if "DeliveredReferenceDoseDefinition" in self._dataset:
                del self._dataset.DeliveredReferenceDoseDefinition
        else:
            self._dataset.DeliveredReferenceDoseDefinition = value
