from decimal import Decimal
from typing import Any, List, Optional  # noqa

import pydicom

from .code_sequence_item import CodeSequenceItem
from .radiation_device_configuration_and_commissioning_key_sequence_item import (
    RadiationDeviceConfigurationAndCommissioningKeySequenceItem,
)


class RadiationGenerationModeSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._RadiationDeviceConfigurationAndCommissioningKeySequence: List[
            RadiationDeviceConfigurationAndCommissioningKeySequenceItem
        ] = []
        self._RadiationGenerationModeMachineCodeSequence: List[CodeSequenceItem] = []
        self._RadiationTypeCodeSequence: List[CodeSequenceItem] = []
        self._RadiationFluenceModifierCodeSequence: List[CodeSequenceItem] = []
        self._EnergyUnitCodeSequence: List[CodeSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def RadiationGenerationModeIndex(self) -> Optional[int]:
        if "RadiationGenerationModeIndex" in self._dataset:
            return self._dataset.RadiationGenerationModeIndex
        return None

    @RadiationGenerationModeIndex.setter
    def RadiationGenerationModeIndex(self, value: Optional[int]):
        if value is None:
            if "RadiationGenerationModeIndex" in self._dataset:
                del self._dataset.RadiationGenerationModeIndex
        else:
            self._dataset.RadiationGenerationModeIndex = value

    @property
    def RadiationDeviceConfigurationAndCommissioningKeySequence(
        self,
    ) -> Optional[List[RadiationDeviceConfigurationAndCommissioningKeySequenceItem]]:
        if "RadiationDeviceConfigurationAndCommissioningKeySequence" in self._dataset:
            if len(self._RadiationDeviceConfigurationAndCommissioningKeySequence) == len(
                self._dataset.RadiationDeviceConfigurationAndCommissioningKeySequence
            ):
                return self._RadiationDeviceConfigurationAndCommissioningKeySequence
            else:
                return [
                    RadiationDeviceConfigurationAndCommissioningKeySequenceItem(x)
                    for x in self._dataset.RadiationDeviceConfigurationAndCommissioningKeySequence
                ]
        return None

    @RadiationDeviceConfigurationAndCommissioningKeySequence.setter
    def RadiationDeviceConfigurationAndCommissioningKeySequence(
        self, value: Optional[List[RadiationDeviceConfigurationAndCommissioningKeySequenceItem]]
    ):
        if value is None:
            self._RadiationDeviceConfigurationAndCommissioningKeySequence = []
            if "RadiationDeviceConfigurationAndCommissioningKeySequence" in self._dataset:
                del self._dataset.RadiationDeviceConfigurationAndCommissioningKeySequence
        elif not isinstance(value, list) or not all(
            isinstance(item, RadiationDeviceConfigurationAndCommissioningKeySequenceItem) for item in value
        ):
            raise ValueError(
                "RadiationDeviceConfigurationAndCommissioningKeySequence must be a list of"
                " RadiationDeviceConfigurationAndCommissioningKeySequenceItem objects"
            )
        else:
            self._RadiationDeviceConfigurationAndCommissioningKeySequence = value
            if "RadiationDeviceConfigurationAndCommissioningKeySequence" not in self._dataset:
                self._dataset.RadiationDeviceConfigurationAndCommissioningKeySequence = pydicom.Sequence()
            self._dataset.RadiationDeviceConfigurationAndCommissioningKeySequence.clear()
            self._dataset.RadiationDeviceConfigurationAndCommissioningKeySequence.extend([item.to_dataset() for item in value])

    def add_RadiationDeviceConfigurationAndCommissioningKey(
        self, item: RadiationDeviceConfigurationAndCommissioningKeySequenceItem
    ):
        if not isinstance(item, RadiationDeviceConfigurationAndCommissioningKeySequenceItem):
            raise ValueError("Item must be an instance of RadiationDeviceConfigurationAndCommissioningKeySequenceItem")
        self._RadiationDeviceConfigurationAndCommissioningKeySequence.append(item)
        if "RadiationDeviceConfigurationAndCommissioningKeySequence" not in self._dataset:
            self._dataset.RadiationDeviceConfigurationAndCommissioningKeySequence = pydicom.Sequence()
        self._dataset.RadiationDeviceConfigurationAndCommissioningKeySequence.append(item.to_dataset())

    @property
    def RadiationGenerationModeLabel(self) -> Optional[str]:
        if "RadiationGenerationModeLabel" in self._dataset:
            return self._dataset.RadiationGenerationModeLabel
        return None

    @RadiationGenerationModeLabel.setter
    def RadiationGenerationModeLabel(self, value: Optional[str]):
        if value is None:
            if "RadiationGenerationModeLabel" in self._dataset:
                del self._dataset.RadiationGenerationModeLabel
        else:
            self._dataset.RadiationGenerationModeLabel = value

    @property
    def RadiationGenerationModeDescription(self) -> Optional[str]:
        if "RadiationGenerationModeDescription" in self._dataset:
            return self._dataset.RadiationGenerationModeDescription
        return None

    @RadiationGenerationModeDescription.setter
    def RadiationGenerationModeDescription(self, value: Optional[str]):
        if value is None:
            if "RadiationGenerationModeDescription" in self._dataset:
                del self._dataset.RadiationGenerationModeDescription
        else:
            self._dataset.RadiationGenerationModeDescription = value

    @property
    def RadiationGenerationModeMachineCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "RadiationGenerationModeMachineCodeSequence" in self._dataset:
            if len(self._RadiationGenerationModeMachineCodeSequence) == len(
                self._dataset.RadiationGenerationModeMachineCodeSequence
            ):
                return self._RadiationGenerationModeMachineCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.RadiationGenerationModeMachineCodeSequence]
        return None

    @RadiationGenerationModeMachineCodeSequence.setter
    def RadiationGenerationModeMachineCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._RadiationGenerationModeMachineCodeSequence = []
            if "RadiationGenerationModeMachineCodeSequence" in self._dataset:
                del self._dataset.RadiationGenerationModeMachineCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("RadiationGenerationModeMachineCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._RadiationGenerationModeMachineCodeSequence = value
            if "RadiationGenerationModeMachineCodeSequence" not in self._dataset:
                self._dataset.RadiationGenerationModeMachineCodeSequence = pydicom.Sequence()
            self._dataset.RadiationGenerationModeMachineCodeSequence.clear()
            self._dataset.RadiationGenerationModeMachineCodeSequence.extend([item.to_dataset() for item in value])

    def add_RadiationGenerationModeMachineCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._RadiationGenerationModeMachineCodeSequence.append(item)
        if "RadiationGenerationModeMachineCodeSequence" not in self._dataset:
            self._dataset.RadiationGenerationModeMachineCodeSequence = pydicom.Sequence()
        self._dataset.RadiationGenerationModeMachineCodeSequence.append(item.to_dataset())

    @property
    def RadiationTypeCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "RadiationTypeCodeSequence" in self._dataset:
            if len(self._RadiationTypeCodeSequence) == len(self._dataset.RadiationTypeCodeSequence):
                return self._RadiationTypeCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.RadiationTypeCodeSequence]
        return None

    @RadiationTypeCodeSequence.setter
    def RadiationTypeCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._RadiationTypeCodeSequence = []
            if "RadiationTypeCodeSequence" in self._dataset:
                del self._dataset.RadiationTypeCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("RadiationTypeCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._RadiationTypeCodeSequence = value
            if "RadiationTypeCodeSequence" not in self._dataset:
                self._dataset.RadiationTypeCodeSequence = pydicom.Sequence()
            self._dataset.RadiationTypeCodeSequence.clear()
            self._dataset.RadiationTypeCodeSequence.extend([item.to_dataset() for item in value])

    def add_RadiationTypeCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._RadiationTypeCodeSequence.append(item)
        if "RadiationTypeCodeSequence" not in self._dataset:
            self._dataset.RadiationTypeCodeSequence = pydicom.Sequence()
        self._dataset.RadiationTypeCodeSequence.append(item.to_dataset())

    @property
    def NominalEnergy(self) -> Optional[Decimal]:
        if "NominalEnergy" in self._dataset:
            return self._dataset.NominalEnergy
        return None

    @NominalEnergy.setter
    def NominalEnergy(self, value: Optional[Decimal]):
        if value is None:
            if "NominalEnergy" in self._dataset:
                del self._dataset.NominalEnergy
        else:
            self._dataset.NominalEnergy = value

    @property
    def MinimumNominalEnergy(self) -> Optional[Decimal]:
        if "MinimumNominalEnergy" in self._dataset:
            return self._dataset.MinimumNominalEnergy
        return None

    @MinimumNominalEnergy.setter
    def MinimumNominalEnergy(self, value: Optional[Decimal]):
        if value is None:
            if "MinimumNominalEnergy" in self._dataset:
                del self._dataset.MinimumNominalEnergy
        else:
            self._dataset.MinimumNominalEnergy = value

    @property
    def MaximumNominalEnergy(self) -> Optional[Decimal]:
        if "MaximumNominalEnergy" in self._dataset:
            return self._dataset.MaximumNominalEnergy
        return None

    @MaximumNominalEnergy.setter
    def MaximumNominalEnergy(self, value: Optional[Decimal]):
        if value is None:
            if "MaximumNominalEnergy" in self._dataset:
                del self._dataset.MaximumNominalEnergy
        else:
            self._dataset.MaximumNominalEnergy = value

    @property
    def RadiationFluenceModifierCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "RadiationFluenceModifierCodeSequence" in self._dataset:
            if len(self._RadiationFluenceModifierCodeSequence) == len(self._dataset.RadiationFluenceModifierCodeSequence):
                return self._RadiationFluenceModifierCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.RadiationFluenceModifierCodeSequence]
        return None

    @RadiationFluenceModifierCodeSequence.setter
    def RadiationFluenceModifierCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._RadiationFluenceModifierCodeSequence = []
            if "RadiationFluenceModifierCodeSequence" in self._dataset:
                del self._dataset.RadiationFluenceModifierCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("RadiationFluenceModifierCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._RadiationFluenceModifierCodeSequence = value
            if "RadiationFluenceModifierCodeSequence" not in self._dataset:
                self._dataset.RadiationFluenceModifierCodeSequence = pydicom.Sequence()
            self._dataset.RadiationFluenceModifierCodeSequence.clear()
            self._dataset.RadiationFluenceModifierCodeSequence.extend([item.to_dataset() for item in value])

    def add_RadiationFluenceModifierCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._RadiationFluenceModifierCodeSequence.append(item)
        if "RadiationFluenceModifierCodeSequence" not in self._dataset:
            self._dataset.RadiationFluenceModifierCodeSequence = pydicom.Sequence()
        self._dataset.RadiationFluenceModifierCodeSequence.append(item.to_dataset())

    @property
    def EnergyUnitCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "EnergyUnitCodeSequence" in self._dataset:
            if len(self._EnergyUnitCodeSequence) == len(self._dataset.EnergyUnitCodeSequence):
                return self._EnergyUnitCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.EnergyUnitCodeSequence]
        return None

    @EnergyUnitCodeSequence.setter
    def EnergyUnitCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._EnergyUnitCodeSequence = []
            if "EnergyUnitCodeSequence" in self._dataset:
                del self._dataset.EnergyUnitCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("EnergyUnitCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._EnergyUnitCodeSequence = value
            if "EnergyUnitCodeSequence" not in self._dataset:
                self._dataset.EnergyUnitCodeSequence = pydicom.Sequence()
            self._dataset.EnergyUnitCodeSequence.clear()
            self._dataset.EnergyUnitCodeSequence.extend([item.to_dataset() for item in value])

    def add_EnergyUnitCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._EnergyUnitCodeSequence.append(item)
        if "EnergyUnitCodeSequence" not in self._dataset:
            self._dataset.EnergyUnitCodeSequence = pydicom.Sequence()
        self._dataset.EnergyUnitCodeSequence.append(item.to_dataset())
