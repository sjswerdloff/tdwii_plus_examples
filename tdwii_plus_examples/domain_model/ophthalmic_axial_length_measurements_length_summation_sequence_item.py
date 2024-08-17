from typing import Any, List, Optional

import pydicom

from .ophthalmic_axial_length_measurements_segmental_length_sequence_item import (
    OphthalmicAxialLengthMeasurementsSegmentalLengthSequenceItem,
)
from .referenced_ophthalmic_axial_length_measurement_qc_image_sequence_item import (
    ReferencedOphthalmicAxialLengthMeasurementQCImageSequenceItem,
)


class OphthalmicAxialLengthMeasurementsLengthSummationSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._OphthalmicAxialLengthMeasurementsSegmentalLengthSequence: List[
            OphthalmicAxialLengthMeasurementsSegmentalLengthSequenceItem
        ] = []
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
    def OphthalmicAxialLengthMeasurementModified(self) -> Optional[str]:
        if "OphthalmicAxialLengthMeasurementModified" in self._dataset:
            return self._dataset.OphthalmicAxialLengthMeasurementModified
        return None

    @OphthalmicAxialLengthMeasurementModified.setter
    def OphthalmicAxialLengthMeasurementModified(self, value: Optional[str]):
        if value is None:
            if "OphthalmicAxialLengthMeasurementModified" in self._dataset:
                del self._dataset.OphthalmicAxialLengthMeasurementModified
        else:
            self._dataset.OphthalmicAxialLengthMeasurementModified = value

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
                f"OphthalmicAxialLengthMeasurementsSegmentalLengthSequence must be a list of OphthalmicAxialLengthMeasurementsSegmentalLengthSequenceItem objects"
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
            raise ValueError(f"Item must be an instance of OphthalmicAxialLengthMeasurementsSegmentalLengthSequenceItem")
        self._OphthalmicAxialLengthMeasurementsSegmentalLengthSequence.append(item)
        if "OphthalmicAxialLengthMeasurementsSegmentalLengthSequence" not in self._dataset:
            self._dataset.OphthalmicAxialLengthMeasurementsSegmentalLengthSequence = pydicom.Sequence()
        self._dataset.OphthalmicAxialLengthMeasurementsSegmentalLengthSequence.append(item.to_dataset())

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
                f"ReferencedOphthalmicAxialLengthMeasurementQCImageSequence must be a list of ReferencedOphthalmicAxialLengthMeasurementQCImageSequenceItem objects"
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
            raise ValueError(f"Item must be an instance of ReferencedOphthalmicAxialLengthMeasurementQCImageSequenceItem")
        self._ReferencedOphthalmicAxialLengthMeasurementQCImageSequence.append(item)
        if "ReferencedOphthalmicAxialLengthMeasurementQCImageSequence" not in self._dataset:
            self._dataset.ReferencedOphthalmicAxialLengthMeasurementQCImageSequence = pydicom.Sequence()
        self._dataset.ReferencedOphthalmicAxialLengthMeasurementQCImageSequence.append(item.to_dataset())
