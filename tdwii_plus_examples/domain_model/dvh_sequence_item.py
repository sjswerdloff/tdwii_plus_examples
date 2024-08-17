from decimal import Decimal
from typing import Any, List, Optional

import pydicom

from .dvh_referenced_roi_sequence_item import DVHReferencedROISequenceItem


class DVHSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._DVHReferencedROISequence: List[DVHReferencedROISequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def DVHType(self) -> Optional[str]:
        if "DVHType" in self._dataset:
            return self._dataset.DVHType
        return None

    @DVHType.setter
    def DVHType(self, value: Optional[str]):
        if value is None:
            if "DVHType" in self._dataset:
                del self._dataset.DVHType
        else:
            self._dataset.DVHType = value

    @property
    def DoseUnits(self) -> Optional[str]:
        if "DoseUnits" in self._dataset:
            return self._dataset.DoseUnits
        return None

    @DoseUnits.setter
    def DoseUnits(self, value: Optional[str]):
        if value is None:
            if "DoseUnits" in self._dataset:
                del self._dataset.DoseUnits
        else:
            self._dataset.DoseUnits = value

    @property
    def DoseType(self) -> Optional[str]:
        if "DoseType" in self._dataset:
            return self._dataset.DoseType
        return None

    @DoseType.setter
    def DoseType(self, value: Optional[str]):
        if value is None:
            if "DoseType" in self._dataset:
                del self._dataset.DoseType
        else:
            self._dataset.DoseType = value

    @property
    def DVHDoseScaling(self) -> Optional[Decimal]:
        if "DVHDoseScaling" in self._dataset:
            return self._dataset.DVHDoseScaling
        return None

    @DVHDoseScaling.setter
    def DVHDoseScaling(self, value: Optional[Decimal]):
        if value is None:
            if "DVHDoseScaling" in self._dataset:
                del self._dataset.DVHDoseScaling
        else:
            self._dataset.DVHDoseScaling = value

    @property
    def DVHVolumeUnits(self) -> Optional[str]:
        if "DVHVolumeUnits" in self._dataset:
            return self._dataset.DVHVolumeUnits
        return None

    @DVHVolumeUnits.setter
    def DVHVolumeUnits(self, value: Optional[str]):
        if value is None:
            if "DVHVolumeUnits" in self._dataset:
                del self._dataset.DVHVolumeUnits
        else:
            self._dataset.DVHVolumeUnits = value

    @property
    def DVHNumberOfBins(self) -> Optional[int]:
        if "DVHNumberOfBins" in self._dataset:
            return self._dataset.DVHNumberOfBins
        return None

    @DVHNumberOfBins.setter
    def DVHNumberOfBins(self, value: Optional[int]):
        if value is None:
            if "DVHNumberOfBins" in self._dataset:
                del self._dataset.DVHNumberOfBins
        else:
            self._dataset.DVHNumberOfBins = value

    @property
    def DVHData(self) -> Optional[List[Decimal]]:
        if "DVHData" in self._dataset:
            return self._dataset.DVHData
        return None

    @DVHData.setter
    def DVHData(self, value: Optional[List[Decimal]]):
        if value is None:
            if "DVHData" in self._dataset:
                del self._dataset.DVHData
        else:
            self._dataset.DVHData = value

    @property
    def DVHReferencedROISequence(self) -> Optional[List[DVHReferencedROISequenceItem]]:
        if "DVHReferencedROISequence" in self._dataset:
            if len(self._DVHReferencedROISequence) == len(self._dataset.DVHReferencedROISequence):
                return self._DVHReferencedROISequence
            else:
                return [DVHReferencedROISequenceItem(x) for x in self._dataset.DVHReferencedROISequence]
        return None

    @DVHReferencedROISequence.setter
    def DVHReferencedROISequence(self, value: Optional[List[DVHReferencedROISequenceItem]]):
        if value is None:
            self._DVHReferencedROISequence = []
            if "DVHReferencedROISequence" in self._dataset:
                del self._dataset.DVHReferencedROISequence
        elif not isinstance(value, list) or not all(isinstance(item, DVHReferencedROISequenceItem) for item in value):
            raise ValueError(f"DVHReferencedROISequence must be a list of DVHReferencedROISequenceItem objects")
        else:
            self._DVHReferencedROISequence = value
            if "DVHReferencedROISequence" not in self._dataset:
                self._dataset.DVHReferencedROISequence = pydicom.Sequence()
            self._dataset.DVHReferencedROISequence.clear()
            self._dataset.DVHReferencedROISequence.extend([item.to_dataset() for item in value])

    def add_DVHReferencedROI(self, item: DVHReferencedROISequenceItem):
        if not isinstance(item, DVHReferencedROISequenceItem):
            raise ValueError(f"Item must be an instance of DVHReferencedROISequenceItem")
        self._DVHReferencedROISequence.append(item)
        if "DVHReferencedROISequence" not in self._dataset:
            self._dataset.DVHReferencedROISequence = pydicom.Sequence()
        self._dataset.DVHReferencedROISequence.append(item.to_dataset())

    @property
    def DVHMinimumDose(self) -> Optional[Decimal]:
        if "DVHMinimumDose" in self._dataset:
            return self._dataset.DVHMinimumDose
        return None

    @DVHMinimumDose.setter
    def DVHMinimumDose(self, value: Optional[Decimal]):
        if value is None:
            if "DVHMinimumDose" in self._dataset:
                del self._dataset.DVHMinimumDose
        else:
            self._dataset.DVHMinimumDose = value

    @property
    def DVHMaximumDose(self) -> Optional[Decimal]:
        if "DVHMaximumDose" in self._dataset:
            return self._dataset.DVHMaximumDose
        return None

    @DVHMaximumDose.setter
    def DVHMaximumDose(self, value: Optional[Decimal]):
        if value is None:
            if "DVHMaximumDose" in self._dataset:
                del self._dataset.DVHMaximumDose
        else:
            self._dataset.DVHMaximumDose = value

    @property
    def DVHMeanDose(self) -> Optional[Decimal]:
        if "DVHMeanDose" in self._dataset:
            return self._dataset.DVHMeanDose
        return None

    @DVHMeanDose.setter
    def DVHMeanDose(self, value: Optional[Decimal]):
        if value is None:
            if "DVHMeanDose" in self._dataset:
                del self._dataset.DVHMeanDose
        else:
            self._dataset.DVHMeanDose = value
