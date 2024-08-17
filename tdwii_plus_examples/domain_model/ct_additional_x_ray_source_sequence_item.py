from decimal import Decimal
from typing import Any, List, Optional

import pydicom


class CTAdditionalXRaySourceSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def KVP(self) -> Optional[Decimal]:
        if "KVP" in self._dataset:
            return self._dataset.KVP
        return None

    @KVP.setter
    def KVP(self, value: Optional[Decimal]):
        if value is None:
            if "KVP" in self._dataset:
                del self._dataset.KVP
        else:
            self._dataset.KVP = value

    @property
    def DataCollectionDiameter(self) -> Optional[Decimal]:
        if "DataCollectionDiameter" in self._dataset:
            return self._dataset.DataCollectionDiameter
        return None

    @DataCollectionDiameter.setter
    def DataCollectionDiameter(self, value: Optional[Decimal]):
        if value is None:
            if "DataCollectionDiameter" in self._dataset:
                del self._dataset.DataCollectionDiameter
        else:
            self._dataset.DataCollectionDiameter = value

    @property
    def FilterType(self) -> Optional[str]:
        if "FilterType" in self._dataset:
            return self._dataset.FilterType
        return None

    @FilterType.setter
    def FilterType(self, value: Optional[str]):
        if value is None:
            if "FilterType" in self._dataset:
                del self._dataset.FilterType
        else:
            self._dataset.FilterType = value

    @property
    def FocalSpots(self) -> Optional[List[Decimal]]:
        if "FocalSpots" in self._dataset:
            return self._dataset.FocalSpots
        return None

    @FocalSpots.setter
    def FocalSpots(self, value: Optional[List[Decimal]]):
        if value is None:
            if "FocalSpots" in self._dataset:
                del self._dataset.FocalSpots
        else:
            self._dataset.FocalSpots = value

    @property
    def FilterMaterial(self) -> Optional[List[str]]:
        if "FilterMaterial" in self._dataset:
            return self._dataset.FilterMaterial
        return None

    @FilterMaterial.setter
    def FilterMaterial(self, value: Optional[List[str]]):
        if value is None:
            if "FilterMaterial" in self._dataset:
                del self._dataset.FilterMaterial
        else:
            self._dataset.FilterMaterial = value

    @property
    def XRayTubeCurrentInmA(self) -> Optional[float]:
        if "XRayTubeCurrentInmA" in self._dataset:
            return self._dataset.XRayTubeCurrentInmA
        return None

    @XRayTubeCurrentInmA.setter
    def XRayTubeCurrentInmA(self, value: Optional[float]):
        if value is None:
            if "XRayTubeCurrentInmA" in self._dataset:
                del self._dataset.XRayTubeCurrentInmA
        else:
            self._dataset.XRayTubeCurrentInmA = value

    @property
    def ExposureInmAs(self) -> Optional[float]:
        if "ExposureInmAs" in self._dataset:
            return self._dataset.ExposureInmAs
        return None

    @ExposureInmAs.setter
    def ExposureInmAs(self, value: Optional[float]):
        if value is None:
            if "ExposureInmAs" in self._dataset:
                del self._dataset.ExposureInmAs
        else:
            self._dataset.ExposureInmAs = value

    @property
    def EnergyWeightingFactor(self) -> Optional[float]:
        if "EnergyWeightingFactor" in self._dataset:
            return self._dataset.EnergyWeightingFactor
        return None

    @EnergyWeightingFactor.setter
    def EnergyWeightingFactor(self, value: Optional[float]):
        if value is None:
            if "EnergyWeightingFactor" in self._dataset:
                del self._dataset.EnergyWeightingFactor
        else:
            self._dataset.EnergyWeightingFactor = value
