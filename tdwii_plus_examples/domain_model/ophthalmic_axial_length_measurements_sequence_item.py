from typing import Any, List, Optional  # noqa

import pydicom

from .ophthalmic_axial_length_measurements_length_summation_sequence_item import (
    OphthalmicAxialLengthMeasurementsLengthSummationSequenceItem,
)
from .ophthalmic_axial_length_measurements_segmental_length_sequence_item import (
    OphthalmicAxialLengthMeasurementsSegmentalLengthSequenceItem,
)
from .ophthalmic_axial_length_measurements_total_length_sequence_item import (
    OphthalmicAxialLengthMeasurementsTotalLengthSequenceItem,
)


class OphthalmicAxialLengthMeasurementsSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._OphthalmicAxialLengthMeasurementsTotalLengthSequence: List[
            OphthalmicAxialLengthMeasurementsTotalLengthSequenceItem
        ] = []
        self._OphthalmicAxialLengthMeasurementsSegmentalLengthSequence: List[
            OphthalmicAxialLengthMeasurementsSegmentalLengthSequenceItem
        ] = []
        self._OphthalmicAxialLengthMeasurementsLengthSummationSequence: List[
            OphthalmicAxialLengthMeasurementsLengthSummationSequenceItem
        ] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def OphthalmicAxialLengthMeasurementsType(self) -> Optional[str]:
        if "OphthalmicAxialLengthMeasurementsType" in self._dataset:
            return self._dataset.OphthalmicAxialLengthMeasurementsType
        return None

    @OphthalmicAxialLengthMeasurementsType.setter
    def OphthalmicAxialLengthMeasurementsType(self, value: Optional[str]):
        if value is None:
            if "OphthalmicAxialLengthMeasurementsType" in self._dataset:
                del self._dataset.OphthalmicAxialLengthMeasurementsType
        else:
            self._dataset.OphthalmicAxialLengthMeasurementsType = value

    @property
    def OphthalmicAxialLengthMeasurementsTotalLengthSequence(
        self,
    ) -> Optional[List[OphthalmicAxialLengthMeasurementsTotalLengthSequenceItem]]:
        if "OphthalmicAxialLengthMeasurementsTotalLengthSequence" in self._dataset:
            if len(self._OphthalmicAxialLengthMeasurementsTotalLengthSequence) == len(
                self._dataset.OphthalmicAxialLengthMeasurementsTotalLengthSequence
            ):
                return self._OphthalmicAxialLengthMeasurementsTotalLengthSequence
            else:
                return [
                    OphthalmicAxialLengthMeasurementsTotalLengthSequenceItem(x)
                    for x in self._dataset.OphthalmicAxialLengthMeasurementsTotalLengthSequence
                ]
        return None

    @OphthalmicAxialLengthMeasurementsTotalLengthSequence.setter
    def OphthalmicAxialLengthMeasurementsTotalLengthSequence(
        self, value: Optional[List[OphthalmicAxialLengthMeasurementsTotalLengthSequenceItem]]
    ):
        if value is None:
            self._OphthalmicAxialLengthMeasurementsTotalLengthSequence = []
            if "OphthalmicAxialLengthMeasurementsTotalLengthSequence" in self._dataset:
                del self._dataset.OphthalmicAxialLengthMeasurementsTotalLengthSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, OphthalmicAxialLengthMeasurementsTotalLengthSequenceItem) for item in value
        ):
            raise ValueError(
                "OphthalmicAxialLengthMeasurementsTotalLengthSequence must be a list of"
                " OphthalmicAxialLengthMeasurementsTotalLengthSequenceItem objects"
            )
        else:
            self._OphthalmicAxialLengthMeasurementsTotalLengthSequence = value
            if "OphthalmicAxialLengthMeasurementsTotalLengthSequence" not in self._dataset:
                self._dataset.OphthalmicAxialLengthMeasurementsTotalLengthSequence = pydicom.Sequence()
            self._dataset.OphthalmicAxialLengthMeasurementsTotalLengthSequence.clear()
            self._dataset.OphthalmicAxialLengthMeasurementsTotalLengthSequence.extend([item.to_dataset() for item in value])

    def add_OphthalmicAxialLengthMeasurementsTotalLength(self, item: OphthalmicAxialLengthMeasurementsTotalLengthSequenceItem):
        if not isinstance(item, OphthalmicAxialLengthMeasurementsTotalLengthSequenceItem):
            raise ValueError("Item must be an instance of OphthalmicAxialLengthMeasurementsTotalLengthSequenceItem")
        self._OphthalmicAxialLengthMeasurementsTotalLengthSequence.append(item)
        if "OphthalmicAxialLengthMeasurementsTotalLengthSequence" not in self._dataset:
            self._dataset.OphthalmicAxialLengthMeasurementsTotalLengthSequence = pydicom.Sequence()
        self._dataset.OphthalmicAxialLengthMeasurementsTotalLengthSequence.append(item.to_dataset())

    @property
    def OphthalmicAxialLengthMeasurementsSegmentalLengthSequence(
        self,
    ) -> Optional[List[OphthalmicAxialLengthMeasurementsSegmentalLengthSequenceItem]]:
        if "OphthalmicAxialLengthMeasurementsSegmentalLengthSequence" in self._dataset:
            if len(self._OphthalmicAxialLengthMeasurementsSegmentalLengthSequence) == len(
                self._dataset.OphthalmicAxialLengthMeasurementsSegmentalLengthSequence
            ):
                return self._OphthalmicAxialLengthMeasurementsSegmentalLengthSequence
            else:
                return [
                    OphthalmicAxialLengthMeasurementsSegmentalLengthSequenceItem(x)
                    for x in self._dataset.OphthalmicAxialLengthMeasurementsSegmentalLengthSequence
                ]
        return None

    @OphthalmicAxialLengthMeasurementsSegmentalLengthSequence.setter
    def OphthalmicAxialLengthMeasurementsSegmentalLengthSequence(
        self, value: Optional[List[OphthalmicAxialLengthMeasurementsSegmentalLengthSequenceItem]]
    ):
        if value is None:
            self._OphthalmicAxialLengthMeasurementsSegmentalLengthSequence = []
            if "OphthalmicAxialLengthMeasurementsSegmentalLengthSequence" in self._dataset:
                del self._dataset.OphthalmicAxialLengthMeasurementsSegmentalLengthSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, OphthalmicAxialLengthMeasurementsSegmentalLengthSequenceItem) for item in value
        ):
            raise ValueError(
                "OphthalmicAxialLengthMeasurementsSegmentalLengthSequence must be a list of"
                " OphthalmicAxialLengthMeasurementsSegmentalLengthSequenceItem objects"
            )
        else:
            self._OphthalmicAxialLengthMeasurementsSegmentalLengthSequence = value
            if "OphthalmicAxialLengthMeasurementsSegmentalLengthSequence" not in self._dataset:
                self._dataset.OphthalmicAxialLengthMeasurementsSegmentalLengthSequence = pydicom.Sequence()
            self._dataset.OphthalmicAxialLengthMeasurementsSegmentalLengthSequence.clear()
            self._dataset.OphthalmicAxialLengthMeasurementsSegmentalLengthSequence.extend(
                [item.to_dataset() for item in value]
            )

    def add_OphthalmicAxialLengthMeasurementsSegmentalLength(
        self, item: OphthalmicAxialLengthMeasurementsSegmentalLengthSequenceItem
    ):
        if not isinstance(item, OphthalmicAxialLengthMeasurementsSegmentalLengthSequenceItem):
            raise ValueError("Item must be an instance of OphthalmicAxialLengthMeasurementsSegmentalLengthSequenceItem")
        self._OphthalmicAxialLengthMeasurementsSegmentalLengthSequence.append(item)
        if "OphthalmicAxialLengthMeasurementsSegmentalLengthSequence" not in self._dataset:
            self._dataset.OphthalmicAxialLengthMeasurementsSegmentalLengthSequence = pydicom.Sequence()
        self._dataset.OphthalmicAxialLengthMeasurementsSegmentalLengthSequence.append(item.to_dataset())

    @property
    def OphthalmicAxialLengthMeasurementsLengthSummationSequence(
        self,
    ) -> Optional[List[OphthalmicAxialLengthMeasurementsLengthSummationSequenceItem]]:
        if "OphthalmicAxialLengthMeasurementsLengthSummationSequence" in self._dataset:
            if len(self._OphthalmicAxialLengthMeasurementsLengthSummationSequence) == len(
                self._dataset.OphthalmicAxialLengthMeasurementsLengthSummationSequence
            ):
                return self._OphthalmicAxialLengthMeasurementsLengthSummationSequence
            else:
                return [
                    OphthalmicAxialLengthMeasurementsLengthSummationSequenceItem(x)
                    for x in self._dataset.OphthalmicAxialLengthMeasurementsLengthSummationSequence
                ]
        return None

    @OphthalmicAxialLengthMeasurementsLengthSummationSequence.setter
    def OphthalmicAxialLengthMeasurementsLengthSummationSequence(
        self, value: Optional[List[OphthalmicAxialLengthMeasurementsLengthSummationSequenceItem]]
    ):
        if value is None:
            self._OphthalmicAxialLengthMeasurementsLengthSummationSequence = []
            if "OphthalmicAxialLengthMeasurementsLengthSummationSequence" in self._dataset:
                del self._dataset.OphthalmicAxialLengthMeasurementsLengthSummationSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, OphthalmicAxialLengthMeasurementsLengthSummationSequenceItem) for item in value
        ):
            raise ValueError(
                "OphthalmicAxialLengthMeasurementsLengthSummationSequence must be a list of"
                " OphthalmicAxialLengthMeasurementsLengthSummationSequenceItem objects"
            )
        else:
            self._OphthalmicAxialLengthMeasurementsLengthSummationSequence = value
            if "OphthalmicAxialLengthMeasurementsLengthSummationSequence" not in self._dataset:
                self._dataset.OphthalmicAxialLengthMeasurementsLengthSummationSequence = pydicom.Sequence()
            self._dataset.OphthalmicAxialLengthMeasurementsLengthSummationSequence.clear()
            self._dataset.OphthalmicAxialLengthMeasurementsLengthSummationSequence.extend(
                [item.to_dataset() for item in value]
            )

    def add_OphthalmicAxialLengthMeasurementsLengthSummation(
        self, item: OphthalmicAxialLengthMeasurementsLengthSummationSequenceItem
    ):
        if not isinstance(item, OphthalmicAxialLengthMeasurementsLengthSummationSequenceItem):
            raise ValueError("Item must be an instance of OphthalmicAxialLengthMeasurementsLengthSummationSequenceItem")
        self._OphthalmicAxialLengthMeasurementsLengthSummationSequence.append(item)
        if "OphthalmicAxialLengthMeasurementsLengthSummationSequence" not in self._dataset:
            self._dataset.OphthalmicAxialLengthMeasurementsLengthSummationSequence = pydicom.Sequence()
        self._dataset.OphthalmicAxialLengthMeasurementsLengthSummationSequence.append(item.to_dataset())
