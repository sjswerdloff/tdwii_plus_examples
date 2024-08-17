from typing import Any, List, Optional

import pydicom

from .contour_sequence_item import ContourSequenceItem
from .source_pixel_planes_characteristics_sequence_item import (
    SourcePixelPlanesCharacteristicsSequenceItem,
)
from .source_series_sequence_item import SourceSeriesSequenceItem


class ROIContourSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._ContourSequence: List[ContourSequenceItem] = []
        self._SourcePixelPlanesCharacteristicsSequence: List[SourcePixelPlanesCharacteristicsSequenceItem] = []
        self._SourceSeriesSequence: List[SourceSeriesSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def RecommendedDisplayGrayscaleValue(self) -> Optional[int]:
        if "RecommendedDisplayGrayscaleValue" in self._dataset:
            return self._dataset.RecommendedDisplayGrayscaleValue
        return None

    @RecommendedDisplayGrayscaleValue.setter
    def RecommendedDisplayGrayscaleValue(self, value: Optional[int]):
        if value is None:
            if "RecommendedDisplayGrayscaleValue" in self._dataset:
                del self._dataset.RecommendedDisplayGrayscaleValue
        else:
            self._dataset.RecommendedDisplayGrayscaleValue = value

    @property
    def RecommendedDisplayCIELabValue(self) -> Optional[List[int]]:
        if "RecommendedDisplayCIELabValue" in self._dataset:
            return self._dataset.RecommendedDisplayCIELabValue
        return None

    @RecommendedDisplayCIELabValue.setter
    def RecommendedDisplayCIELabValue(self, value: Optional[List[int]]):
        if value is None:
            if "RecommendedDisplayCIELabValue" in self._dataset:
                del self._dataset.RecommendedDisplayCIELabValue
        else:
            self._dataset.RecommendedDisplayCIELabValue = value

    @property
    def ROIDisplayColor(self) -> Optional[List[int]]:
        if "ROIDisplayColor" in self._dataset:
            return self._dataset.ROIDisplayColor
        return None

    @ROIDisplayColor.setter
    def ROIDisplayColor(self, value: Optional[List[int]]):
        if value is None:
            if "ROIDisplayColor" in self._dataset:
                del self._dataset.ROIDisplayColor
        else:
            self._dataset.ROIDisplayColor = value

    @property
    def ContourSequence(self) -> Optional[List[ContourSequenceItem]]:
        if "ContourSequence" in self._dataset:
            if len(self._ContourSequence) == len(self._dataset.ContourSequence):
                return self._ContourSequence
            else:
                return [ContourSequenceItem(x) for x in self._dataset.ContourSequence]
        return None

    @ContourSequence.setter
    def ContourSequence(self, value: Optional[List[ContourSequenceItem]]):
        if value is None:
            self._ContourSequence = []
            if "ContourSequence" in self._dataset:
                del self._dataset.ContourSequence
        elif not isinstance(value, list) or not all(isinstance(item, ContourSequenceItem) for item in value):
            raise ValueError(f"ContourSequence must be a list of ContourSequenceItem objects")
        else:
            self._ContourSequence = value
            if "ContourSequence" not in self._dataset:
                self._dataset.ContourSequence = pydicom.Sequence()
            self._dataset.ContourSequence.clear()
            self._dataset.ContourSequence.extend([item.to_dataset() for item in value])

    def add_Contour(self, item: ContourSequenceItem):
        if not isinstance(item, ContourSequenceItem):
            raise ValueError(f"Item must be an instance of ContourSequenceItem")
        self._ContourSequence.append(item)
        if "ContourSequence" not in self._dataset:
            self._dataset.ContourSequence = pydicom.Sequence()
        self._dataset.ContourSequence.append(item.to_dataset())

    @property
    def SourcePixelPlanesCharacteristicsSequence(self) -> Optional[List[SourcePixelPlanesCharacteristicsSequenceItem]]:
        if "SourcePixelPlanesCharacteristicsSequence" in self._dataset:
            if len(self._SourcePixelPlanesCharacteristicsSequence) == len(
                self._dataset.SourcePixelPlanesCharacteristicsSequence
            ):
                return self._SourcePixelPlanesCharacteristicsSequence
            else:
                return [
                    SourcePixelPlanesCharacteristicsSequenceItem(x)
                    for x in self._dataset.SourcePixelPlanesCharacteristicsSequence
                ]
        return None

    @SourcePixelPlanesCharacteristicsSequence.setter
    def SourcePixelPlanesCharacteristicsSequence(self, value: Optional[List[SourcePixelPlanesCharacteristicsSequenceItem]]):
        if value is None:
            self._SourcePixelPlanesCharacteristicsSequence = []
            if "SourcePixelPlanesCharacteristicsSequence" in self._dataset:
                del self._dataset.SourcePixelPlanesCharacteristicsSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, SourcePixelPlanesCharacteristicsSequenceItem) for item in value
        ):
            raise ValueError(
                f"SourcePixelPlanesCharacteristicsSequence must be a list of SourcePixelPlanesCharacteristicsSequenceItem objects"
            )
        else:
            self._SourcePixelPlanesCharacteristicsSequence = value
            if "SourcePixelPlanesCharacteristicsSequence" not in self._dataset:
                self._dataset.SourcePixelPlanesCharacteristicsSequence = pydicom.Sequence()
            self._dataset.SourcePixelPlanesCharacteristicsSequence.clear()
            self._dataset.SourcePixelPlanesCharacteristicsSequence.extend([item.to_dataset() for item in value])

    def add_SourcePixelPlanesCharacteristics(self, item: SourcePixelPlanesCharacteristicsSequenceItem):
        if not isinstance(item, SourcePixelPlanesCharacteristicsSequenceItem):
            raise ValueError(f"Item must be an instance of SourcePixelPlanesCharacteristicsSequenceItem")
        self._SourcePixelPlanesCharacteristicsSequence.append(item)
        if "SourcePixelPlanesCharacteristicsSequence" not in self._dataset:
            self._dataset.SourcePixelPlanesCharacteristicsSequence = pydicom.Sequence()
        self._dataset.SourcePixelPlanesCharacteristicsSequence.append(item.to_dataset())

    @property
    def SourceSeriesSequence(self) -> Optional[List[SourceSeriesSequenceItem]]:
        if "SourceSeriesSequence" in self._dataset:
            if len(self._SourceSeriesSequence) == len(self._dataset.SourceSeriesSequence):
                return self._SourceSeriesSequence
            else:
                return [SourceSeriesSequenceItem(x) for x in self._dataset.SourceSeriesSequence]
        return None

    @SourceSeriesSequence.setter
    def SourceSeriesSequence(self, value: Optional[List[SourceSeriesSequenceItem]]):
        if value is None:
            self._SourceSeriesSequence = []
            if "SourceSeriesSequence" in self._dataset:
                del self._dataset.SourceSeriesSequence
        elif not isinstance(value, list) or not all(isinstance(item, SourceSeriesSequenceItem) for item in value):
            raise ValueError(f"SourceSeriesSequence must be a list of SourceSeriesSequenceItem objects")
        else:
            self._SourceSeriesSequence = value
            if "SourceSeriesSequence" not in self._dataset:
                self._dataset.SourceSeriesSequence = pydicom.Sequence()
            self._dataset.SourceSeriesSequence.clear()
            self._dataset.SourceSeriesSequence.extend([item.to_dataset() for item in value])

    def add_SourceSeries(self, item: SourceSeriesSequenceItem):
        if not isinstance(item, SourceSeriesSequenceItem):
            raise ValueError(f"Item must be an instance of SourceSeriesSequenceItem")
        self._SourceSeriesSequence.append(item)
        if "SourceSeriesSequence" not in self._dataset:
            self._dataset.SourceSeriesSequence = pydicom.Sequence()
        self._dataset.SourceSeriesSequence.append(item.to_dataset())

    @property
    def ReferencedROINumber(self) -> Optional[int]:
        if "ReferencedROINumber" in self._dataset:
            return self._dataset.ReferencedROINumber
        return None

    @ReferencedROINumber.setter
    def ReferencedROINumber(self, value: Optional[int]):
        if value is None:
            if "ReferencedROINumber" in self._dataset:
                del self._dataset.ReferencedROINumber
        else:
            self._dataset.ReferencedROINumber = value
