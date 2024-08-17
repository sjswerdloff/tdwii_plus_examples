from typing import Any, List, Optional  # noqa

import pydicom

from .code_sequence_item import CodeSequenceItem
from .optical_ophthalmic_axial_length_measurements_sequence_item import (
    OpticalOphthalmicAxialLengthMeasurementsSequenceItem,
)
from .ultrasound_ophthalmic_axial_length_measurements_sequence_item import (
    UltrasoundOphthalmicAxialLengthMeasurementsSequenceItem,
)


class OphthalmicAxialLengthMeasurementsSegmentalLengthSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._OphthalmicAxialLengthMeasurementsSegmentNameCodeSequence: List[CodeSequenceItem] = []
        self._UltrasoundOphthalmicAxialLengthMeasurementsSequence: List[
            UltrasoundOphthalmicAxialLengthMeasurementsSequenceItem
        ] = []
        self._OpticalOphthalmicAxialLengthMeasurementsSequence: List[OpticalOphthalmicAxialLengthMeasurementsSequenceItem] = []

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
    def OphthalmicAxialLengthMeasurementsSegmentNameCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "OphthalmicAxialLengthMeasurementsSegmentNameCodeSequence" in self._dataset:
            if len(self._OphthalmicAxialLengthMeasurementsSegmentNameCodeSequence) == len(
                self._dataset.OphthalmicAxialLengthMeasurementsSegmentNameCodeSequence
            ):
                return self._OphthalmicAxialLengthMeasurementsSegmentNameCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.OphthalmicAxialLengthMeasurementsSegmentNameCodeSequence]
        return None

    @OphthalmicAxialLengthMeasurementsSegmentNameCodeSequence.setter
    def OphthalmicAxialLengthMeasurementsSegmentNameCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._OphthalmicAxialLengthMeasurementsSegmentNameCodeSequence = []
            if "OphthalmicAxialLengthMeasurementsSegmentNameCodeSequence" in self._dataset:
                del self._dataset.OphthalmicAxialLengthMeasurementsSegmentNameCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError(
                "OphthalmicAxialLengthMeasurementsSegmentNameCodeSequence must be a list of CodeSequenceItem objects"
            )
        else:
            self._OphthalmicAxialLengthMeasurementsSegmentNameCodeSequence = value
            if "OphthalmicAxialLengthMeasurementsSegmentNameCodeSequence" not in self._dataset:
                self._dataset.OphthalmicAxialLengthMeasurementsSegmentNameCodeSequence = pydicom.Sequence()
            self._dataset.OphthalmicAxialLengthMeasurementsSegmentNameCodeSequence.clear()
            self._dataset.OphthalmicAxialLengthMeasurementsSegmentNameCodeSequence.extend(
                [item.to_dataset() for item in value]
            )

    def add_OphthalmicAxialLengthMeasurementsSegmentNameCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError("Item must be an instance of CodeSequenceItem")
        self._OphthalmicAxialLengthMeasurementsSegmentNameCodeSequence.append(item)
        if "OphthalmicAxialLengthMeasurementsSegmentNameCodeSequence" not in self._dataset:
            self._dataset.OphthalmicAxialLengthMeasurementsSegmentNameCodeSequence = pydicom.Sequence()
        self._dataset.OphthalmicAxialLengthMeasurementsSegmentNameCodeSequence.append(item.to_dataset())

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
