from typing import Any, List, Optional

import pydicom

from .meterset_to_dose_mapping_sequence_item import MetersetToDoseMappingSequenceItem


class ExpectedInVivoMeasurementValuesSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._MetersetToDoseMappingSequence: List[MetersetToDoseMappingSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def MetersetToDoseMappingSequence(self) -> Optional[List[MetersetToDoseMappingSequenceItem]]:
        if "MetersetToDoseMappingSequence" in self._dataset:
            if len(self._MetersetToDoseMappingSequence) == len(self._dataset.MetersetToDoseMappingSequence):
                return self._MetersetToDoseMappingSequence
            else:
                return [MetersetToDoseMappingSequenceItem(x) for x in self._dataset.MetersetToDoseMappingSequence]
        return None

    @MetersetToDoseMappingSequence.setter
    def MetersetToDoseMappingSequence(self, value: Optional[List[MetersetToDoseMappingSequenceItem]]):
        if value is None:
            self._MetersetToDoseMappingSequence = []
            if "MetersetToDoseMappingSequence" in self._dataset:
                del self._dataset.MetersetToDoseMappingSequence
        elif not isinstance(value, list) or not all(isinstance(item, MetersetToDoseMappingSequenceItem) for item in value):
            raise ValueError(f"MetersetToDoseMappingSequence must be a list of MetersetToDoseMappingSequenceItem objects")
        else:
            self._MetersetToDoseMappingSequence = value
            if "MetersetToDoseMappingSequence" not in self._dataset:
                self._dataset.MetersetToDoseMappingSequence = pydicom.Sequence()
            self._dataset.MetersetToDoseMappingSequence.clear()
            self._dataset.MetersetToDoseMappingSequence.extend([item.to_dataset() for item in value])

    def add_MetersetToDoseMapping(self, item: MetersetToDoseMappingSequenceItem):
        if not isinstance(item, MetersetToDoseMappingSequenceItem):
            raise ValueError(f"Item must be an instance of MetersetToDoseMappingSequenceItem")
        self._MetersetToDoseMappingSequence.append(item)
        if "MetersetToDoseMappingSequence" not in self._dataset:
            self._dataset.MetersetToDoseMappingSequence = pydicom.Sequence()
        self._dataset.MetersetToDoseMappingSequence.append(item.to_dataset())

    @property
    def ExpectedInVivoMeasurementValueIndex(self) -> Optional[int]:
        if "ExpectedInVivoMeasurementValueIndex" in self._dataset:
            return self._dataset.ExpectedInVivoMeasurementValueIndex
        return None

    @ExpectedInVivoMeasurementValueIndex.setter
    def ExpectedInVivoMeasurementValueIndex(self, value: Optional[int]):
        if value is None:
            if "ExpectedInVivoMeasurementValueIndex" in self._dataset:
                del self._dataset.ExpectedInVivoMeasurementValueIndex
        else:
            self._dataset.ExpectedInVivoMeasurementValueIndex = value

    @property
    def RadiationDoseInVivoMeasurementLabel(self) -> Optional[str]:
        if "RadiationDoseInVivoMeasurementLabel" in self._dataset:
            return self._dataset.RadiationDoseInVivoMeasurementLabel
        return None

    @RadiationDoseInVivoMeasurementLabel.setter
    def RadiationDoseInVivoMeasurementLabel(self, value: Optional[str]):
        if value is None:
            if "RadiationDoseInVivoMeasurementLabel" in self._dataset:
                del self._dataset.RadiationDoseInVivoMeasurementLabel
        else:
            self._dataset.RadiationDoseInVivoMeasurementLabel = value

    @property
    def RadiationDoseCentralAxisDisplacement(self) -> Optional[List[float]]:
        if "RadiationDoseCentralAxisDisplacement" in self._dataset:
            return self._dataset.RadiationDoseCentralAxisDisplacement
        return None

    @RadiationDoseCentralAxisDisplacement.setter
    def RadiationDoseCentralAxisDisplacement(self, value: Optional[List[float]]):
        if value is None:
            if "RadiationDoseCentralAxisDisplacement" in self._dataset:
                del self._dataset.RadiationDoseCentralAxisDisplacement
        else:
            self._dataset.RadiationDoseCentralAxisDisplacement = value

    @property
    def RadiationDoseSourceToSkinDistance(self) -> Optional[float]:
        if "RadiationDoseSourceToSkinDistance" in self._dataset:
            return self._dataset.RadiationDoseSourceToSkinDistance
        return None

    @RadiationDoseSourceToSkinDistance.setter
    def RadiationDoseSourceToSkinDistance(self, value: Optional[float]):
        if value is None:
            if "RadiationDoseSourceToSkinDistance" in self._dataset:
                del self._dataset.RadiationDoseSourceToSkinDistance
        else:
            self._dataset.RadiationDoseSourceToSkinDistance = value

    @property
    def RadiationDoseMeasurementPointCoordinates(self) -> Optional[List[float]]:
        if "RadiationDoseMeasurementPointCoordinates" in self._dataset:
            return self._dataset.RadiationDoseMeasurementPointCoordinates
        return None

    @RadiationDoseMeasurementPointCoordinates.setter
    def RadiationDoseMeasurementPointCoordinates(self, value: Optional[List[float]]):
        if value is None:
            if "RadiationDoseMeasurementPointCoordinates" in self._dataset:
                del self._dataset.RadiationDoseMeasurementPointCoordinates
        else:
            self._dataset.RadiationDoseMeasurementPointCoordinates = value

    @property
    def RadiationDoseSourceToExternalContourDistance(self) -> Optional[float]:
        if "RadiationDoseSourceToExternalContourDistance" in self._dataset:
            return self._dataset.RadiationDoseSourceToExternalContourDistance
        return None

    @RadiationDoseSourceToExternalContourDistance.setter
    def RadiationDoseSourceToExternalContourDistance(self, value: Optional[float]):
        if value is None:
            if "RadiationDoseSourceToExternalContourDistance" in self._dataset:
                del self._dataset.RadiationDoseSourceToExternalContourDistance
        else:
            self._dataset.RadiationDoseSourceToExternalContourDistance = value
