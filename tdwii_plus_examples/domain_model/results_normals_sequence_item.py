from typing import Any, List, Optional  # noqa

import pydicom

from .global_deviation_probability_sequence_item import (
    GlobalDeviationProbabilitySequenceItem,
)
from .localized_deviation_probability_sequence_item import (
    LocalizedDeviationProbabilitySequenceItem,
)


class ResultsNormalsSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._GlobalDeviationProbabilitySequence: List[GlobalDeviationProbabilitySequenceItem] = []
        self._LocalizedDeviationProbabilitySequence: List[LocalizedDeviationProbabilitySequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def GlobalDeviationProbabilityNormalsFlag(self) -> Optional[str]:
        if "GlobalDeviationProbabilityNormalsFlag" in self._dataset:
            return self._dataset.GlobalDeviationProbabilityNormalsFlag
        return None

    @GlobalDeviationProbabilityNormalsFlag.setter
    def GlobalDeviationProbabilityNormalsFlag(self, value: Optional[str]):
        if value is None:
            if "GlobalDeviationProbabilityNormalsFlag" in self._dataset:
                del self._dataset.GlobalDeviationProbabilityNormalsFlag
        else:
            self._dataset.GlobalDeviationProbabilityNormalsFlag = value

    @property
    def GlobalDeviationFromNormal(self) -> Optional[float]:
        if "GlobalDeviationFromNormal" in self._dataset:
            return self._dataset.GlobalDeviationFromNormal
        return None

    @GlobalDeviationFromNormal.setter
    def GlobalDeviationFromNormal(self, value: Optional[float]):
        if value is None:
            if "GlobalDeviationFromNormal" in self._dataset:
                del self._dataset.GlobalDeviationFromNormal
        else:
            self._dataset.GlobalDeviationFromNormal = value

    @property
    def LocalizedDeviationFromNormal(self) -> Optional[float]:
        if "LocalizedDeviationFromNormal" in self._dataset:
            return self._dataset.LocalizedDeviationFromNormal
        return None

    @LocalizedDeviationFromNormal.setter
    def LocalizedDeviationFromNormal(self, value: Optional[float]):
        if value is None:
            if "LocalizedDeviationFromNormal" in self._dataset:
                del self._dataset.LocalizedDeviationFromNormal
        else:
            self._dataset.LocalizedDeviationFromNormal = value

    @property
    def LocalDeviationProbabilityNormalsFlag(self) -> Optional[str]:
        if "LocalDeviationProbabilityNormalsFlag" in self._dataset:
            return self._dataset.LocalDeviationProbabilityNormalsFlag
        return None

    @LocalDeviationProbabilityNormalsFlag.setter
    def LocalDeviationProbabilityNormalsFlag(self, value: Optional[str]):
        if value is None:
            if "LocalDeviationProbabilityNormalsFlag" in self._dataset:
                del self._dataset.LocalDeviationProbabilityNormalsFlag
        else:
            self._dataset.LocalDeviationProbabilityNormalsFlag = value

    @property
    def GlobalDeviationProbabilitySequence(self) -> Optional[List[GlobalDeviationProbabilitySequenceItem]]:
        if "GlobalDeviationProbabilitySequence" in self._dataset:
            if len(self._GlobalDeviationProbabilitySequence) == len(self._dataset.GlobalDeviationProbabilitySequence):
                return self._GlobalDeviationProbabilitySequence
            else:
                return [GlobalDeviationProbabilitySequenceItem(x) for x in self._dataset.GlobalDeviationProbabilitySequence]
        return None

    @GlobalDeviationProbabilitySequence.setter
    def GlobalDeviationProbabilitySequence(self, value: Optional[List[GlobalDeviationProbabilitySequenceItem]]):
        if value is None:
            self._GlobalDeviationProbabilitySequence = []
            if "GlobalDeviationProbabilitySequence" in self._dataset:
                del self._dataset.GlobalDeviationProbabilitySequence
        elif not isinstance(value, list) or not all(
            isinstance(item, GlobalDeviationProbabilitySequenceItem) for item in value
        ):
            raise ValueError(
                "GlobalDeviationProbabilitySequence must be a list of GlobalDeviationProbabilitySequenceItem objects"
            )
        else:
            self._GlobalDeviationProbabilitySequence = value
            if "GlobalDeviationProbabilitySequence" not in self._dataset:
                self._dataset.GlobalDeviationProbabilitySequence = pydicom.Sequence()
            self._dataset.GlobalDeviationProbabilitySequence.clear()
            self._dataset.GlobalDeviationProbabilitySequence.extend([item.to_dataset() for item in value])

    def add_GlobalDeviationProbability(self, item: GlobalDeviationProbabilitySequenceItem):
        if not isinstance(item, GlobalDeviationProbabilitySequenceItem):
            raise ValueError("Item must be an instance of GlobalDeviationProbabilitySequenceItem")
        self._GlobalDeviationProbabilitySequence.append(item)
        if "GlobalDeviationProbabilitySequence" not in self._dataset:
            self._dataset.GlobalDeviationProbabilitySequence = pydicom.Sequence()
        self._dataset.GlobalDeviationProbabilitySequence.append(item.to_dataset())

    @property
    def LocalizedDeviationProbabilitySequence(self) -> Optional[List[LocalizedDeviationProbabilitySequenceItem]]:
        if "LocalizedDeviationProbabilitySequence" in self._dataset:
            if len(self._LocalizedDeviationProbabilitySequence) == len(self._dataset.LocalizedDeviationProbabilitySequence):
                return self._LocalizedDeviationProbabilitySequence
            else:
                return [
                    LocalizedDeviationProbabilitySequenceItem(x) for x in self._dataset.LocalizedDeviationProbabilitySequence
                ]
        return None

    @LocalizedDeviationProbabilitySequence.setter
    def LocalizedDeviationProbabilitySequence(self, value: Optional[List[LocalizedDeviationProbabilitySequenceItem]]):
        if value is None:
            self._LocalizedDeviationProbabilitySequence = []
            if "LocalizedDeviationProbabilitySequence" in self._dataset:
                del self._dataset.LocalizedDeviationProbabilitySequence
        elif not isinstance(value, list) or not all(
            isinstance(item, LocalizedDeviationProbabilitySequenceItem) for item in value
        ):
            raise ValueError(
                "LocalizedDeviationProbabilitySequence must be a list of LocalizedDeviationProbabilitySequenceItem objects"
            )
        else:
            self._LocalizedDeviationProbabilitySequence = value
            if "LocalizedDeviationProbabilitySequence" not in self._dataset:
                self._dataset.LocalizedDeviationProbabilitySequence = pydicom.Sequence()
            self._dataset.LocalizedDeviationProbabilitySequence.clear()
            self._dataset.LocalizedDeviationProbabilitySequence.extend([item.to_dataset() for item in value])

    def add_LocalizedDeviationProbability(self, item: LocalizedDeviationProbabilitySequenceItem):
        if not isinstance(item, LocalizedDeviationProbabilitySequenceItem):
            raise ValueError("Item must be an instance of LocalizedDeviationProbabilitySequenceItem")
        self._LocalizedDeviationProbabilitySequence.append(item)
        if "LocalizedDeviationProbabilitySequence" not in self._dataset:
            self._dataset.LocalizedDeviationProbabilitySequence = pydicom.Sequence()
        self._dataset.LocalizedDeviationProbabilitySequence.append(item.to_dataset())

    @property
    def DataSetName(self) -> Optional[str]:
        if "DataSetName" in self._dataset:
            return self._dataset.DataSetName
        return None

    @DataSetName.setter
    def DataSetName(self, value: Optional[str]):
        if value is None:
            if "DataSetName" in self._dataset:
                del self._dataset.DataSetName
        else:
            self._dataset.DataSetName = value

    @property
    def DataSetVersion(self) -> Optional[str]:
        if "DataSetVersion" in self._dataset:
            return self._dataset.DataSetVersion
        return None

    @DataSetVersion.setter
    def DataSetVersion(self, value: Optional[str]):
        if value is None:
            if "DataSetVersion" in self._dataset:
                del self._dataset.DataSetVersion
        else:
            self._dataset.DataSetVersion = value

    @property
    def DataSetSource(self) -> Optional[str]:
        if "DataSetSource" in self._dataset:
            return self._dataset.DataSetSource
        return None

    @DataSetSource.setter
    def DataSetSource(self, value: Optional[str]):
        if value is None:
            if "DataSetSource" in self._dataset:
                del self._dataset.DataSetSource
        else:
            self._dataset.DataSetSource = value

    @property
    def DataSetDescription(self) -> Optional[str]:
        if "DataSetDescription" in self._dataset:
            return self._dataset.DataSetDescription
        return None

    @DataSetDescription.setter
    def DataSetDescription(self, value: Optional[str]):
        if value is None:
            if "DataSetDescription" in self._dataset:
                del self._dataset.DataSetDescription
        else:
            self._dataset.DataSetDescription = value
