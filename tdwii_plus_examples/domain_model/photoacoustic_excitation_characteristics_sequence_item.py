from typing import Any, List, Optional  # noqa

import pydicom


class PhotoacousticExcitationCharacteristicsSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ExcitationSpectralWidth(self) -> Optional[float]:
        if "ExcitationSpectralWidth" in self._dataset:
            return self._dataset.ExcitationSpectralWidth
        return None

    @ExcitationSpectralWidth.setter
    def ExcitationSpectralWidth(self, value: Optional[float]):
        if value is None:
            if "ExcitationSpectralWidth" in self._dataset:
                del self._dataset.ExcitationSpectralWidth
        else:
            self._dataset.ExcitationSpectralWidth = value

    @property
    def ExcitationEnergy(self) -> Optional[float]:
        if "ExcitationEnergy" in self._dataset:
            return self._dataset.ExcitationEnergy
        return None

    @ExcitationEnergy.setter
    def ExcitationEnergy(self, value: Optional[float]):
        if value is None:
            if "ExcitationEnergy" in self._dataset:
                del self._dataset.ExcitationEnergy
        else:
            self._dataset.ExcitationEnergy = value

    @property
    def ExcitationPulseDuration(self) -> Optional[float]:
        if "ExcitationPulseDuration" in self._dataset:
            return self._dataset.ExcitationPulseDuration
        return None

    @ExcitationPulseDuration.setter
    def ExcitationPulseDuration(self, value: Optional[float]):
        if value is None:
            if "ExcitationPulseDuration" in self._dataset:
                del self._dataset.ExcitationPulseDuration
        else:
            self._dataset.ExcitationPulseDuration = value

    @property
    def ExcitationWavelength(self) -> Optional[float]:
        if "ExcitationWavelength" in self._dataset:
            return self._dataset.ExcitationWavelength
        return None

    @ExcitationWavelength.setter
    def ExcitationWavelength(self, value: Optional[float]):
        if value is None:
            if "ExcitationWavelength" in self._dataset:
                del self._dataset.ExcitationWavelength
        else:
            self._dataset.ExcitationWavelength = value
