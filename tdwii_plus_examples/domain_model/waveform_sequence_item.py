from decimal import Decimal
from typing import Any, List, Optional

import pydicom

from .channel_definition_sequence_item import ChannelDefinitionSequenceItem


class WaveformSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._ChannelDefinitionSequence: List[ChannelDefinitionSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def MultiplexGroupTimeOffset(self) -> Optional[Decimal]:
        if "MultiplexGroupTimeOffset" in self._dataset:
            return self._dataset.MultiplexGroupTimeOffset
        return None

    @MultiplexGroupTimeOffset.setter
    def MultiplexGroupTimeOffset(self, value: Optional[Decimal]):
        if value is None:
            if "MultiplexGroupTimeOffset" in self._dataset:
                del self._dataset.MultiplexGroupTimeOffset
        else:
            self._dataset.MultiplexGroupTimeOffset = value

    @property
    def TriggerTimeOffset(self) -> Optional[Decimal]:
        if "TriggerTimeOffset" in self._dataset:
            return self._dataset.TriggerTimeOffset
        return None

    @TriggerTimeOffset.setter
    def TriggerTimeOffset(self, value: Optional[Decimal]):
        if value is None:
            if "TriggerTimeOffset" in self._dataset:
                del self._dataset.TriggerTimeOffset
        else:
            self._dataset.TriggerTimeOffset = value

    @property
    def TriggerSamplePosition(self) -> Optional[int]:
        if "TriggerSamplePosition" in self._dataset:
            return self._dataset.TriggerSamplePosition
        return None

    @TriggerSamplePosition.setter
    def TriggerSamplePosition(self, value: Optional[int]):
        if value is None:
            if "TriggerSamplePosition" in self._dataset:
                del self._dataset.TriggerSamplePosition
        else:
            self._dataset.TriggerSamplePosition = value

    @property
    def WaveformOriginality(self) -> Optional[str]:
        if "WaveformOriginality" in self._dataset:
            return self._dataset.WaveformOriginality
        return None

    @WaveformOriginality.setter
    def WaveformOriginality(self, value: Optional[str]):
        if value is None:
            if "WaveformOriginality" in self._dataset:
                del self._dataset.WaveformOriginality
        else:
            self._dataset.WaveformOriginality = value

    @property
    def NumberOfWaveformChannels(self) -> Optional[int]:
        if "NumberOfWaveformChannels" in self._dataset:
            return self._dataset.NumberOfWaveformChannels
        return None

    @NumberOfWaveformChannels.setter
    def NumberOfWaveformChannels(self, value: Optional[int]):
        if value is None:
            if "NumberOfWaveformChannels" in self._dataset:
                del self._dataset.NumberOfWaveformChannels
        else:
            self._dataset.NumberOfWaveformChannels = value

    @property
    def NumberOfWaveformSamples(self) -> Optional[int]:
        if "NumberOfWaveformSamples" in self._dataset:
            return self._dataset.NumberOfWaveformSamples
        return None

    @NumberOfWaveformSamples.setter
    def NumberOfWaveformSamples(self, value: Optional[int]):
        if value is None:
            if "NumberOfWaveformSamples" in self._dataset:
                del self._dataset.NumberOfWaveformSamples
        else:
            self._dataset.NumberOfWaveformSamples = value

    @property
    def SamplingFrequency(self) -> Optional[Decimal]:
        if "SamplingFrequency" in self._dataset:
            return self._dataset.SamplingFrequency
        return None

    @SamplingFrequency.setter
    def SamplingFrequency(self, value: Optional[Decimal]):
        if value is None:
            if "SamplingFrequency" in self._dataset:
                del self._dataset.SamplingFrequency
        else:
            self._dataset.SamplingFrequency = value

    @property
    def MultiplexGroupLabel(self) -> Optional[str]:
        if "MultiplexGroupLabel" in self._dataset:
            return self._dataset.MultiplexGroupLabel
        return None

    @MultiplexGroupLabel.setter
    def MultiplexGroupLabel(self, value: Optional[str]):
        if value is None:
            if "MultiplexGroupLabel" in self._dataset:
                del self._dataset.MultiplexGroupLabel
        else:
            self._dataset.MultiplexGroupLabel = value

    @property
    def ChannelDefinitionSequence(self) -> Optional[List[ChannelDefinitionSequenceItem]]:
        if "ChannelDefinitionSequence" in self._dataset:
            if len(self._ChannelDefinitionSequence) == len(self._dataset.ChannelDefinitionSequence):
                return self._ChannelDefinitionSequence
            else:
                return [ChannelDefinitionSequenceItem(x) for x in self._dataset.ChannelDefinitionSequence]
        return None

    @ChannelDefinitionSequence.setter
    def ChannelDefinitionSequence(self, value: Optional[List[ChannelDefinitionSequenceItem]]):
        if value is None:
            self._ChannelDefinitionSequence = []
            if "ChannelDefinitionSequence" in self._dataset:
                del self._dataset.ChannelDefinitionSequence
        elif not isinstance(value, list) or not all(isinstance(item, ChannelDefinitionSequenceItem) for item in value):
            raise ValueError(f"ChannelDefinitionSequence must be a list of ChannelDefinitionSequenceItem objects")
        else:
            self._ChannelDefinitionSequence = value
            if "ChannelDefinitionSequence" not in self._dataset:
                self._dataset.ChannelDefinitionSequence = pydicom.Sequence()
            self._dataset.ChannelDefinitionSequence.clear()
            self._dataset.ChannelDefinitionSequence.extend([item.to_dataset() for item in value])

    def add_ChannelDefinition(self, item: ChannelDefinitionSequenceItem):
        if not isinstance(item, ChannelDefinitionSequenceItem):
            raise ValueError(f"Item must be an instance of ChannelDefinitionSequenceItem")
        self._ChannelDefinitionSequence.append(item)
        if "ChannelDefinitionSequence" not in self._dataset:
            self._dataset.ChannelDefinitionSequence = pydicom.Sequence()
        self._dataset.ChannelDefinitionSequence.append(item.to_dataset())

    @property
    def MultiplexGroupUID(self) -> Optional[str]:
        if "MultiplexGroupUID" in self._dataset:
            return self._dataset.MultiplexGroupUID
        return None

    @MultiplexGroupUID.setter
    def MultiplexGroupUID(self, value: Optional[str]):
        if value is None:
            if "MultiplexGroupUID" in self._dataset:
                del self._dataset.MultiplexGroupUID
        else:
            self._dataset.MultiplexGroupUID = value

    @property
    def PowerlineFrequency(self) -> Optional[Decimal]:
        if "PowerlineFrequency" in self._dataset:
            return self._dataset.PowerlineFrequency
        return None

    @PowerlineFrequency.setter
    def PowerlineFrequency(self, value: Optional[Decimal]):
        if value is None:
            if "PowerlineFrequency" in self._dataset:
                del self._dataset.PowerlineFrequency
        else:
            self._dataset.PowerlineFrequency = value

    @property
    def WaveformBitsAllocated(self) -> Optional[int]:
        if "WaveformBitsAllocated" in self._dataset:
            return self._dataset.WaveformBitsAllocated
        return None

    @WaveformBitsAllocated.setter
    def WaveformBitsAllocated(self, value: Optional[int]):
        if value is None:
            if "WaveformBitsAllocated" in self._dataset:
                del self._dataset.WaveformBitsAllocated
        else:
            self._dataset.WaveformBitsAllocated = value

    @property
    def WaveformSampleInterpretation(self) -> Optional[str]:
        if "WaveformSampleInterpretation" in self._dataset:
            return self._dataset.WaveformSampleInterpretation
        return None

    @WaveformSampleInterpretation.setter
    def WaveformSampleInterpretation(self, value: Optional[str]):
        if value is None:
            if "WaveformSampleInterpretation" in self._dataset:
                del self._dataset.WaveformSampleInterpretation
        else:
            self._dataset.WaveformSampleInterpretation = value

    @property
    def WaveformPaddingValue(self) -> Optional[bytes]:
        if "WaveformPaddingValue" in self._dataset:
            return self._dataset.WaveformPaddingValue
        return None

    @WaveformPaddingValue.setter
    def WaveformPaddingValue(self, value: Optional[bytes]):
        if value is None:
            if "WaveformPaddingValue" in self._dataset:
                del self._dataset.WaveformPaddingValue
        else:
            self._dataset.WaveformPaddingValue = value

    @property
    def WaveformData(self) -> Optional[bytes]:
        if "WaveformData" in self._dataset:
            return self._dataset.WaveformData
        return None

    @WaveformData.setter
    def WaveformData(self, value: Optional[bytes]):
        if value is None:
            if "WaveformData" in self._dataset:
                del self._dataset.WaveformData
        else:
            self._dataset.WaveformData = value
