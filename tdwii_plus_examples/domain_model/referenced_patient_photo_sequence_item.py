from typing import Any, List, Optional

import pydicom

from .dicom_media_retrieval_sequence_item import DICOMMediaRetrievalSequenceItem
from .dicom_retrieval_sequence_item import DICOMRetrievalSequenceItem
from .referenced_sop_sequence_item import ReferencedSOPSequenceItem
from .wado_retrieval_sequence_item import WADORetrievalSequenceItem
from .wadors_retrieval_sequence_item import WADORSRetrievalSequenceItem
from .xds_retrieval_sequence_item import XDSRetrievalSequenceItem


class ReferencedPatientPhotoSequenceItem:
    def __init__(self, dataset: Optional[pydicom.Dataset] = None):
        self._dataset = dataset if dataset is not None else pydicom.Dataset()
        self._ReferencedSOPSequence: List[ReferencedSOPSequenceItem] = []
        self._DICOMRetrievalSequence: List[DICOMRetrievalSequenceItem] = []
        self._DICOMMediaRetrievalSequence: List[DICOMMediaRetrievalSequenceItem] = []
        self._WADORetrievalSequence: List[WADORetrievalSequenceItem] = []
        self._XDSRetrievalSequence: List[XDSRetrievalSequenceItem] = []
        self._WADORSRetrievalSequence: List[WADORSRetrievalSequenceItem] = []

    def to_dataset(self) -> pydicom.Dataset:
        return self._dataset

    @property
    def ReferencedSOPSequence(self) -> Optional[List[ReferencedSOPSequenceItem]]:
        if "ReferencedSOPSequence" in self._dataset:
            if len(self._ReferencedSOPSequence) == len(self._dataset.ReferencedSOPSequence):
                return self._ReferencedSOPSequence
            else:
                return [ReferencedSOPSequenceItem(x) for x in self._dataset.ReferencedSOPSequence]
        return None

    @ReferencedSOPSequence.setter
    def ReferencedSOPSequence(self, value: Optional[List[ReferencedSOPSequenceItem]]):
        if value is None:
            self._ReferencedSOPSequence = []
            if "ReferencedSOPSequence" in self._dataset:
                del self._dataset.ReferencedSOPSequence
        elif not isinstance(value, list) or not all(isinstance(item, ReferencedSOPSequenceItem) for item in value):
            raise ValueError(f"ReferencedSOPSequence must be a list of ReferencedSOPSequenceItem objects")
        else:
            self._ReferencedSOPSequence = value
            if "ReferencedSOPSequence" not in self._dataset:
                self._dataset.ReferencedSOPSequence = pydicom.Sequence()
            self._dataset.ReferencedSOPSequence.clear()
            self._dataset.ReferencedSOPSequence.extend([item.to_dataset() for item in value])

    def add_ReferencedSOP(self, item: ReferencedSOPSequenceItem):
        if not isinstance(item, ReferencedSOPSequenceItem):
            raise ValueError(f"Item must be an instance of ReferencedSOPSequenceItem")
        self._ReferencedSOPSequence.append(item)
        if "ReferencedSOPSequence" not in self._dataset:
            self._dataset.ReferencedSOPSequence = pydicom.Sequence()
        self._dataset.ReferencedSOPSequence.append(item.to_dataset())

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
    def SeriesInstanceUID(self) -> Optional[str]:
        if "SeriesInstanceUID" in self._dataset:
            return self._dataset.SeriesInstanceUID
        return None

    @SeriesInstanceUID.setter
    def SeriesInstanceUID(self, value: Optional[str]):
        if value is None:
            if "SeriesInstanceUID" in self._dataset:
                del self._dataset.SeriesInstanceUID
        else:
            self._dataset.SeriesInstanceUID = value

    @property
    def TypeOfInstances(self) -> Optional[str]:
        if "TypeOfInstances" in self._dataset:
            return self._dataset.TypeOfInstances
        return None

    @TypeOfInstances.setter
    def TypeOfInstances(self, value: Optional[str]):
        if value is None:
            if "TypeOfInstances" in self._dataset:
                del self._dataset.TypeOfInstances
        else:
            self._dataset.TypeOfInstances = value

    @property
    def DICOMRetrievalSequence(self) -> Optional[List[DICOMRetrievalSequenceItem]]:
        if "DICOMRetrievalSequence" in self._dataset:
            if len(self._DICOMRetrievalSequence) == len(self._dataset.DICOMRetrievalSequence):
                return self._DICOMRetrievalSequence
            else:
                return [DICOMRetrievalSequenceItem(x) for x in self._dataset.DICOMRetrievalSequence]
        return None

    @DICOMRetrievalSequence.setter
    def DICOMRetrievalSequence(self, value: Optional[List[DICOMRetrievalSequenceItem]]):
        if value is None:
            self._DICOMRetrievalSequence = []
            if "DICOMRetrievalSequence" in self._dataset:
                del self._dataset.DICOMRetrievalSequence
        elif not isinstance(value, list) or not all(isinstance(item, DICOMRetrievalSequenceItem) for item in value):
            raise ValueError(f"DICOMRetrievalSequence must be a list of DICOMRetrievalSequenceItem objects")
        else:
            self._DICOMRetrievalSequence = value
            if "DICOMRetrievalSequence" not in self._dataset:
                self._dataset.DICOMRetrievalSequence = pydicom.Sequence()
            self._dataset.DICOMRetrievalSequence.clear()
            self._dataset.DICOMRetrievalSequence.extend([item.to_dataset() for item in value])

    def add_DICOMRetrieval(self, item: DICOMRetrievalSequenceItem):
        if not isinstance(item, DICOMRetrievalSequenceItem):
            raise ValueError(f"Item must be an instance of DICOMRetrievalSequenceItem")
        self._DICOMRetrievalSequence.append(item)
        if "DICOMRetrievalSequence" not in self._dataset:
            self._dataset.DICOMRetrievalSequence = pydicom.Sequence()
        self._dataset.DICOMRetrievalSequence.append(item.to_dataset())

    @property
    def DICOMMediaRetrievalSequence(self) -> Optional[List[DICOMMediaRetrievalSequenceItem]]:
        if "DICOMMediaRetrievalSequence" in self._dataset:
            if len(self._DICOMMediaRetrievalSequence) == len(self._dataset.DICOMMediaRetrievalSequence):
                return self._DICOMMediaRetrievalSequence
            else:
                return [DICOMMediaRetrievalSequenceItem(x) for x in self._dataset.DICOMMediaRetrievalSequence]
        return None

    @DICOMMediaRetrievalSequence.setter
    def DICOMMediaRetrievalSequence(self, value: Optional[List[DICOMMediaRetrievalSequenceItem]]):
        if value is None:
            self._DICOMMediaRetrievalSequence = []
            if "DICOMMediaRetrievalSequence" in self._dataset:
                del self._dataset.DICOMMediaRetrievalSequence
        elif not isinstance(value, list) or not all(isinstance(item, DICOMMediaRetrievalSequenceItem) for item in value):
            raise ValueError(f"DICOMMediaRetrievalSequence must be a list of DICOMMediaRetrievalSequenceItem objects")
        else:
            self._DICOMMediaRetrievalSequence = value
            if "DICOMMediaRetrievalSequence" not in self._dataset:
                self._dataset.DICOMMediaRetrievalSequence = pydicom.Sequence()
            self._dataset.DICOMMediaRetrievalSequence.clear()
            self._dataset.DICOMMediaRetrievalSequence.extend([item.to_dataset() for item in value])

    def add_DICOMMediaRetrieval(self, item: DICOMMediaRetrievalSequenceItem):
        if not isinstance(item, DICOMMediaRetrievalSequenceItem):
            raise ValueError(f"Item must be an instance of DICOMMediaRetrievalSequenceItem")
        self._DICOMMediaRetrievalSequence.append(item)
        if "DICOMMediaRetrievalSequence" not in self._dataset:
            self._dataset.DICOMMediaRetrievalSequence = pydicom.Sequence()
        self._dataset.DICOMMediaRetrievalSequence.append(item.to_dataset())

    @property
    def WADORetrievalSequence(self) -> Optional[List[WADORetrievalSequenceItem]]:
        if "WADORetrievalSequence" in self._dataset:
            if len(self._WADORetrievalSequence) == len(self._dataset.WADORetrievalSequence):
                return self._WADORetrievalSequence
            else:
                return [WADORetrievalSequenceItem(x) for x in self._dataset.WADORetrievalSequence]
        return None

    @WADORetrievalSequence.setter
    def WADORetrievalSequence(self, value: Optional[List[WADORetrievalSequenceItem]]):
        if value is None:
            self._WADORetrievalSequence = []
            if "WADORetrievalSequence" in self._dataset:
                del self._dataset.WADORetrievalSequence
        elif not isinstance(value, list) or not all(isinstance(item, WADORetrievalSequenceItem) for item in value):
            raise ValueError(f"WADORetrievalSequence must be a list of WADORetrievalSequenceItem objects")
        else:
            self._WADORetrievalSequence = value
            if "WADORetrievalSequence" not in self._dataset:
                self._dataset.WADORetrievalSequence = pydicom.Sequence()
            self._dataset.WADORetrievalSequence.clear()
            self._dataset.WADORetrievalSequence.extend([item.to_dataset() for item in value])

    def add_WADORetrieval(self, item: WADORetrievalSequenceItem):
        if not isinstance(item, WADORetrievalSequenceItem):
            raise ValueError(f"Item must be an instance of WADORetrievalSequenceItem")
        self._WADORetrievalSequence.append(item)
        if "WADORetrievalSequence" not in self._dataset:
            self._dataset.WADORetrievalSequence = pydicom.Sequence()
        self._dataset.WADORetrievalSequence.append(item.to_dataset())

    @property
    def XDSRetrievalSequence(self) -> Optional[List[XDSRetrievalSequenceItem]]:
        if "XDSRetrievalSequence" in self._dataset:
            if len(self._XDSRetrievalSequence) == len(self._dataset.XDSRetrievalSequence):
                return self._XDSRetrievalSequence
            else:
                return [XDSRetrievalSequenceItem(x) for x in self._dataset.XDSRetrievalSequence]
        return None

    @XDSRetrievalSequence.setter
    def XDSRetrievalSequence(self, value: Optional[List[XDSRetrievalSequenceItem]]):
        if value is None:
            self._XDSRetrievalSequence = []
            if "XDSRetrievalSequence" in self._dataset:
                del self._dataset.XDSRetrievalSequence
        elif not isinstance(value, list) or not all(isinstance(item, XDSRetrievalSequenceItem) for item in value):
            raise ValueError(f"XDSRetrievalSequence must be a list of XDSRetrievalSequenceItem objects")
        else:
            self._XDSRetrievalSequence = value
            if "XDSRetrievalSequence" not in self._dataset:
                self._dataset.XDSRetrievalSequence = pydicom.Sequence()
            self._dataset.XDSRetrievalSequence.clear()
            self._dataset.XDSRetrievalSequence.extend([item.to_dataset() for item in value])

    def add_XDSRetrieval(self, item: XDSRetrievalSequenceItem):
        if not isinstance(item, XDSRetrievalSequenceItem):
            raise ValueError(f"Item must be an instance of XDSRetrievalSequenceItem")
        self._XDSRetrievalSequence.append(item)
        if "XDSRetrievalSequence" not in self._dataset:
            self._dataset.XDSRetrievalSequence = pydicom.Sequence()
        self._dataset.XDSRetrievalSequence.append(item.to_dataset())

    @property
    def WADORSRetrievalSequence(self) -> Optional[List[WADORSRetrievalSequenceItem]]:
        if "WADORSRetrievalSequence" in self._dataset:
            if len(self._WADORSRetrievalSequence) == len(self._dataset.WADORSRetrievalSequence):
                return self._WADORSRetrievalSequence
            else:
                return [WADORSRetrievalSequenceItem(x) for x in self._dataset.WADORSRetrievalSequence]
        return None

    @WADORSRetrievalSequence.setter
    def WADORSRetrievalSequence(self, value: Optional[List[WADORSRetrievalSequenceItem]]):
        if value is None:
            self._WADORSRetrievalSequence = []
            if "WADORSRetrievalSequence" in self._dataset:
                del self._dataset.WADORSRetrievalSequence
        elif not isinstance(value, list) or not all(isinstance(item, WADORSRetrievalSequenceItem) for item in value):
            raise ValueError(f"WADORSRetrievalSequence must be a list of WADORSRetrievalSequenceItem objects")
        else:
            self._WADORSRetrievalSequence = value
            if "WADORSRetrievalSequence" not in self._dataset:
                self._dataset.WADORSRetrievalSequence = pydicom.Sequence()
            self._dataset.WADORSRetrievalSequence.clear()
            self._dataset.WADORSRetrievalSequence.extend([item.to_dataset() for item in value])

    def add_WADORSRetrieval(self, item: WADORSRetrievalSequenceItem):
        if not isinstance(item, WADORSRetrievalSequenceItem):
            raise ValueError(f"Item must be an instance of WADORSRetrievalSequenceItem")
        self._WADORSRetrievalSequence.append(item)
        if "WADORSRetrievalSequence" not in self._dataset:
            self._dataset.WADORSRetrievalSequence = pydicom.Sequence()
        self._dataset.WADORSRetrievalSequence.append(item.to_dataset())
