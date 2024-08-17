from decimal import Decimal
from typing import Any, List, Optional  # noqa

import pydicom

from .applicator_sequence_item import ApplicatorSequenceItem
from .beam_limiting_device_sequence_item import BeamLimitingDeviceSequenceItem
from .block_sequence_item import BlockSequenceItem
from .enhanced_rt_beam_limiting_opening_sequence_item import (
    EnhancedRTBeamLimitingOpeningSequenceItem,
)
from .general_accessory_sequence_item import GeneralAccessorySequenceItem
from .primary_fluence_mode_sequence_item import PrimaryFluenceModeSequenceItem


class ExposureSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._PrimaryFluenceModeSequence: List[PrimaryFluenceModeSequenceItem] = []
        self._EnhancedRTBeamLimitingOpeningSequence: List[EnhancedRTBeamLimitingOpeningSequenceItem] = []
        self._BeamLimitingDeviceSequence: List[BeamLimitingDeviceSequenceItem] = []
        self._BlockSequence: List[BlockSequenceItem] = []
        self._ApplicatorSequence: List[ApplicatorSequenceItem] = []
        self._GeneralAccessorySequence: List[GeneralAccessorySequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ReferencedFrameNumber(self) -> Optional[List[int]]:
        if "ReferencedFrameNumber" in self._dataset:
            return self._dataset.ReferencedFrameNumber
        return None

    @ReferencedFrameNumber.setter
    def ReferencedFrameNumber(self, value: Optional[List[int]]):
        if value is None:
            if "ReferencedFrameNumber" in self._dataset:
                del self._dataset.ReferencedFrameNumber
        else:
            self._dataset.ReferencedFrameNumber = value

    @property
    def KVP(self) -> Optional[Decimal]:
        if "KVP" in self._dataset:
            return self._dataset.KVP
        return None

    @KVP.setter
    def KVP(self, value: Optional[Decimal]):
        if value is None:
            if "KVP" in self._dataset:
                del self._dataset.KVP
        else:
            self._dataset.KVP = value

    @property
    def ExposureTime(self) -> Optional[int]:
        if "ExposureTime" in self._dataset:
            return self._dataset.ExposureTime
        return None

    @ExposureTime.setter
    def ExposureTime(self, value: Optional[int]):
        if value is None:
            if "ExposureTime" in self._dataset:
                del self._dataset.ExposureTime
        else:
            self._dataset.ExposureTime = value

    @property
    def XRayTubeCurrent(self) -> Optional[int]:
        if "XRayTubeCurrent" in self._dataset:
            return self._dataset.XRayTubeCurrent
        return None

    @XRayTubeCurrent.setter
    def XRayTubeCurrent(self, value: Optional[int]):
        if value is None:
            if "XRayTubeCurrent" in self._dataset:
                del self._dataset.XRayTubeCurrent
        else:
            self._dataset.XRayTubeCurrent = value

    @property
    def ExposureTimeInms(self) -> Optional[float]:
        if "ExposureTimeInms" in self._dataset:
            return self._dataset.ExposureTimeInms
        return None

    @ExposureTimeInms.setter
    def ExposureTimeInms(self, value: Optional[float]):
        if value is None:
            if "ExposureTimeInms" in self._dataset:
                del self._dataset.ExposureTimeInms
        else:
            self._dataset.ExposureTimeInms = value

    @property
    def XRayTubeCurrentInmA(self) -> Optional[float]:
        if "XRayTubeCurrentInmA" in self._dataset:
            return self._dataset.XRayTubeCurrentInmA
        return None

    @XRayTubeCurrentInmA.setter
    def XRayTubeCurrentInmA(self, value: Optional[float]):
        if value is None:
            if "XRayTubeCurrentInmA" in self._dataset:
                del self._dataset.XRayTubeCurrentInmA
        else:
            self._dataset.XRayTubeCurrentInmA = value

    @property
    def MetersetExposure(self) -> Optional[Decimal]:
        if "MetersetExposure" in self._dataset:
            return self._dataset.MetersetExposure
        return None

    @MetersetExposure.setter
    def MetersetExposure(self, value: Optional[Decimal]):
        if value is None:
            if "MetersetExposure" in self._dataset:
                del self._dataset.MetersetExposure
        else:
            self._dataset.MetersetExposure = value

    @property
    def DiaphragmPosition(self) -> Optional[List[Decimal]]:
        if "DiaphragmPosition" in self._dataset:
            return self._dataset.DiaphragmPosition
        return None

    @DiaphragmPosition.setter
    def DiaphragmPosition(self, value: Optional[List[Decimal]]):
        if value is None:
            if "DiaphragmPosition" in self._dataset:
                del self._dataset.DiaphragmPosition
        else:
            self._dataset.DiaphragmPosition = value

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
            raise ValueError("PrimaryFluenceModeSequence must be a list of PrimaryFluenceModeSequenceItem objects")
        else:
            self._PrimaryFluenceModeSequence = value
            if "PrimaryFluenceModeSequence" not in self._dataset:
                self._dataset.PrimaryFluenceModeSequence = pydicom.Sequence()
            self._dataset.PrimaryFluenceModeSequence.clear()
            self._dataset.PrimaryFluenceModeSequence.extend([item.to_dataset() for item in value])

    def add_PrimaryFluenceMode(self, item: PrimaryFluenceModeSequenceItem):
        if not isinstance(item, PrimaryFluenceModeSequenceItem):
            raise ValueError("Item must be an instance of PrimaryFluenceModeSequenceItem")
        self._PrimaryFluenceModeSequence.append(item)
        if "PrimaryFluenceModeSequence" not in self._dataset:
            self._dataset.PrimaryFluenceModeSequence = pydicom.Sequence()
        self._dataset.PrimaryFluenceModeSequence.append(item.to_dataset())

    @property
    def EnhancedRTBeamLimitingOpeningSequence(self) -> Optional[List[EnhancedRTBeamLimitingOpeningSequenceItem]]:
        if "EnhancedRTBeamLimitingOpeningSequence" in self._dataset:
            if len(self._EnhancedRTBeamLimitingOpeningSequence) == len(self._dataset.EnhancedRTBeamLimitingOpeningSequence):
                return self._EnhancedRTBeamLimitingOpeningSequence
            else:
                return [
                    EnhancedRTBeamLimitingOpeningSequenceItem(x) for x in self._dataset.EnhancedRTBeamLimitingOpeningSequence
                ]
        return None

    @EnhancedRTBeamLimitingOpeningSequence.setter
    def EnhancedRTBeamLimitingOpeningSequence(self, value: Optional[List[EnhancedRTBeamLimitingOpeningSequenceItem]]):
        if value is None:
            self._EnhancedRTBeamLimitingOpeningSequence = []
            if "EnhancedRTBeamLimitingOpeningSequence" in self._dataset:
                del self._dataset.EnhancedRTBeamLimitingOpeningSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, EnhancedRTBeamLimitingOpeningSequenceItem) for item in value
        ):
            raise ValueError(
                "EnhancedRTBeamLimitingOpeningSequence must be a list of EnhancedRTBeamLimitingOpeningSequenceItem objects"
            )
        else:
            self._EnhancedRTBeamLimitingOpeningSequence = value
            if "EnhancedRTBeamLimitingOpeningSequence" not in self._dataset:
                self._dataset.EnhancedRTBeamLimitingOpeningSequence = pydicom.Sequence()
            self._dataset.EnhancedRTBeamLimitingOpeningSequence.clear()
            self._dataset.EnhancedRTBeamLimitingOpeningSequence.extend([item.to_dataset() for item in value])

    def add_EnhancedRTBeamLimitingOpening(self, item: EnhancedRTBeamLimitingOpeningSequenceItem):
        if not isinstance(item, EnhancedRTBeamLimitingOpeningSequenceItem):
            raise ValueError("Item must be an instance of EnhancedRTBeamLimitingOpeningSequenceItem")
        self._EnhancedRTBeamLimitingOpeningSequence.append(item)
        if "EnhancedRTBeamLimitingOpeningSequence" not in self._dataset:
            self._dataset.EnhancedRTBeamLimitingOpeningSequence = pydicom.Sequence()
        self._dataset.EnhancedRTBeamLimitingOpeningSequence.append(item.to_dataset())

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
            raise ValueError("BeamLimitingDeviceSequence must be a list of BeamLimitingDeviceSequenceItem objects")
        else:
            self._BeamLimitingDeviceSequence = value
            if "BeamLimitingDeviceSequence" not in self._dataset:
                self._dataset.BeamLimitingDeviceSequence = pydicom.Sequence()
            self._dataset.BeamLimitingDeviceSequence.clear()
            self._dataset.BeamLimitingDeviceSequence.extend([item.to_dataset() for item in value])

    def add_BeamLimitingDevice(self, item: BeamLimitingDeviceSequenceItem):
        if not isinstance(item, BeamLimitingDeviceSequenceItem):
            raise ValueError("Item must be an instance of BeamLimitingDeviceSequenceItem")
        self._BeamLimitingDeviceSequence.append(item)
        if "BeamLimitingDeviceSequence" not in self._dataset:
            self._dataset.BeamLimitingDeviceSequence = pydicom.Sequence()
        self._dataset.BeamLimitingDeviceSequence.append(item.to_dataset())

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
            raise ValueError("BlockSequence must be a list of BlockSequenceItem objects")
        else:
            self._BlockSequence = value
            if "BlockSequence" not in self._dataset:
                self._dataset.BlockSequence = pydicom.Sequence()
            self._dataset.BlockSequence.clear()
            self._dataset.BlockSequence.extend([item.to_dataset() for item in value])

    def add_Block(self, item: BlockSequenceItem):
        if not isinstance(item, BlockSequenceItem):
            raise ValueError("Item must be an instance of BlockSequenceItem")
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
    def GantryAngle(self) -> Optional[Decimal]:
        if "GantryAngle" in self._dataset:
            return self._dataset.GantryAngle
        return None

    @GantryAngle.setter
    def GantryAngle(self, value: Optional[Decimal]):
        if value is None:
            if "GantryAngle" in self._dataset:
                del self._dataset.GantryAngle
        else:
            self._dataset.GantryAngle = value

    @property
    def BeamLimitingDeviceAngle(self) -> Optional[Decimal]:
        if "BeamLimitingDeviceAngle" in self._dataset:
            return self._dataset.BeamLimitingDeviceAngle
        return None

    @BeamLimitingDeviceAngle.setter
    def BeamLimitingDeviceAngle(self, value: Optional[Decimal]):
        if value is None:
            if "BeamLimitingDeviceAngle" in self._dataset:
                del self._dataset.BeamLimitingDeviceAngle
        else:
            self._dataset.BeamLimitingDeviceAngle = value

    @property
    def PatientSupportAngle(self) -> Optional[Decimal]:
        if "PatientSupportAngle" in self._dataset:
            return self._dataset.PatientSupportAngle
        return None

    @PatientSupportAngle.setter
    def PatientSupportAngle(self, value: Optional[Decimal]):
        if value is None:
            if "PatientSupportAngle" in self._dataset:
                del self._dataset.PatientSupportAngle
        else:
            self._dataset.PatientSupportAngle = value

    @property
    def TableTopVerticalPosition(self) -> Optional[Decimal]:
        if "TableTopVerticalPosition" in self._dataset:
            return self._dataset.TableTopVerticalPosition
        return None

    @TableTopVerticalPosition.setter
    def TableTopVerticalPosition(self, value: Optional[Decimal]):
        if value is None:
            if "TableTopVerticalPosition" in self._dataset:
                del self._dataset.TableTopVerticalPosition
        else:
            self._dataset.TableTopVerticalPosition = value

    @property
    def TableTopLongitudinalPosition(self) -> Optional[Decimal]:
        if "TableTopLongitudinalPosition" in self._dataset:
            return self._dataset.TableTopLongitudinalPosition
        return None

    @TableTopLongitudinalPosition.setter
    def TableTopLongitudinalPosition(self, value: Optional[Decimal]):
        if value is None:
            if "TableTopLongitudinalPosition" in self._dataset:
                del self._dataset.TableTopLongitudinalPosition
        else:
            self._dataset.TableTopLongitudinalPosition = value

    @property
    def TableTopLateralPosition(self) -> Optional[Decimal]:
        if "TableTopLateralPosition" in self._dataset:
            return self._dataset.TableTopLateralPosition
        return None

    @TableTopLateralPosition.setter
    def TableTopLateralPosition(self, value: Optional[Decimal]):
        if value is None:
            if "TableTopLateralPosition" in self._dataset:
                del self._dataset.TableTopLateralPosition
        else:
            self._dataset.TableTopLateralPosition = value

    @property
    def TableTopPitchAngle(self) -> Optional[float]:
        if "TableTopPitchAngle" in self._dataset:
            return self._dataset.TableTopPitchAngle
        return None

    @TableTopPitchAngle.setter
    def TableTopPitchAngle(self, value: Optional[float]):
        if value is None:
            if "TableTopPitchAngle" in self._dataset:
                del self._dataset.TableTopPitchAngle
        else:
            self._dataset.TableTopPitchAngle = value

    @property
    def TableTopRollAngle(self) -> Optional[float]:
        if "TableTopRollAngle" in self._dataset:
            return self._dataset.TableTopRollAngle
        return None

    @TableTopRollAngle.setter
    def TableTopRollAngle(self, value: Optional[float]):
        if value is None:
            if "TableTopRollAngle" in self._dataset:
                del self._dataset.TableTopRollAngle
        else:
            self._dataset.TableTopRollAngle = value

    @property
    def GantryPitchAngle(self) -> Optional[float]:
        if "GantryPitchAngle" in self._dataset:
            return self._dataset.GantryPitchAngle
        return None

    @GantryPitchAngle.setter
    def GantryPitchAngle(self, value: Optional[float]):
        if value is None:
            if "GantryPitchAngle" in self._dataset:
                del self._dataset.GantryPitchAngle
        else:
            self._dataset.GantryPitchAngle = value

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
