from typing import Any, List, Optional

import pydicom


class ReferencedDigitalSignatureSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def DigitalSignatureUID(self) -> Optional[str]:
        if "DigitalSignatureUID" in self._dataset:
            return self._dataset.DigitalSignatureUID
        return None

    @DigitalSignatureUID.setter
    def DigitalSignatureUID(self, value: Optional[str]):
        if value is None:
            if "DigitalSignatureUID" in self._dataset:
                del self._dataset.DigitalSignatureUID
        else:
            self._dataset.DigitalSignatureUID = value

    @property
    def Signature(self) -> Optional[bytes]:
        if "Signature" in self._dataset:
            return self._dataset.Signature
        return None

    @Signature.setter
    def Signature(self, value: Optional[bytes]):
        if value is None:
            if "Signature" in self._dataset:
                del self._dataset.Signature
        else:
            self._dataset.Signature = value
