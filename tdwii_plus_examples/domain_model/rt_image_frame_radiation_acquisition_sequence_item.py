from typing import Any, List, Optional  # noqa

import pydicom

from .rt_image_frame_mv_radiation_acquisition_sequence_item import (
    RTImageFrameMVRadiationAcquisitionSequenceItem,
)
from .rt_image_framek_v_radiation_acquisition_sequence_item import (
    RTImageFramekVRadiationAcquisitionSequenceItem,
)


class RTImageFrameRadiationAcquisitionSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._RTImageFramekVRadiationAcquisitionSequence: List[RTImageFramekVRadiationAcquisitionSequenceItem] = []
        self._RTImageFrameMVRadiationAcquisitionSequence: List[RTImageFrameMVRadiationAcquisitionSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def RTImageFramekVRadiationAcquisitionSequence(self) -> Optional[List[RTImageFramekVRadiationAcquisitionSequenceItem]]:
        if "RTImageFramekVRadiationAcquisitionSequence" in self._dataset:
            if len(self._RTImageFramekVRadiationAcquisitionSequence) == len(
                self._dataset.RTImageFramekVRadiationAcquisitionSequence
            ):
                return self._RTImageFramekVRadiationAcquisitionSequence
            else:
                return [
                    RTImageFramekVRadiationAcquisitionSequenceItem(x)
                    for x in self._dataset.RTImageFramekVRadiationAcquisitionSequence
                ]
        return None

    @RTImageFramekVRadiationAcquisitionSequence.setter
    def RTImageFramekVRadiationAcquisitionSequence(
        self, value: Optional[List[RTImageFramekVRadiationAcquisitionSequenceItem]]
    ):
        if value is None:
            self._RTImageFramekVRadiationAcquisitionSequence = []
            if "RTImageFramekVRadiationAcquisitionSequence" in self._dataset:
                del self._dataset.RTImageFramekVRadiationAcquisitionSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, RTImageFramekVRadiationAcquisitionSequenceItem) for item in value
        ):
            raise ValueError(
                "RTImageFramekVRadiationAcquisitionSequence must be a list of RTImageFramekVRadiationAcquisitionSequenceItem"
                " objects"
            )
        else:
            self._RTImageFramekVRadiationAcquisitionSequence = value
            if "RTImageFramekVRadiationAcquisitionSequence" not in self._dataset:
                self._dataset.RTImageFramekVRadiationAcquisitionSequence = pydicom.Sequence()
            self._dataset.RTImageFramekVRadiationAcquisitionSequence.clear()
            self._dataset.RTImageFramekVRadiationAcquisitionSequence.extend([item.to_dataset() for item in value])

    def add_RTImageFramekVRadiationAcquisition(self, item: RTImageFramekVRadiationAcquisitionSequenceItem):
        if not isinstance(item, RTImageFramekVRadiationAcquisitionSequenceItem):
            raise ValueError("Item must be an instance of RTImageFramekVRadiationAcquisitionSequenceItem")
        self._RTImageFramekVRadiationAcquisitionSequence.append(item)
        if "RTImageFramekVRadiationAcquisitionSequence" not in self._dataset:
            self._dataset.RTImageFramekVRadiationAcquisitionSequence = pydicom.Sequence()
        self._dataset.RTImageFramekVRadiationAcquisitionSequence.append(item.to_dataset())

    @property
    def RTImageFrameMVRadiationAcquisitionSequence(self) -> Optional[List[RTImageFrameMVRadiationAcquisitionSequenceItem]]:
        if "RTImageFrameMVRadiationAcquisitionSequence" in self._dataset:
            if len(self._RTImageFrameMVRadiationAcquisitionSequence) == len(
                self._dataset.RTImageFrameMVRadiationAcquisitionSequence
            ):
                return self._RTImageFrameMVRadiationAcquisitionSequence
            else:
                return [
                    RTImageFrameMVRadiationAcquisitionSequenceItem(x)
                    for x in self._dataset.RTImageFrameMVRadiationAcquisitionSequence
                ]
        return None

    @RTImageFrameMVRadiationAcquisitionSequence.setter
    def RTImageFrameMVRadiationAcquisitionSequence(
        self, value: Optional[List[RTImageFrameMVRadiationAcquisitionSequenceItem]]
    ):
        if value is None:
            self._RTImageFrameMVRadiationAcquisitionSequence = []
            if "RTImageFrameMVRadiationAcquisitionSequence" in self._dataset:
                del self._dataset.RTImageFrameMVRadiationAcquisitionSequence
        elif not isinstance(value, list) or not all(
            isinstance(item, RTImageFrameMVRadiationAcquisitionSequenceItem) for item in value
        ):
            raise ValueError(
                "RTImageFrameMVRadiationAcquisitionSequence must be a list of RTImageFrameMVRadiationAcquisitionSequenceItem"
                " objects"
            )
        else:
            self._RTImageFrameMVRadiationAcquisitionSequence = value
            if "RTImageFrameMVRadiationAcquisitionSequence" not in self._dataset:
                self._dataset.RTImageFrameMVRadiationAcquisitionSequence = pydicom.Sequence()
            self._dataset.RTImageFrameMVRadiationAcquisitionSequence.clear()
            self._dataset.RTImageFrameMVRadiationAcquisitionSequence.extend([item.to_dataset() for item in value])

    def add_RTImageFrameMVRadiationAcquisition(self, item: RTImageFrameMVRadiationAcquisitionSequenceItem):
        if not isinstance(item, RTImageFrameMVRadiationAcquisitionSequenceItem):
            raise ValueError("Item must be an instance of RTImageFrameMVRadiationAcquisitionSequenceItem")
        self._RTImageFrameMVRadiationAcquisitionSequence.append(item)
        if "RTImageFrameMVRadiationAcquisitionSequence" not in self._dataset:
            self._dataset.RTImageFrameMVRadiationAcquisitionSequence = pydicom.Sequence()
        self._dataset.RTImageFrameMVRadiationAcquisitionSequence.append(item.to_dataset())
