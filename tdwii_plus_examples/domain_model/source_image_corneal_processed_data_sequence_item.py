from typing import Any, List, Optional

import pydicom


class SourceImageCornealProcessedDataSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def CornealPointLocation(self) -> Optional[List[float]]:
        if "CornealPointLocation" in self._dataset:
            return self._dataset.CornealPointLocation
        return None

    @CornealPointLocation.setter
    def CornealPointLocation(self, value: Optional[List[float]]):
        if value is None:
            if "CornealPointLocation" in self._dataset:
                del self._dataset.CornealPointLocation
        else:
            self._dataset.CornealPointLocation = value

    @property
    def CornealPointEstimated(self) -> Optional[str]:
        if "CornealPointEstimated" in self._dataset:
            return self._dataset.CornealPointEstimated
        return None

    @CornealPointEstimated.setter
    def CornealPointEstimated(self, value: Optional[str]):
        if value is None:
            if "CornealPointEstimated" in self._dataset:
                del self._dataset.CornealPointEstimated
        else:
            self._dataset.CornealPointEstimated = value

    @property
    def AxialPower(self) -> Optional[float]:
        if "AxialPower" in self._dataset:
            return self._dataset.AxialPower
        return None

    @AxialPower.setter
    def AxialPower(self, value: Optional[float]):
        if value is None:
            if "AxialPower" in self._dataset:
                del self._dataset.AxialPower
        else:
            self._dataset.AxialPower = value

    @property
    def TangentialPower(self) -> Optional[float]:
        if "TangentialPower" in self._dataset:
            return self._dataset.TangentialPower
        return None

    @TangentialPower.setter
    def TangentialPower(self, value: Optional[float]):
        if value is None:
            if "TangentialPower" in self._dataset:
                del self._dataset.TangentialPower
        else:
            self._dataset.TangentialPower = value

    @property
    def RefractivePower(self) -> Optional[float]:
        if "RefractivePower" in self._dataset:
            return self._dataset.RefractivePower
        return None

    @RefractivePower.setter
    def RefractivePower(self, value: Optional[float]):
        if value is None:
            if "RefractivePower" in self._dataset:
                del self._dataset.RefractivePower
        else:
            self._dataset.RefractivePower = value

    @property
    def RelativeElevation(self) -> Optional[float]:
        if "RelativeElevation" in self._dataset:
            return self._dataset.RelativeElevation
        return None

    @RelativeElevation.setter
    def RelativeElevation(self, value: Optional[float]):
        if value is None:
            if "RelativeElevation" in self._dataset:
                del self._dataset.RelativeElevation
        else:
            self._dataset.RelativeElevation = value

    @property
    def CornealWavefront(self) -> Optional[float]:
        if "CornealWavefront" in self._dataset:
            return self._dataset.CornealWavefront
        return None

    @CornealWavefront.setter
    def CornealWavefront(self, value: Optional[float]):
        if value is None:
            if "CornealWavefront" in self._dataset:
                del self._dataset.CornealWavefront
        else:
            self._dataset.CornealWavefront = value
