from decimal import Decimal
from typing import Any, List, Optional  # noqa

import pydicom

from .modality_lut_sequence_item import ModalityLUTSequenceItem
from .referenced_series_sequence_item import ReferencedSeriesSequenceItem
from .softcopy_voilut_sequence_item import SoftcopyVOILUTSequenceItem


class BlendingSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._ReferencedSeriesSequence: List[ReferencedSeriesSequenceItem] = []
        self._ModalityLUTSequence: List[ModalityLUTSequenceItem] = []
        self._SoftcopyVOILUTSequence: List[SoftcopyVOILUTSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ReferencedSeriesSequence(self) -> Optional[List[ReferencedSeriesSequenceItem]]:
        if "ReferencedSeriesSequence" in self._dataset:
            if len(self._ReferencedSeriesSequence) == len(self._dataset.ReferencedSeriesSequence):
                return self._ReferencedSeriesSequence
            else:
                return [ReferencedSeriesSequenceItem(x) for x in self._dataset.ReferencedSeriesSequence]
        return None

    @ReferencedSeriesSequence.setter
    def ReferencedSeriesSequence(self, value: Optional[List[ReferencedSeriesSequenceItem]]):
        if value is None:
            self._ReferencedSeriesSequence = []
            if "ReferencedSeriesSequence" in self._dataset:
                del self._dataset.ReferencedSeriesSequence
        elif not isinstance(value, list) or not all(isinstance(item, ReferencedSeriesSequenceItem) for item in value):
            raise ValueError("ReferencedSeriesSequence must be a list of ReferencedSeriesSequenceItem objects")
        else:
            self._ReferencedSeriesSequence = value
            if "ReferencedSeriesSequence" not in self._dataset:
                self._dataset.ReferencedSeriesSequence = pydicom.Sequence()
            self._dataset.ReferencedSeriesSequence.clear()
            self._dataset.ReferencedSeriesSequence.extend([item.to_dataset() for item in value])

    def add_ReferencedSeries(self, item: ReferencedSeriesSequenceItem):
        if not isinstance(item, ReferencedSeriesSequenceItem):
            raise ValueError("Item must be an instance of ReferencedSeriesSequenceItem")
        self._ReferencedSeriesSequence.append(item)
        if "ReferencedSeriesSequence" not in self._dataset:
            self._dataset.ReferencedSeriesSequence = pydicom.Sequence()
        self._dataset.ReferencedSeriesSequence.append(item.to_dataset())

    @property
    def StudyInstanceUID(self) -> Optional[str]:
        if "StudyInstanceUID" in self._dataset:
            return self._dataset.StudyInstanceUID
        return None

    @StudyInstanceUID.setter
    def StudyInstanceUID(self, value: Optional[str]):
        if value is None:
            if "StudyInstanceUID" in self._dataset:
                del self._dataset.StudyInstanceUID
        else:
            self._dataset.StudyInstanceUID = value

    @property
    def RescaleIntercept(self) -> Optional[Decimal]:
        if "RescaleIntercept" in self._dataset:
            return self._dataset.RescaleIntercept
        return None

    @RescaleIntercept.setter
    def RescaleIntercept(self, value: Optional[Decimal]):
        if value is None:
            if "RescaleIntercept" in self._dataset:
                del self._dataset.RescaleIntercept
        else:
            self._dataset.RescaleIntercept = value

    @property
    def RescaleSlope(self) -> Optional[Decimal]:
        if "RescaleSlope" in self._dataset:
            return self._dataset.RescaleSlope
        return None

    @RescaleSlope.setter
    def RescaleSlope(self, value: Optional[Decimal]):
        if value is None:
            if "RescaleSlope" in self._dataset:
                del self._dataset.RescaleSlope
        else:
            self._dataset.RescaleSlope = value

    @property
    def RescaleType(self) -> Optional[str]:
        if "RescaleType" in self._dataset:
            return self._dataset.RescaleType
        return None

    @RescaleType.setter
    def RescaleType(self, value: Optional[str]):
        if value is None:
            if "RescaleType" in self._dataset:
                del self._dataset.RescaleType
        else:
            self._dataset.RescaleType = value

    @property
    def ModalityLUTSequence(self) -> Optional[List[ModalityLUTSequenceItem]]:
        if "ModalityLUTSequence" in self._dataset:
            if len(self._ModalityLUTSequence) == len(self._dataset.ModalityLUTSequence):
                return self._ModalityLUTSequence
            else:
                return [ModalityLUTSequenceItem(x) for x in self._dataset.ModalityLUTSequence]
        return None

    @ModalityLUTSequence.setter
    def ModalityLUTSequence(self, value: Optional[List[ModalityLUTSequenceItem]]):
        if value is None:
            self._ModalityLUTSequence = []
            if "ModalityLUTSequence" in self._dataset:
                del self._dataset.ModalityLUTSequence
        elif not isinstance(value, list) or not all(isinstance(item, ModalityLUTSequenceItem) for item in value):
            raise ValueError("ModalityLUTSequence must be a list of ModalityLUTSequenceItem objects")
        else:
            self._ModalityLUTSequence = value
            if "ModalityLUTSequence" not in self._dataset:
                self._dataset.ModalityLUTSequence = pydicom.Sequence()
            self._dataset.ModalityLUTSequence.clear()
            self._dataset.ModalityLUTSequence.extend([item.to_dataset() for item in value])

    def add_ModalityLUT(self, item: ModalityLUTSequenceItem):
        if not isinstance(item, ModalityLUTSequenceItem):
            raise ValueError("Item must be an instance of ModalityLUTSequenceItem")
        self._ModalityLUTSequence.append(item)
        if "ModalityLUTSequence" not in self._dataset:
            self._dataset.ModalityLUTSequence = pydicom.Sequence()
        self._dataset.ModalityLUTSequence.append(item.to_dataset())

    @property
    def SoftcopyVOILUTSequence(self) -> Optional[List[SoftcopyVOILUTSequenceItem]]:
        if "SoftcopyVOILUTSequence" in self._dataset:
            if len(self._SoftcopyVOILUTSequence) == len(self._dataset.SoftcopyVOILUTSequence):
                return self._SoftcopyVOILUTSequence
            else:
                return [SoftcopyVOILUTSequenceItem(x) for x in self._dataset.SoftcopyVOILUTSequence]
        return None

    @SoftcopyVOILUTSequence.setter
    def SoftcopyVOILUTSequence(self, value: Optional[List[SoftcopyVOILUTSequenceItem]]):
        if value is None:
            self._SoftcopyVOILUTSequence = []
            if "SoftcopyVOILUTSequence" in self._dataset:
                del self._dataset.SoftcopyVOILUTSequence
        elif not isinstance(value, list) or not all(isinstance(item, SoftcopyVOILUTSequenceItem) for item in value):
            raise ValueError("SoftcopyVOILUTSequence must be a list of SoftcopyVOILUTSequenceItem objects")
        else:
            self._SoftcopyVOILUTSequence = value
            if "SoftcopyVOILUTSequence" not in self._dataset:
                self._dataset.SoftcopyVOILUTSequence = pydicom.Sequence()
            self._dataset.SoftcopyVOILUTSequence.clear()
            self._dataset.SoftcopyVOILUTSequence.extend([item.to_dataset() for item in value])

    def add_SoftcopyVOILUT(self, item: SoftcopyVOILUTSequenceItem):
        if not isinstance(item, SoftcopyVOILUTSequenceItem):
            raise ValueError("Item must be an instance of SoftcopyVOILUTSequenceItem")
        self._SoftcopyVOILUTSequence.append(item)
        if "SoftcopyVOILUTSequence" not in self._dataset:
            self._dataset.SoftcopyVOILUTSequence = pydicom.Sequence()
        self._dataset.SoftcopyVOILUTSequence.append(item.to_dataset())

    @property
    def BlendingPosition(self) -> Optional[str]:
        if "BlendingPosition" in self._dataset:
            return self._dataset.BlendingPosition
        return None

    @BlendingPosition.setter
    def BlendingPosition(self, value: Optional[str]):
        if value is None:
            if "BlendingPosition" in self._dataset:
                del self._dataset.BlendingPosition
        else:
            self._dataset.BlendingPosition = value
