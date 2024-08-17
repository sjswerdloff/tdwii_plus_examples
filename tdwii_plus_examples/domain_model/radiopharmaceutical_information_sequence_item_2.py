from decimal import Decimal
from typing import Any, List, Optional

import pydicom

from .calibration_data_sequence_item import CalibrationDataSequenceItem
from .code_sequence_item import CodeSequenceItem


class RadiopharmaceuticalInformationSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._RadionuclideCodeSequence: List[CodeSequenceItem] = []
        self._AdministrationRouteCodeSequence: List[CodeSequenceItem] = []
        self._RadiopharmaceuticalCodeSequence: List[CodeSequenceItem] = []
        self._CalibrationDataSequence: List[CalibrationDataSequenceItem] = []

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
    def Radiopharmaceutical(self) -> Optional[str]:
        if "Radiopharmaceutical" in self._dataset:
            return self._dataset.Radiopharmaceutical
        return None

    @Radiopharmaceutical.setter
    def Radiopharmaceutical(self, value: Optional[str]):
        if value is None:
            if "Radiopharmaceutical" in self._dataset:
                del self._dataset.Radiopharmaceutical
        else:
            self._dataset.Radiopharmaceutical = value

    @property
    def RadiopharmaceuticalRoute(self) -> Optional[str]:
        if "RadiopharmaceuticalRoute" in self._dataset:
            return self._dataset.RadiopharmaceuticalRoute
        return None

    @RadiopharmaceuticalRoute.setter
    def RadiopharmaceuticalRoute(self, value: Optional[str]):
        if value is None:
            if "RadiopharmaceuticalRoute" in self._dataset:
                del self._dataset.RadiopharmaceuticalRoute
        else:
            self._dataset.RadiopharmaceuticalRoute = value

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
    def RadiopharmaceuticalStartTime(self) -> Optional[str]:
        if "RadiopharmaceuticalStartTime" in self._dataset:
            return self._dataset.RadiopharmaceuticalStartTime
        return None

    @RadiopharmaceuticalStartTime.setter
    def RadiopharmaceuticalStartTime(self, value: Optional[str]):
        if value is None:
            if "RadiopharmaceuticalStartTime" in self._dataset:
                del self._dataset.RadiopharmaceuticalStartTime
        else:
            self._dataset.RadiopharmaceuticalStartTime = value

    @property
    def RadiopharmaceuticalStopTime(self) -> Optional[str]:
        if "RadiopharmaceuticalStopTime" in self._dataset:
            return self._dataset.RadiopharmaceuticalStopTime
        return None

    @RadiopharmaceuticalStopTime.setter
    def RadiopharmaceuticalStopTime(self, value: Optional[str]):
        if value is None:
            if "RadiopharmaceuticalStopTime" in self._dataset:
                del self._dataset.RadiopharmaceuticalStopTime
        else:
            self._dataset.RadiopharmaceuticalStopTime = value

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
            raise ValueError(f"RadionuclideCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._RadionuclideCodeSequence = value
            if "RadionuclideCodeSequence" not in self._dataset:
                self._dataset.RadionuclideCodeSequence = pydicom.Sequence()
            self._dataset.RadionuclideCodeSequence.clear()
            self._dataset.RadionuclideCodeSequence.extend([item.to_dataset() for item in value])

    def add_RadionuclideCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError(f"Item must be an instance of CodeSequenceItem")
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
            raise ValueError(f"AdministrationRouteCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._AdministrationRouteCodeSequence = value
            if "AdministrationRouteCodeSequence" not in self._dataset:
                self._dataset.AdministrationRouteCodeSequence = pydicom.Sequence()
            self._dataset.AdministrationRouteCodeSequence.clear()
            self._dataset.AdministrationRouteCodeSequence.extend([item.to_dataset() for item in value])

    def add_AdministrationRouteCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError(f"Item must be an instance of CodeSequenceItem")
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
            raise ValueError(f"RadiopharmaceuticalCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._RadiopharmaceuticalCodeSequence = value
            if "RadiopharmaceuticalCodeSequence" not in self._dataset:
                self._dataset.RadiopharmaceuticalCodeSequence = pydicom.Sequence()
            self._dataset.RadiopharmaceuticalCodeSequence.clear()
            self._dataset.RadiopharmaceuticalCodeSequence.extend([item.to_dataset() for item in value])

    def add_RadiopharmaceuticalCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError(f"Item must be an instance of CodeSequenceItem")
        self._RadiopharmaceuticalCodeSequence.append(item)
        if "RadiopharmaceuticalCodeSequence" not in self._dataset:
            self._dataset.RadiopharmaceuticalCodeSequence = pydicom.Sequence()
        self._dataset.RadiopharmaceuticalCodeSequence.append(item.to_dataset())

    @property
    def CalibrationDataSequence(self) -> Optional[List[CalibrationDataSequenceItem]]:
        if "CalibrationDataSequence" in self._dataset:
            if len(self._CalibrationDataSequence) == len(self._dataset.CalibrationDataSequence):
                return self._CalibrationDataSequence
            else:
                return [CalibrationDataSequenceItem(x) for x in self._dataset.CalibrationDataSequence]
        return None

    @CalibrationDataSequence.setter
    def CalibrationDataSequence(self, value: Optional[List[CalibrationDataSequenceItem]]):
        if value is None:
            self._CalibrationDataSequence = []
            if "CalibrationDataSequence" in self._dataset:
                del self._dataset.CalibrationDataSequence
        elif not isinstance(value, list) or not all(isinstance(item, CalibrationDataSequenceItem) for item in value):
            raise ValueError(f"CalibrationDataSequence must be a list of CalibrationDataSequenceItem objects")
        else:
            self._CalibrationDataSequence = value
            if "CalibrationDataSequence" not in self._dataset:
                self._dataset.CalibrationDataSequence = pydicom.Sequence()
            self._dataset.CalibrationDataSequence.clear()
            self._dataset.CalibrationDataSequence.extend([item.to_dataset() for item in value])

    def add_CalibrationData(self, item: CalibrationDataSequenceItem):
        if not isinstance(item, CalibrationDataSequenceItem):
            raise ValueError(f"Item must be an instance of CalibrationDataSequenceItem")
        self._CalibrationDataSequence.append(item)
        if "CalibrationDataSequence" not in self._dataset:
            self._dataset.CalibrationDataSequence = pydicom.Sequence()
        self._dataset.CalibrationDataSequence.append(item.to_dataset())
