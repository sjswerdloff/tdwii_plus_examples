from typing import Any, List, Optional  # noqa

import pydicom

from .cylinder_sequence_item import CylinderSequenceItem


class AutorefractionRightEyeSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._CylinderSequence: List[CylinderSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def VertexDistance(self) -> Optional[float]:
        if "VertexDistance" in self._dataset:
            return self._dataset.VertexDistance
        return None

    @VertexDistance.setter
    def VertexDistance(self, value: Optional[float]):
        if value is None:
            if "VertexDistance" in self._dataset:
                del self._dataset.VertexDistance
        else:
            self._dataset.VertexDistance = value

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
    def PupilSize(self) -> Optional[float]:
        if "PupilSize" in self._dataset:
            return self._dataset.PupilSize
        return None

    @PupilSize.setter
    def PupilSize(self, value: Optional[float]):
        if value is None:
            if "PupilSize" in self._dataset:
                del self._dataset.PupilSize
        else:
            self._dataset.PupilSize = value

    @property
    def CornealSize(self) -> Optional[float]:
        if "CornealSize" in self._dataset:
            return self._dataset.CornealSize
        return None

    @CornealSize.setter
    def CornealSize(self, value: Optional[float]):
        if value is None:
            if "CornealSize" in self._dataset:
                del self._dataset.CornealSize
        else:
            self._dataset.CornealSize = value

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
