from typing import List, Optional, Union

from pydicom.dataset import Dataset


class ReferencedBeam:
    def __init__(self):
        self._dataset = Dataset()

    @property
    def referenced_beam_number(self) -> int:
        return self._dataset.ReferencedBeamNumber

    @referenced_beam_number.setter
    def referenced_beam_number(self, value: int):
        self._dataset.ReferencedBeamNumber = value

    @property
    def beam_dose_specification_point(self) -> Optional[List[float]]:
        return self._dataset.get("BeamDoseSpecificationPoint")

    @beam_dose_specification_point.setter
    def beam_dose_specification_point(self, value: Optional[List[float]]):
        if value is not None:
            self._dataset.BeamDoseSpecificationPoint = value

    @property
    def beam_dose(self) -> Optional[float]:
        return self._dataset.get("BeamDose")

    @beam_dose.setter
    def beam_dose(self, value: Optional[float]):
        if value is not None:
            self._dataset.BeamDose = value

    @property
    def beam_meterset(self) -> Optional[float]:
        return self._dataset.get("BeamMeterset")

    @beam_meterset.setter
    def beam_meterset(self, value: Optional[float]):
        if value is not None:
            self._dataset.BeamMeterset = value

    def to_dataset(self) -> Dataset:
        return self._dataset

    @classmethod
    def from_dataset(cls, dataset: Dataset):
        referenced_beam = cls()
        referenced_beam._dataset = dataset
        return referenced_beam

    def validate(self) -> List[str]:
        errors = []

        # Check Type 1 elements
        if not hasattr(self._dataset, "ReferencedBeamNumber"):
            errors.append("ReferencedBeamNumber is missing")
        elif self._dataset.ReferencedBeamNumber is None:
            errors.append("ReferencedBeamNumber has no value assigned")

        return errors
