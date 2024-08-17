from decimal import Decimal
from typing import Any, List, Optional

import pydicom

from .channel_impedance_sequence_item import ChannelImpedanceSequenceItem
from .channel_sensitivity_units_sequence_item import ChannelSensitivityUnitsSequenceItem
from .channel_source_modifiers_sequence_item import ChannelSourceModifiersSequenceItem
from .channel_source_sequence_item import ChannelSourceSequenceItem
from .filter_high_frequency_characteristics_sequence_item import (
    FilterHighFrequencyCharacteristicsSequenceItem,
)
from .filter_low_frequency_characteristics_sequence_item import (
    FilterLowFrequencyCharacteristicsSequenceItem,
)
from .notch_filter_characteristics_sequence_item import (
    NotchFilterCharacteristicsSequenceItem,
)
from .source_waveform_sequence_item import SourceWaveformSequenceItem


class ChannelDefinitionSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._ChannelSourceSequence: List[ChannelSourceSequenceItem] = []
        self._ChannelSourceModifiersSequence: List[ChannelSourceModifiersSequenceItem] = []
        self._SourceWaveformSequence: List[SourceWaveformSequenceItem] = []
        self._ChannelSensitivityUnitsSequence: List[ChannelSensitivityUnitsSequenceItem] = []
        self._ChannelImpedanceSequence: List[ChannelImpedanceSequenceItem] = []
        self._FilterLowFrequencyCharacteristicsSequence: List[FilterLowFrequencyCharacteristicsSequenceItem] = []
        self._FilterHighFrequencyCharacteristicsSequence: List[FilterHighFrequencyCharacteristicsSequenceItem] = []
        self._NotchFilterCharacteristicsSequence: List[NotchFilterCharacteristicsSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def WaveformChannelNumber(self) -> Optional[int]:
        if "WaveformChannelNumber" in self._dataset:
            return self._dataset.WaveformChannelNumber
        return None

    @WaveformChannelNumber.setter
    def WaveformChannelNumber(self, value: Optional[int]):
        if value is None:
            if "WaveformChannelNumber" in self._dataset:
                del self._dataset.WaveformChannelNumber
        else:
            self._dataset.WaveformChannelNumber = value

    @property
    def ChannelLabel(self) -> Optional[str]:
        if "ChannelLabel" in self._dataset:
            return self._dataset.ChannelLabel
        return None

    @ChannelLabel.setter
    def ChannelLabel(self, value: Optional[str]):
        if value is None:
            if "ChannelLabel" in self._dataset:
                del self._dataset.ChannelLabel
        else:
            self._dataset.ChannelLabel = value

    @property
    def ChannelStatus(self) -> Optional[List[str]]:
        if "ChannelStatus" in self._dataset:
            return self._dataset.ChannelStatus
        return None

    @ChannelStatus.setter
    def ChannelStatus(self, value: Optional[List[str]]):
        if value is None:
            if "ChannelStatus" in self._dataset:
                del self._dataset.ChannelStatus
        else:
            self._dataset.ChannelStatus = value

    @property
    def ChannelSourceSequence(self) -> Optional[List[ChannelSourceSequenceItem]]:
        if "ChannelSourceSequence" in self._dataset:
            if len(self._ChannelSourceSequence) == len(self._dataset.ChannelSourceSequence):
                return self._ChannelSourceSequence
            else:
                return [ChannelSourceSequenceItem(x) for x in self._dataset.ChannelSourceSequence]
        return None

    @ChannelSourceSequence.setter
    def ChannelSourceSequence(self, value: Optional[List[ChannelSourceSequenceItem]]):
        if value is None:
            self._ChannelSourceSequence = []
            if "ChannelSourceSequence" in self._dataset:
                del self._dataset.ChannelSourceSequence
        elif not isinstance(value, list) or not all(isinstance(item, ChannelSourceSequenceItem) for item in value):
            raise ValueError(f"ChannelSourceSequence must be a list of ChannelSourceSequenceItem objects")
        else:
            self._ChannelSourceSequence = value
            if "ChannelSourceSequence" not in self._dataset:
                self._dataset.ChannelSourceSequence = pydicom.Sequence()
            self._dataset.ChannelSourceSequence.clear()
            self._dataset.ChannelSourceSequence.extend([item.to_dataset() for item in value])

    def add_ChannelSource(self, item: ChannelSourceSequenceItem):
        if not isinstance(item, ChannelSourceSequenceItem):
            raise ValueError(f"Item must be an instance of ChannelSourceSequenceItem")
        self._ChannelSourceSequence.append(item)
        if "ChannelSourceSequence" not in self._dataset:
            self._dataset.ChannelSourceSequence = pydicom.Sequence()
        self._dataset.ChannelSourceSequence.append(item.to_dataset())

    @property
    def ChannelSourceModifiersSequence(self) -> Optional[List[ChannelSourceModifiersSequenceItem]]:
        if "ChannelSourceModifiersSequence" in self._dataset:
            if len(self._ChannelSourceModifiersSequence) == len(self._dataset.ChannelSourceModifiersSequence):
                return self._ChannelSourceModifiersSequence
            else:
                return [ChannelSourceModifiersSequenceItem(x) for x in self._dataset.ChannelSourceModifiersSequence]
        return None

    @ChannelSourceModifiersSequence.setter
    def ChannelSourceModifiersSequence(self, value: Optional[List[ChannelSourceModifiersSequenceItem]]):
        if value is None:
            self._ChannelSourceModifiersSequence = []
            if "ChannelSourceModifiersSequence" in self._dataset:
                del self._dataset.ChannelSourceModifiersSequence
        elif not isinstance(value, list) or not all(isinstance(item, ChannelSourceModifiersSequenceItem) for item in value):
            raise ValueError(f"ChannelSourceModifiersSequence must be a list of ChannelSourceModifiersSequenceItem objects")
        else:
            self._ChannelSourceModifiersSequence = value
            if "ChannelSourceModifiersSequence" not in self._dataset:
                self._dataset.ChannelSourceModifiersSequence = pydicom.Sequence()
            self._dataset.ChannelSourceModifiersSequence.clear()
            self._dataset.ChannelSourceModifiersSequence.extend([item.to_dataset() for item in value])

    def add_ChannelSourceModifiers(self, item: ChannelSourceModifiersSequenceItem):
        if not isinstance(item, ChannelSourceModifiersSequenceItem):
            raise ValueError(f"Item must be an instance of ChannelSourceModifiersSequenceItem")
        self._ChannelSourceModifiersSequence.append(item)
        if "ChannelSourceModifiersSequence" not in self._dataset:
            self._dataset.ChannelSourceModifiersSequence = pydicom.Sequence()
        self._dataset.ChannelSourceModifiersSequence.append(item.to_dataset())

    @property
    def SourceWaveformSequence(self) -> Optional[List[SourceWaveformSequenceItem]]:
        if "SourceWaveformSequence" in self._dataset:
            if len(self._SourceWaveformSequence) == len(self._dataset.SourceWaveformSequence):
                return self._SourceWaveformSequence
            else:
                return [SourceWaveformSequenceItem(x) for x in self._dataset.SourceWaveformSequence]
        return None

    @SourceWaveformSequence.setter
    def SourceWaveformSequence(self, value: Optional[List[SourceWaveformSequenceItem]]):
        if value is None:
            self._SourceWaveformSequence = []
            if "SourceWaveformSequence" in self._dataset:
                del self._dataset.SourceWaveformSequence
        elif not isinstance(value, list) or not all(isinstance(item, SourceWaveformSequenceItem) for item in value):
            raise ValueError(f"SourceWaveformSequence must be a list of SourceWaveformSequenceItem objects")
        else:
            self._SourceWaveformSequence = value
            if "SourceWaveformSequence" not in self._dataset:
                self._dataset.SourceWaveformSequence = pydicom.Sequence()
            self._dataset.SourceWaveformSequence.clear()
            self._dataset.SourceWaveformSequence.extend([item.to_dataset() for item in value])

    def add_SourceWaveform(self, item: SourceWaveformSequenceItem):
        if not isinstance(item, SourceWaveformSequenceItem):
            raise ValueError(f"Item must be an instance of SourceWaveformSequenceItem")
        self._SourceWaveformSequence.append(item)
        if "SourceWaveformSequence" not in self._dataset:
            self._dataset.SourceWaveformSequence = pydicom.Sequence()
        self._dataset.SourceWaveformSequence.append(item.to_dataset())

    @property
    def ChannelDerivationDescription(self) -> Optional[str]:
        if "ChannelDerivationDescription" in self._dataset:
            return self._dataset.ChannelDerivationDescription
        return None

    @ChannelDerivationDescription.setter
    def ChannelDerivationDescription(self, value: Optional[str]):
        if value is None:
            if "ChannelDerivationDescription" in self._dataset:
                del self._dataset.ChannelDerivationDescription
        else:
            self._dataset.ChannelDerivationDescription = value

    @property
    def ChannelSensitivity(self) -> Optional[Decimal]:
        if "ChannelSensitivity" in self._dataset:
            return self._dataset.ChannelSensitivity
        return None

    @ChannelSensitivity.setter
    def ChannelSensitivity(self, value: Optional[Decimal]):
        if value is None:
            if "ChannelSensitivity" in self._dataset:
                del self._dataset.ChannelSensitivity
        else:
            self._dataset.ChannelSensitivity = value

    @property
    def ChannelSensitivityUnitsSequence(self) -> Optional[List[ChannelSensitivityUnitsSequenceItem]]:
        if "ChannelSensitivityUnitsSequence" in self._dataset:
            if len(self._ChannelSensitivityUnitsSequence) == len(self._dataset.ChannelSensitivityUnitsSequence):
                return self._ChannelSensitivityUnitsSequence
            else:
                return [ChannelSensitivityUnitsSequenceItem(x) for x in self._dataset.ChannelSensitivityUnitsSequence]
        return None

    @ChannelSensitivityUnitsSequence.setter
    def ChannelSensitivityUnitsSequence(self, value: Optional[List[ChannelSensitivityUnitsSequenceItem]]):
        if value is None:
            self._ChannelSensitivityUnitsSequence = []
            if "ChannelSensitivityUnitsSequence" in self._dataset:
                del self._dataset.ChannelSensitivityUnitsSequence
        elif not isinstance(value, list) or not all(isinstance(item, ChannelSensitivityUnitsSequenceItem) for item in value):
            raise ValueError(f"ChannelSensitivityUnitsSequence must be a list of ChannelSensitivityUnitsSequenceItem objects")
        else:
            self._ChannelSensitivityUnitsSequence = value
            if "ChannelSensitivityUnitsSequence" not in self._dataset:
                self._dataset.ChannelSensitivityUnitsSequence = pydicom.Sequence()
            self._dataset.ChannelSensitivityUnitsSequence.clear()
            self._dataset.ChannelSensitivityUnitsSequence.extend([item.to_dataset() for item in value])

    def add_ChannelSensitivityUnits(self, item: ChannelSensitivityUnitsSequenceItem):
        if not isinstance(item, ChannelSensitivityUnitsSequenceItem):
            raise ValueError(f"Item must be an instance of ChannelSensitivityUnitsSequenceItem")
        self._ChannelSensitivityUnitsSequence.append(item)
        if "ChannelSensitivityUnitsSequence" not in self._dataset:
            self._dataset.ChannelSensitivityUnitsSequence = pydicom.Sequence()
        self._dataset.ChannelSensitivityUnitsSequence.append(item.to_dataset())

    @property
    def ChannelSensitivityCorrectionFactor(self) -> Optional[Decimal]:
        if "ChannelSensitivityCorrectionFactor" in self._dataset:
            return self._dataset.ChannelSensitivityCorrectionFactor
        return None

    @ChannelSensitivityCorrectionFactor.setter
    def ChannelSensitivityCorrectionFactor(self, value: Optional[Decimal]):
        if value is None:
            if "ChannelSensitivityCorrectionFactor" in self._dataset:
                del self._dataset.ChannelSensitivityCorrectionFactor
        else:
            self._dataset.ChannelSensitivityCorrectionFactor = value

    @property
    def ChannelBaseline(self) -> Optional[Decimal]:
        if "ChannelBaseline" in self._dataset:
            return self._dataset.ChannelBaseline
        return None

    @ChannelBaseline.setter
    def ChannelBaseline(self, value: Optional[Decimal]):
        if value is None:
            if "ChannelBaseline" in self._dataset:
                del self._dataset.ChannelBaseline
        else:
            self._dataset.ChannelBaseline = value

    @property
    def ChannelTimeSkew(self) -> Optional[Decimal]:
        if "ChannelTimeSkew" in self._dataset:
            return self._dataset.ChannelTimeSkew
        return None

    @ChannelTimeSkew.setter
    def ChannelTimeSkew(self, value: Optional[Decimal]):
        if value is None:
            if "ChannelTimeSkew" in self._dataset:
                del self._dataset.ChannelTimeSkew
        else:
            self._dataset.ChannelTimeSkew = value

    @property
    def ChannelSampleSkew(self) -> Optional[Decimal]:
        if "ChannelSampleSkew" in self._dataset:
            return self._dataset.ChannelSampleSkew
        return None

    @ChannelSampleSkew.setter
    def ChannelSampleSkew(self, value: Optional[Decimal]):
        if value is None:
            if "ChannelSampleSkew" in self._dataset:
                del self._dataset.ChannelSampleSkew
        else:
            self._dataset.ChannelSampleSkew = value

    @property
    def ChannelOffset(self) -> Optional[Decimal]:
        if "ChannelOffset" in self._dataset:
            return self._dataset.ChannelOffset
        return None

    @ChannelOffset.setter
    def ChannelOffset(self, value: Optional[Decimal]):
        if value is None:
            if "ChannelOffset" in self._dataset:
                del self._dataset.ChannelOffset
        else:
            self._dataset.ChannelOffset = value

    @property
    def WaveformBitsStored(self) -> Optional[int]:
        if "WaveformBitsStored" in self._dataset:
            return self._dataset.WaveformBitsStored
        return None

    @WaveformBitsStored.setter
    def WaveformBitsStored(self, value: Optional[int]):
        if value is None:
            if "WaveformBitsStored" in self._dataset:
                del self._dataset.WaveformBitsStored
        else:
            self._dataset.WaveformBitsStored = value

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
    def ChannelImpedanceSequence(self) -> Optional[List[ChannelImpedanceSequenceItem]]:
        if "ChannelImpedanceSequence" in self._dataset:
            if len(self._ChannelImpedanceSequence) == len(self._dataset.ChannelImpedanceSequence):
                return self._ChannelImpedanceSequence
            else:
                return [ChannelImpedanceSequenceItem(x) for x in self._dataset.ChannelImpedanceSequence]
        return None

    @ChannelImpedanceSequence.setter
    def ChannelImpedanceSequence(self, value: Optional[List[ChannelImpedanceSequenceItem]]):
        if value is None:
            self._ChannelImpedanceSequence = []
            if "ChannelImpedanceSequence" in self._dataset:
                del self._dataset.ChannelImpedanceSequence
        elif not isinstance(value, list) or not all(isinstance(item, ChannelImpedanceSequenceItem) for item in value):
            raise ValueError(f"ChannelImpedanceSequence must be a list of ChannelImpedanceSequenceItem objects")
        else:
            self._ChannelImpedanceSequence = value
            if "ChannelImpedanceSequence" not in self._dataset:
                self._dataset.ChannelImpedanceSequence = pydicom.Sequence()
            self._dataset.ChannelImpedanceSequence.clear()
            self._dataset.ChannelImpedanceSequence.extend([item.to_dataset() for item in value])

    def add_ChannelImpedance(self, item: ChannelImpedanceSequenceItem):
        if not isinstance(item, ChannelImpedanceSequenceItem):
            raise ValueError(f"Item must be an instance of ChannelImpedanceSequenceItem")
        self._ChannelImpedanceSequence.append(item)
        if "ChannelImpedanceSequence" not in self._dataset:
            self._dataset.ChannelImpedanceSequence = pydicom.Sequence()
        self._dataset.ChannelImpedanceSequence.append(item.to_dataset())

    @property
    def WaveformAmplifierType(self) -> Optional[str]:
        if "WaveformAmplifierType" in self._dataset:
            return self._dataset.WaveformAmplifierType
        return None

    @WaveformAmplifierType.setter
    def WaveformAmplifierType(self, value: Optional[str]):
        if value is None:
            if "WaveformAmplifierType" in self._dataset:
                del self._dataset.WaveformAmplifierType
        else:
            self._dataset.WaveformAmplifierType = value

    @property
    def FilterLowFrequencyCharacteristicsSequence(self) -> Optional[List[FilterLowFrequencyCharacteristicsSequenceItem]]:
        if "FilterLowFrequencyCharacteristicsSequence" in self._dataset:
            if len(self._FilterLowFrequencyCharacteristicsSequence) == len(
                self._dataset.FilterLowFrequencyCharacteristicsSequence
            ):
                return self._FilterLowFrequencyCharacteristicsSequence
            else:
                return [
                    FilterLowFrequencyCharacteristicsSequenceItem(x)
                    for x in self._dataset.FilterLowFrequencyCharacteristicsSequence
                ]
        return None

    @FilterLowFrequencyCharacteristicsSequence.setter
    def FilterLowFrequencyCharacteristicsSequence(self, value: Optional[List[FilterLowFrequencyCharacteristicsSequenceItem]]):
        if value is None:
            self._FilterLowFrequencyCharacteristicsSequence = []
            if "FilterLowFrequencyCharacteristicsSequence" in self._dataset:
                del self._dataset.FilterLowFrequencyCharacteristicsSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, FilterLowFrequencyCharacteristicsSequenceItem) for item in value
        ):
            raise ValueError(
                f"FilterLowFrequencyCharacteristicsSequence must be a list of FilterLowFrequencyCharacteristicsSequenceItem objects"
            )
        else:
            self._FilterLowFrequencyCharacteristicsSequence = value
            if "FilterLowFrequencyCharacteristicsSequence" not in self._dataset:
                self._dataset.FilterLowFrequencyCharacteristicsSequence = pydicom.Sequence()
            self._dataset.FilterLowFrequencyCharacteristicsSequence.clear()
            self._dataset.FilterLowFrequencyCharacteristicsSequence.extend([item.to_dataset() for item in value])

    def add_FilterLowFrequencyCharacteristics(self, item: FilterLowFrequencyCharacteristicsSequenceItem):
        if not isinstance(item, FilterLowFrequencyCharacteristicsSequenceItem):
            raise ValueError(f"Item must be an instance of FilterLowFrequencyCharacteristicsSequenceItem")
        self._FilterLowFrequencyCharacteristicsSequence.append(item)
        if "FilterLowFrequencyCharacteristicsSequence" not in self._dataset:
            self._dataset.FilterLowFrequencyCharacteristicsSequence = pydicom.Sequence()
        self._dataset.FilterLowFrequencyCharacteristicsSequence.append(item.to_dataset())

    @property
    def FilterHighFrequencyCharacteristicsSequence(self) -> Optional[List[FilterHighFrequencyCharacteristicsSequenceItem]]:
        if "FilterHighFrequencyCharacteristicsSequence" in self._dataset:
            if len(self._FilterHighFrequencyCharacteristicsSequence) == len(
                self._dataset.FilterHighFrequencyCharacteristicsSequence
            ):
                return self._FilterHighFrequencyCharacteristicsSequence
            else:
                return [
                    FilterHighFrequencyCharacteristicsSequenceItem(x)
                    for x in self._dataset.FilterHighFrequencyCharacteristicsSequence
                ]
        return None

    @FilterHighFrequencyCharacteristicsSequence.setter
    def FilterHighFrequencyCharacteristicsSequence(
        self, value: Optional[List[FilterHighFrequencyCharacteristicsSequenceItem]]
    ):
        if value is None:
            self._FilterHighFrequencyCharacteristicsSequence = []
            if "FilterHighFrequencyCharacteristicsSequence" in self._dataset:
                del self._dataset.FilterHighFrequencyCharacteristicsSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, FilterHighFrequencyCharacteristicsSequenceItem) for item in value
        ):
            raise ValueError(
                f"FilterHighFrequencyCharacteristicsSequence must be a list of FilterHighFrequencyCharacteristicsSequenceItem objects"
            )
        else:
            self._FilterHighFrequencyCharacteristicsSequence = value
            if "FilterHighFrequencyCharacteristicsSequence" not in self._dataset:
                self._dataset.FilterHighFrequencyCharacteristicsSequence = pydicom.Sequence()
            self._dataset.FilterHighFrequencyCharacteristicsSequence.clear()
            self._dataset.FilterHighFrequencyCharacteristicsSequence.extend([item.to_dataset() for item in value])

    def add_FilterHighFrequencyCharacteristics(self, item: FilterHighFrequencyCharacteristicsSequenceItem):
        if not isinstance(item, FilterHighFrequencyCharacteristicsSequenceItem):
            raise ValueError(f"Item must be an instance of FilterHighFrequencyCharacteristicsSequenceItem")
        self._FilterHighFrequencyCharacteristicsSequence.append(item)
        if "FilterHighFrequencyCharacteristicsSequence" not in self._dataset:
            self._dataset.FilterHighFrequencyCharacteristicsSequence = pydicom.Sequence()
        self._dataset.FilterHighFrequencyCharacteristicsSequence.append(item.to_dataset())

    @property
    def SummarizedFilterLookupTable(self) -> Optional[list]:
        if "SummarizedFilterLookupTable" in self._dataset:
            return self._dataset.SummarizedFilterLookupTable
        return None

    @SummarizedFilterLookupTable.setter
    def SummarizedFilterLookupTable(self, value: Optional[list]):
        if value is None:
            if "SummarizedFilterLookupTable" in self._dataset:
                del self._dataset.SummarizedFilterLookupTable
        else:
            self._dataset.SummarizedFilterLookupTable = value

    @property
    def NotchFilterCharacteristicsSequence(self) -> Optional[List[NotchFilterCharacteristicsSequenceItem]]:
        if "NotchFilterCharacteristicsSequence" in self._dataset:
            if len(self._NotchFilterCharacteristicsSequence) == len(self._dataset.NotchFilterCharacteristicsSequence):
                return self._NotchFilterCharacteristicsSequence
            else:
                return [NotchFilterCharacteristicsSequenceItem(x) for x in self._dataset.NotchFilterCharacteristicsSequence]
        return None

    @NotchFilterCharacteristicsSequence.setter
    def NotchFilterCharacteristicsSequence(self, value: Optional[List[NotchFilterCharacteristicsSequenceItem]]):
        if value is None:
            self._NotchFilterCharacteristicsSequence = []
            if "NotchFilterCharacteristicsSequence" in self._dataset:
                del self._dataset.NotchFilterCharacteristicsSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, NotchFilterCharacteristicsSequenceItem) for item in value
        ):
            raise ValueError(
                f"NotchFilterCharacteristicsSequence must be a list of NotchFilterCharacteristicsSequenceItem objects"
            )
        else:
            self._NotchFilterCharacteristicsSequence = value
            if "NotchFilterCharacteristicsSequence" not in self._dataset:
                self._dataset.NotchFilterCharacteristicsSequence = pydicom.Sequence()
            self._dataset.NotchFilterCharacteristicsSequence.clear()
            self._dataset.NotchFilterCharacteristicsSequence.extend([item.to_dataset() for item in value])

    def add_NotchFilterCharacteristics(self, item: NotchFilterCharacteristicsSequenceItem):
        if not isinstance(item, NotchFilterCharacteristicsSequenceItem):
            raise ValueError(f"Item must be an instance of NotchFilterCharacteristicsSequenceItem")
        self._NotchFilterCharacteristicsSequence.append(item)
        if "NotchFilterCharacteristicsSequence" not in self._dataset:
            self._dataset.NotchFilterCharacteristicsSequence = pydicom.Sequence()
        self._dataset.NotchFilterCharacteristicsSequence.append(item.to_dataset())

    @property
    def ChannelMinimumValue(self) -> Optional[bytes]:
        if "ChannelMinimumValue" in self._dataset:
            return self._dataset.ChannelMinimumValue
        return None

    @ChannelMinimumValue.setter
    def ChannelMinimumValue(self, value: Optional[bytes]):
        if value is None:
            if "ChannelMinimumValue" in self._dataset:
                del self._dataset.ChannelMinimumValue
        else:
            self._dataset.ChannelMinimumValue = value

    @property
    def ChannelMaximumValue(self) -> Optional[bytes]:
        if "ChannelMaximumValue" in self._dataset:
            return self._dataset.ChannelMaximumValue
        return None

    @ChannelMaximumValue.setter
    def ChannelMaximumValue(self, value: Optional[bytes]):
        if value is None:
            if "ChannelMaximumValue" in self._dataset:
                del self._dataset.ChannelMaximumValue
        else:
            self._dataset.ChannelMaximumValue = value
