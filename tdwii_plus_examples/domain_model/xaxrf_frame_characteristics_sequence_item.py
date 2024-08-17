from typing import Any, List, Optional  # noqa

import pydicom

from .code_sequence_item import CodeSequenceItem


class XAXRFFrameCharacteristicsSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._DerivationCodeSequence: List[CodeSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def DerivationDescription(self) -> Optional[str]:
        if "DerivationDescription" in self._dataset:
            return self._dataset.DerivationDescription
        return None

    @DerivationDescription.setter
    def DerivationDescription(self, value: Optional[str]):
        if value is None:
            if "DerivationDescription" in self._dataset:
                del self._dataset.DerivationDescription
        else:
            self._dataset.DerivationDescription = value

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
