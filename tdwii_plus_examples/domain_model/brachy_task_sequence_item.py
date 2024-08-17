from decimal import Decimal
from typing import Any, List, Optional  # noqa

import pydicom

from .channel_delivery_continuation_sequence_item import (
    ChannelDeliveryContinuationSequenceItem,
)
from .channel_delivery_order_sequence_item import ChannelDeliveryOrderSequenceItem


class BrachyTaskSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._ChannelDeliveryOrderSequence: List[ChannelDeliveryOrderSequenceItem] = []
        self._ChannelDeliveryContinuationSequence: List[ChannelDeliveryContinuationSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ContinuationStartTotalReferenceAirKerma(self) -> Optional[Decimal]:
        if "ContinuationStartTotalReferenceAirKerma" in self._dataset:
            return self._dataset.ContinuationStartTotalReferenceAirKerma
        return None

    @ContinuationStartTotalReferenceAirKerma.setter
    def ContinuationStartTotalReferenceAirKerma(self, value: Optional[Decimal]):
        if value is None:
            if "ContinuationStartTotalReferenceAirKerma" in self._dataset:
                del self._dataset.ContinuationStartTotalReferenceAirKerma
        else:
            self._dataset.ContinuationStartTotalReferenceAirKerma = value

    @property
    def ContinuationEndTotalReferenceAirKerma(self) -> Optional[Decimal]:
        if "ContinuationEndTotalReferenceAirKerma" in self._dataset:
            return self._dataset.ContinuationEndTotalReferenceAirKerma
        return None

    @ContinuationEndTotalReferenceAirKerma.setter
    def ContinuationEndTotalReferenceAirKerma(self, value: Optional[Decimal]):
        if value is None:
            if "ContinuationEndTotalReferenceAirKerma" in self._dataset:
                del self._dataset.ContinuationEndTotalReferenceAirKerma
        else:
            self._dataset.ContinuationEndTotalReferenceAirKerma = value

    @property
    def ChannelDeliveryOrderSequence(self) -> Optional[List[ChannelDeliveryOrderSequenceItem]]:
        if "ChannelDeliveryOrderSequence" in self._dataset:
            if len(self._ChannelDeliveryOrderSequence) == len(self._dataset.ChannelDeliveryOrderSequence):
                return self._ChannelDeliveryOrderSequence
            else:
                return [ChannelDeliveryOrderSequenceItem(x) for x in self._dataset.ChannelDeliveryOrderSequence]
        return None

    @ChannelDeliveryOrderSequence.setter
    def ChannelDeliveryOrderSequence(self, value: Optional[List[ChannelDeliveryOrderSequenceItem]]):
        if value is None:
            self._ChannelDeliveryOrderSequence = []
            if "ChannelDeliveryOrderSequence" in self._dataset:
                del self._dataset.ChannelDeliveryOrderSequence
        elif not isinstance(value, list) or not all(isinstance(item, ChannelDeliveryOrderSequenceItem) for item in value):
            raise ValueError("ChannelDeliveryOrderSequence must be a list of ChannelDeliveryOrderSequenceItem objects")
        else:
            self._ChannelDeliveryOrderSequence = value
            if "ChannelDeliveryOrderSequence" not in self._dataset:
                self._dataset.ChannelDeliveryOrderSequence = pydicom.Sequence()
            self._dataset.ChannelDeliveryOrderSequence.clear()
            self._dataset.ChannelDeliveryOrderSequence.extend([item.to_dataset() for item in value])

    def add_ChannelDeliveryOrder(self, item: ChannelDeliveryOrderSequenceItem):
        if not isinstance(item, ChannelDeliveryOrderSequenceItem):
            raise ValueError("Item must be an instance of ChannelDeliveryOrderSequenceItem")
        self._ChannelDeliveryOrderSequence.append(item)
        if "ChannelDeliveryOrderSequence" not in self._dataset:
            self._dataset.ChannelDeliveryOrderSequence = pydicom.Sequence()
        self._dataset.ChannelDeliveryOrderSequence.append(item.to_dataset())

    @property
    def ChannelDeliveryContinuationSequence(self) -> Optional[List[ChannelDeliveryContinuationSequenceItem]]:
        if "ChannelDeliveryContinuationSequence" in self._dataset:
            if len(self._ChannelDeliveryContinuationSequence) == len(self._dataset.ChannelDeliveryContinuationSequence):
                return self._ChannelDeliveryContinuationSequence
            else:
                return [ChannelDeliveryContinuationSequenceItem(x) for x in self._dataset.ChannelDeliveryContinuationSequence]
        return None

    @ChannelDeliveryContinuationSequence.setter
    def ChannelDeliveryContinuationSequence(self, value: Optional[List[ChannelDeliveryContinuationSequenceItem]]):
        if value is None:
            self._ChannelDeliveryContinuationSequence = []
            if "ChannelDeliveryContinuationSequence" in self._dataset:
                del self._dataset.ChannelDeliveryContinuationSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, ChannelDeliveryContinuationSequenceItem) for item in value
        ):
            raise ValueError(
                "ChannelDeliveryContinuationSequence must be a list of ChannelDeliveryContinuationSequenceItem objects"
            )
        else:
            self._ChannelDeliveryContinuationSequence = value
            if "ChannelDeliveryContinuationSequence" not in self._dataset:
                self._dataset.ChannelDeliveryContinuationSequence = pydicom.Sequence()
            self._dataset.ChannelDeliveryContinuationSequence.clear()
            self._dataset.ChannelDeliveryContinuationSequence.extend([item.to_dataset() for item in value])

    def add_ChannelDeliveryContinuation(self, item: ChannelDeliveryContinuationSequenceItem):
        if not isinstance(item, ChannelDeliveryContinuationSequenceItem):
            raise ValueError("Item must be an instance of ChannelDeliveryContinuationSequenceItem")
        self._ChannelDeliveryContinuationSequence.append(item)
        if "ChannelDeliveryContinuationSequence" not in self._dataset:
            self._dataset.ChannelDeliveryContinuationSequence = pydicom.Sequence()
        self._dataset.ChannelDeliveryContinuationSequence.append(item.to_dataset())

    @property
    def TreatmentDeliveryType(self) -> Optional[str]:
        if "TreatmentDeliveryType" in self._dataset:
            return self._dataset.TreatmentDeliveryType
        return None

    @TreatmentDeliveryType.setter
    def TreatmentDeliveryType(self, value: Optional[str]):
        if value is None:
            if "TreatmentDeliveryType" in self._dataset:
                del self._dataset.TreatmentDeliveryType
        else:
            self._dataset.TreatmentDeliveryType = value

    @property
    def ReferencedBrachyApplicationSetupNumber(self) -> Optional[int]:
        if "ReferencedBrachyApplicationSetupNumber" in self._dataset:
            return self._dataset.ReferencedBrachyApplicationSetupNumber
        return None

    @ReferencedBrachyApplicationSetupNumber.setter
    def ReferencedBrachyApplicationSetupNumber(self, value: Optional[int]):
        if value is None:
            if "ReferencedBrachyApplicationSetupNumber" in self._dataset:
                del self._dataset.ReferencedBrachyApplicationSetupNumber
        else:
            self._dataset.ReferencedBrachyApplicationSetupNumber = value
