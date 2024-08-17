from decimal import Decimal
from typing import Any, List, Optional

import pydicom


class BeamDoseVerificationControlPointSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def BeamDosePointDepth(self) -> Optional[float]:
        if "BeamDosePointDepth" in self._dataset:
            return self._dataset.BeamDosePointDepth
        return None

    @BeamDosePointDepth.setter
    def BeamDosePointDepth(self, value: Optional[float]):
        if value is None:
            if "BeamDosePointDepth" in self._dataset:
                del self._dataset.BeamDosePointDepth
        else:
            self._dataset.BeamDosePointDepth = value

    @property
    def BeamDosePointEquivalentDepth(self) -> Optional[float]:
        if "BeamDosePointEquivalentDepth" in self._dataset:
            return self._dataset.BeamDosePointEquivalentDepth
        return None

    @BeamDosePointEquivalentDepth.setter
    def BeamDosePointEquivalentDepth(self, value: Optional[float]):
        if value is None:
            if "BeamDosePointEquivalentDepth" in self._dataset:
                del self._dataset.BeamDosePointEquivalentDepth
        else:
            self._dataset.BeamDosePointEquivalentDepth = value

    @property
    def BeamDosePointSSD(self) -> Optional[float]:
        if "BeamDosePointSSD" in self._dataset:
            return self._dataset.BeamDosePointSSD
        return None

    @BeamDosePointSSD.setter
    def BeamDosePointSSD(self, value: Optional[float]):
        if value is None:
            if "BeamDosePointSSD" in self._dataset:
                del self._dataset.BeamDosePointSSD
        else:
            self._dataset.BeamDosePointSSD = value

    @property
    def BeamDosePointSourceToExternalContourDistance(self) -> Optional[Decimal]:
        if "BeamDosePointSourceToExternalContourDistance" in self._dataset:
            return self._dataset.BeamDosePointSourceToExternalContourDistance
        return None

    @BeamDosePointSourceToExternalContourDistance.setter
    def BeamDosePointSourceToExternalContourDistance(self, value: Optional[Decimal]):
        if value is None:
            if "BeamDosePointSourceToExternalContourDistance" in self._dataset:
                del self._dataset.BeamDosePointSourceToExternalContourDistance
        else:
            self._dataset.BeamDosePointSourceToExternalContourDistance = value

    @property
    def CumulativeMetersetWeight(self) -> Optional[Decimal]:
        if "CumulativeMetersetWeight" in self._dataset:
            return self._dataset.CumulativeMetersetWeight
        return None

    @CumulativeMetersetWeight.setter
    def CumulativeMetersetWeight(self, value: Optional[Decimal]):
        if value is None:
            if "CumulativeMetersetWeight" in self._dataset:
                del self._dataset.CumulativeMetersetWeight
        else:
            self._dataset.CumulativeMetersetWeight = value

    @property
    def ReferencedControlPointIndex(self) -> Optional[int]:
        if "ReferencedControlPointIndex" in self._dataset:
            return self._dataset.ReferencedControlPointIndex
        return None

    @ReferencedControlPointIndex.setter
    def ReferencedControlPointIndex(self, value: Optional[int]):
        if value is None:
            if "ReferencedControlPointIndex" in self._dataset:
                del self._dataset.ReferencedControlPointIndex
        else:
            self._dataset.ReferencedControlPointIndex = value
