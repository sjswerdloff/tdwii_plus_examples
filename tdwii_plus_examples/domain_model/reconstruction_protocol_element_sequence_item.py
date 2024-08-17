from decimal import Decimal
from typing import Any, List, Optional  # noqa

import pydicom

from .code_sequence_item import CodeSequenceItem
from .reconstruction_algorithm_sequence_item import ReconstructionAlgorithmSequenceItem
from .reconstruction_end_location_sequence_item import (
    ReconstructionEndLocationSequenceItem,
)
from .reconstruction_start_location_sequence_item import (
    ReconstructionStartLocationSequenceItem,
)
from .reconstruction_target_center_location_sequence_item import (
    ReconstructionTargetCenterLocationSequenceItem,
)


class ReconstructionProtocolElementSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._DerivationCodeSequence: List[CodeSequenceItem] = []
        self._RequestedSeriesDescriptionCodeSequence: List[CodeSequenceItem] = []
        self._ReconstructionStartLocationSequence: List[ReconstructionStartLocationSequenceItem] = []
        self._ReconstructionEndLocationSequence: List[ReconstructionEndLocationSequenceItem] = []
        self._ReconstructionAlgorithmSequence: List[ReconstructionAlgorithmSequenceItem] = []
        self._ReconstructionTargetCenterLocationSequence: List[ReconstructionTargetCenterLocationSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ReferencedSOPClassUID(self) -> Optional[str]:
        if "ReferencedSOPClassUID" in self._dataset:
            return self._dataset.ReferencedSOPClassUID
        return None

    @ReferencedSOPClassUID.setter
    def ReferencedSOPClassUID(self, value: Optional[str]):
        if value is None:
            if "ReferencedSOPClassUID" in self._dataset:
                del self._dataset.ReferencedSOPClassUID
        else:
            self._dataset.ReferencedSOPClassUID = value

    @property
    def ReferencedSOPInstanceUID(self) -> Optional[str]:
        if "ReferencedSOPInstanceUID" in self._dataset:
            return self._dataset.ReferencedSOPInstanceUID
        return None

    @ReferencedSOPInstanceUID.setter
    def ReferencedSOPInstanceUID(self, value: Optional[str]):
        if value is None:
            if "ReferencedSOPInstanceUID" in self._dataset:
                del self._dataset.ReferencedSOPInstanceUID
        else:
            self._dataset.ReferencedSOPInstanceUID = value

    @property
    def DerivationCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "DerivationCodeSequence" in self._dataset:
            if len(self._DerivationCodeSequence) == len(self._dataset.DerivationCodeSequence):
                return self._DerivationCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.DerivationCodeSequence]
        return None

    @DerivationCodeSequence.setter
    def DerivationCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._DerivationCodeSequence = []
            if "DerivationCodeSequence" in self._dataset:
                del self._dataset.DerivationCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("DerivationCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._DerivationCodeSequence = value
            if "DerivationCodeSequence" not in self._dataset:
                self._dataset.DerivationCodeSequence = pydicom.Sequence()
            self._dataset.DerivationCodeSequence.clear()
            self._dataset.DerivationCodeSequence.extend([item.to_dataset() for item in value])

    def add_DerivationCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._DerivationCodeSequence.append(item)
        if "DerivationCodeSequence" not in self._dataset:
            self._dataset.DerivationCodeSequence = pydicom.Sequence()
        self._dataset.DerivationCodeSequence.append(item.to_dataset())

    @property
    def SliceThickness(self) -> Optional[Decimal]:
        if "SliceThickness" in self._dataset:
            return self._dataset.SliceThickness
        return None

    @SliceThickness.setter
    def SliceThickness(self, value: Optional[Decimal]):
        if value is None:
            if "SliceThickness" in self._dataset:
                del self._dataset.SliceThickness
        else:
            self._dataset.SliceThickness = value

    @property
    def SpacingBetweenSlices(self) -> Optional[Decimal]:
        if "SpacingBetweenSlices" in self._dataset:
            return self._dataset.SpacingBetweenSlices
        return None

    @SpacingBetweenSlices.setter
    def SpacingBetweenSlices(self, value: Optional[Decimal]):
        if value is None:
            if "SpacingBetweenSlices" in self._dataset:
                del self._dataset.SpacingBetweenSlices
        else:
            self._dataset.SpacingBetweenSlices = value

    @property
    def ReconstructionDiameter(self) -> Optional[Decimal]:
        if "ReconstructionDiameter" in self._dataset:
            return self._dataset.ReconstructionDiameter
        return None

    @ReconstructionDiameter.setter
    def ReconstructionDiameter(self, value: Optional[Decimal]):
        if value is None:
            if "ReconstructionDiameter" in self._dataset:
                del self._dataset.ReconstructionDiameter
        else:
            self._dataset.ReconstructionDiameter = value

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
    def ConvolutionKernel(self) -> Optional[List[str]]:
        if "ConvolutionKernel" in self._dataset:
            return self._dataset.ConvolutionKernel
        return None

    @ConvolutionKernel.setter
    def ConvolutionKernel(self, value: Optional[List[str]]):
        if value is None:
            if "ConvolutionKernel" in self._dataset:
                del self._dataset.ConvolutionKernel
        else:
            self._dataset.ConvolutionKernel = value

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
    def ConvolutionKernelGroup(self) -> Optional[str]:
        if "ConvolutionKernelGroup" in self._dataset:
            return self._dataset.ConvolutionKernelGroup
        return None

    @ConvolutionKernelGroup.setter
    def ConvolutionKernelGroup(self, value: Optional[str]):
        if value is None:
            if "ConvolutionKernelGroup" in self._dataset:
                del self._dataset.ConvolutionKernelGroup
        else:
            self._dataset.ConvolutionKernelGroup = value

    @property
    def ReconstructionFieldOfView(self) -> Optional[List[float]]:
        if "ReconstructionFieldOfView" in self._dataset:
            return self._dataset.ReconstructionFieldOfView
        return None

    @ReconstructionFieldOfView.setter
    def ReconstructionFieldOfView(self, value: Optional[List[float]]):
        if value is None:
            if "ReconstructionFieldOfView" in self._dataset:
                del self._dataset.ReconstructionFieldOfView
        else:
            self._dataset.ReconstructionFieldOfView = value

    @property
    def ReconstructionTargetCenterPatient(self) -> Optional[List[float]]:
        if "ReconstructionTargetCenterPatient" in self._dataset:
            return self._dataset.ReconstructionTargetCenterPatient
        return None

    @ReconstructionTargetCenterPatient.setter
    def ReconstructionTargetCenterPatient(self, value: Optional[List[float]]):
        if value is None:
            if "ReconstructionTargetCenterPatient" in self._dataset:
                del self._dataset.ReconstructionTargetCenterPatient
        else:
            self._dataset.ReconstructionTargetCenterPatient = value

    @property
    def ReconstructionAngle(self) -> Optional[float]:
        if "ReconstructionAngle" in self._dataset:
            return self._dataset.ReconstructionAngle
        return None

    @ReconstructionAngle.setter
    def ReconstructionAngle(self, value: Optional[float]):
        if value is None:
            if "ReconstructionAngle" in self._dataset:
                del self._dataset.ReconstructionAngle
        else:
            self._dataset.ReconstructionAngle = value

    @property
    def ImageFilter(self) -> Optional[str]:
        if "ImageFilter" in self._dataset:
            return self._dataset.ImageFilter
        return None

    @ImageFilter.setter
    def ImageFilter(self, value: Optional[str]):
        if value is None:
            if "ImageFilter" in self._dataset:
                del self._dataset.ImageFilter
        else:
            self._dataset.ImageFilter = value

    @property
    def ReconstructionPixelSpacing(self) -> Optional[List[float]]:
        if "ReconstructionPixelSpacing" in self._dataset:
            return self._dataset.ReconstructionPixelSpacing
        return None

    @ReconstructionPixelSpacing.setter
    def ReconstructionPixelSpacing(self, value: Optional[List[float]]):
        if value is None:
            if "ReconstructionPixelSpacing" in self._dataset:
                del self._dataset.ReconstructionPixelSpacing
        else:
            self._dataset.ReconstructionPixelSpacing = value

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

    @property
    def SourceAcquisitionProtocolElementNumber(self) -> Optional[List[int]]:
        if "SourceAcquisitionProtocolElementNumber" in self._dataset:
            return self._dataset.SourceAcquisitionProtocolElementNumber
        return None

    @SourceAcquisitionProtocolElementNumber.setter
    def SourceAcquisitionProtocolElementNumber(self, value: Optional[List[int]]):
        if value is None:
            if "SourceAcquisitionProtocolElementNumber" in self._dataset:
                del self._dataset.SourceAcquisitionProtocolElementNumber
        else:
            self._dataset.SourceAcquisitionProtocolElementNumber = value

    @property
    def SourceAcquisitionBeamNumber(self) -> Optional[List[int]]:
        if "SourceAcquisitionBeamNumber" in self._dataset:
            return self._dataset.SourceAcquisitionBeamNumber
        return None

    @SourceAcquisitionBeamNumber.setter
    def SourceAcquisitionBeamNumber(self, value: Optional[List[int]]):
        if value is None:
            if "SourceAcquisitionBeamNumber" in self._dataset:
                del self._dataset.SourceAcquisitionBeamNumber
        else:
            self._dataset.SourceAcquisitionBeamNumber = value

    @property
    def ReconstructionStartLocationSequence(self) -> Optional[List[ReconstructionStartLocationSequenceItem]]:
        if "ReconstructionStartLocationSequence" in self._dataset:
            if len(self._ReconstructionStartLocationSequence) == len(self._dataset.ReconstructionStartLocationSequence):
                return self._ReconstructionStartLocationSequence
            else:
                return [ReconstructionStartLocationSequenceItem(x) for x in self._dataset.ReconstructionStartLocationSequence]
        return None

    @ReconstructionStartLocationSequence.setter
    def ReconstructionStartLocationSequence(self, value: Optional[List[ReconstructionStartLocationSequenceItem]]):
        if value is None:
            self._ReconstructionStartLocationSequence = []
            if "ReconstructionStartLocationSequence" in self._dataset:
                del self._dataset.ReconstructionStartLocationSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, ReconstructionStartLocationSequenceItem) for item in value
        ):
            raise ValueError(
                "ReconstructionStartLocationSequence must be a list of ReconstructionStartLocationSequenceItem objects"
            )
        else:
            self._ReconstructionStartLocationSequence = value
            if "ReconstructionStartLocationSequence" not in self._dataset:
                self._dataset.ReconstructionStartLocationSequence = pydicom.Sequence()
            self._dataset.ReconstructionStartLocationSequence.clear()
            self._dataset.ReconstructionStartLocationSequence.extend([item.to_dataset() for item in value])

    def add_ReconstructionStartLocation(self, item: ReconstructionStartLocationSequenceItem):
        if not isinstance(item, ReconstructionStartLocationSequenceItem):
            raise ValueError("Item must be an instance of ReconstructionStartLocationSequenceItem")
        self._ReconstructionStartLocationSequence.append(item)
        if "ReconstructionStartLocationSequence" not in self._dataset:
            self._dataset.ReconstructionStartLocationSequence = pydicom.Sequence()
        self._dataset.ReconstructionStartLocationSequence.append(item.to_dataset())

    @property
    def ReconstructionEndLocationSequence(self) -> Optional[List[ReconstructionEndLocationSequenceItem]]:
        if "ReconstructionEndLocationSequence" in self._dataset:
            if len(self._ReconstructionEndLocationSequence) == len(self._dataset.ReconstructionEndLocationSequence):
                return self._ReconstructionEndLocationSequence
            else:
                return [ReconstructionEndLocationSequenceItem(x) for x in self._dataset.ReconstructionEndLocationSequence]
        return None

    @ReconstructionEndLocationSequence.setter
    def ReconstructionEndLocationSequence(self, value: Optional[List[ReconstructionEndLocationSequenceItem]]):
        if value is None:
            self._ReconstructionEndLocationSequence = []
            if "ReconstructionEndLocationSequence" in self._dataset:
                del self._dataset.ReconstructionEndLocationSequence
        elif not isinstance(value, list) or not all(isinstance(item, ReconstructionEndLocationSequenceItem) for item in value):
            raise ValueError(
                "ReconstructionEndLocationSequence must be a list of ReconstructionEndLocationSequenceItem objects"
            )
        else:
            self._ReconstructionEndLocationSequence = value
            if "ReconstructionEndLocationSequence" not in self._dataset:
                self._dataset.ReconstructionEndLocationSequence = pydicom.Sequence()
            self._dataset.ReconstructionEndLocationSequence.clear()
            self._dataset.ReconstructionEndLocationSequence.extend([item.to_dataset() for item in value])

    def add_ReconstructionEndLocation(self, item: ReconstructionEndLocationSequenceItem):
        if not isinstance(item, ReconstructionEndLocationSequenceItem):
            raise ValueError("Item must be an instance of ReconstructionEndLocationSequenceItem")
        self._ReconstructionEndLocationSequence.append(item)
        if "ReconstructionEndLocationSequence" not in self._dataset:
            self._dataset.ReconstructionEndLocationSequence = pydicom.Sequence()
        self._dataset.ReconstructionEndLocationSequence.append(item.to_dataset())

    @property
    def ReconstructionAlgorithmSequence(self) -> Optional[List[ReconstructionAlgorithmSequenceItem]]:
        if "ReconstructionAlgorithmSequence" in self._dataset:
            if len(self._ReconstructionAlgorithmSequence) == len(self._dataset.ReconstructionAlgorithmSequence):
                return self._ReconstructionAlgorithmSequence
            else:
                return [ReconstructionAlgorithmSequenceItem(x) for x in self._dataset.ReconstructionAlgorithmSequence]
        return None

    @ReconstructionAlgorithmSequence.setter
    def ReconstructionAlgorithmSequence(self, value: Optional[List[ReconstructionAlgorithmSequenceItem]]):
        if value is None:
            self._ReconstructionAlgorithmSequence = []
            if "ReconstructionAlgorithmSequence" in self._dataset:
                del self._dataset.ReconstructionAlgorithmSequence
        elif not isinstance(value, list) or not all(isinstance(item, ReconstructionAlgorithmSequenceItem) for item in value):
            raise ValueError("ReconstructionAlgorithmSequence must be a list of ReconstructionAlgorithmSequenceItem objects")
        else:
            self._ReconstructionAlgorithmSequence = value
            if "ReconstructionAlgorithmSequence" not in self._dataset:
                self._dataset.ReconstructionAlgorithmSequence = pydicom.Sequence()
            self._dataset.ReconstructionAlgorithmSequence.clear()
            self._dataset.ReconstructionAlgorithmSequence.extend([item.to_dataset() for item in value])

    def add_ReconstructionAlgorithm(self, item: ReconstructionAlgorithmSequenceItem):
        if not isinstance(item, ReconstructionAlgorithmSequenceItem):
            raise ValueError("Item must be an instance of ReconstructionAlgorithmSequenceItem")
        self._ReconstructionAlgorithmSequence.append(item)
        if "ReconstructionAlgorithmSequence" not in self._dataset:
            self._dataset.ReconstructionAlgorithmSequence = pydicom.Sequence()
        self._dataset.ReconstructionAlgorithmSequence.append(item.to_dataset())

    @property
    def ReconstructionTargetCenterLocationSequence(self) -> Optional[List[ReconstructionTargetCenterLocationSequenceItem]]:
        if "ReconstructionTargetCenterLocationSequence" in self._dataset:
            if len(self._ReconstructionTargetCenterLocationSequence) == len(
                self._dataset.ReconstructionTargetCenterLocationSequence
            ):
                return self._ReconstructionTargetCenterLocationSequence
            else:
                return [
                    ReconstructionTargetCenterLocationSequenceItem(x)
                    for x in self._dataset.ReconstructionTargetCenterLocationSequence
                ]
        return None

    @ReconstructionTargetCenterLocationSequence.setter
    def ReconstructionTargetCenterLocationSequence(
        self, value: Optional[List[ReconstructionTargetCenterLocationSequenceItem]]
    ):
        if value is None:
            self._ReconstructionTargetCenterLocationSequence = []
            if "ReconstructionTargetCenterLocationSequence" in self._dataset:
                del self._dataset.ReconstructionTargetCenterLocationSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, ReconstructionTargetCenterLocationSequenceItem) for item in value
        ):
            raise ValueError(
                "ReconstructionTargetCenterLocationSequence must be a list of ReconstructionTargetCenterLocationSequenceItem"
                " objects"
            )
        else:
            self._ReconstructionTargetCenterLocationSequence = value
            if "ReconstructionTargetCenterLocationSequence" not in self._dataset:
                self._dataset.ReconstructionTargetCenterLocationSequence = pydicom.Sequence()
            self._dataset.ReconstructionTargetCenterLocationSequence.clear()
            self._dataset.ReconstructionTargetCenterLocationSequence.extend([item.to_dataset() for item in value])

    def add_ReconstructionTargetCenterLocation(self, item: ReconstructionTargetCenterLocationSequenceItem):
        if not isinstance(item, ReconstructionTargetCenterLocationSequenceItem):
            raise ValueError("Item must be an instance of ReconstructionTargetCenterLocationSequenceItem")
        self._ReconstructionTargetCenterLocationSequence.append(item)
        if "ReconstructionTargetCenterLocationSequence" not in self._dataset:
            self._dataset.ReconstructionTargetCenterLocationSequence = pydicom.Sequence()
        self._dataset.ReconstructionTargetCenterLocationSequence.append(item.to_dataset())

    @property
    def ImageFilterDescription(self) -> Optional[str]:
        if "ImageFilterDescription" in self._dataset:
            return self._dataset.ImageFilterDescription
        return None

    @ImageFilterDescription.setter
    def ImageFilterDescription(self, value: Optional[str]):
        if value is None:
            if "ImageFilterDescription" in self._dataset:
                del self._dataset.ImageFilterDescription
        else:
            self._dataset.ImageFilterDescription = value

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
    def WindowCenter(self) -> Optional[List[Decimal]]:
        if "WindowCenter" in self._dataset:
            return self._dataset.WindowCenter
        return None

    @WindowCenter.setter
    def WindowCenter(self, value: Optional[List[Decimal]]):
        if value is None:
            if "WindowCenter" in self._dataset:
                del self._dataset.WindowCenter
        else:
            self._dataset.WindowCenter = value

    @property
    def WindowWidth(self) -> Optional[List[Decimal]]:
        if "WindowWidth" in self._dataset:
            return self._dataset.WindowWidth
        return None

    @WindowWidth.setter
    def WindowWidth(self, value: Optional[List[Decimal]]):
        if value is None:
            if "WindowWidth" in self._dataset:
                del self._dataset.WindowWidth
        else:
            self._dataset.WindowWidth = value
