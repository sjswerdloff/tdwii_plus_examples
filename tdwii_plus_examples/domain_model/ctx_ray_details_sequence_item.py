from decimal import Decimal
from typing import Any, List, Optional  # noqa

import pydicom


class CTXRayDetailsSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def KVP(self) -> Optional[Decimal]:
        if "KVP" in self._dataset:
            return self._dataset.KVP
        return None

    @KVP.setter
    def KVP(self, value: Optional[Decimal]):
        if value is None:
            if "KVP" in self._dataset:
                del self._dataset.KVP
        else:
            self._dataset.KVP = value

    @property
    def DataCollectionDiameter(self) -> Optional[Decimal]:
        if "DataCollectionDiameter" in self._dataset:
            return self._dataset.DataCollectionDiameter
        return None

    @DataCollectionDiameter.setter
    def DataCollectionDiameter(self, value: Optional[Decimal]):
        if value is None:
            if "DataCollectionDiameter" in self._dataset:
                del self._dataset.DataCollectionDiameter
        else:
            self._dataset.DataCollectionDiameter = value

    @property
    def CardiacFramingType(self) -> Optional[str]:
        if "CardiacFramingType" in self._dataset:
            return self._dataset.CardiacFramingType
        return None

    @CardiacFramingType.setter
    def CardiacFramingType(self, value: Optional[str]):
        if value is None:
            if "CardiacFramingType" in self._dataset:
                del self._dataset.CardiacFramingType
        else:
            self._dataset.CardiacFramingType = value

    @property
    def LowRRValue(self) -> Optional[int]:
        if "LowRRValue" in self._dataset:
            return self._dataset.LowRRValue
        return None

    @LowRRValue.setter
    def LowRRValue(self, value: Optional[int]):
        if value is None:
            if "LowRRValue" in self._dataset:
                del self._dataset.LowRRValue
        else:
            self._dataset.LowRRValue = value

    @property
    def HighRRValue(self) -> Optional[int]:
        if "HighRRValue" in self._dataset:
            return self._dataset.HighRRValue
        return None

    @HighRRValue.setter
    def HighRRValue(self, value: Optional[int]):
        if value is None:
            if "HighRRValue" in self._dataset:
                del self._dataset.HighRRValue
        else:
            self._dataset.HighRRValue = value

    @property
    def SkipBeats(self) -> Optional[int]:
        if "SkipBeats" in self._dataset:
            return self._dataset.SkipBeats
        return None

    @SkipBeats.setter
    def SkipBeats(self, value: Optional[int]):
        if value is None:
            if "SkipBeats" in self._dataset:
                del self._dataset.SkipBeats
        else:
            self._dataset.SkipBeats = value

    @property
    def FilterType(self) -> Optional[str]:
        if "FilterType" in self._dataset:
            return self._dataset.FilterType
        return None

    @FilterType.setter
    def FilterType(self, value: Optional[str]):
        if value is None:
            if "FilterType" in self._dataset:
                del self._dataset.FilterType
        else:
            self._dataset.FilterType = value

    @property
    def FocalSpots(self) -> Optional[List[Decimal]]:
        if "FocalSpots" in self._dataset:
            return self._dataset.FocalSpots
        return None

    @FocalSpots.setter
    def FocalSpots(self, value: Optional[List[Decimal]]):
        if value is None:
            if "FocalSpots" in self._dataset:
                del self._dataset.FocalSpots
        else:
            self._dataset.FocalSpots = value

    @property
    def CardiacSynchronizationTechnique(self) -> Optional[str]:
        if "CardiacSynchronizationTechnique" in self._dataset:
            return self._dataset.CardiacSynchronizationTechnique
        return None

    @CardiacSynchronizationTechnique.setter
    def CardiacSynchronizationTechnique(self, value: Optional[str]):
        if value is None:
            if "CardiacSynchronizationTechnique" in self._dataset:
                del self._dataset.CardiacSynchronizationTechnique
        else:
            self._dataset.CardiacSynchronizationTechnique = value

    @property
    def CardiacRRIntervalSpecified(self) -> Optional[float]:
        if "CardiacRRIntervalSpecified" in self._dataset:
            return self._dataset.CardiacRRIntervalSpecified
        return None

    @CardiacRRIntervalSpecified.setter
    def CardiacRRIntervalSpecified(self, value: Optional[float]):
        if value is None:
            if "CardiacRRIntervalSpecified" in self._dataset:
                del self._dataset.CardiacRRIntervalSpecified
        else:
            self._dataset.CardiacRRIntervalSpecified = value

    @property
    def CardiacSignalSource(self) -> Optional[str]:
        if "CardiacSignalSource" in self._dataset:
            return self._dataset.CardiacSignalSource
        return None

    @CardiacSignalSource.setter
    def CardiacSignalSource(self, value: Optional[str]):
        if value is None:
            if "CardiacSignalSource" in self._dataset:
                del self._dataset.CardiacSignalSource
        else:
            self._dataset.CardiacSignalSource = value

    @property
    def CardiacBeatRejectionTechnique(self) -> Optional[str]:
        if "CardiacBeatRejectionTechnique" in self._dataset:
            return self._dataset.CardiacBeatRejectionTechnique
        return None

    @CardiacBeatRejectionTechnique.setter
    def CardiacBeatRejectionTechnique(self, value: Optional[str]):
        if value is None:
            if "CardiacBeatRejectionTechnique" in self._dataset:
                del self._dataset.CardiacBeatRejectionTechnique
        else:
            self._dataset.CardiacBeatRejectionTechnique = value

    @property
    def RespiratoryMotionCompensationTechnique(self) -> Optional[str]:
        if "RespiratoryMotionCompensationTechnique" in self._dataset:
            return self._dataset.RespiratoryMotionCompensationTechnique
        return None

    @RespiratoryMotionCompensationTechnique.setter
    def RespiratoryMotionCompensationTechnique(self, value: Optional[str]):
        if value is None:
            if "RespiratoryMotionCompensationTechnique" in self._dataset:
                del self._dataset.RespiratoryMotionCompensationTechnique
        else:
            self._dataset.RespiratoryMotionCompensationTechnique = value

    @property
    def RespiratorySignalSource(self) -> Optional[str]:
        if "RespiratorySignalSource" in self._dataset:
            return self._dataset.RespiratorySignalSource
        return None

    @RespiratorySignalSource.setter
    def RespiratorySignalSource(self, value: Optional[str]):
        if value is None:
            if "RespiratorySignalSource" in self._dataset:
                del self._dataset.RespiratorySignalSource
        else:
            self._dataset.RespiratorySignalSource = value

    @property
    def ExposureModulationType(self) -> Optional[List[str]]:
        if "ExposureModulationType" in self._dataset:
            return self._dataset.ExposureModulationType
        return None

    @ExposureModulationType.setter
    def ExposureModulationType(self, value: Optional[List[str]]):
        if value is None:
            if "ExposureModulationType" in self._dataset:
                del self._dataset.ExposureModulationType
        else:
            self._dataset.ExposureModulationType = value

    @property
    def ExposureTimeInms(self) -> Optional[float]:
        if "ExposureTimeInms" in self._dataset:
            return self._dataset.ExposureTimeInms
        return None

    @ExposureTimeInms.setter
    def ExposureTimeInms(self, value: Optional[float]):
        if value is None:
            if "ExposureTimeInms" in self._dataset:
                del self._dataset.ExposureTimeInms
        else:
            self._dataset.ExposureTimeInms = value

    @property
    def XRayTubeCurrentInmA(self) -> Optional[float]:
        if "XRayTubeCurrentInmA" in self._dataset:
            return self._dataset.XRayTubeCurrentInmA
        return None

    @XRayTubeCurrentInmA.setter
    def XRayTubeCurrentInmA(self, value: Optional[float]):
        if value is None:
            if "XRayTubeCurrentInmA" in self._dataset:
                del self._dataset.XRayTubeCurrentInmA
        else:
            self._dataset.XRayTubeCurrentInmA = value

    @property
    def ExposureInmAs(self) -> Optional[float]:
        if "ExposureInmAs" in self._dataset:
            return self._dataset.ExposureInmAs
        return None

    @ExposureInmAs.setter
    def ExposureInmAs(self, value: Optional[float]):
        if value is None:
            if "ExposureInmAs" in self._dataset:
                del self._dataset.ExposureInmAs
        else:
            self._dataset.ExposureInmAs = value

    @property
    def AutoKVPSelectionType(self) -> Optional[str]:
        if "AutoKVPSelectionType" in self._dataset:
            return self._dataset.AutoKVPSelectionType
        return None

    @AutoKVPSelectionType.setter
    def AutoKVPSelectionType(self, value: Optional[str]):
        if value is None:
            if "AutoKVPSelectionType" in self._dataset:
                del self._dataset.AutoKVPSelectionType
        else:
            self._dataset.AutoKVPSelectionType = value

    @property
    def AutoKVPUpperBound(self) -> Optional[float]:
        if "AutoKVPUpperBound" in self._dataset:
            return self._dataset.AutoKVPUpperBound
        return None

    @AutoKVPUpperBound.setter
    def AutoKVPUpperBound(self, value: Optional[float]):
        if value is None:
            if "AutoKVPUpperBound" in self._dataset:
                del self._dataset.AutoKVPUpperBound
        else:
            self._dataset.AutoKVPUpperBound = value

    @property
    def AutoKVPLowerBound(self) -> Optional[float]:
        if "AutoKVPLowerBound" in self._dataset:
            return self._dataset.AutoKVPLowerBound
        return None

    @AutoKVPLowerBound.setter
    def AutoKVPLowerBound(self, value: Optional[float]):
        if value is None:
            if "AutoKVPLowerBound" in self._dataset:
                del self._dataset.AutoKVPLowerBound
        else:
            self._dataset.AutoKVPLowerBound = value

    @property
    def RespiratoryTriggerType(self) -> Optional[str]:
        if "RespiratoryTriggerType" in self._dataset:
            return self._dataset.RespiratoryTriggerType
        return None

    @RespiratoryTriggerType.setter
    def RespiratoryTriggerType(self, value: Optional[str]):
        if value is None:
            if "RespiratoryTriggerType" in self._dataset:
                del self._dataset.RespiratoryTriggerType
        else:
            self._dataset.RespiratoryTriggerType = value

    @property
    def RespiratoryTriggerDelayThreshold(self) -> Optional[float]:
        if "RespiratoryTriggerDelayThreshold" in self._dataset:
            return self._dataset.RespiratoryTriggerDelayThreshold
        return None

    @RespiratoryTriggerDelayThreshold.setter
    def RespiratoryTriggerDelayThreshold(self, value: Optional[float]):
        if value is None:
            if "RespiratoryTriggerDelayThreshold" in self._dataset:
                del self._dataset.RespiratoryTriggerDelayThreshold
        else:
            self._dataset.RespiratoryTriggerDelayThreshold = value

    @property
    def BeamNumber(self) -> Optional[int]:
        if "BeamNumber" in self._dataset:
            return self._dataset.BeamNumber
        return None

    @BeamNumber.setter
    def BeamNumber(self, value: Optional[int]):
        if value is None:
            if "BeamNumber" in self._dataset:
                del self._dataset.BeamNumber
        else:
            self._dataset.BeamNumber = value
