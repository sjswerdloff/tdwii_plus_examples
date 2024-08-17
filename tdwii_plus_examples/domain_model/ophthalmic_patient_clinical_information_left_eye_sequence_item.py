from typing import Any, List, Optional  # noqa

import pydicom

from .refractive_parameters_used_on_patient_sequence_item import (
    RefractiveParametersUsedOnPatientSequenceItem,
)
from .visual_acuity_measurement_sequence_item import VisualAcuityMeasurementSequenceItem


class OphthalmicPatientClinicalInformationLeftEyeSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._VisualAcuityMeasurementSequence: List[VisualAcuityMeasurementSequenceItem] = []
        self._RefractiveParametersUsedOnPatientSequence: List[RefractiveParametersUsedOnPatientSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def IntraOcularPressure(self) -> Optional[float]:
        if "IntraOcularPressure" in self._dataset:
            return self._dataset.IntraOcularPressure
        return None

    @IntraOcularPressure.setter
    def IntraOcularPressure(self, value: Optional[float]):
        if value is None:
            if "IntraOcularPressure" in self._dataset:
                del self._dataset.IntraOcularPressure
        else:
            self._dataset.IntraOcularPressure = value

    @property
    def PupilDilated(self) -> Optional[str]:
        if "PupilDilated" in self._dataset:
            return self._dataset.PupilDilated
        return None

    @PupilDilated.setter
    def PupilDilated(self, value: Optional[str]):
        if value is None:
            if "PupilDilated" in self._dataset:
                del self._dataset.PupilDilated
        else:
            self._dataset.PupilDilated = value

    @property
    def VisualAcuityMeasurementSequence(self) -> Optional[List[VisualAcuityMeasurementSequenceItem]]:
        if "VisualAcuityMeasurementSequence" in self._dataset:
            if len(self._VisualAcuityMeasurementSequence) == len(self._dataset.VisualAcuityMeasurementSequence):
                return self._VisualAcuityMeasurementSequence
            else:
                return [VisualAcuityMeasurementSequenceItem(x) for x in self._dataset.VisualAcuityMeasurementSequence]
        return None

    @VisualAcuityMeasurementSequence.setter
    def VisualAcuityMeasurementSequence(self, value: Optional[List[VisualAcuityMeasurementSequenceItem]]):
        if value is None:
            self._VisualAcuityMeasurementSequence = []
            if "VisualAcuityMeasurementSequence" in self._dataset:
                del self._dataset.VisualAcuityMeasurementSequence
        elif not isinstance(value, list) or not all(isinstance(item, VisualAcuityMeasurementSequenceItem) for item in value):
            raise ValueError("VisualAcuityMeasurementSequence must be a list of VisualAcuityMeasurementSequenceItem objects")
        else:
            self._VisualAcuityMeasurementSequence = value
            if "VisualAcuityMeasurementSequence" not in self._dataset:
                self._dataset.VisualAcuityMeasurementSequence = pydicom.Sequence()
            self._dataset.VisualAcuityMeasurementSequence.clear()
            self._dataset.VisualAcuityMeasurementSequence.extend([item.to_dataset() for item in value])

    def add_VisualAcuityMeasurement(self, item: VisualAcuityMeasurementSequenceItem):
        if not isinstance(item, VisualAcuityMeasurementSequenceItem):
            raise ValueError("Item must be an instance of VisualAcuityMeasurementSequenceItem")
        self._VisualAcuityMeasurementSequence.append(item)
        if "VisualAcuityMeasurementSequence" not in self._dataset:
            self._dataset.VisualAcuityMeasurementSequence = pydicom.Sequence()
        self._dataset.VisualAcuityMeasurementSequence.append(item.to_dataset())

    @property
    def RefractiveParametersUsedOnPatientSequence(self) -> Optional[List[RefractiveParametersUsedOnPatientSequenceItem]]:
        if "RefractiveParametersUsedOnPatientSequence" in self._dataset:
            if len(self._RefractiveParametersUsedOnPatientSequence) == len(
                self._dataset.RefractiveParametersUsedOnPatientSequence
            ):
                return self._RefractiveParametersUsedOnPatientSequence
            else:
                return [
                    RefractiveParametersUsedOnPatientSequenceItem(x)
                    for x in self._dataset.RefractiveParametersUsedOnPatientSequence
                ]
        return None

    @RefractiveParametersUsedOnPatientSequence.setter
    def RefractiveParametersUsedOnPatientSequence(self, value: Optional[List[RefractiveParametersUsedOnPatientSequenceItem]]):
        if value is None:
            self._RefractiveParametersUsedOnPatientSequence = []
            if "RefractiveParametersUsedOnPatientSequence" in self._dataset:
                del self._dataset.RefractiveParametersUsedOnPatientSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, RefractiveParametersUsedOnPatientSequenceItem) for item in value
        ):
            raise ValueError(
                "RefractiveParametersUsedOnPatientSequence must be a list of RefractiveParametersUsedOnPatientSequenceItem"
                " objects"
            )
        else:
            self._RefractiveParametersUsedOnPatientSequence = value
            if "RefractiveParametersUsedOnPatientSequence" not in self._dataset:
                self._dataset.RefractiveParametersUsedOnPatientSequence = pydicom.Sequence()
            self._dataset.RefractiveParametersUsedOnPatientSequence.clear()
            self._dataset.RefractiveParametersUsedOnPatientSequence.extend([item.to_dataset() for item in value])

    def add_RefractiveParametersUsedOnPatient(self, item: RefractiveParametersUsedOnPatientSequenceItem):
        if not isinstance(item, RefractiveParametersUsedOnPatientSequenceItem):
            raise ValueError("Item must be an instance of RefractiveParametersUsedOnPatientSequenceItem")
        self._RefractiveParametersUsedOnPatientSequence.append(item)
        if "RefractiveParametersUsedOnPatientSequence" not in self._dataset:
            self._dataset.RefractiveParametersUsedOnPatientSequence = pydicom.Sequence()
        self._dataset.RefractiveParametersUsedOnPatientSequence.append(item.to_dataset())

    @property
    def PupilSize(self) -> Optional[float]:
        if "PupilSize" in self._dataset:
            return self._dataset.PupilSize
        return None

    @PupilSize.setter
    def PupilSize(self, value: Optional[float]):
        if value is None:
            if "PupilSize" in self._dataset:
                del self._dataset.PupilSize
        else:
            self._dataset.PupilSize = value
