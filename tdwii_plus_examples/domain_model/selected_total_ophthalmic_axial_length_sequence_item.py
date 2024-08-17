from typing import Any, List, Optional  # noqa

import pydicom

from .ophthalmic_axial_length_quality_metric_sequence_item import (
    OphthalmicAxialLengthQualityMetricSequenceItem,
)
from .referenced_ophthalmic_axial_length_measurement_qc_image_sequence_item import (
    ReferencedOphthalmicAxialLengthMeasurementQCImageSequenceItem,
)


class SelectedTotalOphthalmicAxialLengthSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._OphthalmicAxialLengthQualityMetricSequence: List[OphthalmicAxialLengthQualityMetricSequenceItem] = []
        self._ReferencedOphthalmicAxialLengthMeasurementQCImageSequence: List[
            ReferencedOphthalmicAxialLengthMeasurementQCImageSequenceItem
        ] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def OphthalmicAxialLength(self) -> Optional[float]:
        if "OphthalmicAxialLength" in self._dataset:
            return self._dataset.OphthalmicAxialLength
        return None

    @OphthalmicAxialLength.setter
    def OphthalmicAxialLength(self, value: Optional[float]):
        if value is None:
            if "OphthalmicAxialLength" in self._dataset:
                del self._dataset.OphthalmicAxialLength
        else:
            self._dataset.OphthalmicAxialLength = value

    @property
    def OphthalmicAxialLengthQualityMetricSequence(self) -> Optional[List[OphthalmicAxialLengthQualityMetricSequenceItem]]:
        if "OphthalmicAxialLengthQualityMetricSequence" in self._dataset:
            if len(self._OphthalmicAxialLengthQualityMetricSequence) == len(
                self._dataset.OphthalmicAxialLengthQualityMetricSequence
            ):
                return self._OphthalmicAxialLengthQualityMetricSequence
            else:
                return [
                    OphthalmicAxialLengthQualityMetricSequenceItem(x)
                    for x in self._dataset.OphthalmicAxialLengthQualityMetricSequence
                ]
        return None

    @OphthalmicAxialLengthQualityMetricSequence.setter
    def OphthalmicAxialLengthQualityMetricSequence(
        self, value: Optional[List[OphthalmicAxialLengthQualityMetricSequenceItem]]
    ):
        if value is None:
            self._OphthalmicAxialLengthQualityMetricSequence = []
            if "OphthalmicAxialLengthQualityMetricSequence" in self._dataset:
                del self._dataset.OphthalmicAxialLengthQualityMetricSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, OphthalmicAxialLengthQualityMetricSequenceItem) for item in value
        ):
            raise ValueError(
                "OphthalmicAxialLengthQualityMetricSequence must be a list of OphthalmicAxialLengthQualityMetricSequenceItem"
                " objects"
            )
        else:
            self._OphthalmicAxialLengthQualityMetricSequence = value
            if "OphthalmicAxialLengthQualityMetricSequence" not in self._dataset:
                self._dataset.OphthalmicAxialLengthQualityMetricSequence = pydicom.Sequence()
            self._dataset.OphthalmicAxialLengthQualityMetricSequence.clear()
            self._dataset.OphthalmicAxialLengthQualityMetricSequence.extend([item.to_dataset() for item in value])

    def add_OphthalmicAxialLengthQualityMetric(self, item: OphthalmicAxialLengthQualityMetricSequenceItem):
        if not isinstance(item, OphthalmicAxialLengthQualityMetricSequenceItem):
            raise ValueError("Item must be an instance of OphthalmicAxialLengthQualityMetricSequenceItem")
        self._OphthalmicAxialLengthQualityMetricSequence.append(item)
        if "OphthalmicAxialLengthQualityMetricSequence" not in self._dataset:
            self._dataset.OphthalmicAxialLengthQualityMetricSequence = pydicom.Sequence()
        self._dataset.OphthalmicAxialLengthQualityMetricSequence.append(item.to_dataset())

    @property
    def ReferencedOphthalmicAxialLengthMeasurementQCImageSequence(
        self,
    ) -> Optional[List[ReferencedOphthalmicAxialLengthMeasurementQCImageSequenceItem]]:
        if "ReferencedOphthalmicAxialLengthMeasurementQCImageSequence" in self._dataset:
            if len(self._ReferencedOphthalmicAxialLengthMeasurementQCImageSequence) == len(
                self._dataset.ReferencedOphthalmicAxialLengthMeasurementQCImageSequence
            ):
                return self._ReferencedOphthalmicAxialLengthMeasurementQCImageSequence
            else:
                return [
                    ReferencedOphthalmicAxialLengthMeasurementQCImageSequenceItem(x)
                    for x in self._dataset.ReferencedOphthalmicAxialLengthMeasurementQCImageSequence
                ]
        return None

    @ReferencedOphthalmicAxialLengthMeasurementQCImageSequence.setter
    def ReferencedOphthalmicAxialLengthMeasurementQCImageSequence(
        self, value: Optional[List[ReferencedOphthalmicAxialLengthMeasurementQCImageSequenceItem]]
    ):
        if value is None:
            self._ReferencedOphthalmicAxialLengthMeasurementQCImageSequence = []
            if "ReferencedOphthalmicAxialLengthMeasurementQCImageSequence" in self._dataset:
                del self._dataset.ReferencedOphthalmicAxialLengthMeasurementQCImageSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, ReferencedOphthalmicAxialLengthMeasurementQCImageSequenceItem) for item in value
        ):
            raise ValueError(
                "ReferencedOphthalmicAxialLengthMeasurementQCImageSequence must be a list of"
                " ReferencedOphthalmicAxialLengthMeasurementQCImageSequenceItem objects"
            )
        else:
            self._ReferencedOphthalmicAxialLengthMeasurementQCImageSequence = value
            if "ReferencedOphthalmicAxialLengthMeasurementQCImageSequence" not in self._dataset:
                self._dataset.ReferencedOphthalmicAxialLengthMeasurementQCImageSequence = pydicom.Sequence()
            self._dataset.ReferencedOphthalmicAxialLengthMeasurementQCImageSequence.clear()
            self._dataset.ReferencedOphthalmicAxialLengthMeasurementQCImageSequence.extend(
                [item.to_dataset() for item in value]
            )

    def add_ReferencedOphthalmicAxialLengthMeasurementQCImage(
        self, item: ReferencedOphthalmicAxialLengthMeasurementQCImageSequenceItem
    ):
        if not isinstance(item, ReferencedOphthalmicAxialLengthMeasurementQCImageSequenceItem):
            raise ValueError("Item must be an instance of ReferencedOphthalmicAxialLengthMeasurementQCImageSequenceItem")
        self._ReferencedOphthalmicAxialLengthMeasurementQCImageSequence.append(item)
        if "ReferencedOphthalmicAxialLengthMeasurementQCImageSequence" not in self._dataset:
            self._dataset.ReferencedOphthalmicAxialLengthMeasurementQCImageSequence = pydicom.Sequence()
        self._dataset.ReferencedOphthalmicAxialLengthMeasurementQCImageSequence.append(item.to_dataset())
