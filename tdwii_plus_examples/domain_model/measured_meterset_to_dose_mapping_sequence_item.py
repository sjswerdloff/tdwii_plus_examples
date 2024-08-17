from typing import Any, List, Optional  # noqa

import pydicom

from .code_sequence_item import CodeSequenceItem


class MeasuredMetersetToDoseMappingSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._DoseMeasurementDeviceCodeSequence: List[CodeSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def MeasuredDoseDescription(self) -> Optional[str]:
        if "MeasuredDoseDescription" in self._dataset:
            return self._dataset.MeasuredDoseDescription
        return None

    @MeasuredDoseDescription.setter
    def MeasuredDoseDescription(self, value: Optional[str]):
        if value is None:
            if "MeasuredDoseDescription" in self._dataset:
                del self._dataset.MeasuredDoseDescription
        else:
            self._dataset.MeasuredDoseDescription = value

    @property
    def RadiationDoseValue(self) -> Optional[float]:
        if "RadiationDoseValue" in self._dataset:
            return self._dataset.RadiationDoseValue
        return None

    @RadiationDoseValue.setter
    def RadiationDoseValue(self, value: Optional[float]):
        if value is None:
            if "RadiationDoseValue" in self._dataset:
                del self._dataset.RadiationDoseValue
        else:
            self._dataset.RadiationDoseValue = value

    @property
    def CumulativeMeterset(self) -> Optional[float]:
        if "CumulativeMeterset" in self._dataset:
            return self._dataset.CumulativeMeterset
        return None

    @CumulativeMeterset.setter
    def CumulativeMeterset(self, value: Optional[float]):
        if value is None:
            if "CumulativeMeterset" in self._dataset:
                del self._dataset.CumulativeMeterset
        else:
            self._dataset.CumulativeMeterset = value

    @property
    def ReferencedExpectedInVivoMeasurementValueIndex(self) -> Optional[int]:
        if "ReferencedExpectedInVivoMeasurementValueIndex" in self._dataset:
            return self._dataset.ReferencedExpectedInVivoMeasurementValueIndex
        return None

    @ReferencedExpectedInVivoMeasurementValueIndex.setter
    def ReferencedExpectedInVivoMeasurementValueIndex(self, value: Optional[int]):
        if value is None:
            if "ReferencedExpectedInVivoMeasurementValueIndex" in self._dataset:
                del self._dataset.ReferencedExpectedInVivoMeasurementValueIndex
        else:
            self._dataset.ReferencedExpectedInVivoMeasurementValueIndex = value

    @property
    def DoseMeasurementDeviceCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "DoseMeasurementDeviceCodeSequence" in self._dataset:
            if len(self._DoseMeasurementDeviceCodeSequence) == len(self._dataset.DoseMeasurementDeviceCodeSequence):
                return self._DoseMeasurementDeviceCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.DoseMeasurementDeviceCodeSequence]
        return None

    @DoseMeasurementDeviceCodeSequence.setter
    def DoseMeasurementDeviceCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._DoseMeasurementDeviceCodeSequence = []
            if "DoseMeasurementDeviceCodeSequence" in self._dataset:
                del self._dataset.DoseMeasurementDeviceCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("DoseMeasurementDeviceCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._DoseMeasurementDeviceCodeSequence = value
            if "DoseMeasurementDeviceCodeSequence" not in self._dataset:
                self._dataset.DoseMeasurementDeviceCodeSequence = pydicom.Sequence()
            self._dataset.DoseMeasurementDeviceCodeSequence.clear()
            self._dataset.DoseMeasurementDeviceCodeSequence.extend([item.to_dataset() for item in value])

    def add_DoseMeasurementDeviceCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._DoseMeasurementDeviceCodeSequence.append(item)
        if "DoseMeasurementDeviceCodeSequence" not in self._dataset:
            self._dataset.DoseMeasurementDeviceCodeSequence = pydicom.Sequence()
        self._dataset.DoseMeasurementDeviceCodeSequence.append(item.to_dataset())
