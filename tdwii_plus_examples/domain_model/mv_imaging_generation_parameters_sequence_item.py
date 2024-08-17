from typing import Any, List, Optional

import pydicom

from .code_sequence_item import CodeSequenceItem
from .delivery_rate_unit_sequence_item import DeliveryRateUnitSequenceItem
from .radiation_dosimeter_unit_sequence_item import RadiationDosimeterUnitSequenceItem
from .radiation_generation_mode_sequence_item import RadiationGenerationModeSequenceItem


class MVImagingGenerationParametersSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._EnergyDerivationCodeSequence: List[CodeSequenceItem] = []
        self._DeliveryRateUnitSequence: List[DeliveryRateUnitSequenceItem] = []
        self._RadiationDosimeterUnitSequence: List[RadiationDosimeterUnitSequenceItem] = []
        self._RadiationGenerationModeSequence: List[RadiationGenerationModeSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def EnergyDerivationCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "EnergyDerivationCodeSequence" in self._dataset:
            if len(self._EnergyDerivationCodeSequence) == len(self._dataset.EnergyDerivationCodeSequence):
                return self._EnergyDerivationCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.EnergyDerivationCodeSequence]
        return None

    @EnergyDerivationCodeSequence.setter
    def EnergyDerivationCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._EnergyDerivationCodeSequence = []
            if "EnergyDerivationCodeSequence" in self._dataset:
                del self._dataset.EnergyDerivationCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError(f"EnergyDerivationCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._EnergyDerivationCodeSequence = value
            if "EnergyDerivationCodeSequence" not in self._dataset:
                self._dataset.EnergyDerivationCodeSequence = pydicom.Sequence()
            self._dataset.EnergyDerivationCodeSequence.clear()
            self._dataset.EnergyDerivationCodeSequence.extend([item.to_dataset() for item in value])

    def add_EnergyDerivationCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError(f"Item must be an instance of CodeSequenceItem")
        self._EnergyDerivationCodeSequence.append(item)
        if "EnergyDerivationCodeSequence" not in self._dataset:
            self._dataset.EnergyDerivationCodeSequence = pydicom.Sequence()
        self._dataset.EnergyDerivationCodeSequence.append(item.to_dataset())

    @property
    def MaximumCumulativeMetersetExposure(self) -> Optional[float]:
        if "MaximumCumulativeMetersetExposure" in self._dataset:
            return self._dataset.MaximumCumulativeMetersetExposure
        return None

    @MaximumCumulativeMetersetExposure.setter
    def MaximumCumulativeMetersetExposure(self, value: Optional[float]):
        if value is None:
            if "MaximumCumulativeMetersetExposure" in self._dataset:
                del self._dataset.MaximumCumulativeMetersetExposure
        else:
            self._dataset.MaximumCumulativeMetersetExposure = value

    @property
    def DeliveryRate(self) -> Optional[float]:
        if "DeliveryRate" in self._dataset:
            return self._dataset.DeliveryRate
        return None

    @DeliveryRate.setter
    def DeliveryRate(self, value: Optional[float]):
        if value is None:
            if "DeliveryRate" in self._dataset:
                del self._dataset.DeliveryRate
        else:
            self._dataset.DeliveryRate = value

    @property
    def DeliveryRateUnitSequence(self) -> Optional[List[DeliveryRateUnitSequenceItem]]:
        if "DeliveryRateUnitSequence" in self._dataset:
            if len(self._DeliveryRateUnitSequence) == len(self._dataset.DeliveryRateUnitSequence):
                return self._DeliveryRateUnitSequence
            else:
                return [DeliveryRateUnitSequenceItem(x) for x in self._dataset.DeliveryRateUnitSequence]
        return None

    @DeliveryRateUnitSequence.setter
    def DeliveryRateUnitSequence(self, value: Optional[List[DeliveryRateUnitSequenceItem]]):
        if value is None:
            self._DeliveryRateUnitSequence = []
            if "DeliveryRateUnitSequence" in self._dataset:
                del self._dataset.DeliveryRateUnitSequence
        elif not isinstance(value, list) or not all(isinstance(item, DeliveryRateUnitSequenceItem) for item in value):
            raise ValueError(f"DeliveryRateUnitSequence must be a list of DeliveryRateUnitSequenceItem objects")
        else:
            self._DeliveryRateUnitSequence = value
            if "DeliveryRateUnitSequence" not in self._dataset:
                self._dataset.DeliveryRateUnitSequence = pydicom.Sequence()
            self._dataset.DeliveryRateUnitSequence.clear()
            self._dataset.DeliveryRateUnitSequence.extend([item.to_dataset() for item in value])

    def add_DeliveryRateUnit(self, item: DeliveryRateUnitSequenceItem):
        if not isinstance(item, DeliveryRateUnitSequenceItem):
            raise ValueError(f"Item must be an instance of DeliveryRateUnitSequenceItem")
        self._DeliveryRateUnitSequence.append(item)
        if "DeliveryRateUnitSequence" not in self._dataset:
            self._dataset.DeliveryRateUnitSequence = pydicom.Sequence()
        self._dataset.DeliveryRateUnitSequence.append(item.to_dataset())

    @property
    def RadiationDosimeterUnitSequence(self) -> Optional[List[RadiationDosimeterUnitSequenceItem]]:
        if "RadiationDosimeterUnitSequence" in self._dataset:
            if len(self._RadiationDosimeterUnitSequence) == len(self._dataset.RadiationDosimeterUnitSequence):
                return self._RadiationDosimeterUnitSequence
            else:
                return [RadiationDosimeterUnitSequenceItem(x) for x in self._dataset.RadiationDosimeterUnitSequence]
        return None

    @RadiationDosimeterUnitSequence.setter
    def RadiationDosimeterUnitSequence(self, value: Optional[List[RadiationDosimeterUnitSequenceItem]]):
        if value is None:
            self._RadiationDosimeterUnitSequence = []
            if "RadiationDosimeterUnitSequence" in self._dataset:
                del self._dataset.RadiationDosimeterUnitSequence
        elif not isinstance(value, list) or not all(isinstance(item, RadiationDosimeterUnitSequenceItem) for item in value):
            raise ValueError(f"RadiationDosimeterUnitSequence must be a list of RadiationDosimeterUnitSequenceItem objects")
        else:
            self._RadiationDosimeterUnitSequence = value
            if "RadiationDosimeterUnitSequence" not in self._dataset:
                self._dataset.RadiationDosimeterUnitSequence = pydicom.Sequence()
            self._dataset.RadiationDosimeterUnitSequence.clear()
            self._dataset.RadiationDosimeterUnitSequence.extend([item.to_dataset() for item in value])

    def add_RadiationDosimeterUnit(self, item: RadiationDosimeterUnitSequenceItem):
        if not isinstance(item, RadiationDosimeterUnitSequenceItem):
            raise ValueError(f"Item must be an instance of RadiationDosimeterUnitSequenceItem")
        self._RadiationDosimeterUnitSequence.append(item)
        if "RadiationDosimeterUnitSequence" not in self._dataset:
            self._dataset.RadiationDosimeterUnitSequence = pydicom.Sequence()
        self._dataset.RadiationDosimeterUnitSequence.append(item.to_dataset())

    @property
    def RadiationGenerationModeSequence(self) -> Optional[List[RadiationGenerationModeSequenceItem]]:
        if "RadiationGenerationModeSequence" in self._dataset:
            if len(self._RadiationGenerationModeSequence) == len(self._dataset.RadiationGenerationModeSequence):
                return self._RadiationGenerationModeSequence
            else:
                return [RadiationGenerationModeSequenceItem(x) for x in self._dataset.RadiationGenerationModeSequence]
        return None

    @RadiationGenerationModeSequence.setter
    def RadiationGenerationModeSequence(self, value: Optional[List[RadiationGenerationModeSequenceItem]]):
        if value is None:
            self._RadiationGenerationModeSequence = []
            if "RadiationGenerationModeSequence" in self._dataset:
                del self._dataset.RadiationGenerationModeSequence
        elif not isinstance(value, list) or not all(isinstance(item, RadiationGenerationModeSequenceItem) for item in value):
            raise ValueError(f"RadiationGenerationModeSequence must be a list of RadiationGenerationModeSequenceItem objects")
        else:
            self._RadiationGenerationModeSequence = value
            if "RadiationGenerationModeSequence" not in self._dataset:
                self._dataset.RadiationGenerationModeSequence = pydicom.Sequence()
            self._dataset.RadiationGenerationModeSequence.clear()
            self._dataset.RadiationGenerationModeSequence.extend([item.to_dataset() for item in value])

    def add_RadiationGenerationMode(self, item: RadiationGenerationModeSequenceItem):
        if not isinstance(item, RadiationGenerationModeSequenceItem):
            raise ValueError(f"Item must be an instance of RadiationGenerationModeSequenceItem")
        self._RadiationGenerationModeSequence.append(item)
        if "RadiationGenerationModeSequence" not in self._dataset:
            self._dataset.RadiationGenerationModeSequence = pydicom.Sequence()
        self._dataset.RadiationGenerationModeSequence.append(item.to_dataset())
