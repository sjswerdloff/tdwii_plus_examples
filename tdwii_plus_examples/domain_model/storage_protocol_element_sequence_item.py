from typing import Any, List, Optional  # noqa

import pydicom

from .output_information_sequence_item import OutputInformationSequenceItem


class StorageProtocolElementSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._OutputInformationSequence: List[OutputInformationSequenceItem] = []

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
    def SourceReconstructionProtocolElementNumber(self) -> Optional[List[int]]:
        if "SourceReconstructionProtocolElementNumber" in self._dataset:
            return self._dataset.SourceReconstructionProtocolElementNumber
        return None

    @SourceReconstructionProtocolElementNumber.setter
    def SourceReconstructionProtocolElementNumber(self, value: Optional[List[int]]):
        if value is None:
            if "SourceReconstructionProtocolElementNumber" in self._dataset:
                del self._dataset.SourceReconstructionProtocolElementNumber
        else:
            self._dataset.SourceReconstructionProtocolElementNumber = value

    @property
    def OutputInformationSequence(self) -> Optional[List[OutputInformationSequenceItem]]:
        if "OutputInformationSequence" in self._dataset:
            if len(self._OutputInformationSequence) == len(self._dataset.OutputInformationSequence):
                return self._OutputInformationSequence
            else:
                return [OutputInformationSequenceItem(x) for x in self._dataset.OutputInformationSequence]
        return None

    @OutputInformationSequence.setter
    def OutputInformationSequence(self, value: Optional[List[OutputInformationSequenceItem]]):
        if value is None:
            self._OutputInformationSequence = []
            if "OutputInformationSequence" in self._dataset:
                del self._dataset.OutputInformationSequence
        elif not isinstance(value, list) or not all(isinstance(item, OutputInformationSequenceItem) for item in value):
            raise ValueError("OutputInformationSequence must be a list of OutputInformationSequenceItem objects")
        else:
            self._OutputInformationSequence = value
            if "OutputInformationSequence" not in self._dataset:
                self._dataset.OutputInformationSequence = pydicom.Sequence()
            self._dataset.OutputInformationSequence.clear()
            self._dataset.OutputInformationSequence.extend([item.to_dataset() for item in value])

    def add_OutputInformation(self, item: OutputInformationSequenceItem):
        if not isinstance(item, OutputInformationSequenceItem):
            raise ValueError("Item must be an instance of OutputInformationSequenceItem")
        self._OutputInformationSequence.append(item)
        if "OutputInformationSequence" not in self._dataset:
            self._dataset.OutputInformationSequence = pydicom.Sequence()
        self._dataset.OutputInformationSequence.append(item.to_dataset())
