from decimal import Decimal
from typing import Any, List, Optional

import pydicom


class ChannelImpedanceSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ImpedanceValue(self) -> Optional[Decimal]:
        if "ImpedanceValue" in self._dataset:
            return self._dataset.ImpedanceValue
        return None

    @ImpedanceValue.setter
    def ImpedanceValue(self, value: Optional[Decimal]):
        if value is None:
            if "ImpedanceValue" in self._dataset:
                del self._dataset.ImpedanceValue
        else:
            self._dataset.ImpedanceValue = value

    @property
    def ImpedanceMeasurementDateTime(self) -> Optional[str]:
        if "ImpedanceMeasurementDateTime" in self._dataset:
            return self._dataset.ImpedanceMeasurementDateTime
        return None

    @ImpedanceMeasurementDateTime.setter
    def ImpedanceMeasurementDateTime(self, value: Optional[str]):
        if value is None:
            if "ImpedanceMeasurementDateTime" in self._dataset:
                del self._dataset.ImpedanceMeasurementDateTime
        else:
            self._dataset.ImpedanceMeasurementDateTime = value

    @property
    def ImpedanceMeasurementFrequency(self) -> Optional[Decimal]:
        if "ImpedanceMeasurementFrequency" in self._dataset:
            return self._dataset.ImpedanceMeasurementFrequency
        return None

    @ImpedanceMeasurementFrequency.setter
    def ImpedanceMeasurementFrequency(self, value: Optional[Decimal]):
        if value is None:
            if "ImpedanceMeasurementFrequency" in self._dataset:
                del self._dataset.ImpedanceMeasurementFrequency
        else:
            self._dataset.ImpedanceMeasurementFrequency = value

    @property
    def ImpedanceMeasurementCurrentType(self) -> Optional[str]:
        if "ImpedanceMeasurementCurrentType" in self._dataset:
            return self._dataset.ImpedanceMeasurementCurrentType
        return None

    @ImpedanceMeasurementCurrentType.setter
    def ImpedanceMeasurementCurrentType(self, value: Optional[str]):
        if value is None:
            if "ImpedanceMeasurementCurrentType" in self._dataset:
                del self._dataset.ImpedanceMeasurementCurrentType
        else:
            self._dataset.ImpedanceMeasurementCurrentType = value
