from typing import Any, List, Optional  # noqa

import pydicom

from .code_sequence_item import CodeSequenceItem
from .flat_corneal_axis_sequence_item import FlatCornealAxisSequenceItem
from .referenced_sop_sequence_item import ReferencedSOPSequenceItem
from .steep_corneal_axis_sequence_item import SteepCornealAxisSequenceItem


class CorneaMeasurementsSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._ReferencedSOPSequence: List[ReferencedSOPSequenceItem] = []
        self._SourceOfCorneaMeasurementDataCodeSequence: List[CodeSequenceItem] = []
        self._SteepCornealAxisSequence: List[SteepCornealAxisSequenceItem] = []
        self._FlatCornealAxisSequence: List[FlatCornealAxisSequenceItem] = []
        self._CorneaMeasurementMethodCodeSequence: List[CodeSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ReferencedSOPSequence(self) -> Optional[List[ReferencedSOPSequenceItem]]:
        if "ReferencedSOPSequence" in self._dataset:
            if len(self._ReferencedSOPSequence) == len(self._dataset.ReferencedSOPSequence):
                return self._ReferencedSOPSequence
            else:
                return [ReferencedSOPSequenceItem(x) for x in self._dataset.ReferencedSOPSequence]
        return None

    @ReferencedSOPSequence.setter
    def ReferencedSOPSequence(self, value: Optional[List[ReferencedSOPSequenceItem]]):
        if value is None:
            self._ReferencedSOPSequence = []
            if "ReferencedSOPSequence" in self._dataset:
                del self._dataset.ReferencedSOPSequence
        elif not isinstance(value, list) or not all(isinstance(item, ReferencedSOPSequenceItem) for item in value):
            raise ValueError("ReferencedSOPSequence must be a list of ReferencedSOPSequenceItem objects")
        else:
            self._ReferencedSOPSequence = value
            if "ReferencedSOPSequence" not in self._dataset:
                self._dataset.ReferencedSOPSequence = pydicom.Sequence()
            self._dataset.ReferencedSOPSequence.clear()
            self._dataset.ReferencedSOPSequence.extend([item.to_dataset() for item in value])

    def add_ReferencedSOP(self, item: ReferencedSOPSequenceItem):
        if not isinstance(item, ReferencedSOPSequenceItem):
            raise ValueError("Item must be an instance of ReferencedSOPSequenceItem")
        self._ReferencedSOPSequence.append(item)
        if "ReferencedSOPSequence" not in self._dataset:
            self._dataset.ReferencedSOPSequence = pydicom.Sequence()
        self._dataset.ReferencedSOPSequence.append(item.to_dataset())

    @property
    def KeratometerIndex(self) -> Optional[float]:
        if "KeratometerIndex" in self._dataset:
            return self._dataset.KeratometerIndex
        return None

    @KeratometerIndex.setter
    def KeratometerIndex(self, value: Optional[float]):
        if value is None:
            if "KeratometerIndex" in self._dataset:
                del self._dataset.KeratometerIndex
        else:
            self._dataset.KeratometerIndex = value

    @property
    def SourceOfCorneaMeasurementDataCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "SourceOfCorneaMeasurementDataCodeSequence" in self._dataset:
            if len(self._SourceOfCorneaMeasurementDataCodeSequence) == len(
                self._dataset.SourceOfCorneaMeasurementDataCodeSequence
            ):
                return self._SourceOfCorneaMeasurementDataCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.SourceOfCorneaMeasurementDataCodeSequence]
        return None

    @SourceOfCorneaMeasurementDataCodeSequence.setter
    def SourceOfCorneaMeasurementDataCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._SourceOfCorneaMeasurementDataCodeSequence = []
            if "SourceOfCorneaMeasurementDataCodeSequence" in self._dataset:
                del self._dataset.SourceOfCorneaMeasurementDataCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("SourceOfCorneaMeasurementDataCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._SourceOfCorneaMeasurementDataCodeSequence = value
            if "SourceOfCorneaMeasurementDataCodeSequence" not in self._dataset:
                self._dataset.SourceOfCorneaMeasurementDataCodeSequence = pydicom.Sequence()
            self._dataset.SourceOfCorneaMeasurementDataCodeSequence.clear()
            self._dataset.SourceOfCorneaMeasurementDataCodeSequence.extend([item.to_dataset() for item in value])

    def add_SourceOfCorneaMeasurementDataCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._SourceOfCorneaMeasurementDataCodeSequence.append(item)
        if "SourceOfCorneaMeasurementDataCodeSequence" not in self._dataset:
            self._dataset.SourceOfCorneaMeasurementDataCodeSequence = pydicom.Sequence()
        self._dataset.SourceOfCorneaMeasurementDataCodeSequence.append(item.to_dataset())

    @property
    def SteepCornealAxisSequence(self) -> Optional[List[SteepCornealAxisSequenceItem]]:
        if "SteepCornealAxisSequence" in self._dataset:
            if len(self._SteepCornealAxisSequence) == len(self._dataset.SteepCornealAxisSequence):
                return self._SteepCornealAxisSequence
            else:
                return [SteepCornealAxisSequenceItem(x) for x in self._dataset.SteepCornealAxisSequence]
        return None

    @SteepCornealAxisSequence.setter
    def SteepCornealAxisSequence(self, value: Optional[List[SteepCornealAxisSequenceItem]]):
        if value is None:
            self._SteepCornealAxisSequence = []
            if "SteepCornealAxisSequence" in self._dataset:
                del self._dataset.SteepCornealAxisSequence
        elif not isinstance(value, list) or not all(isinstance(item, SteepCornealAxisSequenceItem) for item in value):
            raise ValueError("SteepCornealAxisSequence must be a list of SteepCornealAxisSequenceItem objects")
        else:
            self._SteepCornealAxisSequence = value
            if "SteepCornealAxisSequence" not in self._dataset:
                self._dataset.SteepCornealAxisSequence = pydicom.Sequence()
            self._dataset.SteepCornealAxisSequence.clear()
            self._dataset.SteepCornealAxisSequence.extend([item.to_dataset() for item in value])

    def add_SteepCornealAxis(self, item: SteepCornealAxisSequenceItem):
        if not isinstance(item, SteepCornealAxisSequenceItem):
            raise ValueError("Item must be an instance of SteepCornealAxisSequenceItem")
        self._SteepCornealAxisSequence.append(item)
        if "SteepCornealAxisSequence" not in self._dataset:
            self._dataset.SteepCornealAxisSequence = pydicom.Sequence()
        self._dataset.SteepCornealAxisSequence.append(item.to_dataset())

    @property
    def FlatCornealAxisSequence(self) -> Optional[List[FlatCornealAxisSequenceItem]]:
        if "FlatCornealAxisSequence" in self._dataset:
            if len(self._FlatCornealAxisSequence) == len(self._dataset.FlatCornealAxisSequence):
                return self._FlatCornealAxisSequence
            else:
                return [FlatCornealAxisSequenceItem(x) for x in self._dataset.FlatCornealAxisSequence]
        return None

    @FlatCornealAxisSequence.setter
    def FlatCornealAxisSequence(self, value: Optional[List[FlatCornealAxisSequenceItem]]):
        if value is None:
            self._FlatCornealAxisSequence = []
            if "FlatCornealAxisSequence" in self._dataset:
                del self._dataset.FlatCornealAxisSequence
        elif not isinstance(value, list) or not all(isinstance(item, FlatCornealAxisSequenceItem) for item in value):
            raise ValueError("FlatCornealAxisSequence must be a list of FlatCornealAxisSequenceItem objects")
        else:
            self._FlatCornealAxisSequence = value
            if "FlatCornealAxisSequence" not in self._dataset:
                self._dataset.FlatCornealAxisSequence = pydicom.Sequence()
            self._dataset.FlatCornealAxisSequence.clear()
            self._dataset.FlatCornealAxisSequence.extend([item.to_dataset() for item in value])

    def add_FlatCornealAxis(self, item: FlatCornealAxisSequenceItem):
        if not isinstance(item, FlatCornealAxisSequenceItem):
            raise ValueError("Item must be an instance of FlatCornealAxisSequenceItem")
        self._FlatCornealAxisSequence.append(item)
        if "FlatCornealAxisSequence" not in self._dataset:
            self._dataset.FlatCornealAxisSequence = pydicom.Sequence()
        self._dataset.FlatCornealAxisSequence.append(item.to_dataset())

    @property
    def CorneaMeasurementMethodCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "CorneaMeasurementMethodCodeSequence" in self._dataset:
            if len(self._CorneaMeasurementMethodCodeSequence) == len(self._dataset.CorneaMeasurementMethodCodeSequence):
                return self._CorneaMeasurementMethodCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.CorneaMeasurementMethodCodeSequence]
        return None

    @CorneaMeasurementMethodCodeSequence.setter
    def CorneaMeasurementMethodCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._CorneaMeasurementMethodCodeSequence = []
            if "CorneaMeasurementMethodCodeSequence" in self._dataset:
                del self._dataset.CorneaMeasurementMethodCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("CorneaMeasurementMethodCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._CorneaMeasurementMethodCodeSequence = value
            if "CorneaMeasurementMethodCodeSequence" not in self._dataset:
                self._dataset.CorneaMeasurementMethodCodeSequence = pydicom.Sequence()
            self._dataset.CorneaMeasurementMethodCodeSequence.clear()
            self._dataset.CorneaMeasurementMethodCodeSequence.extend([item.to_dataset() for item in value])

    def add_CorneaMeasurementMethodCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._CorneaMeasurementMethodCodeSequence.append(item)
        if "CorneaMeasurementMethodCodeSequence" not in self._dataset:
            self._dataset.CorneaMeasurementMethodCodeSequence = pydicom.Sequence()
        self._dataset.CorneaMeasurementMethodCodeSequence.append(item.to_dataset())

    @property
    def RefractiveIndexOfCornea(self) -> Optional[float]:
        if "RefractiveIndexOfCornea" in self._dataset:
            return self._dataset.RefractiveIndexOfCornea
        return None

    @RefractiveIndexOfCornea.setter
    def RefractiveIndexOfCornea(self, value: Optional[float]):
        if value is None:
            if "RefractiveIndexOfCornea" in self._dataset:
                del self._dataset.RefractiveIndexOfCornea
        else:
            self._dataset.RefractiveIndexOfCornea = value

    @property
    def RefractiveIndexOfAqueousHumor(self) -> Optional[float]:
        if "RefractiveIndexOfAqueousHumor" in self._dataset:
            return self._dataset.RefractiveIndexOfAqueousHumor
        return None

    @RefractiveIndexOfAqueousHumor.setter
    def RefractiveIndexOfAqueousHumor(self, value: Optional[float]):
        if value is None:
            if "RefractiveIndexOfAqueousHumor" in self._dataset:
                del self._dataset.RefractiveIndexOfAqueousHumor
        else:
            self._dataset.RefractiveIndexOfAqueousHumor = value
