from typing import Any, List, Optional  # noqa

import pydicom


class FlowIdentifierSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def FlowIdentifier(self) -> Optional[bytes]:
        if "FlowIdentifier" in self._dataset:
            return self._dataset.FlowIdentifier
        return None

    @FlowIdentifier.setter
    def FlowIdentifier(self, value: Optional[bytes]):
        if value is None:
            if "FlowIdentifier" in self._dataset:
                del self._dataset.FlowIdentifier
        else:
            self._dataset.FlowIdentifier = value

    @property
    def FlowTransferSyntaxUID(self) -> Optional[str]:
        if "FlowTransferSyntaxUID" in self._dataset:
            return self._dataset.FlowTransferSyntaxUID
        return None

    @FlowTransferSyntaxUID.setter
    def FlowTransferSyntaxUID(self, value: Optional[str]):
        if value is None:
            if "FlowTransferSyntaxUID" in self._dataset:
                del self._dataset.FlowTransferSyntaxUID
        else:
            self._dataset.FlowTransferSyntaxUID = value

    @property
    def FlowRTPSamplingRate(self) -> Optional[int]:
        if "FlowRTPSamplingRate" in self._dataset:
            return self._dataset.FlowRTPSamplingRate
        return None

    @FlowRTPSamplingRate.setter
    def FlowRTPSamplingRate(self, value: Optional[int]):
        if value is None:
            if "FlowRTPSamplingRate" in self._dataset:
                del self._dataset.FlowRTPSamplingRate
        else:
            self._dataset.FlowRTPSamplingRate = value
