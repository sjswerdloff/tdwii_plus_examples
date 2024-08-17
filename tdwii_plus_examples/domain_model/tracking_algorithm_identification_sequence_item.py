from typing import Any, List, Optional  # noqa

import pydicom

from .code_sequence_item import CodeSequenceItem


class TrackingAlgorithmIdentificationSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._AlgorithmFamilyCodeSequence: List[CodeSequenceItem] = []
        self._AlgorithmNameCodeSequence: List[CodeSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def AlgorithmSource(self) -> Optional[str]:
        if "AlgorithmSource" in self._dataset:
            return self._dataset.AlgorithmSource
        return None

    @AlgorithmSource.setter
    def AlgorithmSource(self, value: Optional[str]):
        if value is None:
            if "AlgorithmSource" in self._dataset:
                del self._dataset.AlgorithmSource
        else:
            self._dataset.AlgorithmSource = value

    @property
    def AlgorithmFamilyCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "AlgorithmFamilyCodeSequence" in self._dataset:
            if len(self._AlgorithmFamilyCodeSequence) == len(self._dataset.AlgorithmFamilyCodeSequence):
                return self._AlgorithmFamilyCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.AlgorithmFamilyCodeSequence]
        return None

    @AlgorithmFamilyCodeSequence.setter
    def AlgorithmFamilyCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._AlgorithmFamilyCodeSequence = []
            if "AlgorithmFamilyCodeSequence" in self._dataset:
                del self._dataset.AlgorithmFamilyCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("AlgorithmFamilyCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._AlgorithmFamilyCodeSequence = value
            if "AlgorithmFamilyCodeSequence" not in self._dataset:
                self._dataset.AlgorithmFamilyCodeSequence = pydicom.Sequence()
            self._dataset.AlgorithmFamilyCodeSequence.clear()
            self._dataset.AlgorithmFamilyCodeSequence.extend([item.to_dataset() for item in value])

    def add_AlgorithmFamilyCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._AlgorithmFamilyCodeSequence.append(item)
        if "AlgorithmFamilyCodeSequence" not in self._dataset:
            self._dataset.AlgorithmFamilyCodeSequence = pydicom.Sequence()
        self._dataset.AlgorithmFamilyCodeSequence.append(item.to_dataset())

    @property
    def AlgorithmNameCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "AlgorithmNameCodeSequence" in self._dataset:
            if len(self._AlgorithmNameCodeSequence) == len(self._dataset.AlgorithmNameCodeSequence):
                return self._AlgorithmNameCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.AlgorithmNameCodeSequence]
        return None

    @AlgorithmNameCodeSequence.setter
    def AlgorithmNameCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._AlgorithmNameCodeSequence = []
            if "AlgorithmNameCodeSequence" in self._dataset:
                del self._dataset.AlgorithmNameCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("AlgorithmNameCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._AlgorithmNameCodeSequence = value
            if "AlgorithmNameCodeSequence" not in self._dataset:
                self._dataset.AlgorithmNameCodeSequence = pydicom.Sequence()
            self._dataset.AlgorithmNameCodeSequence.clear()
            self._dataset.AlgorithmNameCodeSequence.extend([item.to_dataset() for item in value])

    def add_AlgorithmNameCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._AlgorithmNameCodeSequence.append(item)
        if "AlgorithmNameCodeSequence" not in self._dataset:
            self._dataset.AlgorithmNameCodeSequence = pydicom.Sequence()
        self._dataset.AlgorithmNameCodeSequence.append(item.to_dataset())

    @property
    def AlgorithmVersion(self) -> Optional[str]:
        if "AlgorithmVersion" in self._dataset:
            return self._dataset.AlgorithmVersion
        return None

    @AlgorithmVersion.setter
    def AlgorithmVersion(self, value: Optional[str]):
        if value is None:
            if "AlgorithmVersion" in self._dataset:
                del self._dataset.AlgorithmVersion
        else:
            self._dataset.AlgorithmVersion = value

    @property
    def AlgorithmParameters(self) -> Optional[str]:
        if "AlgorithmParameters" in self._dataset:
            return self._dataset.AlgorithmParameters
        return None

    @AlgorithmParameters.setter
    def AlgorithmParameters(self, value: Optional[str]):
        if value is None:
            if "AlgorithmParameters" in self._dataset:
                del self._dataset.AlgorithmParameters
        else:
            self._dataset.AlgorithmParameters = value

    @property
    def AlgorithmName(self) -> Optional[str]:
        if "AlgorithmName" in self._dataset:
            return self._dataset.AlgorithmName
        return None

    @AlgorithmName.setter
    def AlgorithmName(self, value: Optional[str]):
        if value is None:
            if "AlgorithmName" in self._dataset:
                del self._dataset.AlgorithmName
        else:
            self._dataset.AlgorithmName = value
