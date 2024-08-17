from typing import Any, List, Optional

import pydicom

from .code_sequence_item import CodeSequenceItem
from .ophthalmic_axial_length_quality_metric_sequence_item import (
    OphthalmicAxialLengthQualityMetricSequenceItem,
)
from .referenced_ophthalmic_axial_length_measurement_qc_image_sequence_item import (
    ReferencedOphthalmicAxialLengthMeasurementQCImageSequenceItem,
)
from .selected_segmental_ophthalmic_axial_length_sequence_item import (
    SelectedSegmentalOphthalmicAxialLengthSequenceItem,
)


class UltrasoundSelectedOphthalmicAxialLengthSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._OphthalmicAxialLengthSelectionMethodCodeSequence: List[CodeSequenceItem] = []
        self._SelectedSegmentalOphthalmicAxialLengthSequence: List[SelectedSegmentalOphthalmicAxialLengthSequenceItem] = []
        self._OphthalmicAxialLengthQualityMetricSequence: List[OphthalmicAxialLengthQualityMetricSequenceItem] = []
        self._ReferencedOphthalmicAxialLengthMeasurementQCImageSequence: List[
            ReferencedOphthalmicAxialLengthMeasurementQCImageSequenceItem
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
    def OphthalmicAxialLengthSelectionMethodCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "OphthalmicAxialLengthSelectionMethodCodeSequence" in self._dataset:
            if len(self._OphthalmicAxialLengthSelectionMethodCodeSequence) == len(
                self._dataset.OphthalmicAxialLengthSelectionMethodCodeSequence
            ):
                return self._OphthalmicAxialLengthSelectionMethodCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.OphthalmicAxialLengthSelectionMethodCodeSequence]
        return None

    @OphthalmicAxialLengthSelectionMethodCodeSequence.setter
    def OphthalmicAxialLengthSelectionMethodCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._OphthalmicAxialLengthSelectionMethodCodeSequence = []
            if "OphthalmicAxialLengthSelectionMethodCodeSequence" in self._dataset:
                del self._dataset.OphthalmicAxialLengthSelectionMethodCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError(f"OphthalmicAxialLengthSelectionMethodCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._OphthalmicAxialLengthSelectionMethodCodeSequence = value
            if "OphthalmicAxialLengthSelectionMethodCodeSequence" not in self._dataset:
                self._dataset.OphthalmicAxialLengthSelectionMethodCodeSequence = pydicom.Sequence()
            self._dataset.OphthalmicAxialLengthSelectionMethodCodeSequence.clear()
            self._dataset.OphthalmicAxialLengthSelectionMethodCodeSequence.extend([item.to_dataset() for item in value])

    def add_OphthalmicAxialLengthSelectionMethodCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError(f"Item must be an instance of CodeSequenceItem")
        self._OphthalmicAxialLengthSelectionMethodCodeSequence.append(item)
        if "OphthalmicAxialLengthSelectionMethodCodeSequence" not in self._dataset:
            self._dataset.OphthalmicAxialLengthSelectionMethodCodeSequence = pydicom.Sequence()
        self._dataset.OphthalmicAxialLengthSelectionMethodCodeSequence.append(item.to_dataset())

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
                f"SelectedSegmentalOphthalmicAxialLengthSequence must be a list of SelectedSegmentalOphthalmicAxialLengthSequenceItem objects"
            )
        else:
            self._SelectedSegmentalOphthalmicAxialLengthSequence = value
            if "SelectedSegmentalOphthalmicAxialLengthSequence" not in self._dataset:
                self._dataset.SelectedSegmentalOphthalmicAxialLengthSequence = pydicom.Sequence()
            self._dataset.SelectedSegmentalOphthalmicAxialLengthSequence.clear()
            self._dataset.SelectedSegmentalOphthalmicAxialLengthSequence.extend([item.to_dataset() for item in value])

    def add_SelectedSegmentalOphthalmicAxialLength(self, item: SelectedSegmentalOphthalmicAxialLengthSequenceItem):
        if not isinstance(item, SelectedSegmentalOphthalmicAxialLengthSequenceItem):
            raise ValueError(f"Item must be an instance of SelectedSegmentalOphthalmicAxialLengthSequenceItem")
        self._SelectedSegmentalOphthalmicAxialLengthSequence.append(item)
        if "SelectedSegmentalOphthalmicAxialLengthSequence" not in self._dataset:
            self._dataset.SelectedSegmentalOphthalmicAxialLengthSequence = pydicom.Sequence()
        self._dataset.SelectedSegmentalOphthalmicAxialLengthSequence.append(item.to_dataset())

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
                f"OphthalmicAxialLengthQualityMetricSequence must be a list of OphthalmicAxialLengthQualityMetricSequenceItem objects"
            )
        else:
            self._OphthalmicAxialLengthQualityMetricSequence = value
            if "OphthalmicAxialLengthQualityMetricSequence" not in self._dataset:
                self._dataset.OphthalmicAxialLengthQualityMetricSequence = pydicom.Sequence()
            self._dataset.OphthalmicAxialLengthQualityMetricSequence.clear()
            self._dataset.OphthalmicAxialLengthQualityMetricSequence.extend([item.to_dataset() for item in value])

    def add_OphthalmicAxialLengthQualityMetric(self, item: OphthalmicAxialLengthQualityMetricSequenceItem):
        if not isinstance(item, OphthalmicAxialLengthQualityMetricSequenceItem):
            raise ValueError(f"Item must be an instance of OphthalmicAxialLengthQualityMetricSequenceItem")
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
