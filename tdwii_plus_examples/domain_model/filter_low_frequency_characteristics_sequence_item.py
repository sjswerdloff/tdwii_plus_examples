from decimal import Decimal
from typing import Any, List, Optional  # noqa

import pydicom

from .analog_filter_characteristics_sequence_item import (
    AnalogFilterCharacteristicsSequenceItem,
)
from .digital_filter_characteristics_sequence_item import (
    DigitalFilterCharacteristicsSequenceItem,
)
from .filter_lookup_table_sequence_item import FilterLookupTableSequenceItem


class FilterLowFrequencyCharacteristicsSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._AnalogFilterCharacteristicsSequence: List[AnalogFilterCharacteristicsSequenceItem] = []
        self._DigitalFilterCharacteristicsSequence: List[DigitalFilterCharacteristicsSequenceItem] = []
        self._FilterLookupTableSequence: List[FilterLookupTableSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def FilterLowFrequency(self) -> Optional[Decimal]:
        if "FilterLowFrequency" in self._dataset:
            return self._dataset.FilterLowFrequency
        return None

    @FilterLowFrequency.setter
    def FilterLowFrequency(self, value: Optional[Decimal]):
        if value is None:
            if "FilterLowFrequency" in self._dataset:
                del self._dataset.FilterLowFrequency
        else:
            self._dataset.FilterLowFrequency = value

    @property
    def FilterHighFrequency(self) -> Optional[Decimal]:
        if "FilterHighFrequency" in self._dataset:
            return self._dataset.FilterHighFrequency
        return None

    @FilterHighFrequency.setter
    def FilterHighFrequency(self, value: Optional[Decimal]):
        if value is None:
            if "FilterHighFrequency" in self._dataset:
                del self._dataset.FilterHighFrequency
        else:
            self._dataset.FilterHighFrequency = value

    @property
    def NotchFilterFrequency(self) -> Optional[Decimal]:
        if "NotchFilterFrequency" in self._dataset:
            return self._dataset.NotchFilterFrequency
        return None

    @NotchFilterFrequency.setter
    def NotchFilterFrequency(self, value: Optional[Decimal]):
        if value is None:
            if "NotchFilterFrequency" in self._dataset:
                del self._dataset.NotchFilterFrequency
        else:
            self._dataset.NotchFilterFrequency = value

    @property
    def NotchFilterBandwidth(self) -> Optional[Decimal]:
        if "NotchFilterBandwidth" in self._dataset:
            return self._dataset.NotchFilterBandwidth
        return None

    @NotchFilterBandwidth.setter
    def NotchFilterBandwidth(self, value: Optional[Decimal]):
        if value is None:
            if "NotchFilterBandwidth" in self._dataset:
                del self._dataset.NotchFilterBandwidth
        else:
            self._dataset.NotchFilterBandwidth = value

    @property
    def WaveformFilterType(self) -> Optional[str]:
        if "WaveformFilterType" in self._dataset:
            return self._dataset.WaveformFilterType
        return None

    @WaveformFilterType.setter
    def WaveformFilterType(self, value: Optional[str]):
        if value is None:
            if "WaveformFilterType" in self._dataset:
                del self._dataset.WaveformFilterType
        else:
            self._dataset.WaveformFilterType = value

    @property
    def AnalogFilterCharacteristicsSequence(self) -> Optional[List[AnalogFilterCharacteristicsSequenceItem]]:
        if "AnalogFilterCharacteristicsSequence" in self._dataset:
            if len(self._AnalogFilterCharacteristicsSequence) == len(self._dataset.AnalogFilterCharacteristicsSequence):
                return self._AnalogFilterCharacteristicsSequence
            else:
                return [AnalogFilterCharacteristicsSequenceItem(x) for x in self._dataset.AnalogFilterCharacteristicsSequence]
        return None

    @AnalogFilterCharacteristicsSequence.setter
    def AnalogFilterCharacteristicsSequence(self, value: Optional[List[AnalogFilterCharacteristicsSequenceItem]]):
        if value is None:
            self._AnalogFilterCharacteristicsSequence = []
            if "AnalogFilterCharacteristicsSequence" in self._dataset:
                del self._dataset.AnalogFilterCharacteristicsSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, AnalogFilterCharacteristicsSequenceItem) for item in value
        ):
            raise ValueError(
                "AnalogFilterCharacteristicsSequence must be a list of AnalogFilterCharacteristicsSequenceItem objects"
            )
        else:
            self._AnalogFilterCharacteristicsSequence = value
            if "AnalogFilterCharacteristicsSequence" not in self._dataset:
                self._dataset.AnalogFilterCharacteristicsSequence = pydicom.Sequence()
            self._dataset.AnalogFilterCharacteristicsSequence.clear()
            self._dataset.AnalogFilterCharacteristicsSequence.extend([item.to_dataset() for item in value])

    def add_AnalogFilterCharacteristics(self, item: AnalogFilterCharacteristicsSequenceItem):
        if not isinstance(item, AnalogFilterCharacteristicsSequenceItem):
            raise ValueError("Item must be an instance of AnalogFilterCharacteristicsSequenceItem")
        self._AnalogFilterCharacteristicsSequence.append(item)
        if "AnalogFilterCharacteristicsSequence" not in self._dataset:
            self._dataset.AnalogFilterCharacteristicsSequence = pydicom.Sequence()
        self._dataset.AnalogFilterCharacteristicsSequence.append(item.to_dataset())

    @property
    def DigitalFilterCharacteristicsSequence(self) -> Optional[List[DigitalFilterCharacteristicsSequenceItem]]:
        if "DigitalFilterCharacteristicsSequence" in self._dataset:
            if len(self._DigitalFilterCharacteristicsSequence) == len(self._dataset.DigitalFilterCharacteristicsSequence):
                return self._DigitalFilterCharacteristicsSequence
            else:
                return [
                    DigitalFilterCharacteristicsSequenceItem(x) for x in self._dataset.DigitalFilterCharacteristicsSequence
                ]
        return None

    @DigitalFilterCharacteristicsSequence.setter
    def DigitalFilterCharacteristicsSequence(self, value: Optional[List[DigitalFilterCharacteristicsSequenceItem]]):
        if value is None:
            self._DigitalFilterCharacteristicsSequence = []
            if "DigitalFilterCharacteristicsSequence" in self._dataset:
                del self._dataset.DigitalFilterCharacteristicsSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, DigitalFilterCharacteristicsSequenceItem) for item in value
        ):
            raise ValueError(
                "DigitalFilterCharacteristicsSequence must be a list of DigitalFilterCharacteristicsSequenceItem objects"
            )
        else:
            self._DigitalFilterCharacteristicsSequence = value
            if "DigitalFilterCharacteristicsSequence" not in self._dataset:
                self._dataset.DigitalFilterCharacteristicsSequence = pydicom.Sequence()
            self._dataset.DigitalFilterCharacteristicsSequence.clear()
            self._dataset.DigitalFilterCharacteristicsSequence.extend([item.to_dataset() for item in value])

    def add_DigitalFilterCharacteristics(self, item: DigitalFilterCharacteristicsSequenceItem):
        if not isinstance(item, DigitalFilterCharacteristicsSequenceItem):
            raise ValueError("Item must be an instance of DigitalFilterCharacteristicsSequenceItem")
        self._DigitalFilterCharacteristicsSequence.append(item)
        if "DigitalFilterCharacteristicsSequence" not in self._dataset:
            self._dataset.DigitalFilterCharacteristicsSequence = pydicom.Sequence()
        self._dataset.DigitalFilterCharacteristicsSequence.append(item.to_dataset())

    @property
    def WaveformFilterDescription(self) -> Optional[str]:
        if "WaveformFilterDescription" in self._dataset:
            return self._dataset.WaveformFilterDescription
        return None

    @WaveformFilterDescription.setter
    def WaveformFilterDescription(self, value: Optional[str]):
        if value is None:
            if "WaveformFilterDescription" in self._dataset:
                del self._dataset.WaveformFilterDescription
        else:
            self._dataset.WaveformFilterDescription = value

    @property
    def FilterLookupTableSequence(self) -> Optional[List[FilterLookupTableSequenceItem]]:
        if "FilterLookupTableSequence" in self._dataset:
            if len(self._FilterLookupTableSequence) == len(self._dataset.FilterLookupTableSequence):
                return self._FilterLookupTableSequence
            else:
                return [FilterLookupTableSequenceItem(x) for x in self._dataset.FilterLookupTableSequence]
        return None

    @FilterLookupTableSequence.setter
    def FilterLookupTableSequence(self, value: Optional[List[FilterLookupTableSequenceItem]]):
        if value is None:
            self._FilterLookupTableSequence = []
            if "FilterLookupTableSequence" in self._dataset:
                del self._dataset.FilterLookupTableSequence
        elif not isinstance(value, list) or not all(isinstance(item, FilterLookupTableSequenceItem) for item in value):
            raise ValueError("FilterLookupTableSequence must be a list of FilterLookupTableSequenceItem objects")
        else:
            self._FilterLookupTableSequence = value
            if "FilterLookupTableSequence" not in self._dataset:
                self._dataset.FilterLookupTableSequence = pydicom.Sequence()
            self._dataset.FilterLookupTableSequence.clear()
            self._dataset.FilterLookupTableSequence.extend([item.to_dataset() for item in value])

    def add_FilterLookupTable(self, item: FilterLookupTableSequenceItem):
        if not isinstance(item, FilterLookupTableSequenceItem):
            raise ValueError("Item must be an instance of FilterLookupTableSequenceItem")
        self._FilterLookupTableSequence.append(item)
        if "FilterLookupTableSequence" not in self._dataset:
            self._dataset.FilterLookupTableSequence = pydicom.Sequence()
        self._dataset.FilterLookupTableSequence.append(item.to_dataset())
