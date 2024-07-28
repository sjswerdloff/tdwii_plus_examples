# ion_beam_sequence.py

from typing import List, Optional

from pydicom.dataset import Dataset


class IonBeam:
    def __init__(self):
        self._dataset = Dataset()

    # Type 1 elements
    @property
    def beam_number(self) -> int:
        return self._dataset.BeamNumber

    @beam_number.setter
    def beam_number(self, value: int):
        self._dataset.BeamNumber = value

    @property
    def beam_name(self) -> str:
        return self._dataset.BeamName

    @beam_name.setter
    def beam_name(self, value: str):
        self._dataset.BeamName = value

    @property
    def beam_type(self) -> str:
        return self._dataset.BeamType

    @beam_type.setter
    def beam_type(self, value: str):
        self._dataset.BeamType = value

    @property
    def radiation_type(self) -> str:
        return self._dataset.RadiationType

    @radiation_type.setter
    def radiation_type(self, value: str):
        self._dataset.RadiationType = value

    # Type 2 elements
    @property
    def treatment_delivery_type(self) -> str:
        return self._dataset.TreatmentDeliveryType

    @treatment_delivery_type.setter
    def treatment_delivery_type(self, value: str):
        self._dataset.TreatmentDeliveryType = value

    @property
    def number_of_wedges(self) -> int:
        return self._dataset.NumberOfWedges

    @number_of_wedges.setter
    def number_of_wedges(self, value: int):
        self._dataset.NumberOfWedges = value

    @property
    def number_of_compensators(self) -> int:
        return self._dataset.NumberOfCompensators

    @number_of_compensators.setter
    def number_of_compensators(self, value: int):
        self._dataset.NumberOfCompensators = value

    @property
    def number_of_boli(self) -> int:
        return self._dataset.NumberOfBoli

    @number_of_boli.setter
    def number_of_boli(self, value: int):
        self._dataset.NumberOfBoli = value

    @property
    def number_of_blocks(self) -> int:
        return self._dataset.NumberOfBlocks

    @number_of_blocks.setter
    def number_of_blocks(self, value: int):
        self._dataset.NumberOfBlocks = value

    # Type 3 elements
    @property
    def final_cumulative_meterset_weight(self) -> Optional[float]:
        return self._dataset.get("FinalCumulativeMetersetWeight")

    @final_cumulative_meterset_weight.setter
    def final_cumulative_meterset_weight(self, value: Optional[float]):
        if value is not None:
            self._dataset.FinalCumulativeMetersetWeight = value

    # Additional Type 1 and 2 elements specific to Ion Beams
    @property
    def scan_mode(self) -> str:
        return self._dataset.ScanMode

    @scan_mode.setter
    def scan_mode(self, value: str):
        self._dataset.ScanMode = value

    @property
    def modulated_scan_mode_type(self) -> str:
        return self._dataset.ModulatedScanModeType

    @modulated_scan_mode_type.setter
    def modulated_scan_mode_type(self, value: str):
        self._dataset.ModulatedScanModeType = value

    @property
    def virtual_source_axis_distances(self) -> List[float]:
        return self._dataset.VirtualSourceAxisDistances

    @virtual_source_axis_distances.setter
    def virtual_source_axis_distances(self, value: List[float]):
        self._dataset.VirtualSourceAxisDistances = value

    def to_dataset(self) -> Dataset:
        return self._dataset

    @classmethod
    def from_dataset(cls, dataset: Dataset):
        ion_beam = cls()
        ion_beam._dataset = dataset
        return ion_beam

    def validate(self) -> List[str]:
        errors = []

        # Check Type 1 elements

        type1_elements = ["BeamNumber", "BeamName", "BeamType", "RadiationType", "ScanMode", "VirtualSourceAxisDistances"]
        for elem in type1_elements:
            if not hasattr(self._dataset, elem):
                errors.append(f"{elem} is missing")

        # Check Type 2 elements
        type2_elements = [
            "TreatmentDeliveryType",
            "NumberOfWedges",
            "NumberOfCompensators",
            "NumberOfBoli",
            "NumberOfBlocks",
            "ModulatedScanModeType",
        ]
        for elem in type2_elements:
            if not hasattr(self._dataset, elem):
                errors.append(f"{elem} is missing")

        return errors

    # Additional methods and properties specific to Ion Beams

    @property
    def number_of_range_shifters(self) -> int:
        return self._dataset.NumberOfRangeShifters

    @number_of_range_shifters.setter
    def number_of_range_shifters(self, value: int):
        self._dataset.NumberOfRangeShifters = value

    @property
    def number_of_lateral_spreading_devices(self) -> int:
        return self._dataset.NumberOfLateralSpreadingDevices

    @number_of_lateral_spreading_devices.setter
    def number_of_lateral_spreading_devices(self, value: int):
        self._dataset.NumberOfLateralSpreadingDevices = value

    @property
    def number_of_range_modulators(self) -> int:
        return self._dataset.NumberOfRangeModulators

    @number_of_range_modulators.setter
    def number_of_range_modulators(self, value: int):
        self._dataset.NumberOfRangeModulators = value

    @property
    def patient_support_type(self) -> Optional[str]:
        return self._dataset.get("PatientSupportType")

    @patient_support_type.setter
    def patient_support_type(self, value: Optional[str]):
        if value is not None:
            self._dataset.PatientSupportType = value

    @property
    def ion_control_point_sequence(self) -> List[Dataset]:
        return self._dataset.IonControlPointSequence

    @ion_control_point_sequence.setter
    def ion_control_point_sequence(self, value: List[Dataset]):
        self._dataset.IonControlPointSequence = value

    def add_ion_control_point(self, control_point: Dataset):
        if not hasattr(self._dataset, "IonControlPointSequence"):
            self._dataset.IonControlPointSequence = []
        self._dataset.IonControlPointSequence.append(control_point)

    # You might want to add more specific methods for handling range shifters,
    # lateral spreading devices, range modulators, etc.

    def set_snout_sequence(self, snout_sequence: List[Dataset]):
        self._dataset.SnoutSequence = snout_sequence

    def get_snout_sequence(self) -> List[Dataset]:
        return self._dataset.get("SnoutSequence", [])

    def set_range_shifter_sequence(self, range_shifter_sequence: List[Dataset]):
        self._dataset.RangeShifterSequence = range_shifter_sequence

    def get_range_shifter_sequence(self) -> List[Dataset]:
        return self._dataset.get("RangeShifterSequence", [])

    def set_lateral_spreading_device_sequence(self, lateral_spreading_device_sequence: List[Dataset]):
        self._dataset.LateralSpreadingDeviceSequence = lateral_spreading_device_sequence

    def get_lateral_spreading_device_sequence(self) -> List[Dataset]:
        return self._dataset.get("LateralSpreadingDeviceSequence", [])

    def set_range_modulator_sequence(self, range_modulator_sequence: List[Dataset]):
        self._dataset.RangeModulatorSequence = range_modulator_sequence

    def get_range_modulator_sequence(self) -> List[Dataset]:
        return self._dataset.get("RangeModulatorSequence", [])


# End of IonBeam class
