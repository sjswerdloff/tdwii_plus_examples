from decimal import Decimal
from typing import Any, List, Optional  # noqa

import pydicom

from .applicator_sequence_item import ApplicatorSequenceItem
from .code_sequence_item import CodeSequenceItem
from .depth_dose_parameters_sequence_item import DepthDoseParametersSequenceItem
from .enhanced_rt_beam_limiting_device_sequence_item import (
    EnhancedRTBeamLimitingDeviceSequenceItem,
)
from .general_accessory_sequence_item import GeneralAccessorySequenceItem
from .ion_beam_limiting_device_sequence_item import IonBeamLimitingDeviceSequenceItem
from .ion_block_sequence_item import IonBlockSequenceItem
from .ion_control_point_sequence_item import IonControlPointSequenceItem
from .ion_range_compensator_sequence_item import IonRangeCompensatorSequenceItem
from .ion_wedge_sequence_item import IonWedgeSequenceItem
from .lateral_spreading_device_sequence_item import LateralSpreadingDeviceSequenceItem
from .range_modulator_sequence_item import RangeModulatorSequenceItem
from .range_shifter_sequence_item import RangeShifterSequenceItem
from .referenced_bolus_sequence_item import ReferencedBolusSequenceItem
from .referenced_dose_sequence_item import ReferencedDoseSequenceItem
from .referenced_reference_image_sequence_item import (
    ReferencedReferenceImageSequenceItem,
)
from .snout_sequence_item import SnoutSequenceItem


class IonBeamSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._InstitutionalDepartmentTypeCodeSequence: List[CodeSequenceItem] = []
        self._EnhancedRTBeamLimitingDeviceSequence: List[EnhancedRTBeamLimitingDeviceSequenceItem] = []
        self._ApplicatorSequence: List[ApplicatorSequenceItem] = []
        self._IonRangeCompensatorSequence: List[IonRangeCompensatorSequenceItem] = []
        self._SnoutSequence: List[SnoutSequenceItem] = []
        self._RangeShifterSequence: List[RangeShifterSequenceItem] = []
        self._LateralSpreadingDeviceSequence: List[LateralSpreadingDeviceSequenceItem] = []
        self._RangeModulatorSequence: List[RangeModulatorSequenceItem] = []
        self._IonBeamLimitingDeviceSequence: List[IonBeamLimitingDeviceSequenceItem] = []
        self._IonBlockSequence: List[IonBlockSequenceItem] = []
        self._IonControlPointSequence: List[IonControlPointSequenceItem] = []
        self._IonWedgeSequence: List[IonWedgeSequenceItem] = []
        self._GeneralAccessorySequence: List[GeneralAccessorySequenceItem] = []
        self._DepthDoseParametersSequence: List[DepthDoseParametersSequenceItem] = []
        self._ReferencedReferenceImageSequence: List[ReferencedReferenceImageSequenceItem] = []
        self._ReferencedDoseSequence: List[ReferencedDoseSequenceItem] = []
        self._ReferencedBolusSequence: List[ReferencedBolusSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def Manufacturer(self) -> Optional[str]:
        if "Manufacturer" in self._dataset:
            return self._dataset.Manufacturer
        return None

    @Manufacturer.setter
    def Manufacturer(self, value: Optional[str]):
        if value is None:
            if "Manufacturer" in self._dataset:
                del self._dataset.Manufacturer
        else:
            self._dataset.Manufacturer = value

    @property
    def InstitutionName(self) -> Optional[str]:
        if "InstitutionName" in self._dataset:
            return self._dataset.InstitutionName
        return None

    @InstitutionName.setter
    def InstitutionName(self, value: Optional[str]):
        if value is None:
            if "InstitutionName" in self._dataset:
                del self._dataset.InstitutionName
        else:
            self._dataset.InstitutionName = value

    @property
    def InstitutionAddress(self) -> Optional[str]:
        if "InstitutionAddress" in self._dataset:
            return self._dataset.InstitutionAddress
        return None

    @InstitutionAddress.setter
    def InstitutionAddress(self, value: Optional[str]):
        if value is None:
            if "InstitutionAddress" in self._dataset:
                del self._dataset.InstitutionAddress
        else:
            self._dataset.InstitutionAddress = value

    @property
    def InstitutionalDepartmentName(self) -> Optional[str]:
        if "InstitutionalDepartmentName" in self._dataset:
            return self._dataset.InstitutionalDepartmentName
        return None

    @InstitutionalDepartmentName.setter
    def InstitutionalDepartmentName(self, value: Optional[str]):
        if value is None:
            if "InstitutionalDepartmentName" in self._dataset:
                del self._dataset.InstitutionalDepartmentName
        else:
            self._dataset.InstitutionalDepartmentName = value

    @property
    def InstitutionalDepartmentTypeCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "InstitutionalDepartmentTypeCodeSequence" in self._dataset:
            if len(self._InstitutionalDepartmentTypeCodeSequence) == len(
                self._dataset.InstitutionalDepartmentTypeCodeSequence
            ):
                return self._InstitutionalDepartmentTypeCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.InstitutionalDepartmentTypeCodeSequence]
        return None

    @InstitutionalDepartmentTypeCodeSequence.setter
    def InstitutionalDepartmentTypeCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._InstitutionalDepartmentTypeCodeSequence = []
            if "InstitutionalDepartmentTypeCodeSequence" in self._dataset:
                del self._dataset.InstitutionalDepartmentTypeCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("InstitutionalDepartmentTypeCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._InstitutionalDepartmentTypeCodeSequence = value
            if "InstitutionalDepartmentTypeCodeSequence" not in self._dataset:
                self._dataset.InstitutionalDepartmentTypeCodeSequence = pydicom.Sequence()
            self._dataset.InstitutionalDepartmentTypeCodeSequence.clear()
            self._dataset.InstitutionalDepartmentTypeCodeSequence.extend([item.to_dataset() for item in value])

    def add_InstitutionalDepartmentTypeCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._InstitutionalDepartmentTypeCodeSequence.append(item)
        if "InstitutionalDepartmentTypeCodeSequence" not in self._dataset:
            self._dataset.InstitutionalDepartmentTypeCodeSequence = pydicom.Sequence()
        self._dataset.InstitutionalDepartmentTypeCodeSequence.append(item.to_dataset())

    @property
    def ManufacturerModelName(self) -> Optional[str]:
        if "ManufacturerModelName" in self._dataset:
            return self._dataset.ManufacturerModelName
        return None

    @ManufacturerModelName.setter
    def ManufacturerModelName(self, value: Optional[str]):
        if value is None:
            if "ManufacturerModelName" in self._dataset:
                del self._dataset.ManufacturerModelName
        else:
            self._dataset.ManufacturerModelName = value

    @property
    def DeviceSerialNumber(self) -> Optional[str]:
        if "DeviceSerialNumber" in self._dataset:
            return self._dataset.DeviceSerialNumber
        return None

    @DeviceSerialNumber.setter
    def DeviceSerialNumber(self, value: Optional[str]):
        if value is None:
            if "DeviceSerialNumber" in self._dataset:
                del self._dataset.DeviceSerialNumber
        else:
            self._dataset.DeviceSerialNumber = value

    @property
    def DateOfManufacture(self) -> Optional[str]:
        if "DateOfManufacture" in self._dataset:
            return self._dataset.DateOfManufacture
        return None

    @DateOfManufacture.setter
    def DateOfManufacture(self, value: Optional[str]):
        if value is None:
            if "DateOfManufacture" in self._dataset:
                del self._dataset.DateOfManufacture
        else:
            self._dataset.DateOfManufacture = value

    @property
    def DateOfInstallation(self) -> Optional[str]:
        if "DateOfInstallation" in self._dataset:
            return self._dataset.DateOfInstallation
        return None

    @DateOfInstallation.setter
    def DateOfInstallation(self, value: Optional[str]):
        if value is None:
            if "DateOfInstallation" in self._dataset:
                del self._dataset.DateOfInstallation
        else:
            self._dataset.DateOfInstallation = value

    @property
    def EnhancedRTBeamLimitingDeviceSequence(self) -> Optional[List[EnhancedRTBeamLimitingDeviceSequenceItem]]:
        if "EnhancedRTBeamLimitingDeviceSequence" in self._dataset:
            if len(self._EnhancedRTBeamLimitingDeviceSequence) == len(self._dataset.EnhancedRTBeamLimitingDeviceSequence):
                return self._EnhancedRTBeamLimitingDeviceSequence
            else:
                return [
                    EnhancedRTBeamLimitingDeviceSequenceItem(x) for x in self._dataset.EnhancedRTBeamLimitingDeviceSequence
                ]
        return None

    @EnhancedRTBeamLimitingDeviceSequence.setter
    def EnhancedRTBeamLimitingDeviceSequence(self, value: Optional[List[EnhancedRTBeamLimitingDeviceSequenceItem]]):
        if value is None:
            self._EnhancedRTBeamLimitingDeviceSequence = []
            if "EnhancedRTBeamLimitingDeviceSequence" in self._dataset:
                del self._dataset.EnhancedRTBeamLimitingDeviceSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, EnhancedRTBeamLimitingDeviceSequenceItem) for item in value
        ):
            raise ValueError(
                "EnhancedRTBeamLimitingDeviceSequence must be a list of EnhancedRTBeamLimitingDeviceSequenceItem objects"
            )
        else:
            self._EnhancedRTBeamLimitingDeviceSequence = value
            if "EnhancedRTBeamLimitingDeviceSequence" not in self._dataset:
                self._dataset.EnhancedRTBeamLimitingDeviceSequence = pydicom.Sequence()
            self._dataset.EnhancedRTBeamLimitingDeviceSequence.clear()
            self._dataset.EnhancedRTBeamLimitingDeviceSequence.extend([item.to_dataset() for item in value])

    def add_EnhancedRTBeamLimitingDevice(self, item: EnhancedRTBeamLimitingDeviceSequenceItem):
        if not isinstance(item, EnhancedRTBeamLimitingDeviceSequenceItem):
            raise ValueError("Item must be an instance of EnhancedRTBeamLimitingDeviceSequenceItem")
        self._EnhancedRTBeamLimitingDeviceSequence.append(item)
        if "EnhancedRTBeamLimitingDeviceSequence" not in self._dataset:
            self._dataset.EnhancedRTBeamLimitingDeviceSequence = pydicom.Sequence()
        self._dataset.EnhancedRTBeamLimitingDeviceSequence.append(item.to_dataset())

    @property
    def EnhancedRTBeamLimitingDeviceDefinitionFlag(self) -> Optional[str]:
        if "EnhancedRTBeamLimitingDeviceDefinitionFlag" in self._dataset:
            return self._dataset.EnhancedRTBeamLimitingDeviceDefinitionFlag
        return None

    @EnhancedRTBeamLimitingDeviceDefinitionFlag.setter
    def EnhancedRTBeamLimitingDeviceDefinitionFlag(self, value: Optional[str]):
        if value is None:
            if "EnhancedRTBeamLimitingDeviceDefinitionFlag" in self._dataset:
                del self._dataset.EnhancedRTBeamLimitingDeviceDefinitionFlag
        else:
            self._dataset.EnhancedRTBeamLimitingDeviceDefinitionFlag = value

    @property
    def TreatmentMachineName(self) -> Optional[str]:
        if "TreatmentMachineName" in self._dataset:
            return self._dataset.TreatmentMachineName
        return None

    @TreatmentMachineName.setter
    def TreatmentMachineName(self, value: Optional[str]):
        if value is None:
            if "TreatmentMachineName" in self._dataset:
                del self._dataset.TreatmentMachineName
        else:
            self._dataset.TreatmentMachineName = value

    @property
    def PrimaryDosimeterUnit(self) -> Optional[str]:
        if "PrimaryDosimeterUnit" in self._dataset:
            return self._dataset.PrimaryDosimeterUnit
        return None

    @PrimaryDosimeterUnit.setter
    def PrimaryDosimeterUnit(self, value: Optional[str]):
        if value is None:
            if "PrimaryDosimeterUnit" in self._dataset:
                del self._dataset.PrimaryDosimeterUnit
        else:
            self._dataset.PrimaryDosimeterUnit = value

    @property
    def BeamNumber(self) -> Optional[int]:
        if "BeamNumber" in self._dataset:
            return self._dataset.BeamNumber
        return None

    @BeamNumber.setter
    def BeamNumber(self, value: Optional[int]):
        if value is None:
            if "BeamNumber" in self._dataset:
                del self._dataset.BeamNumber
        else:
            self._dataset.BeamNumber = value

    @property
    def BeamName(self) -> Optional[str]:
        if "BeamName" in self._dataset:
            return self._dataset.BeamName
        return None

    @BeamName.setter
    def BeamName(self, value: Optional[str]):
        if value is None:
            if "BeamName" in self._dataset:
                del self._dataset.BeamName
        else:
            self._dataset.BeamName = value

    @property
    def BeamDescription(self) -> Optional[str]:
        if "BeamDescription" in self._dataset:
            return self._dataset.BeamDescription
        return None

    @BeamDescription.setter
    def BeamDescription(self, value: Optional[str]):
        if value is None:
            if "BeamDescription" in self._dataset:
                del self._dataset.BeamDescription
        else:
            self._dataset.BeamDescription = value

    @property
    def BeamType(self) -> Optional[str]:
        if "BeamType" in self._dataset:
            return self._dataset.BeamType
        return None

    @BeamType.setter
    def BeamType(self, value: Optional[str]):
        if value is None:
            if "BeamType" in self._dataset:
                del self._dataset.BeamType
        else:
            self._dataset.BeamType = value

    @property
    def RadiationType(self) -> Optional[str]:
        if "RadiationType" in self._dataset:
            return self._dataset.RadiationType
        return None

    @RadiationType.setter
    def RadiationType(self, value: Optional[str]):
        if value is None:
            if "RadiationType" in self._dataset:
                del self._dataset.RadiationType
        else:
            self._dataset.RadiationType = value

    @property
    def TreatmentDeliveryType(self) -> Optional[str]:
        if "TreatmentDeliveryType" in self._dataset:
            return self._dataset.TreatmentDeliveryType
        return None

    @TreatmentDeliveryType.setter
    def TreatmentDeliveryType(self, value: Optional[str]):
        if value is None:
            if "TreatmentDeliveryType" in self._dataset:
                del self._dataset.TreatmentDeliveryType
        else:
            self._dataset.TreatmentDeliveryType = value

    @property
    def NumberOfWedges(self) -> Optional[int]:
        if "NumberOfWedges" in self._dataset:
            return self._dataset.NumberOfWedges
        return None

    @NumberOfWedges.setter
    def NumberOfWedges(self, value: Optional[int]):
        if value is None:
            if "NumberOfWedges" in self._dataset:
                del self._dataset.NumberOfWedges
        else:
            self._dataset.NumberOfWedges = value

    @property
    def TotalWedgeTrayWaterEquivalentThickness(self) -> Optional[float]:
        if "TotalWedgeTrayWaterEquivalentThickness" in self._dataset:
            return self._dataset.TotalWedgeTrayWaterEquivalentThickness
        return None

    @TotalWedgeTrayWaterEquivalentThickness.setter
    def TotalWedgeTrayWaterEquivalentThickness(self, value: Optional[float]):
        if value is None:
            if "TotalWedgeTrayWaterEquivalentThickness" in self._dataset:
                del self._dataset.TotalWedgeTrayWaterEquivalentThickness
        else:
            self._dataset.TotalWedgeTrayWaterEquivalentThickness = value

    @property
    def NumberOfCompensators(self) -> Optional[int]:
        if "NumberOfCompensators" in self._dataset:
            return self._dataset.NumberOfCompensators
        return None

    @NumberOfCompensators.setter
    def NumberOfCompensators(self, value: Optional[int]):
        if value is None:
            if "NumberOfCompensators" in self._dataset:
                del self._dataset.NumberOfCompensators
        else:
            self._dataset.NumberOfCompensators = value

    @property
    def NumberOfBoli(self) -> Optional[int]:
        if "NumberOfBoli" in self._dataset:
            return self._dataset.NumberOfBoli
        return None

    @NumberOfBoli.setter
    def NumberOfBoli(self, value: Optional[int]):
        if value is None:
            if "NumberOfBoli" in self._dataset:
                del self._dataset.NumberOfBoli
        else:
            self._dataset.NumberOfBoli = value

    @property
    def NumberOfBlocks(self) -> Optional[int]:
        if "NumberOfBlocks" in self._dataset:
            return self._dataset.NumberOfBlocks
        return None

    @NumberOfBlocks.setter
    def NumberOfBlocks(self, value: Optional[int]):
        if value is None:
            if "NumberOfBlocks" in self._dataset:
                del self._dataset.NumberOfBlocks
        else:
            self._dataset.NumberOfBlocks = value

    @property
    def TotalBlockTrayWaterEquivalentThickness(self) -> Optional[float]:
        if "TotalBlockTrayWaterEquivalentThickness" in self._dataset:
            return self._dataset.TotalBlockTrayWaterEquivalentThickness
        return None

    @TotalBlockTrayWaterEquivalentThickness.setter
    def TotalBlockTrayWaterEquivalentThickness(self, value: Optional[float]):
        if value is None:
            if "TotalBlockTrayWaterEquivalentThickness" in self._dataset:
                del self._dataset.TotalBlockTrayWaterEquivalentThickness
        else:
            self._dataset.TotalBlockTrayWaterEquivalentThickness = value

    @property
    def ApplicatorSequence(self) -> Optional[List[ApplicatorSequenceItem]]:
        if "ApplicatorSequence" in self._dataset:
            if len(self._ApplicatorSequence) == len(self._dataset.ApplicatorSequence):
                return self._ApplicatorSequence
            else:
                return [ApplicatorSequenceItem(x) for x in self._dataset.ApplicatorSequence]
        return None

    @ApplicatorSequence.setter
    def ApplicatorSequence(self, value: Optional[List[ApplicatorSequenceItem]]):
        if value is None:
            self._ApplicatorSequence = []
            if "ApplicatorSequence" in self._dataset:
                del self._dataset.ApplicatorSequence
        elif not isinstance(value, list) or not all(isinstance(item, ApplicatorSequenceItem) for item in value):
            raise ValueError("ApplicatorSequence must be a list of ApplicatorSequenceItem objects")
        else:
            self._ApplicatorSequence = value
            if "ApplicatorSequence" not in self._dataset:
                self._dataset.ApplicatorSequence = pydicom.Sequence()
            self._dataset.ApplicatorSequence.clear()
            self._dataset.ApplicatorSequence.extend([item.to_dataset() for item in value])

    def add_Applicator(self, item: ApplicatorSequenceItem):
        if not isinstance(item, ApplicatorSequenceItem):
            raise ValueError("Item must be an instance of ApplicatorSequenceItem")
        self._ApplicatorSequence.append(item)
        if "ApplicatorSequence" not in self._dataset:
            self._dataset.ApplicatorSequence = pydicom.Sequence()
        self._dataset.ApplicatorSequence.append(item.to_dataset())

    @property
    def FinalCumulativeMetersetWeight(self) -> Optional[Decimal]:
        if "FinalCumulativeMetersetWeight" in self._dataset:
            return self._dataset.FinalCumulativeMetersetWeight
        return None

    @FinalCumulativeMetersetWeight.setter
    def FinalCumulativeMetersetWeight(self, value: Optional[Decimal]):
        if value is None:
            if "FinalCumulativeMetersetWeight" in self._dataset:
                del self._dataset.FinalCumulativeMetersetWeight
        else:
            self._dataset.FinalCumulativeMetersetWeight = value

    @property
    def NumberOfControlPoints(self) -> Optional[int]:
        if "NumberOfControlPoints" in self._dataset:
            return self._dataset.NumberOfControlPoints
        return None

    @NumberOfControlPoints.setter
    def NumberOfControlPoints(self, value: Optional[int]):
        if value is None:
            if "NumberOfControlPoints" in self._dataset:
                del self._dataset.NumberOfControlPoints
        else:
            self._dataset.NumberOfControlPoints = value

    @property
    def FixationEye(self) -> Optional[str]:
        if "FixationEye" in self._dataset:
            return self._dataset.FixationEye
        return None

    @FixationEye.setter
    def FixationEye(self, value: Optional[str]):
        if value is None:
            if "FixationEye" in self._dataset:
                del self._dataset.FixationEye
        else:
            self._dataset.FixationEye = value

    @property
    def TotalCompensatorTrayWaterEquivalentThickness(self) -> Optional[float]:
        if "TotalCompensatorTrayWaterEquivalentThickness" in self._dataset:
            return self._dataset.TotalCompensatorTrayWaterEquivalentThickness
        return None

    @TotalCompensatorTrayWaterEquivalentThickness.setter
    def TotalCompensatorTrayWaterEquivalentThickness(self, value: Optional[float]):
        if value is None:
            if "TotalCompensatorTrayWaterEquivalentThickness" in self._dataset:
                del self._dataset.TotalCompensatorTrayWaterEquivalentThickness
        else:
            self._dataset.TotalCompensatorTrayWaterEquivalentThickness = value

    @property
    def IonRangeCompensatorSequence(self) -> Optional[List[IonRangeCompensatorSequenceItem]]:
        if "IonRangeCompensatorSequence" in self._dataset:
            if len(self._IonRangeCompensatorSequence) == len(self._dataset.IonRangeCompensatorSequence):
                return self._IonRangeCompensatorSequence
            else:
                return [IonRangeCompensatorSequenceItem(x) for x in self._dataset.IonRangeCompensatorSequence]
        return None

    @IonRangeCompensatorSequence.setter
    def IonRangeCompensatorSequence(self, value: Optional[List[IonRangeCompensatorSequenceItem]]):
        if value is None:
            self._IonRangeCompensatorSequence = []
            if "IonRangeCompensatorSequence" in self._dataset:
                del self._dataset.IonRangeCompensatorSequence
        elif not isinstance(value, list) or not all(isinstance(item, IonRangeCompensatorSequenceItem) for item in value):
            raise ValueError("IonRangeCompensatorSequence must be a list of IonRangeCompensatorSequenceItem objects")
        else:
            self._IonRangeCompensatorSequence = value
            if "IonRangeCompensatorSequence" not in self._dataset:
                self._dataset.IonRangeCompensatorSequence = pydicom.Sequence()
            self._dataset.IonRangeCompensatorSequence.clear()
            self._dataset.IonRangeCompensatorSequence.extend([item.to_dataset() for item in value])

    def add_IonRangeCompensator(self, item: IonRangeCompensatorSequenceItem):
        if not isinstance(item, IonRangeCompensatorSequenceItem):
            raise ValueError("Item must be an instance of IonRangeCompensatorSequenceItem")
        self._IonRangeCompensatorSequence.append(item)
        if "IonRangeCompensatorSequence" not in self._dataset:
            self._dataset.IonRangeCompensatorSequence = pydicom.Sequence()
        self._dataset.IonRangeCompensatorSequence.append(item.to_dataset())

    @property
    def RadiationMassNumber(self) -> Optional[int]:
        if "RadiationMassNumber" in self._dataset:
            return self._dataset.RadiationMassNumber
        return None

    @RadiationMassNumber.setter
    def RadiationMassNumber(self, value: Optional[int]):
        if value is None:
            if "RadiationMassNumber" in self._dataset:
                del self._dataset.RadiationMassNumber
        else:
            self._dataset.RadiationMassNumber = value

    @property
    def RadiationAtomicNumber(self) -> Optional[int]:
        if "RadiationAtomicNumber" in self._dataset:
            return self._dataset.RadiationAtomicNumber
        return None

    @RadiationAtomicNumber.setter
    def RadiationAtomicNumber(self, value: Optional[int]):
        if value is None:
            if "RadiationAtomicNumber" in self._dataset:
                del self._dataset.RadiationAtomicNumber
        else:
            self._dataset.RadiationAtomicNumber = value

    @property
    def RadiationChargeState(self) -> Optional[int]:
        if "RadiationChargeState" in self._dataset:
            return self._dataset.RadiationChargeState
        return None

    @RadiationChargeState.setter
    def RadiationChargeState(self, value: Optional[int]):
        if value is None:
            if "RadiationChargeState" in self._dataset:
                del self._dataset.RadiationChargeState
        else:
            self._dataset.RadiationChargeState = value

    @property
    def ScanMode(self) -> Optional[str]:
        if "ScanMode" in self._dataset:
            return self._dataset.ScanMode
        return None

    @ScanMode.setter
    def ScanMode(self, value: Optional[str]):
        if value is None:
            if "ScanMode" in self._dataset:
                del self._dataset.ScanMode
        else:
            self._dataset.ScanMode = value

    @property
    def ModulatedScanModeType(self) -> Optional[str]:
        if "ModulatedScanModeType" in self._dataset:
            return self._dataset.ModulatedScanModeType
        return None

    @ModulatedScanModeType.setter
    def ModulatedScanModeType(self, value: Optional[str]):
        if value is None:
            if "ModulatedScanModeType" in self._dataset:
                del self._dataset.ModulatedScanModeType
        else:
            self._dataset.ModulatedScanModeType = value

    @property
    def VirtualSourceAxisDistances(self) -> Optional[List[float]]:
        if "VirtualSourceAxisDistances" in self._dataset:
            return self._dataset.VirtualSourceAxisDistances
        return None

    @VirtualSourceAxisDistances.setter
    def VirtualSourceAxisDistances(self, value: Optional[List[float]]):
        if value is None:
            if "VirtualSourceAxisDistances" in self._dataset:
                del self._dataset.VirtualSourceAxisDistances
        else:
            self._dataset.VirtualSourceAxisDistances = value

    @property
    def SnoutSequence(self) -> Optional[List[SnoutSequenceItem]]:
        if "SnoutSequence" in self._dataset:
            if len(self._SnoutSequence) == len(self._dataset.SnoutSequence):
                return self._SnoutSequence
            else:
                return [SnoutSequenceItem(x) for x in self._dataset.SnoutSequence]
        return None

    @SnoutSequence.setter
    def SnoutSequence(self, value: Optional[List[SnoutSequenceItem]]):
        if value is None:
            self._SnoutSequence = []
            if "SnoutSequence" in self._dataset:
                del self._dataset.SnoutSequence
        elif not isinstance(value, list) or not all(isinstance(item, SnoutSequenceItem) for item in value):
            raise ValueError("SnoutSequence must be a list of SnoutSequenceItem objects")
        else:
            self._SnoutSequence = value
            if "SnoutSequence" not in self._dataset:
                self._dataset.SnoutSequence = pydicom.Sequence()
            self._dataset.SnoutSequence.clear()
            self._dataset.SnoutSequence.extend([item.to_dataset() for item in value])

    def add_Snout(self, item: SnoutSequenceItem):
        if not isinstance(item, SnoutSequenceItem):
            raise ValueError("Item must be an instance of SnoutSequenceItem")
        self._SnoutSequence.append(item)
        if "SnoutSequence" not in self._dataset:
            self._dataset.SnoutSequence = pydicom.Sequence()
        self._dataset.SnoutSequence.append(item.to_dataset())

    @property
    def NumberOfRangeShifters(self) -> Optional[int]:
        if "NumberOfRangeShifters" in self._dataset:
            return self._dataset.NumberOfRangeShifters
        return None

    @NumberOfRangeShifters.setter
    def NumberOfRangeShifters(self, value: Optional[int]):
        if value is None:
            if "NumberOfRangeShifters" in self._dataset:
                del self._dataset.NumberOfRangeShifters
        else:
            self._dataset.NumberOfRangeShifters = value

    @property
    def RangeShifterSequence(self) -> Optional[List[RangeShifterSequenceItem]]:
        if "RangeShifterSequence" in self._dataset:
            if len(self._RangeShifterSequence) == len(self._dataset.RangeShifterSequence):
                return self._RangeShifterSequence
            else:
                return [RangeShifterSequenceItem(x) for x in self._dataset.RangeShifterSequence]
        return None

    @RangeShifterSequence.setter
    def RangeShifterSequence(self, value: Optional[List[RangeShifterSequenceItem]]):
        if value is None:
            self._RangeShifterSequence = []
            if "RangeShifterSequence" in self._dataset:
                del self._dataset.RangeShifterSequence
        elif not isinstance(value, list) or not all(isinstance(item, RangeShifterSequenceItem) for item in value):
            raise ValueError("RangeShifterSequence must be a list of RangeShifterSequenceItem objects")
        else:
            self._RangeShifterSequence = value
            if "RangeShifterSequence" not in self._dataset:
                self._dataset.RangeShifterSequence = pydicom.Sequence()
            self._dataset.RangeShifterSequence.clear()
            self._dataset.RangeShifterSequence.extend([item.to_dataset() for item in value])

    def add_RangeShifter(self, item: RangeShifterSequenceItem):
        if not isinstance(item, RangeShifterSequenceItem):
            raise ValueError("Item must be an instance of RangeShifterSequenceItem")
        self._RangeShifterSequence.append(item)
        if "RangeShifterSequence" not in self._dataset:
            self._dataset.RangeShifterSequence = pydicom.Sequence()
        self._dataset.RangeShifterSequence.append(item.to_dataset())

    @property
    def NumberOfLateralSpreadingDevices(self) -> Optional[int]:
        if "NumberOfLateralSpreadingDevices" in self._dataset:
            return self._dataset.NumberOfLateralSpreadingDevices
        return None

    @NumberOfLateralSpreadingDevices.setter
    def NumberOfLateralSpreadingDevices(self, value: Optional[int]):
        if value is None:
            if "NumberOfLateralSpreadingDevices" in self._dataset:
                del self._dataset.NumberOfLateralSpreadingDevices
        else:
            self._dataset.NumberOfLateralSpreadingDevices = value

    @property
    def LateralSpreadingDeviceSequence(self) -> Optional[List[LateralSpreadingDeviceSequenceItem]]:
        if "LateralSpreadingDeviceSequence" in self._dataset:
            if len(self._LateralSpreadingDeviceSequence) == len(self._dataset.LateralSpreadingDeviceSequence):
                return self._LateralSpreadingDeviceSequence
            else:
                return [LateralSpreadingDeviceSequenceItem(x) for x in self._dataset.LateralSpreadingDeviceSequence]
        return None

    @LateralSpreadingDeviceSequence.setter
    def LateralSpreadingDeviceSequence(self, value: Optional[List[LateralSpreadingDeviceSequenceItem]]):
        if value is None:
            self._LateralSpreadingDeviceSequence = []
            if "LateralSpreadingDeviceSequence" in self._dataset:
                del self._dataset.LateralSpreadingDeviceSequence
        elif not isinstance(value, list) or not all(isinstance(item, LateralSpreadingDeviceSequenceItem) for item in value):
            raise ValueError("LateralSpreadingDeviceSequence must be a list of LateralSpreadingDeviceSequenceItem objects")
        else:
            self._LateralSpreadingDeviceSequence = value
            if "LateralSpreadingDeviceSequence" not in self._dataset:
                self._dataset.LateralSpreadingDeviceSequence = pydicom.Sequence()
            self._dataset.LateralSpreadingDeviceSequence.clear()
            self._dataset.LateralSpreadingDeviceSequence.extend([item.to_dataset() for item in value])

    def add_LateralSpreadingDevice(self, item: LateralSpreadingDeviceSequenceItem):
        if not isinstance(item, LateralSpreadingDeviceSequenceItem):
            raise ValueError("Item must be an instance of LateralSpreadingDeviceSequenceItem")
        self._LateralSpreadingDeviceSequence.append(item)
        if "LateralSpreadingDeviceSequence" not in self._dataset:
            self._dataset.LateralSpreadingDeviceSequence = pydicom.Sequence()
        self._dataset.LateralSpreadingDeviceSequence.append(item.to_dataset())

    @property
    def NumberOfRangeModulators(self) -> Optional[int]:
        if "NumberOfRangeModulators" in self._dataset:
            return self._dataset.NumberOfRangeModulators
        return None

    @NumberOfRangeModulators.setter
    def NumberOfRangeModulators(self, value: Optional[int]):
        if value is None:
            if "NumberOfRangeModulators" in self._dataset:
                del self._dataset.NumberOfRangeModulators
        else:
            self._dataset.NumberOfRangeModulators = value

    @property
    def RangeModulatorSequence(self) -> Optional[List[RangeModulatorSequenceItem]]:
        if "RangeModulatorSequence" in self._dataset:
            if len(self._RangeModulatorSequence) == len(self._dataset.RangeModulatorSequence):
                return self._RangeModulatorSequence
            else:
                return [RangeModulatorSequenceItem(x) for x in self._dataset.RangeModulatorSequence]
        return None

    @RangeModulatorSequence.setter
    def RangeModulatorSequence(self, value: Optional[List[RangeModulatorSequenceItem]]):
        if value is None:
            self._RangeModulatorSequence = []
            if "RangeModulatorSequence" in self._dataset:
                del self._dataset.RangeModulatorSequence
        elif not isinstance(value, list) or not all(isinstance(item, RangeModulatorSequenceItem) for item in value):
            raise ValueError("RangeModulatorSequence must be a list of RangeModulatorSequenceItem objects")
        else:
            self._RangeModulatorSequence = value
            if "RangeModulatorSequence" not in self._dataset:
                self._dataset.RangeModulatorSequence = pydicom.Sequence()
            self._dataset.RangeModulatorSequence.clear()
            self._dataset.RangeModulatorSequence.extend([item.to_dataset() for item in value])

    def add_RangeModulator(self, item: RangeModulatorSequenceItem):
        if not isinstance(item, RangeModulatorSequenceItem):
            raise ValueError("Item must be an instance of RangeModulatorSequenceItem")
        self._RangeModulatorSequence.append(item)
        if "RangeModulatorSequence" not in self._dataset:
            self._dataset.RangeModulatorSequence = pydicom.Sequence()
        self._dataset.RangeModulatorSequence.append(item.to_dataset())

    @property
    def PatientSupportType(self) -> Optional[str]:
        if "PatientSupportType" in self._dataset:
            return self._dataset.PatientSupportType
        return None

    @PatientSupportType.setter
    def PatientSupportType(self, value: Optional[str]):
        if value is None:
            if "PatientSupportType" in self._dataset:
                del self._dataset.PatientSupportType
        else:
            self._dataset.PatientSupportType = value

    @property
    def PatientSupportID(self) -> Optional[str]:
        if "PatientSupportID" in self._dataset:
            return self._dataset.PatientSupportID
        return None

    @PatientSupportID.setter
    def PatientSupportID(self, value: Optional[str]):
        if value is None:
            if "PatientSupportID" in self._dataset:
                del self._dataset.PatientSupportID
        else:
            self._dataset.PatientSupportID = value

    @property
    def PatientSupportAccessoryCode(self) -> Optional[str]:
        if "PatientSupportAccessoryCode" in self._dataset:
            return self._dataset.PatientSupportAccessoryCode
        return None

    @PatientSupportAccessoryCode.setter
    def PatientSupportAccessoryCode(self, value: Optional[str]):
        if value is None:
            if "PatientSupportAccessoryCode" in self._dataset:
                del self._dataset.PatientSupportAccessoryCode
        else:
            self._dataset.PatientSupportAccessoryCode = value

    @property
    def FixationLightAzimuthalAngle(self) -> Optional[float]:
        if "FixationLightAzimuthalAngle" in self._dataset:
            return self._dataset.FixationLightAzimuthalAngle
        return None

    @FixationLightAzimuthalAngle.setter
    def FixationLightAzimuthalAngle(self, value: Optional[float]):
        if value is None:
            if "FixationLightAzimuthalAngle" in self._dataset:
                del self._dataset.FixationLightAzimuthalAngle
        else:
            self._dataset.FixationLightAzimuthalAngle = value

    @property
    def FixationLightPolarAngle(self) -> Optional[float]:
        if "FixationLightPolarAngle" in self._dataset:
            return self._dataset.FixationLightPolarAngle
        return None

    @FixationLightPolarAngle.setter
    def FixationLightPolarAngle(self, value: Optional[float]):
        if value is None:
            if "FixationLightPolarAngle" in self._dataset:
                del self._dataset.FixationLightPolarAngle
        else:
            self._dataset.FixationLightPolarAngle = value

    @property
    def IonBeamLimitingDeviceSequence(self) -> Optional[List[IonBeamLimitingDeviceSequenceItem]]:
        if "IonBeamLimitingDeviceSequence" in self._dataset:
            if len(self._IonBeamLimitingDeviceSequence) == len(self._dataset.IonBeamLimitingDeviceSequence):
                return self._IonBeamLimitingDeviceSequence
            else:
                return [IonBeamLimitingDeviceSequenceItem(x) for x in self._dataset.IonBeamLimitingDeviceSequence]
        return None

    @IonBeamLimitingDeviceSequence.setter
    def IonBeamLimitingDeviceSequence(self, value: Optional[List[IonBeamLimitingDeviceSequenceItem]]):
        if value is None:
            self._IonBeamLimitingDeviceSequence = []
            if "IonBeamLimitingDeviceSequence" in self._dataset:
                del self._dataset.IonBeamLimitingDeviceSequence
        elif not isinstance(value, list) or not all(isinstance(item, IonBeamLimitingDeviceSequenceItem) for item in value):
            raise ValueError("IonBeamLimitingDeviceSequence must be a list of IonBeamLimitingDeviceSequenceItem objects")
        else:
            self._IonBeamLimitingDeviceSequence = value
            if "IonBeamLimitingDeviceSequence" not in self._dataset:
                self._dataset.IonBeamLimitingDeviceSequence = pydicom.Sequence()
            self._dataset.IonBeamLimitingDeviceSequence.clear()
            self._dataset.IonBeamLimitingDeviceSequence.extend([item.to_dataset() for item in value])

    def add_IonBeamLimitingDevice(self, item: IonBeamLimitingDeviceSequenceItem):
        if not isinstance(item, IonBeamLimitingDeviceSequenceItem):
            raise ValueError("Item must be an instance of IonBeamLimitingDeviceSequenceItem")
        self._IonBeamLimitingDeviceSequence.append(item)
        if "IonBeamLimitingDeviceSequence" not in self._dataset:
            self._dataset.IonBeamLimitingDeviceSequence = pydicom.Sequence()
        self._dataset.IonBeamLimitingDeviceSequence.append(item.to_dataset())

    @property
    def IonBlockSequence(self) -> Optional[List[IonBlockSequenceItem]]:
        if "IonBlockSequence" in self._dataset:
            if len(self._IonBlockSequence) == len(self._dataset.IonBlockSequence):
                return self._IonBlockSequence
            else:
                return [IonBlockSequenceItem(x) for x in self._dataset.IonBlockSequence]
        return None

    @IonBlockSequence.setter
    def IonBlockSequence(self, value: Optional[List[IonBlockSequenceItem]]):
        if value is None:
            self._IonBlockSequence = []
            if "IonBlockSequence" in self._dataset:
                del self._dataset.IonBlockSequence
        elif not isinstance(value, list) or not all(isinstance(item, IonBlockSequenceItem) for item in value):
            raise ValueError("IonBlockSequence must be a list of IonBlockSequenceItem objects")
        else:
            self._IonBlockSequence = value
            if "IonBlockSequence" not in self._dataset:
                self._dataset.IonBlockSequence = pydicom.Sequence()
            self._dataset.IonBlockSequence.clear()
            self._dataset.IonBlockSequence.extend([item.to_dataset() for item in value])

    def add_IonBlock(self, item: IonBlockSequenceItem):
        if not isinstance(item, IonBlockSequenceItem):
            raise ValueError("Item must be an instance of IonBlockSequenceItem")
        self._IonBlockSequence.append(item)
        if "IonBlockSequence" not in self._dataset:
            self._dataset.IonBlockSequence = pydicom.Sequence()
        self._dataset.IonBlockSequence.append(item.to_dataset())

    @property
    def IonControlPointSequence(self) -> Optional[List[IonControlPointSequenceItem]]:
        if "IonControlPointSequence" in self._dataset:
            if len(self._IonControlPointSequence) == len(self._dataset.IonControlPointSequence):
                return self._IonControlPointSequence
            else:
                return [IonControlPointSequenceItem(x) for x in self._dataset.IonControlPointSequence]
        return None

    @IonControlPointSequence.setter
    def IonControlPointSequence(self, value: Optional[List[IonControlPointSequenceItem]]):
        if value is None:
            self._IonControlPointSequence = []
            if "IonControlPointSequence" in self._dataset:
                del self._dataset.IonControlPointSequence
        elif not isinstance(value, list) or not all(isinstance(item, IonControlPointSequenceItem) for item in value):
            raise ValueError("IonControlPointSequence must be a list of IonControlPointSequenceItem objects")
        else:
            self._IonControlPointSequence = value
            if "IonControlPointSequence" not in self._dataset:
                self._dataset.IonControlPointSequence = pydicom.Sequence()
            self._dataset.IonControlPointSequence.clear()
            self._dataset.IonControlPointSequence.extend([item.to_dataset() for item in value])

    def add_IonControlPoint(self, item: IonControlPointSequenceItem):
        if not isinstance(item, IonControlPointSequenceItem):
            raise ValueError("Item must be an instance of IonControlPointSequenceItem")
        self._IonControlPointSequence.append(item)
        if "IonControlPointSequence" not in self._dataset:
            self._dataset.IonControlPointSequence = pydicom.Sequence()
        self._dataset.IonControlPointSequence.append(item.to_dataset())

    @property
    def IonWedgeSequence(self) -> Optional[List[IonWedgeSequenceItem]]:
        if "IonWedgeSequence" in self._dataset:
            if len(self._IonWedgeSequence) == len(self._dataset.IonWedgeSequence):
                return self._IonWedgeSequence
            else:
                return [IonWedgeSequenceItem(x) for x in self._dataset.IonWedgeSequence]
        return None

    @IonWedgeSequence.setter
    def IonWedgeSequence(self, value: Optional[List[IonWedgeSequenceItem]]):
        if value is None:
            self._IonWedgeSequence = []
            if "IonWedgeSequence" in self._dataset:
                del self._dataset.IonWedgeSequence
        elif not isinstance(value, list) or not all(isinstance(item, IonWedgeSequenceItem) for item in value):
            raise ValueError("IonWedgeSequence must be a list of IonWedgeSequenceItem objects")
        else:
            self._IonWedgeSequence = value
            if "IonWedgeSequence" not in self._dataset:
                self._dataset.IonWedgeSequence = pydicom.Sequence()
            self._dataset.IonWedgeSequence.clear()
            self._dataset.IonWedgeSequence.extend([item.to_dataset() for item in value])

    def add_IonWedge(self, item: IonWedgeSequenceItem):
        if not isinstance(item, IonWedgeSequenceItem):
            raise ValueError("Item must be an instance of IonWedgeSequenceItem")
        self._IonWedgeSequence.append(item)
        if "IonWedgeSequence" not in self._dataset:
            self._dataset.IonWedgeSequence = pydicom.Sequence()
        self._dataset.IonWedgeSequence.append(item.to_dataset())

    @property
    def GeneralAccessorySequence(self) -> Optional[List[GeneralAccessorySequenceItem]]:
        if "GeneralAccessorySequence" in self._dataset:
            if len(self._GeneralAccessorySequence) == len(self._dataset.GeneralAccessorySequence):
                return self._GeneralAccessorySequence
            else:
                return [GeneralAccessorySequenceItem(x) for x in self._dataset.GeneralAccessorySequence]
        return None

    @GeneralAccessorySequence.setter
    def GeneralAccessorySequence(self, value: Optional[List[GeneralAccessorySequenceItem]]):
        if value is None:
            self._GeneralAccessorySequence = []
            if "GeneralAccessorySequence" in self._dataset:
                del self._dataset.GeneralAccessorySequence
        elif not isinstance(value, list) or not all(isinstance(item, GeneralAccessorySequenceItem) for item in value):
            raise ValueError("GeneralAccessorySequence must be a list of GeneralAccessorySequenceItem objects")
        else:
            self._GeneralAccessorySequence = value
            if "GeneralAccessorySequence" not in self._dataset:
                self._dataset.GeneralAccessorySequence = pydicom.Sequence()
            self._dataset.GeneralAccessorySequence.clear()
            self._dataset.GeneralAccessorySequence.extend([item.to_dataset() for item in value])

    def add_GeneralAccessory(self, item: GeneralAccessorySequenceItem):
        if not isinstance(item, GeneralAccessorySequenceItem):
            raise ValueError("Item must be an instance of GeneralAccessorySequenceItem")
        self._GeneralAccessorySequence.append(item)
        if "GeneralAccessorySequence" not in self._dataset:
            self._dataset.GeneralAccessorySequence = pydicom.Sequence()
        self._dataset.GeneralAccessorySequence.append(item.to_dataset())

    @property
    def DepthDoseParametersSequence(self) -> Optional[List[DepthDoseParametersSequenceItem]]:
        if "DepthDoseParametersSequence" in self._dataset:
            if len(self._DepthDoseParametersSequence) == len(self._dataset.DepthDoseParametersSequence):
                return self._DepthDoseParametersSequence
            else:
                return [DepthDoseParametersSequenceItem(x) for x in self._dataset.DepthDoseParametersSequence]
        return None

    @DepthDoseParametersSequence.setter
    def DepthDoseParametersSequence(self, value: Optional[List[DepthDoseParametersSequenceItem]]):
        if value is None:
            self._DepthDoseParametersSequence = []
            if "DepthDoseParametersSequence" in self._dataset:
                del self._dataset.DepthDoseParametersSequence
        elif not isinstance(value, list) or not all(isinstance(item, DepthDoseParametersSequenceItem) for item in value):
            raise ValueError("DepthDoseParametersSequence must be a list of DepthDoseParametersSequenceItem objects")
        else:
            self._DepthDoseParametersSequence = value
            if "DepthDoseParametersSequence" not in self._dataset:
                self._dataset.DepthDoseParametersSequence = pydicom.Sequence()
            self._dataset.DepthDoseParametersSequence.clear()
            self._dataset.DepthDoseParametersSequence.extend([item.to_dataset() for item in value])

    def add_DepthDoseParameters(self, item: DepthDoseParametersSequenceItem):
        if not isinstance(item, DepthDoseParametersSequenceItem):
            raise ValueError("Item must be an instance of DepthDoseParametersSequenceItem")
        self._DepthDoseParametersSequence.append(item)
        if "DepthDoseParametersSequence" not in self._dataset:
            self._dataset.DepthDoseParametersSequence = pydicom.Sequence()
        self._dataset.DepthDoseParametersSequence.append(item.to_dataset())

    @property
    def ReferencedReferenceImageSequence(self) -> Optional[List[ReferencedReferenceImageSequenceItem]]:
        if "ReferencedReferenceImageSequence" in self._dataset:
            if len(self._ReferencedReferenceImageSequence) == len(self._dataset.ReferencedReferenceImageSequence):
                return self._ReferencedReferenceImageSequence
            else:
                return [ReferencedReferenceImageSequenceItem(x) for x in self._dataset.ReferencedReferenceImageSequence]
        return None

    @ReferencedReferenceImageSequence.setter
    def ReferencedReferenceImageSequence(self, value: Optional[List[ReferencedReferenceImageSequenceItem]]):
        if value is None:
            self._ReferencedReferenceImageSequence = []
            if "ReferencedReferenceImageSequence" in self._dataset:
                del self._dataset.ReferencedReferenceImageSequence
        elif not isinstance(value, list) or not all(isinstance(item, ReferencedReferenceImageSequenceItem) for item in value):
            raise ValueError("ReferencedReferenceImageSequence must be a list of ReferencedReferenceImageSequenceItem objects")
        else:
            self._ReferencedReferenceImageSequence = value
            if "ReferencedReferenceImageSequence" not in self._dataset:
                self._dataset.ReferencedReferenceImageSequence = pydicom.Sequence()
            self._dataset.ReferencedReferenceImageSequence.clear()
            self._dataset.ReferencedReferenceImageSequence.extend([item.to_dataset() for item in value])

    def add_ReferencedReferenceImage(self, item: ReferencedReferenceImageSequenceItem):
        if not isinstance(item, ReferencedReferenceImageSequenceItem):
            raise ValueError("Item must be an instance of ReferencedReferenceImageSequenceItem")
        self._ReferencedReferenceImageSequence.append(item)
        if "ReferencedReferenceImageSequence" not in self._dataset:
            self._dataset.ReferencedReferenceImageSequence = pydicom.Sequence()
        self._dataset.ReferencedReferenceImageSequence.append(item.to_dataset())

    @property
    def ReferencedPatientSetupNumber(self) -> Optional[int]:
        if "ReferencedPatientSetupNumber" in self._dataset:
            return self._dataset.ReferencedPatientSetupNumber
        return None

    @ReferencedPatientSetupNumber.setter
    def ReferencedPatientSetupNumber(self, value: Optional[int]):
        if value is None:
            if "ReferencedPatientSetupNumber" in self._dataset:
                del self._dataset.ReferencedPatientSetupNumber
        else:
            self._dataset.ReferencedPatientSetupNumber = value

    @property
    def ReferencedDoseSequence(self) -> Optional[List[ReferencedDoseSequenceItem]]:
        if "ReferencedDoseSequence" in self._dataset:
            if len(self._ReferencedDoseSequence) == len(self._dataset.ReferencedDoseSequence):
                return self._ReferencedDoseSequence
            else:
                return [ReferencedDoseSequenceItem(x) for x in self._dataset.ReferencedDoseSequence]
        return None

    @ReferencedDoseSequence.setter
    def ReferencedDoseSequence(self, value: Optional[List[ReferencedDoseSequenceItem]]):
        if value is None:
            self._ReferencedDoseSequence = []
            if "ReferencedDoseSequence" in self._dataset:
                del self._dataset.ReferencedDoseSequence
        elif not isinstance(value, list) or not all(isinstance(item, ReferencedDoseSequenceItem) for item in value):
            raise ValueError("ReferencedDoseSequence must be a list of ReferencedDoseSequenceItem objects")
        else:
            self._ReferencedDoseSequence = value
            if "ReferencedDoseSequence" not in self._dataset:
                self._dataset.ReferencedDoseSequence = pydicom.Sequence()
            self._dataset.ReferencedDoseSequence.clear()
            self._dataset.ReferencedDoseSequence.extend([item.to_dataset() for item in value])

    def add_ReferencedDose(self, item: ReferencedDoseSequenceItem):
        if not isinstance(item, ReferencedDoseSequenceItem):
            raise ValueError("Item must be an instance of ReferencedDoseSequenceItem")
        self._ReferencedDoseSequence.append(item)
        if "ReferencedDoseSequence" not in self._dataset:
            self._dataset.ReferencedDoseSequence = pydicom.Sequence()
        self._dataset.ReferencedDoseSequence.append(item.to_dataset())

    @property
    def ReferencedToleranceTableNumber(self) -> Optional[int]:
        if "ReferencedToleranceTableNumber" in self._dataset:
            return self._dataset.ReferencedToleranceTableNumber
        return None

    @ReferencedToleranceTableNumber.setter
    def ReferencedToleranceTableNumber(self, value: Optional[int]):
        if value is None:
            if "ReferencedToleranceTableNumber" in self._dataset:
                del self._dataset.ReferencedToleranceTableNumber
        else:
            self._dataset.ReferencedToleranceTableNumber = value

    @property
    def ReferencedBolusSequence(self) -> Optional[List[ReferencedBolusSequenceItem]]:
        if "ReferencedBolusSequence" in self._dataset:
            if len(self._ReferencedBolusSequence) == len(self._dataset.ReferencedBolusSequence):
                return self._ReferencedBolusSequence
            else:
                return [ReferencedBolusSequenceItem(x) for x in self._dataset.ReferencedBolusSequence]
        return None

    @ReferencedBolusSequence.setter
    def ReferencedBolusSequence(self, value: Optional[List[ReferencedBolusSequenceItem]]):
        if value is None:
            self._ReferencedBolusSequence = []
            if "ReferencedBolusSequence" in self._dataset:
                del self._dataset.ReferencedBolusSequence
        elif not isinstance(value, list) or not all(isinstance(item, ReferencedBolusSequenceItem) for item in value):
            raise ValueError("ReferencedBolusSequence must be a list of ReferencedBolusSequenceItem objects")
        else:
            self._ReferencedBolusSequence = value
            if "ReferencedBolusSequence" not in self._dataset:
                self._dataset.ReferencedBolusSequence = pydicom.Sequence()
            self._dataset.ReferencedBolusSequence.clear()
            self._dataset.ReferencedBolusSequence.extend([item.to_dataset() for item in value])

    def add_ReferencedBolus(self, item: ReferencedBolusSequenceItem):
        if not isinstance(item, ReferencedBolusSequenceItem):
            raise ValueError("Item must be an instance of ReferencedBolusSequenceItem")
        self._ReferencedBolusSequence.append(item)
        if "ReferencedBolusSequence" not in self._dataset:
            self._dataset.ReferencedBolusSequence = pydicom.Sequence()
        self._dataset.ReferencedBolusSequence.append(item.to_dataset())

    @property
    def EntityLongLabel(self) -> Optional[str]:
        if "EntityLongLabel" in self._dataset:
            return self._dataset.EntityLongLabel
        return None

    @EntityLongLabel.setter
    def EntityLongLabel(self, value: Optional[str]):
        if value is None:
            if "EntityLongLabel" in self._dataset:
                del self._dataset.EntityLongLabel
        else:
            self._dataset.EntityLongLabel = value
