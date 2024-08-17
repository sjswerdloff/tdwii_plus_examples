from typing import Any, List, Optional  # noqa

import pydicom

from .applicator_geometry_sequence_item import ApplicatorGeometrySequenceItem


class ApplicatorSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._ApplicatorGeometrySequence: List[ApplicatorGeometrySequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def AccessoryCode(self) -> Optional[str]:
        if "AccessoryCode" in self._dataset:
            return self._dataset.AccessoryCode
        return None

    @AccessoryCode.setter
    def AccessoryCode(self, value: Optional[str]):
        if value is None:
            if "AccessoryCode" in self._dataset:
                del self._dataset.AccessoryCode
        else:
            self._dataset.AccessoryCode = value

    @property
    def ApplicatorID(self) -> Optional[str]:
        if "ApplicatorID" in self._dataset:
            return self._dataset.ApplicatorID
        return None

    @ApplicatorID.setter
    def ApplicatorID(self, value: Optional[str]):
        if value is None:
            if "ApplicatorID" in self._dataset:
                del self._dataset.ApplicatorID
        else:
            self._dataset.ApplicatorID = value

    @property
    def ApplicatorType(self) -> Optional[str]:
        if "ApplicatorType" in self._dataset:
            return self._dataset.ApplicatorType
        return None

    @ApplicatorType.setter
    def ApplicatorType(self, value: Optional[str]):
        if value is None:
            if "ApplicatorType" in self._dataset:
                del self._dataset.ApplicatorType
        else:
            self._dataset.ApplicatorType = value

    @property
    def ApplicatorDescription(self) -> Optional[str]:
        if "ApplicatorDescription" in self._dataset:
            return self._dataset.ApplicatorDescription
        return None

    @ApplicatorDescription.setter
    def ApplicatorDescription(self, value: Optional[str]):
        if value is None:
            if "ApplicatorDescription" in self._dataset:
                del self._dataset.ApplicatorDescription
        else:
            self._dataset.ApplicatorDescription = value

    @property
    def ApplicatorGeometrySequence(self) -> Optional[List[ApplicatorGeometrySequenceItem]]:
        if "ApplicatorGeometrySequence" in self._dataset:
            if len(self._ApplicatorGeometrySequence) == len(self._dataset.ApplicatorGeometrySequence):
                return self._ApplicatorGeometrySequence
            else:
                return [ApplicatorGeometrySequenceItem(x) for x in self._dataset.ApplicatorGeometrySequence]
        return None

    @ApplicatorGeometrySequence.setter
    def ApplicatorGeometrySequence(self, value: Optional[List[ApplicatorGeometrySequenceItem]]):
        if value is None:
            self._ApplicatorGeometrySequence = []
            if "ApplicatorGeometrySequence" in self._dataset:
                del self._dataset.ApplicatorGeometrySequence
        elif not isinstance(value, list) or not all(isinstance(item, ApplicatorGeometrySequenceItem) for item in value):
            raise ValueError("ApplicatorGeometrySequence must be a list of ApplicatorGeometrySequenceItem objects")
        else:
            self._ApplicatorGeometrySequence = value
            if "ApplicatorGeometrySequence" not in self._dataset:
                self._dataset.ApplicatorGeometrySequence = pydicom.Sequence()
            self._dataset.ApplicatorGeometrySequence.clear()
            self._dataset.ApplicatorGeometrySequence.extend([item.to_dataset() for item in value])

    def add_ApplicatorGeometry(self, item: ApplicatorGeometrySequenceItem):
        if not isinstance(item, ApplicatorGeometrySequenceItem):
            raise ValueError("Item must be an instance of ApplicatorGeometrySequenceItem")
        self._ApplicatorGeometrySequence.append(item)
        if "ApplicatorGeometrySequence" not in self._dataset:
            self._dataset.ApplicatorGeometrySequence = pydicom.Sequence()
        self._dataset.ApplicatorGeometrySequence.append(item.to_dataset())

    @property
    def SourceToApplicatorMountingPositionDistance(self) -> Optional[float]:
        if "SourceToApplicatorMountingPositionDistance" in self._dataset:
            return self._dataset.SourceToApplicatorMountingPositionDistance
        return None

    @SourceToApplicatorMountingPositionDistance.setter
    def SourceToApplicatorMountingPositionDistance(self, value: Optional[float]):
        if value is None:
            if "SourceToApplicatorMountingPositionDistance" in self._dataset:
                del self._dataset.SourceToApplicatorMountingPositionDistance
        else:
            self._dataset.SourceToApplicatorMountingPositionDistance = value
