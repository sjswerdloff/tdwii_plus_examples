from decimal import Decimal
from typing import Any, List, Optional  # noqa

import pydicom

from .related_reference_rt_image_sequence_item import (
    RelatedReferenceRTImageSequenceItem,
)


class DeliveryVerificationImageSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._RelatedReferenceRTImageSequence: List[RelatedReferenceRTImageSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def VerificationImageTiming(self) -> Optional[str]:
        if "VerificationImageTiming" in self._dataset:
            return self._dataset.VerificationImageTiming
        return None

    @VerificationImageTiming.setter
    def VerificationImageTiming(self, value: Optional[str]):
        if value is None:
            if "VerificationImageTiming" in self._dataset:
                del self._dataset.VerificationImageTiming
        else:
            self._dataset.VerificationImageTiming = value

    @property
    def DoubleExposureFlag(self) -> Optional[str]:
        if "DoubleExposureFlag" in self._dataset:
            return self._dataset.DoubleExposureFlag
        return None

    @DoubleExposureFlag.setter
    def DoubleExposureFlag(self, value: Optional[str]):
        if value is None:
            if "DoubleExposureFlag" in self._dataset:
                del self._dataset.DoubleExposureFlag
        else:
            self._dataset.DoubleExposureFlag = value

    @property
    def DoubleExposureOrdering(self) -> Optional[str]:
        if "DoubleExposureOrdering" in self._dataset:
            return self._dataset.DoubleExposureOrdering
        return None

    @DoubleExposureOrdering.setter
    def DoubleExposureOrdering(self, value: Optional[str]):
        if value is None:
            if "DoubleExposureOrdering" in self._dataset:
                del self._dataset.DoubleExposureOrdering
        else:
            self._dataset.DoubleExposureOrdering = value

    @property
    def RelatedReferenceRTImageSequence(self) -> Optional[List[RelatedReferenceRTImageSequenceItem]]:
        if "RelatedReferenceRTImageSequence" in self._dataset:
            if len(self._RelatedReferenceRTImageSequence) == len(self._dataset.RelatedReferenceRTImageSequence):
                return self._RelatedReferenceRTImageSequence
            else:
                return [RelatedReferenceRTImageSequenceItem(x) for x in self._dataset.RelatedReferenceRTImageSequence]
        return None

    @RelatedReferenceRTImageSequence.setter
    def RelatedReferenceRTImageSequence(self, value: Optional[List[RelatedReferenceRTImageSequenceItem]]):
        if value is None:
            self._RelatedReferenceRTImageSequence = []
            if "RelatedReferenceRTImageSequence" in self._dataset:
                del self._dataset.RelatedReferenceRTImageSequence
        elif not isinstance(value, list) or not all(isinstance(item, RelatedReferenceRTImageSequenceItem) for item in value):
            raise ValueError("RelatedReferenceRTImageSequence must be a list of RelatedReferenceRTImageSequenceItem objects")
        else:
            self._RelatedReferenceRTImageSequence = value
            if "RelatedReferenceRTImageSequence" not in self._dataset:
                self._dataset.RelatedReferenceRTImageSequence = pydicom.Sequence()
            self._dataset.RelatedReferenceRTImageSequence.clear()
            self._dataset.RelatedReferenceRTImageSequence.extend([item.to_dataset() for item in value])

    def add_RelatedReferenceRTImage(self, item: RelatedReferenceRTImageSequenceItem):
        if not isinstance(item, RelatedReferenceRTImageSequenceItem):
            raise ValueError("Item must be an instance of RelatedReferenceRTImageSequenceItem")
        self._RelatedReferenceRTImageSequence.append(item)
        if "RelatedReferenceRTImageSequence" not in self._dataset:
            self._dataset.RelatedReferenceRTImageSequence = pydicom.Sequence()
        self._dataset.RelatedReferenceRTImageSequence.append(item.to_dataset())

    @property
    def DoubleExposureMeterset(self) -> Optional[float]:
        if "DoubleExposureMeterset" in self._dataset:
            return self._dataset.DoubleExposureMeterset
        return None

    @DoubleExposureMeterset.setter
    def DoubleExposureMeterset(self, value: Optional[float]):
        if value is None:
            if "DoubleExposureMeterset" in self._dataset:
                del self._dataset.DoubleExposureMeterset
        else:
            self._dataset.DoubleExposureMeterset = value

    @property
    def DoubleExposureFieldDelta(self) -> Optional[List[float]]:
        if "DoubleExposureFieldDelta" in self._dataset:
            return self._dataset.DoubleExposureFieldDelta
        return None

    @DoubleExposureFieldDelta.setter
    def DoubleExposureFieldDelta(self, value: Optional[List[float]]):
        if value is None:
            if "DoubleExposureFieldDelta" in self._dataset:
                del self._dataset.DoubleExposureFieldDelta
        else:
            self._dataset.DoubleExposureFieldDelta = value

    @property
    def XRayImageReceptorTranslation(self) -> Optional[List[Decimal]]:
        if "XRayImageReceptorTranslation" in self._dataset:
            return self._dataset.XRayImageReceptorTranslation
        return None

    @XRayImageReceptorTranslation.setter
    def XRayImageReceptorTranslation(self, value: Optional[List[Decimal]]):
        if value is None:
            if "XRayImageReceptorTranslation" in self._dataset:
                del self._dataset.XRayImageReceptorTranslation
        else:
            self._dataset.XRayImageReceptorTranslation = value

    @property
    def MetersetExposure(self) -> Optional[Decimal]:
        if "MetersetExposure" in self._dataset:
            return self._dataset.MetersetExposure
        return None

    @MetersetExposure.setter
    def MetersetExposure(self, value: Optional[Decimal]):
        if value is None:
            if "MetersetExposure" in self._dataset:
                del self._dataset.MetersetExposure
        else:
            self._dataset.MetersetExposure = value

    @property
    def StartCumulativeMetersetWeight(self) -> Optional[Decimal]:
        if "StartCumulativeMetersetWeight" in self._dataset:
            return self._dataset.StartCumulativeMetersetWeight
        return None

    @StartCumulativeMetersetWeight.setter
    def StartCumulativeMetersetWeight(self, value: Optional[Decimal]):
        if value is None:
            if "StartCumulativeMetersetWeight" in self._dataset:
                del self._dataset.StartCumulativeMetersetWeight
        else:
            self._dataset.StartCumulativeMetersetWeight = value

    @property
    def EndCumulativeMetersetWeight(self) -> Optional[Decimal]:
        if "EndCumulativeMetersetWeight" in self._dataset:
            return self._dataset.EndCumulativeMetersetWeight
        return None

    @EndCumulativeMetersetWeight.setter
    def EndCumulativeMetersetWeight(self, value: Optional[Decimal]):
        if value is None:
            if "EndCumulativeMetersetWeight" in self._dataset:
                del self._dataset.EndCumulativeMetersetWeight
        else:
            self._dataset.EndCumulativeMetersetWeight = value
