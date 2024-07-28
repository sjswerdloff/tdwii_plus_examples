from typing import List, Optional, Union

from pydicom.dataset import Dataset


class IonControlPointDelivery:
    def __init__(self):
        self._dataset = Dataset()

    @property
    def referenced_control_point_index(self) -> int:
        return self._dataset.ReferencedControlPointIndex

    @referenced_control_point_index.setter
    def referenced_control_point_index(self, value: int):
        self._dataset.ReferencedControlPointIndex = value

    @property
    def treatment_control_point_date(self) -> str:
        return self._dataset.TreatmentControlPointDate

    @treatment_control_point_date.setter
    def treatment_control_point_date(self, value: str):
        self._dataset.TreatmentControlPointDate = value

    @property
    def treatment_control_point_time(self) -> str:
        return self._dataset.TreatmentControlPointTime

    @treatment_control_point_time.setter
    def treatment_control_point_time(self, value: str):
        self._dataset.TreatmentControlPointTime = value

    @property
    def specified_meterset(self) -> float:
        return self._dataset.SpecifiedMeterset

    @specified_meterset.setter
    def specified_meterset(self, value: float):
        self._dataset.SpecifiedMeterset = value

    @property
    def delivered_meterset(self) -> float:
        return self._dataset.DeliveredMeterset

    @delivered_meterset.setter
    def delivered_meterset(self, value: float):
        self._dataset.DeliveredMeterset = value

    @property
    def nominal_beam_energy(self) -> float:
        return self._dataset.NominalBeamEnergy

    @nominal_beam_energy.setter
    def nominal_beam_energy(self, value: float):
        self._dataset.NominalBeamEnergy = value

    @property
    def scan_spot_position_map(self) -> List[float]:
        return self._dataset.ScanSpotPositionMap

    @scan_spot_position_map.setter
    def scan_spot_position_map(self, value: List[float]):
        self._dataset.ScanSpotPositionMap = value

    @property
    def scan_spot_meterset_weights(self) -> List[float]:
        return self._dataset.ScanSpotMetersetWeights

    @scan_spot_meterset_weights.setter
    def scan_spot_meterset_weights(self, value: List[float]):
        self._dataset.ScanSpotMetersetWeights = value

    def validate(self) -> List[str]:
        errors = []

        type1_elements = [
            "ReferencedControlPointIndex",
            "TreatmentControlPointDate",
            "TreatmentControlPointTime",
            "SpecifiedMeterset",
            "DeliveredMeterset",
            "NominalBeamEnergy",
            "ScanSpotPositionMap",
            "ScanSpotMetersetWeights",
        ]
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
        control_point = cls()
        control_point._dataset = dataset
        return control_point
