from decimal import Decimal
from typing import Any, List, Optional

import pydicom

from .code_sequence_item import CodeSequenceItem
from .recorded_brachy_accessory_device_sequence_item import (
    RecordedBrachyAccessoryDeviceSequenceItem,
)
from .recorded_channel_sequence_item import RecordedChannelSequenceItem
from .referenced_calculated_dose_reference_sequence_item import (
    ReferencedCalculatedDoseReferenceSequenceItem,
)
from .referenced_measured_dose_reference_sequence_item import (
    ReferencedMeasuredDoseReferenceSequenceItem,
)
from .referenced_verification_image_sequence_item import (
    ReferencedVerificationImageSequenceItem,
)


class TreatmentSessionApplicationSetupSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._ReferencedMeasuredDoseReferenceSequence: List[ReferencedMeasuredDoseReferenceSequenceItem] = []
        self._ReferencedCalculatedDoseReferenceSequence: List[ReferencedCalculatedDoseReferenceSequenceItem] = []
        self._RecordedBrachyAccessoryDeviceSequence: List[RecordedBrachyAccessoryDeviceSequenceItem] = []
        self._RecordedChannelSequence: List[RecordedChannelSequenceItem] = []
        self._RTTreatmentTerminationReasonCodeSequence: List[CodeSequenceItem] = []
        self._MachineSpecificTreatmentTerminationCodeSequence: List[CodeSequenceItem] = []
        self._ReferencedVerificationImageSequence: List[ReferencedVerificationImageSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def CurrentFractionNumber(self) -> Optional[int]:
        if "CurrentFractionNumber" in self._dataset:
            return self._dataset.CurrentFractionNumber
        return None

    @CurrentFractionNumber.setter
    def CurrentFractionNumber(self, value: Optional[int]):
        if value is None:
            if "CurrentFractionNumber" in self._dataset:
                del self._dataset.CurrentFractionNumber
        else:
            self._dataset.CurrentFractionNumber = value

    @property
    def TreatmentTerminationStatus(self) -> Optional[str]:
        if "TreatmentTerminationStatus" in self._dataset:
            return self._dataset.TreatmentTerminationStatus
        return None

    @TreatmentTerminationStatus.setter
    def TreatmentTerminationStatus(self, value: Optional[str]):
        if value is None:
            if "TreatmentTerminationStatus" in self._dataset:
                del self._dataset.TreatmentTerminationStatus
        else:
            self._dataset.TreatmentTerminationStatus = value

    @property
    def TreatmentVerificationStatus(self) -> Optional[str]:
        if "TreatmentVerificationStatus" in self._dataset:
            return self._dataset.TreatmentVerificationStatus
        return None

    @TreatmentVerificationStatus.setter
    def TreatmentVerificationStatus(self, value: Optional[str]):
        if value is None:
            if "TreatmentVerificationStatus" in self._dataset:
                del self._dataset.TreatmentVerificationStatus
        else:
            self._dataset.TreatmentVerificationStatus = value

    @property
    def ReferencedMeasuredDoseReferenceSequence(self) -> Optional[List[ReferencedMeasuredDoseReferenceSequenceItem]]:
        if "ReferencedMeasuredDoseReferenceSequence" in self._dataset:
            if len(self._ReferencedMeasuredDoseReferenceSequence) == len(
                self._dataset.ReferencedMeasuredDoseReferenceSequence
            ):
                return self._ReferencedMeasuredDoseReferenceSequence
            else:
                return [
                    ReferencedMeasuredDoseReferenceSequenceItem(x)
                    for x in self._dataset.ReferencedMeasuredDoseReferenceSequence
                ]
        return None

    @ReferencedMeasuredDoseReferenceSequence.setter
    def ReferencedMeasuredDoseReferenceSequence(self, value: Optional[List[ReferencedMeasuredDoseReferenceSequenceItem]]):
        if value is None:
            self._ReferencedMeasuredDoseReferenceSequence = []
            if "ReferencedMeasuredDoseReferenceSequence" in self._dataset:
                del self._dataset.ReferencedMeasuredDoseReferenceSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, ReferencedMeasuredDoseReferenceSequenceItem) for item in value
        ):
            raise ValueError(
                f"ReferencedMeasuredDoseReferenceSequence must be a list of ReferencedMeasuredDoseReferenceSequenceItem objects"
            )
        else:
            self._ReferencedMeasuredDoseReferenceSequence = value
            if "ReferencedMeasuredDoseReferenceSequence" not in self._dataset:
                self._dataset.ReferencedMeasuredDoseReferenceSequence = pydicom.Sequence()
            self._dataset.ReferencedMeasuredDoseReferenceSequence.clear()
            self._dataset.ReferencedMeasuredDoseReferenceSequence.extend([item.to_dataset() for item in value])

    def add_ReferencedMeasuredDoseReference(self, item: ReferencedMeasuredDoseReferenceSequenceItem):
        if not isinstance(item, ReferencedMeasuredDoseReferenceSequenceItem):
            raise ValueError(f"Item must be an instance of ReferencedMeasuredDoseReferenceSequenceItem")
        self._ReferencedMeasuredDoseReferenceSequence.append(item)
        if "ReferencedMeasuredDoseReferenceSequence" not in self._dataset:
            self._dataset.ReferencedMeasuredDoseReferenceSequence = pydicom.Sequence()
        self._dataset.ReferencedMeasuredDoseReferenceSequence.append(item.to_dataset())

    @property
    def ReferencedCalculatedDoseReferenceSequence(self) -> Optional[List[ReferencedCalculatedDoseReferenceSequenceItem]]:
        if "ReferencedCalculatedDoseReferenceSequence" in self._dataset:
            if len(self._ReferencedCalculatedDoseReferenceSequence) == len(
                self._dataset.ReferencedCalculatedDoseReferenceSequence
            ):
                return self._ReferencedCalculatedDoseReferenceSequence
            else:
                return [
                    ReferencedCalculatedDoseReferenceSequenceItem(x)
                    for x in self._dataset.ReferencedCalculatedDoseReferenceSequence
                ]
        return None

    @ReferencedCalculatedDoseReferenceSequence.setter
    def ReferencedCalculatedDoseReferenceSequence(self, value: Optional[List[ReferencedCalculatedDoseReferenceSequenceItem]]):
        if value is None:
            self._ReferencedCalculatedDoseReferenceSequence = []
            if "ReferencedCalculatedDoseReferenceSequence" in self._dataset:
                del self._dataset.ReferencedCalculatedDoseReferenceSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, ReferencedCalculatedDoseReferenceSequenceItem) for item in value
        ):
            raise ValueError(
                f"ReferencedCalculatedDoseReferenceSequence must be a list of ReferencedCalculatedDoseReferenceSequenceItem objects"
            )
        else:
            self._ReferencedCalculatedDoseReferenceSequence = value
            if "ReferencedCalculatedDoseReferenceSequence" not in self._dataset:
                self._dataset.ReferencedCalculatedDoseReferenceSequence = pydicom.Sequence()
            self._dataset.ReferencedCalculatedDoseReferenceSequence.clear()
            self._dataset.ReferencedCalculatedDoseReferenceSequence.extend([item.to_dataset() for item in value])

    def add_ReferencedCalculatedDoseReference(self, item: ReferencedCalculatedDoseReferenceSequenceItem):
        if not isinstance(item, ReferencedCalculatedDoseReferenceSequenceItem):
            raise ValueError(f"Item must be an instance of ReferencedCalculatedDoseReferenceSequenceItem")
        self._ReferencedCalculatedDoseReferenceSequence.append(item)
        if "ReferencedCalculatedDoseReferenceSequence" not in self._dataset:
            self._dataset.ReferencedCalculatedDoseReferenceSequence = pydicom.Sequence()
        self._dataset.ReferencedCalculatedDoseReferenceSequence.append(item.to_dataset())

    @property
    def ApplicationSetupCheck(self) -> Optional[str]:
        if "ApplicationSetupCheck" in self._dataset:
            return self._dataset.ApplicationSetupCheck
        return None

    @ApplicationSetupCheck.setter
    def ApplicationSetupCheck(self, value: Optional[str]):
        if value is None:
            if "ApplicationSetupCheck" in self._dataset:
                del self._dataset.ApplicationSetupCheck
        else:
            self._dataset.ApplicationSetupCheck = value

    @property
    def RecordedBrachyAccessoryDeviceSequence(self) -> Optional[List[RecordedBrachyAccessoryDeviceSequenceItem]]:
        if "RecordedBrachyAccessoryDeviceSequence" in self._dataset:
            if len(self._RecordedBrachyAccessoryDeviceSequence) == len(self._dataset.RecordedBrachyAccessoryDeviceSequence):
                return self._RecordedBrachyAccessoryDeviceSequence
            else:
                return [
                    RecordedBrachyAccessoryDeviceSequenceItem(x) for x in self._dataset.RecordedBrachyAccessoryDeviceSequence
                ]
        return None

    @RecordedBrachyAccessoryDeviceSequence.setter
    def RecordedBrachyAccessoryDeviceSequence(self, value: Optional[List[RecordedBrachyAccessoryDeviceSequenceItem]]):
        if value is None:
            self._RecordedBrachyAccessoryDeviceSequence = []
            if "RecordedBrachyAccessoryDeviceSequence" in self._dataset:
                del self._dataset.RecordedBrachyAccessoryDeviceSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, RecordedBrachyAccessoryDeviceSequenceItem) for item in value
        ):
            raise ValueError(
                f"RecordedBrachyAccessoryDeviceSequence must be a list of RecordedBrachyAccessoryDeviceSequenceItem objects"
            )
        else:
            self._RecordedBrachyAccessoryDeviceSequence = value
            if "RecordedBrachyAccessoryDeviceSequence" not in self._dataset:
                self._dataset.RecordedBrachyAccessoryDeviceSequence = pydicom.Sequence()
            self._dataset.RecordedBrachyAccessoryDeviceSequence.clear()
            self._dataset.RecordedBrachyAccessoryDeviceSequence.extend([item.to_dataset() for item in value])

    def add_RecordedBrachyAccessoryDevice(self, item: RecordedBrachyAccessoryDeviceSequenceItem):
        if not isinstance(item, RecordedBrachyAccessoryDeviceSequenceItem):
            raise ValueError(f"Item must be an instance of RecordedBrachyAccessoryDeviceSequenceItem")
        self._RecordedBrachyAccessoryDeviceSequence.append(item)
        if "RecordedBrachyAccessoryDeviceSequence" not in self._dataset:
            self._dataset.RecordedBrachyAccessoryDeviceSequence = pydicom.Sequence()
        self._dataset.RecordedBrachyAccessoryDeviceSequence.append(item.to_dataset())

    @property
    def RecordedChannelSequence(self) -> Optional[List[RecordedChannelSequenceItem]]:
        if "RecordedChannelSequence" in self._dataset:
            if len(self._RecordedChannelSequence) == len(self._dataset.RecordedChannelSequence):
                return self._RecordedChannelSequence
            else:
                return [RecordedChannelSequenceItem(x) for x in self._dataset.RecordedChannelSequence]
        return None

    @RecordedChannelSequence.setter
    def RecordedChannelSequence(self, value: Optional[List[RecordedChannelSequenceItem]]):
        if value is None:
            self._RecordedChannelSequence = []
            if "RecordedChannelSequence" in self._dataset:
                del self._dataset.RecordedChannelSequence
        elif not isinstance(value, list) or not all(isinstance(item, RecordedChannelSequenceItem) for item in value):
            raise ValueError(f"RecordedChannelSequence must be a list of RecordedChannelSequenceItem objects")
        else:
            self._RecordedChannelSequence = value
            if "RecordedChannelSequence" not in self._dataset:
                self._dataset.RecordedChannelSequence = pydicom.Sequence()
            self._dataset.RecordedChannelSequence.clear()
            self._dataset.RecordedChannelSequence.extend([item.to_dataset() for item in value])

    def add_RecordedChannel(self, item: RecordedChannelSequenceItem):
        if not isinstance(item, RecordedChannelSequenceItem):
            raise ValueError(f"Item must be an instance of RecordedChannelSequenceItem")
        self._RecordedChannelSequence.append(item)
        if "RecordedChannelSequence" not in self._dataset:
            self._dataset.RecordedChannelSequence = pydicom.Sequence()
        self._dataset.RecordedChannelSequence.append(item.to_dataset())

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
    def ApplicationSetupType(self) -> Optional[str]:
        if "ApplicationSetupType" in self._dataset:
            return self._dataset.ApplicationSetupType
        return None

    @ApplicationSetupType.setter
    def ApplicationSetupType(self, value: Optional[str]):
        if value is None:
            if "ApplicationSetupType" in self._dataset:
                del self._dataset.ApplicationSetupType
        else:
            self._dataset.ApplicationSetupType = value

    @property
    def ApplicationSetupName(self) -> Optional[str]:
        if "ApplicationSetupName" in self._dataset:
            return self._dataset.ApplicationSetupName
        return None

    @ApplicationSetupName.setter
    def ApplicationSetupName(self, value: Optional[str]):
        if value is None:
            if "ApplicationSetupName" in self._dataset:
                del self._dataset.ApplicationSetupName
        else:
            self._dataset.ApplicationSetupName = value

    @property
    def ApplicationSetupManufacturer(self) -> Optional[str]:
        if "ApplicationSetupManufacturer" in self._dataset:
            return self._dataset.ApplicationSetupManufacturer
        return None

    @ApplicationSetupManufacturer.setter
    def ApplicationSetupManufacturer(self, value: Optional[str]):
        if value is None:
            if "ApplicationSetupManufacturer" in self._dataset:
                del self._dataset.ApplicationSetupManufacturer
        else:
            self._dataset.ApplicationSetupManufacturer = value

    @property
    def TemplateNumber(self) -> Optional[int]:
        if "TemplateNumber" in self._dataset:
            return self._dataset.TemplateNumber
        return None

    @TemplateNumber.setter
    def TemplateNumber(self, value: Optional[int]):
        if value is None:
            if "TemplateNumber" in self._dataset:
                del self._dataset.TemplateNumber
        else:
            self._dataset.TemplateNumber = value

    @property
    def TemplateType(self) -> Optional[str]:
        if "TemplateType" in self._dataset:
            return self._dataset.TemplateType
        return None

    @TemplateType.setter
    def TemplateType(self, value: Optional[str]):
        if value is None:
            if "TemplateType" in self._dataset:
                del self._dataset.TemplateType
        else:
            self._dataset.TemplateType = value

    @property
    def TemplateName(self) -> Optional[str]:
        if "TemplateName" in self._dataset:
            return self._dataset.TemplateName
        return None

    @TemplateName.setter
    def TemplateName(self, value: Optional[str]):
        if value is None:
            if "TemplateName" in self._dataset:
                del self._dataset.TemplateName
        else:
            self._dataset.TemplateName = value

    @property
    def TotalReferenceAirKerma(self) -> Optional[Decimal]:
        if "TotalReferenceAirKerma" in self._dataset:
            return self._dataset.TotalReferenceAirKerma
        return None

    @TotalReferenceAirKerma.setter
    def TotalReferenceAirKerma(self, value: Optional[Decimal]):
        if value is None:
            if "TotalReferenceAirKerma" in self._dataset:
                del self._dataset.TotalReferenceAirKerma
        else:
            self._dataset.TotalReferenceAirKerma = value

    @property
    def RTTreatmentTerminationReasonCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "RTTreatmentTerminationReasonCodeSequence" in self._dataset:
            if len(self._RTTreatmentTerminationReasonCodeSequence) == len(
                self._dataset.RTTreatmentTerminationReasonCodeSequence
            ):
                return self._RTTreatmentTerminationReasonCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.RTTreatmentTerminationReasonCodeSequence]
        return None

    @RTTreatmentTerminationReasonCodeSequence.setter
    def RTTreatmentTerminationReasonCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._RTTreatmentTerminationReasonCodeSequence = []
            if "RTTreatmentTerminationReasonCodeSequence" in self._dataset:
                del self._dataset.RTTreatmentTerminationReasonCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError(f"RTTreatmentTerminationReasonCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._RTTreatmentTerminationReasonCodeSequence = value
            if "RTTreatmentTerminationReasonCodeSequence" not in self._dataset:
                self._dataset.RTTreatmentTerminationReasonCodeSequence = pydicom.Sequence()
            self._dataset.RTTreatmentTerminationReasonCodeSequence.clear()
            self._dataset.RTTreatmentTerminationReasonCodeSequence.extend([item.to_dataset() for item in value])

    def add_RTTreatmentTerminationReasonCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError(f"Item must be an instance of CodeSequenceItem")
        self._RTTreatmentTerminationReasonCodeSequence.append(item)
        if "RTTreatmentTerminationReasonCodeSequence" not in self._dataset:
            self._dataset.RTTreatmentTerminationReasonCodeSequence = pydicom.Sequence()
        self._dataset.RTTreatmentTerminationReasonCodeSequence.append(item.to_dataset())

    @property
    def MachineSpecificTreatmentTerminationCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "MachineSpecificTreatmentTerminationCodeSequence" in self._dataset:
            if len(self._MachineSpecificTreatmentTerminationCodeSequence) == len(
                self._dataset.MachineSpecificTreatmentTerminationCodeSequence
            ):
                return self._MachineSpecificTreatmentTerminationCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.MachineSpecificTreatmentTerminationCodeSequence]
        return None

    @MachineSpecificTreatmentTerminationCodeSequence.setter
    def MachineSpecificTreatmentTerminationCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._MachineSpecificTreatmentTerminationCodeSequence = []
            if "MachineSpecificTreatmentTerminationCodeSequence" in self._dataset:
                del self._dataset.MachineSpecificTreatmentTerminationCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError(f"MachineSpecificTreatmentTerminationCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._MachineSpecificTreatmentTerminationCodeSequence = value
            if "MachineSpecificTreatmentTerminationCodeSequence" not in self._dataset:
                self._dataset.MachineSpecificTreatmentTerminationCodeSequence = pydicom.Sequence()
            self._dataset.MachineSpecificTreatmentTerminationCodeSequence.clear()
            self._dataset.MachineSpecificTreatmentTerminationCodeSequence.extend([item.to_dataset() for item in value])

    def add_MachineSpecificTreatmentTerminationCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError(f"Item must be an instance of CodeSequenceItem")
        self._MachineSpecificTreatmentTerminationCodeSequence.append(item)
        if "MachineSpecificTreatmentTerminationCodeSequence" not in self._dataset:
            self._dataset.MachineSpecificTreatmentTerminationCodeSequence = pydicom.Sequence()
        self._dataset.MachineSpecificTreatmentTerminationCodeSequence.append(item.to_dataset())

    @property
    def TreatmentTerminationDescription(self) -> Optional[str]:
        if "TreatmentTerminationDescription" in self._dataset:
            return self._dataset.TreatmentTerminationDescription
        return None

    @TreatmentTerminationDescription.setter
    def TreatmentTerminationDescription(self, value: Optional[str]):
        if value is None:
            if "TreatmentTerminationDescription" in self._dataset:
                del self._dataset.TreatmentTerminationDescription
        else:
            self._dataset.TreatmentTerminationDescription = value

    @property
    def ReferencedBrachyApplicationSetupNumber(self) -> Optional[int]:
        if "ReferencedBrachyApplicationSetupNumber" in self._dataset:
            return self._dataset.ReferencedBrachyApplicationSetupNumber
        return None

    @ReferencedBrachyApplicationSetupNumber.setter
    def ReferencedBrachyApplicationSetupNumber(self, value: Optional[int]):
        if value is None:
            if "ReferencedBrachyApplicationSetupNumber" in self._dataset:
                del self._dataset.ReferencedBrachyApplicationSetupNumber
        else:
            self._dataset.ReferencedBrachyApplicationSetupNumber = value

    @property
    def ReferencedVerificationImageSequence(self) -> Optional[List[ReferencedVerificationImageSequenceItem]]:
        if "ReferencedVerificationImageSequence" in self._dataset:
            if len(self._ReferencedVerificationImageSequence) == len(self._dataset.ReferencedVerificationImageSequence):
                return self._ReferencedVerificationImageSequence
            else:
                return [ReferencedVerificationImageSequenceItem(x) for x in self._dataset.ReferencedVerificationImageSequence]
        return None

    @ReferencedVerificationImageSequence.setter
    def ReferencedVerificationImageSequence(self, value: Optional[List[ReferencedVerificationImageSequenceItem]]):
        if value is None:
            self._ReferencedVerificationImageSequence = []
            if "ReferencedVerificationImageSequence" in self._dataset:
                del self._dataset.ReferencedVerificationImageSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, ReferencedVerificationImageSequenceItem) for item in value
        ):
            raise ValueError(
                f"ReferencedVerificationImageSequence must be a list of ReferencedVerificationImageSequenceItem objects"
            )
        else:
            self._ReferencedVerificationImageSequence = value
            if "ReferencedVerificationImageSequence" not in self._dataset:
                self._dataset.ReferencedVerificationImageSequence = pydicom.Sequence()
            self._dataset.ReferencedVerificationImageSequence.clear()
            self._dataset.ReferencedVerificationImageSequence.extend([item.to_dataset() for item in value])

    def add_ReferencedVerificationImage(self, item: ReferencedVerificationImageSequenceItem):
        if not isinstance(item, ReferencedVerificationImageSequenceItem):
            raise ValueError(f"Item must be an instance of ReferencedVerificationImageSequenceItem")
        self._ReferencedVerificationImageSequence.append(item)
        if "ReferencedVerificationImageSequence" not in self._dataset:
            self._dataset.ReferencedVerificationImageSequence = pydicom.Sequence()
        self._dataset.ReferencedVerificationImageSequence.append(item.to_dataset())
