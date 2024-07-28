from typing import List, Optional, Union

from pydicom.dataset import Dataset


class TreatmentSessionIonBeam:
    def __init__(self):
        self._dataset = Dataset()

    @property
    def referenced_beam_number(self) -> int:
        return self._dataset.ReferencedBeamNumber

    @referenced_beam_number.setter
    def referenced_beam_number(self, value: int):
        self._dataset.ReferencedBeamNumber = value

    @property
    def beam_name(self) -> str:
        return self._dataset.BeamName

    @beam_name.setter
    def beam_name(self, value: str):
        self._dataset.BeamName = value

    @property
    def current_fraction_number(self) -> int:
        return self._dataset.CurrentFractionNumber

    @current_fraction_number.setter
    def current_fraction_number(self, value: int):
        self._dataset.CurrentFractionNumber = value

    @property
    def treatment_delivery_type(self) -> str:
        return self._dataset.TreatmentDeliveryType

    @treatment_delivery_type.setter
    def treatment_delivery_type(self, value: str):
        self._dataset.TreatmentDeliveryType = value

    def add_ion_control_point_delivery(self, control_point: "IonControlPointDelivery"):
        if not hasattr(self._dataset, "IonControlPointDeliverySequence"):
            self._dataset.IonControlPointDeliverySequence = []
        self._dataset.IonControlPointDeliverySequence.append(control_point.to_dataset())

    def validate(self) -> List[str]:
        errors = []

        type1_elements = ["ReferencedBeamNumber", "BeamName", "CurrentFractionNumber", "TreatmentDeliveryType"]
        for elem in type1_elements:
            if not hasattr(self._dataset, elem):
                errors.append(f"{elem} is missing")
            elif getattr(self._dataset, elem) is None:
                errors.append(f"{elem} has no value assigned")

        if not hasattr(self._dataset, "IonControlPointDeliverySequence"):
            errors.append("IonControlPointDeliverySequence is missing")
        elif not self._dataset.IonControlPointDeliverySequence:
            errors.append("IonControlPointDeliverySequence is empty")

        return errors

    def to_dataset(self) -> Dataset:
        return self._dataset

    @classmethod
    def from_dataset(cls, dataset: Dataset):
        beam = cls()
        beam._dataset = dataset
        return beam
