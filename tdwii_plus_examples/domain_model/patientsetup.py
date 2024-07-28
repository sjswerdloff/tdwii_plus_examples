# patient_setup_sequence.py

from typing import List, Optional

from pydicom.dataset import Dataset


class PatientSetup:
    def __init__(self):
        self._dataset = Dataset()

    # Type 1 elements
    @property
    def patient_setup_number(self) -> int:
        return self._dataset.PatientSetupNumber

    @patient_setup_number.setter
    def patient_setup_number(self, value: int):
        self._dataset.PatientSetupNumber = value

    @property
    def patient_position(self) -> str:
        return self._dataset.PatientPosition

    @patient_position.setter
    def patient_position(self, value: str):
        self._dataset.PatientPosition = value

    # Type 2 elements
    @property
    def setup_technique(self) -> str:
        return self._dataset.SetupTechnique

    @setup_technique.setter
    def setup_technique(self, value: str):
        self._dataset.SetupTechnique = value

    # Type 3 elements
    @property
    def setup_technique_description(self) -> Optional[str]:
        return self._dataset.get("SetupTechniqueDescription")

    @setup_technique_description.setter
    def setup_technique_description(self, value: Optional[str]):
        if value is not None:
            self._dataset.SetupTechniqueDescription = value

    @property
    def patient_additional_position(self) -> Optional[str]:
        return self._dataset.get("PatientAdditionalPosition")

    @patient_additional_position.setter
    def patient_additional_position(self, value: Optional[str]):
        if value is not None:
            self._dataset.PatientAdditionalPosition = value

    def to_dataset(self) -> Dataset:
        return self._dataset

    @classmethod
    def from_dataset(cls, dataset: Dataset):
        patient_setup = cls()
        patient_setup._dataset = dataset
        return patient_setup

    def validate(self) -> List[str]:
        errors = []

        # Check Type 1 elements
        if not hasattr(self._dataset, "PatientSetupNumber"):
            errors.append("PatientSetupNumber is missing")
        if not hasattr(self._dataset, "PatientPosition"):
            errors.append("PatientPosition is missing")

        # Check Type 2 elements
        if not hasattr(self._dataset, "SetupTechnique"):
            errors.append("SetupTechnique is missing")

        return errors
