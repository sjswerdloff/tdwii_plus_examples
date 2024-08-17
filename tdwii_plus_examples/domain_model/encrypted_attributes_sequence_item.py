from typing import Any, List, Optional

import pydicom


class EncryptedAttributesSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def EncryptedContentTransferSyntaxUID(self) -> Optional[str]:
        if "EncryptedContentTransferSyntaxUID" in self._dataset:
            return self._dataset.EncryptedContentTransferSyntaxUID
        return None

    @EncryptedContentTransferSyntaxUID.setter
    def EncryptedContentTransferSyntaxUID(self, value: Optional[str]):
        if value is None:
            if "EncryptedContentTransferSyntaxUID" in self._dataset:
                del self._dataset.EncryptedContentTransferSyntaxUID
        else:
            self._dataset.EncryptedContentTransferSyntaxUID = value

    @property
    def EncryptedContent(self) -> Optional[bytes]:
        if "EncryptedContent" in self._dataset:
            return self._dataset.EncryptedContent
        return None

    @EncryptedContent.setter
    def EncryptedContent(self, value: Optional[bytes]):
        if value is None:
            if "EncryptedContent" in self._dataset:
                del self._dataset.EncryptedContent
        else:
            self._dataset.EncryptedContent = value
