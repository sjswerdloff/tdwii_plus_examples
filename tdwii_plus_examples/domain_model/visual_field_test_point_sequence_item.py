from typing import Any, List, Optional

import pydicom

from .visual_field_test_point_normals_sequence_item import (
    VisualFieldTestPointNormalsSequenceItem,
)


class VisualFieldTestPointSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._VisualFieldTestPointNormalsSequence: List[VisualFieldTestPointNormalsSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def VisualFieldTestPointXCoordinate(self) -> Optional[float]:
        if "VisualFieldTestPointXCoordinate" in self._dataset:
            return self._dataset.VisualFieldTestPointXCoordinate
        return None

    @VisualFieldTestPointXCoordinate.setter
    def VisualFieldTestPointXCoordinate(self, value: Optional[float]):
        if value is None:
            if "VisualFieldTestPointXCoordinate" in self._dataset:
                del self._dataset.VisualFieldTestPointXCoordinate
        else:
            self._dataset.VisualFieldTestPointXCoordinate = value

    @property
    def VisualFieldTestPointYCoordinate(self) -> Optional[float]:
        if "VisualFieldTestPointYCoordinate" in self._dataset:
            return self._dataset.VisualFieldTestPointYCoordinate
        return None

    @VisualFieldTestPointYCoordinate.setter
    def VisualFieldTestPointYCoordinate(self, value: Optional[float]):
        if value is None:
            if "VisualFieldTestPointYCoordinate" in self._dataset:
                del self._dataset.VisualFieldTestPointYCoordinate
        else:
            self._dataset.VisualFieldTestPointYCoordinate = value

    @property
    def StimulusResults(self) -> Optional[str]:
        if "StimulusResults" in self._dataset:
            return self._dataset.StimulusResults
        return None

    @StimulusResults.setter
    def StimulusResults(self, value: Optional[str]):
        if value is None:
            if "StimulusResults" in self._dataset:
                del self._dataset.StimulusResults
        else:
            self._dataset.StimulusResults = value

    @property
    def SensitivityValue(self) -> Optional[float]:
        if "SensitivityValue" in self._dataset:
            return self._dataset.SensitivityValue
        return None

    @SensitivityValue.setter
    def SensitivityValue(self, value: Optional[float]):
        if value is None:
            if "SensitivityValue" in self._dataset:
                del self._dataset.SensitivityValue
        else:
            self._dataset.SensitivityValue = value

    @property
    def RetestStimulusSeen(self) -> Optional[str]:
        if "RetestStimulusSeen" in self._dataset:
            return self._dataset.RetestStimulusSeen
        return None

    @RetestStimulusSeen.setter
    def RetestStimulusSeen(self, value: Optional[str]):
        if value is None:
            if "RetestStimulusSeen" in self._dataset:
                del self._dataset.RetestStimulusSeen
        else:
            self._dataset.RetestStimulusSeen = value

    @property
    def RetestSensitivityValue(self) -> Optional[float]:
        if "RetestSensitivityValue" in self._dataset:
            return self._dataset.RetestSensitivityValue
        return None

    @RetestSensitivityValue.setter
    def RetestSensitivityValue(self, value: Optional[float]):
        if value is None:
            if "RetestSensitivityValue" in self._dataset:
                del self._dataset.RetestSensitivityValue
        else:
            self._dataset.RetestSensitivityValue = value

    @property
    def VisualFieldTestPointNormalsSequence(self) -> Optional[List[VisualFieldTestPointNormalsSequenceItem]]:
        if "VisualFieldTestPointNormalsSequence" in self._dataset:
            if len(self._VisualFieldTestPointNormalsSequence) == len(self._dataset.VisualFieldTestPointNormalsSequence):
                return self._VisualFieldTestPointNormalsSequence
            else:
                return [VisualFieldTestPointNormalsSequenceItem(x) for x in self._dataset.VisualFieldTestPointNormalsSequence]
        return None

    @VisualFieldTestPointNormalsSequence.setter
    def VisualFieldTestPointNormalsSequence(self, value: Optional[List[VisualFieldTestPointNormalsSequenceItem]]):
        if value is None:
            self._VisualFieldTestPointNormalsSequence = []
            if "VisualFieldTestPointNormalsSequence" in self._dataset:
                del self._dataset.VisualFieldTestPointNormalsSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, VisualFieldTestPointNormalsSequenceItem) for item in value
        ):
            raise ValueError(
                f"VisualFieldTestPointNormalsSequence must be a list of VisualFieldTestPointNormalsSequenceItem objects"
            )
        else:
            self._VisualFieldTestPointNormalsSequence = value
            if "VisualFieldTestPointNormalsSequence" not in self._dataset:
                self._dataset.VisualFieldTestPointNormalsSequence = pydicom.Sequence()
            self._dataset.VisualFieldTestPointNormalsSequence.clear()
            self._dataset.VisualFieldTestPointNormalsSequence.extend([item.to_dataset() for item in value])

    def add_VisualFieldTestPointNormals(self, item: VisualFieldTestPointNormalsSequenceItem):
        if not isinstance(item, VisualFieldTestPointNormalsSequenceItem):
            raise ValueError(f"Item must be an instance of VisualFieldTestPointNormalsSequenceItem")
        self._VisualFieldTestPointNormalsSequence.append(item)
        if "VisualFieldTestPointNormalsSequence" not in self._dataset:
            self._dataset.VisualFieldTestPointNormalsSequence = pydicom.Sequence()
        self._dataset.VisualFieldTestPointNormalsSequence.append(item.to_dataset())

    @property
    def QuantifiedDefect(self) -> Optional[float]:
        if "QuantifiedDefect" in self._dataset:
            return self._dataset.QuantifiedDefect
        return None

    @QuantifiedDefect.setter
    def QuantifiedDefect(self, value: Optional[float]):
        if value is None:
            if "QuantifiedDefect" in self._dataset:
                del self._dataset.QuantifiedDefect
        else:
            self._dataset.QuantifiedDefect = value
