from typing import List, Optional, Union

from pydicom.dataset import Dataset


class TreatmentMachine:
    def __init__(self):
        self._dataset = Dataset()

    @property
    def treatment_machine_name(self) -> str:
        return self._dataset.TreatmentMachineName

    @treatment_machine_name.setter
    def treatment_machine_name(self, value: str):
        self._dataset.TreatmentMachineName = value

    @property
    def machine_type(self) -> str:
        return self._dataset.MachineType

    @machine_type.setter
    def machine_type(self, value: str):
        self._dataset.MachineType = value

    @property
    def manufacturer(self) -> str:
        return self._dataset.Manufacturer

    @manufacturer.setter
    def manufacturer(self, value: str):
        self._dataset.Manufacturer = value

    @property
    def institution_name(self) -> str:
        return self._dataset.InstitutionName

    @institution_name.setter
    def institution_name(self, value: str):
        self._dataset.InstitutionName = value

    def validate(self) -> List[str]:
        errors = []

        type1_elements = ["TreatmentMachineName"]
        for elem in type1_elements:
            if not hasattr(self._dataset, elem):
                errors.append(f"{elem} is missing")
            elif getattr(self._dataset, elem) is None:
                errors.append(f"{elem} has no value assigned")

        return errors

    def to_dataset(self) -> Dataset:
        return self._dataset

    @classmethod
    def from_dataset(cls, dataset: Dataset):
        machine = cls()
        machine._dataset = dataset
        return machine
