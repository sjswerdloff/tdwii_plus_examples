from decimal import Decimal
from typing import Any, List, Optional  # noqa

import pydicom

from .code_sequence_item import CodeSequenceItem


class RadiopharmaceuticalInformationSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._RadionuclideCodeSequence: List[CodeSequenceItem] = []
        self._AdministrationRouteCodeSequence: List[CodeSequenceItem] = []
        self._RadiopharmaceuticalCodeSequence: List[CodeSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def RadiopharmaceuticalAdministrationEventUID(self) -> Optional[str]:
        if "RadiopharmaceuticalAdministrationEventUID" in self._dataset:
            return self._dataset.RadiopharmaceuticalAdministrationEventUID
        return None

    @RadiopharmaceuticalAdministrationEventUID.setter
    def RadiopharmaceuticalAdministrationEventUID(self, value: Optional[str]):
        if value is None:
            if "RadiopharmaceuticalAdministrationEventUID" in self._dataset:
                del self._dataset.RadiopharmaceuticalAdministrationEventUID
        else:
            self._dataset.RadiopharmaceuticalAdministrationEventUID = value

    @property
    def RadiopharmaceuticalVolume(self) -> Optional[Decimal]:
        if "RadiopharmaceuticalVolume" in self._dataset:
            return self._dataset.RadiopharmaceuticalVolume
        return None

    @RadiopharmaceuticalVolume.setter
    def RadiopharmaceuticalVolume(self, value: Optional[Decimal]):
        if value is None:
            if "RadiopharmaceuticalVolume" in self._dataset:
                del self._dataset.RadiopharmaceuticalVolume
        else:
            self._dataset.RadiopharmaceuticalVolume = value

    @property
    def RadionuclideTotalDose(self) -> Optional[Decimal]:
        if "RadionuclideTotalDose" in self._dataset:
            return self._dataset.RadionuclideTotalDose
        return None

    @RadionuclideTotalDose.setter
    def RadionuclideTotalDose(self, value: Optional[Decimal]):
        if value is None:
            if "RadionuclideTotalDose" in self._dataset:
                del self._dataset.RadionuclideTotalDose
        else:
            self._dataset.RadionuclideTotalDose = value

    @property
    def RadionuclideHalfLife(self) -> Optional[Decimal]:
        if "RadionuclideHalfLife" in self._dataset:
            return self._dataset.RadionuclideHalfLife
        return None

    @RadionuclideHalfLife.setter
    def RadionuclideHalfLife(self, value: Optional[Decimal]):
        if value is None:
            if "RadionuclideHalfLife" in self._dataset:
                del self._dataset.RadionuclideHalfLife
        else:
            self._dataset.RadionuclideHalfLife = value

    @property
    def RadionuclidePositronFraction(self) -> Optional[Decimal]:
        if "RadionuclidePositronFraction" in self._dataset:
            return self._dataset.RadionuclidePositronFraction
        return None

    @RadionuclidePositronFraction.setter
    def RadionuclidePositronFraction(self, value: Optional[Decimal]):
        if value is None:
            if "RadionuclidePositronFraction" in self._dataset:
                del self._dataset.RadionuclidePositronFraction
        else:
            self._dataset.RadionuclidePositronFraction = value

    @property
    def RadiopharmaceuticalSpecificActivity(self) -> Optional[Decimal]:
        if "RadiopharmaceuticalSpecificActivity" in self._dataset:
            return self._dataset.RadiopharmaceuticalSpecificActivity
        return None

    @RadiopharmaceuticalSpecificActivity.setter
    def RadiopharmaceuticalSpecificActivity(self, value: Optional[Decimal]):
        if value is None:
            if "RadiopharmaceuticalSpecificActivity" in self._dataset:
                del self._dataset.RadiopharmaceuticalSpecificActivity
        else:
            self._dataset.RadiopharmaceuticalSpecificActivity = value

    @property
    def RadiopharmaceuticalStartDateTime(self) -> Optional[str]:
        if "RadiopharmaceuticalStartDateTime" in self._dataset:
            return self._dataset.RadiopharmaceuticalStartDateTime
        return None

    @RadiopharmaceuticalStartDateTime.setter
    def RadiopharmaceuticalStartDateTime(self, value: Optional[str]):
        if value is None:
            if "RadiopharmaceuticalStartDateTime" in self._dataset:
                del self._dataset.RadiopharmaceuticalStartDateTime
        else:
            self._dataset.RadiopharmaceuticalStartDateTime = value

    @property
    def RadiopharmaceuticalStopDateTime(self) -> Optional[str]:
        if "RadiopharmaceuticalStopDateTime" in self._dataset:
            return self._dataset.RadiopharmaceuticalStopDateTime
        return None

    @RadiopharmaceuticalStopDateTime.setter
    def RadiopharmaceuticalStopDateTime(self, value: Optional[str]):
        if value is None:
            if "RadiopharmaceuticalStopDateTime" in self._dataset:
                del self._dataset.RadiopharmaceuticalStopDateTime
        else:
            self._dataset.RadiopharmaceuticalStopDateTime = value

    @property
    def RadiopharmaceuticalAgentNumber(self) -> Optional[int]:
        if "RadiopharmaceuticalAgentNumber" in self._dataset:
            return self._dataset.RadiopharmaceuticalAgentNumber
        return None

    @RadiopharmaceuticalAgentNumber.setter
    def RadiopharmaceuticalAgentNumber(self, value: Optional[int]):
        if value is None:
            if "RadiopharmaceuticalAgentNumber" in self._dataset:
                del self._dataset.RadiopharmaceuticalAgentNumber
        else:
            self._dataset.RadiopharmaceuticalAgentNumber = value

    @property
    def RadionuclideCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "RadionuclideCodeSequence" in self._dataset:
            if len(self._RadionuclideCodeSequence) == len(self._dataset.RadionuclideCodeSequence):
                return self._RadionuclideCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.RadionuclideCodeSequence]
        return None

    @RadionuclideCodeSequence.setter
    def RadionuclideCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._RadionuclideCodeSequence = []
            if "RadionuclideCodeSequence" in self._dataset:
                del self._dataset.RadionuclideCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("RadionuclideCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._RadionuclideCodeSequence = value
            if "RadionuclideCodeSequence" not in self._dataset:
                self._dataset.RadionuclideCodeSequence = pydicom.Sequence()
            self._dataset.RadionuclideCodeSequence.clear()
            self._dataset.RadionuclideCodeSequence.extend([item.to_dataset() for item in value])

    def add_RadionuclideCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._RadionuclideCodeSequence.append(item)
        if "RadionuclideCodeSequence" not in self._dataset:
            self._dataset.RadionuclideCodeSequence = pydicom.Sequence()
        self._dataset.RadionuclideCodeSequence.append(item.to_dataset())

    @property
    def AdministrationRouteCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "AdministrationRouteCodeSequence" in self._dataset:
            if len(self._AdministrationRouteCodeSequence) == len(self._dataset.AdministrationRouteCodeSequence):
                return self._AdministrationRouteCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.AdministrationRouteCodeSequence]
        return None

    @AdministrationRouteCodeSequence.setter
    def AdministrationRouteCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._AdministrationRouteCodeSequence = []
            if "AdministrationRouteCodeSequence" in self._dataset:
                del self._dataset.AdministrationRouteCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("AdministrationRouteCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._AdministrationRouteCodeSequence = value
            if "AdministrationRouteCodeSequence" not in self._dataset:
                self._dataset.AdministrationRouteCodeSequence = pydicom.Sequence()
            self._dataset.AdministrationRouteCodeSequence.clear()
            self._dataset.AdministrationRouteCodeSequence.extend([item.to_dataset() for item in value])

    def add_AdministrationRouteCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._AdministrationRouteCodeSequence.append(item)
        if "AdministrationRouteCodeSequence" not in self._dataset:
            self._dataset.AdministrationRouteCodeSequence = pydicom.Sequence()
        self._dataset.AdministrationRouteCodeSequence.append(item.to_dataset())

    @property
    def RadiopharmaceuticalCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "RadiopharmaceuticalCodeSequence" in self._dataset:
            if len(self._RadiopharmaceuticalCodeSequence) == len(self._dataset.RadiopharmaceuticalCodeSequence):
                return self._RadiopharmaceuticalCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.RadiopharmaceuticalCodeSequence]
        return None

    @RadiopharmaceuticalCodeSequence.setter
    def RadiopharmaceuticalCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._RadiopharmaceuticalCodeSequence = []
            if "RadiopharmaceuticalCodeSequence" in self._dataset:
                del self._dataset.RadiopharmaceuticalCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("RadiopharmaceuticalCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._RadiopharmaceuticalCodeSequence = value
            if "RadiopharmaceuticalCodeSequence" not in self._dataset:
                self._dataset.RadiopharmaceuticalCodeSequence = pydicom.Sequence()
            self._dataset.RadiopharmaceuticalCodeSequence.clear()
            self._dataset.RadiopharmaceuticalCodeSequence.extend([item.to_dataset() for item in value])

    def add_RadiopharmaceuticalCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._RadiopharmaceuticalCodeSequence.append(item)
        if "RadiopharmaceuticalCodeSequence" not in self._dataset:
            self._dataset.RadiopharmaceuticalCodeSequence = pydicom.Sequence()
        self._dataset.RadiopharmaceuticalCodeSequence.append(item.to_dataset())
