from decimal import Decimal
from typing import Any, List, Optional  # noqa

import pydicom

from .code_sequence_item import CodeSequenceItem
from .wide_field_ophthalmic_photography_quality_threshold_sequence_item import (
    WideFieldOphthalmicPhotographyQualityThresholdSequenceItem,
)


class WideFieldOphthalmicPhotographyQualityRatingSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._WideFieldOphthalmicPhotographyQualityThresholdSequence: List[
            WideFieldOphthalmicPhotographyQualityThresholdSequenceItem
        ] = []
        self._MeasurementUnitsCodeSequence: List[CodeSequenceItem] = []
        self._ConceptNameCodeSequence: List[CodeSequenceItem] = []
        self._AlgorithmFamilyCodeSequence: List[CodeSequenceItem] = []
        self._AlgorithmNameCodeSequence: List[CodeSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def WideFieldOphthalmicPhotographyQualityThresholdSequence(
        self,
    ) -> Optional[List[WideFieldOphthalmicPhotographyQualityThresholdSequenceItem]]:
        if "WideFieldOphthalmicPhotographyQualityThresholdSequence" in self._dataset:
            if len(self._WideFieldOphthalmicPhotographyQualityThresholdSequence) == len(
                self._dataset.WideFieldOphthalmicPhotographyQualityThresholdSequence
            ):
                return self._WideFieldOphthalmicPhotographyQualityThresholdSequence
            else:
                return [
                    WideFieldOphthalmicPhotographyQualityThresholdSequenceItem(x)
                    for x in self._dataset.WideFieldOphthalmicPhotographyQualityThresholdSequence
                ]
        return None

    @WideFieldOphthalmicPhotographyQualityThresholdSequence.setter
    def WideFieldOphthalmicPhotographyQualityThresholdSequence(
        self, value: Optional[List[WideFieldOphthalmicPhotographyQualityThresholdSequenceItem]]
    ):
        if value is None:
            self._WideFieldOphthalmicPhotographyQualityThresholdSequence = []
            if "WideFieldOphthalmicPhotographyQualityThresholdSequence" in self._dataset:
                del self._dataset.WideFieldOphthalmicPhotographyQualityThresholdSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, WideFieldOphthalmicPhotographyQualityThresholdSequenceItem) for item in value
        ):
            raise ValueError(
                "WideFieldOphthalmicPhotographyQualityThresholdSequence must be a list of"
                " WideFieldOphthalmicPhotographyQualityThresholdSequenceItem objects"
            )
        else:
            self._WideFieldOphthalmicPhotographyQualityThresholdSequence = value
            if "WideFieldOphthalmicPhotographyQualityThresholdSequence" not in self._dataset:
                self._dataset.WideFieldOphthalmicPhotographyQualityThresholdSequence = pydicom.Sequence()
            self._dataset.WideFieldOphthalmicPhotographyQualityThresholdSequence.clear()
            self._dataset.WideFieldOphthalmicPhotographyQualityThresholdSequence.extend([item.to_dataset() for item in value])

    def add_WideFieldOphthalmicPhotographyQualityThreshold(
        self, item: WideFieldOphthalmicPhotographyQualityThresholdSequenceItem
    ):
        if not isinstance(item, WideFieldOphthalmicPhotographyQualityThresholdSequenceItem):
            raise ValueError("Item must be an instance of WideFieldOphthalmicPhotographyQualityThresholdSequenceItem")
        self._WideFieldOphthalmicPhotographyQualityThresholdSequence.append(item)
        if "WideFieldOphthalmicPhotographyQualityThresholdSequence" not in self._dataset:
            self._dataset.WideFieldOphthalmicPhotographyQualityThresholdSequence = pydicom.Sequence()
        self._dataset.WideFieldOphthalmicPhotographyQualityThresholdSequence.append(item.to_dataset())

    @property
    def AlgorithmSource(self) -> Optional[str]:
        if "AlgorithmSource" in self._dataset:
            return self._dataset.AlgorithmSource
        return None

    @AlgorithmSource.setter
    def AlgorithmSource(self, value: Optional[str]):
        if value is None:
            if "AlgorithmSource" in self._dataset:
                del self._dataset.AlgorithmSource
        else:
            self._dataset.AlgorithmSource = value

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
            raise ValueError("MeasurementUnitsCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._MeasurementUnitsCodeSequence = value
            if "MeasurementUnitsCodeSequence" not in self._dataset:
                self._dataset.MeasurementUnitsCodeSequence = pydicom.Sequence()
            self._dataset.MeasurementUnitsCodeSequence.clear()
            self._dataset.MeasurementUnitsCodeSequence.extend([item.to_dataset() for item in value])

    def add_MeasurementUnitsCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
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
            raise ValueError("ConceptNameCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._ConceptNameCodeSequence = value
            if "ConceptNameCodeSequence" not in self._dataset:
                self._dataset.ConceptNameCodeSequence = pydicom.Sequence()
            self._dataset.ConceptNameCodeSequence.clear()
            self._dataset.ConceptNameCodeSequence.extend([item.to_dataset() for item in value])

    def add_ConceptNameCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
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

    @property
    def AlgorithmFamilyCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "AlgorithmFamilyCodeSequence" in self._dataset:
            if len(self._AlgorithmFamilyCodeSequence) == len(self._dataset.AlgorithmFamilyCodeSequence):
                return self._AlgorithmFamilyCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.AlgorithmFamilyCodeSequence]
        return None

    @AlgorithmFamilyCodeSequence.setter
    def AlgorithmFamilyCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._AlgorithmFamilyCodeSequence = []
            if "AlgorithmFamilyCodeSequence" in self._dataset:
                del self._dataset.AlgorithmFamilyCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("AlgorithmFamilyCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._AlgorithmFamilyCodeSequence = value
            if "AlgorithmFamilyCodeSequence" not in self._dataset:
                self._dataset.AlgorithmFamilyCodeSequence = pydicom.Sequence()
            self._dataset.AlgorithmFamilyCodeSequence.clear()
            self._dataset.AlgorithmFamilyCodeSequence.extend([item.to_dataset() for item in value])

    def add_AlgorithmFamilyCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._AlgorithmFamilyCodeSequence.append(item)
        if "AlgorithmFamilyCodeSequence" not in self._dataset:
            self._dataset.AlgorithmFamilyCodeSequence = pydicom.Sequence()
        self._dataset.AlgorithmFamilyCodeSequence.append(item.to_dataset())

    @property
    def AlgorithmNameCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "AlgorithmNameCodeSequence" in self._dataset:
            if len(self._AlgorithmNameCodeSequence) == len(self._dataset.AlgorithmNameCodeSequence):
                return self._AlgorithmNameCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.AlgorithmNameCodeSequence]
        return None

    @AlgorithmNameCodeSequence.setter
    def AlgorithmNameCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._AlgorithmNameCodeSequence = []
            if "AlgorithmNameCodeSequence" in self._dataset:
                del self._dataset.AlgorithmNameCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError("AlgorithmNameCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._AlgorithmNameCodeSequence = value
            if "AlgorithmNameCodeSequence" not in self._dataset:
                self._dataset.AlgorithmNameCodeSequence = pydicom.Sequence()
            self._dataset.AlgorithmNameCodeSequence.clear()
            self._dataset.AlgorithmNameCodeSequence.extend([item.to_dataset() for item in value])

    def add_AlgorithmNameCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._AlgorithmNameCodeSequence.append(item)
        if "AlgorithmNameCodeSequence" not in self._dataset:
            self._dataset.AlgorithmNameCodeSequence = pydicom.Sequence()
        self._dataset.AlgorithmNameCodeSequence.append(item.to_dataset())

    @property
    def AlgorithmVersion(self) -> Optional[str]:
        if "AlgorithmVersion" in self._dataset:
            return self._dataset.AlgorithmVersion
        return None

    @AlgorithmVersion.setter
    def AlgorithmVersion(self, value: Optional[str]):
        if value is None:
            if "AlgorithmVersion" in self._dataset:
                del self._dataset.AlgorithmVersion
        else:
            self._dataset.AlgorithmVersion = value

    @property
    def AlgorithmParameters(self) -> Optional[str]:
        if "AlgorithmParameters" in self._dataset:
            return self._dataset.AlgorithmParameters
        return None

    @AlgorithmParameters.setter
    def AlgorithmParameters(self, value: Optional[str]):
        if value is None:
            if "AlgorithmParameters" in self._dataset:
                del self._dataset.AlgorithmParameters
        else:
            self._dataset.AlgorithmParameters = value

    @property
    def AlgorithmName(self) -> Optional[str]:
        if "AlgorithmName" in self._dataset:
            return self._dataset.AlgorithmName
        return None

    @AlgorithmName.setter
    def AlgorithmName(self, value: Optional[str]):
        if value is None:
            if "AlgorithmName" in self._dataset:
                del self._dataset.AlgorithmName
        else:
            self._dataset.AlgorithmName = value
