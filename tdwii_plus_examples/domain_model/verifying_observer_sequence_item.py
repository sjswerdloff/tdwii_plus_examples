from typing import Any, List, Optional

import pydicom

from .code_sequence_item import CodeSequenceItem


class VerifyingObserverSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._VerifyingObserverIdentificationCodeSequence: List[CodeSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def VerifyingOrganization(self) -> Optional[str]:
        if "VerifyingOrganization" in self._dataset:
            return self._dataset.VerifyingOrganization
        return None

    @VerifyingOrganization.setter
    def VerifyingOrganization(self, value: Optional[str]):
        if value is None:
            if "VerifyingOrganization" in self._dataset:
                del self._dataset.VerifyingOrganization
        else:
            self._dataset.VerifyingOrganization = value

    @property
    def VerificationDateTime(self) -> Optional[str]:
        if "VerificationDateTime" in self._dataset:
            return self._dataset.VerificationDateTime
        return None

    @VerificationDateTime.setter
    def VerificationDateTime(self, value: Optional[str]):
        if value is None:
            if "VerificationDateTime" in self._dataset:
                del self._dataset.VerificationDateTime
        else:
            self._dataset.VerificationDateTime = value

    @property
    def VerifyingObserverName(self) -> Optional[str]:
        if "VerifyingObserverName" in self._dataset:
            return self._dataset.VerifyingObserverName
        return None

    @VerifyingObserverName.setter
    def VerifyingObserverName(self, value: Optional[str]):
        if value is None:
            if "VerifyingObserverName" in self._dataset:
                del self._dataset.VerifyingObserverName
        else:
            self._dataset.VerifyingObserverName = value

    @property
    def VerifyingObserverIdentificationCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "VerifyingObserverIdentificationCodeSequence" in self._dataset:
            if len(self._VerifyingObserverIdentificationCodeSequence) == len(
                self._dataset.VerifyingObserverIdentificationCodeSequence
            ):
                return self._VerifyingObserverIdentificationCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.VerifyingObserverIdentificationCodeSequence]
        return None

    @VerifyingObserverIdentificationCodeSequence.setter
    def VerifyingObserverIdentificationCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._VerifyingObserverIdentificationCodeSequence = []
            if "VerifyingObserverIdentificationCodeSequence" in self._dataset:
                del self._dataset.VerifyingObserverIdentificationCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError(f"VerifyingObserverIdentificationCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._VerifyingObserverIdentificationCodeSequence = value
            if "VerifyingObserverIdentificationCodeSequence" not in self._dataset:
                self._dataset.VerifyingObserverIdentificationCodeSequence = pydicom.Sequence()
            self._dataset.VerifyingObserverIdentificationCodeSequence.clear()
            self._dataset.VerifyingObserverIdentificationCodeSequence.extend([item.to_dataset() for item in value])

    def add_VerifyingObserverIdentificationCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError(f"Item must be an instance of CodeSequenceItem")
        self._VerifyingObserverIdentificationCodeSequence.append(item)
        if "VerifyingObserverIdentificationCodeSequence" not in self._dataset:
            self._dataset.VerifyingObserverIdentificationCodeSequence = pydicom.Sequence()
        self._dataset.VerifyingObserverIdentificationCodeSequence.append(item.to_dataset())
