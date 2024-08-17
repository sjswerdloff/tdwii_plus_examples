from decimal import Decimal
from typing import Any, List, Optional

import pydicom

from .acquisition_end_location_sequence_item import AcquisitionEndLocationSequenceItem
from .acquisition_start_location_sequence_item import (
    AcquisitionStartLocationSequenceItem,
)
from .code_sequence_item import CodeSequenceItem
from .ctx_ray_details_sequence_item import CTXRayDetailsSequenceItem


class AcquisitionProtocolElementSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._RequestedSeriesDescriptionCodeSequence: List[CodeSequenceItem] = []
        self._CTXRayDetailsSequence: List[CTXRayDetailsSequenceItem] = []
        self._CTDIPhantomTypeCodeSequence: List[CodeSequenceItem] = []
        self._AcquisitionStartLocationSequence: List[AcquisitionStartLocationSequenceItem] = []
        self._AcquisitionEndLocationSequence: List[AcquisitionEndLocationSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def GantryDetectorTilt(self) -> Optional[Decimal]:
        if "GantryDetectorTilt" in self._dataset:
            return self._dataset.GantryDetectorTilt
        return None

    @GantryDetectorTilt.setter
    def GantryDetectorTilt(self, value: Optional[Decimal]):
        if value is None:
            if "GantryDetectorTilt" in self._dataset:
                del self._dataset.GantryDetectorTilt
        else:
            self._dataset.GantryDetectorTilt = value

    @property
    def TableHeight(self) -> Optional[Decimal]:
        if "TableHeight" in self._dataset:
            return self._dataset.TableHeight
        return None

    @TableHeight.setter
    def TableHeight(self, value: Optional[Decimal]):
        if value is None:
            if "TableHeight" in self._dataset:
                del self._dataset.TableHeight
        else:
            self._dataset.TableHeight = value

    @property
    def RequestedSeriesDescriptionCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "RequestedSeriesDescriptionCodeSequence" in self._dataset:
            if len(self._RequestedSeriesDescriptionCodeSequence) == len(self._dataset.RequestedSeriesDescriptionCodeSequence):
                return self._RequestedSeriesDescriptionCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.RequestedSeriesDescriptionCodeSequence]
        return None

    @RequestedSeriesDescriptionCodeSequence.setter
    def RequestedSeriesDescriptionCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._RequestedSeriesDescriptionCodeSequence = []
            if "RequestedSeriesDescriptionCodeSequence" in self._dataset:
                del self._dataset.RequestedSeriesDescriptionCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError(f"RequestedSeriesDescriptionCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._RequestedSeriesDescriptionCodeSequence = value
            if "RequestedSeriesDescriptionCodeSequence" not in self._dataset:
                self._dataset.RequestedSeriesDescriptionCodeSequence = pydicom.Sequence()
            self._dataset.RequestedSeriesDescriptionCodeSequence.clear()
            self._dataset.RequestedSeriesDescriptionCodeSequence.extend([item.to_dataset() for item in value])

    def add_RequestedSeriesDescriptionCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError(f"Item must be an instance of CodeSequenceItem")
        self._RequestedSeriesDescriptionCodeSequence.append(item)
        if "RequestedSeriesDescriptionCodeSequence" not in self._dataset:
            self._dataset.RequestedSeriesDescriptionCodeSequence = pydicom.Sequence()
        self._dataset.RequestedSeriesDescriptionCodeSequence.append(item.to_dataset())

    @property
    def ContentQualification(self) -> Optional[str]:
        if "ContentQualification" in self._dataset:
            return self._dataset.ContentQualification
        return None

    @ContentQualification.setter
    def ContentQualification(self, value: Optional[str]):
        if value is None:
            if "ContentQualification" in self._dataset:
                del self._dataset.ContentQualification
        else:
            self._dataset.ContentQualification = value

    @property
    def AcquisitionType(self) -> Optional[str]:
        if "AcquisitionType" in self._dataset:
            return self._dataset.AcquisitionType
        return None

    @AcquisitionType.setter
    def AcquisitionType(self, value: Optional[str]):
        if value is None:
            if "AcquisitionType" in self._dataset:
                del self._dataset.AcquisitionType
        else:
            self._dataset.AcquisitionType = value

    @property
    def TubeAngle(self) -> Optional[float]:
        if "TubeAngle" in self._dataset:
            return self._dataset.TubeAngle
        return None

    @TubeAngle.setter
    def TubeAngle(self, value: Optional[float]):
        if value is None:
            if "TubeAngle" in self._dataset:
                del self._dataset.TubeAngle
        else:
            self._dataset.TubeAngle = value

    @property
    def RevolutionTime(self) -> Optional[float]:
        if "RevolutionTime" in self._dataset:
            return self._dataset.RevolutionTime
        return None

    @RevolutionTime.setter
    def RevolutionTime(self, value: Optional[float]):
        if value is None:
            if "RevolutionTime" in self._dataset:
                del self._dataset.RevolutionTime
        else:
            self._dataset.RevolutionTime = value

    @property
    def SingleCollimationWidth(self) -> Optional[float]:
        if "SingleCollimationWidth" in self._dataset:
            return self._dataset.SingleCollimationWidth
        return None

    @SingleCollimationWidth.setter
    def SingleCollimationWidth(self, value: Optional[float]):
        if value is None:
            if "SingleCollimationWidth" in self._dataset:
                del self._dataset.SingleCollimationWidth
        else:
            self._dataset.SingleCollimationWidth = value

    @property
    def TotalCollimationWidth(self) -> Optional[float]:
        if "TotalCollimationWidth" in self._dataset:
            return self._dataset.TotalCollimationWidth
        return None

    @TotalCollimationWidth.setter
    def TotalCollimationWidth(self, value: Optional[float]):
        if value is None:
            if "TotalCollimationWidth" in self._dataset:
                del self._dataset.TotalCollimationWidth
        else:
            self._dataset.TotalCollimationWidth = value

    @property
    def TableSpeed(self) -> Optional[float]:
        if "TableSpeed" in self._dataset:
            return self._dataset.TableSpeed
        return None

    @TableSpeed.setter
    def TableSpeed(self, value: Optional[float]):
        if value is None:
            if "TableSpeed" in self._dataset:
                del self._dataset.TableSpeed
        else:
            self._dataset.TableSpeed = value

    @property
    def TableFeedPerRotation(self) -> Optional[float]:
        if "TableFeedPerRotation" in self._dataset:
            return self._dataset.TableFeedPerRotation
        return None

    @TableFeedPerRotation.setter
    def TableFeedPerRotation(self, value: Optional[float]):
        if value is None:
            if "TableFeedPerRotation" in self._dataset:
                del self._dataset.TableFeedPerRotation
        else:
            self._dataset.TableFeedPerRotation = value

    @property
    def SpiralPitchFactor(self) -> Optional[float]:
        if "SpiralPitchFactor" in self._dataset:
            return self._dataset.SpiralPitchFactor
        return None

    @SpiralPitchFactor.setter
    def SpiralPitchFactor(self, value: Optional[float]):
        if value is None:
            if "SpiralPitchFactor" in self._dataset:
                del self._dataset.SpiralPitchFactor
        else:
            self._dataset.SpiralPitchFactor = value

    @property
    def CTXRayDetailsSequence(self) -> Optional[List[CTXRayDetailsSequenceItem]]:
        if "CTXRayDetailsSequence" in self._dataset:
            if len(self._CTXRayDetailsSequence) == len(self._dataset.CTXRayDetailsSequence):
                return self._CTXRayDetailsSequence
            else:
                return [CTXRayDetailsSequenceItem(x) for x in self._dataset.CTXRayDetailsSequence]
        return None

    @CTXRayDetailsSequence.setter
    def CTXRayDetailsSequence(self, value: Optional[List[CTXRayDetailsSequenceItem]]):
        if value is None:
            self._CTXRayDetailsSequence = []
            if "CTXRayDetailsSequence" in self._dataset:
                del self._dataset.CTXRayDetailsSequence
        elif not isinstance(value, list) or not all(isinstance(item, CTXRayDetailsSequenceItem) for item in value):
            raise ValueError(f"CTXRayDetailsSequence must be a list of CTXRayDetailsSequenceItem objects")
        else:
            self._CTXRayDetailsSequence = value
            if "CTXRayDetailsSequence" not in self._dataset:
                self._dataset.CTXRayDetailsSequence = pydicom.Sequence()
            self._dataset.CTXRayDetailsSequence.clear()
            self._dataset.CTXRayDetailsSequence.extend([item.to_dataset() for item in value])

    def add_CTXRayDetails(self, item: CTXRayDetailsSequenceItem):
        if not isinstance(item, CTXRayDetailsSequenceItem):
            raise ValueError(f"Item must be an instance of CTXRayDetailsSequenceItem")
        self._CTXRayDetailsSequence.append(item)
        if "CTXRayDetailsSequence" not in self._dataset:
            self._dataset.CTXRayDetailsSequence = pydicom.Sequence()
        self._dataset.CTXRayDetailsSequence.append(item.to_dataset())

    @property
    def ConstantVolumeFlag(self) -> Optional[str]:
        if "ConstantVolumeFlag" in self._dataset:
            return self._dataset.ConstantVolumeFlag
        return None

    @ConstantVolumeFlag.setter
    def ConstantVolumeFlag(self, value: Optional[str]):
        if value is None:
            if "ConstantVolumeFlag" in self._dataset:
                del self._dataset.ConstantVolumeFlag
        else:
            self._dataset.ConstantVolumeFlag = value

    @property
    def FluoroscopyFlag(self) -> Optional[str]:
        if "FluoroscopyFlag" in self._dataset:
            return self._dataset.FluoroscopyFlag
        return None

    @FluoroscopyFlag.setter
    def FluoroscopyFlag(self, value: Optional[str]):
        if value is None:
            if "FluoroscopyFlag" in self._dataset:
                del self._dataset.FluoroscopyFlag
        else:
            self._dataset.FluoroscopyFlag = value

    @property
    def CTDIvol(self) -> Optional[float]:
        if "CTDIvol" in self._dataset:
            return self._dataset.CTDIvol
        return None

    @CTDIvol.setter
    def CTDIvol(self, value: Optional[float]):
        if value is None:
            if "CTDIvol" in self._dataset:
                del self._dataset.CTDIvol
        else:
            self._dataset.CTDIvol = value

    @property
    def CTDIPhantomTypeCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "CTDIPhantomTypeCodeSequence" in self._dataset:
            if len(self._CTDIPhantomTypeCodeSequence) == len(self._dataset.CTDIPhantomTypeCodeSequence):
                return self._CTDIPhantomTypeCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.CTDIPhantomTypeCodeSequence]
        return None

    @CTDIPhantomTypeCodeSequence.setter
    def CTDIPhantomTypeCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._CTDIPhantomTypeCodeSequence = []
            if "CTDIPhantomTypeCodeSequence" in self._dataset:
                del self._dataset.CTDIPhantomTypeCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError(f"CTDIPhantomTypeCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._CTDIPhantomTypeCodeSequence = value
            if "CTDIPhantomTypeCodeSequence" not in self._dataset:
                self._dataset.CTDIPhantomTypeCodeSequence = pydicom.Sequence()
            self._dataset.CTDIPhantomTypeCodeSequence.clear()
            self._dataset.CTDIPhantomTypeCodeSequence.extend([item.to_dataset() for item in value])

    def add_CTDIPhantomTypeCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError(f"Item must be an instance of CodeSequenceItem")
        self._CTDIPhantomTypeCodeSequence.append(item)
        if "CTDIPhantomTypeCodeSequence" not in self._dataset:
            self._dataset.CTDIPhantomTypeCodeSequence = pydicom.Sequence()
        self._dataset.CTDIPhantomTypeCodeSequence.append(item.to_dataset())

    @property
    def ProtocolElementNumber(self) -> Optional[int]:
        if "ProtocolElementNumber" in self._dataset:
            return self._dataset.ProtocolElementNumber
        return None

    @ProtocolElementNumber.setter
    def ProtocolElementNumber(self, value: Optional[int]):
        if value is None:
            if "ProtocolElementNumber" in self._dataset:
                del self._dataset.ProtocolElementNumber
        else:
            self._dataset.ProtocolElementNumber = value

    @property
    def ProtocolElementName(self) -> Optional[str]:
        if "ProtocolElementName" in self._dataset:
            return self._dataset.ProtocolElementName
        return None

    @ProtocolElementName.setter
    def ProtocolElementName(self, value: Optional[str]):
        if value is None:
            if "ProtocolElementName" in self._dataset:
                del self._dataset.ProtocolElementName
        else:
            self._dataset.ProtocolElementName = value

    @property
    def ProtocolElementCharacteristicsSummary(self) -> Optional[str]:
        if "ProtocolElementCharacteristicsSummary" in self._dataset:
            return self._dataset.ProtocolElementCharacteristicsSummary
        return None

    @ProtocolElementCharacteristicsSummary.setter
    def ProtocolElementCharacteristicsSummary(self, value: Optional[str]):
        if value is None:
            if "ProtocolElementCharacteristicsSummary" in self._dataset:
                del self._dataset.ProtocolElementCharacteristicsSummary
        else:
            self._dataset.ProtocolElementCharacteristicsSummary = value

    @property
    def ProtocolElementPurpose(self) -> Optional[str]:
        if "ProtocolElementPurpose" in self._dataset:
            return self._dataset.ProtocolElementPurpose
        return None

    @ProtocolElementPurpose.setter
    def ProtocolElementPurpose(self, value: Optional[str]):
        if value is None:
            if "ProtocolElementPurpose" in self._dataset:
                del self._dataset.ProtocolElementPurpose
        else:
            self._dataset.ProtocolElementPurpose = value

    @property
    def AcquisitionMotion(self) -> Optional[str]:
        if "AcquisitionMotion" in self._dataset:
            return self._dataset.AcquisitionMotion
        return None

    @AcquisitionMotion.setter
    def AcquisitionMotion(self, value: Optional[str]):
        if value is None:
            if "AcquisitionMotion" in self._dataset:
                del self._dataset.AcquisitionMotion
        else:
            self._dataset.AcquisitionMotion = value

    @property
    def AcquisitionStartLocationSequence(self) -> Optional[List[AcquisitionStartLocationSequenceItem]]:
        if "AcquisitionStartLocationSequence" in self._dataset:
            if len(self._AcquisitionStartLocationSequence) == len(self._dataset.AcquisitionStartLocationSequence):
                return self._AcquisitionStartLocationSequence
            else:
                return [AcquisitionStartLocationSequenceItem(x) for x in self._dataset.AcquisitionStartLocationSequence]
        return None

    @AcquisitionStartLocationSequence.setter
    def AcquisitionStartLocationSequence(self, value: Optional[List[AcquisitionStartLocationSequenceItem]]):
        if value is None:
            self._AcquisitionStartLocationSequence = []
            if "AcquisitionStartLocationSequence" in self._dataset:
                del self._dataset.AcquisitionStartLocationSequence
        elif not isinstance(value, list) or not all(isinstance(item, AcquisitionStartLocationSequenceItem) for item in value):
            raise ValueError(
                f"AcquisitionStartLocationSequence must be a list of AcquisitionStartLocationSequenceItem objects"
            )
        else:
            self._AcquisitionStartLocationSequence = value
            if "AcquisitionStartLocationSequence" not in self._dataset:
                self._dataset.AcquisitionStartLocationSequence = pydicom.Sequence()
            self._dataset.AcquisitionStartLocationSequence.clear()
            self._dataset.AcquisitionStartLocationSequence.extend([item.to_dataset() for item in value])

    def add_AcquisitionStartLocation(self, item: AcquisitionStartLocationSequenceItem):
        if not isinstance(item, AcquisitionStartLocationSequenceItem):
            raise ValueError(f"Item must be an instance of AcquisitionStartLocationSequenceItem")
        self._AcquisitionStartLocationSequence.append(item)
        if "AcquisitionStartLocationSequence" not in self._dataset:
            self._dataset.AcquisitionStartLocationSequence = pydicom.Sequence()
        self._dataset.AcquisitionStartLocationSequence.append(item.to_dataset())

    @property
    def AcquisitionEndLocationSequence(self) -> Optional[List[AcquisitionEndLocationSequenceItem]]:
        if "AcquisitionEndLocationSequence" in self._dataset:
            if len(self._AcquisitionEndLocationSequence) == len(self._dataset.AcquisitionEndLocationSequence):
                return self._AcquisitionEndLocationSequence
            else:
                return [AcquisitionEndLocationSequenceItem(x) for x in self._dataset.AcquisitionEndLocationSequence]
        return None

    @AcquisitionEndLocationSequence.setter
    def AcquisitionEndLocationSequence(self, value: Optional[List[AcquisitionEndLocationSequenceItem]]):
        if value is None:
            self._AcquisitionEndLocationSequence = []
            if "AcquisitionEndLocationSequence" in self._dataset:
                del self._dataset.AcquisitionEndLocationSequence
        elif not isinstance(value, list) or not all(isinstance(item, AcquisitionEndLocationSequenceItem) for item in value):
            raise ValueError(f"AcquisitionEndLocationSequence must be a list of AcquisitionEndLocationSequenceItem objects")
        else:
            self._AcquisitionEndLocationSequence = value
            if "AcquisitionEndLocationSequence" not in self._dataset:
                self._dataset.AcquisitionEndLocationSequence = pydicom.Sequence()
            self._dataset.AcquisitionEndLocationSequence.clear()
            self._dataset.AcquisitionEndLocationSequence.extend([item.to_dataset() for item in value])

    def add_AcquisitionEndLocation(self, item: AcquisitionEndLocationSequenceItem):
        if not isinstance(item, AcquisitionEndLocationSequenceItem):
            raise ValueError(f"Item must be an instance of AcquisitionEndLocationSequenceItem")
        self._AcquisitionEndLocationSequence.append(item)
        if "AcquisitionEndLocationSequence" not in self._dataset:
            self._dataset.AcquisitionEndLocationSequence = pydicom.Sequence()
        self._dataset.AcquisitionEndLocationSequence.append(item.to_dataset())

    @property
    def RequestedSeriesDescription(self) -> Optional[str]:
        if "RequestedSeriesDescription" in self._dataset:
            return self._dataset.RequestedSeriesDescription
        return None

    @RequestedSeriesDescription.setter
    def RequestedSeriesDescription(self, value: Optional[str]):
        if value is None:
            if "RequestedSeriesDescription" in self._dataset:
                del self._dataset.RequestedSeriesDescription
        else:
            self._dataset.RequestedSeriesDescription = value

    @property
    def CTDIvolNotificationTrigger(self) -> Optional[float]:
        if "CTDIvolNotificationTrigger" in self._dataset:
            return self._dataset.CTDIvolNotificationTrigger
        return None

    @CTDIvolNotificationTrigger.setter
    def CTDIvolNotificationTrigger(self, value: Optional[float]):
        if value is None:
            if "CTDIvolNotificationTrigger" in self._dataset:
                del self._dataset.CTDIvolNotificationTrigger
        else:
            self._dataset.CTDIvolNotificationTrigger = value

    @property
    def DLPNotificationTrigger(self) -> Optional[float]:
        if "DLPNotificationTrigger" in self._dataset:
            return self._dataset.DLPNotificationTrigger
        return None

    @DLPNotificationTrigger.setter
    def DLPNotificationTrigger(self, value: Optional[float]):
        if value is None:
            if "DLPNotificationTrigger" in self._dataset:
                del self._dataset.DLPNotificationTrigger
        else:
            self._dataset.DLPNotificationTrigger = value
