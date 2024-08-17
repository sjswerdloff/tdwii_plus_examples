from typing import Any, List, Optional  # noqa

import pydicom

from .code_sequence_item import CodeSequenceItem
from .referenced_defined_protocol_sequence_item import (
    ReferencedDefinedProtocolSequenceItem,
)
from .referenced_performed_protocol_sequence_item import (
    ReferencedPerformedProtocolSequenceItem,
)
from .xa_acquisition_phase_details_sequence_item import (
    XAAcquisitionPhaseDetailsSequenceItem,
)
from .xa_plane_details_sequence_item import XAPlaneDetailsSequenceItem


class AcquisitionProtocolElementSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._XAAcquisitionPhaseDetailsSequence: List[XAAcquisitionPhaseDetailsSequenceItem] = []
        self._XAPlaneDetailsSequence: List[XAPlaneDetailsSequenceItem] = []
        self._RequestedSeriesDescriptionCodeSequence: List[CodeSequenceItem] = []
        self._ReferencedDefinedProtocolSequence: List[ReferencedDefinedProtocolSequenceItem] = []
        self._ReferencedPerformedProtocolSequence: List[ReferencedPerformedProtocolSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ScanOptions(self) -> Optional[List[str]]:
        if "ScanOptions" in self._dataset:
            return self._dataset.ScanOptions
        return None

    @ScanOptions.setter
    def ScanOptions(self, value: Optional[List[str]]):
        if value is None:
            if "ScanOptions" in self._dataset:
                del self._dataset.ScanOptions
        else:
            self._dataset.ScanOptions = value

    @property
    def RadiationSetting(self) -> Optional[str]:
        if "RadiationSetting" in self._dataset:
            return self._dataset.RadiationSetting
        return None

    @RadiationSetting.setter
    def RadiationSetting(self, value: Optional[str]):
        if value is None:
            if "RadiationSetting" in self._dataset:
                del self._dataset.RadiationSetting
        else:
            self._dataset.RadiationSetting = value

    @property
    def AcquisitionMode(self) -> Optional[str]:
        if "AcquisitionMode" in self._dataset:
            return self._dataset.AcquisitionMode
        return None

    @AcquisitionMode.setter
    def AcquisitionMode(self, value: Optional[str]):
        if value is None:
            if "AcquisitionMode" in self._dataset:
                del self._dataset.AcquisitionMode
        else:
            self._dataset.AcquisitionMode = value

    @property
    def DoseModeName(self) -> Optional[str]:
        if "DoseModeName" in self._dataset:
            return self._dataset.DoseModeName
        return None

    @DoseModeName.setter
    def DoseModeName(self, value: Optional[str]):
        if value is None:
            if "DoseModeName" in self._dataset:
                del self._dataset.DoseModeName
        else:
            self._dataset.DoseModeName = value

    @property
    def AcquiredSubtractionMaskFlag(self) -> Optional[str]:
        if "AcquiredSubtractionMaskFlag" in self._dataset:
            return self._dataset.AcquiredSubtractionMaskFlag
        return None

    @AcquiredSubtractionMaskFlag.setter
    def AcquiredSubtractionMaskFlag(self, value: Optional[str]):
        if value is None:
            if "AcquiredSubtractionMaskFlag" in self._dataset:
                del self._dataset.AcquiredSubtractionMaskFlag
        else:
            self._dataset.AcquiredSubtractionMaskFlag = value

    @property
    def FluoroscopyPersistenceFlag(self) -> Optional[str]:
        if "FluoroscopyPersistenceFlag" in self._dataset:
            return self._dataset.FluoroscopyPersistenceFlag
        return None

    @FluoroscopyPersistenceFlag.setter
    def FluoroscopyPersistenceFlag(self, value: Optional[str]):
        if value is None:
            if "FluoroscopyPersistenceFlag" in self._dataset:
                del self._dataset.FluoroscopyPersistenceFlag
        else:
            self._dataset.FluoroscopyPersistenceFlag = value

    @property
    def FluoroscopyLastImageHoldPersistenceFlag(self) -> Optional[str]:
        if "FluoroscopyLastImageHoldPersistenceFlag" in self._dataset:
            return self._dataset.FluoroscopyLastImageHoldPersistenceFlag
        return None

    @FluoroscopyLastImageHoldPersistenceFlag.setter
    def FluoroscopyLastImageHoldPersistenceFlag(self, value: Optional[str]):
        if value is None:
            if "FluoroscopyLastImageHoldPersistenceFlag" in self._dataset:
                del self._dataset.FluoroscopyLastImageHoldPersistenceFlag
        else:
            self._dataset.FluoroscopyLastImageHoldPersistenceFlag = value

    @property
    def UpperLimitNumberOfPersistentFluoroscopyFrames(self) -> Optional[int]:
        if "UpperLimitNumberOfPersistentFluoroscopyFrames" in self._dataset:
            return self._dataset.UpperLimitNumberOfPersistentFluoroscopyFrames
        return None

    @UpperLimitNumberOfPersistentFluoroscopyFrames.setter
    def UpperLimitNumberOfPersistentFluoroscopyFrames(self, value: Optional[int]):
        if value is None:
            if "UpperLimitNumberOfPersistentFluoroscopyFrames" in self._dataset:
                del self._dataset.UpperLimitNumberOfPersistentFluoroscopyFrames
        else:
            self._dataset.UpperLimitNumberOfPersistentFluoroscopyFrames = value

    @property
    def ContrastBolusAutoInjectionTriggerFlag(self) -> Optional[str]:
        if "ContrastBolusAutoInjectionTriggerFlag" in self._dataset:
            return self._dataset.ContrastBolusAutoInjectionTriggerFlag
        return None

    @ContrastBolusAutoInjectionTriggerFlag.setter
    def ContrastBolusAutoInjectionTriggerFlag(self, value: Optional[str]):
        if value is None:
            if "ContrastBolusAutoInjectionTriggerFlag" in self._dataset:
                del self._dataset.ContrastBolusAutoInjectionTriggerFlag
        else:
            self._dataset.ContrastBolusAutoInjectionTriggerFlag = value

    @property
    def ContrastBolusInjectionDelay(self) -> Optional[float]:
        if "ContrastBolusInjectionDelay" in self._dataset:
            return self._dataset.ContrastBolusInjectionDelay
        return None

    @ContrastBolusInjectionDelay.setter
    def ContrastBolusInjectionDelay(self, value: Optional[float]):
        if value is None:
            if "ContrastBolusInjectionDelay" in self._dataset:
                del self._dataset.ContrastBolusInjectionDelay
        else:
            self._dataset.ContrastBolusInjectionDelay = value

    @property
    def XAAcquisitionPhaseDetailsSequence(self) -> Optional[List[XAAcquisitionPhaseDetailsSequenceItem]]:
        if "XAAcquisitionPhaseDetailsSequence" in self._dataset:
            if len(self._XAAcquisitionPhaseDetailsSequence) == len(self._dataset.XAAcquisitionPhaseDetailsSequence):
                return self._XAAcquisitionPhaseDetailsSequence
            else:
                return [XAAcquisitionPhaseDetailsSequenceItem(x) for x in self._dataset.XAAcquisitionPhaseDetailsSequence]
        return None

    @XAAcquisitionPhaseDetailsSequence.setter
    def XAAcquisitionPhaseDetailsSequence(self, value: Optional[List[XAAcquisitionPhaseDetailsSequenceItem]]):
        if value is None:
            self._XAAcquisitionPhaseDetailsSequence = []
            if "XAAcquisitionPhaseDetailsSequence" in self._dataset:
                del self._dataset.XAAcquisitionPhaseDetailsSequence
        elif not isinstance(value, list) or not all(isinstance(item, XAAcquisitionPhaseDetailsSequenceItem) for item in value):
            raise ValueError(
                "XAAcquisitionPhaseDetailsSequence must be a list of XAAcquisitionPhaseDetailsSequenceItem objects"
            )
        else:
            self._XAAcquisitionPhaseDetailsSequence = value
            if "XAAcquisitionPhaseDetailsSequence" not in self._dataset:
                self._dataset.XAAcquisitionPhaseDetailsSequence = pydicom.Sequence()
            self._dataset.XAAcquisitionPhaseDetailsSequence.clear()
            self._dataset.XAAcquisitionPhaseDetailsSequence.extend([item.to_dataset() for item in value])

    def add_XAAcquisitionPhaseDetails(self, item: XAAcquisitionPhaseDetailsSequenceItem):
        if not isinstance(item, XAAcquisitionPhaseDetailsSequenceItem):
            raise ValueError("Item must be an instance of XAAcquisitionPhaseDetailsSequenceItem")
        self._XAAcquisitionPhaseDetailsSequence.append(item)
        if "XAAcquisitionPhaseDetailsSequence" not in self._dataset:
            self._dataset.XAAcquisitionPhaseDetailsSequence = pydicom.Sequence()
        self._dataset.XAAcquisitionPhaseDetailsSequence.append(item.to_dataset())

    @property
    def XAPlaneDetailsSequence(self) -> Optional[List[XAPlaneDetailsSequenceItem]]:
        if "XAPlaneDetailsSequence" in self._dataset:
            if len(self._XAPlaneDetailsSequence) == len(self._dataset.XAPlaneDetailsSequence):
                return self._XAPlaneDetailsSequence
            else:
                return [XAPlaneDetailsSequenceItem(x) for x in self._dataset.XAPlaneDetailsSequence]
        return None

    @XAPlaneDetailsSequence.setter
    def XAPlaneDetailsSequence(self, value: Optional[List[XAPlaneDetailsSequenceItem]]):
        if value is None:
            self._XAPlaneDetailsSequence = []
            if "XAPlaneDetailsSequence" in self._dataset:
                del self._dataset.XAPlaneDetailsSequence
        elif not isinstance(value, list) or not all(isinstance(item, XAPlaneDetailsSequenceItem) for item in value):
            raise ValueError("XAPlaneDetailsSequence must be a list of XAPlaneDetailsSequenceItem objects")
        else:
            self._XAPlaneDetailsSequence = value
            if "XAPlaneDetailsSequence" not in self._dataset:
                self._dataset.XAPlaneDetailsSequence = pydicom.Sequence()
            self._dataset.XAPlaneDetailsSequence.clear()
            self._dataset.XAPlaneDetailsSequence.extend([item.to_dataset() for item in value])

    def add_XAPlaneDetails(self, item: XAPlaneDetailsSequenceItem):
        if not isinstance(item, XAPlaneDetailsSequenceItem):
            raise ValueError("Item must be an instance of XAPlaneDetailsSequenceItem")
        self._XAPlaneDetailsSequence.append(item)
        if "XAPlaneDetailsSequence" not in self._dataset:
            self._dataset.XAPlaneDetailsSequence = pydicom.Sequence()
        self._dataset.XAPlaneDetailsSequence.append(item.to_dataset())

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
            raise ValueError("RequestedSeriesDescriptionCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._RequestedSeriesDescriptionCodeSequence = value
            if "RequestedSeriesDescriptionCodeSequence" not in self._dataset:
                self._dataset.RequestedSeriesDescriptionCodeSequence = pydicom.Sequence()
            self._dataset.RequestedSeriesDescriptionCodeSequence.clear()
            self._dataset.RequestedSeriesDescriptionCodeSequence.extend([item.to_dataset() for item in value])

    def add_RequestedSeriesDescriptionCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
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
    def PlanesInAcquisition(self) -> Optional[str]:
        if "PlanesInAcquisition" in self._dataset:
            return self._dataset.PlanesInAcquisition
        return None

    @PlanesInAcquisition.setter
    def PlanesInAcquisition(self, value: Optional[str]):
        if value is None:
            if "PlanesInAcquisition" in self._dataset:
                del self._dataset.PlanesInAcquisition
        else:
            self._dataset.PlanesInAcquisition = value

    @property
    def ContrastBolusIngredientOpaque(self) -> Optional[str]:
        if "ContrastBolusIngredientOpaque" in self._dataset:
            return self._dataset.ContrastBolusIngredientOpaque
        return None

    @ContrastBolusIngredientOpaque.setter
    def ContrastBolusIngredientOpaque(self, value: Optional[str]):
        if value is None:
            if "ContrastBolusIngredientOpaque" in self._dataset:
                del self._dataset.ContrastBolusIngredientOpaque
        else:
            self._dataset.ContrastBolusIngredientOpaque = value

    @property
    def ReferencedDefinedProtocolSequence(self) -> Optional[List[ReferencedDefinedProtocolSequenceItem]]:
        if "ReferencedDefinedProtocolSequence" in self._dataset:
            if len(self._ReferencedDefinedProtocolSequence) == len(self._dataset.ReferencedDefinedProtocolSequence):
                return self._ReferencedDefinedProtocolSequence
            else:
                return [ReferencedDefinedProtocolSequenceItem(x) for x in self._dataset.ReferencedDefinedProtocolSequence]
        return None

    @ReferencedDefinedProtocolSequence.setter
    def ReferencedDefinedProtocolSequence(self, value: Optional[List[ReferencedDefinedProtocolSequenceItem]]):
        if value is None:
            self._ReferencedDefinedProtocolSequence = []
            if "ReferencedDefinedProtocolSequence" in self._dataset:
                del self._dataset.ReferencedDefinedProtocolSequence
        elif not isinstance(value, list) or not all(isinstance(item, ReferencedDefinedProtocolSequenceItem) for item in value):
            raise ValueError(
                "ReferencedDefinedProtocolSequence must be a list of ReferencedDefinedProtocolSequenceItem objects"
            )
        else:
            self._ReferencedDefinedProtocolSequence = value
            if "ReferencedDefinedProtocolSequence" not in self._dataset:
                self._dataset.ReferencedDefinedProtocolSequence = pydicom.Sequence()
            self._dataset.ReferencedDefinedProtocolSequence.clear()
            self._dataset.ReferencedDefinedProtocolSequence.extend([item.to_dataset() for item in value])

    def add_ReferencedDefinedProtocol(self, item: ReferencedDefinedProtocolSequenceItem):
        if not isinstance(item, ReferencedDefinedProtocolSequenceItem):
            raise ValueError("Item must be an instance of ReferencedDefinedProtocolSequenceItem")
        self._ReferencedDefinedProtocolSequence.append(item)
        if "ReferencedDefinedProtocolSequence" not in self._dataset:
            self._dataset.ReferencedDefinedProtocolSequence = pydicom.Sequence()
        self._dataset.ReferencedDefinedProtocolSequence.append(item.to_dataset())

    @property
    def ReferencedPerformedProtocolSequence(self) -> Optional[List[ReferencedPerformedProtocolSequenceItem]]:
        if "ReferencedPerformedProtocolSequence" in self._dataset:
            if len(self._ReferencedPerformedProtocolSequence) == len(self._dataset.ReferencedPerformedProtocolSequence):
                return self._ReferencedPerformedProtocolSequence
            else:
                return [ReferencedPerformedProtocolSequenceItem(x) for x in self._dataset.ReferencedPerformedProtocolSequence]
        return None

    @ReferencedPerformedProtocolSequence.setter
    def ReferencedPerformedProtocolSequence(self, value: Optional[List[ReferencedPerformedProtocolSequenceItem]]):
        if value is None:
            self._ReferencedPerformedProtocolSequence = []
            if "ReferencedPerformedProtocolSequence" in self._dataset:
                del self._dataset.ReferencedPerformedProtocolSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, ReferencedPerformedProtocolSequenceItem) for item in value
        ):
            raise ValueError(
                "ReferencedPerformedProtocolSequence must be a list of ReferencedPerformedProtocolSequenceItem objects"
            )
        else:
            self._ReferencedPerformedProtocolSequence = value
            if "ReferencedPerformedProtocolSequence" not in self._dataset:
                self._dataset.ReferencedPerformedProtocolSequence = pydicom.Sequence()
            self._dataset.ReferencedPerformedProtocolSequence.clear()
            self._dataset.ReferencedPerformedProtocolSequence.extend([item.to_dataset() for item in value])

    def add_ReferencedPerformedProtocol(self, item: ReferencedPerformedProtocolSequenceItem):
        if not isinstance(item, ReferencedPerformedProtocolSequenceItem):
            raise ValueError("Item must be an instance of ReferencedPerformedProtocolSequenceItem")
        self._ReferencedPerformedProtocolSequence.append(item)
        if "ReferencedPerformedProtocolSequence" not in self._dataset:
            self._dataset.ReferencedPerformedProtocolSequence = pydicom.Sequence()
        self._dataset.ReferencedPerformedProtocolSequence.append(item.to_dataset())

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
