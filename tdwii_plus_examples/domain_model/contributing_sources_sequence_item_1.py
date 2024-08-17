from decimal import Decimal
from typing import Any, List, Optional  # noqa

import pydicom

from .code_sequence_item import CodeSequenceItem
from .contributing_sop_instances_reference_sequence_item import (
    ContributingSOPInstancesReferenceSequenceItem,
)
from .operator_identification_sequence_item import OperatorIdentificationSequenceItem


class ContributingSourcesSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._OperatorIdentificationSequence: List[OperatorIdentificationSequenceItem] = []
        self._ContributingSOPInstancesReferenceSequence: List[ContributingSOPInstancesReferenceSequenceItem] = []
        self._PerformedProtocolCodeSequence: List[CodeSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def AcquisitionDateTime(self) -> Optional[str]:
        if "AcquisitionDateTime" in self._dataset:
            return self._dataset.AcquisitionDateTime
        return None

    @AcquisitionDateTime.setter
    def AcquisitionDateTime(self, value: Optional[str]):
        if value is None:
            if "AcquisitionDateTime" in self._dataset:
                del self._dataset.AcquisitionDateTime
        else:
            self._dataset.AcquisitionDateTime = value

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
    def StationName(self) -> Optional[str]:
        if "StationName" in self._dataset:
            return self._dataset.StationName
        return None

    @StationName.setter
    def StationName(self, value: Optional[str]):
        if value is None:
            if "StationName" in self._dataset:
                del self._dataset.StationName
        else:
            self._dataset.StationName = value

    @property
    def OperatorsName(self) -> Optional[List[str]]:
        if "OperatorsName" in self._dataset:
            return self._dataset.OperatorsName
        return None

    @OperatorsName.setter
    def OperatorsName(self, value: Optional[List[str]]):
        if value is None:
            if "OperatorsName" in self._dataset:
                del self._dataset.OperatorsName
        else:
            self._dataset.OperatorsName = value

    @property
    def OperatorIdentificationSequence(self) -> Optional[List[OperatorIdentificationSequenceItem]]:
        if "OperatorIdentificationSequence" in self._dataset:
            if len(self._OperatorIdentificationSequence) == len(self._dataset.OperatorIdentificationSequence):
                return self._OperatorIdentificationSequence
            else:
                return [OperatorIdentificationSequenceItem(x) for x in self._dataset.OperatorIdentificationSequence]
        return None

    @OperatorIdentificationSequence.setter
    def OperatorIdentificationSequence(self, value: Optional[List[OperatorIdentificationSequenceItem]]):
        if value is None:
            self._OperatorIdentificationSequence = []
            if "OperatorIdentificationSequence" in self._dataset:
                del self._dataset.OperatorIdentificationSequence
        elif not isinstance(value, list) or not all(isinstance(item, OperatorIdentificationSequenceItem) for item in value):
            raise ValueError("OperatorIdentificationSequence must be a list of OperatorIdentificationSequenceItem objects")
        else:
            self._OperatorIdentificationSequence = value
            if "OperatorIdentificationSequence" not in self._dataset:
                self._dataset.OperatorIdentificationSequence = pydicom.Sequence()
            self._dataset.OperatorIdentificationSequence.clear()
            self._dataset.OperatorIdentificationSequence.extend([item.to_dataset() for item in value])

    def add_OperatorIdentification(self, item: OperatorIdentificationSequenceItem):
        if not isinstance(item, OperatorIdentificationSequenceItem):
            raise ValueError("Item must be an instance of OperatorIdentificationSequenceItem")
        self._OperatorIdentificationSequence.append(item)
        if "OperatorIdentificationSequence" not in self._dataset:
            self._dataset.OperatorIdentificationSequence = pydicom.Sequence()
        self._dataset.OperatorIdentificationSequence.append(item.to_dataset())

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
    def ProtocolName(self) -> Optional[str]:
        if "ProtocolName" in self._dataset:
            return self._dataset.ProtocolName
        return None

    @ProtocolName.setter
    def ProtocolName(self, value: Optional[str]):
        if value is None:
            if "ProtocolName" in self._dataset:
                del self._dataset.ProtocolName
        else:
            self._dataset.ProtocolName = value

    @property
    def ImagerPixelSpacing(self) -> Optional[List[Decimal]]:
        if "ImagerPixelSpacing" in self._dataset:
            return self._dataset.ImagerPixelSpacing
        return None

    @ImagerPixelSpacing.setter
    def ImagerPixelSpacing(self, value: Optional[List[Decimal]]):
        if value is None:
            if "ImagerPixelSpacing" in self._dataset:
                del self._dataset.ImagerPixelSpacing
        else:
            self._dataset.ImagerPixelSpacing = value

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
    def AcquisitionDeviceProcessingDescription(self) -> Optional[str]:
        if "AcquisitionDeviceProcessingDescription" in self._dataset:
            return self._dataset.AcquisitionDeviceProcessingDescription
        return None

    @AcquisitionDeviceProcessingDescription.setter
    def AcquisitionDeviceProcessingDescription(self, value: Optional[str]):
        if value is None:
            if "AcquisitionDeviceProcessingDescription" in self._dataset:
                del self._dataset.AcquisitionDeviceProcessingDescription
        else:
            self._dataset.AcquisitionDeviceProcessingDescription = value

    @property
    def AcquisitionDeviceProcessingCode(self) -> Optional[str]:
        if "AcquisitionDeviceProcessingCode" in self._dataset:
            return self._dataset.AcquisitionDeviceProcessingCode
        return None

    @AcquisitionDeviceProcessingCode.setter
    def AcquisitionDeviceProcessingCode(self, value: Optional[str]):
        if value is None:
            if "AcquisitionDeviceProcessingCode" in self._dataset:
                del self._dataset.AcquisitionDeviceProcessingCode
        else:
            self._dataset.AcquisitionDeviceProcessingCode = value

    @property
    def AcquisitionProtocolName(self) -> Optional[str]:
        if "AcquisitionProtocolName" in self._dataset:
            return self._dataset.AcquisitionProtocolName
        return None

    @AcquisitionProtocolName.setter
    def AcquisitionProtocolName(self, value: Optional[str]):
        if value is None:
            if "AcquisitionProtocolName" in self._dataset:
                del self._dataset.AcquisitionProtocolName
        else:
            self._dataset.AcquisitionProtocolName = value

    @property
    def ContributingSOPInstancesReferenceSequence(self) -> Optional[List[ContributingSOPInstancesReferenceSequenceItem]]:
        if "ContributingSOPInstancesReferenceSequence" in self._dataset:
            if len(self._ContributingSOPInstancesReferenceSequence) == len(
                self._dataset.ContributingSOPInstancesReferenceSequence
            ):
                return self._ContributingSOPInstancesReferenceSequence
            else:
                return [
                    ContributingSOPInstancesReferenceSequenceItem(x)
                    for x in self._dataset.ContributingSOPInstancesReferenceSequence
                ]
        return None

    @ContributingSOPInstancesReferenceSequence.setter
    def ContributingSOPInstancesReferenceSequence(self, value: Optional[List[ContributingSOPInstancesReferenceSequenceItem]]):
        if value is None:
            self._ContributingSOPInstancesReferenceSequence = []
            if "ContributingSOPInstancesReferenceSequence" in self._dataset:
                del self._dataset.ContributingSOPInstancesReferenceSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, ContributingSOPInstancesReferenceSequenceItem) for item in value
        ):
            raise ValueError(
                "ContributingSOPInstancesReferenceSequence must be a list of ContributingSOPInstancesReferenceSequenceItem"
                " objects"
            )
        else:
            self._ContributingSOPInstancesReferenceSequence = value
            if "ContributingSOPInstancesReferenceSequence" not in self._dataset:
                self._dataset.ContributingSOPInstancesReferenceSequence = pydicom.Sequence()
            self._dataset.ContributingSOPInstancesReferenceSequence.clear()
            self._dataset.ContributingSOPInstancesReferenceSequence.extend([item.to_dataset() for item in value])

    def add_ContributingSOPInstancesReference(self, item: ContributingSOPInstancesReferenceSequenceItem):
        if not isinstance(item, ContributingSOPInstancesReferenceSequenceItem):
            raise ValueError("Item must be an instance of ContributingSOPInstancesReferenceSequenceItem")
        self._ContributingSOPInstancesReferenceSequence.append(item)
        if "ContributingSOPInstancesReferenceSequence" not in self._dataset:
            self._dataset.ContributingSOPInstancesReferenceSequence = pydicom.Sequence()
        self._dataset.ContributingSOPInstancesReferenceSequence.append(item.to_dataset())

    @property
    def Rows(self) -> Optional[int]:
        if "Rows" in self._dataset:
            return self._dataset.Rows
        return None

    @Rows.setter
    def Rows(self, value: Optional[int]):
        if value is None:
            if "Rows" in self._dataset:
                del self._dataset.Rows
        else:
            self._dataset.Rows = value

    @property
    def Columns(self) -> Optional[int]:
        if "Columns" in self._dataset:
            return self._dataset.Columns
        return None

    @Columns.setter
    def Columns(self, value: Optional[int]):
        if value is None:
            if "Columns" in self._dataset:
                del self._dataset.Columns
        else:
            self._dataset.Columns = value

    @property
    def BitsStored(self) -> Optional[int]:
        if "BitsStored" in self._dataset:
            return self._dataset.BitsStored
        return None

    @BitsStored.setter
    def BitsStored(self, value: Optional[int]):
        if value is None:
            if "BitsStored" in self._dataset:
                del self._dataset.BitsStored
        else:
            self._dataset.BitsStored = value

    @property
    def LossyImageCompression(self) -> Optional[str]:
        if "LossyImageCompression" in self._dataset:
            return self._dataset.LossyImageCompression
        return None

    @LossyImageCompression.setter
    def LossyImageCompression(self, value: Optional[str]):
        if value is None:
            if "LossyImageCompression" in self._dataset:
                del self._dataset.LossyImageCompression
        else:
            self._dataset.LossyImageCompression = value

    @property
    def LossyImageCompressionRatio(self) -> Optional[List[Decimal]]:
        if "LossyImageCompressionRatio" in self._dataset:
            return self._dataset.LossyImageCompressionRatio
        return None

    @LossyImageCompressionRatio.setter
    def LossyImageCompressionRatio(self, value: Optional[List[Decimal]]):
        if value is None:
            if "LossyImageCompressionRatio" in self._dataset:
                del self._dataset.LossyImageCompressionRatio
        else:
            self._dataset.LossyImageCompressionRatio = value

    @property
    def LossyImageCompressionMethod(self) -> Optional[List[str]]:
        if "LossyImageCompressionMethod" in self._dataset:
            return self._dataset.LossyImageCompressionMethod
        return None

    @LossyImageCompressionMethod.setter
    def LossyImageCompressionMethod(self, value: Optional[List[str]]):
        if value is None:
            if "LossyImageCompressionMethod" in self._dataset:
                del self._dataset.LossyImageCompressionMethod
        else:
            self._dataset.LossyImageCompressionMethod = value

    @property
    def PerformedProtocolCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "PerformedProtocolCodeSequence" in self._dataset:
            if len(self._PerformedProtocolCodeSequence) == len(self._dataset.PerformedProtocolCodeSequence):
                return self._PerformedProtocolCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.PerformedProtocolCodeSequence]
        return None

    @PerformedProtocolCodeSequence.setter
    def PerformedProtocolCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._PerformedProtocolCodeSequence = []
            if "PerformedProtocolCodeSequence" in self._dataset:
                del self._dataset.PerformedProtocolCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("PerformedProtocolCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._PerformedProtocolCodeSequence = value
            if "PerformedProtocolCodeSequence" not in self._dataset:
                self._dataset.PerformedProtocolCodeSequence = pydicom.Sequence()
            self._dataset.PerformedProtocolCodeSequence.clear()
            self._dataset.PerformedProtocolCodeSequence.extend([item.to_dataset() for item in value])

    def add_PerformedProtocolCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._PerformedProtocolCodeSequence.append(item)
        if "PerformedProtocolCodeSequence" not in self._dataset:
            self._dataset.PerformedProtocolCodeSequence = pydicom.Sequence()
        self._dataset.PerformedProtocolCodeSequence.append(item.to_dataset())
