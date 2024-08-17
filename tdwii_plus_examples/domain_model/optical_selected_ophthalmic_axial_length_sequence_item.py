from typing import Any, List, Optional  # noqa

import pydicom

from .selected_segmental_ophthalmic_axial_length_sequence_item import (
    SelectedSegmentalOphthalmicAxialLengthSequenceItem,
)
from .selected_total_ophthalmic_axial_length_sequence_item import (
    SelectedTotalOphthalmicAxialLengthSequenceItem,
)


class OpticalSelectedOphthalmicAxialLengthSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._SelectedSegmentalOphthalmicAxialLengthSequence: List[SelectedSegmentalOphthalmicAxialLengthSequenceItem] = []
        self._SelectedTotalOphthalmicAxialLengthSequence: List[SelectedTotalOphthalmicAxialLengthSequenceItem] = []

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
    def SelectedSegmentalOphthalmicAxialLengthSequence(
        self,
    ) -> Optional[List[SelectedSegmentalOphthalmicAxialLengthSequenceItem]]:
        if "SelectedSegmentalOphthalmicAxialLengthSequence" in self._dataset:
            if len(self._SelectedSegmentalOphthalmicAxialLengthSequence) == len(
                self._dataset.SelectedSegmentalOphthalmicAxialLengthSequence
            ):
                return self._SelectedSegmentalOphthalmicAxialLengthSequence
            else:
                return [
                    SelectedSegmentalOphthalmicAxialLengthSequenceItem(x)
                    for x in self._dataset.SelectedSegmentalOphthalmicAxialLengthSequence
                ]
        return None

    @SelectedSegmentalOphthalmicAxialLengthSequence.setter
    def SelectedSegmentalOphthalmicAxialLengthSequence(
        self, value: Optional[List[SelectedSegmentalOphthalmicAxialLengthSequenceItem]]
    ):
        if value is None:
            self._SelectedSegmentalOphthalmicAxialLengthSequence = []
            if "SelectedSegmentalOphthalmicAxialLengthSequence" in self._dataset:
                del self._dataset.SelectedSegmentalOphthalmicAxialLengthSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, SelectedSegmentalOphthalmicAxialLengthSequenceItem) for item in value
        ):
            raise ValueError(
                "SelectedSegmentalOphthalmicAxialLengthSequence must be a list of"
                " SelectedSegmentalOphthalmicAxialLengthSequenceItem objects"
            )
        else:
            self._SelectedSegmentalOphthalmicAxialLengthSequence = value
            if "SelectedSegmentalOphthalmicAxialLengthSequence" not in self._dataset:
                self._dataset.SelectedSegmentalOphthalmicAxialLengthSequence = pydicom.Sequence()
            self._dataset.SelectedSegmentalOphthalmicAxialLengthSequence.clear()
            self._dataset.SelectedSegmentalOphthalmicAxialLengthSequence.extend([item.to_dataset() for item in value])

    def add_SelectedSegmentalOphthalmicAxialLength(self, item: SelectedSegmentalOphthalmicAxialLengthSequenceItem):
        if not isinstance(item, SelectedSegmentalOphthalmicAxialLengthSequenceItem):
            raise ValueError("Item must be an instance of SelectedSegmentalOphthalmicAxialLengthSequenceItem")
        self._SelectedSegmentalOphthalmicAxialLengthSequence.append(item)
        if "SelectedSegmentalOphthalmicAxialLengthSequence" not in self._dataset:
            self._dataset.SelectedSegmentalOphthalmicAxialLengthSequence = pydicom.Sequence()
        self._dataset.SelectedSegmentalOphthalmicAxialLengthSequence.append(item.to_dataset())

    @property
    def SelectedTotalOphthalmicAxialLengthSequence(self) -> Optional[List[SelectedTotalOphthalmicAxialLengthSequenceItem]]:
        if "SelectedTotalOphthalmicAxialLengthSequence" in self._dataset:
            if len(self._SelectedTotalOphthalmicAxialLengthSequence) == len(
                self._dataset.SelectedTotalOphthalmicAxialLengthSequence
            ):
                return self._SelectedTotalOphthalmicAxialLengthSequence
            else:
                return [
                    SelectedTotalOphthalmicAxialLengthSequenceItem(x)
                    for x in self._dataset.SelectedTotalOphthalmicAxialLengthSequence
                ]
        return None

    @SelectedTotalOphthalmicAxialLengthSequence.setter
    def SelectedTotalOphthalmicAxialLengthSequence(
        self, value: Optional[List[SelectedTotalOphthalmicAxialLengthSequenceItem]]
    ):
        if value is None:
            self._SelectedTotalOphthalmicAxialLengthSequence = []
            if "SelectedTotalOphthalmicAxialLengthSequence" in self._dataset:
                del self._dataset.SelectedTotalOphthalmicAxialLengthSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, SelectedTotalOphthalmicAxialLengthSequenceItem) for item in value
        ):
            raise ValueError(
                "SelectedTotalOphthalmicAxialLengthSequence must be a list of SelectedTotalOphthalmicAxialLengthSequenceItem"
                " objects"
            )
        else:
            self._SelectedTotalOphthalmicAxialLengthSequence = value
            if "SelectedTotalOphthalmicAxialLengthSequence" not in self._dataset:
                self._dataset.SelectedTotalOphthalmicAxialLengthSequence = pydicom.Sequence()
            self._dataset.SelectedTotalOphthalmicAxialLengthSequence.clear()
            self._dataset.SelectedTotalOphthalmicAxialLengthSequence.extend([item.to_dataset() for item in value])

    def add_SelectedTotalOphthalmicAxialLength(self, item: SelectedTotalOphthalmicAxialLengthSequenceItem):
        if not isinstance(item, SelectedTotalOphthalmicAxialLengthSequenceItem):
            raise ValueError("Item must be an instance of SelectedTotalOphthalmicAxialLengthSequenceItem")
        self._SelectedTotalOphthalmicAxialLengthSequence.append(item)
        if "SelectedTotalOphthalmicAxialLengthSequence" not in self._dataset:
            self._dataset.SelectedTotalOphthalmicAxialLengthSequence = pydicom.Sequence()
        self._dataset.SelectedTotalOphthalmicAxialLengthSequence.append(item.to_dataset())
