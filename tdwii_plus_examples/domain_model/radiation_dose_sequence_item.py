from typing import Any, List, Optional  # noqa

import pydicom

from .expected_in_vivo_measurement_values_sequence_item import (
    ExpectedInVivoMeasurementValuesSequenceItem,
)
from .radiation_dose_values_parameters_sequence_item import (
    RadiationDoseValuesParametersSequenceItem,
)
from .referenced_rt_radiation_sequence_item import ReferencedRTRadiationSequenceItem


class RadiationDoseSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._RadiationDoseValuesParametersSequence: List[RadiationDoseValuesParametersSequenceItem] = []
        self._ExpectedInVivoMeasurementValuesSequence: List[ExpectedInVivoMeasurementValuesSequenceItem] = []
        self._ReferencedRTRadiationSequence: List[ReferencedRTRadiationSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def RadiationDoseValuesParametersSequence(self) -> Optional[List[RadiationDoseValuesParametersSequenceItem]]:
        if "RadiationDoseValuesParametersSequence" in self._dataset:
            if len(self._RadiationDoseValuesParametersSequence) == len(self._dataset.RadiationDoseValuesParametersSequence):
                return self._RadiationDoseValuesParametersSequence
            else:
                return [
                    RadiationDoseValuesParametersSequenceItem(x) for x in self._dataset.RadiationDoseValuesParametersSequence
                ]
        return None

    @RadiationDoseValuesParametersSequence.setter
    def RadiationDoseValuesParametersSequence(self, value: Optional[List[RadiationDoseValuesParametersSequenceItem]]):
        if value is None:
            self._RadiationDoseValuesParametersSequence = []
            if "RadiationDoseValuesParametersSequence" in self._dataset:
                del self._dataset.RadiationDoseValuesParametersSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, RadiationDoseValuesParametersSequenceItem) for item in value
        ):
            raise ValueError(
                "RadiationDoseValuesParametersSequence must be a list of RadiationDoseValuesParametersSequenceItem objects"
            )
        else:
            self._RadiationDoseValuesParametersSequence = value
            if "RadiationDoseValuesParametersSequence" not in self._dataset:
                self._dataset.RadiationDoseValuesParametersSequence = pydicom.Sequence()
            self._dataset.RadiationDoseValuesParametersSequence.clear()
            self._dataset.RadiationDoseValuesParametersSequence.extend([item.to_dataset() for item in value])

    def add_RadiationDoseValuesParameters(self, item: RadiationDoseValuesParametersSequenceItem):
        if not isinstance(item, RadiationDoseValuesParametersSequenceItem):
            raise ValueError("Item must be an instance of RadiationDoseValuesParametersSequenceItem")
        self._RadiationDoseValuesParametersSequence.append(item)
        if "RadiationDoseValuesParametersSequence" not in self._dataset:
            self._dataset.RadiationDoseValuesParametersSequence = pydicom.Sequence()
        self._dataset.RadiationDoseValuesParametersSequence.append(item.to_dataset())

    @property
    def ExpectedInVivoMeasurementValuesSequence(self) -> Optional[List[ExpectedInVivoMeasurementValuesSequenceItem]]:
        if "ExpectedInVivoMeasurementValuesSequence" in self._dataset:
            if len(self._ExpectedInVivoMeasurementValuesSequence) == len(
                self._dataset.ExpectedInVivoMeasurementValuesSequence
            ):
                return self._ExpectedInVivoMeasurementValuesSequence
            else:
                return [
                    ExpectedInVivoMeasurementValuesSequenceItem(x)
                    for x in self._dataset.ExpectedInVivoMeasurementValuesSequence
                ]
        return None

    @ExpectedInVivoMeasurementValuesSequence.setter
    def ExpectedInVivoMeasurementValuesSequence(self, value: Optional[List[ExpectedInVivoMeasurementValuesSequenceItem]]):
        if value is None:
            self._ExpectedInVivoMeasurementValuesSequence = []
            if "ExpectedInVivoMeasurementValuesSequence" in self._dataset:
                del self._dataset.ExpectedInVivoMeasurementValuesSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, ExpectedInVivoMeasurementValuesSequenceItem) for item in value
        ):
            raise ValueError(
                "ExpectedInVivoMeasurementValuesSequence must be a list of ExpectedInVivoMeasurementValuesSequenceItem objects"
            )
        else:
            self._ExpectedInVivoMeasurementValuesSequence = value
            if "ExpectedInVivoMeasurementValuesSequence" not in self._dataset:
                self._dataset.ExpectedInVivoMeasurementValuesSequence = pydicom.Sequence()
            self._dataset.ExpectedInVivoMeasurementValuesSequence.clear()
            self._dataset.ExpectedInVivoMeasurementValuesSequence.extend([item.to_dataset() for item in value])

    def add_ExpectedInVivoMeasurementValues(self, item: ExpectedInVivoMeasurementValuesSequenceItem):
        if not isinstance(item, ExpectedInVivoMeasurementValuesSequenceItem):
            raise ValueError("Item must be an instance of ExpectedInVivoMeasurementValuesSequenceItem")
        self._ExpectedInVivoMeasurementValuesSequence.append(item)
        if "ExpectedInVivoMeasurementValuesSequence" not in self._dataset:
            self._dataset.ExpectedInVivoMeasurementValuesSequence = pydicom.Sequence()
        self._dataset.ExpectedInVivoMeasurementValuesSequence.append(item.to_dataset())

    @property
    def ReferencedRTRadiationSequence(self) -> Optional[List[ReferencedRTRadiationSequenceItem]]:
        if "ReferencedRTRadiationSequence" in self._dataset:
            if len(self._ReferencedRTRadiationSequence) == len(self._dataset.ReferencedRTRadiationSequence):
                return self._ReferencedRTRadiationSequence
            else:
                return [ReferencedRTRadiationSequenceItem(x) for x in self._dataset.ReferencedRTRadiationSequence]
        return None

    @ReferencedRTRadiationSequence.setter
    def ReferencedRTRadiationSequence(self, value: Optional[List[ReferencedRTRadiationSequenceItem]]):
        if value is None:
            self._ReferencedRTRadiationSequence = []
            if "ReferencedRTRadiationSequence" in self._dataset:
                del self._dataset.ReferencedRTRadiationSequence
        elif not isinstance(value, list) or not all(isinstance(item, ReferencedRTRadiationSequenceItem) for item in value):
            raise ValueError("ReferencedRTRadiationSequence must be a list of ReferencedRTRadiationSequenceItem objects")
        else:
            self._ReferencedRTRadiationSequence = value
            if "ReferencedRTRadiationSequence" not in self._dataset:
                self._dataset.ReferencedRTRadiationSequence = pydicom.Sequence()
            self._dataset.ReferencedRTRadiationSequence.clear()
            self._dataset.ReferencedRTRadiationSequence.extend([item.to_dataset() for item in value])

    def add_ReferencedRTRadiation(self, item: ReferencedRTRadiationSequenceItem):
        if not isinstance(item, ReferencedRTRadiationSequenceItem):
            raise ValueError("Item must be an instance of ReferencedRTRadiationSequenceItem")
        self._ReferencedRTRadiationSequence.append(item)
        if "ReferencedRTRadiationSequence" not in self._dataset:
            self._dataset.ReferencedRTRadiationSequence = pydicom.Sequence()
        self._dataset.ReferencedRTRadiationSequence.append(item.to_dataset())
