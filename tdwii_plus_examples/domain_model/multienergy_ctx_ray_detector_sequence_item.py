from decimal import Decimal
from typing import Any, List, Optional  # noqa

import pydicom


class MultienergyCTXRayDetectorSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def EffectiveBinEnergy(self) -> Optional[Decimal]:
        if "EffectiveBinEnergy" in self._dataset:
            return self._dataset.EffectiveBinEnergy
        return None

    @EffectiveBinEnergy.setter
    def EffectiveBinEnergy(self, value: Optional[Decimal]):
        if value is None:
            if "EffectiveBinEnergy" in self._dataset:
                del self._dataset.EffectiveBinEnergy
        else:
            self._dataset.EffectiveBinEnergy = value

    @property
    def XRayDetectorIndex(self) -> Optional[int]:
        if "XRayDetectorIndex" in self._dataset:
            return self._dataset.XRayDetectorIndex
        return None

    @XRayDetectorIndex.setter
    def XRayDetectorIndex(self, value: Optional[int]):
        if value is None:
            if "XRayDetectorIndex" in self._dataset:
                del self._dataset.XRayDetectorIndex
        else:
            self._dataset.XRayDetectorIndex = value

    @property
    def XRayDetectorID(self) -> Optional[str]:
        if "XRayDetectorID" in self._dataset:
            return self._dataset.XRayDetectorID
        return None

    @XRayDetectorID.setter
    def XRayDetectorID(self, value: Optional[str]):
        if value is None:
            if "XRayDetectorID" in self._dataset:
                del self._dataset.XRayDetectorID
        else:
            self._dataset.XRayDetectorID = value

    @property
    def MultienergyDetectorType(self) -> Optional[str]:
        if "MultienergyDetectorType" in self._dataset:
            return self._dataset.MultienergyDetectorType
        return None

    @MultienergyDetectorType.setter
    def MultienergyDetectorType(self, value: Optional[str]):
        if value is None:
            if "MultienergyDetectorType" in self._dataset:
                del self._dataset.MultienergyDetectorType
        else:
            self._dataset.MultienergyDetectorType = value

    @property
    def XRayDetectorLabel(self) -> Optional[str]:
        if "XRayDetectorLabel" in self._dataset:
            return self._dataset.XRayDetectorLabel
        return None

    @XRayDetectorLabel.setter
    def XRayDetectorLabel(self, value: Optional[str]):
        if value is None:
            if "XRayDetectorLabel" in self._dataset:
                del self._dataset.XRayDetectorLabel
        else:
            self._dataset.XRayDetectorLabel = value

    @property
    def NominalMaxEnergy(self) -> Optional[Decimal]:
        if "NominalMaxEnergy" in self._dataset:
            return self._dataset.NominalMaxEnergy
        return None

    @NominalMaxEnergy.setter
    def NominalMaxEnergy(self, value: Optional[Decimal]):
        if value is None:
            if "NominalMaxEnergy" in self._dataset:
                del self._dataset.NominalMaxEnergy
        else:
            self._dataset.NominalMaxEnergy = value

    @property
    def NominalMinEnergy(self) -> Optional[Decimal]:
        if "NominalMinEnergy" in self._dataset:
            return self._dataset.NominalMinEnergy
        return None

    @NominalMinEnergy.setter
    def NominalMinEnergy(self, value: Optional[Decimal]):
        if value is None:
            if "NominalMinEnergy" in self._dataset:
                del self._dataset.NominalMinEnergy
        else:
            self._dataset.NominalMinEnergy = value
