from typing import Any, List, Optional

import pydicom

from .code_sequence_item import CodeSequenceItem


class SelectedSegmentalOphthalmicAxialLengthSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._OphthalmicAxialLengthMeasurementsSegmentNameCodeSequence: List[CodeSequenceItem] = []

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
                f"OphthalmicAxialLengthMeasurementsSegmentNameCodeSequence must be a list of CodeSequenceItem objects"
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
            raise ValueError(f"Item must be an instance of CodeSequenceItem")
        self._OphthalmicAxialLengthMeasurementsSegmentNameCodeSequence.append(item)
        if "OphthalmicAxialLengthMeasurementsSegmentNameCodeSequence" not in self._dataset:
            self._dataset.OphthalmicAxialLengthMeasurementsSegmentNameCodeSequence = pydicom.Sequence()
        self._dataset.OphthalmicAxialLengthMeasurementsSegmentNameCodeSequence.append(item.to_dataset())
