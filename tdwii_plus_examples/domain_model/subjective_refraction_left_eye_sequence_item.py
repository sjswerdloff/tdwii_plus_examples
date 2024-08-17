from typing import Any, List, Optional  # noqa

import pydicom

from .add_intermediate_sequence_item import AddIntermediateSequenceItem
from .add_near_sequence_item import AddNearSequenceItem
from .add_other_sequence_item import AddOtherSequenceItem
from .cylinder_sequence_item import CylinderSequenceItem
from .prism_sequence_item import PrismSequenceItem


class SubjectiveRefractionLeftEyeSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._CylinderSequence: List[CylinderSequenceItem] = []
        self._PrismSequence: List[PrismSequenceItem] = []
        self._AddNearSequence: List[AddNearSequenceItem] = []
        self._AddIntermediateSequence: List[AddIntermediateSequenceItem] = []
        self._AddOtherSequence: List[AddOtherSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def CylinderSequence(self) -> Optional[List[CylinderSequenceItem]]:
        if "CylinderSequence" in self._dataset:
            if len(self._CylinderSequence) == len(self._dataset.CylinderSequence):
                return self._CylinderSequence
            else:
                return [CylinderSequenceItem(x) for x in self._dataset.CylinderSequence]
        return None

    @CylinderSequence.setter
    def CylinderSequence(self, value: Optional[List[CylinderSequenceItem]]):
        if value is None:
            self._CylinderSequence = []
            if "CylinderSequence" in self._dataset:
                del self._dataset.CylinderSequence
        elif not isinstance(value, list) or not all(isinstance(item, CylinderSequenceItem) for item in value):
            raise ValueError("CylinderSequence must be a list of CylinderSequenceItem objects")
        else:
            self._CylinderSequence = value
            if "CylinderSequence" not in self._dataset:
                self._dataset.CylinderSequence = pydicom.Sequence()
            self._dataset.CylinderSequence.clear()
            self._dataset.CylinderSequence.extend([item.to_dataset() for item in value])

    def add_Cylinder(self, item: CylinderSequenceItem):
        if not isinstance(item, CylinderSequenceItem):
            raise ValueError("Item must be an instance of CylinderSequenceItem")
        self._CylinderSequence.append(item)
        if "CylinderSequence" not in self._dataset:
            self._dataset.CylinderSequence = pydicom.Sequence()
        self._dataset.CylinderSequence.append(item.to_dataset())

    @property
    def PrismSequence(self) -> Optional[List[PrismSequenceItem]]:
        if "PrismSequence" in self._dataset:
            if len(self._PrismSequence) == len(self._dataset.PrismSequence):
                return self._PrismSequence
            else:
                return [PrismSequenceItem(x) for x in self._dataset.PrismSequence]
        return None

    @PrismSequence.setter
    def PrismSequence(self, value: Optional[List[PrismSequenceItem]]):
        if value is None:
            self._PrismSequence = []
            if "PrismSequence" in self._dataset:
                del self._dataset.PrismSequence
        elif not isinstance(value, list) or not all(isinstance(item, PrismSequenceItem) for item in value):
            raise ValueError("PrismSequence must be a list of PrismSequenceItem objects")
        else:
            self._PrismSequence = value
            if "PrismSequence" not in self._dataset:
                self._dataset.PrismSequence = pydicom.Sequence()
            self._dataset.PrismSequence.clear()
            self._dataset.PrismSequence.extend([item.to_dataset() for item in value])

    def add_Prism(self, item: PrismSequenceItem):
        if not isinstance(item, PrismSequenceItem):
            raise ValueError("Item must be an instance of PrismSequenceItem")
        self._PrismSequence.append(item)
        if "PrismSequence" not in self._dataset:
            self._dataset.PrismSequence = pydicom.Sequence()
        self._dataset.PrismSequence.append(item.to_dataset())

    @property
    def AddNearSequence(self) -> Optional[List[AddNearSequenceItem]]:
        if "AddNearSequence" in self._dataset:
            if len(self._AddNearSequence) == len(self._dataset.AddNearSequence):
                return self._AddNearSequence
            else:
                return [AddNearSequenceItem(x) for x in self._dataset.AddNearSequence]
        return None

    @AddNearSequence.setter
    def AddNearSequence(self, value: Optional[List[AddNearSequenceItem]]):
        if value is None:
            self._AddNearSequence = []
            if "AddNearSequence" in self._dataset:
                del self._dataset.AddNearSequence
        elif not isinstance(value, list) or not all(isinstance(item, AddNearSequenceItem) for item in value):
            raise ValueError("AddNearSequence must be a list of AddNearSequenceItem objects")
        else:
            self._AddNearSequence = value
            if "AddNearSequence" not in self._dataset:
                self._dataset.AddNearSequence = pydicom.Sequence()
            self._dataset.AddNearSequence.clear()
            self._dataset.AddNearSequence.extend([item.to_dataset() for item in value])

    def add_AddNear(self, item: AddNearSequenceItem):
        if not isinstance(item, AddNearSequenceItem):
            raise ValueError("Item must be an instance of AddNearSequenceItem")
        self._AddNearSequence.append(item)
        if "AddNearSequence" not in self._dataset:
            self._dataset.AddNearSequence = pydicom.Sequence()
        self._dataset.AddNearSequence.append(item.to_dataset())

    @property
    def AddIntermediateSequence(self) -> Optional[List[AddIntermediateSequenceItem]]:
        if "AddIntermediateSequence" in self._dataset:
            if len(self._AddIntermediateSequence) == len(self._dataset.AddIntermediateSequence):
                return self._AddIntermediateSequence
            else:
                return [AddIntermediateSequenceItem(x) for x in self._dataset.AddIntermediateSequence]
        return None

    @AddIntermediateSequence.setter
    def AddIntermediateSequence(self, value: Optional[List[AddIntermediateSequenceItem]]):
        if value is None:
            self._AddIntermediateSequence = []
            if "AddIntermediateSequence" in self._dataset:
                del self._dataset.AddIntermediateSequence
        elif not isinstance(value, list) or not all(isinstance(item, AddIntermediateSequenceItem) for item in value):
            raise ValueError("AddIntermediateSequence must be a list of AddIntermediateSequenceItem objects")
        else:
            self._AddIntermediateSequence = value
            if "AddIntermediateSequence" not in self._dataset:
                self._dataset.AddIntermediateSequence = pydicom.Sequence()
            self._dataset.AddIntermediateSequence.clear()
            self._dataset.AddIntermediateSequence.extend([item.to_dataset() for item in value])

    def add_AddIntermediate(self, item: AddIntermediateSequenceItem):
        if not isinstance(item, AddIntermediateSequenceItem):
            raise ValueError("Item must be an instance of AddIntermediateSequenceItem")
        self._AddIntermediateSequence.append(item)
        if "AddIntermediateSequence" not in self._dataset:
            self._dataset.AddIntermediateSequence = pydicom.Sequence()
        self._dataset.AddIntermediateSequence.append(item.to_dataset())

    @property
    def AddOtherSequence(self) -> Optional[List[AddOtherSequenceItem]]:
        if "AddOtherSequence" in self._dataset:
            if len(self._AddOtherSequence) == len(self._dataset.AddOtherSequence):
                return self._AddOtherSequence
            else:
                return [AddOtherSequenceItem(x) for x in self._dataset.AddOtherSequence]
        return None

    @AddOtherSequence.setter
    def AddOtherSequence(self, value: Optional[List[AddOtherSequenceItem]]):
        if value is None:
            self._AddOtherSequence = []
            if "AddOtherSequence" in self._dataset:
                del self._dataset.AddOtherSequence
        elif not isinstance(value, list) or not all(isinstance(item, AddOtherSequenceItem) for item in value):
            raise ValueError("AddOtherSequence must be a list of AddOtherSequenceItem objects")
        else:
            self._AddOtherSequence = value
            if "AddOtherSequence" not in self._dataset:
                self._dataset.AddOtherSequence = pydicom.Sequence()
            self._dataset.AddOtherSequence.clear()
            self._dataset.AddOtherSequence.extend([item.to_dataset() for item in value])

    def add_AddOther(self, item: AddOtherSequenceItem):
        if not isinstance(item, AddOtherSequenceItem):
            raise ValueError("Item must be an instance of AddOtherSequenceItem")
        self._AddOtherSequence.append(item)
        if "AddOtherSequence" not in self._dataset:
            self._dataset.AddOtherSequence = pydicom.Sequence()
        self._dataset.AddOtherSequence.append(item.to_dataset())

    @property
    def SpherePower(self) -> Optional[float]:
        if "SpherePower" in self._dataset:
            return self._dataset.SpherePower
        return None

    @SpherePower.setter
    def SpherePower(self, value: Optional[float]):
        if value is None:
            if "SpherePower" in self._dataset:
                del self._dataset.SpherePower
        else:
            self._dataset.SpherePower = value
