from decimal import Decimal
from typing import Any, List, Optional

import pydicom

from .code_sequence_item import CodeSequenceItem
from .ophthalmic_thickness_map_quality_threshold_sequence_item import (
    OphthalmicThicknessMapQualityThresholdSequenceItem,
)


class OphthalmicThicknessMapQualityRatingSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._OphthalmicThicknessMapQualityThresholdSequence: List[OphthalmicThicknessMapQualityThresholdSequenceItem] = []
        self._MeasurementUnitsCodeSequence: List[CodeSequenceItem] = []
        self._ConceptNameCodeSequence: List[CodeSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def OphthalmicThicknessMapQualityThresholdSequence(
        self,
    ) -> Optional[List[OphthalmicThicknessMapQualityThresholdSequenceItem]]:
        if "OphthalmicThicknessMapQualityThresholdSequence" in self._dataset:
            if len(self._OphthalmicThicknessMapQualityThresholdSequence) == len(
                self._dataset.OphthalmicThicknessMapQualityThresholdSequence
            ):
                return self._OphthalmicThicknessMapQualityThresholdSequence
            else:
                return [
                    OphthalmicThicknessMapQualityThresholdSequenceItem(x)
                    for x in self._dataset.OphthalmicThicknessMapQualityThresholdSequence
                ]
        return None

    @OphthalmicThicknessMapQualityThresholdSequence.setter
    def OphthalmicThicknessMapQualityThresholdSequence(
        self, value: Optional[List[OphthalmicThicknessMapQualityThresholdSequenceItem]]
    ):
        if value is None:
            self._OphthalmicThicknessMapQualityThresholdSequence = []
            if "OphthalmicThicknessMapQualityThresholdSequence" in self._dataset:
                del self._dataset.OphthalmicThicknessMapQualityThresholdSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, OphthalmicThicknessMapQualityThresholdSequenceItem) for item in value
        ):
            raise ValueError(
                f"OphthalmicThicknessMapQualityThresholdSequence must be a list of OphthalmicThicknessMapQualityThresholdSequenceItem objects"
            )
        else:
            self._OphthalmicThicknessMapQualityThresholdSequence = value
            if "OphthalmicThicknessMapQualityThresholdSequence" not in self._dataset:
                self._dataset.OphthalmicThicknessMapQualityThresholdSequence = pydicom.Sequence()
            self._dataset.OphthalmicThicknessMapQualityThresholdSequence.clear()
            self._dataset.OphthalmicThicknessMapQualityThresholdSequence.extend([item.to_dataset() for item in value])

    def add_OphthalmicThicknessMapQualityThreshold(self, item: OphthalmicThicknessMapQualityThresholdSequenceItem):
        if not isinstance(item, OphthalmicThicknessMapQualityThresholdSequenceItem):
            raise ValueError(f"Item must be an instance of OphthalmicThicknessMapQualityThresholdSequenceItem")
        self._OphthalmicThicknessMapQualityThresholdSequence.append(item)
        if "OphthalmicThicknessMapQualityThresholdSequence" not in self._dataset:
            self._dataset.OphthalmicThicknessMapQualityThresholdSequence = pydicom.Sequence()
        self._dataset.OphthalmicThicknessMapQualityThresholdSequence.append(item.to_dataset())

    @property
    def MeasurementUnitsCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "MeasurementUnitsCodeSequence" in self._dataset:
            if len(self._MeasurementUnitsCodeSequence) == len(self._dataset.MeasurementUnitsCodeSequence):
                return self._MeasurementUnitsCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.MeasurementUnitsCodeSequence]
        return None

    @MeasurementUnitsCodeSequence.setter
    def MeasurementUnitsCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._MeasurementUnitsCodeSequence = []
            if "MeasurementUnitsCodeSequence" in self._dataset:
                del self._dataset.MeasurementUnitsCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError(f"MeasurementUnitsCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._MeasurementUnitsCodeSequence = value
            if "MeasurementUnitsCodeSequence" not in self._dataset:
                self._dataset.MeasurementUnitsCodeSequence = pydicom.Sequence()
            self._dataset.MeasurementUnitsCodeSequence.clear()
            self._dataset.MeasurementUnitsCodeSequence.extend([item.to_dataset() for item in value])

    def add_MeasurementUnitsCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError(f"Item must be an instance of CodeSequenceItem")
        self._MeasurementUnitsCodeSequence.append(item)
        if "MeasurementUnitsCodeSequence" not in self._dataset:
            self._dataset.MeasurementUnitsCodeSequence = pydicom.Sequence()
        self._dataset.MeasurementUnitsCodeSequence.append(item.to_dataset())

    @property
    def ConceptNameCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "ConceptNameCodeSequence" in self._dataset:
            if len(self._ConceptNameCodeSequence) == len(self._dataset.ConceptNameCodeSequence):
                return self._ConceptNameCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.ConceptNameCodeSequence]
        return None

    @ConceptNameCodeSequence.setter
    def ConceptNameCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._ConceptNameCodeSequence = []
            if "ConceptNameCodeSequence" in self._dataset:
                del self._dataset.ConceptNameCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError(f"ConceptNameCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._ConceptNameCodeSequence = value
            if "ConceptNameCodeSequence" not in self._dataset:
                self._dataset.ConceptNameCodeSequence = pydicom.Sequence()
            self._dataset.ConceptNameCodeSequence.clear()
            self._dataset.ConceptNameCodeSequence.extend([item.to_dataset() for item in value])

    def add_ConceptNameCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError(f"Item must be an instance of CodeSequenceItem")
        self._ConceptNameCodeSequence.append(item)
        if "ConceptNameCodeSequence" not in self._dataset:
            self._dataset.ConceptNameCodeSequence = pydicom.Sequence()
        self._dataset.ConceptNameCodeSequence.append(item.to_dataset())

    @property
    def NumericValue(self) -> Optional[List[Decimal]]:
        if "NumericValue" in self._dataset:
            return self._dataset.NumericValue
        return None

    @NumericValue.setter
    def NumericValue(self, value: Optional[List[Decimal]]):
        if value is None:
            if "NumericValue" in self._dataset:
                del self._dataset.NumericValue
        else:
            self._dataset.NumericValue = value
