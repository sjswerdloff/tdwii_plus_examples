from typing import Any, List, Optional  # noqa

import pydicom

from .device_motion_control_sequence_item import DeviceMotionControlSequenceItem
from .referenced_rt_radiation_sequence_item import ReferencedRTRadiationSequenceItem
from .referenced_rt_treatment_preparation_sequence_item import (
    ReferencedRTTreatmentPreparationSequenceItem,
)
from .rt_delivery_start_patient_position_sequence_item import (
    RTDeliveryStartPatientPositionSequenceItem,
)


class RTRadiationTaskSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._DeviceMotionControlSequence: List[DeviceMotionControlSequenceItem] = []
        self._ReferencedRTRadiationSequence: List[ReferencedRTRadiationSequenceItem] = []
        self._RTDeliveryStartPatientPositionSequence: List[RTDeliveryStartPatientPositionSequenceItem] = []
        self._ReferencedRTTreatmentPreparationSequence: List[ReferencedRTTreatmentPreparationSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ContinuationStartMeterset(self) -> Optional[float]:
        if "ContinuationStartMeterset" in self._dataset:
            return self._dataset.ContinuationStartMeterset
        return None

    @ContinuationStartMeterset.setter
    def ContinuationStartMeterset(self, value: Optional[float]):
        if value is None:
            if "ContinuationStartMeterset" in self._dataset:
                del self._dataset.ContinuationStartMeterset
        else:
            self._dataset.ContinuationStartMeterset = value

    @property
    def ContinuationEndMeterset(self) -> Optional[float]:
        if "ContinuationEndMeterset" in self._dataset:
            return self._dataset.ContinuationEndMeterset
        return None

    @ContinuationEndMeterset.setter
    def ContinuationEndMeterset(self, value: Optional[float]):
        if value is None:
            if "ContinuationEndMeterset" in self._dataset:
                del self._dataset.ContinuationEndMeterset
        else:
            self._dataset.ContinuationEndMeterset = value

    @property
    def DeviceMotionControlSequence(self) -> Optional[List[DeviceMotionControlSequenceItem]]:
        if "DeviceMotionControlSequence" in self._dataset:
            if len(self._DeviceMotionControlSequence) == len(self._dataset.DeviceMotionControlSequence):
                return self._DeviceMotionControlSequence
            else:
                return [DeviceMotionControlSequenceItem(x) for x in self._dataset.DeviceMotionControlSequence]
        return None

    @DeviceMotionControlSequence.setter
    def DeviceMotionControlSequence(self, value: Optional[List[DeviceMotionControlSequenceItem]]):
        if value is None:
            self._DeviceMotionControlSequence = []
            if "DeviceMotionControlSequence" in self._dataset:
                del self._dataset.DeviceMotionControlSequence
        elif not isinstance(value, list) or not all(isinstance(item, DeviceMotionControlSequenceItem) for item in value):
            raise ValueError("DeviceMotionControlSequence must be a list of DeviceMotionControlSequenceItem objects")
        else:
            self._DeviceMotionControlSequence = value
            if "DeviceMotionControlSequence" not in self._dataset:
                self._dataset.DeviceMotionControlSequence = pydicom.Sequence()
            self._dataset.DeviceMotionControlSequence.clear()
            self._dataset.DeviceMotionControlSequence.extend([item.to_dataset() for item in value])

    def add_DeviceMotionControl(self, item: DeviceMotionControlSequenceItem):
        if not isinstance(item, DeviceMotionControlSequenceItem):
            raise ValueError("Item must be an instance of DeviceMotionControlSequenceItem")
        self._DeviceMotionControlSequence.append(item)
        if "DeviceMotionControlSequence" not in self._dataset:
            self._dataset.DeviceMotionControlSequence = pydicom.Sequence()
        self._dataset.DeviceMotionControlSequence.append(item.to_dataset())

    @property
    def ReferencedRTRadiationSequence(self) -> Optional[List[ReferencedRTRadiationSequenceItem]]:
        if "ReferencedRTRadiationSequence" in self._dataset:
            if len(self._ReferencedRTRadiationSequence) == len(self._dataset.ReferencedRTRadiationSequence):
                return self._ReferencedRTRadiationSequence
            else:
                return [ReferencedRTRadiationSequenceItem(x) for x in self._dataset.ReferencedRTRadiationSequence]
        return None

    @ReferencedRTRadiationSequence.setter
    def ReferencedRTRadiationSequence(self, value: Optional[List[ReferencedRTRadiationSequenceItem]]):
        if value is None:
            self._ReferencedRTRadiationSequence = []
            if "ReferencedRTRadiationSequence" in self._dataset:
                del self._dataset.ReferencedRTRadiationSequence
        elif not isinstance(value, list) or not all(isinstance(item, ReferencedRTRadiationSequenceItem) for item in value):
            raise ValueError("ReferencedRTRadiationSequence must be a list of ReferencedRTRadiationSequenceItem objects")
        else:
            self._ReferencedRTRadiationSequence = value
            if "ReferencedRTRadiationSequence" not in self._dataset:
                self._dataset.ReferencedRTRadiationSequence = pydicom.Sequence()
            self._dataset.ReferencedRTRadiationSequence.clear()
            self._dataset.ReferencedRTRadiationSequence.extend([item.to_dataset() for item in value])

    def add_ReferencedRTRadiation(self, item: ReferencedRTRadiationSequenceItem):
        if not isinstance(item, ReferencedRTRadiationSequenceItem):
            raise ValueError("Item must be an instance of ReferencedRTRadiationSequenceItem")
        self._ReferencedRTRadiationSequence.append(item)
        if "ReferencedRTRadiationSequence" not in self._dataset:
            self._dataset.ReferencedRTRadiationSequence = pydicom.Sequence()
        self._dataset.ReferencedRTRadiationSequence.append(item.to_dataset())

    @property
    def TreatmentDeliveryContinuationFlag(self) -> Optional[str]:
        if "TreatmentDeliveryContinuationFlag" in self._dataset:
            return self._dataset.TreatmentDeliveryContinuationFlag
        return None

    @TreatmentDeliveryContinuationFlag.setter
    def TreatmentDeliveryContinuationFlag(self, value: Optional[str]):
        if value is None:
            if "TreatmentDeliveryContinuationFlag" in self._dataset:
                del self._dataset.TreatmentDeliveryContinuationFlag
        else:
            self._dataset.TreatmentDeliveryContinuationFlag = value

    @property
    def RadiationOrderIndex(self) -> Optional[int]:
        if "RadiationOrderIndex" in self._dataset:
            return self._dataset.RadiationOrderIndex
        return None

    @RadiationOrderIndex.setter
    def RadiationOrderIndex(self, value: Optional[int]):
        if value is None:
            if "RadiationOrderIndex" in self._dataset:
                del self._dataset.RadiationOrderIndex
        else:
            self._dataset.RadiationOrderIndex = value

    @property
    def RTDeliveryStartPatientPositionSequence(self) -> Optional[List[RTDeliveryStartPatientPositionSequenceItem]]:
        if "RTDeliveryStartPatientPositionSequence" in self._dataset:
            if len(self._RTDeliveryStartPatientPositionSequence) == len(self._dataset.RTDeliveryStartPatientPositionSequence):
                return self._RTDeliveryStartPatientPositionSequence
            else:
                return [
                    RTDeliveryStartPatientPositionSequenceItem(x) for x in self._dataset.RTDeliveryStartPatientPositionSequence
                ]
        return None

    @RTDeliveryStartPatientPositionSequence.setter
    def RTDeliveryStartPatientPositionSequence(self, value: Optional[List[RTDeliveryStartPatientPositionSequenceItem]]):
        if value is None:
            self._RTDeliveryStartPatientPositionSequence = []
            if "RTDeliveryStartPatientPositionSequence" in self._dataset:
                del self._dataset.RTDeliveryStartPatientPositionSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, RTDeliveryStartPatientPositionSequenceItem) for item in value
        ):
            raise ValueError(
                "RTDeliveryStartPatientPositionSequence must be a list of RTDeliveryStartPatientPositionSequenceItem objects"
            )
        else:
            self._RTDeliveryStartPatientPositionSequence = value
            if "RTDeliveryStartPatientPositionSequence" not in self._dataset:
                self._dataset.RTDeliveryStartPatientPositionSequence = pydicom.Sequence()
            self._dataset.RTDeliveryStartPatientPositionSequence.clear()
            self._dataset.RTDeliveryStartPatientPositionSequence.extend([item.to_dataset() for item in value])

    def add_RTDeliveryStartPatientPosition(self, item: RTDeliveryStartPatientPositionSequenceItem):
        if not isinstance(item, RTDeliveryStartPatientPositionSequenceItem):
            raise ValueError("Item must be an instance of RTDeliveryStartPatientPositionSequenceItem")
        self._RTDeliveryStartPatientPositionSequence.append(item)
        if "RTDeliveryStartPatientPositionSequence" not in self._dataset:
            self._dataset.RTDeliveryStartPatientPositionSequence = pydicom.Sequence()
        self._dataset.RTDeliveryStartPatientPositionSequence.append(item.to_dataset())

    @property
    def ReferencedRTTreatmentPreparationSequence(self) -> Optional[List[ReferencedRTTreatmentPreparationSequenceItem]]:
        if "ReferencedRTTreatmentPreparationSequence" in self._dataset:
            if len(self._ReferencedRTTreatmentPreparationSequence) == len(
                self._dataset.ReferencedRTTreatmentPreparationSequence
            ):
                return self._ReferencedRTTreatmentPreparationSequence
            else:
                return [
                    ReferencedRTTreatmentPreparationSequenceItem(x)
                    for x in self._dataset.ReferencedRTTreatmentPreparationSequence
                ]
        return None

    @ReferencedRTTreatmentPreparationSequence.setter
    def ReferencedRTTreatmentPreparationSequence(self, value: Optional[List[ReferencedRTTreatmentPreparationSequenceItem]]):
        if value is None:
            self._ReferencedRTTreatmentPreparationSequence = []
            if "ReferencedRTTreatmentPreparationSequence" in self._dataset:
                del self._dataset.ReferencedRTTreatmentPreparationSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, ReferencedRTTreatmentPreparationSequenceItem) for item in value
        ):
            raise ValueError(
                "ReferencedRTTreatmentPreparationSequence must be a list of ReferencedRTTreatmentPreparationSequenceItem"
                " objects"
            )
        else:
            self._ReferencedRTTreatmentPreparationSequence = value
            if "ReferencedRTTreatmentPreparationSequence" not in self._dataset:
                self._dataset.ReferencedRTTreatmentPreparationSequence = pydicom.Sequence()
            self._dataset.ReferencedRTTreatmentPreparationSequence.clear()
            self._dataset.ReferencedRTTreatmentPreparationSequence.extend([item.to_dataset() for item in value])

    def add_ReferencedRTTreatmentPreparation(self, item: ReferencedRTTreatmentPreparationSequenceItem):
        if not isinstance(item, ReferencedRTTreatmentPreparationSequenceItem):
            raise ValueError("Item must be an instance of ReferencedRTTreatmentPreparationSequenceItem")
        self._ReferencedRTTreatmentPreparationSequence.append(item)
        if "ReferencedRTTreatmentPreparationSequence" not in self._dataset:
            self._dataset.ReferencedRTTreatmentPreparationSequence = pydicom.Sequence()
        self._dataset.ReferencedRTTreatmentPreparationSequence.append(item.to_dataset())
