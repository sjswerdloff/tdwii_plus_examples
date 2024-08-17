from typing import Any, List, Optional

import pydicom

from .code_sequence_item import CodeSequenceItem


class UltrasoundOphthalmicAxialLengthMeasurementsSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._OphthalmicAxialLengthDataSourceCodeSequence: List[CodeSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def OphthalmicAxialLengthVelocity(self) -> Optional[float]:
        if "OphthalmicAxialLengthVelocity" in self._dataset:
            return self._dataset.OphthalmicAxialLengthVelocity
        return None

    @OphthalmicAxialLengthVelocity.setter
    def OphthalmicAxialLengthVelocity(self, value: Optional[float]):
        if value is None:
            if "OphthalmicAxialLengthVelocity" in self._dataset:
                del self._dataset.OphthalmicAxialLengthVelocity
        else:
            self._dataset.OphthalmicAxialLengthVelocity = value

    @property
    def OphthalmicAxialLengthDataSourceCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "OphthalmicAxialLengthDataSourceCodeSequence" in self._dataset:
            if len(self._OphthalmicAxialLengthDataSourceCodeSequence) == len(
                self._dataset.OphthalmicAxialLengthDataSourceCodeSequence
            ):
                return self._OphthalmicAxialLengthDataSourceCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.OphthalmicAxialLengthDataSourceCodeSequence]
        return None

    @OphthalmicAxialLengthDataSourceCodeSequence.setter
    def OphthalmicAxialLengthDataSourceCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._OphthalmicAxialLengthDataSourceCodeSequence = []
            if "OphthalmicAxialLengthDataSourceCodeSequence" in self._dataset:
                del self._dataset.OphthalmicAxialLengthDataSourceCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError(f"OphthalmicAxialLengthDataSourceCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._OphthalmicAxialLengthDataSourceCodeSequence = value
            if "OphthalmicAxialLengthDataSourceCodeSequence" not in self._dataset:
                self._dataset.OphthalmicAxialLengthDataSourceCodeSequence = pydicom.Sequence()
            self._dataset.OphthalmicAxialLengthDataSourceCodeSequence.clear()
            self._dataset.OphthalmicAxialLengthDataSourceCodeSequence.extend([item.to_dataset() for item in value])

    def add_OphthalmicAxialLengthDataSourceCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError(f"Item must be an instance of CodeSequenceItem")
        self._OphthalmicAxialLengthDataSourceCodeSequence.append(item)
        if "OphthalmicAxialLengthDataSourceCodeSequence" not in self._dataset:
            self._dataset.OphthalmicAxialLengthDataSourceCodeSequence = pydicom.Sequence()
        self._dataset.OphthalmicAxialLengthDataSourceCodeSequence.append(item.to_dataset())

    @property
    def OphthalmicAxialLengthDataSourceDescription(self) -> Optional[str]:
        if "OphthalmicAxialLengthDataSourceDescription" in self._dataset:
            return self._dataset.OphthalmicAxialLengthDataSourceDescription
        return None

    @OphthalmicAxialLengthDataSourceDescription.setter
    def OphthalmicAxialLengthDataSourceDescription(self, value: Optional[str]):
        if value is None:
            if "OphthalmicAxialLengthDataSourceDescription" in self._dataset:
                del self._dataset.OphthalmicAxialLengthDataSourceDescription
        else:
            self._dataset.OphthalmicAxialLengthDataSourceDescription = value

    @property
    def ObserverType(self) -> Optional[str]:
        if "ObserverType" in self._dataset:
            return self._dataset.ObserverType
        return None

    @ObserverType.setter
    def ObserverType(self, value: Optional[str]):
        if value is None:
            if "ObserverType" in self._dataset:
                del self._dataset.ObserverType
        else:
            self._dataset.ObserverType = value
