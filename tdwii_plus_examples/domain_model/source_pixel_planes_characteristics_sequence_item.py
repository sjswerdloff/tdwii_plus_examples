from decimal import Decimal
from typing import Any, List, Optional  # noqa

import pydicom


class SourcePixelPlanesCharacteristicsSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def SpacingBetweenSlices(self) -> Optional[Decimal]:
        if "SpacingBetweenSlices" in self._dataset:
            return self._dataset.SpacingBetweenSlices
        return None

    @SpacingBetweenSlices.setter
    def SpacingBetweenSlices(self, value: Optional[Decimal]):
        if value is None:
            if "SpacingBetweenSlices" in self._dataset:
                del self._dataset.SpacingBetweenSlices
        else:
            self._dataset.SpacingBetweenSlices = value

    @property
    def ImagePositionPatient(self) -> Optional[List[Decimal]]:
        if "ImagePositionPatient" in self._dataset:
            return self._dataset.ImagePositionPatient
        return None

    @ImagePositionPatient.setter
    def ImagePositionPatient(self, value: Optional[List[Decimal]]):
        if value is None:
            if "ImagePositionPatient" in self._dataset:
                del self._dataset.ImagePositionPatient
        else:
            self._dataset.ImagePositionPatient = value

    @property
    def ImageOrientationPatient(self) -> Optional[List[Decimal]]:
        if "ImageOrientationPatient" in self._dataset:
            return self._dataset.ImageOrientationPatient
        return None

    @ImageOrientationPatient.setter
    def ImageOrientationPatient(self, value: Optional[List[Decimal]]):
        if value is None:
            if "ImageOrientationPatient" in self._dataset:
                del self._dataset.ImageOrientationPatient
        else:
            self._dataset.ImageOrientationPatient = value

    @property
    def NumberOfFrames(self) -> Optional[int]:
        if "NumberOfFrames" in self._dataset:
            return self._dataset.NumberOfFrames
        return None

    @NumberOfFrames.setter
    def NumberOfFrames(self, value: Optional[int]):
        if value is None:
            if "NumberOfFrames" in self._dataset:
                del self._dataset.NumberOfFrames
        else:
            self._dataset.NumberOfFrames = value

    @property
    def Rows(self) -> Optional[int]:
        if "Rows" in self._dataset:
            return self._dataset.Rows
        return None

    @Rows.setter
    def Rows(self, value: Optional[int]):
        if value is None:
            if "Rows" in self._dataset:
                del self._dataset.Rows
        else:
            self._dataset.Rows = value

    @property
    def Columns(self) -> Optional[int]:
        if "Columns" in self._dataset:
            return self._dataset.Columns
        return None

    @Columns.setter
    def Columns(self, value: Optional[int]):
        if value is None:
            if "Columns" in self._dataset:
                del self._dataset.Columns
        else:
            self._dataset.Columns = value

    @property
    def PixelSpacing(self) -> Optional[List[Decimal]]:
        if "PixelSpacing" in self._dataset:
            return self._dataset.PixelSpacing
        return None

    @PixelSpacing.setter
    def PixelSpacing(self, value: Optional[List[Decimal]]):
        if value is None:
            if "PixelSpacing" in self._dataset:
                del self._dataset.PixelSpacing
        else:
            self._dataset.PixelSpacing = value
