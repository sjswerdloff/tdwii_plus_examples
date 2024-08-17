from decimal import Decimal
from typing import Any, List, Optional

import pydicom

from .applicator_sequence_item import ApplicatorSequenceItem
from .beam_limiting_device_sequence_item import BeamLimitingDeviceSequenceItem
from .block_sequence_item import BlockSequenceItem
from .code_sequence_item import CodeSequenceItem
from .compensator_sequence_item import CompensatorSequenceItem
from .control_point_sequence_item import ControlPointSequenceItem
from .definition_source_sequence_item import DefinitionSourceSequenceItem
from .enhanced_rt_beam_limiting_device_sequence_item import (
    EnhancedRTBeamLimitingDeviceSequenceItem,
)
from .general_accessory_sequence_item import GeneralAccessorySequenceItem
from .planned_verification_image_sequence_item import (
    PlannedVerificationImageSequenceItem,
)
from .primary_fluence_mode_sequence_item import PrimaryFluenceModeSequenceItem
from .referenced_bolus_sequence_item import ReferencedBolusSequenceItem
from .referenced_dose_reference_sequence_item import ReferencedDoseReferenceSequenceItem
from .referenced_dose_sequence_item import ReferencedDoseSequenceItem
from .referenced_reference_image_sequence_item import (
    ReferencedReferenceImageSequenceItem,
)
from .wedge_sequence_item import WedgeSequenceItem


class BeamSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._InstitutionalDepartmentTypeCodeSequence: List[CodeSequenceItem] = []
        self._DefinitionSourceSequence: List[DefinitionSourceSequenceItem] = []
        self._PrimaryFluenceModeSequence: List[PrimaryFluenceModeSequenceItem] = []
        self._EnhancedRTBeamLimitingDeviceSequence: List[EnhancedRTBeamLimitingDeviceSequenceItem] = []
        self._BeamLimitingDeviceSequence: List[BeamLimitingDeviceSequenceItem] = []
        self._PlannedVerificationImageSequence: List[PlannedVerificationImageSequenceItem] = []
        self._WedgeSequence: List[WedgeSequenceItem] = []
        self._CompensatorSequence: List[CompensatorSequenceItem] = []
        self._BlockSequence: List[BlockSequenceItem] = []
        self._ApplicatorSequence: List[ApplicatorSequenceItem] = []
        self._ControlPointSequence: List[ControlPointSequenceItem] = []
        self._GeneralAccessorySequence: List[GeneralAccessorySequenceItem] = []
        self._ReferencedReferenceImageSequence: List[ReferencedReferenceImageSequenceItem] = []
        self._ReferencedDoseReferenceSequence: List[ReferencedDoseReferenceSequenceItem] = []
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
            raise ValueError(f"InstitutionalDepartmentTypeCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._InstitutionalDepartmentTypeCodeSequence = value
            if "InstitutionalDepartmentTypeCodeSequence" not in self._dataset:
                self._dataset.InstitutionalDepartmentTypeCodeSequence = pydicom.Sequence()
            self._dataset.InstitutionalDepartmentTypeCodeSequence.clear()
            self._dataset.InstitutionalDepartmentTypeCodeSequence.extend([item.to_dataset() for item in value])

    def add_InstitutionalDepartmentTypeCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError(f"Item must be an instance of CodeSequenceItem")
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
    def DefinitionSourceSequence(self) -> Optional[List[DefinitionSourceSequenceItem]]:
        if "DefinitionSourceSequence" in self._dataset:
            if len(self._DefinitionSourceSequence) == len(self._dataset.DefinitionSourceSequence):
                return self._DefinitionSourceSequence
            else:
                return [DefinitionSourceSequenceItem(x) for x in self._dataset.DefinitionSourceSequence]
        return None

    @DefinitionSourceSequence.setter
    def DefinitionSourceSequence(self, value: Optional[List[DefinitionSourceSequenceItem]]):
        if value is None:
            self._DefinitionSourceSequence = []
            if "DefinitionSourceSequence" in self._dataset:
                del self._dataset.DefinitionSourceSequence
        elif not isinstance(value, list) or not all(isinstance(item, DefinitionSourceSequenceItem) for item in value):
            raise ValueError(f"DefinitionSourceSequence must be a list of DefinitionSourceSequenceItem objects")
        else:
            self._DefinitionSourceSequence = value
            if "DefinitionSourceSequence" not in self._dataset:
                self._dataset.DefinitionSourceSequence = pydicom.Sequence()
            self._dataset.DefinitionSourceSequence.clear()
            self._dataset.DefinitionSourceSequence.extend([item.to_dataset() for item in value])

    def add_DefinitionSource(self, item: DefinitionSourceSequenceItem):
        if not isinstance(item, DefinitionSourceSequenceItem):
            raise ValueError(f"Item must be an instance of DefinitionSourceSequenceItem")
        self._DefinitionSourceSequence.append(item)
        if "DefinitionSourceSequence" not in self._dataset:
            self._dataset.DefinitionSourceSequence = pydicom.Sequence()
        self._dataset.DefinitionSourceSequence.append(item.to_dataset())

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
    def PrimaryFluenceModeSequence(self) -> Optional[List[PrimaryFluenceModeSequenceItem]]:
        if "PrimaryFluenceModeSequence" in self._dataset:
            if len(self._PrimaryFluenceModeSequence) == len(self._dataset.PrimaryFluenceModeSequence):
                return self._PrimaryFluenceModeSequence
            else:
                return [PrimaryFluenceModeSequenceItem(x) for x in self._dataset.PrimaryFluenceModeSequence]
        return None

    @PrimaryFluenceModeSequence.setter
    def PrimaryFluenceModeSequence(self, value: Optional[List[PrimaryFluenceModeSequenceItem]]):
        if value is None:
            self._PrimaryFluenceModeSequence = []
            if "PrimaryFluenceModeSequence" in self._dataset:
                del self._dataset.PrimaryFluenceModeSequence
        elif not isinstance(value, list) or not all(isinstance(item, PrimaryFluenceModeSequenceItem) for item in value):
            raise ValueError(f"PrimaryFluenceModeSequence must be a list of PrimaryFluenceModeSequenceItem objects")
        else:
            self._PrimaryFluenceModeSequence = value
            if "PrimaryFluenceModeSequence" not in self._dataset:
                self._dataset.PrimaryFluenceModeSequence = pydicom.Sequence()
            self._dataset.PrimaryFluenceModeSequence.clear()
            self._dataset.PrimaryFluenceModeSequence.extend([item.to_dataset() for item in value])

    def add_PrimaryFluenceMode(self, item: PrimaryFluenceModeSequenceItem):
        if not isinstance(item, PrimaryFluenceModeSequenceItem):
            raise ValueError(f"Item must be an instance of PrimaryFluenceModeSequenceItem")
        self._PrimaryFluenceModeSequence.append(item)
        if "PrimaryFluenceModeSequence" not in self._dataset:
            self._dataset.PrimaryFluenceModeSequence = pydicom.Sequence()
        self._dataset.PrimaryFluenceModeSequence.append(item.to_dataset())

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
                f"EnhancedRTBeamLimitingDeviceSequence must be a list of EnhancedRTBeamLimitingDeviceSequenceItem objects"
            )
        else:
            self._EnhancedRTBeamLimitingDeviceSequence = value
            if "EnhancedRTBeamLimitingDeviceSequence" not in self._dataset:
                self._dataset.EnhancedRTBeamLimitingDeviceSequence = pydicom.Sequence()
            self._dataset.EnhancedRTBeamLimitingDeviceSequence.clear()
            self._dataset.EnhancedRTBeamLimitingDeviceSequence.extend([item.to_dataset() for item in value])

    def add_EnhancedRTBeamLimitingDevice(self, item: EnhancedRTBeamLimitingDeviceSequenceItem):
        if not isinstance(item, EnhancedRTBeamLimitingDeviceSequenceItem):
            raise ValueError(f"Item must be an instance of EnhancedRTBeamLimitingDeviceSequenceItem")
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
    def SourceAxisDistance(self) -> Optional[Decimal]:
        if "SourceAxisDistance" in self._dataset:
            return self._dataset.SourceAxisDistance
        return None

    @SourceAxisDistance.setter
    def SourceAxisDistance(self, value: Optional[Decimal]):
        if value is None:
            if "SourceAxisDistance" in self._dataset:
                del self._dataset.SourceAxisDistance
        else:
            self._dataset.SourceAxisDistance = value

    @property
    def BeamLimitingDeviceSequence(self) -> Optional[List[BeamLimitingDeviceSequenceItem]]:
        if "BeamLimitingDeviceSequence" in self._dataset:
            if len(self._BeamLimitingDeviceSequence) == len(self._dataset.BeamLimitingDeviceSequence):
                return self._BeamLimitingDeviceSequence
            else:
                return [BeamLimitingDeviceSequenceItem(x) for x in self._dataset.BeamLimitingDeviceSequence]
        return None

    @BeamLimitingDeviceSequence.setter
    def BeamLimitingDeviceSequence(self, value: Optional[List[BeamLimitingDeviceSequenceItem]]):
        if value is None:
            self._BeamLimitingDeviceSequence = []
            if "BeamLimitingDeviceSequence" in self._dataset:
                del self._dataset.BeamLimitingDeviceSequence
        elif not isinstance(value, list) or not all(isinstance(item, BeamLimitingDeviceSequenceItem) for item in value):
            raise ValueError(f"BeamLimitingDeviceSequence must be a list of BeamLimitingDeviceSequenceItem objects")
        else:
            self._BeamLimitingDeviceSequence = value
            if "BeamLimitingDeviceSequence" not in self._dataset:
                self._dataset.BeamLimitingDeviceSequence = pydicom.Sequence()
            self._dataset.BeamLimitingDeviceSequence.clear()
            self._dataset.BeamLimitingDeviceSequence.extend([item.to_dataset() for item in value])

    def add_BeamLimitingDevice(self, item: BeamLimitingDeviceSequenceItem):
        if not isinstance(item, BeamLimitingDeviceSequenceItem):
            raise ValueError(f"Item must be an instance of BeamLimitingDeviceSequenceItem")
        self._BeamLimitingDeviceSequence.append(item)
        if "BeamLimitingDeviceSequence" not in self._dataset:
            self._dataset.BeamLimitingDeviceSequence = pydicom.Sequence()
        self._dataset.BeamLimitingDeviceSequence.append(item.to_dataset())

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
    def HighDoseTechniqueType(self) -> Optional[str]:
        if "HighDoseTechniqueType" in self._dataset:
            return self._dataset.HighDoseTechniqueType
        return None

    @HighDoseTechniqueType.setter
    def HighDoseTechniqueType(self, value: Optional[str]):
        if value is None:
            if "HighDoseTechniqueType" in self._dataset:
                del self._dataset.HighDoseTechniqueType
        else:
            self._dataset.HighDoseTechniqueType = value

    @property
    def PlannedVerificationImageSequence(self) -> Optional[List[PlannedVerificationImageSequenceItem]]:
        if "PlannedVerificationImageSequence" in self._dataset:
            if len(self._PlannedVerificationImageSequence) == len(self._dataset.PlannedVerificationImageSequence):
                return self._PlannedVerificationImageSequence
            else:
                return [PlannedVerificationImageSequenceItem(x) for x in self._dataset.PlannedVerificationImageSequence]
        return None

    @PlannedVerificationImageSequence.setter
    def PlannedVerificationImageSequence(self, value: Optional[List[PlannedVerificationImageSequenceItem]]):
        if value is None:
            self._PlannedVerificationImageSequence = []
            if "PlannedVerificationImageSequence" in self._dataset:
                del self._dataset.PlannedVerificationImageSequence
        elif not isinstance(value, list) or not all(isinstance(item, PlannedVerificationImageSequenceItem) for item in value):
            raise ValueError(
                f"PlannedVerificationImageSequence must be a list of PlannedVerificationImageSequenceItem objects"
            )
        else:
            self._PlannedVerificationImageSequence = value
            if "PlannedVerificationImageSequence" not in self._dataset:
                self._dataset.PlannedVerificationImageSequence = pydicom.Sequence()
            self._dataset.PlannedVerificationImageSequence.clear()
            self._dataset.PlannedVerificationImageSequence.extend([item.to_dataset() for item in value])

    def add_PlannedVerificationImage(self, item: PlannedVerificationImageSequenceItem):
        if not isinstance(item, PlannedVerificationImageSequenceItem):
            raise ValueError(f"Item must be an instance of PlannedVerificationImageSequenceItem")
        self._PlannedVerificationImageSequence.append(item)
        if "PlannedVerificationImageSequence" not in self._dataset:
            self._dataset.PlannedVerificationImageSequence = pydicom.Sequence()
        self._dataset.PlannedVerificationImageSequence.append(item.to_dataset())

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
    def WedgeSequence(self) -> Optional[List[WedgeSequenceItem]]:
        if "WedgeSequence" in self._dataset:
            if len(self._WedgeSequence) == len(self._dataset.WedgeSequence):
                return self._WedgeSequence
            else:
                return [WedgeSequenceItem(x) for x in self._dataset.WedgeSequence]
        return None

    @WedgeSequence.setter
    def WedgeSequence(self, value: Optional[List[WedgeSequenceItem]]):
        if value is None:
            self._WedgeSequence = []
            if "WedgeSequence" in self._dataset:
                del self._dataset.WedgeSequence
        elif not isinstance(value, list) or not all(isinstance(item, WedgeSequenceItem) for item in value):
            raise ValueError(f"WedgeSequence must be a list of WedgeSequenceItem objects")
        else:
            self._WedgeSequence = value
            if "WedgeSequence" not in self._dataset:
                self._dataset.WedgeSequence = pydicom.Sequence()
            self._dataset.WedgeSequence.clear()
            self._dataset.WedgeSequence.extend([item.to_dataset() for item in value])

    def add_Wedge(self, item: WedgeSequenceItem):
        if not isinstance(item, WedgeSequenceItem):
            raise ValueError(f"Item must be an instance of WedgeSequenceItem")
        self._WedgeSequence.append(item)
        if "WedgeSequence" not in self._dataset:
            self._dataset.WedgeSequence = pydicom.Sequence()
        self._dataset.WedgeSequence.append(item.to_dataset())

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
    def TotalCompensatorTrayFactor(self) -> Optional[Decimal]:
        if "TotalCompensatorTrayFactor" in self._dataset:
            return self._dataset.TotalCompensatorTrayFactor
        return None

    @TotalCompensatorTrayFactor.setter
    def TotalCompensatorTrayFactor(self, value: Optional[Decimal]):
        if value is None:
            if "TotalCompensatorTrayFactor" in self._dataset:
                del self._dataset.TotalCompensatorTrayFactor
        else:
            self._dataset.TotalCompensatorTrayFactor = value

    @property
    def CompensatorSequence(self) -> Optional[List[CompensatorSequenceItem]]:
        if "CompensatorSequence" in self._dataset:
            if len(self._CompensatorSequence) == len(self._dataset.CompensatorSequence):
                return self._CompensatorSequence
            else:
                return [CompensatorSequenceItem(x) for x in self._dataset.CompensatorSequence]
        return None

    @CompensatorSequence.setter
    def CompensatorSequence(self, value: Optional[List[CompensatorSequenceItem]]):
        if value is None:
            self._CompensatorSequence = []
            if "CompensatorSequence" in self._dataset:
                del self._dataset.CompensatorSequence
        elif not isinstance(value, list) or not all(isinstance(item, CompensatorSequenceItem) for item in value):
            raise ValueError(f"CompensatorSequence must be a list of CompensatorSequenceItem objects")
        else:
            self._CompensatorSequence = value
            if "CompensatorSequence" not in self._dataset:
                self._dataset.CompensatorSequence = pydicom.Sequence()
            self._dataset.CompensatorSequence.clear()
            self._dataset.CompensatorSequence.extend([item.to_dataset() for item in value])

    def add_Compensator(self, item: CompensatorSequenceItem):
        if not isinstance(item, CompensatorSequenceItem):
            raise ValueError(f"Item must be an instance of CompensatorSequenceItem")
        self._CompensatorSequence.append(item)
        if "CompensatorSequence" not in self._dataset:
            self._dataset.CompensatorSequence = pydicom.Sequence()
        self._dataset.CompensatorSequence.append(item.to_dataset())

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
    def TotalBlockTrayFactor(self) -> Optional[Decimal]:
        if "TotalBlockTrayFactor" in self._dataset:
            return self._dataset.TotalBlockTrayFactor
        return None

    @TotalBlockTrayFactor.setter
    def TotalBlockTrayFactor(self, value: Optional[Decimal]):
        if value is None:
            if "TotalBlockTrayFactor" in self._dataset:
                del self._dataset.TotalBlockTrayFactor
        else:
            self._dataset.TotalBlockTrayFactor = value

    @property
    def BlockSequence(self) -> Optional[List[BlockSequenceItem]]:
        if "BlockSequence" in self._dataset:
            if len(self._BlockSequence) == len(self._dataset.BlockSequence):
                return self._BlockSequence
            else:
                return [BlockSequenceItem(x) for x in self._dataset.BlockSequence]
        return None

    @BlockSequence.setter
    def BlockSequence(self, value: Optional[List[BlockSequenceItem]]):
        if value is None:
            self._BlockSequence = []
            if "BlockSequence" in self._dataset:
                del self._dataset.BlockSequence
        elif not isinstance(value, list) or not all(isinstance(item, BlockSequenceItem) for item in value):
            raise ValueError(f"BlockSequence must be a list of BlockSequenceItem objects")
        else:
            self._BlockSequence = value
            if "BlockSequence" not in self._dataset:
                self._dataset.BlockSequence = pydicom.Sequence()
            self._dataset.BlockSequence.clear()
            self._dataset.BlockSequence.extend([item.to_dataset() for item in value])

    def add_Block(self, item: BlockSequenceItem):
        if not isinstance(item, BlockSequenceItem):
            raise ValueError(f"Item must be an instance of BlockSequenceItem")
        self._BlockSequence.append(item)
        if "BlockSequence" not in self._dataset:
            self._dataset.BlockSequence = pydicom.Sequence()
        self._dataset.BlockSequence.append(item.to_dataset())

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
            raise ValueError(f"ApplicatorSequence must be a list of ApplicatorSequenceItem objects")
        else:
            self._ApplicatorSequence = value
            if "ApplicatorSequence" not in self._dataset:
                self._dataset.ApplicatorSequence = pydicom.Sequence()
            self._dataset.ApplicatorSequence.clear()
            self._dataset.ApplicatorSequence.extend([item.to_dataset() for item in value])

    def add_Applicator(self, item: ApplicatorSequenceItem):
        if not isinstance(item, ApplicatorSequenceItem):
            raise ValueError(f"Item must be an instance of ApplicatorSequenceItem")
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
    def ControlPointSequence(self) -> Optional[List[ControlPointSequenceItem]]:
        if "ControlPointSequence" in self._dataset:
            if len(self._ControlPointSequence) == len(self._dataset.ControlPointSequence):
                return self._ControlPointSequence
            else:
                return [ControlPointSequenceItem(x) for x in self._dataset.ControlPointSequence]
        return None

    @ControlPointSequence.setter
    def ControlPointSequence(self, value: Optional[List[ControlPointSequenceItem]]):
        if value is None:
            self._ControlPointSequence = []
            if "ControlPointSequence" in self._dataset:
                del self._dataset.ControlPointSequence
        elif not isinstance(value, list) or not all(isinstance(item, ControlPointSequenceItem) for item in value):
            raise ValueError(f"ControlPointSequence must be a list of ControlPointSequenceItem objects")
        else:
            self._ControlPointSequence = value
            if "ControlPointSequence" not in self._dataset:
                self._dataset.ControlPointSequence = pydicom.Sequence()
            self._dataset.ControlPointSequence.clear()
            self._dataset.ControlPointSequence.extend([item.to_dataset() for item in value])

    def add_ControlPoint(self, item: ControlPointSequenceItem):
        if not isinstance(item, ControlPointSequenceItem):
            raise ValueError(f"Item must be an instance of ControlPointSequenceItem")
        self._ControlPointSequence.append(item)
        if "ControlPointSequence" not in self._dataset:
            self._dataset.ControlPointSequence = pydicom.Sequence()
        self._dataset.ControlPointSequence.append(item.to_dataset())

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
            raise ValueError(f"GeneralAccessorySequence must be a list of GeneralAccessorySequenceItem objects")
        else:
            self._GeneralAccessorySequence = value
            if "GeneralAccessorySequence" not in self._dataset:
                self._dataset.GeneralAccessorySequence = pydicom.Sequence()
            self._dataset.GeneralAccessorySequence.clear()
            self._dataset.GeneralAccessorySequence.extend([item.to_dataset() for item in value])

    def add_GeneralAccessory(self, item: GeneralAccessorySequenceItem):
        if not isinstance(item, GeneralAccessorySequenceItem):
            raise ValueError(f"Item must be an instance of GeneralAccessorySequenceItem")
        self._GeneralAccessorySequence.append(item)
        if "GeneralAccessorySequence" not in self._dataset:
            self._dataset.GeneralAccessorySequence = pydicom.Sequence()
        self._dataset.GeneralAccessorySequence.append(item.to_dataset())

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
            raise ValueError(
                f"ReferencedReferenceImageSequence must be a list of ReferencedReferenceImageSequenceItem objects"
            )
        else:
            self._ReferencedReferenceImageSequence = value
            if "ReferencedReferenceImageSequence" not in self._dataset:
                self._dataset.ReferencedReferenceImageSequence = pydicom.Sequence()
            self._dataset.ReferencedReferenceImageSequence.clear()
            self._dataset.ReferencedReferenceImageSequence.extend([item.to_dataset() for item in value])

    def add_ReferencedReferenceImage(self, item: ReferencedReferenceImageSequenceItem):
        if not isinstance(item, ReferencedReferenceImageSequenceItem):
            raise ValueError(f"Item must be an instance of ReferencedReferenceImageSequenceItem")
        self._ReferencedReferenceImageSequence.append(item)
        if "ReferencedReferenceImageSequence" not in self._dataset:
            self._dataset.ReferencedReferenceImageSequence = pydicom.Sequence()
        self._dataset.ReferencedReferenceImageSequence.append(item.to_dataset())

    @property
    def ReferencedDoseReferenceSequence(self) -> Optional[List[ReferencedDoseReferenceSequenceItem]]:
        if "ReferencedDoseReferenceSequence" in self._dataset:
            if len(self._ReferencedDoseReferenceSequence) == len(self._dataset.ReferencedDoseReferenceSequence):
                return self._ReferencedDoseReferenceSequence
            else:
                return [ReferencedDoseReferenceSequenceItem(x) for x in self._dataset.ReferencedDoseReferenceSequence]
        return None

    @ReferencedDoseReferenceSequence.setter
    def ReferencedDoseReferenceSequence(self, value: Optional[List[ReferencedDoseReferenceSequenceItem]]):
        if value is None:
            self._ReferencedDoseReferenceSequence = []
            if "ReferencedDoseReferenceSequence" in self._dataset:
                del self._dataset.ReferencedDoseReferenceSequence
        elif not isinstance(value, list) or not all(isinstance(item, ReferencedDoseReferenceSequenceItem) for item in value):
            raise ValueError(f"ReferencedDoseReferenceSequence must be a list of ReferencedDoseReferenceSequenceItem objects")
        else:
            self._ReferencedDoseReferenceSequence = value
            if "ReferencedDoseReferenceSequence" not in self._dataset:
                self._dataset.ReferencedDoseReferenceSequence = pydicom.Sequence()
            self._dataset.ReferencedDoseReferenceSequence.clear()
            self._dataset.ReferencedDoseReferenceSequence.extend([item.to_dataset() for item in value])

    def add_ReferencedDoseReference(self, item: ReferencedDoseReferenceSequenceItem):
        if not isinstance(item, ReferencedDoseReferenceSequenceItem):
            raise ValueError(f"Item must be an instance of ReferencedDoseReferenceSequenceItem")
        self._ReferencedDoseReferenceSequence.append(item)
        if "ReferencedDoseReferenceSequence" not in self._dataset:
            self._dataset.ReferencedDoseReferenceSequence = pydicom.Sequence()
        self._dataset.ReferencedDoseReferenceSequence.append(item.to_dataset())

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
            raise ValueError(f"ReferencedDoseSequence must be a list of ReferencedDoseSequenceItem objects")
        else:
            self._ReferencedDoseSequence = value
            if "ReferencedDoseSequence" not in self._dataset:
                self._dataset.ReferencedDoseSequence = pydicom.Sequence()
            self._dataset.ReferencedDoseSequence.clear()
            self._dataset.ReferencedDoseSequence.extend([item.to_dataset() for item in value])

    def add_ReferencedDose(self, item: ReferencedDoseSequenceItem):
        if not isinstance(item, ReferencedDoseSequenceItem):
            raise ValueError(f"Item must be an instance of ReferencedDoseSequenceItem")
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
            raise ValueError(f"ReferencedBolusSequence must be a list of ReferencedBolusSequenceItem objects")
        else:
            self._ReferencedBolusSequence = value
            if "ReferencedBolusSequence" not in self._dataset:
                self._dataset.ReferencedBolusSequence = pydicom.Sequence()
            self._dataset.ReferencedBolusSequence.clear()
            self._dataset.ReferencedBolusSequence.extend([item.to_dataset() for item in value])

    def add_ReferencedBolus(self, item: ReferencedBolusSequenceItem):
        if not isinstance(item, ReferencedBolusSequenceItem):
            raise ValueError(f"Item must be an instance of ReferencedBolusSequenceItem")
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
