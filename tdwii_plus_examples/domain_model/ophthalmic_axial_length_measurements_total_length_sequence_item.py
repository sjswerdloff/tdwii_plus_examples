from typing import Any, List, Optional  # noqa

import pydicom

from .optical_ophthalmic_axial_length_measurements_sequence_item import (
    OpticalOphthalmicAxialLengthMeasurementsSequenceItem,
)
from .referenced_ophthalmic_axial_length_measurement_qc_image_sequence_item import (
    ReferencedOphthalmicAxialLengthMeasurementQCImageSequenceItem,
)
from .ultrasound_ophthalmic_axial_length_measurements_sequence_item import (
    UltrasoundOphthalmicAxialLengthMeasurementsSequenceItem,
)


class OphthalmicAxialLengthMeasurementsTotalLengthSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._UltrasoundOphthalmicAxialLengthMeasurementsSequence: List[
            UltrasoundOphthalmicAxialLengthMeasurementsSequenceItem
        ] = []
        self._OpticalOphthalmicAxialLengthMeasurementsSequence: List[OpticalOphthalmicAxialLengthMeasurementsSequenceItem] = []
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
    def UltrasoundOphthalmicAxialLengthMeasurementsSequence(
        self,
    ) -> Optional[List[UltrasoundOphthalmicAxialLengthMeasurementsSequenceItem]]:
        if "UltrasoundOphthalmicAxialLengthMeasurementsSequence" in self._dataset:
            if len(self._UltrasoundOphthalmicAxialLengthMeasurementsSequence) == len(
                self._dataset.UltrasoundOphthalmicAxialLengthMeasurementsSequence
            ):
                return self._UltrasoundOphthalmicAxialLengthMeasurementsSequence
            else:
                return [
                    UltrasoundOphthalmicAxialLengthMeasurementsSequenceItem(x)
                    for x in self._dataset.UltrasoundOphthalmicAxialLengthMeasurementsSequence
                ]
        return None

    @UltrasoundOphthalmicAxialLengthMeasurementsSequence.setter
    def UltrasoundOphthalmicAxialLengthMeasurementsSequence(
        self, value: Optional[List[UltrasoundOphthalmicAxialLengthMeasurementsSequenceItem]]
    ):
        if value is None:
            self._UltrasoundOphthalmicAxialLengthMeasurementsSequence = []
            if "UltrasoundOphthalmicAxialLengthMeasurementsSequence" in self._dataset:
                del self._dataset.UltrasoundOphthalmicAxialLengthMeasurementsSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, UltrasoundOphthalmicAxialLengthMeasurementsSequenceItem) for item in value
        ):
            raise ValueError(
                "UltrasoundOphthalmicAxialLengthMeasurementsSequence must be a list of"
                " UltrasoundOphthalmicAxialLengthMeasurementsSequenceItem objects"
            )
        else:
            self._UltrasoundOphthalmicAxialLengthMeasurementsSequence = value
            if "UltrasoundOphthalmicAxialLengthMeasurementsSequence" not in self._dataset:
                self._dataset.UltrasoundOphthalmicAxialLengthMeasurementsSequence = pydicom.Sequence()
            self._dataset.UltrasoundOphthalmicAxialLengthMeasurementsSequence.clear()
            self._dataset.UltrasoundOphthalmicAxialLengthMeasurementsSequence.extend([item.to_dataset() for item in value])

    def add_UltrasoundOphthalmicAxialLengthMeasurements(self, item: UltrasoundOphthalmicAxialLengthMeasurementsSequenceItem):
        if not isinstance(item, UltrasoundOphthalmicAxialLengthMeasurementsSequenceItem):
            raise ValueError("Item must be an instance of UltrasoundOphthalmicAxialLengthMeasurementsSequenceItem")
        self._UltrasoundOphthalmicAxialLengthMeasurementsSequence.append(item)
        if "UltrasoundOphthalmicAxialLengthMeasurementsSequence" not in self._dataset:
            self._dataset.UltrasoundOphthalmicAxialLengthMeasurementsSequence = pydicom.Sequence()
        self._dataset.UltrasoundOphthalmicAxialLengthMeasurementsSequence.append(item.to_dataset())

    @property
    def OpticalOphthalmicAxialLengthMeasurementsSequence(
        self,
    ) -> Optional[List[OpticalOphthalmicAxialLengthMeasurementsSequenceItem]]:
        if "OpticalOphthalmicAxialLengthMeasurementsSequence" in self._dataset:
            if len(self._OpticalOphthalmicAxialLengthMeasurementsSequence) == len(
                self._dataset.OpticalOphthalmicAxialLengthMeasurementsSequence
            ):
                return self._OpticalOphthalmicAxialLengthMeasurementsSequence
            else:
                return [
                    OpticalOphthalmicAxialLengthMeasurementsSequenceItem(x)
                    for x in self._dataset.OpticalOphthalmicAxialLengthMeasurementsSequence
                ]
        return None

    @OpticalOphthalmicAxialLengthMeasurementsSequence.setter
    def OpticalOphthalmicAxialLengthMeasurementsSequence(
        self, value: Optional[List[OpticalOphthalmicAxialLengthMeasurementsSequenceItem]]
    ):
        if value is None:
            self._OpticalOphthalmicAxialLengthMeasurementsSequence = []
            if "OpticalOphthalmicAxialLengthMeasurementsSequence" in self._dataset:
                del self._dataset.OpticalOphthalmicAxialLengthMeasurementsSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, OpticalOphthalmicAxialLengthMeasurementsSequenceItem) for item in value
        ):
            raise ValueError(
                "OpticalOphthalmicAxialLengthMeasurementsSequence must be a list of"
                " OpticalOphthalmicAxialLengthMeasurementsSequenceItem objects"
            )
        else:
            self._OpticalOphthalmicAxialLengthMeasurementsSequence = value
            if "OpticalOphthalmicAxialLengthMeasurementsSequence" not in self._dataset:
                self._dataset.OpticalOphthalmicAxialLengthMeasurementsSequence = pydicom.Sequence()
            self._dataset.OpticalOphthalmicAxialLengthMeasurementsSequence.clear()
            self._dataset.OpticalOphthalmicAxialLengthMeasurementsSequence.extend([item.to_dataset() for item in value])

    def add_OpticalOphthalmicAxialLengthMeasurements(self, item: OpticalOphthalmicAxialLengthMeasurementsSequenceItem):
        if not isinstance(item, OpticalOphthalmicAxialLengthMeasurementsSequenceItem):
            raise ValueError("Item must be an instance of OpticalOphthalmicAxialLengthMeasurementsSequenceItem")
        self._OpticalOphthalmicAxialLengthMeasurementsSequence.append(item)
        if "OpticalOphthalmicAxialLengthMeasurementsSequence" not in self._dataset:
            self._dataset.OpticalOphthalmicAxialLengthMeasurementsSequence = pydicom.Sequence()
        self._dataset.OpticalOphthalmicAxialLengthMeasurementsSequence.append(item.to_dataset())

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
