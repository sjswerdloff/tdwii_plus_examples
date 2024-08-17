from decimal import Decimal
from typing import Any, List, Optional  # noqa

import pydicom

from .brachy_accessory_device_sequence_item import BrachyAccessoryDeviceSequenceItem
from .channel_sequence_item import ChannelSequenceItem
from .referenced_reference_image_sequence_item import (
    ReferencedReferenceImageSequenceItem,
)


class ApplicationSetupSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._BrachyAccessoryDeviceSequence: List[BrachyAccessoryDeviceSequenceItem] = []
        self._ChannelSequence: List[ChannelSequenceItem] = []
        self._ReferencedReferenceImageSequence: List[ReferencedReferenceImageSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

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
    def ApplicationSetupNumber(self) -> Optional[int]:
        if "ApplicationSetupNumber" in self._dataset:
            return self._dataset.ApplicationSetupNumber
        return None

    @ApplicationSetupNumber.setter
    def ApplicationSetupNumber(self, value: Optional[int]):
        if value is None:
            if "ApplicationSetupNumber" in self._dataset:
                del self._dataset.ApplicationSetupNumber
        else:
            self._dataset.ApplicationSetupNumber = value

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
    def BrachyAccessoryDeviceSequence(self) -> Optional[List[BrachyAccessoryDeviceSequenceItem]]:
        if "BrachyAccessoryDeviceSequence" in self._dataset:
            if len(self._BrachyAccessoryDeviceSequence) == len(self._dataset.BrachyAccessoryDeviceSequence):
                return self._BrachyAccessoryDeviceSequence
            else:
                return [BrachyAccessoryDeviceSequenceItem(x) for x in self._dataset.BrachyAccessoryDeviceSequence]
        return None

    @BrachyAccessoryDeviceSequence.setter
    def BrachyAccessoryDeviceSequence(self, value: Optional[List[BrachyAccessoryDeviceSequenceItem]]):
        if value is None:
            self._BrachyAccessoryDeviceSequence = []
            if "BrachyAccessoryDeviceSequence" in self._dataset:
                del self._dataset.BrachyAccessoryDeviceSequence
        elif not isinstance(value, list) or not all(isinstance(item, BrachyAccessoryDeviceSequenceItem) for item in value):
            raise ValueError("BrachyAccessoryDeviceSequence must be a list of BrachyAccessoryDeviceSequenceItem objects")
        else:
            self._BrachyAccessoryDeviceSequence = value
            if "BrachyAccessoryDeviceSequence" not in self._dataset:
                self._dataset.BrachyAccessoryDeviceSequence = pydicom.Sequence()
            self._dataset.BrachyAccessoryDeviceSequence.clear()
            self._dataset.BrachyAccessoryDeviceSequence.extend([item.to_dataset() for item in value])

    def add_BrachyAccessoryDevice(self, item: BrachyAccessoryDeviceSequenceItem):
        if not isinstance(item, BrachyAccessoryDeviceSequenceItem):
            raise ValueError("Item must be an instance of BrachyAccessoryDeviceSequenceItem")
        self._BrachyAccessoryDeviceSequence.append(item)
        if "BrachyAccessoryDeviceSequence" not in self._dataset:
            self._dataset.BrachyAccessoryDeviceSequence = pydicom.Sequence()
        self._dataset.BrachyAccessoryDeviceSequence.append(item.to_dataset())

    @property
    def ChannelSequence(self) -> Optional[List[ChannelSequenceItem]]:
        if "ChannelSequence" in self._dataset:
            if len(self._ChannelSequence) == len(self._dataset.ChannelSequence):
                return self._ChannelSequence
            else:
                return [ChannelSequenceItem(x) for x in self._dataset.ChannelSequence]
        return None

    @ChannelSequence.setter
    def ChannelSequence(self, value: Optional[List[ChannelSequenceItem]]):
        if value is None:
            self._ChannelSequence = []
            if "ChannelSequence" in self._dataset:
                del self._dataset.ChannelSequence
        elif not isinstance(value, list) or not all(isinstance(item, ChannelSequenceItem) for item in value):
            raise ValueError("ChannelSequence must be a list of ChannelSequenceItem objects")
        else:
            self._ChannelSequence = value
            if "ChannelSequence" not in self._dataset:
                self._dataset.ChannelSequence = pydicom.Sequence()
            self._dataset.ChannelSequence.clear()
            self._dataset.ChannelSequence.extend([item.to_dataset() for item in value])

    def add_Channel(self, item: ChannelSequenceItem):
        if not isinstance(item, ChannelSequenceItem):
            raise ValueError("Item must be an instance of ChannelSequenceItem")
        self._ChannelSequence.append(item)
        if "ChannelSequence" not in self._dataset:
            self._dataset.ChannelSequence = pydicom.Sequence()
        self._dataset.ChannelSequence.append(item.to_dataset())

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
