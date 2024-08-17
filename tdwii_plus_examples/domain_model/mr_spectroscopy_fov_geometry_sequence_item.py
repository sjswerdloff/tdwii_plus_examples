from decimal import Decimal
from typing import Any, List, Optional

import pydicom


class MRSpectroscopyFOVGeometrySequenceItem:
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
    def SpectroscopyAcquisitionPhaseRows(self) -> Optional[int]:
        if "SpectroscopyAcquisitionPhaseRows" in self._dataset:
            return self._dataset.SpectroscopyAcquisitionPhaseRows
        return None

    @SpectroscopyAcquisitionPhaseRows.setter
    def SpectroscopyAcquisitionPhaseRows(self, value: Optional[int]):
        if value is None:
            if "SpectroscopyAcquisitionPhaseRows" in self._dataset:
                del self._dataset.SpectroscopyAcquisitionPhaseRows
        else:
            self._dataset.SpectroscopyAcquisitionPhaseRows = value

    @property
    def SpectroscopyAcquisitionDataColumns(self) -> Optional[int]:
        if "SpectroscopyAcquisitionDataColumns" in self._dataset:
            return self._dataset.SpectroscopyAcquisitionDataColumns
        return None

    @SpectroscopyAcquisitionDataColumns.setter
    def SpectroscopyAcquisitionDataColumns(self, value: Optional[int]):
        if value is None:
            if "SpectroscopyAcquisitionDataColumns" in self._dataset:
                del self._dataset.SpectroscopyAcquisitionDataColumns
        else:
            self._dataset.SpectroscopyAcquisitionDataColumns = value

    @property
    def SpectroscopyAcquisitionOutOfPlanePhaseSteps(self) -> Optional[int]:
        if "SpectroscopyAcquisitionOutOfPlanePhaseSteps" in self._dataset:
            return self._dataset.SpectroscopyAcquisitionOutOfPlanePhaseSteps
        return None

    @SpectroscopyAcquisitionOutOfPlanePhaseSteps.setter
    def SpectroscopyAcquisitionOutOfPlanePhaseSteps(self, value: Optional[int]):
        if value is None:
            if "SpectroscopyAcquisitionOutOfPlanePhaseSteps" in self._dataset:
                del self._dataset.SpectroscopyAcquisitionOutOfPlanePhaseSteps
        else:
            self._dataset.SpectroscopyAcquisitionOutOfPlanePhaseSteps = value

    @property
    def SpectroscopyAcquisitionPhaseColumns(self) -> Optional[int]:
        if "SpectroscopyAcquisitionPhaseColumns" in self._dataset:
            return self._dataset.SpectroscopyAcquisitionPhaseColumns
        return None

    @SpectroscopyAcquisitionPhaseColumns.setter
    def SpectroscopyAcquisitionPhaseColumns(self, value: Optional[int]):
        if value is None:
            if "SpectroscopyAcquisitionPhaseColumns" in self._dataset:
                del self._dataset.SpectroscopyAcquisitionPhaseColumns
        else:
            self._dataset.SpectroscopyAcquisitionPhaseColumns = value
