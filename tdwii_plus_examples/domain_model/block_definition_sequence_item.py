from typing import Any, List, Optional

import pydicom

from .block_edge_data_sequence_item import BlockEdgeDataSequenceItem
from .block_slab_sequence_item import BlockSlabSequenceItem
from .code_sequence_item import CodeSequenceItem
from .udi_sequence_item import UDISequenceItem


class BlockDefinitionSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._UDISequence: List[UDISequenceItem] = []
        self._BlockSlabSequence: List[BlockSlabSequenceItem] = []
        self._BlockEdgeDataSequence: List[BlockEdgeDataSequenceItem] = []
        self._DeviceTypeCodeSequence: List[CodeSequenceItem] = []

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
    def UDISequence(self) -> Optional[List[UDISequenceItem]]:
        if "UDISequence" in self._dataset:
            if len(self._UDISequence) == len(self._dataset.UDISequence):
                return self._UDISequence
            else:
                return [UDISequenceItem(x) for x in self._dataset.UDISequence]
        return None

    @UDISequence.setter
    def UDISequence(self, value: Optional[List[UDISequenceItem]]):
        if value is None:
            self._UDISequence = []
            if "UDISequence" in self._dataset:
                del self._dataset.UDISequence
        elif not isinstance(value, list) or not all(isinstance(item, UDISequenceItem) for item in value):
            raise ValueError(f"UDISequence must be a list of UDISequenceItem objects")
        else:
            self._UDISequence = value
            if "UDISequence" not in self._dataset:
                self._dataset.UDISequence = pydicom.Sequence()
            self._dataset.UDISequence.clear()
            self._dataset.UDISequence.extend([item.to_dataset() for item in value])

    def add_UDI(self, item: UDISequenceItem):
        if not isinstance(item, UDISequenceItem):
            raise ValueError(f"Item must be an instance of UDISequenceItem")
        self._UDISequence.append(item)
        if "UDISequence" not in self._dataset:
            self._dataset.UDISequence = pydicom.Sequence()
        self._dataset.UDISequence.append(item.to_dataset())

    @property
    def SoftwareVersions(self) -> Optional[List[str]]:
        if "SoftwareVersions" in self._dataset:
            return self._dataset.SoftwareVersions
        return None

    @SoftwareVersions.setter
    def SoftwareVersions(self, value: Optional[List[str]]):
        if value is None:
            if "SoftwareVersions" in self._dataset:
                del self._dataset.SoftwareVersions
        else:
            self._dataset.SoftwareVersions = value

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
    def LongDeviceDescription(self) -> Optional[str]:
        if "LongDeviceDescription" in self._dataset:
            return self._dataset.LongDeviceDescription
        return None

    @LongDeviceDescription.setter
    def LongDeviceDescription(self, value: Optional[str]):
        if value is None:
            if "LongDeviceDescription" in self._dataset:
                del self._dataset.LongDeviceDescription
        else:
            self._dataset.LongDeviceDescription = value

    @property
    def MaterialID(self) -> Optional[str]:
        if "MaterialID" in self._dataset:
            return self._dataset.MaterialID
        return None

    @MaterialID.setter
    def MaterialID(self, value: Optional[str]):
        if value is None:
            if "MaterialID" in self._dataset:
                del self._dataset.MaterialID
        else:
            self._dataset.MaterialID = value

    @property
    def BlockDivergence(self) -> Optional[str]:
        if "BlockDivergence" in self._dataset:
            return self._dataset.BlockDivergence
        return None

    @BlockDivergence.setter
    def BlockDivergence(self, value: Optional[str]):
        if value is None:
            if "BlockDivergence" in self._dataset:
                del self._dataset.BlockDivergence
        else:
            self._dataset.BlockDivergence = value

    @property
    def NumberOfBlockSlabItems(self) -> Optional[int]:
        if "NumberOfBlockSlabItems" in self._dataset:
            return self._dataset.NumberOfBlockSlabItems
        return None

    @NumberOfBlockSlabItems.setter
    def NumberOfBlockSlabItems(self, value: Optional[int]):
        if value is None:
            if "NumberOfBlockSlabItems" in self._dataset:
                del self._dataset.NumberOfBlockSlabItems
        else:
            self._dataset.NumberOfBlockSlabItems = value

    @property
    def BlockSlabSequence(self) -> Optional[List[BlockSlabSequenceItem]]:
        if "BlockSlabSequence" in self._dataset:
            if len(self._BlockSlabSequence) == len(self._dataset.BlockSlabSequence):
                return self._BlockSlabSequence
            else:
                return [BlockSlabSequenceItem(x) for x in self._dataset.BlockSlabSequence]
        return None

    @BlockSlabSequence.setter
    def BlockSlabSequence(self, value: Optional[List[BlockSlabSequenceItem]]):
        if value is None:
            self._BlockSlabSequence = []
            if "BlockSlabSequence" in self._dataset:
                del self._dataset.BlockSlabSequence
        elif not isinstance(value, list) or not all(isinstance(item, BlockSlabSequenceItem) for item in value):
            raise ValueError(f"BlockSlabSequence must be a list of BlockSlabSequenceItem objects")
        else:
            self._BlockSlabSequence = value
            if "BlockSlabSequence" not in self._dataset:
                self._dataset.BlockSlabSequence = pydicom.Sequence()
            self._dataset.BlockSlabSequence.clear()
            self._dataset.BlockSlabSequence.extend([item.to_dataset() for item in value])

    def add_BlockSlab(self, item: BlockSlabSequenceItem):
        if not isinstance(item, BlockSlabSequenceItem):
            raise ValueError(f"Item must be an instance of BlockSlabSequenceItem")
        self._BlockSlabSequence.append(item)
        if "BlockSlabSequence" not in self._dataset:
            self._dataset.BlockSlabSequence = pydicom.Sequence()
        self._dataset.BlockSlabSequence.append(item.to_dataset())

    @property
    def ReferencedDefinedDeviceIndex(self) -> Optional[int]:
        if "ReferencedDefinedDeviceIndex" in self._dataset:
            return self._dataset.ReferencedDefinedDeviceIndex
        return None

    @ReferencedDefinedDeviceIndex.setter
    def ReferencedDefinedDeviceIndex(self, value: Optional[int]):
        if value is None:
            if "ReferencedDefinedDeviceIndex" in self._dataset:
                del self._dataset.ReferencedDefinedDeviceIndex
        else:
            self._dataset.ReferencedDefinedDeviceIndex = value

    @property
    def ReferencedRTAccessoryHolderDeviceIndex(self) -> Optional[int]:
        if "ReferencedRTAccessoryHolderDeviceIndex" in self._dataset:
            return self._dataset.ReferencedRTAccessoryHolderDeviceIndex
        return None

    @ReferencedRTAccessoryHolderDeviceIndex.setter
    def ReferencedRTAccessoryHolderDeviceIndex(self, value: Optional[int]):
        if value is None:
            if "ReferencedRTAccessoryHolderDeviceIndex" in self._dataset:
                del self._dataset.ReferencedRTAccessoryHolderDeviceIndex
        else:
            self._dataset.ReferencedRTAccessoryHolderDeviceIndex = value

    @property
    def RTAccessoryHolderSlotID(self) -> Optional[str]:
        if "RTAccessoryHolderSlotID" in self._dataset:
            return self._dataset.RTAccessoryHolderSlotID
        return None

    @RTAccessoryHolderSlotID.setter
    def RTAccessoryHolderSlotID(self, value: Optional[str]):
        if value is None:
            if "RTAccessoryHolderSlotID" in self._dataset:
                del self._dataset.RTAccessoryHolderSlotID
        else:
            self._dataset.RTAccessoryHolderSlotID = value

    @property
    def RTAccessorySlotDistance(self) -> Optional[float]:
        if "RTAccessorySlotDistance" in self._dataset:
            return self._dataset.RTAccessorySlotDistance
        return None

    @RTAccessorySlotDistance.setter
    def RTAccessorySlotDistance(self, value: Optional[float]):
        if value is None:
            if "RTAccessorySlotDistance" in self._dataset:
                del self._dataset.RTAccessorySlotDistance
        else:
            self._dataset.RTAccessorySlotDistance = value

    @property
    def RTAccessoryDeviceSlotID(self) -> Optional[str]:
        if "RTAccessoryDeviceSlotID" in self._dataset:
            return self._dataset.RTAccessoryDeviceSlotID
        return None

    @RTAccessoryDeviceSlotID.setter
    def RTAccessoryDeviceSlotID(self, value: Optional[str]):
        if value is None:
            if "RTAccessoryDeviceSlotID" in self._dataset:
                del self._dataset.RTAccessoryDeviceSlotID
        else:
            self._dataset.RTAccessoryDeviceSlotID = value

    @property
    def BeamModifierOrientationAngle(self) -> Optional[float]:
        if "BeamModifierOrientationAngle" in self._dataset:
            return self._dataset.BeamModifierOrientationAngle
        return None

    @BeamModifierOrientationAngle.setter
    def BeamModifierOrientationAngle(self, value: Optional[float]):
        if value is None:
            if "BeamModifierOrientationAngle" in self._dataset:
                del self._dataset.BeamModifierOrientationAngle
        else:
            self._dataset.BeamModifierOrientationAngle = value

    @property
    def BlockOrientation(self) -> Optional[str]:
        if "BlockOrientation" in self._dataset:
            return self._dataset.BlockOrientation
        return None

    @BlockOrientation.setter
    def BlockOrientation(self, value: Optional[str]):
        if value is None:
            if "BlockOrientation" in self._dataset:
                del self._dataset.BlockOrientation
        else:
            self._dataset.BlockOrientation = value

    @property
    def RadiationBeamBlockThickness(self) -> Optional[float]:
        if "RadiationBeamBlockThickness" in self._dataset:
            return self._dataset.RadiationBeamBlockThickness
        return None

    @RadiationBeamBlockThickness.setter
    def RadiationBeamBlockThickness(self, value: Optional[float]):
        if value is None:
            if "RadiationBeamBlockThickness" in self._dataset:
                del self._dataset.RadiationBeamBlockThickness
        else:
            self._dataset.RadiationBeamBlockThickness = value

    @property
    def BlockEdgeDataSequence(self) -> Optional[List[BlockEdgeDataSequenceItem]]:
        if "BlockEdgeDataSequence" in self._dataset:
            if len(self._BlockEdgeDataSequence) == len(self._dataset.BlockEdgeDataSequence):
                return self._BlockEdgeDataSequence
            else:
                return [BlockEdgeDataSequenceItem(x) for x in self._dataset.BlockEdgeDataSequence]
        return None

    @BlockEdgeDataSequence.setter
    def BlockEdgeDataSequence(self, value: Optional[List[BlockEdgeDataSequenceItem]]):
        if value is None:
            self._BlockEdgeDataSequence = []
            if "BlockEdgeDataSequence" in self._dataset:
                del self._dataset.BlockEdgeDataSequence
        elif not isinstance(value, list) or not all(isinstance(item, BlockEdgeDataSequenceItem) for item in value):
            raise ValueError(f"BlockEdgeDataSequence must be a list of BlockEdgeDataSequenceItem objects")
        else:
            self._BlockEdgeDataSequence = value
            if "BlockEdgeDataSequence" not in self._dataset:
                self._dataset.BlockEdgeDataSequence = pydicom.Sequence()
            self._dataset.BlockEdgeDataSequence.clear()
            self._dataset.BlockEdgeDataSequence.extend([item.to_dataset() for item in value])

    def add_BlockEdgeData(self, item: BlockEdgeDataSequenceItem):
        if not isinstance(item, BlockEdgeDataSequenceItem):
            raise ValueError(f"Item must be an instance of BlockEdgeDataSequenceItem")
        self._BlockEdgeDataSequence.append(item)
        if "BlockEdgeDataSequence" not in self._dataset:
            self._dataset.BlockEdgeDataSequence = pydicom.Sequence()
        self._dataset.BlockEdgeDataSequence.append(item.to_dataset())

    @property
    def ManufacturerModelVersion(self) -> Optional[str]:
        if "ManufacturerModelVersion" in self._dataset:
            return self._dataset.ManufacturerModelVersion
        return None

    @ManufacturerModelVersion.setter
    def ManufacturerModelVersion(self, value: Optional[str]):
        if value is None:
            if "ManufacturerModelVersion" in self._dataset:
                del self._dataset.ManufacturerModelVersion
        else:
            self._dataset.ManufacturerModelVersion = value

    @property
    def DeviceAlternateIdentifier(self) -> Optional[str]:
        if "DeviceAlternateIdentifier" in self._dataset:
            return self._dataset.DeviceAlternateIdentifier
        return None

    @DeviceAlternateIdentifier.setter
    def DeviceAlternateIdentifier(self, value: Optional[str]):
        if value is None:
            if "DeviceAlternateIdentifier" in self._dataset:
                del self._dataset.DeviceAlternateIdentifier
        else:
            self._dataset.DeviceAlternateIdentifier = value

    @property
    def DeviceAlternateIdentifierType(self) -> Optional[str]:
        if "DeviceAlternateIdentifierType" in self._dataset:
            return self._dataset.DeviceAlternateIdentifierType
        return None

    @DeviceAlternateIdentifierType.setter
    def DeviceAlternateIdentifierType(self, value: Optional[str]):
        if value is None:
            if "DeviceAlternateIdentifierType" in self._dataset:
                del self._dataset.DeviceAlternateIdentifierType
        else:
            self._dataset.DeviceAlternateIdentifierType = value

    @property
    def DeviceAlternateIdentifierFormat(self) -> Optional[str]:
        if "DeviceAlternateIdentifierFormat" in self._dataset:
            return self._dataset.DeviceAlternateIdentifierFormat
        return None

    @DeviceAlternateIdentifierFormat.setter
    def DeviceAlternateIdentifierFormat(self, value: Optional[str]):
        if value is None:
            if "DeviceAlternateIdentifierFormat" in self._dataset:
                del self._dataset.DeviceAlternateIdentifierFormat
        else:
            self._dataset.DeviceAlternateIdentifierFormat = value

    @property
    def DeviceLabel(self) -> Optional[str]:
        if "DeviceLabel" in self._dataset:
            return self._dataset.DeviceLabel
        return None

    @DeviceLabel.setter
    def DeviceLabel(self, value: Optional[str]):
        if value is None:
            if "DeviceLabel" in self._dataset:
                del self._dataset.DeviceLabel
        else:
            self._dataset.DeviceLabel = value

    @property
    def DeviceTypeCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "DeviceTypeCodeSequence" in self._dataset:
            if len(self._DeviceTypeCodeSequence) == len(self._dataset.DeviceTypeCodeSequence):
                return self._DeviceTypeCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.DeviceTypeCodeSequence]
        return None

    @DeviceTypeCodeSequence.setter
    def DeviceTypeCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._DeviceTypeCodeSequence = []
            if "DeviceTypeCodeSequence" in self._dataset:
                del self._dataset.DeviceTypeCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError(f"DeviceTypeCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._DeviceTypeCodeSequence = value
            if "DeviceTypeCodeSequence" not in self._dataset:
                self._dataset.DeviceTypeCodeSequence = pydicom.Sequence()
            self._dataset.DeviceTypeCodeSequence.clear()
            self._dataset.DeviceTypeCodeSequence.extend([item.to_dataset() for item in value])

    def add_DeviceTypeCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError(f"Item must be an instance of CodeSequenceItem")
        self._DeviceTypeCodeSequence.append(item)
        if "DeviceTypeCodeSequence" not in self._dataset:
            self._dataset.DeviceTypeCodeSequence = pydicom.Sequence()
        self._dataset.DeviceTypeCodeSequence.append(item.to_dataset())

    @property
    def DeviceIndex(self) -> Optional[int]:
        if "DeviceIndex" in self._dataset:
            return self._dataset.DeviceIndex
        return None

    @DeviceIndex.setter
    def DeviceIndex(self, value: Optional[int]):
        if value is None:
            if "DeviceIndex" in self._dataset:
                del self._dataset.DeviceIndex
        else:
            self._dataset.DeviceIndex = value

    @property
    def ManufacturerDeviceIdentifier(self) -> Optional[str]:
        if "ManufacturerDeviceIdentifier" in self._dataset:
            return self._dataset.ManufacturerDeviceIdentifier
        return None

    @ManufacturerDeviceIdentifier.setter
    def ManufacturerDeviceIdentifier(self, value: Optional[str]):
        if value is None:
            if "ManufacturerDeviceIdentifier" in self._dataset:
                del self._dataset.ManufacturerDeviceIdentifier
        else:
            self._dataset.ManufacturerDeviceIdentifier = value
