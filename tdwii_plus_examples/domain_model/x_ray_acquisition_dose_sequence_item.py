from decimal import Decimal
from typing import Any, List, Optional  # noqa

import pydicom


class XRayAcquisitionDoseSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def RelativeXRayExposure(self) -> Optional[int]:
        if "RelativeXRayExposure" in self._dataset:
            return self._dataset.RelativeXRayExposure
        return None

    @RelativeXRayExposure.setter
    def RelativeXRayExposure(self, value: Optional[int]):
        if value is None:
            if "RelativeXRayExposure" in self._dataset:
                del self._dataset.RelativeXRayExposure
        else:
            self._dataset.RelativeXRayExposure = value

    @property
    def ExposureTimeInms(self) -> Optional[float]:
        if "ExposureTimeInms" in self._dataset:
            return self._dataset.ExposureTimeInms
        return None

    @ExposureTimeInms.setter
    def ExposureTimeInms(self, value: Optional[float]):
        if value is None:
            if "ExposureTimeInms" in self._dataset:
                del self._dataset.ExposureTimeInms
        else:
            self._dataset.ExposureTimeInms = value

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
    def HalfValueLayer(self) -> Optional[Decimal]:
        if "HalfValueLayer" in self._dataset:
            return self._dataset.HalfValueLayer
        return None

    @HalfValueLayer.setter
    def HalfValueLayer(self, value: Optional[Decimal]):
        if value is None:
            if "HalfValueLayer" in self._dataset:
                del self._dataset.HalfValueLayer
        else:
            self._dataset.HalfValueLayer = value

    @property
    def OrganDose(self) -> Optional[Decimal]:
        if "OrganDose" in self._dataset:
            return self._dataset.OrganDose
        return None

    @OrganDose.setter
    def OrganDose(self, value: Optional[Decimal]):
        if value is None:
            if "OrganDose" in self._dataset:
                del self._dataset.OrganDose
        else:
            self._dataset.OrganDose = value

    @property
    def EntranceDoseInmGy(self) -> Optional[Decimal]:
        if "EntranceDoseInmGy" in self._dataset:
            return self._dataset.EntranceDoseInmGy
        return None

    @EntranceDoseInmGy.setter
    def EntranceDoseInmGy(self, value: Optional[Decimal]):
        if value is None:
            if "EntranceDoseInmGy" in self._dataset:
                del self._dataset.EntranceDoseInmGy
        else:
            self._dataset.EntranceDoseInmGy = value

    @property
    def EntranceDoseDerivation(self) -> Optional[str]:
        if "EntranceDoseDerivation" in self._dataset:
            return self._dataset.EntranceDoseDerivation
        return None

    @EntranceDoseDerivation.setter
    def EntranceDoseDerivation(self, value: Optional[str]):
        if value is None:
            if "EntranceDoseDerivation" in self._dataset:
                del self._dataset.EntranceDoseDerivation
        else:
            self._dataset.EntranceDoseDerivation = value
