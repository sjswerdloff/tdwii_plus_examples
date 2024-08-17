from decimal import Decimal
from typing import Any, List, Optional  # noqa

import pydicom


class MaterialAttenuationSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def PhotonEnergy(self) -> Optional[Decimal]:
        if "PhotonEnergy" in self._dataset:
            return self._dataset.PhotonEnergy
        return None

    @PhotonEnergy.setter
    def PhotonEnergy(self, value: Optional[Decimal]):
        if value is None:
            if "PhotonEnergy" in self._dataset:
                del self._dataset.PhotonEnergy
        else:
            self._dataset.PhotonEnergy = value

    @property
    def XRayMassAttenuationCoefficient(self) -> Optional[Decimal]:
        if "XRayMassAttenuationCoefficient" in self._dataset:
            return self._dataset.XRayMassAttenuationCoefficient
        return None

    @XRayMassAttenuationCoefficient.setter
    def XRayMassAttenuationCoefficient(self, value: Optional[Decimal]):
        if value is None:
            if "XRayMassAttenuationCoefficient" in self._dataset:
                del self._dataset.XRayMassAttenuationCoefficient
        else:
            self._dataset.XRayMassAttenuationCoefficient = value
