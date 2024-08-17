from decimal import Decimal
from typing import Any, List, Optional

import pydicom


class MRFOVGeometrySequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def PercentSampling(self) -> Optional[Decimal]:
        if "PercentSampling" in self._dataset:
            return self._dataset.PercentSampling
        return None

    @PercentSampling.setter
    def PercentSampling(self, value: Optional[Decimal]):
        if value is None:
            if "PercentSampling" in self._dataset:
                del self._dataset.PercentSampling
        else:
            self._dataset.PercentSampling = value

    @property
    def PercentPhaseFieldOfView(self) -> Optional[Decimal]:
        if "PercentPhaseFieldOfView" in self._dataset:
            return self._dataset.PercentPhaseFieldOfView
        return None

    @PercentPhaseFieldOfView.setter
    def PercentPhaseFieldOfView(self, value: Optional[Decimal]):
        if value is None:
            if "PercentPhaseFieldOfView" in self._dataset:
                del self._dataset.PercentPhaseFieldOfView
        else:
            self._dataset.PercentPhaseFieldOfView = value

    @property
    def InPlanePhaseEncodingDirection(self) -> Optional[str]:
        if "InPlanePhaseEncodingDirection" in self._dataset:
            return self._dataset.InPlanePhaseEncodingDirection
        return None

    @InPlanePhaseEncodingDirection.setter
    def InPlanePhaseEncodingDirection(self, value: Optional[str]):
        if value is None:
            if "InPlanePhaseEncodingDirection" in self._dataset:
                del self._dataset.InPlanePhaseEncodingDirection
        else:
            self._dataset.InPlanePhaseEncodingDirection = value

    @property
    def MRAcquisitionFrequencyEncodingSteps(self) -> Optional[int]:
        if "MRAcquisitionFrequencyEncodingSteps" in self._dataset:
            return self._dataset.MRAcquisitionFrequencyEncodingSteps
        return None

    @MRAcquisitionFrequencyEncodingSteps.setter
    def MRAcquisitionFrequencyEncodingSteps(self, value: Optional[int]):
        if value is None:
            if "MRAcquisitionFrequencyEncodingSteps" in self._dataset:
                del self._dataset.MRAcquisitionFrequencyEncodingSteps
        else:
            self._dataset.MRAcquisitionFrequencyEncodingSteps = value

    @property
    def MRAcquisitionPhaseEncodingStepsInPlane(self) -> Optional[int]:
        if "MRAcquisitionPhaseEncodingStepsInPlane" in self._dataset:
            return self._dataset.MRAcquisitionPhaseEncodingStepsInPlane
        return None

    @MRAcquisitionPhaseEncodingStepsInPlane.setter
    def MRAcquisitionPhaseEncodingStepsInPlane(self, value: Optional[int]):
        if value is None:
            if "MRAcquisitionPhaseEncodingStepsInPlane" in self._dataset:
                del self._dataset.MRAcquisitionPhaseEncodingStepsInPlane
        else:
            self._dataset.MRAcquisitionPhaseEncodingStepsInPlane = value

    @property
    def MRAcquisitionPhaseEncodingStepsOutOfPlane(self) -> Optional[int]:
        if "MRAcquisitionPhaseEncodingStepsOutOfPlane" in self._dataset:
            return self._dataset.MRAcquisitionPhaseEncodingStepsOutOfPlane
        return None

    @MRAcquisitionPhaseEncodingStepsOutOfPlane.setter
    def MRAcquisitionPhaseEncodingStepsOutOfPlane(self, value: Optional[int]):
        if value is None:
            if "MRAcquisitionPhaseEncodingStepsOutOfPlane" in self._dataset:
                del self._dataset.MRAcquisitionPhaseEncodingStepsOutOfPlane
        else:
            self._dataset.MRAcquisitionPhaseEncodingStepsOutOfPlane = value
