from typing import Any, List, Optional

import pydicom

from .code_sequence_item import CodeSequenceItem
from .prescription_overview_sequence_item import PrescriptionOverviewSequenceItem
from .referenced_image_sequence_item import ReferencedImageSequenceItem
from .referenced_structure_set_sequence_item import ReferencedStructureSetSequenceItem


class PlanOverviewSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._ReferencedImageSequence: List[ReferencedImageSequenceItem] = []
        self._ReferencedStructureSetSequence: List[ReferencedStructureSetSequenceItem] = []
        self._PrescriptionOverviewSequence: List[PrescriptionOverviewSequenceItem] = []
        self._TreatmentSiteCodeSequence: List[CodeSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ReferencedImageSequence(self) -> Optional[List[ReferencedImageSequenceItem]]:
        if "ReferencedImageSequence" in self._dataset:
            if len(self._ReferencedImageSequence) == len(self._dataset.ReferencedImageSequence):
                return self._ReferencedImageSequence
            else:
                return [ReferencedImageSequenceItem(x) for x in self._dataset.ReferencedImageSequence]
        return None

    @ReferencedImageSequence.setter
    def ReferencedImageSequence(self, value: Optional[List[ReferencedImageSequenceItem]]):
        if value is None:
            self._ReferencedImageSequence = []
            if "ReferencedImageSequence" in self._dataset:
                del self._dataset.ReferencedImageSequence
        elif not isinstance(value, list) or not all(isinstance(item, ReferencedImageSequenceItem) for item in value):
            raise ValueError(f"ReferencedImageSequence must be a list of ReferencedImageSequenceItem objects")
        else:
            self._ReferencedImageSequence = value
            if "ReferencedImageSequence" not in self._dataset:
                self._dataset.ReferencedImageSequence = pydicom.Sequence()
            self._dataset.ReferencedImageSequence.clear()
            self._dataset.ReferencedImageSequence.extend([item.to_dataset() for item in value])

    def add_ReferencedImage(self, item: ReferencedImageSequenceItem):
        if not isinstance(item, ReferencedImageSequenceItem):
            raise ValueError(f"Item must be an instance of ReferencedImageSequenceItem")
        self._ReferencedImageSequence.append(item)
        if "ReferencedImageSequence" not in self._dataset:
            self._dataset.ReferencedImageSequence = pydicom.Sequence()
        self._dataset.ReferencedImageSequence.append(item.to_dataset())

    @property
    def CurrentFractionNumber(self) -> Optional[int]:
        if "CurrentFractionNumber" in self._dataset:
            return self._dataset.CurrentFractionNumber
        return None

    @CurrentFractionNumber.setter
    def CurrentFractionNumber(self, value: Optional[int]):
        if value is None:
            if "CurrentFractionNumber" in self._dataset:
                del self._dataset.CurrentFractionNumber
        else:
            self._dataset.CurrentFractionNumber = value

    @property
    def RTPlanLabel(self) -> Optional[str]:
        if "RTPlanLabel" in self._dataset:
            return self._dataset.RTPlanLabel
        return None

    @RTPlanLabel.setter
    def RTPlanLabel(self, value: Optional[str]):
        if value is None:
            if "RTPlanLabel" in self._dataset:
                del self._dataset.RTPlanLabel
        else:
            self._dataset.RTPlanLabel = value

    @property
    def ReferencedStructureSetSequence(self) -> Optional[List[ReferencedStructureSetSequenceItem]]:
        if "ReferencedStructureSetSequence" in self._dataset:
            if len(self._ReferencedStructureSetSequence) == len(self._dataset.ReferencedStructureSetSequence):
                return self._ReferencedStructureSetSequence
            else:
                return [ReferencedStructureSetSequenceItem(x) for x in self._dataset.ReferencedStructureSetSequence]
        return None

    @ReferencedStructureSetSequence.setter
    def ReferencedStructureSetSequence(self, value: Optional[List[ReferencedStructureSetSequenceItem]]):
        if value is None:
            self._ReferencedStructureSetSequence = []
            if "ReferencedStructureSetSequence" in self._dataset:
                del self._dataset.ReferencedStructureSetSequence
        elif not isinstance(value, list) or not all(isinstance(item, ReferencedStructureSetSequenceItem) for item in value):
            raise ValueError(f"ReferencedStructureSetSequence must be a list of ReferencedStructureSetSequenceItem objects")
        else:
            self._ReferencedStructureSetSequence = value
            if "ReferencedStructureSetSequence" not in self._dataset:
                self._dataset.ReferencedStructureSetSequence = pydicom.Sequence()
            self._dataset.ReferencedStructureSetSequence.clear()
            self._dataset.ReferencedStructureSetSequence.extend([item.to_dataset() for item in value])

    def add_ReferencedStructureSet(self, item: ReferencedStructureSetSequenceItem):
        if not isinstance(item, ReferencedStructureSetSequenceItem):
            raise ValueError(f"Item must be an instance of ReferencedStructureSetSequenceItem")
        self._ReferencedStructureSetSequence.append(item)
        if "ReferencedStructureSetSequence" not in self._dataset:
            self._dataset.ReferencedStructureSetSequence = pydicom.Sequence()
        self._dataset.ReferencedStructureSetSequence.append(item.to_dataset())

    @property
    def PrescriptionOverviewSequence(self) -> Optional[List[PrescriptionOverviewSequenceItem]]:
        if "PrescriptionOverviewSequence" in self._dataset:
            if len(self._PrescriptionOverviewSequence) == len(self._dataset.PrescriptionOverviewSequence):
                return self._PrescriptionOverviewSequence
            else:
                return [PrescriptionOverviewSequenceItem(x) for x in self._dataset.PrescriptionOverviewSequence]
        return None

    @PrescriptionOverviewSequence.setter
    def PrescriptionOverviewSequence(self, value: Optional[List[PrescriptionOverviewSequenceItem]]):
        if value is None:
            self._PrescriptionOverviewSequence = []
            if "PrescriptionOverviewSequence" in self._dataset:
                del self._dataset.PrescriptionOverviewSequence
        elif not isinstance(value, list) or not all(isinstance(item, PrescriptionOverviewSequenceItem) for item in value):
            raise ValueError(f"PrescriptionOverviewSequence must be a list of PrescriptionOverviewSequenceItem objects")
        else:
            self._PrescriptionOverviewSequence = value
            if "PrescriptionOverviewSequence" not in self._dataset:
                self._dataset.PrescriptionOverviewSequence = pydicom.Sequence()
            self._dataset.PrescriptionOverviewSequence.clear()
            self._dataset.PrescriptionOverviewSequence.extend([item.to_dataset() for item in value])

    def add_PrescriptionOverview(self, item: PrescriptionOverviewSequenceItem):
        if not isinstance(item, PrescriptionOverviewSequenceItem):
            raise ValueError(f"Item must be an instance of PrescriptionOverviewSequenceItem")
        self._PrescriptionOverviewSequence.append(item)
        if "PrescriptionOverviewSequence" not in self._dataset:
            self._dataset.PrescriptionOverviewSequence = pydicom.Sequence()
        self._dataset.PrescriptionOverviewSequence.append(item.to_dataset())

    @property
    def PlanOverviewIndex(self) -> Optional[int]:
        if "PlanOverviewIndex" in self._dataset:
            return self._dataset.PlanOverviewIndex
        return None

    @PlanOverviewIndex.setter
    def PlanOverviewIndex(self, value: Optional[int]):
        if value is None:
            if "PlanOverviewIndex" in self._dataset:
                del self._dataset.PlanOverviewIndex
        else:
            self._dataset.PlanOverviewIndex = value

    @property
    def NumberOfFractionsIncluded(self) -> Optional[int]:
        if "NumberOfFractionsIncluded" in self._dataset:
            return self._dataset.NumberOfFractionsIncluded
        return None

    @NumberOfFractionsIncluded.setter
    def NumberOfFractionsIncluded(self, value: Optional[int]):
        if value is None:
            if "NumberOfFractionsIncluded" in self._dataset:
                del self._dataset.NumberOfFractionsIncluded
        else:
            self._dataset.NumberOfFractionsIncluded = value

    @property
    def TreatmentSite(self) -> Optional[str]:
        if "TreatmentSite" in self._dataset:
            return self._dataset.TreatmentSite
        return None

    @TreatmentSite.setter
    def TreatmentSite(self, value: Optional[str]):
        if value is None:
            if "TreatmentSite" in self._dataset:
                del self._dataset.TreatmentSite
        else:
            self._dataset.TreatmentSite = value

    @property
    def TreatmentSiteCodeSequence(self) -> Optional[List[CodeSequenceItem]]:
        if "TreatmentSiteCodeSequence" in self._dataset:
            if len(self._TreatmentSiteCodeSequence) == len(self._dataset.TreatmentSiteCodeSequence):
                return self._TreatmentSiteCodeSequence
            else:
                return [CodeSequenceItem(x) for x in self._dataset.TreatmentSiteCodeSequence]
        return None

    @TreatmentSiteCodeSequence.setter
    def TreatmentSiteCodeSequence(self, value: Optional[List[CodeSequenceItem]]):
        if value is None:
            self._TreatmentSiteCodeSequence = []
            if "TreatmentSiteCodeSequence" in self._dataset:
                del self._dataset.TreatmentSiteCodeSequence
        elif not isinstance(value, list) or not all(isinstance(item, CodeSequenceItem) for item in value):
            raise ValueError(f"TreatmentSiteCodeSequence must be a list of CodeSequenceItem objects")
        else:
            self._TreatmentSiteCodeSequence = value
            if "TreatmentSiteCodeSequence" not in self._dataset:
                self._dataset.TreatmentSiteCodeSequence = pydicom.Sequence()
            self._dataset.TreatmentSiteCodeSequence.clear()
            self._dataset.TreatmentSiteCodeSequence.extend([item.to_dataset() for item in value])

    def add_TreatmentSiteCode(self, item: CodeSequenceItem):
        if not isinstance(item, CodeSequenceItem):
            raise ValueError(f"Item must be an instance of CodeSequenceItem")
        self._TreatmentSiteCodeSequence.append(item)
        if "TreatmentSiteCodeSequence" not in self._dataset:
            self._dataset.TreatmentSiteCodeSequence = pydicom.Sequence()
        self._dataset.TreatmentSiteCodeSequence.append(item.to_dataset())
