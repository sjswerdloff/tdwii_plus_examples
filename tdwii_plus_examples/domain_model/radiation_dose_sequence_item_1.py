from typing import Any, List, Optional  # noqa

import pydicom

from .measured_meterset_to_dose_mapping_sequence_item import (
    MeasuredMetersetToDoseMappingSequenceItem,
)
from .radiation_dose_values_parameters_sequence_item import (
    RadiationDoseValuesParametersSequenceItem,
)
from .referenced_rt_radiation_record_sequence_item import (
    ReferencedRTRadiationRecordSequenceItem,
)


class RadiationDoseSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._RadiationDoseValuesParametersSequence: List[RadiationDoseValuesParametersSequenceItem] = []
        self._ReferencedRTRadiationRecordSequence: List[ReferencedRTRadiationRecordSequenceItem] = []
        self._MeasuredMetersetToDoseMappingSequence: List[MeasuredMetersetToDoseMappingSequenceItem] = []

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
    def ReferencedRTRadiationRecordSequence(self) -> Optional[List[ReferencedRTRadiationRecordSequenceItem]]:
        if "ReferencedRTRadiationRecordSequence" in self._dataset:
            if len(self._ReferencedRTRadiationRecordSequence) == len(self._dataset.ReferencedRTRadiationRecordSequence):
                return self._ReferencedRTRadiationRecordSequence
            else:
                return [ReferencedRTRadiationRecordSequenceItem(x) for x in self._dataset.ReferencedRTRadiationRecordSequence]
        return None

    @ReferencedRTRadiationRecordSequence.setter
    def ReferencedRTRadiationRecordSequence(self, value: Optional[List[ReferencedRTRadiationRecordSequenceItem]]):
        if value is None:
            self._ReferencedRTRadiationRecordSequence = []
            if "ReferencedRTRadiationRecordSequence" in self._dataset:
                del self._dataset.ReferencedRTRadiationRecordSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, ReferencedRTRadiationRecordSequenceItem) for item in value
        ):
            raise ValueError(
                "ReferencedRTRadiationRecordSequence must be a list of ReferencedRTRadiationRecordSequenceItem objects"
            )
        else:
            self._ReferencedRTRadiationRecordSequence = value
            if "ReferencedRTRadiationRecordSequence" not in self._dataset:
                self._dataset.ReferencedRTRadiationRecordSequence = pydicom.Sequence()
            self._dataset.ReferencedRTRadiationRecordSequence.clear()
            self._dataset.ReferencedRTRadiationRecordSequence.extend([item.to_dataset() for item in value])

    def add_ReferencedRTRadiationRecord(self, item: ReferencedRTRadiationRecordSequenceItem):
        if not isinstance(item, ReferencedRTRadiationRecordSequenceItem):
            raise ValueError("Item must be an instance of ReferencedRTRadiationRecordSequenceItem")
        self._ReferencedRTRadiationRecordSequence.append(item)
        if "ReferencedRTRadiationRecordSequence" not in self._dataset:
            self._dataset.ReferencedRTRadiationRecordSequence = pydicom.Sequence()
        self._dataset.ReferencedRTRadiationRecordSequence.append(item.to_dataset())

    @property
    def MeasuredMetersetToDoseMappingSequence(self) -> Optional[List[MeasuredMetersetToDoseMappingSequenceItem]]:
        if "MeasuredMetersetToDoseMappingSequence" in self._dataset:
            if len(self._MeasuredMetersetToDoseMappingSequence) == len(self._dataset.MeasuredMetersetToDoseMappingSequence):
                return self._MeasuredMetersetToDoseMappingSequence
            else:
                return [
                    MeasuredMetersetToDoseMappingSequenceItem(x) for x in self._dataset.MeasuredMetersetToDoseMappingSequence
                ]
        return None

    @MeasuredMetersetToDoseMappingSequence.setter
    def MeasuredMetersetToDoseMappingSequence(self, value: Optional[List[MeasuredMetersetToDoseMappingSequenceItem]]):
        if value is None:
            self._MeasuredMetersetToDoseMappingSequence = []
            if "MeasuredMetersetToDoseMappingSequence" in self._dataset:
                del self._dataset.MeasuredMetersetToDoseMappingSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, MeasuredMetersetToDoseMappingSequenceItem) for item in value
        ):
            raise ValueError(
                "MeasuredMetersetToDoseMappingSequence must be a list of MeasuredMetersetToDoseMappingSequenceItem objects"
            )
        else:
            self._MeasuredMetersetToDoseMappingSequence = value
            if "MeasuredMetersetToDoseMappingSequence" not in self._dataset:
                self._dataset.MeasuredMetersetToDoseMappingSequence = pydicom.Sequence()
            self._dataset.MeasuredMetersetToDoseMappingSequence.clear()
            self._dataset.MeasuredMetersetToDoseMappingSequence.extend([item.to_dataset() for item in value])

    def add_MeasuredMetersetToDoseMapping(self, item: MeasuredMetersetToDoseMappingSequenceItem):
        if not isinstance(item, MeasuredMetersetToDoseMappingSequenceItem):
            raise ValueError("Item must be an instance of MeasuredMetersetToDoseMappingSequenceItem")
        self._MeasuredMetersetToDoseMappingSequence.append(item)
        if "MeasuredMetersetToDoseMappingSequence" not in self._dataset:
            self._dataset.MeasuredMetersetToDoseMappingSequence = pydicom.Sequence()
        self._dataset.MeasuredMetersetToDoseMappingSequence.append(item.to_dataset())
