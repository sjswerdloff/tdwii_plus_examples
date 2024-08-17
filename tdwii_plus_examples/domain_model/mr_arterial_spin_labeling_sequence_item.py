from typing import Any, List, Optional  # noqa

import pydicom

from .asl_bolus_cutoff_timing_sequence_item import ASLBolusCutoffTimingSequenceItem
from .asl_slab_sequence_item import ASLSlabSequenceItem


class MRArterialSpinLabelingSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._ASLBolusCutoffTimingSequence: List[ASLBolusCutoffTimingSequenceItem] = []
        self._ASLSlabSequence: List[ASLSlabSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ASLTechniqueDescription(self) -> Optional[str]:
        if "ASLTechniqueDescription" in self._dataset:
            return self._dataset.ASLTechniqueDescription
        return None

    @ASLTechniqueDescription.setter
    def ASLTechniqueDescription(self, value: Optional[str]):
        if value is None:
            if "ASLTechniqueDescription" in self._dataset:
                del self._dataset.ASLTechniqueDescription
        else:
            self._dataset.ASLTechniqueDescription = value

    @property
    def ASLContext(self) -> Optional[str]:
        if "ASLContext" in self._dataset:
            return self._dataset.ASLContext
        return None

    @ASLContext.setter
    def ASLContext(self, value: Optional[str]):
        if value is None:
            if "ASLContext" in self._dataset:
                del self._dataset.ASLContext
        else:
            self._dataset.ASLContext = value

    @property
    def ASLCrusherFlag(self) -> Optional[str]:
        if "ASLCrusherFlag" in self._dataset:
            return self._dataset.ASLCrusherFlag
        return None

    @ASLCrusherFlag.setter
    def ASLCrusherFlag(self, value: Optional[str]):
        if value is None:
            if "ASLCrusherFlag" in self._dataset:
                del self._dataset.ASLCrusherFlag
        else:
            self._dataset.ASLCrusherFlag = value

    @property
    def ASLCrusherFlowLimit(self) -> Optional[float]:
        if "ASLCrusherFlowLimit" in self._dataset:
            return self._dataset.ASLCrusherFlowLimit
        return None

    @ASLCrusherFlowLimit.setter
    def ASLCrusherFlowLimit(self, value: Optional[float]):
        if value is None:
            if "ASLCrusherFlowLimit" in self._dataset:
                del self._dataset.ASLCrusherFlowLimit
        else:
            self._dataset.ASLCrusherFlowLimit = value

    @property
    def ASLCrusherDescription(self) -> Optional[str]:
        if "ASLCrusherDescription" in self._dataset:
            return self._dataset.ASLCrusherDescription
        return None

    @ASLCrusherDescription.setter
    def ASLCrusherDescription(self, value: Optional[str]):
        if value is None:
            if "ASLCrusherDescription" in self._dataset:
                del self._dataset.ASLCrusherDescription
        else:
            self._dataset.ASLCrusherDescription = value

    @property
    def ASLBolusCutoffFlag(self) -> Optional[str]:
        if "ASLBolusCutoffFlag" in self._dataset:
            return self._dataset.ASLBolusCutoffFlag
        return None

    @ASLBolusCutoffFlag.setter
    def ASLBolusCutoffFlag(self, value: Optional[str]):
        if value is None:
            if "ASLBolusCutoffFlag" in self._dataset:
                del self._dataset.ASLBolusCutoffFlag
        else:
            self._dataset.ASLBolusCutoffFlag = value

    @property
    def ASLBolusCutoffTimingSequence(self) -> Optional[List[ASLBolusCutoffTimingSequenceItem]]:
        if "ASLBolusCutoffTimingSequence" in self._dataset:
            if len(self._ASLBolusCutoffTimingSequence) == len(self._dataset.ASLBolusCutoffTimingSequence):
                return self._ASLBolusCutoffTimingSequence
            else:
                return [ASLBolusCutoffTimingSequenceItem(x) for x in self._dataset.ASLBolusCutoffTimingSequence]
        return None

    @ASLBolusCutoffTimingSequence.setter
    def ASLBolusCutoffTimingSequence(self, value: Optional[List[ASLBolusCutoffTimingSequenceItem]]):
        if value is None:
            self._ASLBolusCutoffTimingSequence = []
            if "ASLBolusCutoffTimingSequence" in self._dataset:
                del self._dataset.ASLBolusCutoffTimingSequence
        elif not isinstance(value, list) or not all(isinstance(item, ASLBolusCutoffTimingSequenceItem) for item in value):
            raise ValueError("ASLBolusCutoffTimingSequence must be a list of ASLBolusCutoffTimingSequenceItem objects")
        else:
            self._ASLBolusCutoffTimingSequence = value
            if "ASLBolusCutoffTimingSequence" not in self._dataset:
                self._dataset.ASLBolusCutoffTimingSequence = pydicom.Sequence()
            self._dataset.ASLBolusCutoffTimingSequence.clear()
            self._dataset.ASLBolusCutoffTimingSequence.extend([item.to_dataset() for item in value])

    def add_ASLBolusCutoffTiming(self, item: ASLBolusCutoffTimingSequenceItem):
        if not isinstance(item, ASLBolusCutoffTimingSequenceItem):
            raise ValueError("Item must be an instance of ASLBolusCutoffTimingSequenceItem")
        self._ASLBolusCutoffTimingSequence.append(item)
        if "ASLBolusCutoffTimingSequence" not in self._dataset:
            self._dataset.ASLBolusCutoffTimingSequence = pydicom.Sequence()
        self._dataset.ASLBolusCutoffTimingSequence.append(item.to_dataset())

    @property
    def ASLSlabSequence(self) -> Optional[List[ASLSlabSequenceItem]]:
        if "ASLSlabSequence" in self._dataset:
            if len(self._ASLSlabSequence) == len(self._dataset.ASLSlabSequence):
                return self._ASLSlabSequence
            else:
                return [ASLSlabSequenceItem(x) for x in self._dataset.ASLSlabSequence]
        return None

    @ASLSlabSequence.setter
    def ASLSlabSequence(self, value: Optional[List[ASLSlabSequenceItem]]):
        if value is None:
            self._ASLSlabSequence = []
            if "ASLSlabSequence" in self._dataset:
                del self._dataset.ASLSlabSequence
        elif not isinstance(value, list) or not all(isinstance(item, ASLSlabSequenceItem) for item in value):
            raise ValueError("ASLSlabSequence must be a list of ASLSlabSequenceItem objects")
        else:
            self._ASLSlabSequence = value
            if "ASLSlabSequence" not in self._dataset:
                self._dataset.ASLSlabSequence = pydicom.Sequence()
            self._dataset.ASLSlabSequence.clear()
            self._dataset.ASLSlabSequence.extend([item.to_dataset() for item in value])

    def add_ASLSlab(self, item: ASLSlabSequenceItem):
        if not isinstance(item, ASLSlabSequenceItem):
            raise ValueError("Item must be an instance of ASLSlabSequenceItem")
        self._ASLSlabSequence.append(item)
        if "ASLSlabSequence" not in self._dataset:
            self._dataset.ASLSlabSequence = pydicom.Sequence()
        self._dataset.ASLSlabSequence.append(item.to_dataset())
