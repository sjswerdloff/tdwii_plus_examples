from typing import Any, List, Optional

import pydicom

from .code_sequence_item import CodeSequenceItem


class FilterLookupTableSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._FrequencyEncodingCodeSequence: List[CodeSequenceItem] = []
        self._MagnitudeEncodingCodeSequence: List[CodeSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def FilterLookupTableDescription(self) -> Optional[str]:
        if "FilterLookupTableDescription" in self._dataset:
            return self._dataset.FilterLookupTableDescription
        return None

    @FilterLookupTableDescription.setter
    def FilterLookupTableDescription(self, value: Optional[str]):
        if value is None:
            if "FilterLookupTableDescription" in self._dataset:
                del self._dataset.FilterLookupTableDescription
        else:
            self._dataset.FilterLookupTableDescription = value

    @property
    def FrequencyEncodingCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "FrequencyEncodingCodeSequence" in self._dataset:
            if len(self._FrequencyEncodingCodeSequence) == len(self._dataset.FrequencyEncodingCodeSequence):
                return self._FrequencyEncodingCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.FrequencyEncodingCodeSequence]
        return None

    @FrequencyEncodingCodeSequence.setter
    def FrequencyEncodingCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._FrequencyEncodingCodeSequence = []
            if "FrequencyEncodingCodeSequence" in self._dataset:
                del self._dataset.FrequencyEncodingCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError(f"FrequencyEncodingCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._FrequencyEncodingCodeSequence = value
            if "FrequencyEncodingCodeSequence" not in self._dataset:
                self._dataset.FrequencyEncodingCodeSequence = pydicom.Sequence()
            self._dataset.FrequencyEncodingCodeSequence.clear()
            self._dataset.FrequencyEncodingCodeSequence.extend([item.to_dataset() for item in value])

    def add_FrequencyEncodingCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError(f"Item must be an instance of CodeSequenceItem")
        self._FrequencyEncodingCodeSequence.append(item)
        if "FrequencyEncodingCodeSequence" not in self._dataset:
            self._dataset.FrequencyEncodingCodeSequence = pydicom.Sequence()
        self._dataset.FrequencyEncodingCodeSequence.append(item.to_dataset())

    @property
    def MagnitudeEncodingCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "MagnitudeEncodingCodeSequence" in self._dataset:
            if len(self._MagnitudeEncodingCodeSequence) == len(self._dataset.MagnitudeEncodingCodeSequence):
                return self._MagnitudeEncodingCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.MagnitudeEncodingCodeSequence]
        return None

    @MagnitudeEncodingCodeSequence.setter
    def MagnitudeEncodingCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._MagnitudeEncodingCodeSequence = []
            if "MagnitudeEncodingCodeSequence" in self._dataset:
                del self._dataset.MagnitudeEncodingCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError(f"MagnitudeEncodingCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._MagnitudeEncodingCodeSequence = value
            if "MagnitudeEncodingCodeSequence" not in self._dataset:
                self._dataset.MagnitudeEncodingCodeSequence = pydicom.Sequence()
            self._dataset.MagnitudeEncodingCodeSequence.clear()
            self._dataset.MagnitudeEncodingCodeSequence.extend([item.to_dataset() for item in value])

    def add_MagnitudeEncodingCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError(f"Item must be an instance of CodeSequenceItem")
        self._MagnitudeEncodingCodeSequence.append(item)
        if "MagnitudeEncodingCodeSequence" not in self._dataset:
            self._dataset.MagnitudeEncodingCodeSequence = pydicom.Sequence()
        self._dataset.MagnitudeEncodingCodeSequence.append(item.to_dataset())

    @property
    def FilterLookupTableData(self) -> Optional[bytes]:
        if "FilterLookupTableData" in self._dataset:
            return self._dataset.FilterLookupTableData
        return None

    @FilterLookupTableData.setter
    def FilterLookupTableData(self, value: Optional[bytes]):
        if value is None:
            if "FilterLookupTableData" in self._dataset:
                del self._dataset.FilterLookupTableData
        else:
            self._dataset.FilterLookupTableData = value
