from typing import Any, List, Optional  # noqa

import pydicom

from .code_sequence_item import CodeSequenceItem


class DigitalSignaturesSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._DigitalSignaturePurposeCodeSequence: List[CodeSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def MACIDNumber(self) -> Optional[int]:
        if "MACIDNumber" in self._dataset:
            return self._dataset.MACIDNumber
        return None

    @MACIDNumber.setter
    def MACIDNumber(self, value: Optional[int]):
        if value is None:
            if "MACIDNumber" in self._dataset:
                del self._dataset.MACIDNumber
        else:
            self._dataset.MACIDNumber = value

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
    def DigitalSignatureDateTime(self) -> Optional[str]:
        if "DigitalSignatureDateTime" in self._dataset:
            return self._dataset.DigitalSignatureDateTime
        return None

    @DigitalSignatureDateTime.setter
    def DigitalSignatureDateTime(self, value: Optional[str]):
        if value is None:
            if "DigitalSignatureDateTime" in self._dataset:
                del self._dataset.DigitalSignatureDateTime
        else:
            self._dataset.DigitalSignatureDateTime = value

    @property
    def CertificateType(self) -> Optional[str]:
        if "CertificateType" in self._dataset:
            return self._dataset.CertificateType
        return None

    @CertificateType.setter
    def CertificateType(self, value: Optional[str]):
        if value is None:
            if "CertificateType" in self._dataset:
                del self._dataset.CertificateType
        else:
            self._dataset.CertificateType = value

    @property
    def CertificateOfSigner(self) -> Optional[bytes]:
        if "CertificateOfSigner" in self._dataset:
            return self._dataset.CertificateOfSigner
        return None

    @CertificateOfSigner.setter
    def CertificateOfSigner(self, value: Optional[bytes]):
        if value is None:
            if "CertificateOfSigner" in self._dataset:
                del self._dataset.CertificateOfSigner
        else:
            self._dataset.CertificateOfSigner = value

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

    @property
    def CertifiedTimestampType(self) -> Optional[str]:
        if "CertifiedTimestampType" in self._dataset:
            return self._dataset.CertifiedTimestampType
        return None

    @CertifiedTimestampType.setter
    def CertifiedTimestampType(self, value: Optional[str]):
        if value is None:
            if "CertifiedTimestampType" in self._dataset:
                del self._dataset.CertifiedTimestampType
        else:
            self._dataset.CertifiedTimestampType = value

    @property
    def CertifiedTimestamp(self) -> Optional[bytes]:
        if "CertifiedTimestamp" in self._dataset:
            return self._dataset.CertifiedTimestamp
        return None

    @CertifiedTimestamp.setter
    def CertifiedTimestamp(self, value: Optional[bytes]):
        if value is None:
            if "CertifiedTimestamp" in self._dataset:
                del self._dataset.CertifiedTimestamp
        else:
            self._dataset.CertifiedTimestamp = value

    @property
    def DigitalSignaturePurposeCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "DigitalSignaturePurposeCodeSequence" in self._dataset:
            if len(self._DigitalSignaturePurposeCodeSequence) == len(self._dataset.DigitalSignaturePurposeCodeSequence):
                return self._DigitalSignaturePurposeCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.DigitalSignaturePurposeCodeSequence]
        return None

    @DigitalSignaturePurposeCodeSequence.setter
    def DigitalSignaturePurposeCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._DigitalSignaturePurposeCodeSequence = []
            if "DigitalSignaturePurposeCodeSequence" in self._dataset:
                del self._dataset.DigitalSignaturePurposeCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("DigitalSignaturePurposeCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._DigitalSignaturePurposeCodeSequence = value
            if "DigitalSignaturePurposeCodeSequence" not in self._dataset:
                self._dataset.DigitalSignaturePurposeCodeSequence = pydicom.Sequence()
            self._dataset.DigitalSignaturePurposeCodeSequence.clear()
            self._dataset.DigitalSignaturePurposeCodeSequence.extend([item.to_dataset() for item in value])

    def add_DigitalSignaturePurposeCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._DigitalSignaturePurposeCodeSequence.append(item)
        if "DigitalSignaturePurposeCodeSequence" not in self._dataset:
            self._dataset.DigitalSignaturePurposeCodeSequence = pydicom.Sequence()
        self._dataset.DigitalSignaturePurposeCodeSequence.append(item.to_dataset())
