from decimal import Decimal
from typing import Any, List, Optional  # noqa

import pydicom

from .code_sequence_item import CodeSequenceItem
from .image_filter_details_sequence_item import ImageFilterDetailsSequenceItem
from .referenced_defined_protocol_sequence_item import (
    ReferencedDefinedProtocolSequenceItem,
)
from .referenced_performed_protocol_sequence_item import (
    ReferencedPerformedProtocolSequenceItem,
)


class ReconstructionProtocolElementSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._DerivationCodeSequence: List[CodeSequenceItem] = []
        self._ImageFilterDetailsSequence: List[ImageFilterDetailsSequenceItem] = []
        self._RequestedSeriesDescriptionCodeSequence: List[CodeSequenceItem] = []
        self._ReferencedDefinedProtocolSequence: List[ReferencedDefinedProtocolSequenceItem] = []
        self._ReferencedPerformedProtocolSequence: List[ReferencedPerformedProtocolSequenceItem] = []

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
    def ReconstructionPipelineType(self) -> Optional[str]:
        if "ReconstructionPipelineType" in self._dataset:
            return self._dataset.ReconstructionPipelineType
        return None

    @ReconstructionPipelineType.setter
    def ReconstructionPipelineType(self, value: Optional[str]):
        if value is None:
            if "ReconstructionPipelineType" in self._dataset:
                del self._dataset.ReconstructionPipelineType
        else:
            self._dataset.ReconstructionPipelineType = value

    @property
    def ImageFilterDetailsSequence(self) -> Optional[List[ImageFilterDetailsSequenceItem]]:
        if "ImageFilterDetailsSequence" in self._dataset:
            if len(self._ImageFilterDetailsSequence) == len(self._dataset.ImageFilterDetailsSequence):
                return self._ImageFilterDetailsSequence
            else:
                return [ImageFilterDetailsSequenceItem(x) for x in self._dataset.ImageFilterDetailsSequence]
        return None

    @ImageFilterDetailsSequence.setter
    def ImageFilterDetailsSequence(self, value: Optional[List[ImageFilterDetailsSequenceItem]]):
        if value is None:
            self._ImageFilterDetailsSequence = []
            if "ImageFilterDetailsSequence" in self._dataset:
                del self._dataset.ImageFilterDetailsSequence
        elif not isinstance(value, list) or not all(isinstance(item, ImageFilterDetailsSequenceItem) for item in value):
            raise ValueError("ImageFilterDetailsSequence must be a list of ImageFilterDetailsSequenceItem objects")
        else:
            self._ImageFilterDetailsSequence = value
            if "ImageFilterDetailsSequence" not in self._dataset:
                self._dataset.ImageFilterDetailsSequence = pydicom.Sequence()
            self._dataset.ImageFilterDetailsSequence.clear()
            self._dataset.ImageFilterDetailsSequence.extend([item.to_dataset() for item in value])

    def add_ImageFilterDetails(self, item: ImageFilterDetailsSequenceItem):
        if not isinstance(item, ImageFilterDetailsSequenceItem):
            raise ValueError("Item must be an instance of ImageFilterDetailsSequenceItem")
        self._ImageFilterDetailsSequence.append(item)
        if "ImageFilterDetailsSequence" not in self._dataset:
            self._dataset.ImageFilterDetailsSequence = pydicom.Sequence()
        self._dataset.ImageFilterDetailsSequence.append(item.to_dataset())

    @property
    def AppliedMaskSubtractionFlag(self) -> Optional[str]:
        if "AppliedMaskSubtractionFlag" in self._dataset:
            return self._dataset.AppliedMaskSubtractionFlag
        return None

    @AppliedMaskSubtractionFlag.setter
    def AppliedMaskSubtractionFlag(self, value: Optional[str]):
        if value is None:
            if "AppliedMaskSubtractionFlag" in self._dataset:
                del self._dataset.AppliedMaskSubtractionFlag
        else:
            self._dataset.AppliedMaskSubtractionFlag = value

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
    def AlgorithmType(self) -> Optional[str]:
        if "AlgorithmType" in self._dataset:
            return self._dataset.AlgorithmType
        return None

    @AlgorithmType.setter
    def AlgorithmType(self, value: Optional[str]):
        if value is None:
            if "AlgorithmType" in self._dataset:
                del self._dataset.AlgorithmType
        else:
            self._dataset.AlgorithmType = value

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

    @property
    def MaskVisibilityPercentage(self) -> Optional[float]:
        if "MaskVisibilityPercentage" in self._dataset:
            return self._dataset.MaskVisibilityPercentage
        return None

    @MaskVisibilityPercentage.setter
    def MaskVisibilityPercentage(self, value: Optional[float]):
        if value is None:
            if "MaskVisibilityPercentage" in self._dataset:
                del self._dataset.MaskVisibilityPercentage
        else:
            self._dataset.MaskVisibilityPercentage = value

    @property
    def NumberOfSlices(self) -> Optional[int]:
        if "NumberOfSlices" in self._dataset:
            return self._dataset.NumberOfSlices
        return None

    @NumberOfSlices.setter
    def NumberOfSlices(self, value: Optional[int]):
        if value is None:
            if "NumberOfSlices" in self._dataset:
                del self._dataset.NumberOfSlices
        else:
            self._dataset.NumberOfSlices = value

    @property
    def ImageHorizontalFlip(self) -> Optional[str]:
        if "ImageHorizontalFlip" in self._dataset:
            return self._dataset.ImageHorizontalFlip
        return None

    @ImageHorizontalFlip.setter
    def ImageHorizontalFlip(self, value: Optional[str]):
        if value is None:
            if "ImageHorizontalFlip" in self._dataset:
                del self._dataset.ImageHorizontalFlip
        else:
            self._dataset.ImageHorizontalFlip = value

    @property
    def ImageRotation(self) -> Optional[int]:
        if "ImageRotation" in self._dataset:
            return self._dataset.ImageRotation
        return None

    @ImageRotation.setter
    def ImageRotation(self, value: Optional[int]):
        if value is None:
            if "ImageRotation" in self._dataset:
                del self._dataset.ImageRotation
        else:
            self._dataset.ImageRotation = value
