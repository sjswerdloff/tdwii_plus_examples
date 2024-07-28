from typing import List, Optional, Union

from pydicom.dataset import Dataset

from .treatmentmachine import TreatmentMachine
from .treatmentsessionionbeam import TreatmentSessionIonBeam


class RTIonBeamsTreatmentIOD:
    def __init__(self):
        self._dataset = Dataset()

    # SOP Common Module
    @property
    def sop_class_uid(self) -> str:
        return self._dataset.SOPClassUID

    @sop_class_uid.setter
    def sop_class_uid(self, value: str):
        self._dataset.SOPClassUID = value

    @property
    def sop_instance_uid(self) -> str:
        return self._dataset.SOPInstanceUID

    @sop_instance_uid.setter
    def sop_instance_uid(self, value: str):
        self._dataset.SOPInstanceUID = value

    # General Series Module
    @property
    def modality(self) -> str:
        return self._dataset.Modality

    @modality.setter
    def modality(self, value: str):
        self._dataset.Modality = value

    @property
    def series_instance_uid(self) -> str:
        return self._dataset.SeriesInstanceUID

    @series_instance_uid.setter
    def series_instance_uid(self, value: str):
        self._dataset.SeriesInstanceUID = value

    # General Equipment Module
    @property
    def manufacturer(self) -> str:
        return self._dataset.Manufacturer

    @manufacturer.setter
    def manufacturer(self, value: str):
        self._dataset.Manufacturer = value

    def add_treatment_session_beam(self, beam: "TreatmentSessionIonBeam"):
        if not hasattr(self._dataset, "TreatmentSessionIonBeamSequence"):
            self._dataset.TreatmentSessionIonBeamSequence = []
        self._dataset.TreatmentSessionIonBeamSequence.append(beam.to_dataset())

    def validate(self) -> List[str]:
        errors = []

        # Check Type 1 elements
        type1_elements = [
            "SOPClassUID",
            "SOPInstanceUID",
            "Modality",
            "SeriesInstanceUID",
            "Manufacturer",
            "TreatmentMachineName",
        ]
        for elem in type1_elements:
            if not hasattr(self._dataset, elem):
                errors.append(f"{elem} is missing")
            elif getattr(self._dataset, elem) is None:
                errors.append(f"{elem} has no value assigned")

        # Check for required sequences
        if not hasattr(self._dataset, "TreatmentSessionIonBeamSequence"):
            errors.append("TreatmentSessionIonBeamSequence is missing")
        elif not self._dataset.TreatmentSessionIonBeamSequence:
            errors.append("TreatmentSessionIonBeamSequence is empty")

        # Check for Treatment Machine Sequence
        if not hasattr(self._dataset, "TreatmentMachineSequence"):
            errors.append("TreatmentMachineSequence is missing")
        elif not self._dataset.TreatmentMachineSequence:
            errors.append("TreatmentMachineSequence is empty")

        return errors

    def to_dataset(self) -> Dataset:
        return self._dataset

    @classmethod
    def from_dataset(cls, dataset: Dataset):
        iod = cls()
        iod._dataset = dataset
        return iod
